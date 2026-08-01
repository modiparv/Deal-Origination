"""Beneficial ownership — records, statements, exemptions.

Control natures are stored verbatim as the registry's own enum strings:
neutral column names, adapter-native values. Ownership interest exists
only as whatever bands or forms the registry publishes — the schema
never models a numeric percentage, because none exists in the data and
any number would be fabricated.

Registry-specific structure (kinds, statement vocabularies, known
misspellings in canonical enum keys) is documented and mapped in the
owning adapter, never here.
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class BeneficialOwner(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    external_id: str  # registry-native record identity
    kind: str  # registry kind string, verbatim (individual / corporate / ...)
    name: str | None = None
    name_elements: dict[str, str] = Field(default_factory=dict)
    control_natures: list[str] = Field(default_factory=list)  # verbatim enum strings
    notified_on: date | None = None
    ceased_on: date | None = None
    dob_month: int | None = Field(default=None, ge=1, le=12)
    dob_year: int | None = Field(default=None, ge=1850, le=2100)
    identification: dict[str, str] = Field(default_factory=dict)  # corporate owners


class OwnershipStatement(BaseModel):
    """A registry statement about beneficial ownership (e.g. "no
    identifiable controller", "steps not yet completed"). Stored verbatim;
    the classifier must see these — a company whose controller filed an
    opaque statement is `unclassifiable`, never `independent`."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    statement: str  # verbatim registry enum string
    notified_on: date | None = None
    ceased_on: date | None = None


class Exemption(BaseModel):
    """A registry exemption from ownership disclosure — typically because
    the company is listed on a regulated market; a near-definitive listed
    marker."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    exemption_type: str
    items: list[dict] = Field(default_factory=list)
