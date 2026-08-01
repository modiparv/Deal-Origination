"""Officers.

Persisted as their own table, never embedded in Company: succession
detection needs appointment history and cross-ingest diffing, and the same
person holds multiple directorships. Person identity links through the
registry's officer ID, never name+DOB alone (names collide; DOB is
month/year only — the day is suppressed on the public register).
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class Officer(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    appointment_id: str  # registry-native appointment identity
    officer_id: str | None = None  # registry person link (appointments URL)
    name: str
    role: str
    appointed_on: date | None = None
    resigned_on: date | None = None
    dob_month: int | None = Field(default=None, ge=1, le=12)
    dob_year: int | None = Field(default=None, ge=1850, le=2100)
    nationality: str | None = None
    country_of_residence: str | None = None
