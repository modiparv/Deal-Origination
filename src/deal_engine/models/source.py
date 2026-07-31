"""Source documents: immutable once written.

The fetch/lookup key is the adapter-native document identity
`(adapter, external_document_id)` — for Companies House, the document ID
from the filing-history item's `links.document_metadata` URL.
`content_hash` is computed after fetch and serves integrity verification
and change detection only: if refetching the same document ID ever yields
a different hash, alert loudly rather than overwrite.
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
    document_type: str
    account_type: str | None = None  # per-filing size regime; the coverage-cliff marker
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
