"""Raw filing-history rows.

Stored verbatim, keyed by the registry transaction ID. Two things depend
on this table: incremental refresh (diff transaction IDs against the live
filing history, fetch only what is new) and the Event stream, which is a
deterministic projection of these rows — never independently written, so
the two cannot drift.

Categories, types and descriptions are adapter-native strings stored in
neutral columns; core never validates them against a registry's
documented enum (registries' published enums are routinely incomplete —
the owning adapter documents the specifics).
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class FilingRecord(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    transaction_id: str
    category: str | None = None
    subcategory: str | None = None
    type: str | None = None  # registry form code, verbatim
    date: date | None = None
    description: str | None = None
    description_values: dict[str, str] = Field(default_factory=dict)
    document_id: str | None = None  # parsed from links.document_metadata
    paper_filed: bool | None = None
