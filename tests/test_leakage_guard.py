"""Jurisdiction-leakage guard.

Core code must contain no jurisdiction-specific vocabulary; adapters
translate. This test is what keeps the abstraction honest — everything
else was a one-time rename, this stops the rename undoing itself in
Phase 1.

Scope: every Python file under src/deal_engine/ EXCEPT adapters/ (the
designated home of local terminology). The jurisdictions/ directory is
data, not code, and is not scanned; neither are tests (which exercise
the adapter declarations) nor mandate YAMLs (configuration may name
jurisdictions — that is data, not a leak).
"""

from __future__ import annotations

import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src" / "deal_engine"
EXCLUDED = {SRC / "adapters"}

# Case-insensitive token patterns unless stated. Word-bounded so that
# e.g. "intrinsic" does not trip "sic" and "discharge" does not trip
# "charge".
TOKEN_PATTERNS = [
    (r"\bpsc\b", "psc"),
    (r"\bsic\b", "sic"),
    (r"\bcrn\b", "crn"),
    (r"companies\s+house", "companies house"),
    (r"\bfilleted\b", "filleted"),
    (r"\babridged\b", "abridged"),
    (r"accounting\s+reference\s+date", "accounting reference date"),
    (r"\bcharges?\b", "charge (as a noun for security)"),
    (r"\bMR01\b", "MR01"),
    (r"\bAA01\b", "AA01"),
    (r"\bCS01\b", "CS01"),
    (r"confirmation\s+statement", "confirmation statement"),
    (r"\bECCTA\b", "ECCTA"),
    # Hardcoded jurisdiction literals in code. "GBP" and the like do not
    # match; only the bare quoted country strings do.
    (r"[\"']GB[\"']", 'hardcoded "GB" literal'),
    (r"[\"']UK[\"']", 'hardcoded "UK" literal'),
    (r"\bUnited\s+Kingdom\b", "United Kingdom"),
]

COMPILED = [(re.compile(pat, re.IGNORECASE), label) for pat, label in TOKEN_PATTERNS]


def scanned_files() -> list[Path]:
    files = []
    for path in sorted(SRC.rglob("*.py")):
        if any(excluded in path.parents for excluded in EXCLUDED):
            continue
        files.append(path)
    return files


def test_scan_scope_is_nonempty_and_excludes_adapters():
    files = scanned_files()
    assert len(files) > 10
    assert not any("adapters" in p.parts for p in files)


def test_no_jurisdiction_tokens_outside_adapters():
    violations: list[str] = []
    for path in scanned_files():
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for pattern, label in COMPILED:
                if pattern.search(line):
                    rel = path.relative_to(SRC.parent.parent)
                    violations.append(f"{rel}:{lineno}: {label}: {line.strip()[:90]}")
    assert not violations, (
        "jurisdiction-specific vocabulary leaked into core "
        "(move it to src/deal_engine/adapters/ or jurisdictions/):\n"
        + "\n".join(violations)
    )


def test_adapter_declaration_still_owns_the_vocabulary():
    # The tokens must not simply have been deleted — the Companies House
    # declaration is their designated home.
    decl = (SRC / "adapters" / "companies_house_decl.py").read_text(encoding="utf-8")
    for needle in ("psc", "charge", "sic", "accounting reference date"):
        assert re.search(needle, decl, re.IGNORECASE), (
            f"expected {needle!r} to live in the adapter declaration"
        )
