"""Company and ownership assessment."""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field, model_validator

from deal_engine.models.common import OwnershipClass


class OwnershipAssessment(BaseModel):
    """Ownership classification with its evidence.

    Never a bare label: classification + confidence + the record IDs the
    rules engine cited. `unclassifiable` is a legitimate value, and
    exclusion mandates treat it fail-closed.

    Stated explicitly, per the decision record: ABSENCE OF A PSC STATEMENT
    IS NOT EVIDENCE OF INDEPENDENCE. Sponsor-held topcos routinely file
    no-PSC or opaque-PSC statements because control sits in an LP or an
    overseas entity. A company with no resolvable controller classifies as
    `unclassifiable`, never as `independent`.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    classification: OwnershipClass
    confidence: float = Field(ge=0.0, le=1.0)
    evidence: list[str] = Field(default_factory=list)  # PSC/officer/charge record IDs

    @model_validator(mode="after")
    def _evidence_required(self) -> "OwnershipAssessment":
        if self.classification is not OwnershipClass.UNCLASSIFIABLE and not self.evidence:
            raise ValueError(
                f"classification {self.classification.value!r} requires evidence; "
                f"only 'unclassifiable' may stand without it"
            )
        return self


class Company(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    jurisdiction: str
    company_number: str
    name: str
    name_variants: list[str] = Field(default_factory=list)
    incorporation_date: date | None = None
    status: str | None = None
    sic_codes: list[str] = Field(default_factory=list)
    registered_address: dict[str, str] = Field(default_factory=dict)
    ownership: OwnershipAssessment | None = None
