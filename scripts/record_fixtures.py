#!/usr/bin/env python3
"""Record a company's full registry API surface as fixture data.

For each company number given, saves the VERBATIM response body of every
endpoint the ingest pipeline reads — profile, officers, ownership
records and statements, exemptions, security registrations, filing
history — plus document metadata and content for the most recent
accounts filings. 404-when-none responses are recorded as
`<name>.404.json` so the absence itself is fixture data, never
flattened into an empty list.

Output layout (one directory per company under --out):

    <regid>/profile.json
    <regid>/officers.json
    <regid>/psc.json                    (adapter-native endpoint names —
    <regid>/psc-statements.404.json      these files ARE registry data)
    <regid>/exemptions.json
    <regid>/charges.json
    <regid>/filing-history.json
    <regid>/documents/<document_id>.meta.json
    <regid>/documents/<document_id>.xhtml | .pdf

This is the raw half of the company-level golden set (decision record
§14); the hand-verified expected.yaml for each company is written
separately, by a human reading these files.

Requires CH_API_KEY in the environment. Read-only against the registry;
respects the client's rate limiter.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from deal_engine.adapters.companies_house.client import (  # noqa: E402
    IXBRL_TYPE,
    CompaniesHouseClient,
    CompaniesHouseError,
)

ENDPOINTS = [
    ("profile", "/company/{n}"),
    ("officers", "/company/{n}/officers"),
    ("psc", "/company/{n}/persons-with-significant-control"),
    ("psc-statements", "/company/{n}/persons-with-significant-control-statements"),
    ("exemptions", "/company/{n}/exemptions"),
    ("charges", "/company/{n}/charges"),
    ("filing-history", "/company/{n}/filing-history?items_per_page=100"),
]

EXTENSIONS = {IXBRL_TYPE: "xhtml", "application/pdf": "pdf"}


def record_company(client: CompaniesHouseClient, number: str, out: Path, docs: int) -> None:
    company_dir = out / number
    company_dir.mkdir(parents=True, exist_ok=True)

    filing_history: dict = {}
    for name, template in ENDPOINTS:
        url = f"{client.base_url}{template.format(n=number)}"
        response = client._request(url)
        if response.status_code == 200:
            path = company_dir / f"{name}.json"
            body = response.json()
        elif response.status_code == 404:
            path = company_dir / f"{name}.404.json"
            try:
                body = response.json()
            except ValueError:
                body = {"raw": response.text}
        else:
            raise CompaniesHouseError(f"GET {url} -> HTTP {response.status_code}")
        path.write_text(json.dumps(body, indent=1, sort_keys=True), encoding="utf-8")
        print(f"  {path.relative_to(out)}")
        if name == "filing-history" and response.status_code == 200:
            filing_history = body

    accounts = [
        item
        for item in filing_history.get("items", [])
        if item.get("category") == "accounts"
        and (item.get("links") or {}).get("document_metadata")
    ]
    accounts.sort(key=lambda i: (i.get("date") or "", i.get("transaction_id") or ""), reverse=True)
    documents_dir = company_dir / "documents"
    for item in accounts[:docs]:
        url = item["links"]["document_metadata"]
        document_id = url.rstrip("/").rsplit("/", 1)[-1]
        documents_dir.mkdir(parents=True, exist_ok=True)
        metadata = client.get_document_metadata(url)
        (documents_dir / f"{document_id}.meta.json").write_text(
            json.dumps(metadata, indent=1, sort_keys=True), encoding="utf-8"
        )
        try:
            result = client.fetch_document(url)
        except CompaniesHouseError as exc:
            (documents_dir / f"{document_id}.unfetchable.txt").write_text(
                str(exc), encoding="utf-8"
            )
            print(f"  documents/{document_id}: unfetchable ({exc})")
            continue
        ext = EXTENSIONS.get(result.content_type, "bin")
        (documents_dir / f"{document_id}.{ext}").write_bytes(result.content)
        print(f"  documents/{document_id}.{ext} ({len(result.content)} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("companies", nargs="+", help="Company numbers to record")
    parser.add_argument("--out", type=Path, default=Path("evals/golden/companies"))
    parser.add_argument("--docs", type=int, default=3, help="Accounts documents per company")
    args = parser.parse_args()

    api_key = os.environ.get("CH_API_KEY", "")
    if not api_key:
        raise SystemExit("CH_API_KEY is not set")

    with CompaniesHouseClient(api_key) as client:
        for number in args.companies:
            print(f"recording {number}")
            record_company(client, number, args.out, args.docs)


if __name__ == "__main__":
    main()
