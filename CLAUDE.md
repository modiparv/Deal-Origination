# House rules — deal origination engine

Read PLAN.md before changing anything structural. Build one phase at a
time; stop at each phase gate, run the tests, show the output, and wait.
If a requirement conflicts with what the data actually supports, stop and
say so — never work around it silently.

## Invariants (enforced in code and tests, not prompts)

1. **The language model never computes a financial figure.** Every stored
   figure has basis `filed` (verbatim from a source document, tag/location
   recorded), `derived` (named, tested Python function; input figure IDs
   recorded), or `modelled` (explicit model run). LLM prose cites figures
   with `{fig:ID}` markers; the renderer substitutes values. A bare
   financial numeral in rendered output fails the render.
2. **Provenance is mandatory and transitive.** A filed figure without a
   source document cannot be persisted (Pydantic validator + DB CHECK). A
   derived figure records its inputs; `provenance_walk` resolves any
   figure to source documents and detects cycles.
3. **Figures are observations.** The same (company, concept, period) from
   different filings coexists; `is_current` selection is deterministic
   (latest filed date wins). Re-ingest is idempotent: zero new rows, zero
   flag changes.
4. **Aggregators are not sources.** Aggregator-derived numbers carry
   basis `unverified` and never render in a profile.
5. **Every unattended run is logged** to `logs/runs/` (RunLogger).
6. **Ownership fail-closed:** ABSENCE OF A PSC STATEMENT IS NOT EVIDENCE
   OF INDEPENDENCE. Unclassifiable ownership is flagged, never passed.
7. **Signals are named after what is observed, not what is inferred** —
   `new_security_registered`, not `recent_debt_raise`.
8. **Core is jurisdiction-generic.** Jurisdiction facts live in
   `jurisdictions/*.yaml`; local registry vocabulary lives in
   `src/deal_engine/adapters/` and nowhere else — enforced by the
   leakage-guard test (`tests/test_leakage_guard.py`), which fails on any
   jurisdiction-specific token in core. Add local terms to the adapter's
   VOCABULARY map, never to core.
9. **Screening mode is per company.** `financial` (filed statements
   machine-readable) vs `signal` (observable behaviour only); rubric
   dimensions declare `requires_mode`; skipped dimensions are recorded
   and composites over partial dimensions carry `renormalised=True` —
   a partial score never renders as complete.

## Execution model

Pipeline writes to `data/` happen inside the `deal-engine` CLI process,
invoked via Bash. The PreToolUse guard (`.claude/hooks/guard.py`) denies
subagent Write/Edit on `data/**`, network calls outside the Companies
House allowlist, and anything touching credential files. The guard
pattern-matches tool arguments; it is a guardrail, **not** a network
egress sandbox — do not present it as containment.

## The commercial claim

Profiles state: "no public evidence of a current or recent sale process
as of {date}" with a dated evidence-of-absence list. Never claim a company
is "not being marketed" — no public registry can evidence that negative,
and filed data is 9–21 months stale by construction. Every rendered figure
shows its period end and filed date.

## Data reality (UK)

Most UK small companies file no public P&L (filleted accounts), and the
April 2028 reforms allow them to keep it non-public. EBITDA screening is
two-stage by design — filed P&L where it exists, balance-sheet/employee
proxies elsewhere, `insufficient_data` as a first-class outcome. This is
permanent architecture. The coverage report (by SIC code, within the
mandate's filtered universe) is a standing output of every ingest.

## Do not build

Automated outreach sending; ToS-violating scrapers; "total pipeline value"
metrics; adapter #2 before adapter #1 passes eval; dashboards before data
is verified; any LLM arithmetic.
