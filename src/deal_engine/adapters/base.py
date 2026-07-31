"""Adapter protocol and capability matrix.

The capability matrix is a *static declaration*, importable without any
adapter implementation or live API — this is what lets Phase 0 mandate
validation run against adapters that are not built yet.

Coverage is tiered, not boolean: concept availability in the UK is a
per-company property (a filleted small company files no P&L), so a
`CONDITIONAL` tier carries a machine-readable condition the coverage
report can evaluate per company before ingest.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, Mapping, Protocol


class CoverageTier(str, Enum):
    ALWAYS = "always"
    CONDITIONAL = "conditional"
    NEVER = "never"


@dataclass(frozen=True)
class Condition:
    """Machine-readable availability condition: `field` must be in `allowed`."""

    field: str
    allowed: frozenset[str]

    def describe(self) -> str:
        return f"{self.field} in {{{', '.join(sorted(self.allowed))}}}"

    def evaluate(self, record: Mapping[str, object]) -> bool:
        return record.get(self.field) in self.allowed


@dataclass(frozen=True)
class ConceptCoverage:
    tier: CoverageTier
    condition: Condition | None = None

    def __post_init__(self) -> None:
        if self.tier is CoverageTier.CONDITIONAL and self.condition is None:
            raise ValueError("CONDITIONAL coverage requires a condition")
        if self.tier is not CoverageTier.CONDITIONAL and self.condition is not None:
            raise ValueError(f"{self.tier.value} coverage must not carry a condition")


NEVER = ConceptCoverage(CoverageTier.NEVER)


@dataclass(frozen=True)
class CapabilityMatrix:
    adapter: str
    jurisdictions: frozenset[str]
    coverage: Mapping[str, ConceptCoverage] = field(default_factory=dict)

    def concept_coverage(self, concept: str) -> ConceptCoverage:
        return self.coverage.get(concept, NEVER)

    def covers_jurisdiction(self, jurisdiction: str) -> bool:
        return jurisdiction in self.jurisdictions


class Adapter(Protocol):
    """Interface each registry adapter implements (Phase 1 onward).

    Signatures are deliberately minimal in Phase 0; the Companies House
    adapter refines them against the verified live API surface.
    """

    name: str
    capability_matrix: CapabilityMatrix

    def enumerate_universe(self, sic_codes: Iterable[str], status: str) -> Iterable[str]:
        """Yield registry company identifiers matching the filters."""
        ...

    def ingest_company(self, company_number: str) -> None:
        """Fetch, cache and persist one company's records and documents."""
        ...
