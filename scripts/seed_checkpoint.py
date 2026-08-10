#!/usr/bin/env python3
"""Synthesize an ingest checkpoint from an existing engine database.

Used once when the rolling data-store release does not yet exist: the
store seeded from a committed run knows which companies it already
holds, so the first accumulating run must not spend API budget
re-ingesting them. Every company in the database is marked
"ingested" in the checkpoint file the pipeline's --resume path reads.
"""

from __future__ import annotations

import argparse
import gzip
import json
import shutil
import sqlite3
import tempfile
from pathlib import Path


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

    db = sqlite3.connect(db_path)
    processed = {
        str(reg): "ingested"
        for (reg,) in db.execute("SELECT registration_id FROM companies")
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({"processed": processed}, indent=1), encoding="utf-8")
    print(f"checkpoint seeded with {len(processed)} companies -> {args.out}")


if __name__ == "__main__":
    main()
