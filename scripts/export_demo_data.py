#!/usr/bin/env python3
"""Export the demo-surface dataset from a run's engine database.

Reads the committed engine.db of a verified ingest run and emits one
JSON document consumed by the demo frontend (web/src/demo/). Everything
in the output is a verbatim copy or a mechanical aggregate (counts,
max-period selection) of rows already in the audit trail; nothing
financial is computed here — margins, growth and scores are Phase 2
derived figures and are absent by design, so the frontend renders their
absence states instead.

Usage:
    python scripts/export_demo_data.py <engine.db|engine.db.gz> \
        --out web/demo-data/demo-data.json
"""

from __future__ import annotations

import argparse
import gzip
import json
import shutil
import sqlite3
import tempfile
from pathlib import Path


def _rows(db: sqlite3.Connection, sql: str, args: tuple = ()) -> list[dict]:
    db.row_factory = sqlite3.Row
    return [dict(r) for r in db.execute(sql, args)]


def _maybe_json(value):
    if value is None or value == "":
        return None
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except (TypeError, ValueError):
        return value


def export(db_path: Path) -> dict:
    db = sqlite3.connect(db_path)

    runs = _rows(db, "SELECT * FROM runs ORDER BY started_at DESC LIMIT 1")
    run_meta = runs[0] if runs else {}

    companies = _rows(db, "SELECT * FROM companies ORDER BY name")
    figures = _rows(db, "SELECT * FROM figures")
    documents = _rows(db, "SELECT * FROM source_documents")
    coverage = _rows(db, "SELECT * FROM concept_coverage")

    by_company_cov: dict[str, list[dict]] = {}
    for f in coverage:
        by_company_cov.setdefault(f["company_id"], []).append(f)

    by_company_figs: dict[str, list[str]] = {}
    for f in figures:
        f["dimensions"] = _maybe_json(f["dimensions"]) or {}
        f["derivation_inputs"] = _maybe_json(f["derivation_inputs"])
        by_company_figs.setdefault(f["company_id"], []).append(f["id"])

    fig_by_id = {f["id"]: f for f in figures}

    def latest_current(cid: str, concept: str):
        best = None
        for fid in by_company_figs.get(cid, []):
            f = fig_by_id[fid]
            if f["concept"] != concept or not f["is_current"] or f["dimensions"]:
                continue
            if best is None or (f["period_end"] or "") > (best["period_end"] or ""):
                best = f
        return best["id"] if best else None

    def freshest_period(cid: str):
        ends = [
            fig_by_id[fid]["period_end"]
            for fid in by_company_figs.get(cid, [])
            if fig_by_id[fid]["is_current"] and fig_by_id[fid]["period_end"]
        ]
        return max(ends) if ends else None

    def scalar(sql: str, args: tuple) -> int:
        return db.execute(sql, args).fetchone()[0]

    out_companies = []
    for c in companies:
        cid = c["id"]
        facts = by_company_cov.get(cid, [])
        statuses: dict[str, int] = {}
        for f in facts:
            statuses[f["status"]] = statuses.get(f["status"], 0) + 1
        if statuses.get("available"):
            mode = "financial"
        elif statuses.get("parse_failed"):
            mode = "parse_failed"
        else:
            mode = "signal"

        charge_statuses: dict[str, int] = {}
        for r in _rows(
            db, "SELECT status, COUNT(*) n FROM security_interests WHERE company_id=? GROUP BY status", (cid,)
        ):
            charge_statuses[r["status"] or "unknown"] = r["n"]

        out_companies.append(
            {
                "id": cid,
                "registration_id": c["registration_id"],
                "name": c["name"],
                "jurisdiction": c["jurisdiction"],
                "status": c["status"],
                "incorporated": c["incorporation_date"],
                "sic": _maybe_json(c["classification_codes"]) or [],
                "address": _maybe_json(c["registered_address"]) or {},
                "ownership_classification": c["ownership_classification"],
                "mode": mode,
                "coverage": {
                    "statuses": statuses,
                    "of": len(facts),
                    "period_end": max((f["period_end"] for f in facts if f["period_end"]), default=None),
                },
                "freshest_period": freshest_period(cid),
                "latest_revenue_fig": latest_current(cid, "revenue"),
                "latest_net_assets_fig": latest_current(cid, "net_assets") or latest_current(cid, "equity"),
                "latest_employees_fig": latest_current(cid, "average_employees"),
                "counts": {
                    "officers_active": scalar(
                        "SELECT COUNT(*) FROM officers WHERE company_id=? AND resigned_on IS NULL", (cid,)
                    ),
                    "officers_total": scalar("SELECT COUNT(*) FROM officers WHERE company_id=?", (cid,)),
                    "beneficial_owners": scalar(
                        "SELECT COUNT(*) FROM beneficial_owners WHERE company_id=?", (cid,)
                    ),
                    "ownership_statements": scalar(
                        "SELECT COUNT(*) FROM ownership_statements WHERE company_id=?", (cid,)
                    ),
                    "exemptions": scalar("SELECT COUNT(*) FROM exemptions WHERE company_id=?", (cid,)),
                    "filings": scalar("SELECT COUNT(*) FROM filings WHERE company_id=?", (cid,)),
                    "documents": scalar(
                        "SELECT COUNT(*) FROM source_documents WHERE company_id=?", (cid,)
                    ),
                },
                "charges": charge_statuses,
                "beneficial_owners": [
                    {
                        "name": r["name"],
                        "kind": r["kind"],
                        "natures": _maybe_json(r["control_natures"]) or [],
                        "notified_on": r["notified_on"],
                        "ceased_on": r["ceased_on"],
                        "dob_year": r["dob_year"],
                        "dob_month": r["dob_month"],
                    }
                    for r in _rows(
                        db,
                        "SELECT * FROM beneficial_owners WHERE company_id=? ORDER BY notified_on",
                        (cid,),
                    )
                ],
                "ownership_statements": [
                    {
                        "statement": r["statement"],
                        "notified_on": r["notified_on"],
                        "ceased_on": r["ceased_on"],
                    }
                    for r in _rows(
                        db,
                        "SELECT * FROM ownership_statements WHERE company_id=? ORDER BY notified_on",
                        (cid,),
                    )
                ],
                "officers": [
                    {
                        "name": r["name"],
                        "role": r["role"],
                        "appointed_on": r["appointed_on"],
                        "resigned_on": r["resigned_on"],
                        "dob_year": r["dob_year"],
                    }
                    for r in _rows(
                        db,
                        "SELECT * FROM officers WHERE company_id=? ORDER BY appointed_on",
                        (cid,),
                    )
                ],
                "recent_charges": [
                    {
                        "status": r["status"],
                        "created_on": r["created_on"],
                        "satisfied_on": r["satisfied_on"],
                        "classification": _maybe_json(r["classification"]),
                        "secured_parties": _maybe_json(r["secured_parties"]) or [],
                    }
                    for r in _rows(
                        db,
                        "SELECT * FROM security_interests WHERE company_id=? "
                        "ORDER BY created_on DESC",
                        (cid,),
                    )
                ],
            }
        )

    out_figures = {
        f["id"]: {
            "id": f["id"],
            "company_id": f["company_id"],
            "concept": f["concept"],
            "value": f["value"],
            "unit": f["unit"],
            "currency": f["currency"],
            "period_start": f["period_start"],
            "period_end": f["period_end"],
            "dimensions": f["dimensions"],
            "decimals": f["decimals"],
            "raw_text": f["raw_text"],
            "basis": f["basis"],
            "source_document_id": f["source_document_id"],
            "source_tag": f["source_tag"],
            "derivation_function": f["derivation_function"],
            "derivation_inputs": f["derivation_inputs"],
            "is_current": bool(f["is_current"]),
        }
        for f in figures
    }

    out_documents = {
        d["id"]: {
            "id": d["id"],
            "company_id": d["company_id"],
            "external_document_id": d["external_document_id"],
            "transaction_id": d["transaction_id"],
            "document_type": d["document_type"],
            "account_type": d["account_type"],
            "filed_date": d["filed_date"],
            "period_end": d["period_end"],
            "content_type": d["content_type"],
            "content_hash": d["content_hash"],
            "parse_status": d["parse_status"],
            "production_software": d["production_software"],
            "retrieved_at": d["retrieved_at"],
        }
        for d in documents
    }

    out_coverage = {
        cid: [
            {
                "concept": f["concept"],
                "status": f["status"],
                "detail": f["detail"],
                "period_end": f["period_end"],
                "source_document_id": f["source_document_id"],
            }
            for f in sorted(facts, key=lambda x: x["concept"])
        ]
        for cid, facts in by_company_cov.items()
    }

    return {
        "run": {
            "run_id": run_meta.get("run_id"),
            "git_sha": run_meta.get("git_sha"),
            "started_at": run_meta.get("started_at"),
            "finished_at": run_meta.get("finished_at"),
        },
        "companies": out_companies,
        "figures": out_figures,
        "figures_by_company": by_company_figs,
        "documents": out_documents,
        "coverage": out_coverage,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("db", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    db_path = args.db
    if db_path.suffix == ".gz":
        tmp = Path(tempfile.mkstemp(suffix=".db")[1])
        with gzip.open(db_path, "rb") as src, tmp.open("wb") as dst:
            shutil.copyfileobj(src, dst)
        db_path = tmp

    data = export(db_path)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(
        f"exported {len(data['companies'])} companies, {len(data['figures'])} figures, "
        f"{len(data['documents'])} documents -> {args.out}"
    )


if __name__ == "__main__":
    main()
