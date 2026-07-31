"""Persons with significant control — records, statements, exemptions.

Natures of control are stored verbatim as the registry's enum strings.
Ownership exists only as bands (25–50 / 50–75 / 75–100): the schema never
models a numeric percentage, because none exists in the data and any
number would be fabricated.

Parser note (Phase 1): Companies House's canonical statement enum key
misspells "significant" — `no-individual-or-entity-with-signficant-control`
— and the charges list misspells `unfiletered_count`. Store verbatim,
match tolerantly.
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class PscRecord(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    psc_id: str
    kind: str  # registry kind string, verbatim
    name: str | None = None
    name_elements: dict[str, str] = Field(default_factory=dict)
    natures_of_control: list[str] = Field(default_factory=list)  # verbatim enum strings
    notified_on: date | None = None
    ceased_on: date | None = None
    dob_month: int | None = Field(default=None, ge=1, le=12)
    dob_year: int | None = Field(default=None, ge=1850, le=2100)
    identification: dict[str, str] = Field(default_factory=dict)  # corporate PSCs


class PscStatement(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    statement: str  # verbatim enum string, misspellings included
    notified_on: date | None = None
    ceased_on: date | None = None


class Exemption(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    exemption_type: str  # near-definitive "listed" marker
    items: list[dict] = Field(default_factory=list)
