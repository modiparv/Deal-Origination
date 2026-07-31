"""Signal detector declarations.

Standing rule (decision record §4): signals are named after what is
*observed*, never after what is inferred. A registered security is not a
debt raise; there is no public field for a "successor". Each declaration
records the specific observation backing the signal so a profile can show
why a company was flagged rather than asserting the conclusion.

Detector implementations arrive in Phase 2; Phase 0 declares names and
parameter schemas so mandate validation can reject unknown signals and
malformed parameters.
"""

from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, Field


class _Params(BaseModel):
    model_config = ConfigDict(extra="forbid")


class NoYoungerDirector(_Params):
    age_below: int = Field(ge=18, le=100)
    within_years: int = Field(ge=1, le=50)


class SuccessionRiskParams(_Params):
    """Age keyed on individual PSCs holding a control band — the owner's
    age is the buyout-relevant one, not any director's. The no-younger-
    director rule is an explicitly named heuristic with known failure
    modes (non-board successors are invisible by design)."""

    psc_age_threshold: int = Field(ge=18, le=100)
    no_younger_director_appointed: NoYoungerDirector | None = None


class NewSecurityRegisteredParams(_Params):
    """Observes charge registrations only: no amounts (post-2013 charges
    state none), secured lending only, lender may be a security agent."""

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
            "Individual PSC with a control band aged at or above the threshold "
            "(DOB month/year from the register), optionally with no younger "
            "director appointed within the stated window.",
        ),
        SignalDecl(
            "new_security_registered",
            NewSecurityRegisteredParams,
            "Charge registered within the lookback window with status "
            "outstanding, minus refinance patterns and excluded lender "
            "categories.",
        ),
    ]
}
