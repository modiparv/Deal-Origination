"""Jurisdiction profiles: per-jurisdiction facts as configuration.

Everything a registry jurisdiction is — which screening modes it can
support, how registration identifiers are shaped, which classification
taxonomy applies, what gets filed and how stale it arrives, and the
known caveats — lives in a YAML profile under ``jurisdictions/``, not in
code. Core modules read profiles; only adapters know local terminology.

The mandate validator reads these profiles alongside adapter capability
matrices: a mandate over a jurisdiction with no profile, or requiring a
screening mode the profile does not offer, fails validation with the
jurisdiction and reason named.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator

from deal_engine.models.mode import ScreeningMode

DEFAULT_PROFILE_DIR = Path("jurisdictions")


class RegistrationIdSpec(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    pattern: str  # anchored regex for the registry's identifier format
    description: str

    @field_validator("pattern")
    @classmethod
    def _compiles(cls, v: str) -> str:
        re.compile(v)
        return v


class FilingSpec(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    type: str  # neutral name, e.g. "annual_accounts", "ownership_declaration"
    cadence: str  # e.g. "annual"
    availability_lag_months: float | None = None  # deadline after period end


class FilingLag(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    min_months: float
    max_months: float


class JurisdictionProfile(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str = Field(pattern=r"^[A-Z]{2}$")
    name: str
    available_modes: list[ScreeningMode] = Field(min_length=1)
    registration_id: RegistrationIdSpec
    classification_taxonomy: str
    currency: str
    statutory_filings: list[FilingSpec] = Field(default_factory=list)
    filing_lag: FilingLag | None = None  # typical staleness of filed data
    caveats: list[str] = Field(default_factory=list)

    def validate_registration_id(self, value: str) -> bool:
        return re.fullmatch(self.registration_id.pattern, value) is not None


class JurisdictionLoadError(Exception):
    pass


def load_jurisdictions(
    profile_dir: Path | str = DEFAULT_PROFILE_DIR,
) -> dict[str, JurisdictionProfile]:
    """Load every profile in the directory, keyed by jurisdiction id.

    A missing directory yields an empty mapping — the validator then
    rejects every jurisdiction as unprofiled, which is the fail-loud
    behaviour we want rather than a crash at import time.
    """
    profile_dir = Path(profile_dir)
    profiles: dict[str, JurisdictionProfile] = {}
    if not profile_dir.is_dir():
        return profiles
    for path in sorted(profile_dir.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            profile = JurisdictionProfile.model_validate(data)
        except Exception as exc:
            raise JurisdictionLoadError(f"invalid jurisdiction profile {path}: {exc}") from exc
        if profile.id in profiles:
            raise JurisdictionLoadError(f"duplicate jurisdiction profile for {profile.id!r}")
        profiles[profile.id] = profile
    return profiles
