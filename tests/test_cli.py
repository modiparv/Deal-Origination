import pytest

pytest.importorskip(
    "pydantic",
    reason="pydantic v2 unavailable in this environment (PyPI blocked); "
    "the full Phase 0 gate requires it — see PLAN.md §8",
)

from pathlib import Path  # noqa: E402

from typer.testing import CliRunner  # noqa: E402

from deal_engine import cli  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EXAMPLE = ROOT / "mandates" / "example-lmm-uk.yaml"
FIXTURES = ROOT / "tests" / "fixtures" / "mandates"

runner = CliRunner()


@pytest.fixture(autouse=True)
def _isolated_logs(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)  # run logs land in tmp, not the repo


def test_validate_example_exits_zero_with_warning():
    result = runner.invoke(cli.app, ["mandate", "validate", str(EXAMPLE)])
    assert result.exit_code == 0, result.output
    assert "VALID: lmm-uk-buyout" in result.output
    assert "conditional_coverage" in result.output


def test_validate_gb_ie_exits_nonzero_naming_jurisdiction():
    result = runner.invoke(
        cli.app, ["mandate", "validate", str(FIXTURES / "gb-ie-ebitda.yaml")]
    )
    assert result.exit_code == cli.EXIT_VALIDATION_FAILED
    combined = result.output
    assert "no_adapter_for_jurisdiction" in combined
    assert "'IE'" in combined


def test_validate_missing_file_exits_load_error():
    result = runner.invoke(cli.app, ["mandate", "validate", "nope.yaml"])
    assert result.exit_code == cli.EXIT_LOAD_FAILED


def test_validate_logs_run(tmp_path):
    result = runner.invoke(cli.app, ["mandate", "validate", str(EXAMPLE)])
    assert result.exit_code == 0
    logs = list((tmp_path / "logs" / "runs").glob("*.jsonl"))
    assert len(logs) == 1


def test_ingest_validates_then_reports_not_implemented():
    result = runner.invoke(cli.app, ["ingest", "--mandate", str(EXAMPLE)])
    assert result.exit_code == cli.EXIT_NOT_IMPLEMENTED
    assert "Phase 1" in result.output


def test_db_init(tmp_path):
    result = runner.invoke(cli.app, ["db", "init", "--db", str(tmp_path / "e.db")])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "e.db").exists()
