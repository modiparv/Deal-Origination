"""Prose numeral validation and marker substitution.

The LLM never writes financial numerals. It writes citation markers —
``{fig:F0123}``, optionally with a format hint ``{fig:F0123:pct}`` — and
the renderer substitutes formatted values from the database, so a quantity
cannot appear in rendered output without a figure ID. Anything the LLM
would want to compute ("grew 12%") must pre-exist as a derived figure and
be cited by marker.

This module is a pure string layer with no LLM or pipeline dependency —
buildable and fully testable in Phase 0 (DoD #5).

The bare-numeral whitelist is deliberately tight; every addition is a
hole. Allowed:

- four-digit years 1900–2099 (incl. inside tokens like "FY2024")
- ISO dates (YYYY-MM-DD)
- single digits 0–9, EXCEPT when adjacent to a currency symbol or a
  magnitude/percent suffix ("£1m" and "3%" are financial quantities and
  must be cited; "three of 5 directors" is a count and may pass)
- numerals appearing verbatim in the mandate YAML, comma-normalised
  ("above the £1,000,000 floor" passes; the reformatted "£1m" does not)
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Collection, Mapping

MARKER_RE = re.compile(r"\{fig:([A-Za-z0-9_-]+)(?::([a-z]+))?\}")
_ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_NUMERAL_RE = re.compile(r"\d+(?:[.,]\d+)*")
_CURRENCY_CHARS = "£$€"
_MAGNITUDE_RE = re.compile(r"^\s?(m|bn|k|%)(\b|$)", re.IGNORECASE)


@dataclass(frozen=True)
class Violation:
    kind: str  # "unresolved_marker" | "bare_numeral"
    token: str
    position: int

    def __str__(self) -> str:
        return f"{self.kind}: {self.token!r} at offset {self.position}"


class RenderError(Exception):
    def __init__(self, violations: list[Violation]):
        self.violations = violations
        super().__init__(
            "render failed: " + "; ".join(str(v) for v in violations)
        )


def _normalise(numeral: str) -> str:
    return numeral.replace(",", "")


def validate_rendered_text(
    text: str,
    known_figure_ids: Collection[str],
    allowed_numerals: Collection[str] = (),
) -> list[Violation]:
    """Validate LLM-authored prose. Empty result means renderable."""
    violations: list[Violation] = []
    known = set(known_figure_ids)
    allowed = {_normalise(n) for n in allowed_numerals}

    for match in MARKER_RE.finditer(text):
        if match.group(1) not in known:
            violations.append(
                Violation("unresolved_marker", match.group(0), match.start())
            )

    # Strip resolved constructs, preserving offsets with padding.
    stripped = MARKER_RE.sub(lambda m: " " * len(m.group(0)), text)
    stripped = _ISO_DATE_RE.sub(lambda m: " " * len(m.group(0)), stripped)

    for match in _NUMERAL_RE.finditer(stripped):
        token = match.group(0)
        if _is_allowed_numeral(token, stripped, match.start(), match.end(), allowed):
            continue
        violations.append(Violation("bare_numeral", token, match.start()))
    return violations


def _is_allowed_numeral(
    token: str, text: str, start: int, end: int, allowed: set[str]
) -> bool:
    if _normalise(token) in allowed:
        return True
    prev_char = text[start - 1] if start > 0 else ""
    quantity_adjacent = prev_char in _CURRENCY_CHARS or bool(
        _MAGNITUDE_RE.match(text[end : end + 3])
    )
    if quantity_adjacent:
        return False
    if len(token) == 4 and token.isdigit() and 1900 <= int(token) <= 2099:
        return True
    if len(token) == 1 and token.isdigit():
        return True
    return False


def substitute_markers(
    text: str,
    figure_display: Mapping[str, str],
    allowed_numerals: Collection[str] = (),
) -> str:
    """Substitute markers with formatted figure values.

    Validates first; raises RenderError on any violation rather than
    rendering partially. `figure_display` maps figure ID to its formatted
    display string (formatting from stored values is the Phase 4
    renderer's job; the contract is fixed here).
    """
    violations = validate_rendered_text(text, figure_display.keys(), allowed_numerals)
    if violations:
        raise RenderError(violations)
    return MARKER_RE.sub(lambda m: figure_display[m.group(1)], text)
