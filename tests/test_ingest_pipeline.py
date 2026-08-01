"""Ingest pipeline integration: universe → rows, idempotency, coverage.

Runs the full pipeline over a MockTransport registry assembled from the
recorded live fixtures and the golden micro-entity filing, then proves
DoD #4: re-ingesting the same universe inserts zero new rows and flips
zero `is_current` flags. Restatement classification and coverage-fact
causes are pinned at unit level against hand-built observation sets.
"""

import hashlib
import json
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

import pytest

pytest.importorskip("pydantic", reason="pydantic unavailable; pipeline tests run in CI")
httpx = pytest.importorskip("httpx", reason="httpx unavailable; pipeline tests run in CI")
pytest.importorskip("sqlalchemy", reason="sqlalchemy unavailable; pipeline tests run in CI")
pytest.importorskip("ixbrlparse", reason="ixbrlparse unavailable; pipeline tests run in CI")

import yaml  # noqa: E402
from sqlalchemy import func, select  # noqa: E402

from deal_engine.adapters.companies_house.client import (  # noqa: E402
    CompaniesHouseClient,
    RateLimiter,
)
from deal_engine.db.repository import (  # noqa: E402
    add_figure,
    add_source_document,
    validate_provenance,
)
from deal_engine.db.session import get_engine, init_db, make_session_factory  # noqa: E402
from deal_engine.db.tables import (  # noqa: E402
    BeneficialOwnerRow,
    CompanyRow,
    ConceptCoverageRow,
    EventRow,
    FigureRow,
    FilingRow,
    OfficerRow,
    RunRow,
)
from deal_engine.adapters.companies_house.pipeline import (  # noqa: E402
    IngestConfig,
    detect_restatements,
    enumerate_universe,
    refresh_current_flags,
    run_ingest,
    triage,
    write_coverage_facts,
)
from deal_engine.mandate.loader import load_mandate  # noqa: E402
from deal_engine.models.common import Basis, ParseStatus  # noqa: E402
from deal_engine.models.figure import Figure  # noqa: E402
from deal_engine.models.source import SourceDocument  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "companies_house"
GOLDEN = ROOT / "evals" / "golden" / "filings"
DOC_HOST = "https://document-api.company-information.service.gov.uk"

GOLDEN_XHTML = (GOLDEN / "gb-10122954-2022-04-30-micro-entity.xhtml").read_bytes()
GOLDEN_EXPECTED = yaml.safe_load(
    (GOLDEN / "gb-10122954-2022-04-30-micro-entity.expected.yaml").read_text(encoding="utf-8")
)


def fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


SEARCH_MICRO = {
    "company_number": "10122954",
    "company_status": "active",
    "sic_codes": ["47910", "62012"],
}
SEARCH_DORMANT = {
    "company_number": "08140876",
    "company_status": "active",
    "sic_codes": ["62012", "62090", "70229", "74909"],
}
FILING_ITEM = {
    "transaction_id": "TXNMICRO1",
    "type": "AA",
    "date": "2022-11-05",
    "category": "accounts",
    "description": "accounts-with-accounts-type-micro-entity",
    "description_values": {"made_up_date": "2022-04-30"},
    "paper_filed": False,
    "links": {
        "self": "/company/10122954/filing-history/TXNMICRO1",
        "document_metadata": f"{DOC_HOST}/document/docmicro1",
    },
}


def make_handler(state: dict):
    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path == "/advanced-search/companies":
            items = [SEARCH_MICRO, SEARCH_DORMANT]
            size = int(request.url.params.get("size", "100"))
            start = int(request.url.params.get("start_index", "0"))
            return httpx.Response(200, json={"hits": 2, "items": items[start : start + size]})
        if path == "/company/10122954":
            return httpx.Response(200, json=fixture("company-profile-10122954-micro.json"))
        if path == "/company/08140876":
            return httpx.Response(200, json=fixture("company-profile-08140876-dormant.json"))
        if path == "/company/10122954/officers":
            return httpx.Response(200, json=fixture("officers-10122954.json"))
        if path == "/company/10122954/persons-with-significant-control":
            return httpx.Response(200, json=fixture("psc-10122954.json"))
        if path == "/company/10122954/persons-with-significant-control-statements":
            return httpx.Response(404, json={"error": "not-found"})
        if path == "/company/10122954/exemptions":
            return httpx.Response(404, json={"error": "not-found"})
        if path == "/company/10122954/charges":
            return httpx.Response(404, json={"error": "not-found"})
        if path == "/company/10122954/filing-history":
            return httpx.Response(200, json={"items": [FILING_ITEM], "total_count": 1})
        if path == "/document/docmicro1":
            return httpx.Response(
                200, json={"resources": {"application/xhtml+xml": {"content_length": 1}}}
            )
        if path == "/document/docmicro1/content":
            state["content_fetches"] = state.get("content_fetches", 0) + 1
            return httpx.Response(
                200,
                content=GOLDEN_XHTML,
                headers={"Content-Type": "application/xhtml+xml"},
            )
        raise AssertionError(f"unexpected request: {request.url}")

    return handler


def make_client(state: dict) -> CompaniesHouseClient:
    return CompaniesHouseClient(
        api_key="test-key",
        transport=httpx.MockTransport(make_handler(state)),
        rate_limiter=RateLimiter(clock=lambda: 0.0, sleep=lambda s: None),
        backoff=lambda s: None,
    )


@pytest.fixture()
def mandate():
    return load_mandate(ROOT / "mandates" / "example-lmm-gb.yaml")


@pytest.fixture()
def db(tmp_path):
    engine = get_engine(tmp_path / "engine.db")
    init_db(engine)
    return make_session_factory(engine)


def _table_counts(session) -> dict[str, int]:
    return {
        table.__tablename__: session.execute(
            select(func.count()).select_from(table)
        ).scalar_one()
        for table in (CompanyRow, FigureRow, FilingRow, OfficerRow, BeneficialOwnerRow, EventRow)
    }


class TestFullIngest:
    def test_ingest_and_reingest_idempotency(self, tmp_path, mandate, db):
        state: dict = {}
        with make_client(state) as client:
            summary1 = run_ingest(
                client,
                db,
                mandate,
                run_id="run1",
                data_root=tmp_path / "data",
                config=IngestConfig(limit=10),
                incorporated_to=date(2026, 1, 1),
            )

        assert summary1["ingested"] == 1
        assert summary1["skipped"] == {"dormant": 1}
        assert summary1["universe_hits"] == 2
        assert summary1["errors"] == []
        assert state["content_fetches"] == 1

        session = db()
        counts1 = _table_counts(session)
        assert counts1["companies"] == 1
        assert counts1["filings"] == 1
        assert counts1["events"] == 0

        # Every hand-verified golden figure persisted with its exact value.
        for row in GOLDEN_EXPECTED["figures"]:
            got = session.execute(
                select(FigureRow).where(
                    FigureRow.company_id == "gb:10122954",
                    FigureRow.concept == row["concept"],
                    FigureRow.period_end == date.fromisoformat(str(row["period_end"])),
                    FigureRow.dimensions_hash.isnot(None),
                )
            ).scalars().all()
            values = {Decimal(str(f.value)).normalize() for f in got}
            assert Decimal(str(row["value"])).normalize() in values, (
                f"{row['concept']} {row['period_end']}: expected {row['value']}, got {values}"
            )
        present = {
            c
            for (c,) in session.execute(
                select(FigureRow.concept).where(FigureRow.company_id == "gb:10122954")
            )
        }
        for concept in GOLDEN_EXPECTED.get("absent_concepts", []):
            assert concept not in present

        # All persisted figures are current (single document) and walk cleanly.
        assert summary1["counts"].get("current_flag_changes", 0) == 0
        assert validate_provenance(session) == []

        # Coverage: absence carries a cause.
        facts = {
            f.concept: f
            for f in session.execute(
                select(ConceptCoverageRow).where(ConceptCoverageRow.run_id == "run1")
            ).scalars()
        }
        assert facts["net_assets"].status == "available"
        assert facts["revenue"].status == "filed_without_concept"
        assert "micro-entity" in facts["revenue"].detail
        assert all(f.source_document_id for f in facts.values())

        # The document blob is content-addressed and intact.
        doc = session.execute(select(FigureRow.source_document_id)).scalars().first()
        from deal_engine.db.tables import SourceDocumentRow

        doc_row = session.get(SourceDocumentRow, doc)
        assert doc_row.content_hash == hashlib.sha256(GOLDEN_XHTML).hexdigest()
        assert Path(doc_row.raw_path).is_file()
        assert doc_row.account_type == "micro-entity"

        # Standing coverage report, by classification code within mandate.
        report = summary1["coverage"]
        assert report["by_classification_code"]["62012"]["companies"] == 1
        assert "47910" not in report["by_classification_code"]  # outside the mandate
        assert report["screening_modes"] == {"financial": 1, "signal": 0}
        assert Path(summary1["report_path"]).is_file()

        # ---- Re-ingest: zero new rows, zero flag changes (DoD #4). ----
        with make_client(state) as client:
            summary2 = run_ingest(
                client,
                db,
                mandate,
                run_id="run2",
                data_root=tmp_path / "data",
                config=IngestConfig(limit=10),
                incorporated_to=date(2026, 1, 1),
            )

        session2 = db()
        counts2 = _table_counts(session2)
        assert counts2 == counts1
        assert summary2["counts"].get("figures_new", 0) == 0
        assert summary2["counts"].get("companies_new", 0) == 0
        assert summary2["counts"].get("companies_updated", 0) == 0
        assert summary2["counts"].get("current_flag_changes", 0) == 0
        assert summary2["counts"].get("documents_fetched", 0) == 0
        assert summary2["counts"].get("documents_cached", 0) == 1
        assert state["content_fetches"] == 1  # never refetched
        # Coverage facts are per-run observations and must reproduce exactly.
        assert summary2["counts"]["coverage_facts"] == summary1["counts"]["coverage_facts"]

    def test_checkpoint_resumes_without_refetching(self, tmp_path, mandate, db):
        state: dict = {}
        checkpoint = tmp_path / "ckpt.json"
        with make_client(state) as client:
            run_ingest(
                client,
                db,
                mandate,
                run_id="run1",
                data_root=tmp_path / "data",
                config=IngestConfig(limit=10),
                checkpoint_path=checkpoint,
                incorporated_to=date(2026, 1, 1),
            )
        recorded = json.loads(checkpoint.read_text())["processed"]
        assert recorded == {"10122954": "ingested", "08140876": "skipped:dormant"}

        with make_client(state) as client:
            summary = run_ingest(
                client,
                db,
                mandate,
                run_id="run2",
                data_root=tmp_path / "data",
                config=IngestConfig(limit=10),
                checkpoint_path=checkpoint,
                incorporated_to=date(2026, 1, 1),
            )
        assert summary["examined"] == 0
        assert summary["skipped"] == {"checkpointed": 2}


class TestTriage:
    def test_dormant_skipped(self, mandate):
        assert triage(fixture("company-profile-08140876-dormant.json"), mandate) == "dormant"

    def test_active_trading_company_passes(self, mandate):
        assert triage(fixture("company-profile-10122954-micro.json"), mandate) is None

    def test_wrong_status_skipped(self, mandate):
        profile = {"company_status": "dissolved", "sic_codes": ["62012"]}
        assert triage(profile, mandate) == "status_dissolved"

    def test_excluded_classification_skipped(self, mandate):
        profile = {"company_status": "active", "sic_codes": ["62012", "64191"]}
        assert triage(profile, mandate) == "excluded_classification"

    def test_unrelated_classification_skipped(self, mandate):
        profile = {"company_status": "active", "sic_codes": ["10110"]}
        assert triage(profile, mandate) == "no_included_classification"


class TestUniverseSlicing:
    def test_over_window_ranges_bisect_on_incorporation_date(self):
        class SliceStub:
            def advanced_search(
                self,
                sic_codes,
                company_status="active",
                size=100,
                start_index=0,
                incorporated_from=None,
                incorporated_to=None,
            ):
                lo = date.fromisoformat(incorporated_from)
                hi = date.fromisoformat(incorporated_to)
                if (hi - lo).days > 40_000:
                    return {"hits": 20_000, "items": []}
                items = [
                    {"company_number": f"{incorporated_from}:{i}"} for i in range(2)
                ]
                return {"hits": 2, "items": items[start_index : start_index + size]}

        stats: dict = {}
        items = list(
            enumerate_universe(
                SliceStub(),
                ["62012"],
                page_size=500,
                window=10_000,
                incorporated_to=date(2026, 1, 1),
                stats=stats,
            )
        )
        assert len(items) == 4  # two slices x two companies
        assert stats["slices"] == 3  # parent probe + two child slices
        assert len({i["company_number"] for i in items}) == 4


# --------------------------------------------------------------------------
# observation currency + restatements over hand-built documents


def _mk_company(session, cid="gb:11111111"):
    session.add(
        CompanyRow(
            id=cid,
            jurisdiction="GB",
            registration_id=cid.split(":")[1],
            name="TEST LTD",
            name_variants=[],
            classification_codes=["62012"],
            classification_taxonomy="sic_2007",
            registered_address={},
        )
    )
    session.flush()
    return cid


def _mk_doc(session, cid, doc_id, filed, txn):
    doc = SourceDocument(
        id=doc_id,
        adapter="companies_house",
        jurisdiction="GB",
        company_id=cid,
        external_document_id=doc_id.rsplit(":", 1)[-1],
        transaction_id=txn,
        document_type="AA",
        account_type="micro-entity",
        filed_date=filed,
        period_end=date(2022, 4, 30),
        retrieved_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        parse_status=ParseStatus.PARSED,
    )
    row = add_source_document(session, doc)
    session.flush()
    return row


def _mk_figure(session, cid, doc_id, fid, concept, value):
    figure = Figure(
        id=fid,
        company_id=cid,
        concept=concept,
        value=Decimal(value),
        unit="GBP",
        currency="GBP",
        period_type="instant",
        period_start=date(2022, 4, 30),
        period_end=date(2022, 4, 30),
        decimals=0,
        basis=Basis.FILED,
        source_document_id=doc_id,
        source_tag=f"uk-core:{concept}",
    )
    add_figure(session, figure)
    session.flush()


class TestRestatements:
    @pytest.fixture()
    def seeded(self, db):
        session = db()
        cid = _mk_company(session)
        _mk_doc(session, cid, f"{cid}:doc:A", date(2022, 11, 5), "TXA")
        _mk_doc(session, cid, f"{cid}:doc:B", date(2023, 6, 1), "TXB")
        rows = [
            ("net_assets", "7656", "7656"),  # agreement: no restatement
            ("creditors_within_one_year", "500", "300"),  # moved, total stable
            ("cash", "1000", "1001"),  # within filed precision
            ("equity", "5000", "9000"),  # material genuine restatement
        ]
        for concept, a, b in rows:
            _mk_figure(session, cid, f"{cid}:doc:A", f"fa-{concept}", concept, a)
            _mk_figure(session, cid, f"{cid}:doc:B", f"fb-{concept}", concept, b)
        return session, cid

    def test_current_selection_latest_filed_wins(self, seeded):
        session, cid = seeded
        changes = refresh_current_flags(session, cid)
        assert changes == 4  # every doc-A observation superseded
        current = {
            f.concept: f.source_document_id
            for f in session.execute(
                select(FigureRow).where(FigureRow.company_id == cid, FigureRow.is_current)
            ).scalars()
        }
        assert set(current.values()) == {f"{cid}:doc:B"}
        assert refresh_current_flags(session, cid) == 0  # deterministic fixpoint

    def test_restatement_classification_and_materiality(self, seeded):
        session, cid = seeded
        refresh_current_flags(session, cid)
        created = detect_restatements(session, cid, IngestConfig())
        assert created == 1

        event = session.execute(select(EventRow)).scalars().one()
        assert event.event_type == "restatement"
        assert event.event_date == date(2023, 6, 1)
        assert event.transaction_id == "TXB"
        assert event.payload["superseded_document_id"] == f"{cid}:doc:A"

        items = {i["concept"]: i for i in event.payload["restatements"]}
        assert set(items) == {"creditors_within_one_year", "cash", "equity"}
        assert items["cash"]["classification"] == "rounding"
        assert items["cash"]["material"] is False
        assert items["creditors_within_one_year"]["classification"] == "reclassification"
        assert items["creditors_within_one_year"]["material"] is False
        assert items["equity"]["classification"] == "genuine"
        assert items["equity"]["material"] is True

        # Idempotent re-detection.
        assert detect_restatements(session, cid, IngestConfig()) == 0


class TestCoverageFacts:
    def test_not_filed_carries_cause_without_document(self, db):
        session = db()
        cid = _mk_company(session, "gb:22222222")
        session.add(
            RunRow(
                run_id="runX",
                command="ingest",
                args={},
                started_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
            )
        )
        session.flush()
        profile = {
            "company_number": "22222222",
            "accounts": {"last_accounts": {"period_end_on": "2025-07-31"}},
        }
        counts: dict = {}
        note = write_coverage_facts(session, cid, "runX", profile, [], counts)
        assert note is None
        facts = session.execute(select(ConceptCoverageRow)).scalars().all()
        assert facts and all(f.status == "not_filed" for f in facts)
        assert all(f.source_document_id is None for f in facts)
        assert all(f.period_end == date(2025, 7, 31) for f in facts)

    def test_company_with_no_period_is_reported_not_invented(self, db):
        session = db()
        cid = _mk_company(session, "gb:33333333")
        note = write_coverage_facts(
            session, cid, "runX", {"company_number": "33333333"}, [], {}
        )
        assert note == "no_reporting_period"
        assert session.execute(select(ConceptCoverageRow)).scalars().all() == []
