"""Mandate YAML loading."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import ValidationError

from deal_engine.models.mandate import Mandate


class MandateLoadError(Exception):
    """The file could not be read, parsed, or structurally validated."""


def load_mandate(path: Path | str) -> Mandate:
    path = Path(path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise MandateLoadError(f"cannot read {path}: {exc}") from exc
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise MandateLoadError(f"invalid YAML in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise MandateLoadError(f"{path} does not contain a mapping")
    try:
        return Mandate.model_validate(data)
    except ValidationError as exc:
        raise MandateLoadError(f"mandate {path} failed structural validation:\n{exc}") from exc


def mandate_numerals(mandate: Mandate) -> frozenset[str]:
    """Numeric literals appearing verbatim in the mandate.

    The render validator whitelists these (comma-normalised) so prose may
    echo mandate thresholds — "above the £1,000,000 floor" — without a
    figure citation. Reformatted amounts ("£1m") are deliberately NOT
    whitelisted.
    """
    out: set[str] = set()

    def add(v: object) -> None:
        if isinstance(v, bool):
            return
        if isinstance(v, (int, float)):
            s = f"{v:g}"
            out.add(s)
            if isinstance(v, float) and v.is_integer():
                out.add(str(int(v)))

    for spec in (mandate.size.primary, mandate.size.secondary):
        if spec is not None:
            add(spec.min)
            add(spec.max)
    add(mandate.thresholds.advance_to_profile)
    add(mandate.thresholds.flag_for_review)
    for params in mandate.signals.values():
        for v in _walk_numbers(params):
            add(v)
    for dim in mandate.rubric:
        add(dim.weight)
        add(dim.scale[0])
        add(dim.scale[1])
    return frozenset(out)


def _walk_numbers(obj: object) -> list[int | float]:
    found: list[int | float] = []
    if isinstance(obj, bool):
        return found
    if isinstance(obj, (int, float)):
        found.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            found.extend(_walk_numbers(v))
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            found.extend(_walk_numbers(v))
    return found
