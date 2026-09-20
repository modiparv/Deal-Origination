"""Web data export: the static site's bundle is a mechanical projection of
the store. Pins the bucket rule, the index/record shapes the frontend
depends on, the manifest's integrity fields, and that every value in the
export is a verbatim copy or a count — nothing financial is computed.
"""

import gzip
import hashlib
import importlib.util
import json
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

pytest.importorskip("sqlalchemy", reason="sqlalchemy unavailable; export tests run in CI")

from deal_engine.db.session import get_engine, init_db, make_session_factory  # noqa: E402
from deal_engine.db.tables import (  # noqa: E402
    BeneficialOwnerRow,
    CompanyRow,
    ConceptCoverageRow,
    FigureRow,
    FilingRow,
    OfficerRow,
    RunRow,
    SecurityInterestRow,
    SourceDocumentRow,
)

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("export_web_data", ROOT / "scripts" / "export_web_data.py")
export_web_data = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(export_web_data)


@pytest.fixture()
def store(tmp_path):
    db_path = tmp_path / "engine.db"
    engine = get_engine(db_path)
    init_db(engine)
    session = make_session_factory(engine)()
    session.add(RunRow(run_id="20260901T020000Z-aaaaaaaa", command="ingest", args={},
                       started_at=datetime(2026, 9, 1, 2, tzinfo=timezone.utc),
                       finished_at=datetime(2026, 9, 1, 4, tzinfo=timezone.utc), exit_status=0,
                       counts={"ingested": 1, "errors": 0, "figures_new": 3}))
    session.add(CompanyRow(id="gb:SC157026", jurisdiction="GB", registration_id="SC157026", name="TEST LTD",
                           name_variants=["OLD NAME LTD"], incorporation_date=date(1995, 3, 29), status="active",
                           classification_codes=["62012", "69102"], classification_taxonomy="sic_2007",
                           registered_address={"locality": "Glasgow", "country": "Scotland"}))
    # Foreign keys are enforced; parents flush before children, as the pipeline does.
    session.commit()
    session.add(SourceDocumentRow(id="gb:SC157026:doc:D1", adapter="companies_house", jurisdiction="GB",
                                  company_id="gb:SC157026", external_document_id="D1", transaction_id="TXN1",
                                  document_type="AA", account_type="total-exemption-full", filed_date=date(2026, 3, 27),
                                  period_end=date(2026, 3, 25), retrieved_at=datetime(2026, 9, 1, 3),
                                  content_type="application/xhtml+xml", content_hash="ab" * 32,
                                  parse_status="parsed", production_software="Companies House"))
    session.add(SourceDocumentRow(id="gb:SC157026:doc:D0", adapter="companies_house", jurisdiction="GB",
                                  company_id="gb:SC157026", external_document_id="D0", transaction_id="TXN0",
                                  document_type="AA", account_type="micro-entity", filed_date=date(2025, 3, 20),
                                  period_end=date(2025, 3, 25), retrieved_at=datetime(2026, 9, 1, 3),
                                  content_type="application/xhtml+xml", content_hash="cd" * 32,
                                  parse_status="quarantined", parse_error_count=31))
    # Parsed cleanly but yielded no figures: the coverage layer records
    # parse_failed against it — the defect list must carry it too.
    session.add(SourceDocumentRow(id="gb:SC157026:doc:D2", adapter="companies_house", jurisdiction="GB",
                                  company_id="gb:SC157026", external_document_id="D2", transaction_id="TXN2",
                                  document_type="AA", account_type="micro-entity", filed_date=date(2024, 3, 20),
                                  period_end=date(2024, 3, 25), retrieved_at=datetime(2026, 9, 1, 3),
                                  content_type="application/xhtml+xml", content_hash="ef" * 32,
                                  parse_status="parsed", production_software="Zero Yield Ltd"))
    session.commit()
    for fid, concept, value, pe, current in (
        ("fig:1", "revenue", 17009, date(2026, 3, 25), True),
        ("fig:2", "net_assets", 334222, date(2026, 3, 25), True),
        ("fig:3", "net_assets", 300000, date(2025, 3, 25), True),
    ):
        session.add(FigureRow(id=fid, company_id="gb:SC157026", concept=concept, value=value, unit="iso4217:GBP",
                              currency="GBP", period_type="instant" if concept == "net_assets" else "duration",
                              period_start=date(2025, 3, 26) if concept == "revenue" else pe, period_end=pe,
                              dimensions={}, dimensions_hash="0", basis="filed",
                              source_document_id="gb:SC157026:doc:D1", source_tag="core:X", raw_text=str(value),
                              is_current=current))
    session.add(ConceptCoverageRow(id="cov:1", company_id="gb:SC157026", concept="revenue", period_end=date(2026, 3, 25),
                                   status="available", source_document_id="gb:SC157026:doc:D1",
                                   run_id="20260901T020000Z-aaaaaaaa"))
    session.add(ConceptCoverageRow(id="cov:2", company_id="gb:SC157026", concept="cash", period_end=date(2026, 3, 25),
                                   status="filed_without_concept", source_document_id="gb:SC157026:doc:D1",
                                   detail="regime 'total-exemption-full' omits this concept",
                                   run_id="20260901T020000Z-aaaaaaaa"))
    session.add(ConceptCoverageRow(id="cov:3", company_id="gb:SC157026", concept="gross_profit",
                                   period_end=date(2026, 3, 25), status="parse_failed",
                                   source_document_id="gb:SC157026:doc:D2",
                                   detail="0 figures extracted; unmapped tags: x:Foo, x:Bar",
                                   run_id="20260901T020000Z-aaaaaaaa"))
    session.add(OfficerRow(id="o1", company_id="gb:SC157026", appointment_id="p1:2000-11-01", name="DOE, Jane",
                           role="director", appointed_on=date(2000, 11, 1), dob_year=1961))
    session.add(BeneficialOwnerRow(id="b1", company_id="gb:SC157026", external_id="x1",
                                   kind="individual-person-with-significant-control", name="Jane Doe",
                                   control_natures=["ownership-of-shares-75-to-100-percent"],
                                   notified_on=date(2016, 4, 6), dob_year=1961, dob_month=5))
    session.add(FilingRow(id="f1", company_id="gb:SC157026", transaction_id="TXN1", category="accounts", type="AA",
                          filing_date=date(2026, 3, 27), description="accounts-with-accounts-type-total-exemption-full",
                          description_values={"made_up_date": "2026-03-25"}, document_id="D1", paper_filed=False))
    session.add(FilingRow(id="f2", company_id="gb:SC157026", transaction_id="TXNOLD", category="capital", type="SH01",
                          filing_date=date(2010, 1, 1), description="capital-allotment-shares"))
    session.add(SecurityInterestRow(id="s1", company_id="gb:SC157026", external_id="c1", status="outstanding",
                                    created_on=date(2014, 11, 19), secured_parties=["A BANK PLC"]))
    session.commit()
    return db_path


def test_bucket_key_is_last_three_characters_sanitised():
    assert export_web_data.bucket_key("SC157026") == "026"
    assert export_web_data.bucket_key("R-1/2") == "1_2"
    assert export_web_data.bucket_key("") == "_"


def test_export_shapes_and_integrity(store, tmp_path):
    out = tmp_path / "web-data"
    manifest = export_web_data.export(store, out, "https://example.invalid/web-data.jsonl.gz")

    # manifest: totals are counts, the bundle is hashed, run history carried
    assert manifest["totals"] == {
        "companies": 1, "figures": 3, "documents": 3, "filings": 2, "officers": 1,
        "beneficial_owners": 1, "security_interests": 1, "restatement_events": 0,
    }
    assert manifest["modes"] == {"financial": 1}
    assert manifest["parse_failures"] == {"documents": 2, "companies": 1}
    assert manifest["run"]["run_id"] == "20260901T020000Z-aaaaaaaa"
    assert manifest["runs"][-1]["ingested"] == 1
    bundle = out / "web-data.jsonl.gz"
    assert manifest["bundle"]["sha256"] == hashlib.sha256(bundle.read_bytes()).hexdigest()
    assert manifest["bundle"]["bytes"] == bundle.stat().st_size
    assert json.loads((out / "manifest.json").read_text())["bundle"]["sha256"] == manifest["bundle"]["sha256"]

    # index: one row, latest current figures referenced by id, owner dob verbatim
    index = json.loads((out / "index.json").read_text())
    row = index["companies"][0]
    assert row["id"] == "gb:SC157026"
    assert row["latest"]["revenue"] == {"figure_id": "fig:1", "value": 17009.0, "period_end": "2026-03-25",
                                        "filed_date": "2026-03-27"}
    assert row["latest"]["net_assets"]["figure_id"] == "fig:2"  # latest period wins
    assert row["latest"]["employees"] is None
    assert row["owner_dob"] == {"year": 1961, "month": 5}
    assert row["single_owner_75"] is True
    assert row["coverage"] == {"statuses": {"available": 1, "filed_without_concept": 1, "parse_failed": 1},
                               "of": 3, "period_end": "2026-03-25"}
    assert row["freshest_period"] == "2026-03-25" and row["freshest_filed"] == "2026-03-27"
    assert row["last_charge_created"] == "2014-11-19"
    assert row["last_officer_appointed"] == "2000-11-01"
    assert row["filings"] == 2 and row["documents"] == 3
    assert row["first_seen"] == "20260901T020000Z-aaaaaaaa"
    assert row["software"] == "Companies House"
    assert "EBITDA" not in json.dumps(row).upper()  # no derived figure sneaks into the export

    # bucket record: full figures with provenance; only recent + accounts filings carried
    bucket = json.loads((out / "c" / "026.json").read_text())
    rec = bucket["gb:SC157026"]
    assert {f["id"] for f in rec["figures"]} == {"fig:1", "fig:2", "fig:3"}
    assert all(f["source_document_id"] and f["source_tag"] for f in rec["figures"])
    assert [f["transaction_id"] for f in rec["filings"]] == ["TXN1"]  # the 2010 capital filing is out of window
    assert rec["company"]["filings_on_register"] == 2
    assert rec["company"]["name_variants"] == ["OLD NAME LTD"]
    assert rec["coverage"][0]["concept"] == "cash"  # sorted by concept
    assert rec["charges"][0]["secured_parties"] == ["A BANK PLC"]

    # ops: the quarantined document AND the zero-yield parsed document
    # are listed defects, each with its software and recorded cause
    ops = json.loads((out / "ops.json").read_text())
    failures = {r["document_id"]: r for r in ops["parse_failures"]}
    assert set(failures) == {"gb:SC157026:doc:D0", "gb:SC157026:doc:D2"}
    assert failures["gb:SC157026:doc:D0"]["parse_status"] == "quarantined"
    assert failures["gb:SC157026:doc:D0"]["detail"] == "parse_status quarantined"
    assert failures["gb:SC157026:doc:D2"]["detail"].startswith("0 figures extracted")
    assert failures["gb:SC157026:doc:D2"]["production_software"] == "Zero Yield Ltd"
    assert ops["by_production_software"]["Companies House"]["with_figures"] == 1
    assert ops["by_production_software"]["Zero Yield Ltd"]["zero_figure"] == 1
    assert ops["by_production_software"]["undeclared"]["quarantined"] == 1

    # bundle: streamable records, manifest first, one bucket line
    with gzip.open(bundle, "rt", encoding="utf-8") as fh:
        kinds = [line.split("\t", 2)[:2] for line in fh]
    assert kinds[0] == ["manifest", "-"] and kinds[1] == ["index", "-"] and kinds[2] == ["ops", "-"]
    assert kinds[3:] == [["bucket", "026"]]
    assert manifest["bundle"]["asset"] == "web-data.jsonl.gz"
    assert manifest["bundle"]["url"] == "https://example.invalid/web-data.jsonl.gz"


def test_versioned_bundle_named_per_run(store, tmp_path):
    # A {run_id} in the URL names the asset per run, so an older
    # manifest keeps pointing at a bundle that still exists.
    out = tmp_path / "web-data-v"
    manifest = export_web_data.export(store, out, "https://example.invalid/web-data-{run_id}.jsonl.gz")
    assert manifest["bundle"]["asset"] == "web-data-20260901T020000Z-aaaaaaaa.jsonl.gz"
    assert manifest["bundle"]["url"] == "https://example.invalid/web-data-20260901T020000Z-aaaaaaaa.jsonl.gz"
    bundle = out / manifest["bundle"]["asset"]
    assert bundle.is_file()
    assert manifest["bundle"]["sha256"] == hashlib.sha256(bundle.read_bytes()).hexdigest()
    assert not (out / "web-data.jsonl.gz").exists()
