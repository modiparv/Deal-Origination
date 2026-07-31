import pytest

pytest.importorskip(
    "pydantic",
    reason="pydantic v2 unavailable in this environment (PyPI blocked); "
    "the full Phase 0 gate requires it — see PLAN.md §8",
)

from pathlib import Path  # noqa: E402

from deal_engine.jurisdiction import load_jurisdictions  # noqa: E402
from deal_engine.mandate.loader import MandateLoadError, load_mandate, mandate_numerals  # noqa: E402
from deal_engine.mandate.validator import Severity, validate_mandate  # noqa: E402
from deal_engine.models.mode import ModeRequirement, ScreeningMode  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EXAMPLE = ROOT / "mandates" / "example-lmm-gb.yaml"
FIXTURES = ROOT / "tests" / "fixtures" / "mandates"

# Real profiles plus the signal-only test jurisdiction (XS).
PROFILES = {
    **load_jurisdictions(ROOT / "jurisdictions"),
    **load_jurisdictions(ROOT / "tests" / "fixtures" / "jurisdictions"),
}


def report_for(path):
    return validate_mandate(load_mandate(path), jurisdictions=PROFILES)


class TestJurisdictionProfiles:
    def test_gb_profile_loads(self):
        gb = load_jurisdictions(ROOT / "jurisdictions")["GB"]
        assert set(gb.available_modes) == {ScreeningMode.FINANCIAL, ScreeningMode.SIGNAL}
        assert gb.classification_taxonomy == "sic_2007"
        assert gb.validate_registration_id("00000006")
        assert gb.validate_registration_id("SC123456")
        assert not gb.validate_registration_id("1234")
        assert gb.filing_lag is not None and gb.filing_lag.max_months == 21


class TestExampleMandate:
    def test_loads(self):
        mandate = load_mandate(EXAMPLE)
        assert mandate.id == "lmm-gb-buyout"
        assert mandate.geography.include == ["GB"]
        assert mandate.size.primary.min == 1_000_000  # YAML underscore literal
        assert set(mandate.required_modes) == {ScreeningMode.FINANCIAL, ScreeningMode.SIGNAL}
        by_id = {d.id: d for d in mandate.rubric}
        assert by_id["financial_quality"].requires_mode is ModeRequirement.FINANCIAL
        assert by_id["market_position"].requires_mode is ModeRequirement.ANY

    def test_validates_with_conditional_coverage_warning(self):
        report = report_for(EXAMPLE)
        assert report.ok, [str(i) for i in report.errors]
        codes = {i.code for i in report.warnings}
        assert "conditional_coverage" in codes
        # The warning carries the machine-readable condition for the
        # coverage report to evaluate per company before ingest.
        warning = next(i for i in report.warnings if i.code == "conditional_coverage")
        assert warning.data["condition_field"] == "account_type"
        assert "full" in warning.data["condition_allowed"]


class TestBrokenMandates:
    def test_gb_ie_rejected_naming_concept_and_jurisdiction(self):
        report = report_for(FIXTURES / "gb-ie-ebitda.yaml")
        assert not report.ok
        codes = {i.code for i in report.errors}
        assert "unknown_jurisdiction" in codes  # IE has no profile
        assert "no_adapter_for_jurisdiction" in codes
        assert "concept_unavailable" in codes
        # The amended Phase 0 gate: errors name the specific unsatisfied
        # concept and jurisdiction.
        messages = " | ".join(i.message for i in report.errors)
        assert "'IE'" in messages
        assert "operating_profit" in messages
        assert "ebitda" in messages

    def test_financial_mode_over_signal_only_jurisdiction_rejected(self):
        report = report_for(FIXTURES / "financial-mode-over-signal-only.yaml")
        assert not report.ok
        issue = next(i for i in report.errors if i.code == "mode_unavailable")
        # Names the modes, the jurisdiction, and the reason.
        assert "'XS'" in issue.message
        assert "financial" in issue.message
        assert "signal" in issue.message
        assert issue.data["jurisdiction"] == "XS"
        assert issue.data["available_modes"] == ["signal"]

    def test_bad_weights_rejected(self):
        report = report_for(FIXTURES / "bad-weights.yaml")
        assert any(i.code == "rubric_weights" for i in report.errors)

    def test_unknown_taxonomy_rejected(self):
        report = report_for(FIXTURES / "unknown-taxonomy.yaml")
        assert any(i.code == "unknown_taxonomy" for i in report.errors)

    def test_unknown_signal_rejected(self):
        report = report_for(FIXTURES / "unknown-signal.yaml")
        assert any(i.code == "unknown_signal" for i in report.errors)

    def test_undeclared_modelled_metric_rejected(self):
        # enterprise_value is unobservable for private companies; a mandate
        # using it must declare basis: modelled with a named model.
        report = report_for(FIXTURES / "undeclared-modelled.yaml")
        assert any(i.code == "unobservable_metric" for i in report.errors)
        message = next(i for i in report.errors if i.code == "unobservable_metric").message
        assert "enterprise_value" in message
        assert "modelled" in message

    def test_missing_file_raises_load_error(self):
        with pytest.raises(MandateLoadError, match="cannot read"):
            load_mandate(FIXTURES / "does-not-exist.yaml")


class TestSignalParams:
    def test_bad_signal_params_rejected(self, tmp_path):
        text = (EXAMPLE).read_text().replace("beneficial_owner_age_threshold: 58", "beneficial_owner_age_threshold: 300")
        bad = tmp_path / "bad-params.yaml"
        bad.write_text(text)
        report = report_for(bad)
        assert any(i.code == "bad_signal_params" for i in report.errors)


class TestMandateNumerals:
    def test_thresholds_extracted_for_render_whitelist(self):
        numerals = mandate_numerals(load_mandate(EXAMPLE))
        assert "1000000" in numerals or "1e+06" in numerals
        assert "3.5" in numerals
        assert "58" in numerals


def test_severity_enum_has_no_silent_third_state():
    assert {s.value for s in Severity} == {"error", "warning"}
