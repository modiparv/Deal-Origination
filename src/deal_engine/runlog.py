"""Run logging: an unattended run you didn't capture didn't happen (§3.4).

One JSONL file per run under logs/runs/: a start line, optional progress
lines, and an end line with duration, counts and exit status. LLM cost
fields join in Phase 3 from the `claude -p` JSON envelope.
"""

from __future__ import annotations

import json
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path
from types import TracebackType

DEFAULT_LOG_DIR = Path("logs/runs")


def _git_sha() -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return out.stdout.strip() or None
    except OSError:
        return None


class RunLogger:
    def __init__(
        self,
        command: str,
        args: dict | None = None,
        log_dir: Path | str = DEFAULT_LOG_DIR,
    ):
        self.command = command
        self.args = args or {}
        started = datetime.now(timezone.utc)
        self.started_at = started
        self.run_id = f"{started:%Y%m%dT%H%M%SZ}-{uuid.uuid4().hex[:8]}"
        self.log_dir = Path(log_dir)
        self.path = self.log_dir / f"{self.run_id}.jsonl"
        self._finished = False

    def _write(self, record: dict) -> None:
        self.log_dir.mkdir(parents=True, exist_ok=True)
        record = {"run_id": self.run_id, "ts": datetime.now(timezone.utc).isoformat(), **record}
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, default=str) + "\n")

    def start(self) -> "RunLogger":
        self._write(
            {
                "event": "start",
                "command": self.command,
                "args": self.args,
                "git_sha": _git_sha(),
            }
        )
        return self

    def log(self, event: str, **fields: object) -> None:
        self._write({"event": event, **fields})

    def finish(
        self,
        exit_status: int,
        counts: dict[str, int] | None = None,
        cost_usd: float | None = None,
    ) -> None:
        if self._finished:
            return
        self._finished = True
        duration = (datetime.now(timezone.utc) - self.started_at).total_seconds()
        self._write(
            {
                "event": "end",
                "exit_status": exit_status,
                "duration_seconds": round(duration, 3),
                "counts": counts or {},
                **({"cost_usd": cost_usd} if cost_usd is not None else {}),
            }
        )

    def __enter__(self) -> "RunLogger":
        return self.start()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        if exc_type is None:
            self.finish(exit_status=0)
        else:
            self.log("error", error=repr(exc))
            self.finish(exit_status=1)
