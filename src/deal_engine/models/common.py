"""Shared enums and helpers for the canonical schema."""

from __future__ import annotations

import hashlib
import json
from enum import Enum
from typing import Mapping


class Basis(str, Enum):
    FILED = "filed"          # extracted verbatim from a source document
    DERIVED = "derived"      # computed by a named function from other figures
    MODELLED = "modelled"    # output of an explicit model run
    UNVERIFIED = "unverified"  # aggregator-sourced; never renders in a profile


class Consolidation(str, Enum):
    GROUP = "group"
    COMPANY = "company"
    NONE = "none"


class ParseStatus(str, Enum):
    PENDING = "pending"
    PARSED = "parsed"
    PDF_ONLY = "pdf_only"        # scanned image, no structured data — an outcome, not an error
    QUARANTINED = "quarantined"  # parse errors beyond threshold; excluded from figures


class OwnershipClass(str, Enum):
    OWNER_MANAGED = "owner_managed"  # founder- and family-owned, merged
    INDEPENDENT = "independent"
    PE_BACKED = "pe_backed"
    LISTED = "listed"
    LISTED_SUBSIDIARY = "listed_subsidiary"
    UNCLASSIFIABLE = "unclassifiable"


class ScreenOutcome(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    INSUFFICIENT_DATA = "insufficient_data"  # first-class, distinct from failed
    FLAGGED = "flagged"                      # e.g. unclassifiable ownership, fail-closed


class RestatementClass(str, Enum):
    ROUNDING = "rounding"
    RECLASSIFICATION = "reclassification"
    GENUINE = "genuine"


def dimensions_hash(dimensions: Mapping[str, str]) -> str:
    """Canonical hash of an XBRL dimension mapping.

    Key-sorted JSON, sha256, 16 hex chars. The empty mapping hashes too —
    a figure with no dimensions still participates in the observation
    natural key.
    """
    canonical = json.dumps(dict(sorted(dimensions.items())), separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
