"""Static capability declaration for the Companies House adapter.

Declared in Phase 0 so mandate validation can run before the adapter is
implemented (Phase 1). Jurisdiction `GB` means the Companies House register
in full — England & Wales, Scotland and Northern Ireland — not Great
Britain in the geographic sense. The Republic of Ireland is a separate
registry (CRO) and is deliberately absent.

Account-type values come from Companies House's own enumeration source
(`companieshouse/api-enumerations`, constants.yml `account_type`). The
tiers reflect UK filing regimes as of 2026:

- micro-entity accounts: ~5 balance-sheet lines plus the average-employees
  footnote; no P&L, no cash/debtors breakdown.
- small "filleted" accounts (total-exemption-*): full balance sheet and
  notes, average employees; no P&L.
- medium/full/group accounts: full P&L filed.

The P&L gap is permanent architecture, not transitional: the April 2028
ECCTA reforms require small companies to file a P&L but allow them to opt
out of public display.

This module is also the home of Companies House vocabulary. Core modules
use neutral terms; the adapter translates (see VOCABULARY). Registry
gotchas that Phase 1 parsers must honour, recorded here rather than in
core: the canonical PSC statement enum key misspells "significant"
(`no-individual-or-entity-with-signficant-control`), the charges list
misspells `unfiletered_count`, officer and PSC dates of birth are
month/year only, and the filing-history category enum is officially
incomplete — store verbatim, match tolerantly, never validate strictly.
"""

from __future__ import annotations

from deal_engine.adapters.base import (
    CapabilityMatrix,
    Condition,
    ConceptCoverage,
    CoverageTier,
)

# Local term -> canonical vocabulary. Every Companies House-specific name
# lives on the left; core code knows only the right-hand terms. Phase 1
# mappers translate at the adapter boundary.
VOCABULARY = {
    "psc": "beneficial_owner",
    "psc statement": "ownership_statement",
    "natures of control": "control_natures",
    "charge": "security_interest",
    "persons entitled": "secured_parties",
    "particulars": "details",
    "company number (CRN)": "registration_id",
    "sic code": "classification_code (taxonomy: sic_2007)",
    "accounting reference date": "fiscal_period_end",
    "filleted / abridged / micro-entity accounts": (
        "account_type value feeding capability-matrix conditions; "
        "concept unavailability is a coverage fact, not a core state"
    ),
    "form codes (AA, CS01, MR01, AA01, ...)": "FilingRecord.type, verbatim",
    "confirmation statement": "statutory filing: confirmation_of_details",
}

# Account types under which a P&L is on the public record.
_PL_BEARING = frozenset({"full", "medium", "group"})

# Account types with a full (non-micro) balance sheet and notes.
_FULL_BALANCE_SHEET = _PL_BEARING | frozenset(
    {
        "small",
        "total-exemption-full",
        "total-exemption-small",
        "partial-exemption",
        "audited-abridged",
        "unaudited-abridged",
    }
)

_ALWAYS = ConceptCoverage(CoverageTier.ALWAYS)
_IF_NOT_MICRO = ConceptCoverage(
    CoverageTier.CONDITIONAL, Condition("account_type", _FULL_BALANCE_SHEET)
)
_IF_PL_FILED = ConceptCoverage(
    CoverageTier.CONDITIONAL, Condition("account_type", _PL_BEARING)
)

COMPANIES_HOUSE_CAPABILITIES = CapabilityMatrix(
    adapter="companies_house",
    jurisdictions=frozenset({"GB"}),
    coverage={
        # Present in every regime, micro included.
        "net_assets": _ALWAYS,
        "equity": _ALWAYS,
        "current_assets": _ALWAYS,
        "creditors_within_one_year": _ALWAYS,
        "total_assets_less_current_liabilities": _ALWAYS,
        "average_employees": _ALWAYS,
        # Present with a non-micro balance sheet and notes.
        "cash": _IF_NOT_MICRO,
        "debtors": _IF_NOT_MICRO,
        "fixed_assets": _IF_NOT_MICRO,
        "creditors_after_one_year": _IF_NOT_MICRO,
        "net_current_assets": _IF_NOT_MICRO,
        "share_capital": _IF_NOT_MICRO,
        "retained_earnings": _IF_NOT_MICRO,
        # Present only where a P&L is filed.
        "revenue": _IF_PL_FILED,
        "gross_profit": _IF_PL_FILED,
        "operating_profit": _IF_PL_FILED,
        "profit_before_tax": _IF_PL_FILED,
        "profit_for_period": _IF_PL_FILED,
        "staff_costs": _IF_PL_FILED,
        "depreciation_amortisation": _IF_PL_FILED,
        "tax_charge": _IF_PL_FILED,
    },
)
