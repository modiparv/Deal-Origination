"""Unit tests for parse-layer helpers, pinned to ixbrlparse's ACTUAL
data shapes (read from its source, not its docs):

- IXBRL.namespaces values are LISTS — the library splits the xmlns
  attribute value on spaces, so a single URI arrives as ["<uri>"]. The
  first CI run of the golden eval failed precisely because the resolver
  stringified the list.
- context.segments entries are dicts of the form
  {"tag": <element name>, "value": <member text>, **attrs} where the
  attrs include the "dimension" attribute as a QName.
"""

from decimal import Decimal

from deal_engine.parse.figures import extract_figures
from deal_engine.parse.ixbrl import (
    ParsedDocument,
    RawFact,
    _resolve_namespace,
    _scan_xmlns_bindings,
    _segment_dimensions,
    _strip_prefix,
)

FRC_2019 = "http://xbrl.frc.org.uk/fr/2019-01-01/core"
FRC_2024 = "http://xbrl.frc.org.uk/fr/2024-01-01/core"


class TestNamespaceResolution:
    def test_list_valued_namespaces_resolve_to_first_uri(self):
        namespaces = {"xmlns:uk-core": [FRC_2019]}
        assert _resolve_namespace("uk-core", namespaces) == FRC_2019

    def test_plain_string_values_also_accepted(self):
        assert _resolve_namespace("uk-core", {"xmlns:uk-core": FRC_2019}) == FRC_2019
        assert _resolve_namespace("uk-core", {"uk-core": FRC_2019}) == FRC_2019

    def test_unknown_prefix_resolves_empty(self):
        assert _resolve_namespace("mystery", {}) == ""


class TestDocumentWideBindingFallback:
    """Some production software (observed: Digita Accounts Production
    Advanced) declares xmlns:core per element instead of on the root, so
    ixbrlparse's root-level namespaces dict never sees it. Resolution
    falls back to the document-wide scan — but only when the binding is
    unambiguous."""

    def test_scan_collects_per_element_declarations(self):
        content = (
            '<html xmlns="http://www.w3.org/1999/xhtml">'
            f'<ix:nonFraction xmlns:core="{FRC_2024}" name="core:Equity"/>'
            f'<ix:nonFraction xmlns:core="{FRC_2024}" name="core:CashBankOnHand"/>'
            "</html>"
        )
        assert _scan_xmlns_bindings(content) == {"core": {FRC_2024}}

    def test_fallback_resolves_prefix_missing_from_root(self):
        bindings = {"core": {FRC_2024}}
        assert _resolve_namespace("core", {}, bindings) == FRC_2024

    def test_root_declaration_wins_over_fallback(self):
        bindings = {"core": {FRC_2024}}
        assert (
            _resolve_namespace("core", {"xmlns:core": [FRC_2019]}, bindings)
            == FRC_2019
        )

    def test_ambiguous_binding_stays_unresolved(self):
        bindings = {"core": {FRC_2019, FRC_2024}}
        assert _resolve_namespace("core", {}, bindings) == ""


class TestSegmentDimensions:
    def test_ixbrlparse_segment_shape(self):
        class Ctx:
            segments = [
                {
                    "tag": "xbrldi:explicitMember",
                    "value": "uk-core:WithinOneYear",
                    "dimension": "uk-core:MaturitiesOrExpirationPeriodsDimension",
                }
            ]

        assert _segment_dimensions(Ctx()) == {
            "MaturitiesOrExpirationPeriodsDimension": "WithinOneYear"
        }

    def test_strip_prefix(self):
        assert _strip_prefix("uk-core:FixedAssets") == "FixedAssets"
        assert _strip_prefix("FixedAssets") == "FixedAssets"


class TestExtractionAgainstConceptMap:
    def _fact(self, local, value, dims=None, instant="2022-04-30"):
        return RawFact(
            namespace=FRC_2019,
            prefix="uk-core",
            local_name=local,
            value=Decimal(value),
            unit="GBP",
            decimals=2,
            period_start=None,
            period_end=None,
            instant=instant,
            dimensions=dims or {},
            raw_text=value,
        )

    def test_dimensional_creditors_and_direct_concepts_map(self):
        from deal_engine.adapters.companies_house.concept_map import ConceptMap

        doc = ParsedDocument(
            facts=[
                self._fact("FixedAssets", "1084"),
                self._fact(
                    "Creditors",
                    "500",
                    dims={"MaturitiesOrExpirationPeriodsDimension": "WithinOneYear"},
                ),
                self._fact(
                    "Creditors",
                    "1960",
                    dims={"MaturitiesOrExpirationPeriodsDimension": "AfterOneYear"},
                ),
                self._fact("SomethingNovel", "7"),
            ],
            namespaces={"uk-core": FRC_2019},
            error_count=0,
        )
        figures = extract_figures(doc, ConceptMap.load())
        assert figures.present_concepts == {
            "fixed_assets",
            "creditors_within_one_year",
            "creditors_after_one_year",
        }
        assert figures.unmapped == {"uk-core:SomethingNovel": 1}
        assert figures.quality_flags == []

    def test_duplicate_disagreement_is_flagged(self):
        from deal_engine.adapters.companies_house.concept_map import ConceptMap

        doc = ParsedDocument(
            facts=[
                self._fact("FixedAssets", "1084"),
                self._fact("FixedAssets", "9999"),
            ],
            namespaces={"uk-core": FRC_2019},
            error_count=0,
        )
        figures = extract_figures(doc, ConceptMap.load())
        assert any("disagree" in flag for flag in figures.quality_flags)
