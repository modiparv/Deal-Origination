import pytest

from deal_engine.concepts import CONCEPTS
from deal_engine.derive.registry import DERIVED_METRICS, resolve_required_concepts


def test_declarations_reference_known_names():
    for decl in DERIVED_METRICS.values():
        for inp in decl.inputs:
            assert inp in CONCEPTS or inp in DERIVED_METRICS, (
                f"{decl.name}: input {inp!r} is neither a concept nor a metric"
            )


def test_ebitda_resolves_to_pl_concepts():
    assert resolve_required_concepts("ebitda") == frozenset(
        {"operating_profit", "depreciation_amortisation"}
    )


def test_nested_metric_flattens():
    # ebitda_margin -> ebitda -> operating_profit + depreciation_amortisation
    assert resolve_required_concepts("ebitda_margin") == frozenset(
        {"operating_profit", "depreciation_amortisation", "revenue"}
    )


def test_unknown_metric_raises():
    with pytest.raises(KeyError, match="unknown derived metric"):
        resolve_required_concepts("enterprise_value")


def test_cycle_detection(monkeypatch):
    from deal_engine.derive import registry as reg

    a = reg.DerivedMetricDecl("metric_a", ("metric_b",), "test")
    b = reg.DerivedMetricDecl("metric_b", ("metric_a",), "test")
    monkeypatch.setitem(reg.DERIVED_METRICS, "metric_a", a)
    monkeypatch.setitem(reg.DERIVED_METRICS, "metric_b", b)
    with pytest.raises(ValueError, match="cycle"):
        reg.resolve_required_concepts("metric_a")
