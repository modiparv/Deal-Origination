"""Incremental refresh: the transaction diff is the whole contract.

Phase 1 of the mock registry is the ingest-time world; phase 2 adds an
amended accounts re-filing (new document, same figures), an officer
termination filing, and the updated officers list. The tests pin:

- an unchanged company costs exactly ONE request (filing history) and
  changes nothing, while its coverage facts still reproduce;
- a changed company refetches only the record families its new filing
  categories name, ingests the new document, flips observation currency
  to the later-filed document, and emits no restatement when the
  re-filed figures agree;
- refreshing again after that is a no-op — refresh is idempotent.
"""

import json
from datetime import date
from pathlib import Path

import pytest

pytest.importorskip("pydantic", reason="pydantic unavailable; refresh tests run in CI")
httpx = pytest.importorskip("httpx", reason="httpx unavailable; refresh tests run in CI")
pytest.importorskip("sqlalchemy", reason="sqlalchemy unavailable; refresh tests run in CI")
pytest.importorskip("ixbrlparse", reason="ixbrlparse unavailable; refresh tests run in CI")

from sqlalchemy import func, select  # noqa: E402

from deal_engine.adapters.companies_house.client import (  # noqa: E402
    CompaniesHouseClient,
    RateLimiter,
)
from deal_engine.adapters.companies_house.pipeline import IngestConfig, run_ingest  # noqa: E402
from deal_engine.adapters.companies_house.refresh import run_refresh  # noqa: E402
from deal_engine.db.session import get_engine, init_db, make_session_factory  # noqa: E402
from deal_engine.db.tables import (  # noqa: E402
    ConceptCoverageRow,
    EventRow,
    FigureRow,
    FilingRow,
    OfficerRow,
)
from deal_engine.mandate.loader import load_mandate  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "companies_house"
GOLDEN_XHTML = (
    ROOT / "evals" / "golden" / "filings" / "gb-10122954-2022-04-30-micro-entity.xhtml"
).read_bytes()
DOC_HOST = "https://document-api.company-information.service.gov.uk"


def fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def filing(txn: str, category: str, filed: str, description: str, doc: str | None, **extra):
    item = {
        "transaction_id": txn,
        "category": category,
        "date": filed,
        "description": description,
        "links": {"self": f"/company/10122954/filing-history/{txn}"},
        **extra,
    }
    if doc:
        item["links"]["document_metadata"] = f"{DOC_HOST}/document/{doc}"
    return item


TXN1 = filing(
    "TXN1",
    "accounts",
    "2022-11-05",
    "accounts-with-accounts-type-micro-entity",
    "docmicro1",
    type="AA",
    description_values={"made_up_date": "2022-04-30"},
)
# Amended re-filing of the same period: a new document carrying the same
# figures (registry reality for corrected-but-unchanged accounts).
TXN2 = filing(
    "TXN2",
    "accounts",
    "2023-01-15",
    "accounts-with-accounts-type-micro-entity",
    "docmicro2",
    type="AA",
    description_values={"made_up_date": "2022-04-30"},
)
TXN3 = filing(
    "TXN3", "officers", "2023-02-01", "termination-director-company-with-name", None, type="TM01"
)


def make_handler(state: dict):
    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        state.setdefault("requests", []).append(path)
        if path == "/advanced-search/companies":
            items = [
                {
                    "company_number": "10122954",
                    "company_status": "active",
                    "sic_codes": ["47910", "62012"],
                }
            ]
            size = int(request.url.params.get("size", "100"))
            start = int(request.url.params.get("start_index", "0"))
            return httpx.Response(200, json={"hits": 1, "items": items[start : start + size]})
        if path == "/company/10122954":
            return httpx.Response(200, json=fixture("company-profile-10122954-micro.json"))
        if path == "/company/10122954/officers":
            payload = fixture("officers-10122954.json")
            if state.get("officer_resigned"):
                payload["items"][0]["resigned_on"] = "2023-02-01"
            return httpx.Response(200, json=payload)
        if path == "/company/10122954/persons-with-significant-control":
            return httpx.Response(200, json=fixture("psc-10122954.json"))
        if path in (
            "/company/10122954/persons-with-significant-control-statements",
            "/company/10122954/exemptions",
            "/company/10122954/charges",
        ):
            return httpx.Response(404, json={"error": "not-found"})
        if path == "/company/10122954/filing-history":
            items = state.get("filing_items") or [TXN1]
            return httpx.Response(200, json={"items": items, "total_count": len(items)})
        if path in ("/document/docmicro1", "/document/docmicro2"):
            return httpx.Response(
                200, json={"resources": {"application/xhtml+xml": {"content_length": 1}}}
            )
        if path in ("/document/docmicro1/content", "/document/docmicro2/content"):
            state["content_fetches"] = state.get("content_fetches", 0) + 1
            return httpx.Response(
                200, content=GOLDEN_XHTML, headers={"Content-Type": "application/xhtml+xml"}
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
def world(tmp_path):
    """Ingested baseline store + the shared mutable registry state."""
    state: dict = {}
    engine = get_engine(tmp_path / "engine.db")
    init_db(engine)
    factory = make_session_factory(engine)
    mandate = load_mandate(ROOT / "mandates" / "example-lmm-gb.yaml")
    with make_client(state) as client:
        run_ingest(
            client,
            factory,
            mandate,
            run_id="ingest1",
            data_root=tmp_path / "data",
            config=IngestConfig(limit=10),
            incorporated_to=date(2026, 1, 1),
        )
    return state, factory, mandate, tmp_path


def _counts(session) -> dict[str, int]:
    return {
        t.__tablename__: session.execute(select(func.count()).select_from(t)).scalar_one()
        for t in (FigureRow, FilingRow, OfficerRow, EventRow)
    }


class TestUnchangedCompany:
    def test_one_request_zero_changes_full_coverage(self, world):
        state, factory, mandate, tmp_path = world
        before = _counts(factory())
        state["requests"] = []

        with make_client(state) as client:
            summary = run_refresh(
                client, factory, mandate, run_id="refresh1", data_root=tmp_path / "data"
            )

        assert summary["counts"] == {
            "companies_unchanged": 1,
            "coverage_facts": summary["counts"]["coverage_facts"],
        }
        assert state["requests"] == ["/company/10122954/filing-history"]
        assert _counts(factory()) == before
        # The refresh run's coverage report is complete, not a delta.
        session = factory()
        facts = session.execute(
            select(ConceptCoverageRow).where(ConceptCoverageRow.run_id == "refresh1")
        ).scalars().all()
        ingest_facts = session.execute(
            select(ConceptCoverageRow).where(ConceptCoverageRow.run_id == "ingest1")
        ).scalars().all()
        assert {(f.concept, f.status) for f in facts} == {
            (f.concept, f.status) for f in ingest_facts
        }
        assert summary["coverage"]["by_classification_code"]["62012"]["companies"] == 1


class TestChangedCompany:
    def test_diff_driven_refetch_and_currency_flip(self, world):
        state, factory, mandate, tmp_path = world
        session = factory()
        doc1_figures = session.execute(
            select(func.count()).select_from(FigureRow).where(
                FigureRow.source_document_id == "gb:10122954:doc:docmicro1"
            )
        ).scalar_one()
        state["filing_items"] = [TXN3, TXN2, TXN1]
        state["officer_resigned"] = True
        state["requests"] = []

        with make_client(state) as client:
            summary = run_refresh(
                client, factory, mandate, run_id="refresh2", data_root=tmp_path / "data"
            )

        counts = summary["counts"]
        assert counts["companies_changed"] == 1
        assert counts["new_transactions"] == 2
        assert counts["filings_new"] == 2
        assert counts["officers_updated"] == 1  # resignation landed as an update
        assert counts.get("officers_new", 0) == 0
        assert counts["documents_fetched"] == 1
        assert counts["figures_new"] == doc1_figures  # re-filing carries same facts
        assert counts["current_flag_changes"] == doc1_figures  # doc1 superseded
        assert counts.get("restatement_events_new", 0) == 0  # values agree

        # Only the families named by the new filing categories were fetched:
        # accounts (documents) and officers — never ownership or securities.
        assert "/company/10122954/persons-with-significant-control" not in state["requests"]
        assert "/company/10122954/charges" not in state["requests"]
        assert "/company/10122954/officers" in state["requests"]
        assert "/company/10122954" in state["requests"]  # profile, changed company only

        session = factory()
        current_docs = {
            d
            for (d,) in session.execute(
                select(FigureRow.source_document_id).where(FigureRow.is_current)
            )
        }
        assert current_docs == {"gb:10122954:doc:docmicro2"}
        officer = session.execute(select(OfficerRow)).scalars().first()
        assert officer.resigned_on == date(2023, 2, 1)

    def test_officer_only_change_keeps_store_coverage(self, world):
        state, factory, mandate, tmp_path = world
        state["filing_items"] = [TXN3, TXN1]  # no new accounts filing
        state["officer_resigned"] = True

        with make_client(state) as client:
            summary = run_refresh(
                client, factory, mandate, run_id="refresh-officers", data_root=tmp_path / "data"
            )

        assert summary["counts"]["companies_changed"] == 1
        assert summary["counts"].get("documents_fetched", 0) == 0
        session = factory()
        facts = {
            f.concept: f.status
            for f in session.execute(
                select(ConceptCoverageRow).where(
                    ConceptCoverageRow.run_id == "refresh-officers"
                )
            ).scalars()
        }
        # Coverage still reads the parsed store — never not_filed.
        assert facts["net_assets"] == "available"
        assert "not_filed" not in facts.values()

    def test_refresh_is_idempotent(self, world):
        state, factory, mandate, tmp_path = world
        state["filing_items"] = [TXN3, TXN2, TXN1]
        state["officer_resigned"] = True
        with make_client(state) as client:
            run_refresh(
                client, factory, mandate, run_id="refresh2", data_root=tmp_path / "data"
            )
        before = _counts(factory())
        fetches = state.get("content_fetches", 0)

        with make_client(state) as client:
            summary = run_refresh(
                client, factory, mandate, run_id="refresh3", data_root=tmp_path / "data"
            )

        assert summary["counts"].get("companies_changed", 0) == 0
        assert summary["counts"]["companies_unchanged"] == 1
        assert summary["counts"].get("current_flag_changes", 0) == 0
        assert _counts(factory()) == before
        assert state.get("content_fetches", 0) == fetches
