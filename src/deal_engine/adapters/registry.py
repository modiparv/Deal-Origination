"""Registry of enabled adapters' capability declarations.

Mandate validation reads this; adapter implementations register here as
they are built. Declarations exist from Phase 0, implementations from
their phase — that asymmetry is deliberate (it breaks the circularity of
validating mandates against adapters that do not exist yet).
"""

from __future__ import annotations

from deal_engine.adapters.base import CapabilityMatrix
from deal_engine.adapters.companies_house_decl import COMPANIES_HOUSE_CAPABILITIES

ENABLED_ADAPTERS: dict[str, CapabilityMatrix] = {
    COMPANIES_HOUSE_CAPABILITIES.adapter: COMPANIES_HOUSE_CAPABILITIES,
}


def matrices_for_jurisdiction(jurisdiction: str) -> list[CapabilityMatrix]:
    return [
        m for m in ENABLED_ADAPTERS.values() if m.covers_jurisdiction(jurisdiction)
    ]
