"""deal-engine CLI."""

from __future__ import annotations

from pathlib import Path

import typer

from deal_engine.mandate.loader import MandateLoadError, load_mandate
from deal_engine.mandate.validator import Severity, validate_mandate
from deal_engine.runlog import RunLogger

app = typer.Typer(no_args_is_help=True, add_completion=False)
mandate_app = typer.Typer(no_args_is_help=True)
db_app = typer.Typer(no_args_is_help=True)
app.add_typer(mandate_app, name="mandate", help="Load and validate mandates")
app.add_typer(db_app, name="db", help="Database administration")

EXIT_VALIDATION_FAILED = 1
EXIT_LOAD_FAILED = 2
EXIT_NOT_IMPLEMENTED = 3
EXIT_MISSING_ENV = 4
EXIT_INGEST_ERRORS = 5


@mandate_app.command("validate")
def mandate_validate(
    path: Path = typer.Argument(..., help="Mandate YAML file"),
    jurisdictions: Path = typer.Option(
        Path("jurisdictions"), "--jurisdictions", help="Jurisdiction profile directory"
    ),
) -> None:
    """Validate a mandate against schema, registries, jurisdiction
    profiles and adapter capabilities."""
    logger = RunLogger("mandate validate", {"path": str(path)}).start()
    try:
        mandate = load_mandate(path)
    except MandateLoadError as exc:
        typer.echo(f"LOAD ERROR: {exc}", err=True)
        logger.finish(EXIT_LOAD_FAILED)
        raise typer.Exit(EXIT_LOAD_FAILED)

    report = validate_mandate(mandate, profile_dir=jurisdictions)
    for issue in report.issues:
        stream_err = issue.severity is Severity.ERROR
        typer.echo(f"{issue.severity.value.upper()} [{issue.code}] {issue.message}", err=stream_err)

    counts = {"errors": len(report.errors), "warnings": len(report.warnings)}
    if not report.ok:
        typer.echo(f"INVALID: {mandate.id} ({counts['errors']} error(s))", err=True)
        logger.finish(EXIT_VALIDATION_FAILED, counts)
        raise typer.Exit(EXIT_VALIDATION_FAILED)
    typer.echo(f"VALID: {mandate.id} ({counts['warnings']} warning(s) recorded)")
    logger.finish(0, counts)


@db_app.command("init")
def db_init(
    db_path: Path = typer.Option(Path("data/engine.db"), "--db", help="SQLite database path"),
) -> None:
    """Create the database schema."""
    from deal_engine.db.session import get_engine, init_db

    with RunLogger("db init", {"db": str(db_path)}):
        db_path.parent.mkdir(parents=True, exist_ok=True)
        init_db(get_engine(db_path))
        typer.echo(f"initialised {db_path}")


@app.command()
def ingest(
    mandate: Path = typer.Option(..., "--mandate", help="Mandate YAML file"),
    limit: int = typer.Option(200, "--limit", help="Maximum companies to ingest"),
    jurisdictions: Path = typer.Option(
        Path("jurisdictions"), "--jurisdictions", help="Jurisdiction profile directory"
    ),
    db_path: Path = typer.Option(Path("data/engine.db"), "--db", help="SQLite database path"),
    data_dir: Path = typer.Option(Path("data"), "--data", help="Data root (cache, reports)"),
    docs_per_company: int = typer.Option(
        3, "--docs-per-company", help="Accounts documents fetched per company"
    ),
    resume: bool = typer.Option(
        True, "--resume/--no-resume", help="Skip companies recorded in the checkpoint file"
    ),
) -> None:
    """Ingest the mandate's universe through the registered adapter for
    its jurisdictions.

    Adapter credentials come from environment variables (never flags:
    keys must not land in shell history or run logs); the adapter's
    runner declaration names which ones it needs."""
    import os

    logger = RunLogger("ingest", {"mandate": str(mandate), "limit": limit}).start()
    try:
        loaded = load_mandate(mandate)
    except MandateLoadError as exc:
        typer.echo(f"LOAD ERROR: {exc}", err=True)
        logger.finish(EXIT_LOAD_FAILED)
        raise typer.Exit(EXIT_LOAD_FAILED)
    report = validate_mandate(loaded, profile_dir=jurisdictions)
    if not report.ok:
        for issue in report.errors:
            typer.echo(f"ERROR [{issue.code}] {issue.message}", err=True)
        logger.finish(EXIT_VALIDATION_FAILED)
        raise typer.Exit(EXIT_VALIDATION_FAILED)

    from deal_engine.adapters.registry import ingest_runner_for

    runner = ingest_runner_for(set(loaded.geography.include))
    if runner is None:
        typer.echo(
            f"ERROR: no ingest adapter is implemented for jurisdictions "
            f"{sorted(loaded.geography.include)}",
            err=True,
        )
        logger.finish(EXIT_NOT_IMPLEMENTED)
        raise typer.Exit(EXIT_NOT_IMPLEMENTED)

    missing = [name for name in runner.required_env if not os.environ.get(name)]
    if missing:
        typer.echo(
            f"ERROR: adapter {runner.adapter!r} requires environment "
            f"variable(s) {', '.join(missing)} — set them before running ingest.",
            err=True,
        )
        logger.finish(EXIT_MISSING_ENV)
        raise typer.Exit(EXIT_MISSING_ENV)

    from deal_engine.db.session import get_engine, init_db, make_session_factory

    db_path.parent.mkdir(parents=True, exist_ok=True)
    engine = get_engine(db_path)
    init_db(engine)
    checkpoint = (
        data_dir / "ingest" / f"{loaded.id}.checkpoint.json" if resume else None
    )
    run = runner.load()
    summary = run(
        os.environ,
        make_session_factory(engine),
        loaded,
        run_id=logger.run_id,
        data_root=data_dir,
        limit=limit,
        docs_per_company=docs_per_company,
        checkpoint_path=checkpoint,
        progress=lambda msg: logger.log("progress", message=msg),
    )

    counts = {**summary["counts"], "ingested": summary["ingested"]}
    typer.echo(
        f"ingested {summary['ingested']} companies "
        f"(universe hits {summary['universe_hits']}, examined {summary['examined']}, "
        f"skipped {sum(summary['skipped'].values())}: {summary['skipped']})"
    )
    for key in sorted(counts):
        typer.echo(f"  {key}: {counts[key]}")
    typer.echo(f"coverage report: {summary['report_path']}")
    for code, bucket in summary["coverage"]["by_classification_code"].items():
        typer.echo(f"  {code}: {bucket['companies']} companies")
    if summary["errors"]:
        for line in summary["errors"]:
            typer.echo(f"ERROR: {line}", err=True)
        logger.finish(EXIT_INGEST_ERRORS, counts)
        raise typer.Exit(EXIT_INGEST_ERRORS)
    logger.finish(0, counts)


if __name__ == "__main__":
    app()
