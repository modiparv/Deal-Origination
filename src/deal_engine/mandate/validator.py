"""Semantic mandate validation against static declarations.

Reads two kinds of declaration: jurisdiction profiles (what a
jurisdiction is — modes, taxonomy, identifier format) and adapter
capability matrices (what an adapter can supply). Produces a report of
issues with two severities:

- ERROR: the mandate cannot run — a jurisdiction with no profile, a
  required screening mode the profile does not offer, an unknown
  taxonomy or signal, malformed parameters, a jurisdiction no enabled
  adapter covers, a size metric whose required concepts no adapter
  supplies for a jurisdiction, or an unobservable metric not explicitly
  declared modelled.
- WARNING: the mandate runs with recorded coverage gaps — e.g. a metric
  whose inputs are only conditionally available, with the
  machine-readable condition attached so the coverage report can predict
  observability before ingest.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from pydantic import ValidationError

from deal_engine.adapters.base import CapabilityMatrix, CoverageTier
from deal_engine.adapters.registry import ENABLED_ADAPTERS
from deal_engine.concepts import CONCEPTS
from deal_engine.derive.registry import DERIVED_METRICS, resolve_required_concepts
from deal_engine.jurisdiction import (
    DEFAULT_PROFILE_DIR,
    JurisdictionProfile,
    load_jurisdictions,
)
from deal_engine.models.mandate import Mandate, SizeMetricSpec
from deal_engine.signals.registry import SIGNALS

_SECTOR_CODE_RE = re.compile(r"^\d{1,5}\*?$")
_WEIGHT_TOLERANCE = 1e-6


class Severity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True)
class Issue:
    severity: Severity
    code: str
    message: str
    data: dict = field(default_factory=dict)  # machine-readable payload


@dataclass
class ValidationReport:
    issues: list[Issue] = field(default_factory=list)

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity is Severity.ERROR]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity is Severity.WARNING]

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_mandate(
    mandate: Mandate,
    adapters: dict[str, CapabilityMatrix] | None = None,
    jurisdictions: dict[str, JurisdictionProfile] | None = None,
    profile_dir: Path | str = DEFAULT_PROFILE_DIR,
) -> ValidationReport:
    matrices = list((adapters if adapters is not None else ENABLED_ADAPTERS).values())
    profiles = jurisdictions if jurisdictions is not None else load_jurisdictions(profile_dir)
    report = ValidationReport()

    _check_rubric(mandate, report)
    _check_thresholds(mandate, report)
    _check_sectors(mandate, profiles, report)
    _check_ownership(mandate, report)
    _check_signals(mandate, report)
    _check_geography(mandate, matrices, profiles, report)
    _check_size_metric(mandate, mandate.size.primary, "size.primary", matrices, report)
    if mandate.size.secondary is not None:
        _check_size_metric(mandate, mandate.size.secondary, "size.secondary", matrices, report)
    return report


def _check_rubric(mandate: Mandate, report: ValidationReport) -> None:
    total = sum(d.weight for d in mandate.rubric)
    if abs(total - 1.0) > _WEIGHT_TOLERANCE:
        report.issues.append(
            Issue(
                Severity.ERROR,
                "rubric_weights",
                f"rubric weights must sum to 1.0, got {total:.6g}",
            )
        )
    ids = [d.id for d in mandate.rubric]
    for dup in {i for i in ids if ids.count(i) > 1}:
        report.issues.append(
            Issue(Severity.ERROR, "rubric_duplicate", f"duplicate rubric dimension {dup!r}")
        )


def _check_thresholds(mandate: Mandate, report: ValidationReport) -> None:
    lo = min(d.scale[0] for d in mandate.rubric)
    hi = max(d.scale[1] for d in mandate.rubric)
    for name, value in (
        ("advance_to_profile", mandate.thresholds.advance_to_profile),
        ("flag_for_review", mandate.thresholds.flag_for_review),
    ):
        if not (lo <= value <= hi):
            report.issues.append(
                Issue(
                    Severity.ERROR,
                    "threshold_out_of_range",
                    f"thresholds.{name}={value} outside rubric scale range [{lo}, {hi}]",
                )
            )


def _check_sectors(
    mandate: Mandate,
    profiles: dict[str, JurisdictionProfile],
    report: ValidationReport,
) -> None:
    # A taxonomy is "known" if some included jurisdiction's profile
    # declares it — taxonomies are jurisdiction data, not a code constant.
    declared = {
        p.classification_taxonomy
        for j, p in profiles.items()
        if j in mandate.geography.include
    }
    if declared and mandate.sectors.taxonomy not in declared:
        report.issues.append(
            Issue(
                Severity.ERROR,
                "unknown_taxonomy",
                f"sectors.taxonomy {mandate.sectors.taxonomy!r} is not the "
                f"classification taxonomy of any included jurisdiction "
                f"(declared: {sorted(declared)})",
            )
        )
    for code in [*mandate.sectors.include, *mandate.sectors.exclude]:
        if not _SECTOR_CODE_RE.match(code):
            report.issues.append(
                Issue(
                    Severity.ERROR,
                    "bad_sector_code",
                    f"sector code {code!r} is not digits with optional trailing '*'",
                )
            )


def _check_ownership(mandate: Mandate, report: ValidationReport) -> None:
    overlap = set(mandate.ownership.include) & set(mandate.ownership.exclude)
    if overlap:
        report.issues.append(
            Issue(
                Severity.ERROR,
                "ownership_overlap",
                f"ownership classes in both include and exclude: "
                f"{sorted(c.value for c in overlap)}",
            )
        )


def _check_signals(mandate: Mandate, report: ValidationReport) -> None:
    for name, params in mandate.signals.items():
        decl = SIGNALS.get(name)
        if decl is None:
            report.issues.append(
                Issue(
                    Severity.ERROR,
                    "unknown_signal",
                    f"signal {name!r} has no registered detector; known signals: "
                    f"{sorted(SIGNALS)}",
                )
            )
            continue
        try:
            decl.params_model.model_validate(params)
        except ValidationError as exc:
            report.issues.append(
                Issue(
                    Severity.ERROR,
                    "bad_signal_params",
                    f"signal {name!r} parameters invalid: {exc.errors()}",
                )
            )


def _check_geography(
    mandate: Mandate,
    matrices: list[CapabilityMatrix],
    profiles: dict[str, JurisdictionProfile],
    report: ValidationReport,
) -> None:
    for jurisdiction in mandate.geography.include:
        profile = profiles.get(jurisdiction)
        if profile is None:
            report.issues.append(
                Issue(
                    Severity.ERROR,
                    "unknown_jurisdiction",
                    f"no jurisdiction profile exists for {jurisdiction!r}; add "
                    f"one under jurisdictions/ before mandates may include it",
                    data={"jurisdiction": jurisdiction},
                )
            )
        else:
            offered = set(profile.available_modes)
            if not offered & set(mandate.required_modes):
                report.issues.append(
                    Issue(
                        Severity.ERROR,
                        "mode_unavailable",
                        f"required_modes "
                        f"{[m.value for m in mandate.required_modes]} not "
                        f"available for jurisdiction {jurisdiction!r}: its "
                        f"profile offers only "
                        f"{sorted(m.value for m in offered)}",
                        data={
                            "jurisdiction": jurisdiction,
                            "required_modes": [m.value for m in mandate.required_modes],
                            "available_modes": sorted(m.value for m in offered),
                        },
                    )
                )
        if not any(m.covers_jurisdiction(jurisdiction) for m in matrices):
            report.issues.append(
                Issue(
                    Severity.ERROR,
                    "no_adapter_for_jurisdiction",
                    f"no enabled adapter covers jurisdiction {jurisdiction!r}",
                    data={"jurisdiction": jurisdiction},
                )
            )


def _required_concepts(spec: SizeMetricSpec) -> frozenset[str] | None:
    if spec.metric in CONCEPTS:
        return frozenset({spec.metric})
    if spec.metric in DERIVED_METRICS:
        return resolve_required_concepts(spec.metric)
    return None


def _check_size_metric(
    mandate: Mandate,
    spec: SizeMetricSpec,
    where: str,
    matrices: list[CapabilityMatrix],
    report: ValidationReport,
) -> None:
    if not (len(spec.currency) == 3 and spec.currency.isalpha() and spec.currency.isupper()):
        report.issues.append(
            Issue(
                Severity.ERROR,
                "bad_currency",
                f"{where}.currency {spec.currency!r} is not an ISO 4217 code",
            )
        )
    if spec.min is not None and spec.max is not None and spec.min >= spec.max:
        report.issues.append(
            Issue(Severity.ERROR, "bad_size_band", f"{where}: min must be below max")
        )

    if spec.basis == "modelled":
        # Declared modelled with a named model: exempt from coverage checks.
        return

    required = _required_concepts(spec)
    if required is None:
        report.issues.append(
            Issue(
                Severity.ERROR,
                "unobservable_metric",
                f"{where}.metric {spec.metric!r} is neither a canonical concept "
                f"nor a declared derived metric; if it is only obtainable from a "
                f"model, declare it 'basis: modelled' with a named model",
            )
        )
        return

    for jurisdiction in mandate.geography.include:
        covering = [m for m in matrices if m.covers_jurisdiction(jurisdiction)]
        if not covering:
            continue  # already an ERROR from _check_geography
        for concept in sorted(required):
            best = _best_coverage(covering, concept)
            if best is None:
                report.issues.append(
                    Issue(
                        Severity.ERROR,
                        "concept_unavailable",
                        f"{where}.metric {spec.metric!r} requires concept "
                        f"{concept!r}; no enabled adapter supplies it for "
                        f"jurisdiction {jurisdiction!r}",
                        data={"concept": concept, "jurisdiction": jurisdiction},
                    )
                )
            elif best[0] is CoverageTier.CONDITIONAL:
                matrix, coverage = best[1], best[2]
                report.issues.append(
                    Issue(
                        Severity.WARNING,
                        "conditional_coverage",
                        f"{where}.metric {spec.metric!r}: concept {concept!r} is "
                        f"only conditionally available for {jurisdiction!r} via "
                        f"adapter {matrix.adapter!r} "
                        f"({coverage.condition.describe()}); companies outside "
                        f"the condition screen as insufficient_data",
                        data={
                            "concept": concept,
                            "jurisdiction": jurisdiction,
                            "adapter": matrix.adapter,
                            "condition_field": coverage.condition.field,
                            "condition_allowed": sorted(coverage.condition.allowed),
                        },
                    )
                )


def _best_coverage(matrices: list[CapabilityMatrix], concept: str):
    """Best available tier for a concept: ALWAYS beats CONDITIONAL beats none."""
    best = None
    for m in matrices:
        cov = m.concept_coverage(concept)
        if cov.tier is CoverageTier.ALWAYS:
            return (CoverageTier.ALWAYS, m, cov)
        if cov.tier is CoverageTier.CONDITIONAL and best is None:
            best = (CoverageTier.CONDITIONAL, m, cov)
    return best
