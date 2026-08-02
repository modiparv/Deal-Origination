"""Source documents: immutable once written.

The fetch/lookup key is the adapter-native document identity
`(adapter, external_document_id)`; how that identity is derived from the
registry is the adapter's business. `content_hash` is computed after
fetch and serves integrity verification and change detection only: if
refetching the same document ID ever yields a different hash, alert
loudly rather than overwrite.

`document_type` and `account_type` carry adapter-native values in
neutral columns: core never branches on local document-type names.
Concept availability (e.g. "no income statement published for this
period") is expressed through the capability matrix's conditions over
these values — a coverage fact, not a document-type vocabulary in core.
"""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from deal_engine.models.common import ParseStatus


class SourceDocument(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    adapter: str
    jurisdiction: str
    company_id: str
    external_document_id: str
    transaction_id: str | None = None
    document_type: str  # adapter-native filing type label
    account_type: str | None = None  # adapter-native accounts regime; coverage-condition input
    filed_date: date | None = None
    period_start: date | None = None
    period_end: date | None = None
    retrieved_at: datetime
    content_type: str | None = None
    raw_path: str | None = None  # content-addressed: data/cache/sha256/ab/abcd...
    content_hash: str | None = None
    fetch_headers: dict[str, str] = Field(default_factory=dict)
    parse_status: ParseStatus = ParseStatus.PENDING
    parse_error_count: int = 0
    # Document self-description: which software produced the filing, as
    # tagged in the filing itself. Every parse defect found so far has
    # clustered by product, so the coverage report breaks parse yield
    # down by this field — a product silently yielding zero figures must
    # be visible without a cluster investigation.
    production_software: str | None = None
