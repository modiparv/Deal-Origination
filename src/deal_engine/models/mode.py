"""Screening modes: how a company can be screened, resolved per company.

FINANCIAL — filed statements exist and are machine-readable; screening
runs on reported financials.

SIGNAL — no usable filed financials; screening runs on observable
behaviour: headcount, hiring, registration events, funding events,
infrastructure footprint, leadership movement.

Mode is a per-company property, never a per-mandate or per-jurisdiction
one: two companies in the same jurisdiction under the same mandate can
resolve to different modes depending on what their filings actually
contain. Mandates declare which modes satisfy them (`required_modes` —
any one suffices); rubric dimensions declare which mode they need
(`requires_mode`). The scorer skips dimensions whose mode is unavailable
for a company, records the skip on the Score row, and renormalises the
composite over the dimensions that ran — a renormalised composite is
flagged and must never render as a complete one.

Phase 2 implements the per-company resolver (from concept availability
per the capability matrix); this module fixes the contract.

Deliberately dependency-free: enums only, importable everywhere.
"""

from __future__ import annotations

from enum import Enum


class ScreeningMode(str, Enum):
    FINANCIAL = "financial"
    SIGNAL = "signal"


class ModeRequirement(str, Enum):
    """What a rubric dimension needs: a specific mode, or any."""

    FINANCIAL = "financial"
    SIGNAL = "signal"
    ANY = "any"


def mode_satisfied(requirement: ModeRequirement, available: set[ScreeningMode]) -> bool:
    if requirement is ModeRequirement.ANY:
        return True
    return ScreeningMode(requirement.value) in available
