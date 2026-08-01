"""SQLAlchemy 2.0 typed declarative schema.

The invariants live here as constraints, not conventions:

- figures: UNIQUE observation key (source doc, concept, period, dimensions,
  unit) makes re-ingest idempotent; CHECK constraints enforce the
  provenance rules per basis so "the write raises" holds even for writes
  that bypass the Pydantic layer.
- source_documents: UNIQUE (adapter, external_document_id) — the fetch key.
- events: UNIQUE projection key so re-projection is idempotent.

SQLite note: NULLs are distinct in UNIQUE constraints, so derived figures
(source_document_id NULL) are not deduped by the observation constraint;
their identity is managed by the derive layer, which is deterministic.
"""

from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class CompanyRow(Base):
    __tablename__ = "companies"
    __table_args__ = (
        UniqueConstraint("jurisdiction", "registration_id", name="uq_company_registration"),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    jurisdiction: Mapped[str] = mapped_column(String, nullable=False)
    registration_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    name_variants: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    incorporation_date: Mapped[date | None] = mapped_column(Date)
    status: Mapped[str | None] = mapped_column(String)
    classification_codes: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    classification_taxonomy: Mapped[str | None] = mapped_column(String)
    registered_address: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    ownership_classification: Mapped[str | None] = mapped_column(String)
    ownership_confidence: Mapped[float | None] = mapped_column(Float)
    ownership_evidence: Mapped[list] = mapped_column(JSON, nullable=False, default=list)


class SourceDocumentRow(Base):
    __tablename__ = "source_documents"
    __table_args__ = (
        UniqueConstraint("adapter", "external_document_id", name="uq_source_document_identity"),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    adapter: Mapped[str] = mapped_column(String, nullable=False)
    jurisdiction: Mapped[str] = mapped_column(String, nullable=False)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    external_document_id: Mapped[str] = mapped_column(String, nullable=False)
    transaction_id: Mapped[str | None] = mapped_column(String)
    document_type: Mapped[str] = mapped_column(String, nullable=False)
    account_type: Mapped[str | None] = mapped_column(String)
    filed_date: Mapped[date | None] = mapped_column(Date)
    period_start: Mapped[date | None] = mapped_column(Date)
    period_end: Mapped[date | None] = mapped_column(Date)
    retrieved_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    content_type: Mapped[str | None] = mapped_column(String)
    raw_path: Mapped[str | None] = mapped_column(String)
    content_hash: Mapped[str | None] = mapped_column(String)
    fetch_headers: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    parse_status: Mapped[str] = mapped_column(String, nullable=False, default="pending")
    parse_error_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)


class FigureRow(Base):
    __tablename__ = "figures"
    __table_args__ = (
        UniqueConstraint(
            "source_document_id",
            "concept",
            "period_start",
            "period_end",
            "dimensions_hash",
            "unit",
            name="uq_figure_observation",
        ),
        CheckConstraint(
            "(basis != 'filed') OR (source_document_id IS NOT NULL "
            "AND source_tag IS NOT NULL AND derivation_function IS NULL)",
            name="ck_figure_filed_provenance",
        ),
        CheckConstraint(
            "(basis != 'derived') OR (derivation_function IS NOT NULL "
            "AND derivation_inputs IS NOT NULL AND source_document_id IS NULL)",
            name="ck_figure_derived_provenance",
        ),
        CheckConstraint(
            "(basis != 'modelled') OR (model_run_id IS NOT NULL)",
            name="ck_figure_modelled_provenance",
        ),
        CheckConstraint(
            "(basis != 'unverified') OR (aggregator_ref IS NOT NULL)",
            name="ck_figure_unverified_provenance",
        ),
        CheckConstraint(
            "(period_type != 'instant') OR (period_start = period_end)",
            name="ck_figure_instant_period",
        ),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    concept: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Numeric(20, 4), nullable=False)
    unit: Mapped[str] = mapped_column(String, nullable=False)
    currency: Mapped[str | None] = mapped_column(String(3))
    period_type: Mapped[str] = mapped_column(String, nullable=False)
    period_start: Mapped[date] = mapped_column(Date, nullable=False)
    period_end: Mapped[date] = mapped_column(Date, nullable=False)
    dimensions: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    dimensions_hash: Mapped[str] = mapped_column(String(16), nullable=False)
    consolidation: Mapped[str] = mapped_column(String, nullable=False, default="none")
    decimals: Mapped[int | None] = mapped_column(Integer)
    raw_text: Mapped[str | None] = mapped_column(Text)
    basis: Mapped[str] = mapped_column(String, nullable=False)
    source_document_id: Mapped[str | None] = mapped_column(ForeignKey("source_documents.id"))
    source_tag: Mapped[str | None] = mapped_column(String)
    derivation_function: Mapped[str | None] = mapped_column(String)
    derivation_inputs: Mapped[list | None] = mapped_column(JSON)
    model_run_id: Mapped[str | None] = mapped_column(String)
    aggregator_ref: Mapped[str | None] = mapped_column(String)
    is_current: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class OfficerRow(Base):
    __tablename__ = "officers"
    __table_args__ = (
        UniqueConstraint("company_id", "appointment_id", name="uq_officer_appointment"),
        CheckConstraint(
            "dob_month IS NULL OR (dob_month >= 1 AND dob_month <= 12)",
            name="ck_officer_dob_month",
        ),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    appointment_id: Mapped[str] = mapped_column(String, nullable=False)
    officer_id: Mapped[str | None] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    appointed_on: Mapped[date | None] = mapped_column(Date)
    resigned_on: Mapped[date | None] = mapped_column(Date)
    dob_month: Mapped[int | None] = mapped_column(Integer)
    dob_year: Mapped[int | None] = mapped_column(Integer)
    nationality: Mapped[str | None] = mapped_column(String)
    country_of_residence: Mapped[str | None] = mapped_column(String)


class BeneficialOwnerRow(Base):
    __tablename__ = "beneficial_owners"
    __table_args__ = (UniqueConstraint("company_id", "external_id", name="uq_beneficial_owner"),)

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    external_id: Mapped[str] = mapped_column(String, nullable=False)
    kind: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str | None] = mapped_column(String)
    name_elements: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    control_natures: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    notified_on: Mapped[date | None] = mapped_column(Date)
    ceased_on: Mapped[date | None] = mapped_column(Date)
    dob_month: Mapped[int | None] = mapped_column(Integer)
    dob_year: Mapped[int | None] = mapped_column(Integer)
    identification: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)


class OwnershipStatementRow(Base):
    __tablename__ = "ownership_statements"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    statement: Mapped[str] = mapped_column(String, nullable=False)
    notified_on: Mapped[date | None] = mapped_column(Date)
    ceased_on: Mapped[date | None] = mapped_column(Date)


class ExemptionRow(Base):
    __tablename__ = "exemptions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    exemption_type: Mapped[str] = mapped_column(String, nullable=False)
    items: Mapped[list] = mapped_column(JSON, nullable=False, default=list)


class FilingRow(Base):
    __tablename__ = "filings"
    __table_args__ = (UniqueConstraint("company_id", "transaction_id", name="uq_filing_transaction"),)

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    transaction_id: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str | None] = mapped_column(String)
    subcategory: Mapped[str | None] = mapped_column(String)
    type: Mapped[str | None] = mapped_column(String)
    filing_date: Mapped[date | None] = mapped_column(Date)
    description: Mapped[str | None] = mapped_column(String)
    description_values: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    document_id: Mapped[str | None] = mapped_column(String)
    paper_filed: Mapped[bool | None] = mapped_column(Boolean)


class SecurityInterestRow(Base):
    __tablename__ = "security_interests"
    __table_args__ = (UniqueConstraint("company_id", "external_id", name="uq_security_interest"),)

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    external_id: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str | None] = mapped_column(String)
    created_on: Mapped[date | None] = mapped_column(Date)
    delivered_on: Mapped[date | None] = mapped_column(Date)
    satisfied_on: Mapped[date | None] = mapped_column(Date)
    classification: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    details: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    secured_parties: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    transactions: Mapped[list] = mapped_column(JSON, nullable=False, default=list)


class EventRow(Base):
    __tablename__ = "events"
    __table_args__ = (
        UniqueConstraint(
            "company_id", "event_type", "event_date", "transaction_id", name="uq_event_projection"
        ),
        CheckConstraint(
            "transaction_id IS NOT NULL OR source_document_id IS NOT NULL",
            name="ck_event_sourced",
        ),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    event_type: Mapped[str] = mapped_column(String, nullable=False)
    event_date: Mapped[date] = mapped_column(Date, nullable=False)
    transaction_id: Mapped[str | None] = mapped_column(String)
    source_document_id: Mapped[str | None] = mapped_column(ForeignKey("source_documents.id"))
    payload: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)


class RunRow(Base):
    __tablename__ = "runs"

    run_id: Mapped[str] = mapped_column(String, primary_key=True)
    command: Mapped[str] = mapped_column(String, nullable=False)
    args: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    git_sha: Mapped[str | None] = mapped_column(String)
    started_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime)
    exit_status: Mapped[int | None] = mapped_column(Integer)
    counts: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    cost_usd: Mapped[float | None] = mapped_column(Float)


class ScreenResultRow(Base):
    __tablename__ = "screen_results"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    mandate_id: Mapped[str] = mapped_column(String, nullable=False)
    stage: Mapped[str] = mapped_column(String, nullable=False)
    outcome: Mapped[str] = mapped_column(String, nullable=False)
    failed_criteria: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.run_id"), nullable=False)


class ScoreRow(Base):
    __tablename__ = "scores"
    __table_args__ = (
        CheckConstraint(
            "(state = 'scored' AND score IS NOT NULL) OR "
            "(state != 'scored' AND score IS NULL AND state_reason IS NOT NULL)",
            name="ck_score_state_consistency",
        ),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    mandate_id: Mapped[str] = mapped_column(String, nullable=False)
    rubric_dimension: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False, default="scored")
    score: Mapped[float | None] = mapped_column(Float)
    rationale: Mapped[str] = mapped_column(Text, nullable=False)
    figure_ids_cited: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    state_reason: Mapped[str | None] = mapped_column(String)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.run_id"), nullable=False)


class CompositeScoreRow(Base):
    __tablename__ = "composite_scores"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    mandate_id: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    renormalised: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    dimensions_scored: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    dimensions_not_scored: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.run_id"), nullable=False)


class ConceptCoverageRow(Base):
    __tablename__ = "concept_coverage"
    __table_args__ = (
        UniqueConstraint(
            "run_id", "company_id", "concept", "period_end", name="uq_coverage_fact"
        ),
        CheckConstraint(
            "(status = 'not_filed' AND source_document_id IS NULL) OR "
            "(status != 'not_filed' AND source_document_id IS NOT NULL)",
            name="ck_coverage_document_reference",
        ),
        CheckConstraint(
            "(status != 'parse_failed') OR (detail IS NOT NULL)",
            name="ck_coverage_parse_failure_detail",
        ),
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.id"), nullable=False)
    concept: Mapped[str] = mapped_column(String, nullable=False)
    period_end: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    source_document_id: Mapped[str | None] = mapped_column(ForeignKey("source_documents.id"))
    detail: Mapped[str | None] = mapped_column(String)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.run_id"), nullable=False)
