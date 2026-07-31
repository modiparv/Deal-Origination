"""Canonical concept registry.

The jurisdiction-agnostic vocabulary of financial concepts the engine
understands. Adapters map source-native tags (XBRL concepts, PDF
locations) onto these names; the capability matrix and derive registry
both key off them. Deliberately dependency-free so every layer can
import it.

Concepts reliably present even under reduced-disclosure filing regimes
(where smaller companies publish balance-sheet data but no income
statement) are first-class citizens here — for much of the
lower-mid-market universe they are the only filed financial fields, not
an afterthought.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class PeriodType(str, Enum):
    INSTANT = "instant"    # balance-sheet facts: a single date
    DURATION = "duration"  # flow facts: a period


class Flow(str, Enum):
    """What kind of quantity a concept is.

    Used by the parse-time sign-normalisation layer: cost/expense
    concepts are conventionally tagged positive under negated-label
    presentation, and the parser needs a concept's nature to normalise
    safely.
    """

    INCOME = "income"
    EXPENSE = "expense"
    ASSET = "asset"
    LIABILITY = "liability"
    EQUITY = "equity"
    COUNT = "count"


@dataclass(frozen=True)
class Concept:
    name: str
    period_type: PeriodType
    flow: Flow
    description: str


_ALL = [
    # Income statement — available only where one is published; see each
    # adapter's capability matrix conditions.
    Concept("revenue", PeriodType.DURATION, Flow.INCOME, "Turnover / revenue"),
    Concept("gross_profit", PeriodType.DURATION, Flow.INCOME, "Gross profit or loss"),
    Concept("operating_profit", PeriodType.DURATION, Flow.INCOME, "Operating profit or loss"),
    Concept("profit_before_tax", PeriodType.DURATION, Flow.INCOME, "Profit or loss before tax"),
    Concept("profit_for_period", PeriodType.DURATION, Flow.INCOME, "Profit or loss for the financial period"),
    Concept("staff_costs", PeriodType.DURATION, Flow.EXPENSE, "Staff costs / employee benefits expense"),
    Concept("depreciation_amortisation", PeriodType.DURATION, Flow.EXPENSE, "Depreciation, amortisation and impairment expense"),
    Concept("tax_charge", PeriodType.DURATION, Flow.EXPENSE, "Tax on profit or loss"),
    # Balance sheet — reliably present across regimes (the smallest
    # regimes aggregate some lines).
    Concept("cash", PeriodType.INSTANT, Flow.ASSET, "Cash at bank and in hand"),
    Concept("debtors", PeriodType.INSTANT, Flow.ASSET, "Debtors / receivables"),
    Concept("current_assets", PeriodType.INSTANT, Flow.ASSET, "Total current assets"),
    Concept("fixed_assets", PeriodType.INSTANT, Flow.ASSET, "Total fixed assets"),
    Concept("creditors_within_one_year", PeriodType.INSTANT, Flow.LIABILITY, "Creditors: amounts falling due within one year"),
    Concept("creditors_after_one_year", PeriodType.INSTANT, Flow.LIABILITY, "Creditors: amounts falling due after more than one year"),
    Concept("net_current_assets", PeriodType.INSTANT, Flow.ASSET, "Net current assets or liabilities"),
    Concept("total_assets_less_current_liabilities", PeriodType.INSTANT, Flow.ASSET, "Total assets less current liabilities"),
    Concept("net_assets", PeriodType.INSTANT, Flow.EQUITY, "Net assets or liabilities"),
    Concept("equity", PeriodType.INSTANT, Flow.EQUITY, "Shareholders' funds / equity"),
    Concept("share_capital", PeriodType.INSTANT, Flow.EQUITY, "Called-up share capital"),
    Concept("retained_earnings", PeriodType.INSTANT, Flow.EQUITY, "Retained earnings / accumulated profit and loss"),
    # The one income-adjacent datum most registries require in every
    # regime — the best free size proxy where no income statement is
    # published, and a first-class screening field.
    Concept("average_employees", PeriodType.DURATION, Flow.COUNT, "Average number of employees during the period"),
]

CONCEPTS: dict[str, Concept] = {c.name: c for c in _ALL}


def get_concept(name: str) -> Concept:
    try:
        return CONCEPTS[name]
    except KeyError:
        raise KeyError(
            f"unknown canonical concept {name!r}; known concepts: {sorted(CONCEPTS)}"
        ) from None
