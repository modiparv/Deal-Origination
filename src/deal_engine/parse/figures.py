"""Raw facts × concept map → figure drafts, with within-document
discipline.

- Every fact appears at least twice per document (current and prior
  periods); drafts key on exact dates.
- The same fact is routinely tagged in several places (balance sheet and
  notes): duplicates by (concept, period, dimensions) must agree within
  filed precision — a disagreement is a document-quality flag, never a
  coin flip.
- Unmapped taxonomy names are reported with counts so the concept map
  grows from evidence; mapped-but-absent concepts become coverage facts
  downstream.

Sign normalisation note: values are kept as filed. The concept
registry's Flow metadata drives normalisation once an income-statement
fixture exists to pin the convention against — recorded as a known
Phase 1 follow-up, not silently guessed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from deal_engine.parse.ixbrl import ParsedDocument, RawFact


@dataclass(frozen=True)
class FigureDraft:
    concept: str
    value: Decimal
    unit: str | None
    period_type: str  # "instant" | "duration"
    period_start: str  # instants use start == end
    period_end: str
    dimensions: dict[str, str] = field(hash=False, default_factory=dict)
    decimals: int | None = None
    raw_text: str = ""
    source_tag: str = ""


@dataclass
class DocumentFigures:
    drafts: list[FigureDraft]
    present_concepts: set[str]
    unmapped: dict[str, int]  # "prefix:LocalName" -> occurrences
    quality_flags: list[str]
    parse_error_count: int


def _period(fact: RawFact) -> tuple[str, str, str] | None:
    if fact.instant:
        return ("instant", fact.instant, fact.instant)
    if fact.period_end:
        return ("duration", fact.period_start or fact.period_end, fact.period_end)
    return None


def _tolerance(decimals: int | None) -> Decimal:
    if decimals is None:
        return Decimal("0")
    return Decimal(10) ** -decimals


def extract_figures(document: ParsedDocument, concept_map) -> DocumentFigures:
    drafts: dict[tuple, FigureDraft] = {}
    unmapped: dict[str, int] = {}
    quality_flags: list[str] = []

    for fact in document.facts:
        canonical = concept_map.resolve(
            fact.namespace, fact.local_name, fact.dimensions
        )
        if canonical is None:
            key = f"{fact.prefix}:{fact.local_name}"
            unmapped[key] = unmapped.get(key, 0) + 1
            continue
        period = _period(fact)
        if period is None:
            quality_flags.append(
                f"{canonical}: fact with no usable period (context dates missing)"
            )
            continue
        period_type, start, end = period
        dedupe_key = (canonical, start, end, tuple(sorted(fact.dimensions.items())))
        draft = FigureDraft(
            concept=canonical,
            value=fact.value,
            unit=fact.unit,
            period_type=period_type,
            period_start=start,
            period_end=end,
            dimensions=dict(fact.dimensions),
            decimals=fact.decimals,
            raw_text=fact.raw_text,
            source_tag=f"{fact.prefix}:{fact.local_name}",
        )
        existing = drafts.get(dedupe_key)
        if existing is None:
            drafts[dedupe_key] = draft
        elif abs(existing.value - draft.value) > _tolerance(existing.decimals):
            quality_flags.append(
                f"{canonical} {end}: duplicate facts disagree beyond filed "
                f"precision ({existing.value} vs {draft.value})"
            )

    result = list(drafts.values())
    return DocumentFigures(
        drafts=result,
        present_concepts={d.concept for d in result},
        unmapped=unmapped,
        quality_flags=quality_flags,
        parse_error_count=document.error_count,
    )
