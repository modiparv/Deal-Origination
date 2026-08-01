"""Concept coverage facts: absence carries a cause.

One row per (run, company, concept, period): either the concept was
available, or it was not — and if not, WHY, with the causes kept
distinct (see CoverageStatus). The coverage report is an aggregation of
these rows, and a `parse_failed` row is a system defect surfaced as
data, never silently folded into "unavailable".

Populated by ingest from Phase 1 onward; the schema and its invariants
are fixed here so Phase 1 cannot write cause-less absence.
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, model_validator

from deal_engine.concepts import CONCEPTS
from deal_engine.models.common import CoverageStatus


class ConceptCoverageFact(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    concept: str
    period_end: date
    status: CoverageStatus
    # The document examined; null only when there was nothing to examine.
    source_document_id: str | None = None
    detail: str | None = None  # e.g. parse error summary for parse_failed
    run_id: str

    @model_validator(mode="after")
    def _check(self) -> "ConceptCoverageFact":
        if self.concept not in CONCEPTS:
            raise ValueError(f"unknown canonical concept {self.concept!r}")
        if self.status is CoverageStatus.NOT_FILED:
            if self.source_document_id is not None:
                raise ValueError(
                    "not_filed means no document exists for the period; a "
                    "document reference contradicts that"
                )
        elif self.source_document_id is None:
            raise ValueError(
                f"status {self.status.value!r} refers to a document that was "
                f"examined; source_document_id is required"
            )
        if self.status is CoverageStatus.PARSE_FAILED and not self.detail:
            raise ValueError(
                "parse_failed is a system defect and requires detail — it must "
                "never be indistinguishable from a data limitation"
            )
        return self
