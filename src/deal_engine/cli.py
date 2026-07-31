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


@mandate_app.command("validate")
def mandate_validate(path: Path = typer.Argument(..., help="Mandate YAML file")) -> None:
    """Validate a mandate against schema, registries and adapter capabilities."""
    logger = RunLogger("mandate validate", {"path": str(path)}).start()
    try:
        mandate = load_mandate(path)
    except MandateLoadError as exc:
        typer.echo(f"LOAD ERROR: {exc}", err=True)
        logger.finish(EXIT_LOAD_FAILED)
        raise typer.Exit(EXIT_LOAD_FAILED)

    report = validate_mandate(mandate)
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
) -> None:
    """Ingest companies for a mandate (Companies House adapter: Phase 1)."""
    logger = RunLogger("ingest", {"mandate": str(mandate), "limit": limit}).start()
    try:
        loaded = load_mandate(mandate)
    except MandateLoadError as exc:
        typer.echo(f"LOAD ERROR: {exc}", err=True)
        logger.finish(EXIT_LOAD_FAILED)
        raise typer.Exit(EXIT_LOAD_FAILED)
    report = validate_mandate(loaded)
    if not report.ok:
        for issue in report.errors:
            typer.echo(f"ERROR [{issue.code}] {issue.message}", err=True)
        logger.finish(EXIT_VALIDATION_FAILED)
        raise typer.Exit(EXIT_VALIDATION_FAILED)
    typer.echo(
        "ingest is not available yet: the Companies House adapter arrives in "
        "Phase 1 (the mandate itself validated successfully)",
        err=True,
    )
    logger.finish(EXIT_NOT_IMPLEMENTED)
    raise typer.Exit(EXIT_NOT_IMPLEMENTED)


if __name__ == "__main__":
    app()
