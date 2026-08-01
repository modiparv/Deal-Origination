import pytest

from deal_engine.adapters.base import (
    CapabilityMatrix,
    Condition,
    ConceptCoverage,
    CoverageTier,
)
from deal_engine.adapters.companies_house_decl import COMPANIES_HOUSE_CAPABILITIES
from deal_engine.adapters.registry import ENABLED_ADAPTERS, matrices_for_jurisdiction
from deal_engine.concepts import CONCEPTS


def test_conditional_coverage_requires_condition():
    with pytest.raises(ValueError, match="requires a condition"):
        ConceptCoverage(CoverageTier.CONDITIONAL)
    with pytest.raises(ValueError, match="must not carry a condition"):
        ConceptCoverage(CoverageTier.ALWAYS, Condition("account_type", frozenset({"full"})))


def test_condition_is_machine_readable():
    cond = Condition("account_type", frozenset({"full", "group", "medium"}))
    assert cond.evaluate({"account_type": "full"})
    assert not cond.evaluate({"account_type": "micro-entity"})
    assert not cond.evaluate({})
    assert "account_type" in cond.describe()


def test_companies_house_declaration_integrity():
    matrix = COMPANIES_HOUSE_CAPABILITIES
    # GB means the whole Companies House register (England & Wales, Scotland,
    # Northern Ireland); IE is a different registry and must be absent.
    assert matrix.jurisdictions == frozenset({"GB"})
    assert not matrix.covers_jurisdiction("IE")
    for concept in matrix.coverage:
        assert concept in CONCEPTS, f"declared coverage for unknown concept {concept!r}"


def test_pl_concepts_are_conditional_not_always():
    # Register reality: a P&L is only on the public record for P&L-bearing
    # account types. Declaring revenue ALWAYS would falsely promise coverage.
    for concept in ("revenue", "operating_profit", "depreciation_amortisation"):
        cov = COMPANIES_HOUSE_CAPABILITIES.concept_coverage(concept)
        assert cov.tier is CoverageTier.CONDITIONAL
        assert cov.condition is not None
        assert cov.condition.field == "account_type"


def test_always_available_concepts():
    for concept in ("net_assets", "average_employees"):
        assert (
            COMPANIES_HOUSE_CAPABILITIES.concept_coverage(concept).tier
            is CoverageTier.ALWAYS
        )


def test_undeclared_concept_is_never():
    assert (
        COMPANIES_HOUSE_CAPABILITIES.concept_coverage("no_such_concept").tier
        is CoverageTier.NEVER
    )


def test_jurisdiction_lookup():
    assert ENABLED_ADAPTERS
    assert [m.adapter for m in matrices_for_jurisdiction("GB")] == ["companies_house"]
    assert matrices_for_jurisdiction("IE") == []


def test_matrix_is_static_data():
    assert isinstance(COMPANIES_HOUSE_CAPABILITIES, CapabilityMatrix)
