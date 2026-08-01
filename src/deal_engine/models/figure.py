"""The provenance-carrying primitive.

A Figure is an *observation*: what one source document says a concept's
value was for a period. The same (company, concept, period) legitimately
arrives from multiple documents — statutory filings routinely restate
prior-period comparatives — so the natural key includes the source document, and a
deterministic `is_current` selection (latest filed date wins) chooses the
canonical observation. Superseded observations are never deleted.

Provenance is transitive and enforced here and in the database schema:
- filed     ⇒ source_document_id and source_tag required
- derived   ⇒ derivation (named function + input figure IDs) required
- modelled  ⇒ model_run_id required
- unverified⇒ aggregator_ref required; never renders in a profile
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from deal_engine.concepts import CONCEPTS, PeriodType
from deal_engine.derive.registry import DERIVED_METRICS
from deal_engine.models.common import Basis, Consolidation, dimensions_hash


class Derivation(BaseModel):
    model_config = ConfigDict(frozen=True)

    function: str = Field(min_length=1)
    inputs: list[str] = Field(min_length=1)  # figure IDs


class Figure(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    company_id: str
    concept: str
    value: Decimal
    unit: str  # XBRL measure, e.g. "iso4217:GBP", "xbrli:pure"
    currency: str | None = None  # ISO 4217 when monetary
    period_type: PeriodType
    period_start: date
    period_end: date
    dimensions: dict[str, str] = Field(default_factory=dict)
    dimensions_hash: str | None = None  # computed if absent; checked if present
    consolidation: Consolidation = Consolidation.NONE
    decimals: int | None = None  # filed precision; defines agreement tolerance
    raw_text: str | None = None
    basis: Basis
    source_document_id: str | None = None
    source_tag: str | None = None  # XBRL tag or document location
    derivation: Derivation | None = None
    model_run_id: str | None = None
    aggregator_ref: str | None = None
    is_current: bool = True

    @model_validator(mode="after")
    def _check(self) -> "Figure":
        if self.concept not in CONCEPTS and self.concept not in DERIVED_METRICS:
            raise ValueError(
                f"concept {self.concept!r} is neither a canonical concept nor a "
                f"declared derived metric"
            )

        if self.basis is Basis.FILED:
            if not self.source_document_id or not self.source_tag:
                raise ValueError(
                    "filed figure requires source_document_id and source_tag — "
                    "a figure with no traceable source cannot exist"
                )
            if self.derivation is not None:
                raise ValueError("filed figure must not carry a derivation")
        elif self.basis is Basis.DERIVED:
            if self.derivation is None:
                raise ValueError(
                    "derived figure requires derivation (named function + input "
                    "figure IDs)"
                )
            if self.source_document_id is not None:
                raise ValueError(
                    "derived figure must not carry a source_document_id; its "
                    "provenance is transitive through derivation inputs"
                )
        elif self.basis is Basis.MODELLED:
            if not self.model_run_id:
                raise ValueError("modelled figure requires model_run_id")
        elif self.basis is Basis.UNVERIFIED:
            if not self.aggregator_ref:
                raise ValueError("unverified figure requires aggregator_ref")

        if self.period_type is PeriodType.INSTANT:
            if self.period_start != self.period_end:
                raise ValueError(
                    "instant figure must have period_start == period_end"
                )
        elif self.period_start > self.period_end:
            raise ValueError("period_start after period_end")

        if self.currency is not None and not (
            len(self.currency) == 3 and self.currency.isalpha() and self.currency.isupper()
        ):
            raise ValueError(f"currency must be an ISO 4217 code, got {self.currency!r}")

        expected = dimensions_hash(self.dimensions)
        if self.dimensions_hash is None:
            object.__setattr__(self, "dimensions_hash", expected)
        elif self.dimensions_hash != expected:
            raise ValueError(
                f"dimensions_hash {self.dimensions_hash!r} does not match "
                f"dimensions (expected {expected!r})"
            )
        return self
