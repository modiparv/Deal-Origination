"""Companies House client tests over recorded live responses.

Every mocked behaviour here was observed on the wire during live
verification (docs/live-api-verification-report.md): the 404-means-none
endpoints, the resources-driven Accept negotiation, the 406 on absent
renditions, the 302-to-storage redirect, and 429 retry.
"""

import json
from pathlib import Path

import pytest

httpx = pytest.importorskip(
    "httpx", reason="httpx unavailable; client tests run in CI"
)

from deal_engine.adapters.companies_house.client import (  # noqa: E402
    CompaniesHouseClient,
    CompaniesHouseError,
    RateLimiter,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "companies_house"
DOC_HOST = "https://document-api.company-information.service.gov.uk"


def fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def make_client(handler) -> CompaniesHouseClient:
    return CompaniesHouseClient(
        api_key="test-key",
        transport=httpx.MockTransport(handler),
        rate_limiter=RateLimiter(clock=lambda: 0.0, sleep=lambda s: None),
        backoff=lambda s: None,
    )


class TestEndpoints:
    def test_company_profile(self):
        def handler(request):
            assert request.url.path == "/company/10122954"
            return httpx.Response(200, json=fixture("company-profile-10122954-micro.json"))

        with make_client(handler) as client:
            profile = client.get_company_profile("10122954")
        assert profile["accounts"]["last_accounts"]["type"] == "micro-entity"

    def test_psc_statements_404_means_none(self):
        def handler(request):
            return httpx.Response(404, json={"error": "not-found"})

        with make_client(handler) as client:
            assert client.get_ownership_statements("10122954") == []

    def test_beneficial_owners_from_recorded_response(self):
        def handler(request):
            return httpx.Response(200, json=fixture("psc-10122954.json"))

        with make_client(handler) as client:
            owners = client.get_beneficial_owners("10122954")
        assert {o["kind"] for o in owners} == {"individual-person-with-significant-control"}
        assert owners[0]["natures_of_control"] == ["ownership-of-shares-25-to-50-percent"]
        assert set(owners[0]["date_of_birth"]) == {"month", "year"}

    def test_charges_envelope_spelling(self):
        def handler(request):
            return httpx.Response(200, json=fixture("charges-00445790.json"))

        with make_client(handler) as client:
            charges = client.get_charges("00445790")
        # Live API spells it correctly; the published spec does not.
        assert "unfiltered_count" in charges

    def test_advanced_search_repeats_sic_codes(self):
        def handler(request):
            assert request.url.params.get_list("sic_codes") == ["62012", "62020"]
            return httpx.Response(200, json=fixture("advanced-search-62012.json"))

        with make_client(handler) as client:
            page = client.advanced_search(sic_codes=["62012", "62020"], size=25)
        assert page["hits"] == 116600
        assert "sic_codes" in page["items"][0]

    def test_pagination_walks_all_pages(self):
        items = [{"n": i} for i in range(150)]

        def handler(request):
            start = int(request.url.params.get("start_index", 0))
            per = int(request.url.params["items_per_page"])
            return httpx.Response(
                200,
                json={"items": items[start : start + per], "total_results": len(items)},
            )

        with make_client(handler) as client:
            got = client.get_officers("10122954", items_per_page=100)
        assert [i["n"] for i in got] == list(range(150))

    def test_429_retries_then_succeeds(self):
        calls = {"count": 0}

        def handler(request):
            calls["count"] += 1
            if calls["count"] < 3:
                return httpx.Response(429)
            return httpx.Response(200, json={"ok": True})

        with make_client(handler) as client:
            assert client._get_json("/company/x") == {"ok": True}
        assert calls["count"] == 3


class TestDocuments:
    META_URL = f"{DOC_HOST}/document/Dqa6FnsnOSxkLrg_Y39CgSuK7NiIN5GVRMJBMnJFHGs"

    def test_ixbrl_chosen_when_available_and_redirect_followed(self):
        def handler(request):
            if request.url.path.endswith("/content"):
                assert request.headers["Accept"] == "application/xhtml+xml"
                return httpx.Response(
                    302, headers={"Location": "https://storage.test/doc.xhtml"}
                )
            if request.url.host == "storage.test":
                # Storage must not see forwarded auth (verified: cross-host
                # redirect drops Authorization).
                assert "authorization" not in request.headers
                return httpx.Response(200, content=b"<?xml ix-doc")
            return httpx.Response(200, json=fixture("document-metadata-with-ixbrl.json"))

        with make_client(handler) as client:
            result = client.fetch_document(self.META_URL)
        assert result.content_type == "application/xhtml+xml"
        assert result.content.startswith(b"<?xml")
        assert "application/pdf" in result.available_types

    def test_pdf_fallback_for_paper_filing(self):
        def handler(request):
            if request.url.path.endswith("/content"):
                assert request.headers["Accept"] == "application/pdf"
                return httpx.Response(200, content=b"%PDF-")
            return httpx.Response(200, json=fixture("document-metadata-pdf-only.json"))

        with make_client(handler) as client:
            result = client.fetch_document(self.META_URL)
        assert result.content_type == "application/pdf"
        assert result.available_types == ("application/pdf",)

    def test_no_rendition_fails_loudly(self):
        def handler(request):
            return httpx.Response(200, json={"resources": {}})

        with make_client(handler) as client:
            with pytest.raises(CompaniesHouseError, match="no fetchable rendition"):
                client.fetch_document(self.META_URL)


class TestRateLimiter:
    def test_sleeps_only_when_budget_exhausted(self):
        now = {"t": 0.0}
        slept: list[float] = []
        limiter = RateLimiter(
            budget=2, window=300.0, clock=lambda: now["t"], sleep=slept.append
        )
        limiter.acquire()
        limiter.acquire()
        assert slept == []
        limiter.acquire()  # third within window -> must wait out the window
        assert slept and slept[0] == pytest.approx(300.0)

    def test_window_expiry_frees_budget(self):
        now = {"t": 0.0}
        slept: list[float] = []
        limiter = RateLimiter(
            budget=2, window=300.0, clock=lambda: now["t"], sleep=slept.append
        )
        limiter.acquire()
        limiter.acquire()
        now["t"] = 301.0
        limiter.acquire()
        assert slept == []
