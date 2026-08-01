# Live API surface verification — run locally, report back

Phase 1 step zero. The sandbox cannot reach Companies House (fixed
network policy), so these requests run on your machine. ~25 calls total,
well inside the 600-per-5-minute limit. Nothing here writes anything.

Setup (your machine):

```bash
export CH_API_KEY=...   # your key; lives in your local .env, never committed
CH="https://api.company-information.service.gov.uk"
```

Auth is HTTP Basic with the key as username, empty password: `-u "$CH_API_KEY:"`.

**What to report for every request:** the HTTP status code plus the
specific items listed. Paste raw JSON where asked — it is public
register data. Where a step says SAVE, keep the file: those become the
first golden fixtures.

---

1. **Auth smoke test + large-filer profile** (Tesco PLC):
   ```bash
   curl -sS -D r1.headers -u "$CH_API_KEY:" "$CH/company/00445790" -o r1.json
   ```
   Report: status; every `X-Ratelimit-*` header from `r1.headers`
   verbatim; from `r1.json`: `type`, `jurisdiction`, `sic_codes`, the
   full `accounts` object, and the key names of `links`.

2. **Advanced search** (the universe-enumeration endpoint):
   ```bash
   curl -sS -u "$CH_API_KEY:" "$CH/advanced-search/companies?sic_codes=62012&company_status=active&size=25" -o r2.json
   ```
   Report: status; the `hits` value; the key names of `items[0]`;
   whether items carry `sic_codes`; whether items carry ANY accounts
   fields (expected: none). Paste `items[0..2]` raw.

3. **Find the two probe companies.** From R2's items, fetch profiles
   (`$CH/company/{number}`) until you have:
   - **SMALLCO** — `accounts.last_accounts.type` in
     {`micro-entity`, `total-exemption-full`, `total-exemption-small`, `small`, `unaudited-abridged`}
   - **FULLCO** — `accounts.last_accounts.type` in {`full`, `medium`, `group`}
   Report: both company numbers, each profile's full
   `accounts.last_accounts` object verbatim, `has_charges`, and how many
   profiles you had to try (that ratio is itself coverage data).

4. **Officers** (SMALLCO):
   ```bash
   curl -sS -u "$CH_API_KEY:" "$CH/company/{SMALLCO}/officers?items_per_page=100" -o r4.json
   ```
   Report: `total_results`, `active_count`; key names of `items[0]`; the
   exact shape of `items[0].date_of_birth`. Then repeat with
   `items_per_page=200` and report whether it errors or silently caps
   (compare `items_per_page` echoed in the response).

5. **Beneficial owners / PSC** (SMALLCO):
   ```bash
   curl -sS -u "$CH_API_KEY:" "$CH/company/{SMALLCO}/persons-with-significant-control" -o r5.json
   curl -sS -u "$CH_API_KEY:" "$CH/company/{SMALLCO}/persons-with-significant-control-statements" -o r5s.json
   ```
   Report: both statuses (404 is informative); `kind` values;
   `natures_of_control` strings VERBATIM; any corporate owner's
   `identification` object; any `statement` values VERBATIM (we expect
   the register's canonical misspelling `...-signficant-...` — confirm
   or refute). Paste both JSON bodies.

6. **Filing history** (FULLCO):
   ```bash
   curl -sS -u "$CH_API_KEY:" "$CH/company/{FULLCO}/filing-history?category=accounts&items_per_page=10" -o r6.json
   ```
   Report: `total_count`; key names of `items[0]`; the `type` values
   seen; one example `transaction_id` verbatim; one example
   `links.document_metadata` value VERBATIM (we need the exact host).
   Paste `items[0]` raw.

7. **Document metadata** (newest accounts filing from R6; use its
   `links.document_metadata` URL exactly as returned):
   ```bash
   curl -sS -u "$CH_API_KEY:" "{document_metadata_url}" -o r7.json
   ```
   Report: status; the full `resources` object VERBATIM (MIME types +
   content lengths); the `links` object.

8. **Document content — the redirect dance** (same URL + `/content`):
   ```bash
   # (a) do NOT follow the redirect:
   curl -sS -i -u "$CH_API_KEY:" -H "Accept: application/xhtml+xml" "{document_metadata_url}/content" | head -30
   # (b) follow the Location manually WITHOUT auth:
   curl -sS -o fullco-accounts.xhtml -w '%{http_code}\n' "{location_from_a}"
   # (c) one-shot with -L and auth, to document whether auth-forwarding breaks:
   curl -sSL -u "$CH_API_KEY:" -H "Accept: application/xhtml+xml" -o /dev/null -w '%{http_code}\n' "{document_metadata_url}/content"
   ```
   Report: (a) status + `Location` header host; (b) status + first ~300
   chars of `fullco-accounts.xhtml` (expect XHTML with `ix:` tags);
   (c) status — success or the S3 double-auth failure. SAVE
   `fullco-accounts.xhtml`.

9. **Repeat 6–8 for SMALLCO's latest accounts.** Report especially:
   does `resources` contain `application/xhtml+xml` at all, and the
   `accounts.last_accounts.type` it corresponds to. SAVE
   `smallco-accounts.xhtml` (or note it is PDF-only — that is a finding,
   not a failure).

10. **Security interests / charges** (Tesco, which has many):
    ```bash
    curl -sS -u "$CH_API_KEY:" "$CH/company/00445790/charges?items_per_page=5" -o r10.json
    ```
    Report: the envelope key names VERBATIM (we expect the documented
    misspelling `unfiletered_count` — confirm or refute); key names of
    `items[0]`; the shapes of `persons_entitled` and `particulars`.
    Paste `items[0]` raw.

11. **Exemptions**:
    ```bash
    curl -sS -o /dev/null -w '%{http_code}\n' -u "$CH_API_KEY:" "$CH/company/00445790/exemptions"
    ```
    Report: status; if 200, the body. (404 for a non-exempt company is
    itself the answer.)

12. *(Optional)* If any R2 company's profile showed
    `has_insolvency_history: true`, fetch `$CH/company/{n}/insolvency`
    and report the case `type`/`dates` shapes.

---

Hand back: the numbered report, the pasted JSON bodies (2, 5, 6, 7, 10),
and the two saved `.xhtml` files. I fold the findings into the adapter
client and concept map, and the saved documents seed
`evals/golden/filings/`. A `scripts/record_fixtures.py` (Phase 1) will
then systematise fixture capture — auth headers stripped — so the golden
set grows without hand-editing.
