"""Screening results and rubric scores (populated Phases 2–3).

Absence carries a cause. A dimension without a value records WHY on the
Score row via `state` (`not_observable` / `skipped_mode` / `not_reached`)
plus a human-readable `state_reason` — a blank cell in an export must be
distinguishable between a coverage gap, a mode skip, and a deliberate
earlier-stage exclusion. The composite over the dimensions that actually
scored is renormalised and carries `renormalised=True` — a partial score
must never render as a complete one.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator

from deal_engine.models.common import ScoreState, ScreenOutcome


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
    state: ScoreState = ScoreState.SCORED
    score: float | None = None
    rationale: str
    figure_ids_cited: list[str] = Field(default_factory=list)  # what makes a score auditable
    state_reason: str | None = None  # required whenever state != scored
    run_id: str

    @model_validator(mode="after")
    def _state_consistency(self) -> "Score":
        if self.state is ScoreState.SCORED:
            if self.score is None:
                raise ValueError("scored dimension requires a score value")
        else:
            if self.score is not None:
                raise ValueError(
                    f"dimension in state {self.state.value!r} must not carry a "
                    f"score value"
                )
            if not self.state_reason:
                raise ValueError(
                    f"dimension in state {self.state.value!r} requires a "
                    f"state_reason — absence carries a cause"
                )
        return self


class CompositeScore(BaseModel):
    """The weighted composite over the dimensions that actually scored.

    Per-dimension absence causes live on the Score rows; the composite
    records which dimensions contributed and which did not, and must be
    flagged renormalised whenever any dimension is missing.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    mandate_id: str
    value: float
    renormalised: bool = False  # True whenever any dimension did not score
    dimensions_scored: list[str] = Field(default_factory=list)
    dimensions_not_scored: list[str] = Field(default_factory=list)
    run_id: str

    @model_validator(mode="after")
    def _renormalisation_flagged(self) -> "CompositeScore":
        if self.dimensions_not_scored and not self.renormalised:
            raise ValueError(
                "composite with unscored dimensions must be flagged renormalised "
                "— a partial score must never render as a complete one"
            )
        if not self.dimensions_scored:
            raise ValueError("composite requires at least one scored dimension")
        return self
