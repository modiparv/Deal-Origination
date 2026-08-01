"""DoD #5: an LLM-authored string containing an unresolvable numeral fails
render. Pure string layer — no LLM, no pipeline dependency."""

import pytest

from deal_engine.render.validator import (
    RenderError,
    substitute_markers,
    validate_rendered_text,
)

KNOWN = {"F001", "F002", "F-growth"}


def violations(text, allowed=()):
    return validate_rendered_text(text, KNOWN, allowed)


class TestHonestProsePasses:
    def test_markers_resolve(self):
        assert violations("Revenue of {fig:F001} against {fig:F002}.") == []

    def test_marker_with_format_hint(self):
        assert violations("Revenue grew {fig:F-growth:pct} over the period.") == []

    def test_years_pass(self):
        assert violations("Incorporated in 1998; FY2024 accounts filed.") == []

    def test_iso_dates_pass(self):
        assert violations("Accounts made up to 2024-03-31.") == []

    def test_small_counts_pass(self):
        assert violations("Three of 5 directors are family members.") == []

    def test_mandate_verbatim_numerals_pass(self):
        assert violations(
            "Above the £1,000,000 floor set by the mandate.",
            allowed={"1000000"},
        ) == []


class TestDishonestProseFails:
    def test_bare_financial_amount_fails(self):
        assert violations("Revenue of £4.2m in the latest period.")

    def test_computed_percentage_fails(self):
        # "grew 12%" is exactly the banned LLM arithmetic: growth must
        # pre-exist as a derived figure and be cited by marker.
        assert violations("Revenue grew 12% year on year.")

    def test_currency_adjacent_single_digit_fails(self):
        # The single-digit allowance must not leak financial amounts.
        assert violations("EBITDA of £1m and rising.")

    def test_reformatted_mandate_threshold_fails(self):
        # "£1m" is a reformatting of 1_000_000, not a verbatim echo.
        assert violations("Above the £1m floor.", allowed={"1000000"})

    def test_unresolved_marker_fails(self):
        vs = violations("Revenue of {fig:F999}.")
        assert [v.kind for v in vs] == ["unresolved_marker"]

    def test_multi_digit_count_fails(self):
        assert violations("The company employs 47 people.")


class TestSubstitution:
    def test_substitutes_display_values(self):
        out = substitute_markers(
            "Revenue of {fig:F001} in FY2024.",
            {"F001": "£4,200,000", "F002": "£1,000,000"},
        )
        assert out == "Revenue of £4,200,000 in FY2024."

    def test_refuses_to_render_with_violations(self):
        with pytest.raises(RenderError) as exc_info:
            substitute_markers("Revenue of £4.2m.", {"F001": "x"})
        assert exc_info.value.violations

    def test_refuses_unresolved_marker(self):
        with pytest.raises(RenderError):
            substitute_markers("{fig:F999}", {"F001": "x"})
