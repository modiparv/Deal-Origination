"""Resumable per-item progress for unattended runs.

Adapter pipelines mark each processed identifier with an outcome; a
re-run with the same checkpoint file skips them. JSON, written
atomically after every mark so an interrupted run never loses progress
or leaves a torn file.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path


class Checkpoint:
    def __init__(self, path: Path, processed: dict[str, str] | None = None):
        self.path = path
        self.processed: dict[str, str] = processed or {}

    @classmethod
    def load(cls, path: Path) -> "Checkpoint":
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            return cls(path, dict(data.get("processed", {})))
        return cls(path)

    def mark(self, item_id: str, outcome: str) -> None:
        self.processed[item_id] = outcome
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, prefix=".ckpt-")
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump({"processed": self.processed}, handle, indent=1)
        os.replace(tmp, self.path)
