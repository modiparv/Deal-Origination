"""Signal detector declarations.

Standing rule (decision record §4): signals are named after what is
*observed*, never after what is inferred. A registered security interest
is not a debt raise; there is no filed concept of a "successor". Each
declaration records the specific observation backing the signal so a
profile can show why a company was flagged rather than asserting the
conclusion.

Detector implementations arrive in Phase 2; Phase 0 declares names and
parameter schemas so mandate validation can reject unknown signals and
malformed parameters. Registry-specific detection mechanics live with
the owning adapter.
"""

from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, Field


class _Params(BaseModel):
    model_config = ConfigDict(extra="forbid")


class NoYoungerOfficer(_Params):
    age_below: int = Field(ge=18, le=100)
    within_years: int = Field(ge=1, le=50)


class SuccessionRiskParams(_Params):
    """Age keyed on individual beneficial owners holding a control
    interest — the owner's age is the buyout-relevant one, not any
    officer's. Ages derive from registry-published birth data (often
    month/year granularity). The no-younger-officer rule is an explicitly
    named heuristic with known failure modes: successors not yet
    appointed to the board are invisible by design."""

    beneficial_owner_age_threshold: int = Field(ge=18, le=100)
    no_younger_officer_appointed: NoYoungerOfficer | None = None


class NewSecurityRegisteredParams(_Params):
    """Observes registered security interests only: registered
    particulars commonly omit secured amounts, unsecured borrowing never
    appears, and the named secured party may be an agent rather than the
    economic lender."""

    lookback_months: int = Field(ge=1, le=120)
    exclude_refinance: bool = True
    exclude_lender_categories: list[str] = Field(default_factory=list)


@dataclass(frozen=True)
class SignalDecl:
    name: str
    params_model: type[_Params]
    observation: str  # what is actually observed, verbatim in profiles


SIGNALS: dict[str, SignalDecl] = {
    s.name: s
    for s in [
        SignalDecl(
            "succession_risk",
            SuccessionRiskParams,
            "Individual beneficial owner with a control interest aged at or "
            "above the threshold (registry-published birth data), optionally "
            "with no younger officer appointed within the stated window.",
        ),
        SignalDecl(
            "new_security_registered",
            NewSecurityRegisteredParams,
            "Security interest registered within the lookback window and "
            "still outstanding, minus refinance patterns and excluded "
            "lender categories.",
        ),
    ]
}
