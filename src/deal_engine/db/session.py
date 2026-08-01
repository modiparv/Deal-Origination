"""Engine and session helpers.

SQLite runs with WAL and enforced foreign keys. Everything stays
dialect-portable — no SQLite-only SQL — so the migration trigger to
Postgres (a second concurrent writer, multi-GB analytics, concurrent
refresh) is a config change plus data copy, not a rewrite.
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from deal_engine.db.tables import Base

DEFAULT_DB_PATH = Path("data/engine.db")


def get_engine(db_path: Path | str = DEFAULT_DB_PATH) -> Engine:
    url = f"sqlite:///{Path(db_path)}"
    engine = create_engine(url)

    @event.listens_for(engine, "connect")
    def _pragmas(dbapi_connection, _record) -> None:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.close()

    return engine


def init_db(engine: Engine) -> None:
    Base.metadata.create_all(engine)


def make_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, expire_on_commit=False)
