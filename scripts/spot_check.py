#!/usr/bin/env python3
"""Deterministic spot-check extract for the Phase 1 gate review.

Samples ingested companies (evenly across the id-ordered universe, so
the sample is reproducible and not clustered in one classification
code) and writes a markdown dossier per company: profile fields, every
persisted figure with its provenance (source document, period end and
filed date — no figure appears without both), concept-coverage causes
from the latest run, and record counts.

Stdlib only (sqlite3), so it runs anywhere the database file exists —
no engine install required. Read-only.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def sample_company_ids(conn: sqlite3.Connection, sample: int) -> list[str]:
    ids = [r["id"] for r in conn.execute("SELECT id FROM companies ORDER BY id")]
    if not ids or sample <= 0:
        return []
    step = max(1, len(ids) // sample)
    return ids[::step][:sample]


def latest_run_id(conn: sqlite3.Connection) -> str | None:
    row = conn.execute(
        "SELECT run_id FROM runs ORDER BY started_at DESC, run_id DESC LIMIT 1"
    ).fetchone()
    return row["run_id"] if row else None


def company_section(conn: sqlite3.Connection, cid: str, run_id: str | None) -> str:
    company = conn.execute("SELECT * FROM companies WHERE id = ?", (cid,)).fetchone()
    lines = [
        f"## {company['name']} (`{company['id']}`)",
        "",
        f"- registration: `{company['registration_id']}` ({company['jurisdiction']}),"
        f" status {company['status']}, incorporated {company['incorporation_date']}",
        f"- classification: {json.loads(company['classification_codes'])}"
        f" ({company['classification_taxonomy']})",
    ]

    counts = {}
    for label, table in [
        ("officers", "officers"),
        ("beneficial owners", "beneficial_owners"),
        ("ownership statements", "ownership_statements"),
        ("security interests", "security_interests"),
        ("filings", "filings"),
        ("events", "events"),
        ("source documents", "source_documents"),
    ]:
        counts[label] = conn.execute(
            f"SELECT COUNT(*) c FROM {table} WHERE company_id = ?", (cid,)
        ).fetchone()["c"]
    lines.append("- records: " + ", ".join(f"{v} {k}" for k, v in counts.items()))
    lines.append("")

    figures = conn.execute(
        """
        SELECT f.concept, f.value, f.unit, f.currency, f.period_end, f.is_current,
               f.basis, f.source_tag, f.dimensions,
               d.id AS doc_id, d.filed_date, d.account_type
        FROM figures f LEFT JOIN source_documents d ON d.id = f.source_document_id
        WHERE f.company_id = ?
        ORDER BY f.period_end DESC, f.concept, f.id
        """,
        (cid,),
    ).fetchall()
    if figures:
        lines += [
            "| concept | value | unit | period end | filed | basis | current | source tag | regime |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for f in figures:
            dims = json.loads(f["dimensions"] or "{}")
            concept = f["concept"] + (f" `{dims}`" if dims else "")
            lines.append(
                f"| {concept} | {f['value']} | {f['currency'] or f['unit']} "
                f"| {f['period_end']} | {f['filed_date']} | {f['basis']} "
                f"| {'yes' if f['is_current'] else 'no'} | `{f['source_tag']}` "
                f"| {f['account_type']} |"
            )
    else:
        lines.append("_No figures persisted for this company._")
    lines.append("")

    if run_id:
        coverage = conn.execute(
            """
            SELECT concept, period_end, status, detail
            FROM concept_coverage WHERE company_id = ? AND run_id = ?
            ORDER BY status, concept
            """,
            (cid, run_id),
        ).fetchall()
        if coverage:
            available = [c["concept"] for c in coverage if c["status"] == "available"]
            lines.append(
                f"Coverage @ {coverage[0]['period_end']}: "
                f"{len(available)}/{len(coverage)} concepts available"
                + (f" ({', '.join(available)})" if available else "")
            )
            absences = [c for c in coverage if c["status"] != "available"]
            for c in absences:
                detail = f" — {c['detail']}" if c["detail"] else ""
                lines.append(f"- `{c['concept']}`: {c['status']}{detail}")
        else:
            lines.append("_No coverage facts for the latest run._")
    lines.append("")

    events = conn.execute(
        "SELECT event_type, event_date, payload FROM events WHERE company_id = ? "
        "ORDER BY event_date, id",
        (cid,),
    ).fetchall()
    for e in events:
        lines.append(f"- event {e['event_type']} @ {e['event_date']}: `{e['payload'][:200]}`")
    if events:
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, required=True)
    parser.add_argument("--sample", type=int, default=10)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    conn = connect(args.db)
    run_id = latest_run_id(conn)
    cids = sample_company_ids(conn, args.sample)

    total = conn.execute("SELECT COUNT(*) c FROM companies").fetchone()["c"]
    header = [
        "# Ingest spot-check",
        "",
        f"- database: `{args.db}`",
        f"- latest run: `{run_id}`",
        f"- companies in store: {total}; sampled: {len(cids)} (deterministic stride)",
        "",
        "Every figure below is a filed observation citing its source document's "
        "period end and filed date; `current = no` marks superseded observations "
        "retained for the restatement record.",
        "",
    ]
    sections = [company_section(conn, cid, run_id) for cid in cids]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(header + sections), encoding="utf-8")
    print(f"wrote {args.out} ({len(cids)} companies)")


if __name__ == "__main__":
    main()
