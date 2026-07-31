"""Provenance enforcement at both layers, and the provenance walk.

Layer 1 (Pydantic) is covered in test_models.py. This file covers layer 2
— the database CHECK constraints, for writes that bypass the model — and
the transitive walk with cycle detection (DoD #3).
"""

import pytest

pytest.importorskip(
    "pydantic",
    reason="pydantic v2 unavailable in this environment (PyPI blocked); "
    "the full Phase 0 gate requires it — see PLAN.md §8",
)
pytest.importorskip("sqlalchemy")

from datetime import date, datetime, timezone  # noqa: E402
from decimal import Decimal  # noqa: E402

from sqlalchemy.exc import IntegrityError  # noqa: E402

from deal_engine.concepts import PeriodType  # noqa: E402
from deal_engine.db.repository import (  # noqa: E402
    ProvenanceCycleError,
    ProvenanceError,
    add_figure,
    add_source_document,
    provenance_walk,
    validate_provenance,
)
from deal_engine.db.session import get_engine, init_db, make_session_factory  # noqa: E402
from deal_engine.db.tables import CompanyRow, FigureRow  # noqa: E402
from deal_engine.models import Basis, Derivation, Figure, ParseStatus, SourceDocument  # noqa: E402

D = date(2024, 3, 31)


@pytest.fixture()
def session(tmp_path):
    engine = get_engine(tmp_path / "test.db")
    init_db(engine)
    factory = make_session_factory(engine)
    with factory() as s:
        s.add(CompanyRow(id="C1", jurisdiction="GB", registration_id="00000006", name="Test Ltd"))
        s.add_row = None
        add_source_document(
            s,
            SourceDocument(
                id="DOC1",
                adapter="companies_house",
                jurisdiction="GB",
                company_id="C1",
                external_document_id="ext-1",
                document_type="AA",
                retrieved_at=datetime.now(timezone.utc),
                parse_status=ParseStatus.PARSED,
            ),
        )
        s.commit()
        yield s


def filed(fid, concept="revenue", **overrides):
    base = dict(
        id=fid,
        company_id="C1",
        concept=concept,
        value=Decimal("100"),
        unit="iso4217:GBP",
        currency="GBP",
        period_type=PeriodType.DURATION,
        period_start=date(2023, 4, 1),
        period_end=D,
        basis=Basis.FILED,
        source_document_id="DOC1",
        source_tag="uk-core:TurnoverRevenue",
    )
    base.update(overrides)
    return Figure(**base)


class TestDatabaseChecks:
    def test_raw_insert_filed_without_source_raises(self, session):
        # Bypasses Pydantic entirely: the CHECK constraint must hold alone.
        session.add(
            FigureRow(
                id="BAD1",
                company_id="C1",
                concept="revenue",
                value=1,
                unit="iso4217:GBP",
                period_type="duration",
                period_start=date(2023, 4, 1),
                period_end=D,
                dimensions_hash="x" * 16,
                basis="filed",
                source_document_id=None,
                source_tag=None,
            )
        )
        with pytest.raises(IntegrityError):
            session.commit()
        session.rollback()

    def test_raw_insert_derived_without_inputs_raises(self, session):
        session.add(
            FigureRow(
                id="BAD2",
                company_id="C1",
                concept="ebitda",
                value=1,
                unit="iso4217:GBP",
                period_type="duration",
                period_start=date(2023, 4, 1),
                period_end=D,
                dimensions_hash="x" * 16,
                basis="derived",
                derivation_function=None,
                derivation_inputs=None,
            )
        )
        with pytest.raises(IntegrityError):
            session.commit()
        session.rollback()

    def test_duplicate_observation_raises(self, session):
        add_figure(session, filed("F1"))
        session.commit()
        add_figure(session, filed("F1-dup"))  # same doc/concept/period/dims/unit
        with pytest.raises(IntegrityError):
            session.commit()
        session.rollback()


class TestProvenanceWalk:
    def test_filed_resolves_to_document(self, session):
        add_figure(session, filed("F1"))
        session.commit()
        assert provenance_walk(session, "F1") == {"DOC1"}

    def test_derived_resolves_transitively(self, session):
        add_figure(session, filed("F1", concept="operating_profit", source_tag="t1"))
        add_figure(
            session, filed("F2", concept="depreciation_amortisation", source_tag="t2")
        )
        add_figure(
            session,
            Figure(
                id="F3",
                company_id="C1",
                concept="ebitda",
                value=Decimal("120"),
                unit="iso4217:GBP",
                currency="GBP",
                period_type=PeriodType.DURATION,
                period_start=date(2023, 4, 1),
                period_end=D,
                basis=Basis.DERIVED,
                derivation=Derivation(function="ebitda", inputs=["F1", "F2"]),
            ),
        )
        session.commit()
        assert provenance_walk(session, "F3") == {"DOC1"}

    def test_missing_input_fails_loudly(self, session):
        add_figure(
            session,
            Figure(
                id="F4",
                company_id="C1",
                concept="ebitda",
                value=Decimal("1"),
                unit="iso4217:GBP",
                period_type=PeriodType.DURATION,
                period_start=date(2023, 4, 1),
                period_end=D,
                basis=Basis.DERIVED,
                derivation=Derivation(function="ebitda", inputs=["NOPE"]),
            ),
        )
        session.commit()
        with pytest.raises(ProvenanceError, match="does not exist"):
            provenance_walk(session, "F4")
        assert validate_provenance(session)

    def test_cycle_detected_not_recursed(self, session):
        for fid, other in (("FA", "FB"), ("FB", "FA")):
            add_figure(
                session,
                Figure(
                    id=fid,
                    company_id="C1",
                    concept="ebitda",
                    value=Decimal("1"),
                    unit="iso4217:GBP",
                    period_type=PeriodType.DURATION,
                    period_start=date(2023, 4, 1),
                    period_end=D,
                    basis=Basis.DERIVED,
                    derivation=Derivation(function="ebitda", inputs=[other]),
                ),
            )
        session.commit()
        with pytest.raises(ProvenanceCycleError, match="cycle"):
            provenance_walk(session, "FA")

    def test_validate_provenance_clean_store(self, session):
        add_figure(session, filed("F1"))
        session.commit()
        assert validate_provenance(session) == []
