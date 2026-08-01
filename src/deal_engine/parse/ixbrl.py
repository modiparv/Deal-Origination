"""Generic inline-XBRL mechanics.

Wraps the ixbrlparse library and normalises its output into RawFacts
with resolved namespace URIs, prefix-stripped dimension names, and
explicit periods. Registry- and taxonomy-specific mapping lives in the
owning adapter's concept map, never here.

Discipline this layer owns (per the plan):
- parser errors are harvested, counted and surfaced — nil facts land in
  the error list silently otherwise;
- prefixes are vendor-arbitrary: facts are keyed by resolved namespace
  URI, and contexts are read by their dates, never their ids;
- every fact's dimensions ride along, prefix-stripped, so dimensional
  concepts (e.g. maturity splits) can be resolved by the concept map.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import IO


@dataclass(frozen=True)
class RawFact:
    namespace: str  # resolved URI ("" when the prefix could not be resolved)
    prefix: str
    local_name: str
    value: Decimal
    unit: str | None
    decimals: int | None
    period_start: str | None  # ISO dates as strings; None for instants
    period_end: str | None
    instant: str | None
    dimensions: dict[str, str]  # dimension local name -> member local name
    raw_text: str


@dataclass
class ParsedDocument:
    facts: list[RawFact]
    namespaces: dict[str, str]  # prefix -> URI
    error_count: int
    errors: list[str] = field(default_factory=list)


def _strip_prefix(qname: str) -> str:
    return qname.rsplit(":", 1)[-1].strip()


def _resolve_namespace(prefix: str, namespaces: dict[str, str]) -> str:
    return namespaces.get(f"xmlns:{prefix}") or namespaces.get(prefix) or ""


def _segment_dimensions(context: object) -> dict[str, str]:
    dims: dict[str, str] = {}
    for seg in getattr(context, "segments", None) or []:
        if not isinstance(seg, dict):
            continue
        dimension = seg.get("dimension") or seg.get("tag")
        member = seg.get("value") or seg.get("text")
        if dimension and member:
            dims[_strip_prefix(str(dimension))] = _strip_prefix(str(member))
    return dims


def parse_ixbrl(handle: IO) -> ParsedDocument:
    from ixbrlparse import IXBRL  # heavy import kept local

    parsed = IXBRL(handle, raise_on_error=False)
    raw_namespaces = {
        str(k): str(v) for k, v in (getattr(parsed, "namespaces", {}) or {}).items()
    }

    facts: list[RawFact] = []
    for numeric in parsed.numeric:
        if numeric.value is None:
            continue
        context = numeric.context
        fmt = getattr(numeric, "format", None)
        decimals = getattr(fmt, "decimals", None)
        try:
            decimals = int(decimals) if decimals is not None else None
        except (TypeError, ValueError):
            decimals = None
        instant = getattr(context, "instant", None)
        start = getattr(context, "startdate", None)
        end = getattr(context, "enddate", None)
        facts.append(
            RawFact(
                namespace=_resolve_namespace(str(numeric.schema), raw_namespaces),
                prefix=str(numeric.schema),
                local_name=str(numeric.name),
                value=Decimal(str(numeric.value)),
                unit=str(numeric.unit) if numeric.unit is not None else None,
                decimals=decimals,
                period_start=str(start) if start else None,
                period_end=str(end) if end else None,
                instant=str(instant) if instant else None,
                dimensions=_segment_dimensions(context),
                raw_text=str(getattr(numeric, "text", "")),
            )
        )

    errors = [repr(e) for e in (getattr(parsed, "errors", None) or [])]
    return ParsedDocument(
        facts=facts,
        namespaces=raw_namespaces,
        error_count=len(errors),
        errors=errors,
    )
