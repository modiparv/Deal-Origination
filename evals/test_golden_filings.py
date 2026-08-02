"""Golden-filing eval: extraction correctness against hand-verified rows.

For every evals/golden/filings/*.xhtml with a matching *.expected.yaml:
parse it with the real parser, map it with the adapter's concept map,
and require every expected figure (concept, period, value) to come out
exactly — plus every listed absent concept to stay absent, zero
unexplained parse errors, and zero quality flags.

This is the adapter eval set that gates adapter #2, and the parser's
regression suite across taxonomy generations.
"""

from decimal import Decimal
from pathlib import Path

import pytest
import yaml

pytest.importorskip(
    "ixbrlparse",
    reason="ixbrlparse unavailable in this environment (PyPI blocked); "
    "the golden eval runs in CI",
)

from deal_engine.adapters.companies_house.concept_map import ConceptMap  # noqa: E402
from deal_engine.parse import extract_figures, parse_ixbrl  # noqa: E402

FILINGS = Path(__file__).resolve().parent / "golden" / "filings"

CASES = sorted(FILINGS.glob("*.expected.yaml"))


@pytest.mark.parametrize("expected_path", CASES, ids=[p.stem for p in CASES])
def test_golden_filing(expected_path):
    expected = yaml.safe_load(expected_path.read_text(encoding="utf-8"))
    document_path = FILINGS / expected["document"]
    with document_path.open("rb") as handle:
        parsed = parse_ixbrl(handle)

    concept_map = ConceptMap.load()
    figures = extract_figures(parsed, concept_map)

    assert figures.parse_error_count == 0, parsed.errors
    assert figures.quality_flags == []

    by_key = {
        (d.concept, d.period_end): d
        for d in figures.drafts
    }
    for row in expected["figures"]:
        key = (row["concept"], str(row["period_end"]))
        assert key in by_key, (
            f"expected figure missing: {key}; got {sorted(by_key)}; "
            f"unmapped tags: {figures.unmapped}; "
            f"namespaces: {parsed.namespaces}"
        )
        draft = by_key[key]
        assert draft.value == Decimal(str(row["value"])), (
            f"{key}: value {draft.value} != expected {row['value']}"
        )
        if "period_start" in row:
            assert draft.period_start == str(row["period_start"])

    for concept in expected.get("absent_concepts", []):
        assert concept not in figures.present_concepts, (
            f"{concept} should be absent from this regime's filing"
        )

    if "production_software" in expected:
        from deal_engine.adapters.companies_house import mapping

        assert mapping.production_software(parsed) == expected["production_software"]


def test_golden_set_is_nonempty():
    assert CASES, "the golden filing set must not be empty from Phase 1 onward"
