"""Derived-metric declarations.

Phase 0 declares each metric's name and required input concepts so mandate
validation can resolve `size.metric: ebitda` down to filed concepts and
check them against adapter capability matrices. Implementations — the
named, tested Python functions of §3.1 — arrive in Phase 2.

Inputs may reference other derived metrics; `resolve_required_concepts`
flattens to canonical filed concepts with cycle detection.
"""

from __future__ import annotations

from dataclasses import dataclass

from deal_engine.concepts import CONCEPTS


@dataclass(frozen=True)
class DerivedMetricDecl:
    name: str
    inputs: tuple[str, ...]  # canonical concepts or other derived metrics
    description: str


_ALL = [
    DerivedMetricDecl(
        "ebitda",
        ("operating_profit", "depreciation_amortisation"),
        "Operating profit plus depreciation, amortisation and impairment. "
        "Only computable where a P&L was filed; never a tagged concept.",
    ),
    DerivedMetricDecl(
        "ebitda_margin",
        ("ebitda", "revenue"),
        "EBITDA over revenue.",
    ),
    DerivedMetricDecl(
        "revenue_growth",
        ("revenue",),
        "Period-on-period revenue growth; refuses to compare periods of "
        "materially different lengths.",
    ),
    DerivedMetricDecl(
        "gearing",
        ("creditors_after_one_year", "equity"),
        "Long-term creditors over equity.",
    ),
    DerivedMetricDecl(
        "working_capital_movement",
        ("current_assets", "creditors_within_one_year"),
        "Movement in (current assets less current creditors) between periods.",
    ),
]

DERIVED_METRICS: dict[str, DerivedMetricDecl] = {m.name: m for m in _ALL}


def resolve_required_concepts(metric: str) -> frozenset[str]:
    """Flatten a derived metric to the canonical concepts it needs.

    Raises KeyError for an unknown metric and ValueError on a declaration
    cycle.
    """
    if metric not in DERIVED_METRICS:
        raise KeyError(
            f"unknown derived metric {metric!r}; known: {sorted(DERIVED_METRICS)}"
        )
    required: set[str] = set()
    in_progress: set[str] = set()

    def walk(name: str) -> None:
        if name in CONCEPTS:
            required.add(name)
            return
        if name in in_progress:
            raise ValueError(f"cycle in derived-metric declarations at {name!r}")
        decl = DERIVED_METRICS.get(name)
        if decl is None:
            raise KeyError(
                f"derived metric input {name!r} is neither a canonical concept "
                f"nor a declared derived metric"
            )
        in_progress.add(name)
        for inp in decl.inputs:
            walk(inp)
        in_progress.discard(name)

    walk(metric)
    return frozenset(required)
