# Deal Origination Engine

A mandate-driven deal origination engine. It ingests public company data
from statutory registries, normalises it into a canonical schema, screens
it against configurable investment mandates, and produces sourced company
profiles and first-draft screening memos.

Its defining property is **traceability**: every financial figure it
displays resolves to a specific filed document. The language model reads
figures and writes prose; it never computes or stores a number.

The claim the system makes for a candidate is deliberately modest: *"no
public evidence of a current or recent sale process as of {date}"*, backed
by a dated evidence list. It does not claim to find deals before brokers,
predict outcomes, or replace relationship-based origination — and it does
not claim a company is "not being marketed", because no public registry
can evidence that negative.

## Status

Phase 0 (foundation) built: canonical schema, mandate loader/validator
with capability-matrix declarations, provenance enforcement, prose-numeral
render validator, guard hooks, run logging, CLI. The Companies House
adapter is Phase 1. See PLAN.md for the full plan and decision record.

## Quickstart

```bash
pip install -e ".[dev]"
deal-engine mandate validate mandates/example-lmm-uk.yaml
deal-engine db init
pytest
```

Copy `.env.example` to `.env` and set `CH_API_KEY` (free, from the
Companies House Developer Hub) before Phase 1 ingest.

## Layout

```
mandates/            mandate YAMLs (nothing about a mandate is hardcoded)
src/deal_engine/
  concepts.py        canonical concept registry
  models/            Pydantic v2 domain models (validation at boundaries)
  db/                SQLAlchemy 2.0 schema (constraints own the invariants)
  adapters/          adapter protocol + static capability declarations
  mandate/           YAML loader + ERROR/WARNING validator
  derive/            derived-metric declarations (implementations: Phase 2)
  signals/           signal detector declarations (implementations: Phase 2)
  render/            {fig:ID} marker validation and substitution
  runlog.py          per-run JSONL logging
  cli.py             Typer CLI
evals/               golden fixtures (populated in Phase 1)
tests/
```
