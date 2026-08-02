"""Adapter mapping: registry JSON → canonical dicts with deterministic ids.

Runs over the recorded live fixtures, so every asserted field shape was
observed on the wire. Pure functions — no pydantic, no network — so this
suite runs in the restricted local environment too.
"""

import json
from pathlib import Path

from deal_engine.adapters.companies_house import mapping, sic

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "companies_house"


def fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class TestCompanyMapping:
    def test_micro_profile(self):
        mapped = mapping.map_company(fixture("company-profile-10122954-micro.json"))
        assert mapped["id"] == "gb:10122954"
        assert mapped["jurisdiction"] == "GB"
        assert mapped["registration_id"] == "10122954"
        assert mapped["classification_codes"] == ["47910", "62012"]
        assert mapped["classification_taxonomy"] == "sic_2007"
        assert mapped["incorporation_date"] == "2016-04-14"
        assert mapped["name_variants"] == []

    def test_previous_names_become_variants(self):
        mapped = mapping.map_company(fixture("company-profile-08140876-dormant.json"))
        assert len(mapped["name_variants"]) == 4
        assert "WE TECHNOLOGY (UK) LIMITED" in mapped["name_variants"]


class TestOfficerMapping:
    def test_person_number_keys_the_appointment(self):
        item = fixture("officers-10122954.json")["items"][0]
        mapped = mapping.map_officer(item, "gb:10122954")
        assert mapped["appointment_id"] == "207133220001:2016-04-14"
        assert mapped["id"] == "gb:10122954:officer:207133220001:2016-04-14"
        assert mapped["officer_id"] == "207133220001"
        assert mapped["role"] == "director"
        assert mapped["dob_month"] == 9 and mapped["dob_year"] == 1984


class TestBeneficialOwnerMapping:
    def test_external_id_from_links_self(self):
        item = fixture("psc-10122954.json")["items"][0]
        mapped = mapping.map_beneficial_owner(item, "gb:10122954")
        assert mapped["external_id"] != "unknown"
        assert mapped["id"] == f"gb:10122954:bo:{mapped['external_id']}"
        assert mapped["control_natures"] == ["ownership-of-shares-25-to-50-percent"]
        assert mapped["dob_month"] is not None and mapped["dob_year"] is not None


class TestFilingMapping:
    def test_accounts_filing(self):
        item = fixture("filing-history-accounts-00445790.json")["items"][0]
        mapped = mapping.map_filing(item, "gb:00445790")
        assert mapped["id"] == "gb:00445790:filing:MzUzNDMwNDQ5M2FkaXF6a2N4"
        assert mapped["filing_date"] == "2026-07-25"
        assert mapped["document_id"] == "-uIFIZvVQM2_WxuNYmjA10Fv96C0Yuxb-wNWhAqNezY"
        assert mapped["paper_filed"] is True

    def test_account_type_parsed_from_description(self):
        assert mapping.account_type_from_description("accounts-with-accounts-type-group") == "group"
        assert (
            mapping.account_type_from_description("accounts-with-accounts-type-micro-entity")
            == "micro-entity"
        )
        assert mapping.account_type_from_description("confirmation-statement") is None
        assert mapping.account_type_from_description(None) is None


class TestSecurityInterestMapping:
    def test_pre_2013_charge_falls_back_to_number(self):
        item = fixture("charges-00445790.json")["items"][0]
        mapped = mapping.map_security_interest(item, "gb:00445790")
        # Pre-April-2013 charges carry no charge_code (verified live).
        assert mapped["external_id"] == "num-9"
        assert mapped["status"] == "outstanding"
        assert mapped["secured_parties"][0].startswith("Tesco Trustee Company")
        assert mapped["details"]["description"].startswith("Right title benefit")


class TestExemptionsMapping:
    def test_live_envelope_shape(self):
        mapped = mapping.map_exemptions(fixture("exemptions-00445790.json"), "gb:00445790")
        by_id = {m["id"]: m for m in mapped}
        key = "gb:00445790:exemption:psc_exempt_as_trading_on_uk_regulated_market"
        assert key in by_id
        assert by_id[key]["exemption_type"] == "psc-exempt-as-trading-on-uk-regulated-market"
        assert by_id[key]["items"] == [{"exempt_from": "2018-06-18"}]

    def test_none_payload_maps_to_nothing(self):
        assert mapping.map_exemptions(None, "gb:x") == []


class TestOwnershipStatementMapping:
    def test_external_id_from_links_self(self):
        item = {
            "statement": "no-individual-or-entity-with-signficant-control",
            "notified_on": "2017-01-01",
            "links": {"self": "/company/1/persons-with-significant-control-statements/abc123"},
        }
        mapped = mapping.map_ownership_statement(item, "gb:1")
        assert mapped["id"] == "gb:1:stmt:abc123"
        # The registry's canonical enum misspells "significant" — stored verbatim.
        assert "signficant" in mapped["statement"]


class TestSicExpansion:
    def test_wildcards_expand_to_exact_codes(self):
        codes = sic.expand(["620*"])
        assert set(codes) == {"62011", "62012", "62020", "62030", "62090"}

    def test_exact_codes_pass_through_only_if_real(self):
        assert sic.expand(["62012"]) == ["62012"]
        assert sic.expand(["99999x"]) == []

    def test_expansion_deduplicates(self):
        assert sic.expand(["620*", "62012"]) == sic.expand(["620*"])

    def test_matches_any(self):
        assert sic.matches_any("62012", ["620*"])
        assert sic.matches_any("62012", ["62012"])
        assert not sic.matches_any("64191", ["620*"])
        assert sic.matches_any("64191", ["6419*"])


class TestProductionSoftware:
    def _doc(self, text_facts):
        from deal_engine.parse.ixbrl import ParsedDocument, TextFact

        return ParsedDocument(
            facts=[],
            namespaces={},
            error_count=0,
            text_facts=[TextFact(*tf) for tf in text_facts],
        )

    def test_reads_name_production_software_by_local_name(self):
        doc = self._doc(
            [
                ("http://xbrl.frc.org.uk/cd/2024-01-01/business", "bus",
                 "NameProductionSoftware", "Digita Accounts Production Advanced"),
            ]
        )
        assert mapping.production_software(doc) == "Digita Accounts Production Advanced"

    def test_prefix_is_irrelevant(self):
        # Older filings use uk-bus:, and prefixes are vendor-arbitrary.
        doc = self._doc(
            [("", "uk-bus", "NameProductionSoftware", "Companies House")]
        )
        assert mapping.production_software(doc) == "Companies House"

    def test_absent_or_empty_tag_yields_none(self):
        assert mapping.production_software(self._doc([])) is None
        empty = self._doc([("", "bus", "NameProductionSoftware", "")])
        assert mapping.production_software(empty) is None
