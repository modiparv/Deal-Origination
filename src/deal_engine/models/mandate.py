"""Mandate: structural schema.

Structure lives here (types, ranges, required fields); semantic and
capability validation — weights, taxonomies, signal registration, adapter
coverage — lives in `deal_engine.mandate.validator`, which produces
ERROR/WARNING issues rather than exceptions.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from deal_engine.models.common import OwnershipClass


class _Spec(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


class SizeMetricSpec(_Spec):
    metric: str
    currency: str
    min: float | None = None
    max: float | None = None
    # Any metric no adapter supplies as filed/derived must be declared
    # modelled, with the model named and its assumptions recorded.
    basis: Literal["modelled"] | None = None
    model: str | None = None
    assumptions: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _modelled_named(self) -> "SizeMetricSpec":
        if self.basis == "modelled" and not self.model:
            raise ValueError("basis: modelled requires a named model")
        return self


class SizeSpec(_Spec):
    primary: SizeMetricSpec
    secondary: SizeMetricSpec | None = None
    # Resolved per company at screen time, not globally: P&L observability
    # is a per-company property.
    on_insufficient_data: Literal["flag", "exclude", "include"] = "flag"


class GeographySpec(_Spec):
    include: list[str] = Field(min_length=1)


class SectorsSpec(_Spec):
    taxonomy: str
    include: list[str] = Field(min_length=1)
    exclude: list[str] = Field(default_factory=list)


class OwnershipSpec(_Spec):
    include: list[OwnershipClass] = Field(default_factory=list)
    exclude: list[OwnershipClass] = Field(default_factory=list)
    # Fail-closed by default: unclassifiable companies are flagged for
    # manual review, never silently passed.
    on_unclassifiable: Literal["flag", "exclude"] = "flag"


class RubricDimension(_Spec):
    id: str
    weight: float = Field(gt=0.0, le=1.0)
    scale: tuple[int, int]
    guidance: str | None = None

    @model_validator(mode="after")
    def _scale_ordered(self) -> "RubricDimension":
        lo, hi = self.scale
        if lo >= hi:
            raise ValueError(f"scale must be (low, high) with low < high, got {self.scale}")
        return self


class Thresholds(_Spec):
    advance_to_profile: float
    flag_for_review: float


class Mandate(_Spec):
    id: str
    name: str
    asset_class: str
    deal_type: str
    geography: GeographySpec
    size: SizeSpec
    sectors: SectorsSpec
    ownership: OwnershipSpec
    signals: dict[str, dict] = Field(default_factory=dict)
    rubric: list[RubricDimension] = Field(min_length=1)
    thresholds: Thresholds
