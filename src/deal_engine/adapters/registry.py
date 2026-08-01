"""Registry of enabled adapters: capability declarations and runners.

Mandate validation reads the capability declarations; the CLI resolves
ingest runners by jurisdiction. Adapter implementations register here as
they are built. Declarations exist from Phase 0, implementations from
their phase — that asymmetry is deliberate (it breaks the circularity of
validating mandates against adapters that do not exist yet).

Runner loading is lazy: importing this registry must never pull in an
adapter's HTTP client or parser stack, so declaration-only consumers
(validation, tests) stay dependency-light.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from deal_engine.adapters.base import CapabilityMatrix
from deal_engine.adapters.companies_house_decl import COMPANIES_HOUSE_CAPABILITIES

ENABLED_ADAPTERS: dict[str, CapabilityMatrix] = {
    COMPANIES_HOUSE_CAPABILITIES.adapter: COMPANIES_HOUSE_CAPABILITIES,
}


def matrices_for_jurisdiction(jurisdiction: str) -> list[CapabilityMatrix]:
    return [
        m for m in ENABLED_ADAPTERS.values() if m.covers_jurisdiction(jurisdiction)
    ]


@dataclass(frozen=True)
class IngestRunnerDecl:
    """A registered ingest implementation.

    `required_env` names the credential variables the runner needs, so
    core can fail closed with a precise message without knowing any
    registry's vocabulary. `load` imports the implementation on demand.
    """

    adapter: str
    jurisdictions: frozenset[str]
    required_env: tuple[str, ...]
    load: Callable[[], Callable]
    load_refresh: Callable[[], Callable] | None = None


def _load_companies_house_runner() -> Callable:
    from deal_engine.adapters.companies_house.pipeline import run_from_env

    return run_from_env


def _load_companies_house_refresh() -> Callable:
    from deal_engine.adapters.companies_house.refresh import refresh_from_env

    return refresh_from_env


INGEST_RUNNERS: tuple[IngestRunnerDecl, ...] = (
    IngestRunnerDecl(
        adapter=COMPANIES_HOUSE_CAPABILITIES.adapter,
        jurisdictions=COMPANIES_HOUSE_CAPABILITIES.jurisdictions,
        required_env=("CH_API_KEY",),
        load=_load_companies_house_runner,
        load_refresh=_load_companies_house_refresh,
    ),
)


def ingest_runner_for(jurisdictions: set[str]) -> IngestRunnerDecl | None:
    """First registered runner covering any wanted jurisdiction (one
    adapter per jurisdiction until adapter #2 exists)."""
    for runner in INGEST_RUNNERS:
        if runner.jurisdictions & jurisdictions:
            return runner
    return None
