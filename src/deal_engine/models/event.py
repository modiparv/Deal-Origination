"""Events: a deterministic, idempotent projection of sourced records.

Every event resolves to the filing-history transaction or source document
it was projected from — an event with neither cannot exist. Restatement
events carry a materiality classification (rounding / reclassification /
genuine) so a £1 rounding delta never shares a table's meaning with a
restated prior-year figure.
"""

from __future__ import annotations

from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class EventType(str, Enum):
    SECURITY_INTEREST_REGISTERED = "security_interest_registered"
    SECURITY_INTEREST_SATISFIED = "security_interest_satisfied"
    OFFICER_APPOINTED = "officer_appointed"
    OFFICER_RESIGNED = "officer_resigned"
    AUDITOR_RESIGNED = "auditor_resigned"
    FILING_LATE = "filing_late"
    FISCAL_PERIOD_END_CHANGED = "fiscal_period_end_changed"
    NAME_CHANGED = "name_changed"
    INSOLVENCY_CASE = "insolvency_case"
    RESTATEMENT = "restatement"


class Event(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    event_type: EventType
    event_date: date
    transaction_id: str | None = None
    source_document_id: str | None = None
    payload: dict = Field(default_factory=dict)

    @model_validator(mode="after")
    def _sourced(self) -> "Event":
        if self.transaction_id is None and self.source_document_id is None:
            raise ValueError(
                "event requires a transaction_id or source_document_id — events "
                "are projections of sourced records, never free-standing"
            )
        return self
