"""Companies House REST client.

Thin and faithful to the live-verified surface
(docs/live-api-verification-report.md): HTTP Basic with the key as
username; 600 requests per 5-minute window with `x-ratelimit-*` response
headers (`remain`, not `remaining`); PSC statements and exemptions
return 404 when none exist; accounts documents are fetched via the
absolute `links.document_metadata` URL, whose `resources` object decides
the Accept header — requesting a type not present returns 406, and the
content endpoint 302-redirects to storage which must be followed without
forwarding auth (httpx drops Authorization on cross-host redirects by
default).

The client returns parsed JSON dictionaries; mapping into canonical
models is the ingest layer's job.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable, Iterator

import httpx

API_BASE = "https://api.company-information.service.gov.uk"

IXBRL_TYPE = "application/xhtml+xml"
PDF_TYPE = "application/pdf"

# Client-side budget kept below the server's 600/5min to leave headroom.
DEFAULT_BUDGET = 500
WINDOW_SECONDS = 300.0


class CompaniesHouseError(Exception):
    pass


class RateLimiter:
    """Token bucket over a rolling window, with injectable clock/sleep so
    tests never wait."""

    def __init__(
        self,
        budget: int = DEFAULT_BUDGET,
        window: float = WINDOW_SECONDS,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.budget = budget
        self.window = window
        self._clock = clock
        self._sleep = sleep
        self._stamps: list[float] = []

    def acquire(self) -> None:
        now = self._clock()
        cutoff = now - self.window
        self._stamps = [s for s in self._stamps if s > cutoff]
        if len(self._stamps) >= self.budget:
            wait = self._stamps[0] + self.window - now
            if wait > 0:
                self._sleep(wait)
        self._stamps.append(self._clock())


@dataclass(frozen=True)
class DocumentResult:
    content_type: str
    content: bytes
    document_metadata_url: str
    available_types: tuple[str, ...]


class CompaniesHouseClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = API_BASE,
        rate_limiter: RateLimiter | None = None,
        transport: httpx.BaseTransport | None = None,
        max_retries: int = 3,
        backoff: Callable[[float], None] = time.sleep,
        timeout: float = 30.0,
    ):
        if not api_key:
            raise CompaniesHouseError("api_key is required")
        self.base_url = base_url.rstrip("/")
        self.rate_limiter = rate_limiter or RateLimiter()
        self.max_retries = max_retries
        self._backoff = backoff
        self._client = httpx.Client(
            auth=(api_key, ""),
            follow_redirects=True,  # auth is not forwarded cross-host
            timeout=timeout,
            transport=transport,
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "CompaniesHouseClient":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- low level ----------------------------------------------------------

    def _request(self, url: str, accept: str | None = None) -> httpx.Response:
        headers = {"Accept": accept} if accept else {}
        attempt = 0
        while True:
            self.rate_limiter.acquire()
            response = self._client.get(url, headers=headers)
            if response.status_code == 429 and attempt < self.max_retries:
                attempt += 1
                self._backoff(2.0**attempt)
                continue
            return response

    def _get_json(self, path: str, not_found: Any = ...) -> Any:
        url = path if path.startswith("http") else f"{self.base_url}{path}"
        response = self._request(url)
        if response.status_code == 404 and not_found is not ...:
            return not_found
        if response.status_code != 200:
            raise CompaniesHouseError(
                f"GET {url} -> HTTP {response.status_code}: {response.text[:200]}"
            )
        return response.json()

    # -- public data --------------------------------------------------------

    def get_company_profile(self, registration_id: str) -> dict:
        return self._get_json(f"/company/{registration_id}")

    def get_officers(self, registration_id: str, items_per_page: int = 100) -> list[dict]:
        return list(
            self._paginate(f"/company/{registration_id}/officers", items_per_page)
        )

    def get_beneficial_owners(self, registration_id: str) -> list[dict]:
        data = self._get_json(
            f"/company/{registration_id}/persons-with-significant-control",
            not_found={"items": []},
        )
        return data.get("items", [])

    def get_ownership_statements(self, registration_id: str) -> list[dict]:
        # 404 means no statements exist — verified live, not an error.
        data = self._get_json(
            f"/company/{registration_id}/persons-with-significant-control-statements",
            not_found={"items": []},
        )
        return data.get("items", [])

    def get_exemptions(self, registration_id: str) -> dict | None:
        # Live shape: {"exemptions": {<snake_key>: {items, exemption_type}}}
        return self._get_json(f"/company/{registration_id}/exemptions", not_found=None)

    def get_charges(self, registration_id: str) -> dict:
        # Envelope is correctly spelled `unfiltered_count` in the live API;
        # the published spec repo misspells it. Tolerate both downstream.
        return self._get_json(
            f"/company/{registration_id}/charges",
            not_found={"items": [], "total_count": 0},
        )

    def get_filing_history(
        self, registration_id: str, category: str | None = None, items_per_page: int = 100
    ) -> list[dict]:
        path = f"/company/{registration_id}/filing-history"
        if category:
            path += f"?category={category}"
        return list(self._paginate(path, items_per_page))

    def advanced_search(
        self,
        sic_codes: list[str],
        company_status: str = "active",
        size: int = 100,
        start_index: int = 0,
        incorporated_from: str | None = None,
        incorporated_to: str | None = None,
    ) -> dict:
        params = [("company_status", company_status), ("size", str(size))]
        params += [("sic_codes", c) for c in sic_codes]
        if start_index:
            params.append(("start_index", str(start_index)))
        if incorporated_from:
            params.append(("incorporated_from", incorporated_from))
        if incorporated_to:
            params.append(("incorporated_to", incorporated_to))
        query = "&".join(f"{k}={v}" for k, v in params)
        return self._get_json(f"/advanced-search/companies?{query}")

    def _paginate(self, path: str, items_per_page: int) -> Iterator[dict]:
        sep = "&" if "?" in path else "?"
        start = 0
        while True:
            page = self._get_json(
                f"{path}{sep}items_per_page={items_per_page}&start_index={start}"
            )
            items = page.get("items", [])
            yield from items
            total = page.get("total_results") or page.get("total_count") or 0
            start += len(items)
            if not items or start >= total:
                return

    # -- documents ----------------------------------------------------------

    def get_document_metadata(self, document_metadata_url: str) -> dict:
        # filing-history links.document_metadata is an absolute URL on the
        # (hyphenated) document API host — never construct it.
        return self._get_json(document_metadata_url)

    def fetch_document(self, document_metadata_url: str) -> DocumentResult:
        """Fetch the best available rendition.

        The metadata `resources` object decides the Accept header: iXBRL
        when present, otherwise PDF. Requesting an absent type returns
        406 (verified live on a paper-filed group filing).
        """
        metadata = self.get_document_metadata(document_metadata_url)
        available = tuple(sorted((metadata.get("resources") or {}).keys()))
        if IXBRL_TYPE in available:
            accept = IXBRL_TYPE
        elif PDF_TYPE in available:
            accept = PDF_TYPE
        else:
            raise CompaniesHouseError(
                f"document {document_metadata_url} offers no fetchable rendition "
                f"(resources: {available})"
            )
        response = self._request(f"{document_metadata_url}/content", accept=accept)
        if response.status_code != 200:
            raise CompaniesHouseError(
                f"document content fetch -> HTTP {response.status_code}"
            )
        return DocumentResult(
            content_type=accept,
            content=response.content,
            document_metadata_url=document_metadata_url,
            available_types=available,
        )
