"""Incremental refresh: filing-history transaction diff drives fetching.

For every company already in the store, one filing-history request
decides everything else. The registry's transaction ids are immutable,
so `live transactions − stored transactions` is an exact change list:

- no new transactions → the company is untouched (that one request was
  the whole cost — no profile, record or document fetches);
- new transactions → their categories say which record families to
  refetch (officer filings → officers; ownership filings and
  confirmation-of-details filings → beneficial owners and statements;
  security filings → security interests), and new accounts filings with
  document links get their documents ingested, observation currency
  recomputed, and restatements detected — same code paths as ingest,
  same deterministic ids, so a refresh is idempotent too.

Coverage facts are rewritten for every refreshed company (from the
store, no extra requests), so each refresh run's coverage report is a
complete standing output, not a delta.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Mapping

from sqlalchemy import select
from sqlalchemy.orm import Session

from deal_engine.adapters.companies_house import mapping
from deal_engine.adapters.companies_house.client import CompaniesHouseClient
from deal_engine.adapters.companies_house.concept_map import ConceptMap
from deal_engine.adapters.companies_house.pipeline import (
    IngestConfig,
    IngestError,
    _bump,
    _ingest_accounts_document,
    _upsert_company,
    build_coverage_report,
    detect_restatements,
    refresh_current_flags,
    sync_beneficial_owners,
    sync_filings,
    sync_officers,
    sync_security_interests,
    write_coverage_facts,
)
from deal_engine.db.tables import CompanyRow, FilingRow, RunRow, SourceDocumentRow

# Filing-history categories → record families to refetch. The registry's
# category enum is officially incomplete; anything unrecognised falls
# through harmlessly (its filing row is still stored verbatim).
_OFFICER_CATEGORIES = {"officers"}
_OWNERSHIP_CATEGORIES = {"persons-with-significant-control", "confirmation-statement"}
_SECURITY_CATEGORIES = {"mortgage"}
_ACCOUNTS_CATEGORY = "accounts"


def refresh_company(
    session: Session,
    client: CompaniesHouseClient,
    cache_root: Path,
    company: CompanyRow,
    concept_map: ConceptMap,
    config: IngestConfig,
    run_id: str,
    counts: dict[str, int],
) -> dict:
    cid = company.id
    registration_id = company.registration_id
    stored = {
        txn
        for (txn,) in session.execute(
            select(FilingRow.transaction_id).where(FilingRow.company_id == cid)
        )
    }
    raw_filings = client.get_filing_history(registration_id)
    new_items = [
        item for item in raw_filings if item.get("transaction_id") not in stored
    ]
    if not new_items:
        _bump(counts, "companies_unchanged")
        _write_coverage_from_store(session, cid, registration_id, run_id, counts)
        return {"company_id": cid, "changed": False, "new_transactions": 0}

    _bump(counts, "companies_changed")
    _bump(counts, "new_transactions", len(new_items))
    sync_filings(session, raw_filings, cid, counts)

    # Status and name changes always arrive with filings, so a changed
    # company warrants one profile fetch; an unchanged one never does.
    profile = client.get_company_profile(registration_id)
    _upsert_company(session, mapping.map_company(profile), counts)

    categories = {item.get("category") for item in new_items}
    if categories & _OFFICER_CATEGORIES:
        sync_officers(session, client, registration_id, cid, counts)
    if categories & _OWNERSHIP_CATEGORIES:
        sync_beneficial_owners(session, client, registration_id, cid, counts)
    if categories & _SECURITY_CATEGORIES:
        sync_security_interests(session, client, registration_id, cid, counts)

    new_accounts = [
        item
        for item in new_items
        if item.get("category") == _ACCOUNTS_CATEGORY
        and (item.get("links") or {}).get("document_metadata")
    ]
    documents = [
        _ingest_accounts_document(
            session, client, cache_root, cid, item, concept_map, config, counts
        )
        for item in new_accounts
    ]
    if documents:
        _bump(counts, "current_flag_changes", refresh_current_flags(session, cid))
        _bump(counts, "restatement_events_new", detect_restatements(session, cid, config))

    # Coverage always considers the WHOLE store, not just this refresh's
    # documents — an officer-only change must not degrade a company with
    # parsed accounts to not_filed.
    fresh = {row.id: figures for row, figures in documents}
    stored = (
        session.execute(
            select(SourceDocumentRow).where(SourceDocumentRow.company_id == cid)
        )
        .scalars()
        .all()
    )
    note = write_coverage_facts(
        session, cid, run_id, profile, [(row, fresh.get(row.id)) for row in stored], counts
    )
    return {
        "company_id": cid,
        "changed": True,
        "new_transactions": len(new_items),
        "note": note,
    }


def _write_coverage_from_store(
    session: Session, cid: str, registration_id: str, run_id: str, counts: dict[str, int]
) -> None:
    """Coverage facts for an unchanged company come from persisted
    documents — zero requests, but the run's report stays complete."""
    docs = (
        session.execute(
            select(SourceDocumentRow).where(SourceDocumentRow.company_id == cid)
        )
        .scalars()
        .all()
    )
    write_coverage_facts(
        session,
        cid,
        run_id,
        {"company_number": registration_id},
        [(doc, None) for doc in docs],
        counts,
    )


def run_refresh(
    client: CompaniesHouseClient,
    session_factory: Callable[[], Session],
    mandate,
    *,
    run_id: str,
    data_root: Path = Path("data"),
    config: IngestConfig = IngestConfig(),
    progress: Callable[[str], None] | None = None,
) -> dict:
    cache_root = data_root / "cache"
    concept_map = ConceptMap.load()
    session = session_factory()
    say = progress or (lambda _msg: None)

    if session.get(RunRow, run_id) is None:
        session.add(
            RunRow(
                run_id=run_id,
                command="refresh",
                args={"mandate": mandate.id, "limit": config.limit},
                started_at=datetime.now(timezone.utc),
            )
        )
        session.commit()

    companies = (
        session.execute(select(CompanyRow).order_by(CompanyRow.id))
        .scalars()
        .all()
    )
    if config.limit:
        companies = companies[: config.limit]

    counts: dict[str, int] = {}
    errors: list[str] = []
    refreshed = 0
    for company in companies:
        try:
            outcome = refresh_company(
                session, client, cache_root, company, concept_map, config, run_id, counts
            )
            session.commit()
            refreshed += 1
            if outcome["changed"]:
                say(
                    f"{company.registration_id}: {outcome['new_transactions']} "
                    f"new transaction(s)"
                )
        except Exception as exc:  # per-company isolation, same as ingest
            session.rollback()
            errors.append(f"{company.registration_id}: {exc!r}")

    report = build_coverage_report(session, run_id, mandate)
    summary = {
        "run_id": run_id,
        "companies_in_store": len(companies),
        "refreshed": refreshed,
        "counts": counts,
        "errors": errors,
        "coverage": report,
    }
    reports_dir = data_root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / f"refresh-{run_id}.json"
    report_path.write_text(json.dumps(summary, indent=1, default=str), encoding="utf-8")
    summary["report_path"] = report_path.as_posix()

    run_row = session.get(RunRow, run_id)
    run_row.finished_at = datetime.now(timezone.utc)
    run_row.exit_status = 0 if not errors else 1
    run_row.counts = {**counts, "refreshed": refreshed, "errors": len(errors)}
    session.commit()
    return summary


def refresh_from_env(
    env: Mapping[str, str],
    session_factory: Callable[[], Session],
    mandate,
    *,
    run_id: str,
    data_root: Path,
    limit: int = 0,
    checkpoint_path: Path | None = None,  # accepted for interface parity; unused
    docs_per_company: int = 3,
    progress: Callable[[str], None] | None = None,
) -> dict:
    """Adapter-registry refresh entry point (limit 0 = whole store)."""
    api_key = env.get("CH_API_KEY", "")
    if not api_key:
        raise IngestError("CH_API_KEY is not set in the environment")
    config = IngestConfig(limit=limit, accounts_docs_per_company=docs_per_company)
    with CompaniesHouseClient(api_key) as client:
        return run_refresh(
            client,
            session_factory,
            mandate,
            run_id=run_id,
            data_root=data_root,
            config=config,
            progress=progress,
        )
