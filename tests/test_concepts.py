import pytest

from deal_engine.concepts import CONCEPTS, Flow, PeriodType, get_concept


def test_registry_integrity():
    assert CONCEPTS, "concept registry must not be empty"
    for name, concept in CONCEPTS.items():
        assert concept.name == name
        assert isinstance(concept.period_type, PeriodType)
        assert isinstance(concept.flow, Flow)
        assert concept.description


def test_reliable_lower_mid_market_concepts_are_first_class():
    # The only financial fields present for filleted/micro filers must exist
    # as canonical concepts (decision record §3 / finding W1).
    for name in (
        "net_assets",
        "equity",
        "current_assets",
        "creditors_within_one_year",
        "total_assets_less_current_liabilities",
        "average_employees",
    ):
        assert name in CONCEPTS


def test_get_concept_unknown_raises_with_context():
    with pytest.raises(KeyError, match="unknown canonical concept"):
        get_concept("ebitda")  # derived metric, not a filed concept


def test_balance_sheet_concepts_are_instant():
    assert get_concept("net_assets").period_type is PeriodType.INSTANT
    assert get_concept("revenue").period_type is PeriodType.DURATION
    assert get_concept("average_employees").period_type is PeriodType.DURATION
