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

import io
import re
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


def _first(value: object) -> object:
    # ixbrlparse stores namespace values as LISTS (it splits the xmlns
    # attribute on spaces); a single URI arrives as a one-element list.
    if isinstance(value, (list, tuple)):
        return value[0] if value else ""
    return value


def _resolve_namespace(
    prefix: str,
    namespaces: dict[str, object],
    document_bindings: dict[str, set[str]] | None = None,
) -> str:
    value = namespaces.get(f"xmlns:{prefix}") or namespaces.get(prefix) or ""
    resolved = str(_first(value))
    if resolved:
        return resolved
    # Some production software (e.g. Digita Accounts Production) declares
    # xmlns: on each element that uses the prefix instead of on the root;
    # ixbrlparse only reads root-level declarations. Fall back to the
    # document-wide scan, but only when the binding is unambiguous — a
    # prefix bound to several URIs in one document stays unresolved and
    # is reported unmapped rather than guessed.
    if document_bindings:
        uris = document_bindings.get(prefix, set())
        if len(uris) == 1:
            return next(iter(uris))
    return ""


_XMLNS_DECL_RE = re.compile(r"xmlns:([A-Za-z_][\w.-]*)\s*=\s*\"([^\"]+)\"")


def _scan_xmlns_bindings(content: str) -> dict[str, set[str]]:
    """Collect every xmlns:prefix="uri" declaration anywhere in the
    document, root-level or per-element."""
    bindings: dict[str, set[str]] = {}
    for prefix, uri in _XMLNS_DECL_RE.findall(content):
        bindings.setdefault(prefix, set()).add(uri.strip())
    return bindings


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

    content = handle.read()
    if isinstance(content, bytes):
        text = content.decode("utf-8", errors="replace")
        buffer: IO = io.BytesIO(content)
    else:
        text = content
        buffer = io.StringIO(content)
    document_bindings = _scan_xmlns_bindings(text)

    parsed = IXBRL(buffer, raise_on_error=False)
    raw_namespaces: dict[str, object] = dict(getattr(parsed, "namespaces", {}) or {})
    display_namespaces = {
        str(k): str(_first(v)) for k, v in raw_namespaces.items()
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
                namespace=_resolve_namespace(
                    str(numeric.schema), raw_namespaces, document_bindings
                ),
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
        namespaces=display_namespaces,
        error_count=len(errors),
        errors=errors,
    )
