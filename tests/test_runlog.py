import json

import pytest

from deal_engine.runlog import RunLogger


def read_lines(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def test_start_and_finish(tmp_path):
    logger = RunLogger("mandate validate", {"path": "x.yaml"}, log_dir=tmp_path).start()
    logger.log("progress", companies=3)
    logger.finish(exit_status=0, counts={"errors": 0})

    lines = read_lines(logger.path)
    assert [rec["event"] for rec in lines] == ["start", "progress", "end"]
    start, progress, end = lines
    assert start["command"] == "mandate validate"
    assert start["args"] == {"path": "x.yaml"}
    assert progress["companies"] == 3
    assert end["exit_status"] == 0
    assert end["duration_seconds"] >= 0
    assert all(rec["run_id"] == logger.run_id for rec in lines)


def test_context_manager_records_failure(tmp_path):
    with pytest.raises(RuntimeError):
        with RunLogger("ingest", log_dir=tmp_path) as logger:
            raise RuntimeError("boom")
    lines = read_lines(logger.path)
    assert lines[-1]["event"] == "end"
    assert lines[-1]["exit_status"] == 1
    assert any(rec["event"] == "error" for rec in lines)


def test_finish_is_idempotent(tmp_path):
    logger = RunLogger("x", log_dir=tmp_path).start()
    logger.finish(0)
    logger.finish(1)  # ignored
    lines = read_lines(logger.path)
    assert sum(1 for rec in lines if rec["event"] == "end") == 1
    assert lines[-1]["exit_status"] == 0


def test_run_ids_unique(tmp_path):
    a = RunLogger("x", log_dir=tmp_path)
    b = RunLogger("x", log_dir=tmp_path)
    assert a.run_id != b.run_id
