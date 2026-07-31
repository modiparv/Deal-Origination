"""Run records: every unattended run is logged (§3.4)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class RunRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    run_id: str
    command: str
    args: dict = Field(default_factory=dict)
    git_sha: str | None = None
    started_at: datetime
    finished_at: datetime | None = None
    exit_status: int | None = None
    counts: dict[str, int] = Field(default_factory=dict)
    cost_usd: float | None = None  # LLM spend, Phase 3 onward
