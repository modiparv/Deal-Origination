#!/usr/bin/env python3
"""Export the static site's data bundle from an engine database.

The site is a read-only view over the whole store, so the export has to
scale past "one JSON file": it writes a compact per-company INDEX (what
the SCREEN needs for every company at once) plus BUCKETED full records
(what the COMPANY, TRACE and COMPARE pages fetch on demand, one small
file per bucket). The build downloads one bundle and unpacks it.

Produces, in --out:

    manifest.json        small; committed to git as web/data/manifest.json
                         (run id, totals, bundle sha-256 the build verifies)
    index.json           one row per company
    c/<bucket>.json      full records for the companies in one bucket
    ops.json             store operations: parse failures, parse yield by
                         filing software, coverage by classification code,
                         run history
    web-data.jsonl.gz    the bundle: manifest + index + ops + buckets, one
                         record per line, "<kind>\\t<name>\\t<json>"

Everything here is a verbatim copy or a mechanical aggregate (counts,
max/min over dates, latest-observation selection) of rows already in the
audit trail. Nothing financial is computed: margins, growth and scores
are Phase 2 derived figures and are absent by design — the frontend
renders their absence states. Date arithmetic (ages, staleness, "within
the last N months") is left to the renderer so that the bundle carries
observations, not judgements about them.

Usage:
    python scripts/export_web_data.py data/engine.db --out /tmp/web-data \\
        --bundle-url https://github.com/<owner>/<repo>/releases/download/data-store/web-data.jsonl.gz
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import shutil
import sqlite3
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

FORMAT_VERSION = 1
BUNDLE_ASSET = "web-data.jsonl.gz"
# A bundle URL may carry "{run_id}"; the asset is then named per run so
# every committed manifest keeps naming a bundle that still exists, and
# a build of an older commit (or a branch behind main) still verifies.
VERSIONED_ASSET = "web-data-{run_id}.jsonl.gz"
BUCKET_KEY_RULE = "registration_id[-3:] (non-alphanumerics → _)"
FILINGS_WINDOW_YEARS = 5  # per-company filing timeline carried in the record
RUN_HISTORY = 40


def bucket_key(registration_id: str) -> str:
    tail = str(registration_id or "")[-3:] or "_"
    return re.sub(r"[^A-Za-z0-9]", "_", tail)


def _maybe_json(value):
    if value is None or value == "":
        return None
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except (TypeError, ValueError):
        return value


def _bool(value):
    return None if value is None else bool(value)


def _rows(db: sqlite3.Connection, sql: str, args: tuple = ()) -> list[dict]:
    db.row_factory = sqlite3.Row
    return [dict(r) for r in db.execute(sql, args)]


def _group(rows: list[dict], key: str = "company_id") -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        out[r[key]].append(r)
    return out


def _table_exists(db: sqlite3.Connection, name: str) -> bool:
    return bool(
        db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone()
    )


def export(db_path: Path, out: Path, bundle_url: str | None) -> dict:
    db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    # ---- whole-table loads, grouped once (no per-company queries: the
    # store has no company_id index on figures/filings and never will
    # need one for the CLI's own access patterns) ----
    runs = _rows(db, "SELECT run_id, command, git_sha, started_at, finished_at, exit_status, counts "
                     "FROM runs ORDER BY started_at")
    for r in runs:
        r["counts"] = _maybe_json(r["counts"]) or {}
    latest_run = runs[-1] if runs else {}

    companies = _rows(db, "SELECT id, jurisdiction, registration_id, name, name_variants, "
                          "incorporation_date, status, classification_codes, classification_taxonomy, "
                          "registered_address, ownership_classification, ownership_confidence, "
                          "ownership_evidence FROM companies ORDER BY id")

    figures = _rows(db, "SELECT id, company_id, concept, value, unit, currency, period_type, "
                        "period_start, period_end, dimensions, decimals, raw_text, basis, "
                        "source_document_id, source_tag, derivation_function, derivation_inputs, "
                        "is_current FROM figures")
    for f in figures:
        f["dimensions"] = _maybe_json(f["dimensions"]) or {}
        f["derivation_inputs"] = _maybe_json(f["derivation_inputs"])
        f["is_current"] = bool(f["is_current"])
    figs_by_company = _group(figures)

    documents = _rows(db, "SELECT id, company_id, external_document_id, transaction_id, document_type, "
                          "account_type, filed_date, period_start, period_end, retrieved_at, content_type, "
                          "content_hash, parse_status, parse_error_count, production_software "
                          "FROM source_documents")
    docs_by_id = {d["id"]: d for d in documents}
    docs_by_company = _group(documents)

    coverage_all = _rows(db, "SELECT company_id, concept, period_end, status, source_document_id, "
                             "detail, run_id FROM concept_coverage")
    latest_cov_run: dict[str, str] = {}
    first_seen: dict[str, str] = {}
    for f in coverage_all:
        cid = f["company_id"]
        if f["run_id"] > latest_cov_run.get(cid, ""):
            latest_cov_run[cid] = f["run_id"]
        if f["run_id"] < first_seen.get(cid, "~"):
            first_seen[cid] = f["run_id"]
    cov_by_company: dict[str, list[dict]] = defaultdict(list)
    for f in coverage_all:
        if f["run_id"] == latest_cov_run[f["company_id"]]:
            cov_by_company[f["company_id"]].append(f)

    officers = _group(_rows(db, "SELECT company_id, name, role, appointed_on, resigned_on, dob_month, "
                                "dob_year, nationality, country_of_residence FROM officers "
                                "ORDER BY appointed_on"))
    owners = _group(_rows(db, "SELECT company_id, name, kind, name_elements, control_natures, "
                              "notified_on, ceased_on, dob_month, dob_year, identification "
                              "FROM beneficial_owners ORDER BY notified_on"))
    statements = _group(_rows(db, "SELECT company_id, statement, notified_on, ceased_on "
                                  "FROM ownership_statements ORDER BY notified_on"))
    exemptions = _group(_rows(db, "SELECT company_id, exemption_type, items FROM exemptions")) \
        if _table_exists(db, "exemptions") else {}
    charges = _group(_rows(db, "SELECT company_id, external_id, status, created_on, delivered_on, "
                               "satisfied_on, classification, details, secured_parties, transactions "
                               "FROM security_interests ORDER BY created_on DESC"))
    events = _group(_rows(db, "SELECT company_id, event_type, event_date, transaction_id, "
                              "source_document_id, payload FROM events ORDER BY event_date DESC")) \
        if _table_exists(db, "events") else {}

    filing_counts = {r["company_id"]: r["n"] for r in
                     _rows(db, "SELECT company_id, COUNT(*) n FROM filings GROUP BY company_id")}
    cutoff = f"{datetime.now(timezone.utc).year - FILINGS_WINDOW_YEARS}-01-01"
    filings = _group(_rows(db, "SELECT company_id, transaction_id, category, subcategory, type, "
                               "filing_date, description, description_values, document_id, paper_filed "
                               "FROM filings WHERE filing_date >= ? OR category = 'accounts' "
                               "ORDER BY filing_date DESC", (cutoff,)))

    # ---- per-company assembly ----
    def latest_current(figs: list[dict], concept: str) -> dict | None:
        best = None
        for f in figs:
            if f["concept"] != concept or not f["is_current"] or f["dimensions"]:
                continue
            if best is None or (f["period_end"] or "") > (best["period_end"] or ""):
                best = f
        return best

    def fig_ref(f: dict | None) -> dict | None:
        # Index-sized reference: the value plus what a reader needs to
        # judge it (period, filed date) and the id to trace it. Unit,
        # currency and basis travel with the full figure in the bucket.
        if not f:
            return None
        d = docs_by_id.get(f["source_document_id"] or "")
        return {
            "figure_id": f["id"],
            "value": f["value"],
            "period_end": f["period_end"],
            "filed_date": d["filed_date"] if d else None,
        }

    index_rows: list[dict] = []
    buckets: dict[str, dict[str, dict]] = defaultdict(dict)
    mode_totals: dict[str, int] = defaultdict(int)
    coverage_by_status: dict[str, int] = defaultdict(int)
    by_code: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    products: set[str] = set()

    for c in companies:
        cid = c["id"]
        figs = figs_by_company.get(cid, [])
        docs = sorted(docs_by_company.get(cid, []), key=lambda d: (d["filed_date"] or "", d["id"]),
                      reverse=True)
        facts = sorted(cov_by_company.get(cid, []), key=lambda x: x["concept"])
        statuses: dict[str, int] = defaultdict(int)
        for f in facts:
            statuses[f["status"]] += 1
            coverage_by_status[f["status"]] += 1
        if statuses.get("available"):
            mode = "financial"
        elif statuses.get("parse_failed"):
            mode = "parse_failed"
        else:
            mode = "signal"
        mode_totals[mode] += 1

        sic = _maybe_json(c["classification_codes"]) or []
        for code in sic:
            by_code[str(code)]["companies"] += 1
            by_code[str(code)][mode] += 1
        address = _maybe_json(c["registered_address"]) or {}

        current_ends = [f["period_end"] for f in figs if f["is_current"] and f["period_end"]]
        freshest = max(current_ends) if current_ends else None
        fresh_docs = [docs_by_id.get(f["source_document_id"]) for f in figs
                      if f["is_current"] and f["period_end"] == freshest and f["source_document_id"]]
        fresh_docs = [d for d in fresh_docs if d]
        freshest_filed = max((d["filed_date"] for d in fresh_docs if d["filed_date"]), default=None)

        bos = owners.get(cid, [])
        for b in bos:
            b["control_natures"] = _maybe_json(b["control_natures"]) or []
            b["name_elements"] = _maybe_json(b["name_elements"]) or {}
            b["identification"] = _maybe_json(b["identification"]) or {}
        active_bos = [b for b in bos if not b["ceased_on"]]
        dobs = [(b["dob_year"], b["dob_month"]) for b in active_bos
                if b["dob_year"] and str(b["kind"] or "").startswith("individual")]
        owner_dob = min(dobs) if dobs else None  # earliest birth = oldest owner
        single_75 = len(active_bos) == 1 and any(
            "75-to-100" in str(n) for n in active_bos[0]["control_natures"])

        offs = officers.get(cid, [])
        active_offs = [o for o in offs if not o["resigned_on"]]
        last_appointed = max((o["appointed_on"] for o in active_offs if o["appointed_on"]), default=None)
        last_resigned = max((o["resigned_on"] for o in offs if o["resigned_on"]), default=None)

        chs = charges.get(cid, [])
        for ch in chs:
            ch["classification"] = _maybe_json(ch["classification"]) or {}
            ch["details"] = _maybe_json(ch["details"]) or {}
            ch["secured_parties"] = _maybe_json(ch["secured_parties"]) or []
            ch["transactions"] = _maybe_json(ch["transactions"]) or []
        outstanding = sum(1 for ch in chs if ch["status"] in ("outstanding", "part-satisfied"))

        evs = events.get(cid, [])
        for e in evs:
            e["payload"] = _maybe_json(e["payload"]) or {}

        fils = filings.get(cid, [])
        for fl in fils:
            dv = _maybe_json(fl["description_values"]) or {}
            fl["description_values"] = dv
            fl["paper_filed"] = _bool(fl["paper_filed"])

        parsed_docs = [d for d in docs if d["parse_status"] == "parsed"]
        software = next((d["production_software"] for d in parsed_docs if d["production_software"]), None)
        for d in docs:
            if d["production_software"]:
                products.add(d["production_software"])

        rev = latest_current(figs, "revenue")
        na = latest_current(figs, "net_assets") or latest_current(figs, "equity")
        emp = latest_current(figs, "average_employees")

        index_rows.append({
            "id": cid,
            "registration_id": c["registration_id"],
            "name": c["name"],
            "status": c["status"],
            "incorporated": c["incorporation_date"],
            "sic": sic,
            "locality": address.get("locality"),
            "region": address.get("region"),
            "country": address.get("country"),
            "postal_code": address.get("postal_code"),
            "mode": mode,
            "ownership_classification": c["ownership_classification"],
            "coverage": {"statuses": dict(statuses), "of": len(facts),
                         "period_end": max((f["period_end"] for f in facts if f["period_end"]), default=None)},
            "freshest_period": freshest,
            "freshest_filed": freshest_filed,
            "latest": {"revenue": fig_ref(rev), "net_assets": fig_ref(na), "employees": fig_ref(emp)},
            "owner_dob": {"year": owner_dob[0], "month": owner_dob[1]} if owner_dob else None,
            "active_owners": len(active_bos),
            "single_owner_75": single_75,
            "ownership_statements": len(statements.get(cid, [])),
            "officers_active": len(active_offs),
            "officers_total": len(offs),
            "last_officer_appointed": last_appointed,
            "last_officer_resigned": last_resigned,
            "last_psc_notified": max((b["notified_on"] for b in bos if b["notified_on"]), default=None),
            "last_psc_ceased": max((b["ceased_on"] for b in bos if b["ceased_on"]), default=None),
            "charges_outstanding": outstanding,
            "charges_total": len(chs),
            "last_charge_created": max((ch["created_on"] for ch in chs if ch["created_on"]), default=None),
            "restatements": len(evs),
            "filings": filing_counts.get(cid, 0),
            "documents": len(docs),
            "software": software,
            "first_seen": first_seen.get(cid),
        })

        buckets[bucket_key(c["registration_id"])][cid] = {
            "company": {
                "id": cid,
                "registration_id": c["registration_id"],
                "name": c["name"],
                "name_variants": _maybe_json(c["name_variants"]) or [],
                "jurisdiction": c["jurisdiction"],
                "status": c["status"],
                "incorporated": c["incorporation_date"],
                "sic": sic,
                "classification_taxonomy": c["classification_taxonomy"],
                "address": address,
                "ownership_classification": c["ownership_classification"],
                "ownership_confidence": c["ownership_confidence"],
                "ownership_evidence": _maybe_json(c["ownership_evidence"]) or [],
                "mode": mode,
                "first_seen": first_seen.get(cid),
                "filings_on_register": filing_counts.get(cid, 0),
            },
            "figures": [{k: v for k, v in f.items() if k != "company_id"} for f in figs],
            "documents": [{k: v for k, v in d.items() if k != "company_id"} for d in docs],
            "coverage": [{"concept": f["concept"], "status": f["status"], "detail": f["detail"],
                          "period_end": f["period_end"], "source_document_id": f["source_document_id"]}
                         for f in facts],
            "officers": [{k: v for k, v in o.items() if k != "company_id"} for o in offs],
            "beneficial_owners": [{k: v for k, v in b.items() if k != "company_id"} for b in bos],
            "ownership_statements": [{k: v for k, v in s.items() if k != "company_id"}
                                     for s in statements.get(cid, [])],
            "exemptions": [{"exemption_type": e["exemption_type"], "items": _maybe_json(e["items"]) or []}
                           for e in exemptions.get(cid, [])],
            "charges": [{k: v for k, v in ch.items() if k != "company_id"} for ch in chs],
            "filings": [{k: v for k, v in fl.items() if k != "company_id"} for fl in fils],
            "events": [{k: v for k, v in e.items() if k != "company_id"} for e in evs],
        }

    # ---- store operations ----
    figures_per_doc: dict[str, int] = defaultdict(int)
    for f in figures:
        if f["source_document_id"]:
            figures_per_doc[f["source_document_id"]] += 1
    by_software: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for d in documents:
        name = d["production_software"] or "undeclared"
        s = by_software[name]
        s["documents"] += 1
        s[d["parse_status"]] += 1
        if d["parse_status"] == "parsed":
            if figures_per_doc.get(d["id"]):
                s["with_figures"] += 1
            else:
                s["zero_figure"] += 1
    for s in by_software.values():
        parsed = s.get("parsed", 0)
        s["figure_yield"] = round(s.get("with_figures", 0) / parsed, 3) if parsed else None

    company_by_id = {c["id"]: c for c in companies}
    # The defect list is what the coverage layer calls parse_failed — a
    # quarantined document OR a machine-readable document that parsed
    # to zero figures (each latest-run fact names its document and
    # carries the recorded cause) — plus any document still "pending"
    # after a run: fetched and never parsed, also a defect.
    failed_docs: dict[str, str | None] = {}
    for facts in cov_by_company.values():
        for f in facts:
            if f["status"] == "parse_failed" and f["source_document_id"]:
                failed_docs.setdefault(f["source_document_id"], f["detail"])
    for d in documents:
        if d["parse_status"] in ("quarantined", "pending"):
            failed_docs.setdefault(d["id"], f"parse_status {d['parse_status']}")
    parse_failures = []
    for d in documents:
        if d["id"] not in failed_docs:
            continue
        c = company_by_id.get(d["company_id"], {})
        detail = failed_docs[d["id"]]
        parse_failures.append({
            "company_id": d["company_id"],
            "registration_id": c.get("registration_id"),
            "name": c.get("name"),
            "document_id": d["id"],
            "transaction_id": d["transaction_id"],
            "filed_date": d["filed_date"],
            "period_end": d["period_end"],
            "account_type": d["account_type"],
            "content_type": d["content_type"],
            "production_software": d["production_software"],
            "parse_status": d["parse_status"],
            "parse_error_count": d["parse_error_count"],
            "detail": detail,
        })
    parse_failures.sort(key=lambda r: (r["production_software"] or "~", r["filed_date"] or ""), reverse=False)

    ops = {
        "generated_at": generated_at,
        "run_id": latest_run.get("run_id"),
        "parse_failures": parse_failures,
        "by_production_software": {k: dict(v) for k, v in
                                   sorted(by_software.items(), key=lambda kv: -kv[1]["documents"])},
        "by_classification_code": {k: dict(v) for k, v in sorted(by_code.items())},
        "runs": runs,
    }

    run_id = latest_run.get("run_id") or "no-run"
    versioned = bool(bundle_url and "{run_id}" in bundle_url)
    asset = VERSIONED_ASSET.format(run_id=run_id) if versioned else BUNDLE_ASSET
    manifest = {
        "format": FORMAT_VERSION,
        "generated_at": generated_at,
        "run": {
            "run_id": latest_run.get("run_id"),
            "git_sha": latest_run.get("git_sha"),
            "started_at": latest_run.get("started_at"),
            "finished_at": latest_run.get("finished_at"),
        },
        "bundle": {
            "asset": asset,
            "url": bundle_url.replace("{run_id}", run_id) if bundle_url else None,
            "sha256": None,
            "bytes": None,
        },
        "buckets": {"count": len(buckets), "key": BUCKET_KEY_RULE},
        "totals": {
            "companies": len(companies),
            "figures": len(figures),
            "documents": len(documents),
            "filings": sum(filing_counts.values()),
            "officers": sum(len(v) for v in officers.values()),
            "beneficial_owners": sum(len(v) for v in owners.values()),
            "security_interests": sum(len(v) for v in charges.values()),
            "restatement_events": sum(len(v) for v in events.values()),
        },
        "modes": dict(mode_totals),
        "products": len(products),
        "coverage_by_status": dict(coverage_by_status),
        "parse_failures": {
            "documents": len(parse_failures),
            "companies": len({r["company_id"] for r in parse_failures}),
        },
        "runs": [
            {"run_id": r["run_id"], "command": r["command"], "started_at": r["started_at"],
             "finished_at": r["finished_at"], "exit_status": r["exit_status"],
             "ingested": (r["counts"] or {}).get("ingested"),
             "errors": (r["counts"] or {}).get("errors"),
             "figures_new": (r["counts"] or {}).get("figures_new")}
            for r in runs[-RUN_HISTORY:]
        ],
    }

    index = {"run_id": manifest["run"]["run_id"], "generated_at": generated_at, "companies": index_rows}

    # ---- write ----
    out.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(out / "c", ignore_errors=True)
    (out / "c").mkdir()
    compact = dict(separators=(",", ":"), ensure_ascii=False)
    (out / "index.json").write_text(json.dumps(index, **compact), encoding="utf-8")
    (out / "ops.json").write_text(json.dumps(ops, **compact), encoding="utf-8")
    for key, obj in buckets.items():
        (out / "c" / f"{key}.json").write_text(json.dumps(obj, **compact), encoding="utf-8")

    bundle_path = out / asset
    with gzip.open(bundle_path, "wt", encoding="utf-8", compresslevel=6) as fh:
        fh.write("manifest\t-\t" + json.dumps(manifest, **compact) + "\n")
        fh.write("index\t-\t" + json.dumps(index, **compact) + "\n")
        fh.write("ops\t-\t" + json.dumps(ops, **compact) + "\n")
        for key in sorted(buckets):
            fh.write(f"bucket\t{key}\t" + json.dumps(buckets[key], **compact) + "\n")
    digest = hashlib.sha256()
    with bundle_path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    manifest["bundle"]["sha256"] = digest.hexdigest()
    manifest["bundle"]["bytes"] = bundle_path.stat().st_size
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("db", type=Path, help="engine.db or engine.db.gz")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--bundle-url", default=None,
                    help="public URL the site build downloads the bundle from (recorded in the manifest); "
                         "may contain {run_id}, in which case the bundle file is named per run")
    args = ap.parse_args()

    db_path = args.db
    if db_path.suffix == ".gz":
        tmp = Path(tempfile.mkstemp(suffix=".db")[1])
        with gzip.open(db_path, "rb") as src, tmp.open("wb") as dst:
            shutil.copyfileobj(src, dst)
        db_path = tmp

    manifest = export(db_path, args.out, args.bundle_url)
    t = manifest["totals"]
    print(
        f"exported {t['companies']} companies, {t['figures']} figures, {t['documents']} documents "
        f"into {manifest['buckets']['count']} buckets -> {args.out} "
        f"(bundle {manifest['bundle']['asset']}, {manifest['bundle']['bytes']:,} bytes, "
        f"sha256 {manifest['bundle']['sha256'][:12]}…)"
    )


if __name__ == "__main__":
    main()
