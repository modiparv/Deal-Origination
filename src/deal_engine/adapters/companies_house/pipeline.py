"""Companies House ingest pipeline: mandate universe → canonical rows.

This module is registry-specific by design and therefore lives in the
adapter package: it speaks SIC codes, the advanced-search window, the
accounts-filing description grammar and the document API. Everything it
persists is canonical — core never sees the local vocabulary. The CLI
reaches it through the adapter registry's ingest-runner declaration,
never by name.

Universe enumeration expands the mandate's sector patterns to exact
classification codes and walks the registry's advanced search; when a
query's hit count exceeds the retrievable window the incorporation-date
range is bisected until every slice fits. Triage skips companies the
mandate can never want (wrong status, excluded sector, dormant) before
any per-company fetching, capped so a dormant-heavy code cannot burn the
whole request budget.

Per company, registry records are mapped through the adapter's
vocabulary into rows with deterministic identifiers, so re-ingesting is
idempotent: zero new rows, zero `is_current` flag changes (DoD #4).
Accounts documents land in the content-addressed cache, are parsed, and
their figures persist through the provenance-enforcing Figure model.
Observation currency (`is_current`) is recomputed deterministically —
latest filed date wins, document id breaks ties. When two documents
disagree about the same observation, a restatement event records every
delta with a classification (rounding / reclassification / genuine) and
an explicit materiality verdict from the mandate-level floors.

Every run writes concept-coverage facts — absence carries a cause — and
the coverage report by classification code is a standing output.
"""

from __future__ import annotations

import io
import json
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
from typing import Callable, Iterator, Mapping

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from deal_engine.adapters.companies_house import mapping, sic
from deal_engine.adapters.companies_house.client import (
    IXBRL_TYPE,
    CompaniesHouseClient,
    CompaniesHouseError,
)
from deal_engine.adapters.companies_house.concept_map import ConceptMap
from deal_engine.adapters.companies_house_decl import COMPANIES_HOUSE_CAPABILITIES
from deal_engine.concepts import CONCEPTS, Flow
from deal_engine.db.repository import add_figure, add_source_document
from deal_engine.db.tables import (
    BeneficialOwnerRow,
    CompanyRow,
    ConceptCoverageRow,
    EventRow,
    ExemptionRow,
    FigureRow,
    FilingRow,
    OfficerRow,
    OwnershipStatementRow,
    RunRow,
    SecurityInterestRow,
    SourceDocumentRow,
)
from deal_engine.ingest.cache import store_blob
from deal_engine.ingest.checkpoint import Checkpoint
from deal_engine.models.common import (
    Basis,
    Consolidation,
    CoverageStatus,
    ParseStatus,
    RestatementClass,
    dimensions_hash,
)
from deal_engine.models.coverage import ConceptCoverageFact
from deal_engine.models.event import Event, EventType
from deal_engine.models.figure import Figure
from deal_engine.models.source import SourceDocument
from deal_engine.parse import extract_figures, parse_ixbrl
from deal_engine.parse.figures import DocumentFigures, FigureDraft


class IngestError(Exception):
    pass


# First possible incorporation date on the register (Joint Stock
# Companies Act era) — the left edge for date-slicing the search window.
_SEARCH_EPOCH = date(1844, 1, 1)


@dataclass(frozen=True)
class IngestConfig:
    limit: int = 200
    accounts_docs_per_company: int = 3
    search_page_size: int = 500
    search_window: int = 10_000  # advanced-search retrievable-results ceiling
    max_triage_factor: int = 5  # examine at most limit*factor profiles
    quarantine_error_threshold: int = 25
    # Restatement materiality gate (decision record §6): a delta is
    # material when it clears the larger of an absolute floor and a
    # relative floor against the larger operand.
    materiality_absolute: Decimal = Decimal("1000")
    materiality_relative: Decimal = Decimal("0.005")


# --------------------------------------------------------------------------
# universe enumeration


def enumerate_universe(
    client: CompaniesHouseClient,
    classification_codes: list[str],
    *,
    page_size: int = 500,
    window: int = 10_000,
    incorporated_from: date = _SEARCH_EPOCH,
    incorporated_to: date | None = None,
    stats: dict | None = None,
) -> Iterator[dict]:
    """Yield advanced-search company items for exact classification codes.

    The search only exposes ~`window` results per query, so ranges whose
    hit count exceeds it are bisected on incorporation date until each
    slice fits. Order is deterministic (slices ascend by date range).
    """
    upper = incorporated_to or date.today()
    probe = client.advanced_search(
        sic_codes=classification_codes,
        size=1,
        incorporated_from=incorporated_from.isoformat(),
        incorporated_to=upper.isoformat(),
    )
    hits = int(probe.get("hits") or 0)
    if stats is not None:
        stats["hits"] = stats.get("hits", 0) + hits
        stats.setdefault("slices", 0)
        stats["slices"] += 1
    if hits > window and incorporated_from < upper:
        mid = incorporated_from + timedelta(days=(upper - incorporated_from).days // 2)
        yield from enumerate_universe(
            client,
            classification_codes,
            page_size=page_size,
            window=window,
            incorporated_from=incorporated_from,
            incorporated_to=mid,
            stats=stats,
        )
        yield from enumerate_universe(
            client,
            classification_codes,
            page_size=page_size,
            window=window,
            incorporated_from=mid + timedelta(days=1),
            incorporated_to=upper,
            stats=stats,
        )
        return
    start = 0
    reachable = min(hits, window)
    while start < reachable:
        page = client.advanced_search(
            sic_codes=classification_codes,
            size=page_size,
            start_index=start,
            incorporated_from=incorporated_from.isoformat(),
            incorporated_to=upper.isoformat(),
        )
        items = page.get("items") or []
        if not items:
            return
        yield from items
        start += len(items)


def triage(profile: dict, mandate) -> str | None:
    """Reason to skip a company before per-company fetching, or None."""
    status = profile.get("company_status")
    if status != "active":
        return f"status_{status}"
    codes = [str(c) for c in profile.get("sic_codes", [])]
    exclude = list(mandate.sectors.exclude)
    if exclude and any(sic.matches_any(c, exclude) for c in codes):
        return "excluded_classification"
    if not any(sic.matches_any(c, list(mandate.sectors.include)) for c in codes):
        return "no_included_classification"
    last_type = ((profile.get("accounts") or {}).get("last_accounts") or {}).get("type")
    if last_type == "dormant":
        return "dormant"
    return None


# --------------------------------------------------------------------------
# row helpers


def _d(value: str | None) -> date | None:
    return date.fromisoformat(value) if value else None


def _bump(counts: dict[str, int], key: str, by: int = 1) -> None:
    counts[key] = counts.get(key, 0) + by


def _insert_if_absent(session: Session, row) -> bool:
    if session.get(type(row), row.id) is None:
        session.add(row)
        session.flush()
        return True
    return False


def _upsert(
    session: Session,
    row_cls,
    mapped: dict,
    date_fields: tuple[str, ...],
    counts: dict[str, int],
    family: str,
) -> None:
    """Insert a mapped record, or update the changed columns of the
    existing row (same deterministic id). Identical data touches
    nothing, which is what keeps re-ingest and no-op refresh at zero."""
    data = dict(mapped)
    for field in date_fields:
        data[field] = _d(data[field])
    existing = session.get(row_cls, data["id"])
    if existing is None:
        session.add(row_cls(**data))
        session.flush()
        _bump(counts, f"{family}_new")
        return
    changed = False
    for key, value in data.items():
        if key != "id" and getattr(existing, key) != value:
            setattr(existing, key, value)
            changed = True
    if changed:
        _bump(counts, f"{family}_updated")


def figure_id(source_document_id: str, draft: FigureDraft, dims_hash: str, unit: str) -> str:
    key = "|".join(
        [source_document_id, draft.concept, draft.period_start, draft.period_end, dims_hash, unit]
    )
    return "fig:" + sha256(key.encode("utf-8")).hexdigest()[:24]


def _currency_from_unit(concept: str, unit: str | None) -> str | None:
    # Registry quirk honoured: some filers tag pure counts (e.g. average
    # employees) with a currency unit — a COUNT concept never carries one.
    if unit is None or CONCEPTS[concept].flow is Flow.COUNT:
        return None
    tail = unit.rsplit(":", 1)[-1].upper()
    if len(tail) == 3 and tail.isalpha():
        return tail
    return None


# --------------------------------------------------------------------------
# per-company ingest


def _upsert_company(session: Session, mapped: dict, counts: dict[str, int]) -> str:
    cid = mapped["id"]
    row = session.get(CompanyRow, cid)
    fields = dict(
        jurisdiction=mapped["jurisdiction"],
        registration_id=mapped["registration_id"],
        name=mapped["name"],
        name_variants=mapped["name_variants"],
        incorporation_date=_d(mapped["incorporation_date"]),
        status=mapped["status"],
        classification_codes=mapped["classification_codes"],
        classification_taxonomy=mapped["classification_taxonomy"],
        registered_address=mapped["registered_address"],
    )
    if row is None:
        session.add(CompanyRow(id=cid, **fields))
        session.flush()
        _bump(counts, "companies_new")
    else:
        changed = False
        for key, value in fields.items():
            if getattr(row, key) != value:
                setattr(row, key, value)
                changed = True
        if changed:
            _bump(counts, "companies_updated")
    return cid


def sync_officers(
    session: Session, client: CompaniesHouseClient, registration_id: str, cid: str, counts: dict[str, int]
) -> None:
    for item in client.get_officers(registration_id):
        _upsert(
            session,
            OfficerRow,
            mapping.map_officer(item, cid),
            ("appointed_on", "resigned_on"),
            counts,
            "officers",
        )


def sync_beneficial_owners(
    session: Session, client: CompaniesHouseClient, registration_id: str, cid: str, counts: dict[str, int]
) -> None:
    for item in client.get_beneficial_owners(registration_id):
        _upsert(
            session,
            BeneficialOwnerRow,
            mapping.map_beneficial_owner(item, cid),
            ("notified_on", "ceased_on"),
            counts,
            "beneficial_owners",
        )
    for item in client.get_ownership_statements(registration_id):
        _upsert(
            session,
            OwnershipStatementRow,
            mapping.map_ownership_statement(item, cid),
            ("notified_on", "ceased_on"),
            counts,
            "ownership_statements",
        )
    for mapped in mapping.map_exemptions(client.get_exemptions(registration_id), cid):
        _upsert(session, ExemptionRow, mapped, (), counts, "exemptions")


def sync_security_interests(
    session: Session, client: CompaniesHouseClient, registration_id: str, cid: str, counts: dict[str, int]
) -> None:
    for item in client.get_charges(registration_id).get("items", []):
        _upsert(
            session,
            SecurityInterestRow,
            mapping.map_security_interest(item, cid),
            ("created_on", "delivered_on", "satisfied_on"),
            counts,
            "security_interests",
        )


def sync_filings(
    session: Session, raw_items: list[dict], cid: str, counts: dict[str, int]
) -> None:
    # Filing-history transactions are immutable registry records: insert
    # only, never update — the transaction diff depends on that.
    for item in raw_items:
        mapped = mapping.map_filing(item, cid)
        row = FilingRow(**{**mapped, "filing_date": _d(mapped["filing_date"])})
        if _insert_if_absent(session, row):
            _bump(counts, "filings_new")


def _ingest_registry_records(
    session: Session,
    client: CompaniesHouseClient,
    registration_id: str,
    cid: str,
    counts: dict[str, int],
) -> list[dict]:
    """Officers, beneficial owners, statements, exemptions, security
    interests and filing history. Returns the RAW filing-history items —
    accounts-document selection needs the absolute metadata URLs the
    mapped rows deliberately do not carry."""
    sync_officers(session, client, registration_id, cid, counts)
    sync_beneficial_owners(session, client, registration_id, cid, counts)
    sync_security_interests(session, client, registration_id, cid, counts)
    raw_filings = client.get_filing_history(registration_id)
    sync_filings(session, raw_filings, cid, counts)
    return raw_filings


def _ingest_accounts_document(
    session: Session,
    client: CompaniesHouseClient,
    cache_root: Path,
    cid: str,
    raw_filing: dict,
    concept_map: ConceptMap,
    config: IngestConfig,
    counts: dict[str, int],
) -> tuple[SourceDocumentRow, DocumentFigures | None]:
    metadata_url = raw_filing["links"]["document_metadata"]
    external_document_id = mapping.document_id_from_metadata_url(metadata_url)
    doc_id = f"{cid}:doc:{external_document_id}"
    existing = session.get(SourceDocumentRow, doc_id)
    if existing is not None:
        _bump(counts, "documents_cached")
        return existing, None

    account_type = mapping.account_type_from_description(raw_filing.get("description"))
    period_end = _d((raw_filing.get("description_values") or {}).get("made_up_date"))
    filed = _d(raw_filing.get("date"))
    base = dict(
        id=doc_id,
        adapter=mapping.ADAPTER,
        jurisdiction=mapping.JURISDICTION,
        company_id=cid,
        external_document_id=external_document_id or "unknown",
        transaction_id=raw_filing.get("transaction_id"),
        document_type=raw_filing.get("type") or "accounts",
        account_type=account_type,
        filed_date=filed,
        period_end=period_end,
        retrieved_at=datetime.now(timezone.utc),
    )

    try:
        result = client.fetch_document(metadata_url)
    except CompaniesHouseError as exc:
        # Filed, but the registry offers no fetchable rendition: an
        # unparseable-format outcome with the failure recorded verbatim.
        doc = SourceDocument(
            **base,
            parse_status=ParseStatus.PDF_ONLY,
            fetch_headers={"fetch_error": str(exc)},
        )
        row = add_source_document(session, doc)
        session.flush()
        _bump(counts, "documents_unfetchable")
        return row, None

    content_hash, blob = store_blob(cache_root, result.content)
    base.update(
        content_type=result.content_type,
        raw_path=blob.as_posix(),
        content_hash=content_hash,
        fetch_headers={"available_types": ",".join(result.available_types)},
    )
    _bump(counts, "documents_fetched")

    if result.content_type != IXBRL_TYPE:
        doc = SourceDocument(**base, parse_status=ParseStatus.PDF_ONLY)
        row = add_source_document(session, doc)
        session.flush()
        return row, None

    parsed = parse_ixbrl(io.BytesIO(result.content))
    figures = extract_figures(parsed, concept_map)
    if figures.parse_error_count > config.quarantine_error_threshold:
        doc = SourceDocument(
            **base,
            parse_status=ParseStatus.QUARANTINED,
            parse_error_count=figures.parse_error_count,
        )
        row = add_source_document(session, doc)
        session.flush()
        _bump(counts, "documents_quarantined")
        return row, figures

    doc = SourceDocument(
        **base,
        parse_status=ParseStatus.PARSED,
        parse_error_count=figures.parse_error_count,
    )
    row = add_source_document(session, doc)
    session.flush()

    for draft in figures.drafts:
        unit = draft.unit or "unspecified"
        fid = figure_id(doc_id, draft, dimensions_hash(dict(draft.dimensions)), unit)
        if session.get(FigureRow, fid) is not None:
            continue
        figure = Figure(
            id=fid,
            company_id=cid,
            concept=draft.concept,
            value=draft.value,
            unit=unit,
            currency=_currency_from_unit(draft.concept, draft.unit),
            period_type=draft.period_type,
            period_start=date.fromisoformat(draft.period_start),
            period_end=date.fromisoformat(draft.period_end),
            dimensions=dict(draft.dimensions),
            consolidation=(
                Consolidation.GROUP if account_type == "group" else Consolidation.COMPANY
            ),
            decimals=draft.decimals,
            raw_text=draft.raw_text or None,
            basis=Basis.FILED,
            source_document_id=doc_id,
            source_tag=draft.source_tag,
        )
        add_figure(session, figure)
        session.flush()
        _bump(counts, "figures_new")
    return row, figures


# --------------------------------------------------------------------------
# observation currency and restatements


def _observation_groups(
    session: Session, cid: str
) -> dict[tuple, list[tuple[FigureRow, SourceDocumentRow]]]:
    rows = session.execute(
        select(FigureRow, SourceDocumentRow)
        .join(SourceDocumentRow, FigureRow.source_document_id == SourceDocumentRow.id)
        .where(FigureRow.company_id == cid, FigureRow.basis == Basis.FILED.value)
    ).all()
    groups: dict[tuple, list[tuple[FigureRow, SourceDocumentRow]]] = {}
    for fig, doc in rows:
        key = (fig.concept, fig.period_start, fig.period_end, fig.dimensions_hash, fig.unit)
        groups.setdefault(key, []).append((fig, doc))
    return groups


def _doc_order(doc: SourceDocumentRow) -> tuple:
    return (doc.filed_date or date.min, doc.id)


def refresh_current_flags(session: Session, cid: str) -> int:
    """Deterministic `is_current` selection: latest filed date wins,
    document id breaks ties. Returns the number of flag changes."""
    changes = 0
    for members in _observation_groups(session, cid).values():
        winner = max(members, key=lambda pair: _doc_order(pair[1]))[0]
        for fig, _doc in members:
            desired = fig.id == winner.id
            if fig.is_current != desired:
                fig.is_current = desired
                changes += 1
    return changes


def _precision_tolerance(*rows: FigureRow) -> Decimal:
    # Filed precision defines agreement: with no stated decimals, whole
    # units are assumed (statutory accounts are filed in whole pounds).
    tolerances = [
        Decimal(10) ** -row.decimals if row.decimals is not None else Decimal(1)
        for row in rows
    ]
    return max(tolerances)


def classify_restatement(
    old: FigureRow, new: FigureRow, total_delta_within_tolerance: bool | None
) -> RestatementClass:
    delta = abs(Decimal(str(new.value)) - Decimal(str(old.value)))
    if delta <= _precision_tolerance(old, new):
        return RestatementClass.ROUNDING
    if total_delta_within_tolerance and old.concept not in ("net_assets", "equity"):
        return RestatementClass.RECLASSIFICATION
    return RestatementClass.GENUINE


def _is_material(old: FigureRow, new: FigureRow, config: IngestConfig) -> bool:
    delta = abs(Decimal(str(new.value)) - Decimal(str(old.value)))
    base = max(abs(Decimal(str(old.value))), abs(Decimal(str(new.value))))
    floor = max(config.materiality_absolute, config.materiality_relative * base)
    return delta >= floor


def detect_restatements(session: Session, cid: str, config: IngestConfig) -> int:
    """Project restatement events from disagreeing observations.

    One event per superseding document, listing every concept delta with
    its classification and materiality verdict. Deterministic ids make
    re-detection idempotent."""
    groups = _observation_groups(session, cid)

    # Balance-stability lookup for the reclassification test: net-assets
    # (equity fallback) value per (document, period) with no dimensions.
    totals: dict[tuple[str, date], Decimal] = {}
    for (concept, _start, end, _dims, _unit), members in groups.items():
        if concept not in ("net_assets", "equity"):
            continue
        for fig, doc in members:
            key = (doc.id, end)
            if concept == "net_assets" or key not in totals:
                totals[key] = Decimal(str(fig.value))

    by_new_doc: dict[str, dict] = {}
    for members in groups.values():
        if len({doc.id for _fig, doc in members}) < 2:
            continue
        ordered = sorted(members, key=lambda pair: _doc_order(pair[1]))
        for (old, old_doc), (new, new_doc) in zip(ordered, ordered[1:]):
            if old_doc.id == new_doc.id:
                continue
            if Decimal(str(new.value)) == Decimal(str(old.value)):
                continue
            old_total = totals.get((old_doc.id, old.period_end))
            new_total = totals.get((new_doc.id, new.period_end))
            total_stable = (
                abs(new_total - old_total) <= _precision_tolerance(old, new)
                if old_total is not None and new_total is not None
                else None
            )
            entry = by_new_doc.setdefault(
                new_doc.id,
                {"doc": new_doc, "superseded": old_doc.id, "items": []},
            )
            entry["items"].append(
                {
                    "concept": new.concept,
                    "period_end": new.period_end.isoformat(),
                    "old_value": str(old.value),
                    "new_value": str(new.value),
                    "old_figure_id": old.id,
                    "new_figure_id": new.id,
                    "classification": classify_restatement(old, new, total_stable).value,
                    "material": _is_material(old, new, config),
                }
            )

    created = 0
    for new_doc_id, entry in sorted(by_new_doc.items()):
        event_id = f"{cid}:event:restatement:{new_doc_id}"
        if session.get(EventRow, event_id) is not None:
            continue
        doc = entry["doc"]
        event_date = doc.filed_date or doc.period_end
        if event_date is None:
            continue  # cannot date the event; leave to refresh once dated
        event = Event(
            id=event_id,
            company_id=cid,
            event_type=EventType.RESTATEMENT,
            event_date=event_date,
            transaction_id=doc.transaction_id,
            source_document_id=new_doc_id,
            payload={
                "superseded_document_id": entry["superseded"],
                "restatements": entry["items"],
            },
        )
        session.add(
            EventRow(
                id=event.id,
                company_id=event.company_id,
                event_type=event.event_type.value,
                event_date=event.event_date,
                transaction_id=event.transaction_id,
                source_document_id=event.source_document_id,
                payload=event.payload,
            )
        )
        session.flush()
        created += 1
    return created


# --------------------------------------------------------------------------
# coverage facts


def write_coverage_facts(
    session: Session,
    cid: str,
    run_id: str,
    profile: dict,
    documents: list[tuple[SourceDocumentRow, DocumentFigures | None]],
    counts: dict[str, int],
) -> str | None:
    """One fact per canonical concept for the company's latest reporting
    period. Returns a report note when no period exists to report on."""
    last_accounts = (profile.get("accounts") or {}).get("last_accounts") or {}
    profile_period_end = _d(
        last_accounts.get("period_end_on") or last_accounts.get("made_up_to")
    )

    dated = [(doc, figs) for doc, figs in documents if doc.period_end is not None]
    newest: SourceDocumentRow | None = None
    newest_figures: DocumentFigures | None = None
    if dated:
        newest, newest_figures = max(dated, key=lambda pair: (pair[0].period_end, pair[0].id))
        period_end = newest.period_end
    elif profile_period_end is not None:
        period_end = profile_period_end
    else:
        return "no_reporting_period"

    account_type = newest.account_type if newest else None
    present_for_period: set[str] = set()
    if newest_figures is not None:
        present_for_period = {
            d.concept
            for d in newest_figures.drafts
            if d.period_end == period_end.isoformat()
        }
    elif newest is not None and newest.parse_status == ParseStatus.PARSED.value:
        # Re-ingest: the document was parsed on a previous run and its
        # figures are already persisted; read presence from the store.
        present_for_period = set(
            session.execute(
                select(FigureRow.concept).where(
                    FigureRow.source_document_id == newest.id,
                    FigureRow.period_end == period_end,
                )
            ).scalars()
        )

    for concept in sorted(COMPANIES_HOUSE_CAPABILITIES.coverage):
        detail: str | None = None
        source_document_id: str | None = None
        if newest is None:
            status = CoverageStatus.NOT_FILED
            if profile_period_end is not None:
                detail = "accounts filed per profile but no retrievable document"
        elif newest.parse_status == ParseStatus.PDF_ONLY.value:
            status = CoverageStatus.UNPARSEABLE_FORMAT
            source_document_id = newest.id
            detail = f"no machine-readable rendition (content_type={newest.content_type})"
        elif newest.parse_status == ParseStatus.QUARANTINED.value:
            status = CoverageStatus.PARSE_FAILED
            source_document_id = newest.id
            detail = f"quarantined: {newest.parse_error_count} parse errors beyond threshold"
        elif not present_for_period and not _document_has_any_figures(session, newest.id):
            status = CoverageStatus.PARSE_FAILED
            source_document_id = newest.id
            unmapped = (
                ", ".join(sorted(newest_figures.unmapped)[:5])
                if newest_figures is not None and newest_figures.unmapped
                else "none"
            )
            detail = f"document parsed to zero mapped figures (unmapped tags: {unmapped})"
        elif concept in present_for_period:
            status = CoverageStatus.AVAILABLE
            source_document_id = newest.id
        else:
            status = CoverageStatus.FILED_WITHOUT_CONCEPT
            source_document_id = newest.id
            coverage = COMPANIES_HOUSE_CAPABILITIES.concept_coverage(concept)
            predicted_absent = coverage.condition is not None and not coverage.condition.evaluate(
                {"account_type": account_type}
            )
            detail = (
                f"regime {account_type!r} omits this concept"
                if predicted_absent
                else f"absent though regime {account_type!r} typically includes it"
            )

        fact = ConceptCoverageFact(
            id=f"{run_id}:{cid}:{concept}:{period_end.isoformat()}",
            company_id=cid,
            concept=concept,
            period_end=period_end,
            status=status,
            source_document_id=source_document_id,
            detail=detail,
            run_id=run_id,
        )
        if session.get(ConceptCoverageRow, fact.id) is None:
            session.add(
                ConceptCoverageRow(
                    id=fact.id,
                    company_id=fact.company_id,
                    concept=fact.concept,
                    period_end=fact.period_end,
                    status=fact.status.value,
                    source_document_id=fact.source_document_id,
                    detail=fact.detail,
                    run_id=fact.run_id,
                )
            )
            session.flush()
            _bump(counts, "coverage_facts")
    return None


def _document_has_any_figures(session: Session, doc_id: str) -> bool:
    return (
        session.execute(
            select(func.count()).select_from(FigureRow).where(
                FigureRow.source_document_id == doc_id
            )
        ).scalar_one()
        > 0
    )


# --------------------------------------------------------------------------
# company orchestration


def ingest_company(
    session: Session,
    client: CompaniesHouseClient,
    cache_root: Path,
    profile: dict,
    concept_map: ConceptMap,
    config: IngestConfig,
    run_id: str,
    counts: dict[str, int],
) -> dict:
    registration_id = profile["company_number"]
    cid = _upsert_company(session, mapping.map_company(profile), counts)
    raw_filings = _ingest_registry_records(session, client, registration_id, cid, counts)

    accounts_filings = [
        item
        for item in raw_filings
        if item.get("category") == "accounts"
        and (item.get("links") or {}).get("document_metadata")
    ]
    accounts_filings.sort(
        key=lambda item: (item.get("date") or "", item.get("transaction_id") or ""),
        reverse=True,
    )
    documents: list[tuple[SourceDocumentRow, DocumentFigures | None]] = []
    for raw_filing in accounts_filings[: config.accounts_docs_per_company]:
        documents.append(
            _ingest_accounts_document(
                session, client, cache_root, cid, raw_filing, concept_map, config, counts
            )
        )

    flag_changes = refresh_current_flags(session, cid)
    _bump(counts, "current_flag_changes", flag_changes)
    _bump(counts, "restatement_events_new", detect_restatements(session, cid, config))

    note = write_coverage_facts(session, cid, run_id, profile, documents, counts)
    return {"company_id": cid, "note": note}


# --------------------------------------------------------------------------
# run orchestration and the standing coverage report


def build_coverage_report(session: Session, run_id: str, mandate) -> dict:
    """Concept coverage by classification code, within the mandate's
    filtered universe — the standing output of every ingest (§ data
    reality). A company is counted under every include-matching code it
    declares."""
    include = list(mandate.sectors.include)
    rows = session.execute(
        select(ConceptCoverageRow, CompanyRow)
        .join(CompanyRow, ConceptCoverageRow.company_id == CompanyRow.id)
        .where(ConceptCoverageRow.run_id == run_id)
    ).all()

    by_code: dict[str, dict] = {}
    company_status: dict[str, bool] = {}  # cid -> any AVAILABLE concept
    company_parse_failed: dict[str, bool] = {}  # cid -> any PARSE_FAILED concept
    for fact, company in rows:
        available = fact.status == CoverageStatus.AVAILABLE.value
        failed = fact.status == CoverageStatus.PARSE_FAILED.value
        company_status[company.id] = company_status.get(company.id, False) or available
        company_parse_failed[company.id] = (
            company_parse_failed.get(company.id, False) or failed
        )
        for code in company.classification_codes:
            if not sic.matches_any(str(code), include):
                continue
            bucket = by_code.setdefault(str(code), {"companies": set(), "concepts": {}})
            bucket["companies"].add(company.id)
            concept_bucket = bucket["concepts"].setdefault(fact.concept, {})
            concept_bucket[fact.status] = concept_bucket.get(fact.status, 0) + 1

    # A company whose only machine-readable documents failed to parse is
    # a system defect, not an observation about the company — it must not
    # inflate the signal-mode count (which asserts "no machine-readable
    # accounts exist"). Reported as its own bucket until the defect is
    # fixed and the company re-ingested.
    modes = {
        "financial": sum(1 for has in company_status.values() if has),
        "signal": sum(
            1
            for cid, has in company_status.items()
            if not has and not company_parse_failed.get(cid, False)
        ),
        "parse_failed": sum(
            1
            for cid, has in company_status.items()
            if not has and company_parse_failed.get(cid, False)
        ),
    }
    return {
        "run_id": run_id,
        "mandate_id": mandate.id,
        "companies_with_coverage_facts": len(company_status),
        "screening_modes": modes,
        "by_classification_code": {
            code: {
                "companies": len(bucket["companies"]),
                "concepts": {
                    concept: dict(sorted(statuses.items()))
                    for concept, statuses in sorted(bucket["concepts"].items())
                },
            }
            for code, bucket in sorted(by_code.items())
        },
    }


def run_ingest(
    client: CompaniesHouseClient,
    session_factory: Callable[[], Session],
    mandate,
    *,
    run_id: str,
    data_root: Path = Path("data"),
    config: IngestConfig = IngestConfig(),
    checkpoint_path: Path | None = None,
    incorporated_to: date | None = None,
    progress: Callable[[str], None] | None = None,
) -> dict:
    include_codes = sic.expand(list(mandate.sectors.include))
    if not include_codes:
        raise IngestError(
            f"mandate sector patterns {list(mandate.sectors.include)} expand to "
            f"zero classification codes"
        )

    cache_root = data_root / "cache"
    concept_map = ConceptMap.load()
    session = session_factory()
    say = progress or (lambda _msg: None)

    run_row = RunRow(
        run_id=run_id,
        command="ingest",
        args={"mandate": mandate.id, "limit": config.limit},
        started_at=datetime.now(timezone.utc),
    )
    if session.get(RunRow, run_id) is None:
        session.add(run_row)
        session.commit()

    checkpoint = Checkpoint.load(checkpoint_path) if checkpoint_path else None
    counts: dict[str, int] = {}
    skipped: dict[str, int] = {}
    errors: list[str] = []
    notes: dict[str, int] = {}
    stats: dict = {}
    seen: set[str] = set()
    examined = 0
    ingested = 0
    max_examined = config.limit * config.max_triage_factor

    for item in enumerate_universe(
        client,
        include_codes,
        page_size=config.search_page_size,
        window=config.search_window,
        incorporated_to=incorporated_to,
        stats=stats,
    ):
        if ingested >= config.limit or examined >= max_examined:
            break
        registration_id = str(item.get("company_number") or "")
        if not registration_id or registration_id in seen:
            continue
        seen.add(registration_id)
        if checkpoint and registration_id in checkpoint.processed:
            _bump(skipped, "checkpointed")
            continue
        examined += 1
        try:
            profile = client.get_company_profile(registration_id)
        except CompaniesHouseError as exc:
            errors.append(f"{registration_id}: profile fetch failed: {exc}")
            continue
        reason = triage(profile, mandate)
        if reason:
            _bump(skipped, reason)
            if checkpoint:
                checkpoint.mark(registration_id, f"skipped:{reason}")
            continue
        try:
            outcome = ingest_company(
                session, client, cache_root, profile, concept_map, config, run_id, counts
            )
            session.commit()
            ingested += 1
            if outcome["note"]:
                _bump(notes, outcome["note"])
            if checkpoint:
                checkpoint.mark(registration_id, "ingested")
            say(f"[{ingested}/{config.limit}] {registration_id} ingested")
        except Exception as exc:  # per-company isolation: log, continue
            session.rollback()
            errors.append(f"{registration_id}: {exc!r}")
            if checkpoint:
                checkpoint.mark(registration_id, "error")

    report = build_coverage_report(session, run_id, mandate)
    summary = {
        "run_id": run_id,
        "universe_hits": stats.get("hits", 0),
        "search_slices": stats.get("slices", 0),
        "examined": examined,
        "ingested": ingested,
        "skipped": skipped,
        "notes": notes,
        "counts": counts,
        "errors": errors,
        "coverage": report,
    }

    reports_dir = data_root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / f"coverage-{run_id}.json"
    report_path.write_text(json.dumps(summary, indent=1, default=str), encoding="utf-8")
    summary["report_path"] = report_path.as_posix()

    run_row = session.get(RunRow, run_id)
    run_row.finished_at = datetime.now(timezone.utc)
    run_row.exit_status = 0 if not errors else 1
    run_row.counts = {**counts, "ingested": ingested, "errors": len(errors)}
    session.commit()
    return summary


def run_from_env(
    env: Mapping[str, str],
    session_factory: Callable[[], Session],
    mandate,
    *,
    run_id: str,
    data_root: Path,
    limit: int = 200,
    docs_per_company: int = 3,
    checkpoint_path: Path | None = None,
    progress: Callable[[str], None] | None = None,
) -> dict:
    """The adapter-registry ingest entry point: credentials from the
    environment, canonical rows out. Core calls this through the runner
    declaration and never imports this module by name."""
    api_key = env.get("CH_API_KEY", "")
    if not api_key:
        raise IngestError("CH_API_KEY is not set in the environment")
    config = IngestConfig(limit=limit, accounts_docs_per_company=docs_per_company)
    with CompaniesHouseClient(api_key) as client:
        return run_ingest(
            client,
            session_factory,
            mandate,
            run_id=run_id,
            data_root=data_root,
            config=config,
            checkpoint_path=checkpoint_path,
            progress=progress,
        )
