"""Eval harness skeleton.

Phase 1 populates two distinct golden sets (decision record §11/§14):

- evals/golden/filings/ — real cached filings with hand-verified expected
  figure rows (extraction correctness), including filleted accounts, a
  restatement, a period-length change, and a non-standard filer.
- evals/golden/companies/ — hand-labelled companies with expected
  ownership classification and screening outcome (inclusion/exclusion
  correctness), covering the ownership edge cases.

Phase 3 adds the scorer golden set (judgment quality) — a separate
artifact measured separately.
"""

from pathlib import Path

import pytest

GOLDEN = Path(__file__).resolve().parent / "golden"


def test_golden_directory_exists():
    assert GOLDEN.is_dir()


def test_filing_fixtures_present():
    filings = GOLDEN / "filings"
    if not filings.is_dir() or not any(filings.iterdir()):
        pytest.skip("golden filing fixtures are populated in Phase 1")


def test_company_fixtures_present():
    companies = GOLDEN / "companies"
    if not companies.is_dir() or not any(companies.iterdir()):
        pytest.skip("golden company fixtures are populated in Phase 1")
