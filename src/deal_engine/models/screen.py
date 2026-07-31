"""Screening results and rubric scores (populated Phases 2–3)."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

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
    score: float
    rationale: str
    figure_ids_cited: list[str] = Field(default_factory=list)  # what makes a score auditable
    run_id: str
