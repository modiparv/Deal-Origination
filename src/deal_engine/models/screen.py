"""Screening results and rubric scores (populated Phases 2–3).

Mode-awareness contract: a rubric dimension whose required screening
mode is unavailable for a company is SKIPPED, and the skip is recorded on
the Score row (never silently absent). The composite over the dimensions
that ran is renormalised and carries `renormalised=True` — a partial
score must never render as a complete one.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator

from deal_engine.models.common import ScreenOutcome


class ScreenResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    mandate_id: str
    stage: str
    outcome: ScreenOutcome
    failed_criteria: list[str] = Field(default_factory=list)
    run_id: str


class Score(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    mandate_id: str
    rubric_dimension: str
    score: float | None = None
    rationale: str
    figure_ids_cited: list[str] = Field(default_factory=list)  # what makes a score auditable
    skipped: bool = False  # dimension's required mode unavailable for this company
    skip_reason: str | None = None
    run_id: str

    @model_validator(mode="after")
    def _skip_consistency(self) -> "Score":
        if self.skipped:
            if self.score is not None:
                raise ValueError("skipped dimension must not carry a score value")
            if not self.skip_reason:
                raise ValueError("skipped dimension requires a skip_reason")
        elif self.score is None:
            raise ValueError("non-skipped dimension requires a score value")
        return self


class CompositeScore(BaseModel):
    """The weighted composite over the dimensions that actually ran."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    mandate_id: str
    value: float
    renormalised: bool = False  # True whenever any dimension was skipped
    dimensions_run: list[str] = Field(default_factory=list)
    dimensions_skipped: list[str] = Field(default_factory=list)
    run_id: str

    @model_validator(mode="after")
    def _renormalisation_flagged(self) -> "CompositeScore":
        if self.dimensions_skipped and not self.renormalised:
            raise ValueError(
                "composite with skipped dimensions must be flagged renormalised — "
                "a partial score must never render as a complete one"
            )
        if not self.dimensions_run:
            raise ValueError("composite requires at least one dimension that ran")
        return self
