import pytest

pydantic = pytest.importorskip(
    "pydantic",
    reason="pydantic v2 unavailable in this environment (PyPI blocked); "
    "the full Phase 0 gate requires it — see PLAN.md §8",
)

from datetime import date  # noqa: E402
from decimal import Decimal  # noqa: E402

from deal_engine.concepts import PeriodType  # noqa: E402
from deal_engine.models import (  # noqa: E402
    Basis,
    Derivation,
    Event,
    EventType,
    Figure,
    OwnershipAssessment,
    OwnershipClass,
    dimensions_hash,
)

D = date(2024, 3, 31)


def filed_figure(**overrides):
    base = dict(
        id="F001",
        company_id="C1",
        concept="revenue",
        value=Decimal("4200000"),
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


class TestFigureProvenance:
    def test_filed_figure_valid(self):
        fig = filed_figure()
        assert fig.dimensions_hash == dimensions_hash({})

    def test_filed_without_source_raises(self):
        with pytest.raises(pydantic.ValidationError, match="no traceable source"):
            filed_figure(source_document_id=None)

    def test_filed_without_tag_raises(self):
        with pytest.raises(pydantic.ValidationError, match="no traceable source"):
            filed_figure(source_tag=None)

    def test_derived_requires_inputs(self):
        with pytest.raises(pydantic.ValidationError, match="derivation"):
            filed_figure(
                concept="ebitda",
                basis=Basis.DERIVED,
                source_document_id=None,
                source_tag=None,
            )

    def test_derived_valid_and_source_forbidden(self):
        fig = filed_figure(
            concept="ebitda",
            basis=Basis.DERIVED,
            source_document_id=None,
            source_tag=None,
            derivation=Derivation(function="ebitda", inputs=["F001", "F002"]),
        )
        assert fig.derivation.function == "ebitda"
        with pytest.raises(pydantic.ValidationError, match="transitive"):
            filed_figure(
                concept="ebitda",
                basis=Basis.DERIVED,
                derivation=Derivation(function="ebitda", inputs=["F001"]),
            )

    def test_modelled_requires_run(self):
        with pytest.raises(pydantic.ValidationError, match="model_run_id"):
            filed_figure(basis=Basis.MODELLED, source_document_id=None, source_tag=None)

    def test_unverified_requires_aggregator_ref(self):
        with pytest.raises(pydantic.ValidationError, match="aggregator_ref"):
            filed_figure(basis=Basis.UNVERIFIED, source_document_id=None, source_tag=None)

    def test_unknown_concept_rejected(self):
        with pytest.raises(pydantic.ValidationError, match="neither a canonical concept"):
            filed_figure(concept="enterprise_value")


class TestFigurePeriods:
    def test_instant_requires_equal_dates(self):
        with pytest.raises(pydantic.ValidationError, match="period_start == period_end"):
            filed_figure(concept="net_assets", period_type=PeriodType.INSTANT)

    def test_instant_valid_with_equal_dates(self):
        fig = filed_figure(
            concept="net_assets",
            period_type=PeriodType.INSTANT,
            period_start=D,
            period_end=D,
        )
        assert fig.period_start == fig.period_end

    def test_reversed_duration_rejected(self):
        with pytest.raises(pydantic.ValidationError, match="period_start after"):
            filed_figure(period_start=date(2025, 1, 1))


class TestFigureDimensions:
    def test_hash_computed_and_checked(self):
        dims = {"consolidation": "group"}
        fig = filed_figure(dimensions=dims)
        assert fig.dimensions_hash == dimensions_hash(dims)
        with pytest.raises(pydantic.ValidationError, match="does not match"):
            filed_figure(dimensions=dims, dimensions_hash="0" * 16)

    def test_different_dimensions_different_hash(self):
        a = filed_figure(dimensions={"consolidation": "group"})
        b = filed_figure(dimensions={"consolidation": "company"})
        assert a.dimensions_hash != b.dimensions_hash


class TestOwnership:
    def test_classification_requires_evidence(self):
        with pytest.raises(pydantic.ValidationError, match="requires evidence"):
            OwnershipAssessment(classification=OwnershipClass.PE_BACKED, confidence=0.9)

    def test_unclassifiable_stands_without_evidence(self):
        # Fail-closed doctrine: unclassifiable is a legitimate terminal state.
        oa = OwnershipAssessment(
            classification=OwnershipClass.UNCLASSIFIABLE, confidence=0.0
        )
        assert oa.classification is OwnershipClass.UNCLASSIFIABLE


class TestEvent:
    def test_event_requires_source(self):
        with pytest.raises(pydantic.ValidationError, match="projections of sourced"):
            Event(id="E1", company_id="C1", event_type=EventType.NAME_CHANGED, event_date=D)

    def test_event_with_transaction_valid(self):
        ev = Event(
            id="E1",
            company_id="C1",
            event_type=EventType.CHARGE_REGISTERED,
            event_date=D,
            transaction_id="TX1",
        )
        assert ev.event_type is EventType.CHARGE_REGISTERED


class TestModelTableParity:
    """The Pydantic and SQLAlchemy layers must not drift."""

    def test_field_parity(self):
        sqlalchemy = pytest.importorskip("sqlalchemy")  # noqa: F841
        from deal_engine.db import tables
        from deal_engine.models import (
            Company,
            FilingRecord,
            Officer,
            PscRecord,
            RunRecord,
            Score,
            ScreenResult,
            SourceDocument,
        )

        pairs = [
            # (model, table row class, model-only fields, row-only fields)
            (
                Figure,
                tables.FigureRow,
                {"derivation"},
                {"derivation_function", "derivation_inputs"},
            ),
            (SourceDocument, tables.SourceDocumentRow, set(), set()),
            (
                Company,
                tables.CompanyRow,
                {"ownership"},
                {
                    "ownership_classification",
                    "ownership_confidence",
                    "ownership_evidence",
                },
            ),
            (Officer, tables.OfficerRow, set(), set()),
            (PscRecord, tables.PscRecordRow, set(), set()),
            (FilingRecord, tables.FilingRow, set(), set()),
            (Event, tables.EventRow, set(), set()),
            (RunRecord, tables.RunRow, set(), set()),
            (ScreenResult, tables.ScreenResultRow, set(), set()),
            (Score, tables.ScoreRow, set(), set()),
        ]
        for model, row_cls, model_only, row_only in pairs:
            model_fields = set(model.model_fields)
            columns = {c.key for c in row_cls.__table__.columns}
            missing_in_table = model_fields - columns - model_only
            missing_in_model = columns - model_fields - row_only
            assert not missing_in_table, (
                f"{model.__name__}: fields absent from {row_cls.__tablename__}: "
                f"{sorted(missing_in_table)}"
            )
            assert not missing_in_model, (
                f"{row_cls.__tablename__}: columns absent from {model.__name__}: "
                f"{sorted(missing_in_model)}"
            )
