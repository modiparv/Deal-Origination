"""Repository layer: domain models in, rows out — and provenance walking.

Provenance is enforced at two layers (decision record §7): the Pydantic
model validators and the database CHECK constraints. There is no pre-flush
listener; if bulk inserts that bypass ORM validation are ever introduced,
it returns with them.
"""

from __future__ import annotations

from deal_engine.models.common import Basis
from deal_engine.db.tables import FigureRow, SourceDocumentRow
from deal_engine.models.figure import Figure
from deal_engine.models.source import SourceDocument

from sqlalchemy import select
from sqlalchemy.orm import Session


class ProvenanceError(Exception):
    """A figure's provenance chain is broken."""


class ProvenanceCycleError(ProvenanceError):
    """Derivation inputs form a cycle."""


def add_source_document(session: Session, doc: SourceDocument) -> SourceDocumentRow:
    row = SourceDocumentRow(
        id=doc.id,
        adapter=doc.adapter,
        jurisdiction=doc.jurisdiction,
        company_id=doc.company_id,
        external_document_id=doc.external_document_id,
        transaction_id=doc.transaction_id,
        document_type=doc.document_type,
        account_type=doc.account_type,
        filed_date=doc.filed_date,
        period_start=doc.period_start,
        period_end=doc.period_end,
        retrieved_at=doc.retrieved_at,
        content_type=doc.content_type,
        raw_path=doc.raw_path,
        content_hash=doc.content_hash,
        fetch_headers=dict(doc.fetch_headers),
        parse_status=doc.parse_status.value,
        parse_error_count=doc.parse_error_count,
    )
    session.add(row)
    return row


def add_figure(session: Session, figure: Figure) -> FigureRow:
    """Persist a validated Figure.

    The Figure model has already enforced the provenance rules; the row
    mapping is mechanical, and the DB CHECK constraints back the same
    rules for any write path that skips the model.
    """
    row = FigureRow(
        id=figure.id,
        company_id=figure.company_id,
        concept=figure.concept,
        value=figure.value,
        unit=figure.unit,
        currency=figure.currency,
        period_type=figure.period_type.value,
        period_start=figure.period_start,
        period_end=figure.period_end,
        dimensions=dict(figure.dimensions),
        dimensions_hash=figure.dimensions_hash,
        consolidation=figure.consolidation.value,
        decimals=figure.decimals,
        raw_text=figure.raw_text,
        basis=figure.basis.value,
        source_document_id=figure.source_document_id,
        source_tag=figure.source_tag,
        derivation_function=figure.derivation.function if figure.derivation else None,
        derivation_inputs=list(figure.derivation.inputs) if figure.derivation else None,
        model_run_id=figure.model_run_id,
        aggregator_ref=figure.aggregator_ref,
        is_current=figure.is_current,
    )
    session.add(row)
    return row


def provenance_walk(session: Session, figure_id: str) -> set[str]:
    """Resolve a figure to the set of source document IDs backing it.

    Filed figures contribute their document; derived figures recurse
    through their inputs; modelled and unverified figures terminate the
    walk contributing nothing. Detects cycles and missing inputs, failing
    loudly rather than recursing forever or returning a partial answer.
    """
    documents: set[str] = set()
    resolved: set[str] = set()
    in_stack: list[str] = []

    def walk(fid: str) -> None:
        if fid in resolved:
            return
        if fid in in_stack:
            chain = " -> ".join([*in_stack, fid])
            raise ProvenanceCycleError(f"derivation cycle: {chain}")
        row = session.get(FigureRow, fid)
        if row is None:
            raise ProvenanceError(
                f"figure {fid!r} referenced in a derivation does not exist"
            )
        in_stack.append(fid)
        try:
            basis = Basis(row.basis)
            if basis is Basis.FILED:
                if row.source_document_id is None:
                    raise ProvenanceError(
                        f"filed figure {fid!r} has no source document (schema "
                        f"constraint should have prevented this)"
                    )
                documents.add(row.source_document_id)
            elif basis is Basis.DERIVED:
                inputs = row.derivation_inputs or []
                if not inputs:
                    raise ProvenanceError(
                        f"derived figure {fid!r} has no recorded inputs"
                    )
                for inp in inputs:
                    walk(inp)
        finally:
            in_stack.pop()
        resolved.add(fid)

    walk(figure_id)
    return documents


def validate_provenance(session: Session) -> list[str]:
    """The DoD #3 validator: every persisted figure must walk cleanly.

    Returns human-readable violation strings; empty means the store is
    provenance-complete (zero figures without a source, zero derived
    figures without recorded inputs, all source documents present).
    """
    violations: list[str] = []
    for (fid,) in session.execute(select(FigureRow.id)):
        try:
            docs = provenance_walk(session, fid)
        except ProvenanceError as exc:
            violations.append(str(exc))
            continue
        for doc_id in docs:
            if session.get(SourceDocumentRow, doc_id) is None:
                violations.append(
                    f"figure {fid!r} cites missing source document {doc_id!r}"
                )
    return violations
