# Implementation Plan — Phase 0 & Phase 1

Status: **approved 2026-07-31 — all twelve §7 decisions accepted, three with amendments (3, 6, 7), plus two additions (§13 permanence of the P&L gap, §14 company-level eval set). Phase 0 built on this basis.**

**Amendment 2 (2026-07-31, pre-merge): generalise before merge.** The system is jurisdiction-generic in its interfaces with Companies House as the first and only implemented adapter. Applied: (1) screening mode (`financial`/`signal`) promoted to a first-class per-company concept — mandates declare `required_modes`, rubric dimensions declare `requires_mode`, skipped dimensions are recorded on Score rows and composites renormalise with a mandatory flag; decision #3's two-stage screening is the FINANCIAL path with per-company SIGNAL fallback, `on_insufficient_data` unchanged. (2) `jurisdictions/` profile layer added — `gb.yaml` holds the register scope, identifier format, taxonomy, filing cadence/lag and disclosure caveats; the validator reads profiles alongside capability matrices. (3) Core vocabulary neutralised (beneficial_owner, security_interest, classification_code, registration_id, fiscal_period_end; document-regime names are coverage facts, not core states) with the Companies House terms mapped in the adapter's VOCABULARY. (4) A leakage-guard test fails on any jurisdiction token outside `adapters/` and `jurisdictions/`. (5) Second negative fixture: FINANCIAL-mode mandate over a signal-only jurisdiction profile. Everything in decisions 2, 5–12 is unchanged. The decision record is summarised inline below; amendments are marked **[AMENDED]**.

This plan covers Phase 0 (Foundation) and Phase 1 (Companies House adapter) only, per §0 of the brief. Before writing it, the external facts the design depends on were verified against primary sources: Companies House's own API spec and enumeration repositories, the `ixbrlparse` and `stream-read-xbrl` source code, GOV.UK/ICAEW/FRC publications on filing regimes and the ECCTA timeline, CRO (Ireland) documentation, and the current Claude Code CLI documentation. Where a claim below could not be verified from a primary source, it is marked. Live-API verification (hitting the real endpoints with a key) remains the first task of Phase 1 — this document tells us what to expect, not what the wire returned.

Contents:

1. [Summary](#1-summary)
2. [Where the brief is wrong — findings that change the design](#2-where-the-brief-is-wrong)
3. [Phase 0 plan](#3-phase-0-plan)
4. [Phase 1 plan](#4-phase-1-plan)
5. [Canonical schema, concretely](#5-canonical-schema-concretely)
6. [Answers to the §11 open questions](#6-answers-to-the-11-open-questions)
7. [Decisions needing your approval](#7-decisions-needing-your-approval)
8. [Environment prerequisites](#8-environment-prerequisites)

---

## 1. Summary

Phase 0 delivers the scaffold, the canonical schema (Pydantic v2 domain models + SQLAlchemy 2.0 tables), the mandate loader/validator with static capability-matrix declarations, the prose-numeral validator, PreToolUse hook config, the run logger, and a Typer CLI — gated on `deal-engine mandate validate` correctly accepting a clean mandate and rejecting broken ones for the *right reasons*.

Phase 1 delivers the Companies House adapter end to end: live API verification, universe enumeration via advanced search, per-company ingestion (profile, officers, PSC, charges, filing history), document retrieval with iXBRL content negotiation, parsing into provenance-carrying figure rows via a versioned concept map, entity resolution, idempotent re-ingest, incremental refresh via filing-history diff, and a golden fixture set for the parser — gated on the 200-company ingest with a spot-checkable sample **plus a coverage report** (see below for why that addition matters).

The single most important research finding, stated up front because §0 requires it: **the brief's §2 claim "UK: full statutory accounts, iXBRL-tagged" is false for most of the companies the example mandate targets.** Small companies file "filleted" accounts with no profit & loss at Companies House, and the small-company threshold rose to £15m turnover for periods beginning on/after 6 April 2025. A large share of the £1–2.5m EBITDA band therefore has **no public revenue or operating profit at all**, and this does not improve before April 2028 (and possibly not after — see Finding W1). The architecture survives this; the example mandate and the capability-matrix design as specified do not. Everything else in this plan is downstream of handling that honestly.

---

## 2. Where the brief is wrong

Per §0's instruction to list decisions I think are wrong, ranked by how much they change the Phase 0/1 design. "W" findings are wrong claims/decisions; "C" findings are internal contradictions in the brief.

### W1 (critical) — The UK data does not support register-wide EBITDA screening

§2's table says UK has "full statutory accounts, iXBRL-tagged, free API. Financial screening is genuinely possible." §6's example mandate screens on EBITDA £1–5m. Reality:

- **Micro-entities** (turnover ≤ £1m) file ~5 balance-sheet lines. No P&L, no cash breakdown.
- **Small companies** — now turnover ≤ £15m, balance sheet ≤ £7.5m, ≤ 50 employees (2 of 3), after the ~50% threshold uplift for periods beginning on/after 6 April 2025 — may file "filleted" (s444) accounts: **no P&L, no directors' report**. Nearly all of them do. What survives: full balance sheet, notes (PPE incl. depreciation charge, debtors, cash, creditors splits), and the statutory **average-employees** footnote.
- Register-wide, roughly **95% of filed accounts contain no public P&L** (micro + total-exemption-full + dormant dominate the register; full/group/medium accounts are ~4–8% of filings).
- Split the mandate band by implied turnover: **£2.5–5m EBITDA** companies are usually medium/large → full audited accounts, P&L available, screenable as the brief imagines. **£1–2.5m EBITDA** companies very often qualify as small → filleted → revenue and operating profit are simply not on the public record. The April 2025 uplift moved ~14,000 companies from medium to small, so go-forward coverage in the band gets *worse* through 2027.
- **The ECCTA fix does not rescue this.** Confirmed 9 June 2026: accounts reform lands 1 April 2028 (delayed from 2027) — software-only iXBRL filing, abridged accounts abolished, small/micro companies must file a P&L — **but small/micro companies may opt out of the P&L appearing on the public register**. Privacy-motivated founder/family owners — precisely this mandate's targets — are the likeliest opt-outs. Do not architect on the assumption the gap closes.

**Design consequences (all incorporated below):**

1. The **capability matrix cannot be boolean**. It needs per-concept coverage tiers — `always` / `conditional(condition)` / `never` — because `revenue` availability in the UK is per-company, knowable cheaply in advance from the accounts type (`micro-entity`, `total-exemption-full`, `small`, `medium`, `full`, `group`, `dormant`, …) on the company profile and filing history.
2. Mandate validation over `size.metric: ebitda` for GB must **pass with a recorded warning and estimated coverage**, not pass clean or fail hard. Hard-fail stays reserved for "no adapter covers this jurisdiction/metric at all" (which is exactly what IE triggers — see W2).
3. Screening (Phase 2, but the schema is Phase 0) must treat **"insufficient data" as a first-class outcome distinct from "failed"**. Filleted-accounts companies are not "not matching"; they are "primary metric unobservable", carried forward on proxy metrics or parked, per mandate policy. **[AMENDED]** The `on_insufficient_data` policy resolves **per company**, not globally per mandate; and the two-stage design is **permanent architecture, not a transitional stopgap** — the April 2028 reform's publication opt-out means the population likeliest to opt out is exactly the mandate's target population (§13 of the decision record).
   **[AMENDED]** Two corrections to how this finding is quantified: (a) the ~95% figure is register-wide and dominated by dormant/micro entities no mandate would screen — the rate **within the mandate's filtered universe** is what matters, is far lower, and gets measured and reported in Phase 1 rather than assumed; (b) the P&L observability crossover is **sector-margin-dependent, not a fixed EBITDA level** (filing obligation keys off turnover: at 25% margins the small-company threshold crosses ~£3.75m EBITDA, at 5% distribution margins ~£750k), so the Phase 1 coverage report breaks down observability **by classification code**, not just in aggregate — and it is a **standing output** of every ingest, not a one-off diagnostic.
4. **`average_number_employees` is promoted to a first-class canonical concept.** It is the one P&L-adjacent figure present in *every* regime including micro and filleted accounts (statutory footnote), and the best free size proxy for P&L-invisible companies. Same promotion for `net_assets`/`equity`, `cash`, `creditors_within_one_year`, `creditors_after_one_year`, `total_assets_less_current_liabilities`.
5. The Phase 1 gate gains a **coverage report**: of the 200 ingested companies, how many have a filed P&L vs balance-sheet-only. You should see this number before approving Phase 2's screening design.

### W2 (critical) — IE does not belong next to UK, and the example mandate fails its own validator

§2 groups "UK / IE" as one cell. Ireland's CRO has a free search/metadata API (CRO Open Services), but **filed accounts are pay-per-document (€2.50–€3.50), PDF-only** — Irish iXBRL goes to Revenue with the tax return and is not public — and Irish small companies use the s352/353 abridgement exemption to omit the P&L anyway. Companies House covers GB only (incl. Northern Ireland); it has no Irish companies beyond overseas-establishment registrations.

So the shipped `example-lmm-uk.yaml` (`geography: [GB, IE]`, `size.metric: ebitda`) **fails the brief's own §6 validation rule** ("every size.metric is supplied by at least one enabled adapter for every included jurisdiction") the moment the capability matrix is honest — and the Phase 0 gate needs that same file to validate cleanly.

**Proposal:** ship `example-lmm-uk.yaml` with `geography: [GB]`; keep a `[GB, IE]` variant as the Phase 0 gate's *deliberately broken* mandate — it exercises exactly the capability-matrix rejection path with a real-world error ("no enabled adapter supplies ebitda for jurisdiction IE") rather than a synthetic one. IE stays in the system's vocabulary as a documented future paid adapter (~€2.5–3.5k per 1,000 companies for latest accounts, PDF parsing burden, partial P&L coverage even then). `Figure.source_tag`'s "tag **or location**" wording already accommodates a future PDF adapter's page-reference provenance — no schema change needed, and none of this justifies touching adapter #2 before adapter #1 passes eval.

### W3 (high) — `enterprise_value` as a secondary size metric is unobservable

EV = equity value + net debt. Private companies have no observable equity value; net debt is only partially reconstructable (borrowings are folded into `creditors_*` mixed with trade creditors and accruals; the bank-loans note is often untagged in small accounts). Under the brief's own §3.1 taxonomy, any EV is `basis: modelled`; under §3.5 an aggregator's EV is `unverified` and unrenderable. The shipped example would violate the brief's own fail-loudly rule on day one.

**Proposal:** drop `enterprise_value` from the example mandate. Add a validator rule: a mandate metric no adapter supplies as `filed`/`derived` must be explicitly declared `modelled` in the YAML with a named model, or validation fails.

### W4 (high) — `recent_debt_raise` detects less than its name claims

Post-April-2013 charge registrations (MR01 regime) **do not state the amount secured** — `secured_details` is typically "all monies due or to become due". Charges capture secured lending only (shareholder loans, unsecured debt, facility drawdowns are invisible), and a new charge frequently accompanies refinancing, invoice-finance setup, asset finance, or a rent deposit deed rather than new money. What *is* reliable: the event dates, the lender identity (`persons_entitled` — often a security agent), and fixed/floating classification.

**Proposal:** rename the signal to `new_security_registered`, with lender name and classification as attributes and documented false-positive filters (refinance = prior charge satisfied within ±90 days; invoice-finance/asset-finance lender name lists; landlord deposit deeds; intra-group security). A jump in `creditors_after_one_year` between two filed balance sheets is a legitimate `derived` corroborator. The mandate vocabulary should not imply an amount or new borrowing that the data cannot show.

### W5 (high) — Succession signal: `require_no_successor` has no public-data denotation, and director ≠ owner

Officer and PSC DOBs are month+year (day suppressed since 2015) — ample for an age threshold, and the brief's `dob_month`/`dob_year` model is exactly right. But there is no filed concept of a "successor"; any implementation is a heuristic. And the age that matters for a buyout thesis is the **owner's** (individual PSC with a control band), not any director's — a 60-year-old non-shareholder FD is not a succession signal. Non-board successors (a hired MD not yet appointed director) are invisible by design; the `occupation` field is unreliable free text and must be ignored.

**Proposal:** split the signal in the mandate schema into (a) `psc_age_threshold` — implementable, grounded in filed data, keyed on individual PSCs holding ≥25% bands, with director age as a secondary check; and (b) an explicitly named heuristic `no_younger_director_appointed: {age_below: 48, within_years: 5}` replacing `require_no_successor`, documented with its failure modes. Exclude formation-agent directors (appointed at incorporation, resigned within ~30 days).

### W6 (high) — The §1 commercial claim "not currently being marketed" cannot be evidenced

Nothing in public statutory data can positively evidence that a company is *not* being marketed: sale mandates, IMs, and data rooms leave no trace at Companies House, and filed financials are 9–21 months stale by construction (private companies file 9 months after year end) — an entire sale process fits inside the staleness window. §11 already doubts this; §1 should not promise what §11 doubts.

**Proposal:** reword the claim (in README/CLAUDE.md at Phase 0) to **"no public evidence of a current or recent sale process as of {date}"**, rendered in profiles as an explicit dated evidence-of-absence list: PSC unchanged N years, no holdco insertion or share-for-share reorganisation, no acquisition-pattern charges, no exemption, active status, no strike-off action. Weak positive tells (ARD change for a clean year-end, auditor upgrade, subsidiary cleanup) become a "possible process" flag — never proof of the negative. Every rendered figure carries its period-end and filed date so staleness is visible.

### W7 (medium) — Ownership include/exclude cannot be a hard boolean filter

PSC data supports classification, but: percentages exist only as three bands (25–50/50–75/75–100 — the schema must model bands, never a number); corporate-PSC chains need recursive resolution (PE deals show stacked Topco/Midco/Bidco newcos, and the fund vehicle is usually not a registrable RLE, so the top UK company often shows a `significant-influence-or-control`-only entry or a **statement**); ~20% of entities declare no individual beneficial owner; nominee and trust structures are partially visible at best. The dangerous error for an exclusion mandate is a PE-backed company classified "independent" because its Topco filed a no-PSC statement.

**Proposal:** ownership classification is a rules engine outputting `(classification, confidence, evidence[])` with an explicit `unclassifiable` value; mandate exclude-rules operate "exclude when confidently excluded; **flag** when unclassifiable" (fail-closed, per-mandate policy). `founder_owned` and `family_owned` merge into one screening class (they overlap heavily and the mandate treats them identically). Listed/listed-subsidiary detection uses the `/company/{n}/exemptions` resource (near-definitive) plus corporate-PSC chain resolution; note AIM companies are not exemption-covered and ~65k companies unlawfully name unlisted foreign parents, so overseas-parent inference needs a small reference list before it is trusted.

### W8 (medium) — SIC wildcards are a recall net, not a precision filter

SIC codes are self-reported, never verified, frequently stale, up to 4 per company; huge mass sits in generic codes (82990 "other business support", 70100 "head office", 64209 holding companies), and group topcos carry holding-company codes while the trading subsidiary carries the real one. Also, mechanically: **the advanced search API takes exact 5-digit codes only — `620*` wildcards must be expanded client-side** against the SIC 2007 condensed list.

**Proposal:** treat SIC as candidate generation (recall-oriented); confirm sector downstream from the filed "principal activity" text in the directors' report/accounts, which is traceable to a document. Entity resolution must eventually link topco filers to trading subsidiaries (Phase 2+; Phase 1 records group links where PSC/parent data reveals them).

### C1 (critical) — Figure has no workable natural key: restated comparatives guarantee collisions

Every UK filing contains the current period **and** prior-period comparatives. After ingesting FY2024 and FY2023 accounts you hold two figures for (company, revenue, FY2023) from two different documents — and they can legitimately disagree (FRS 102 s.10 prior-period adjustments, re-presented comparatives). As specified, DoD #4 ("no duplicate figures") is either unimplementable or forces silent overwrites that destroy provenance.

**Proposal (schema-level, Phase 0):** figures are **observations** — natural key `(source_document_id, concept, period_start, period_end, dimensions_hash, unit)`, UNIQUE-constrained. A deterministic **canonical selection** marks one observation per `(company, concept, period, dimensions)` as `is_current`: latest filed date wins, tie-break on document ID; superseded observations are never deleted. A later filing whose comparative disagrees with an earlier primary figure emits a `restatement` Event — that divergence is itself a screening-quality signal. **[AMENDED]** Restatement events carry a **materiality gate**: both a relative and an absolute floor, configurable per concept (in the concept-map data), and the event is classified where possible (`rounding` / `reclassification` / `genuine`) — a £1 rounding delta must not share a table with a restated prior-year EBITDA, or the flag is worthless. **DoD #4 is redefined precisely: re-running ingest produces zero new rows and zero changed `is_current` flags.** Periods key on exact dates, never "year" — ARD changes produce stub/long periods, and growth functions must refuse to compare materially different period lengths.

### C2 (critical) — §3.1 vs §3.2: derived figures cannot have a NOT NULL `source_document_id`

A derived figure (EBITDA = operating profit + D&A) has no single source document — its inputs may span filings. §3.2's "no nullable path" and §3.1's derivation recording cannot both hold on one NOT NULL column.

**Proposal:** provenance is **transitive**. `source_document_id` is required iff `basis = filed`; `derivation` (function name + input figure IDs) is required iff `basis = derived`. **[AMENDED]** Enforced at **two** layers — Pydantic model validator + SQLAlchemy CHECK constraint — not three; the pre-flush listener is dropped unless bulk inserts that bypass ORM validation are ever introduced, at which point it returns with them, stated explicitly. A `provenance_walk(figure_id)` function resolves any figure to its full set of source documents — **with cycle detection that fails loudly** — and the provenance validator (DoD #3) asserts the walk terminates at filed figures for every persisted row.

### C3 (high) — `content_hash` cannot be the cache key: it's circular

You can't know a document's hash before fetching it, so a hash-keyed cache can never answer "have I already fetched this?" — every refresh becomes a full re-download.

**Proposal:** fetch decisions key on the adapter-native identity: `(adapter, external_document_id)` — for CH, the document ID from the filing-history item's `links.document_metadata` URL (plus `transaction_id`). `content_hash` is computed **after** fetch and stored for integrity re-verification and change detection: if refetching the same document ID ever yields a different hash, alert loudly rather than overwrite (§5 immutability). Blobs are stored content-addressed (`data/cache/sha256/ab/abcd…`) with `SourceDocument.raw_path` pointing in — dedupe for free, immutability physically true, and the SourceDocument row commits only after the blob is fully written and hashed.

### C4 (high) — The §3.1 numeral validator as specified makes honest prose unwritable

Prose necessarily contains years, dates, counts ("three of five directors"), ages, and mandate-threshold echoes; and computed percentages ("grew 12%") are exactly the LLM arithmetic §3.1 bans.

**Proposal (invert the problem):** the LLM **never writes financial numerals at all**. It writes citation markers — `{fig:F0123}`, optionally `{fig:F0123:pct}` — and the renderer substitutes formatted values from the database, so a quantity *cannot* appear without a figure ID. Anything the LLM would want to compute (growth, margins) must pre-exist as a Phase 2 derived figure; the derive layer eagerly computes the standard ratio set per company so there is something to cite. The validator is a pure string function (no LLM dependency — buildable and testable in Phase 0, satisfying DoD #5 before Phase 3 exists): every marker must resolve; any remaining bare numeral fails unless it matches a small typed whitelist (4-digit years, ISO dates, single-digit counts, numerals appearing verbatim in the mandate YAML). Whitelist enumerated in code and tested in both directions.

### C5 (high) — The §6 validator rules are circular at Phase 0

"Every size.metric is supplied by an enabled adapter" and "every signal has an implementing detector" reference adapters (Phase 1) and detectors (Phase 2) that don't exist at the Phase 0 gate.

**Proposal:** Phase 0 ships **static declaration registries**: each adapter's `CapabilityMatrix` is an importable declaration (no live API, no implementation needed); derived metrics register `name → required input concepts` (so `ebitda` capability resolves through its inputs); signal detectors register names + parameter schemas. Implementations land in their phases; declarations exist day one, and the Phase 0 gate validates against declarations. Validation results carry **severities**: ERROR (reject — e.g. no adapter for a jurisdiction, unknown detector, weights ≠ 1.0) vs WARNING (proceed with recorded coverage gaps — e.g. `ebitda` only conditionally available for GB).

### C6 (medium) — §3.3's data/-write deny vs the Phase 1 gate; and hooks are not an egress sandbox

Denying "writes to `data/` from any subagent" while the Phase 1 gate *is* an ingest that writes to `data/` requires stating the execution model: pipeline writes happen inside the `deal-engine` CLI process invoked via Bash; the PreToolUse deny targets subagent `Write`/`Edit` tool calls on `data/**` and must not block invoking the CLI. Verified against current docs: PreToolUse hooks in `.claude/settings.json` can return `permissionDecision: "deny"`, deny holds under permissive permission modes, and hook input carries an `agent_id` field allowing subagent-scoped rules — all as the brief assumes. One honesty note for CLAUDE.md: hooks pattern-match tool-call **arguments** (URLs, command strings); they are not a network egress sandbox — a subprocess spawned by an allowed command can reach any domain. The allowlist is a guardrail, not containment.

### C7 (medium) — The adapter eval set is mis-scheduled to Phase 3

§2 gates adapter #2 on adapter #1 "passing its eval set", but §7 first mentions golden sets in Phase 3. The adapter eval must exist in **Phase 1**: a golden set of real cached iXBRL filings with hand-verified expected figure rows, doubling as the parser regression suite across FRC taxonomy generations. (Phase 3's scorer golden set is a separate, additional artifact.)

### Minor factual corrections

- The Document API host is `document-api.company-information.service.gov.uk` (hyphenated), not `document.api...`. Better: never construct it — filing-history items return `links.document_metadata` as an absolute URL.
- Fetching document content returns a **302 to a presigned S3 URL, which must be followed without the Authorization header** (S3 rejects double auth) — handle the redirect manually in httpx.
- `claude -p --output-format json --json-schema` exists, but `--json-schema` takes the **schema as a JSON string argument**, not a file path; the validated object arrives in a `structured_output` field. `--model haiku|sonnet|opus` aliases are confirmed. `duration_ms` is not in the JSON envelope (capture wall time and exit code in the wrapper); `--max-turns` could not be verified in current docs — the Phase 3 design should re-verify or drop it.
- The filing-history `category` enum documented by CH is officially incomplete (CH acknowledges `confirmation-statement`, `gazette`, etc. appear in live data) — never validate strictly against it. Vendor `companieshouse/api-enumerations` as the canonical enum source. Two verbatim-spelling gotchas: the canonical PSC statement enum key `no-individual-or-entity-with-signficant-control` (sic) and the charges field `unfiletered_count` (sic) — parse tolerantly.
- Officer/PSC DOB month+year and the charges/insolvency field surfaces match the brief's assumptions — verified against CH's own spec repos.

---

## 3. Phase 0 plan

### 3.1 Files to create

Repo root is this repository (the brief's `deal-engine/` becomes the repo root; the package name stays `deal_engine`).

```
pyproject.toml                  # hatchling; py>=3.11; pydantic>=2.7, sqlalchemy>=2.0,
                                # typer, httpx, pyyaml, ixbrlparse==0.11.*, pytest, respx (dev)
README.md                       # incl. reworded commercial claim (W6)
CLAUDE.md                       # house rules: invariants §3.1–3.5, execution model (C6),
                                # "hooks are guardrails not containment" note
.env.example                    # CH_API_KEY= (REST key; stream key is a distinct type, unused Phase 1)
.gitignore                      # data/, logs/, .env
.claude/settings.json           # PreToolUse hooks (see 3.4)
.claude/hooks/guard_network.py  # allowlist deny for WebFetch/Bash-curl outside source domains
.claude/hooks/guard_data.py     # deny subagent Write/Edit on data/**; deny anything touching .env*
mandates/example-lmm-uk.yaml    # geography [GB]; signals renamed (W4/W5); no enterprise_value (W3)
tests/fixtures/mandates/        # broken mandates: bad weights, unknown taxonomy, unknown detector,
                                #   gb-ie-ebitda.yaml (the real-world capability failure, W2)
src/deal_engine/__init__.py
src/deal_engine/concepts.py     # canonical concept registry: name, period_type, expected sign,
                                #   coverage notes (W1 promotions)
src/deal_engine/models/         # Pydantic v2 domain models (validation at boundaries)
    company.py officer.py psc.py figure.py source.py event.py filing.py
    mandate.py screen.py run.py
src/deal_engine/db/             # SQLAlchemy 2.0 typed declarative (constraints live here)
    tables.py session.py repository.py   # + pre-flush provenance listener (C2)
src/deal_engine/adapters/
    base.py                     # Adapter Protocol + CapabilityMatrix (tiered, per-jurisdiction)
    registry.py                 # static declarations importable without implementations (C5)
src/deal_engine/mandate/
    loader.py validator.py      # YAML → Mandate; rules with ERROR/WARNING severities
src/deal_engine/derive/
    registry.py                 # declarations only: metric name → required input concepts (C5)
src/deal_engine/signals/
    registry.py                 # detector declarations: name → parameter schema (C5)
src/deal_engine/render/
    validator.py                # {fig:ID} marker resolution + numeral whitelist (C4) — pure strings
src/deal_engine/runlog.py       # JSONL per run to logs/runs/; run_id, args, counts, duration, exit
src/deal_engine/cli.py          # Typer: `mandate validate`, `db init`, `ingest` (stub until Phase 1)
data/cache/.gitkeep  data/.gitkeep  logs/runs/.gitkeep
evals/golden/.gitkeep  evals/test_eval.py   # harness skeleton; populated in Phase 1 (C7)
tests/
    test_models.py              # incl. Pydantic↔SQLAlchemy field parity test
    test_provenance.py          # write-raises tests: figure w/o source, derived w/o inputs
    test_mandate_validator.py   # accepts example; rejects each broken fixture w/ specific error
    test_render_validator.py    # marker resolution + whitelist, both directions (DoD #5)
    test_runlog.py
```

Not in Phase 0: `.claude/skills/`, `.claude/agents/`, `src/deal_engine/{ingest,parse,resolve,screen,score,profile,llm}/` — created in their phases so the repo never contains dead scaffolding ahead of its gate. (`derive/` and `signals/` exist in Phase 0 as declaration registries only.)

### 3.2 Persistence pattern

Two thin layers, not SQLModel: **SQLAlchemy 2.0 typed declarative** models own the invariants (UNIQUE, CHECK, FK, NOT NULL, pre-flush listeners) — the constraints that make §3.2 "the write raises" true regardless of caller. **Pydantic v2** domain models (`from_attributes=True`) own boundary validation with good error messages (`derivation` required iff `basis=derived`, band-only ownership, etc.). A thin repository bridges them; a unit test asserts field parity so the layers can't drift. SQLModel is avoided deliberately: it couples the layers and makes multi-field CHECKs awkward.

### 3.3 Mandate spec changes (the YAML you'll approve)

```yaml
id: lmm-uk-buyout
geography:
  include: [GB]                        # W2; NI is GB for registry purposes
size:
  primary:
    metric: ebitda                     # stays — but validates to WARNING for GB (W1):
    currency: GBP                      #   conditional coverage, recorded on the run
    min: 1_000_000
    max: 5_000_000
  on_insufficient_data: flag           # W1: park, don't fail — explicit policy
sectors:                               # unchanged; wildcards expanded client-side (W8)
ownership:
  include: [owner_managed, independent]  # founder+family merged (W7)
  exclude: [pe_backed, listed, listed_subsidiary]
  on_unclassifiable: flag              # fail-closed policy (W7)
signals:
  succession_risk:
    psc_age_threshold: 58              # W5: keyed on individual PSCs
    no_younger_director_appointed: {age_below: 48, within_years: 5}   # named heuristic
  new_security_registered:             # W4: renamed from recent_debt_raise
    lookback_months: 24
    exclude_refinance: true
    exclude_lender_categories: [invoice_finance, asset_finance, landlord]
rubric: (unchanged)
thresholds: (unchanged)
```

Validator rules: weights sum to 1.0 (ERROR); referenced taxonomy exists (ERROR); every signal has a registered detector declaration (ERROR); every jurisdiction covered by ≥1 enabled adapter (ERROR); every size metric resolvable to `filed`/`derived`-with-available-inputs per jurisdiction — full coverage passes, conditional coverage → WARNING with estimated coverage recorded, none → ERROR; metrics resolvable only as `modelled` must be declared so in the YAML (W3, ERROR otherwise).

### 3.4 Hooks (`.claude/settings.json`)

PreToolUse, per verified current hook semantics (JSON `permissionDecision: "deny"`, holds under permissive modes, `agent_id` distinguishes subagents):

- **Network**: deny `WebFetch`/`WebSearch` and Bash network commands (`curl`/`wget`/`httpx`) to hosts outside the allowlist: `api.company-information.service.gov.uk`, `document-api.company-information.service.gov.uk`, `download.companieshouse.gov.uk`, `stream.companieshouse.gov.uk` (future).
- **Data**: deny `Write`/`Edit` matching `data/**` when `agent_id` is present (subagent), allowing the main-agent-invoked `deal-engine` CLI to write via Bash (C6).
- **Credentials**: deny any tool call whose arguments reference `.env`, `*.pem`, `secrets*`.

Each hook is a small Python script with its own unit test (hooks are code, so they get tests like code). CLAUDE.md documents the containment limitation honestly.

### 3.5 Run logger

Every CLI invocation writes `logs/runs/{run_id}.jsonl`: command, args, git SHA, start/end, duration, per-stage counts (companies fetched, documents cached, figures written, errors), exit status. LLM-call cost fields join in Phase 3 (`total_cost_usd` + `session_id` from the `claude -p` JSON envelope; wall time and exit code captured by the wrapper since the envelope lacks them). `run_id` is a foreign key on `ScreenResult`/`Score` rows from Phase 2 on.

### 3.6 Phase 0 gate (expanded from the brief)

`deal-engine mandate validate mandates/example-lmm-uk.yaml` exits 0 with the recorded WARNING (conditional EBITDA coverage for GB). Each broken fixture is rejected with its *specific* error — including `gb-ie-ebitda.yaml` failing on "no enabled adapter supplies ebitda for jurisdiction IE". Provenance write-raises tests pass. Render-validator tests pass (DoD #5, satisfied in Phase 0 rather than waiting for Phase 3). `pytest` green.

---

## 4. Phase 1 plan

### 4.0 Step zero — verify the live API surface (executed by you, locally)

**Execution split (decision record, 2026-08-01):** the sandbox network
policy is fixed to package managers; Companies House hosts are
permanently unreachable from it. Therefore: the sandbox writes the
adapter, parsers, concept map and tests against committed fixtures; **you
run live fetches locally** and commit cached responses as fixtures; the
200-company ingest gate run happens on your machine via the CLI
(`CH_API_KEY` in your local `.env`), with the run log, coverage report
and sample handed back for the gate review.

Step zero accordingly: `docs/live-api-verification.md` is the numbered
request list — ~25 calls verifying auth, rate-limit headers, advanced
search shape, officer DOB granularity, PSC kinds/statement spellings,
filing-history links, the document-metadata `resources` object, the
302-to-storage redirect (with and without forwarded auth), charge
envelope spellings, and exemptions — plus two saved accounts documents
(one full filer, one small filer) that seed `evals/golden/filings/`.
Adapter coding against live-response reality starts when that report is
back; a `scripts/record_fixtures.py` then systematises fixture capture
with auth stripped.

### 4.1 New files

```
src/deal_engine/adapters/companies_house/
    client.py          # httpx; basic auth (key-as-username); global token bucket ≤500 req/5min;
                       #   429 backoff; manual 302 handling for S3 (no auth header cross-host)
    adapter.py         # implements the Protocol; declares the tiered CapabilityMatrix (GB)
    universe.py        # advanced-search enumeration + SIC wildcard expansion
    concept_map/       # versioned YAML per FRC taxonomy generation (see 4.4) — data, not code
    enums.py           # vendored api-enumerations subsets (account types, categories, PSC kinds)
src/deal_engine/ingest/
    pipeline.py        # per-company state machine, checkpointed in DB → resumable (rate limit
                       #   makes 200 companies ≈ 20–30 min of wall time; interruption is normal)
    cache.py           # content-addressed blob store (C3)
    refresh.py         # incremental: filing-history transaction_id diff → fetch only new
src/deal_engine/parse/
    ixbrl.py           # ixbrlparse wrapper: error harvesting, within-doc dedupe, dimensions
    figures.py         # parsed facts × concept map → FigureObservation rows
src/deal_engine/resolve/
    companies.py       # dedupe on (jurisdiction, company_number); previous names → variants
    persons.py         # officer↔PSC matching: name_elements + DOB month/year; CH officer IDs
evals/golden/filings/  # real cached filings + hand-verified expected figure rows (C7)
tests/                 # adapter (respx-mocked from live transcripts), parser, cache, resolve,
                       #   idempotency (re-ingest → zero new rows), refresh-diff
```

### 4.2 Universe enumeration

`GET /advanced-search/companies` with client-side-expanded 5-digit SIC codes (W8), `company_status=active`. Constraints planned for: `size` ≤ 5,000 per page, ~10,000-result retrieval window per query (slice by `incorporated_from/to` when `hits` reveals overflow); results carry `sic_codes` but **no accounts data**, so size triage needs the company profile call (`accounts.last_accounts.type`: dormant/micro-entity discarded immediately for this mandate — that's most of the register). `/search/companies` (1,000-result cap, no SIC) is for entity resolution only. The free monthly bulk snapshot CSV (has SIC, status, and `Accounts.AccountCategory`, costs zero quota) is the documented scale path; the universe source sits behind an interface so it can swap in without touching the pipeline. For the gate: enumerate → triage → cap at 200 non-dormant, non-micro candidates.

### 4.3 Per-company ingestion

Per company (~8–10 requests): profile, officers, PSC (+statements/exemptions), charges, filing history, then accounts documents for the latest 2 periods where available: filing-history item → `links.document_metadata` → inspect `resources` for `application/xhtml+xml` (presence = parseable iXBRL; absence = scanned PDF) → fetch with Accept header → 302 → S3 without auth header → content-addressed store. `pdf_only` is a recorded SourceDocument status, not an error — the paper tail skews toward exactly the older family companies this mandate hunts, so it must be visible in the coverage report. Raw filing-history rows persist keyed by `transaction_id`; **Events are a deterministic, idempotent projection of them** (charge registered/satisfied, officer appointed/resigned, ARD change, name change, late filing computed from period-end + 9 months vs delivery date) — never independently written, so the Event stream and the refresh diff cannot drift.

### 4.4 Parsing into figures

`ixbrlparse` (v0.11.x, maintained, MIT) wrapped with the discipline its source demands:

- **Concept map is versioned YAML data owned by the CH adapter**, keyed `(taxonomy namespace URI, local name) → canonical concept`, with per-concept expected sign and period type. Seeded from the old-GAAP/FRC synonym pairs (`TurnoverGrossOperatingRevenue`/`TurnoverRevenue`, `ShareholderFunds`/`Equity`, `CashBankInHand`/`CashBankOnHand`, `EmployeesTotal`/`AverageNumberEmployeesDuringPeriod`, `StaffCosts`/`StaffCostsEmployeeBenefitsExpense`, …) — cribbed from `uktrade/stream-read-xbrl`, the UK government's own battle-tested mapping. Roughly 2–4 synonyms per concept across ~7 taxonomy generations; unmapped tags are logged with counts so the map grows from evidence.
- Select periods by **context dates, never context IDs** (vendor-arbitrary strings); resolve namespace prefixes via the document's own namespace table (prefixes are vendor-arbitrary too).
- Harvest `parser.errors` after every parse — nil facts land there silently; a document with parse errors beyond threshold is **quarantined** (recorded, excluded from figures), not partially ingested.
- Within-document duplicate facts (same fact tagged in balance sheet + notes) dedupe by `(concept, context, unit)` with agreement required within filed `decimals`; disagreement is a document-quality flag, not a coin flip.
- **Dimensions**: contexts carry segment dimensions (group vs company-only columns in consolidated accounts; the FRC-era `Creditors` maturity split). Figures carry canonically-ordered dimensions JSON + `dimensions_hash` (in the natural key) + a derived `consolidation` enum. The exact group/company axis QName gets confirmed empirically in step 4.0 and encoded in the concept-map data. For the Creditors split, implement dimension-aware handling with the documented substring fallback, recording which path produced each figure.
- Sign conventions: costs/creditors arrive tagged positive under negated-label presentation; the concept map's expected-sign column normalises at parse time, and raw text + filed decimals are retained on the row.
- Non-GBP filings (legitimate: some UK companies file in EUR/USD) store the filed currency; no silent FX — conversion is a Phase 2 `derived` function.

### 4.5 Golden fixtures (C7 — moved into Phase 1)

`evals/golden/filings/`: 10–15 real filings spanning micro-entity, filleted small, abridged, full, and group accounts across at least 3 taxonomy generations and 3+ filing-software vendors, each with hand-verified expected figure rows. **[AMENDED]** The set must include the deliberately awkward cases: filleted accounts, a restatement, a period-length change (ARD move), and at least one filer with non-standard tagging. This is the adapter's eval set that §2 gates adapter #2 on, and the parser's regression suite. (Phase 3's scorer golden set remains a separate artifact.)

### 4.5a Company-level fixture set (decision record §14)

Figure-level fixtures test extraction; nothing there tests whether a *company* is correctly included or excluded — and under §5's fail-closed rule, misclassification is the likelier error. Proposal: `evals/golden/companies/` — 15–20 hand-labelled companies as recorded API-response fixtures (profile, officers, PSC, statements, exemptions, charges), each with an expected `(ownership_classification, confidence_floor, screening_outcome)` triple, where `screening_outcome` includes `insufficient_data` and `flagged_unclassifiable` as first-class expected values. The roster deliberately covers the ownership edge cases: a sponsor-held topco filing a no-PSC statement (must NOT pass as independent), an EOT trustee company (must NOT classify as PE), a personal-holding-company founder (one recursion hop), a family with differing surnames, a listed subsidiary via exemption, an AIM company (no exemption — caught via PSC), a 50/50 JV, and a genuinely unclassifiable case. The eval reports inclusion/exclusion accuracy separately from figure-extraction accuracy. Built in Phase 1 alongside the classifier's evidence output; extended in Phase 2 when the screening rules consume it.

### 4.6 Phase 1 gate (expanded from the brief)

1. `deal-engine ingest --mandate mandates/example-lmm-uk.yaml --limit 200` completes, checkpointed and resumable, logged to `logs/runs/`.
2. Every persisted figure resolves via `provenance_walk` to a SourceDocument with a retrievable cached original (DoD #2, #3).
3. **Idempotency, redefined per C1:** immediate re-run → zero new rows, zero changed `is_current` flags (DoD #4).
4. Random sample of 10 companies with every figure traced to a filing, for your spot-check against the live register (DoD #6).
5. **Coverage report** (new, W1): of 200 companies — how many with filed P&L vs balance-sheet-only vs `pdf_only` vs quarantined; per-concept fill rates; **[AMENDED] broken down by classification code, measured within the mandate's filtered universe (not register-wide), and produced as a standing output of every ingest run**. This decides what Phase 2's screening design must handle and you should see it before approving Phase 2.
6. Golden fixture eval passes — including the filleted / restatement / period-length-change / non-standard-tagging cases; `pytest` green including render-validator (DoD #5) and idempotency tests.

---

## 5. Canonical schema, concretely

Pydantic models mirror these; constraints shown are enforced in SQLAlchemy DDL. (Abbreviated — nullable/id plumbing omitted where obvious.)

**companies** — `id`, `jurisdiction`, `company_number`, `name`, `name_variants JSON`, `incorporation_date`, `status`, `sic_codes JSON`, `registered_address JSON`, `ownership_classification`, `ownership_confidence`, `ownership_evidence JSON` (PSC record IDs — W7). UNIQUE `(jurisdiction, company_number)`. Officers are **not** embedded (a JSON list would kill the succession query; the Pydantic read-DTO may embed them).

**source_documents** — `id`, `adapter`, `jurisdiction`, `company_id`, `external_document_id`, `transaction_id`, `document_type`, `account_type` (the coverage cliff marker, W1), `filed_date`, `period_start`, `period_end`, `retrieved_at`, `content_type`, `raw_path`, `content_hash`, `parse_status` (`parsed | pdf_only | quarantined`), `parse_error_count`. UNIQUE `(adapter, external_document_id)` (C3). Immutable: no UPDATE path in the repository; hash mismatch on refetch alerts.

**figures** (observations, C1/C2) — `id`, `company_id`, `concept`, `value`, `unit`, `currency`, `period_type` (`instant|duration`), `period_start` (null for instants), `period_end`, `dimensions JSON`, `dimensions_hash`, `consolidation` (`group|company|none`), `decimals`, `raw_text`, `basis` (`filed|derived|modelled|unverified`), `source_document_id`, `source_tag`, `derivation_function`, `derivation_inputs JSON`, `is_current`. UNIQUE `(source_document_id, concept, period_start, period_end, dimensions_hash, unit)`. CHECK: `basis='filed' ⇒ source_document_id NOT NULL ∧ derivation NULL`; `basis='derived' ⇒ derivation NOT NULL`. Pre-flush listener raises on violation (§3.2).

**officers** — `id`, `company_id`, `ch_appointment_id`, `ch_officer_id` (person link), `name`, `role`, `appointed_on`, `resigned_on`, `dob_month`, `dob_year`, `nationality`, `country_of_residence`. UNIQUE `(company_id, ch_appointment_id)`. Person identity via CH officer IDs, never name+DOB alone.

**psc_records** — `id`, `company_id`, `psc_id`, `kind`, `name`, `name_elements JSON`, `natures_of_control JSON` (verbatim enum strings — bands only, never numeric %), `notified_on`, `ceased_on`, `dob_month`, `dob_year`, `identification JSON` (corporate PSCs: legal form, registration number, country — the classifier's raw material). Companion **psc_statements** and **exemptions** tables (W7: a no-PSC statement must be visible to the classifier).

**filings** — raw filing-history rows: `company_id`, `transaction_id` UNIQUE, `category`, `type`, `date`, `description`, `description_values JSON`, `document_id`. Drives refresh diffing and Event projection.

**charges** — `company_id`, `charge_code`, `status`, `created_on`, `delivered_on`, `satisfied_on`, `classification JSON`, `particulars JSON`, `persons_entitled JSON`, `transactions JSON`.

**events** — projection (C6 in §4.3): `company_id`, `event_type` (incl. `restatement`, C1), `event_date`, `transaction_id`/`source_document_id`, `payload JSON`. UNIQUE on the projection key so re-projection is idempotent.

**runs** — `run_id`, `command`, `args JSON`, `git_sha`, `started_at`, `finished_at`, `exit_status`, `counts JSON`, `cost_usd` (Phase 3+).

**screen_results / scores** — as briefed, `run_id` FK; `scores.figure_ids_cited JSON` validated against the figures table on write. (Tables defined in Phase 0; populated in Phases 2–3.)

---

## 6. Answers to the §11 open questions

**iXBRL tag variance.** Bounded and manageable: concept names are fixed per taxonomy generation (~7 generations in the wild, 2–4 synonyms per canonical concept); real variance lives in vendor-arbitrary namespace prefixes and context IDs (never key on them), dimensional tagging style (Creditors maturity, group/company axis), Format 1 vs 2 P&L, and sign/scale usage (ixbrlparse normalises sign/scale into values). Handled by: versioned concept-map YAML seeded from the UK government's own mapping, dimension-aware contexts, golden fixtures across vendors, and unmapped-tag logging so the map grows from evidence. The genuinely hard residue is small-company accounts *omitting* concepts, which is a coverage problem (W1), not a parsing problem.

**Ownership classification from PSC.** Feasible as scored evidence, not as a boolean (W7). Expected precision (to be validated on the 200-company set, since no published benchmark exists): owner-managed via individual-PSC×director match ~85–90%; PE-backed via name-pattern + legal-form + chain-walk + charge corroboration ~90% on control buyouts; UK-listed parents via exemptions >95%. Known failure modes are enumerated in W7; `unclassifiable` is an explicit output and exclusion mandates fail closed.

**SQLite.** Holds comfortably for Phase 1–3 volumes (10⁴–10⁵ companies, 10⁵–10⁶ figure rows) with WAL mode; the pipeline is single-writer by design. Migration triggers, in order of likelihood: a second concurrent writer (dashboard/API), multi-GB database with analytic queries, or a need for real concurrent refresh. Insurance: SQLAlchemy throughout, no SQLite-only SQL, JSON columns kept portable, Alembic from Phase 0 — migration is a config change plus data copy, not a rewrite.

**"Unmarketed".** Cannot be evidenced from public data; the honest claim is the evidence-of-absence formulation (W6), rendered with its dated evidence list and per-figure staleness. This needs a decision from you because it touches the system's §1 commercial claim, not just code.

---

## 7. Decisions needing your approval

> **Decision record 2026-07-31: all twelve APPROVED.** Amendments to 3, 6, 7 are folded into the findings above ([AMENDED] marks). Additional rulings: the `GB` jurisdiction profile maps to all three Companies House registers (England & Wales, Scotland, Northern Ireland), not Great Britain in the geographic sense; the modelled-declaration rule (2) is general, not an EV special case; every signal records the specific observation backing it so profiles show *why*, not conclusions; "name signals after what is observed, not what is inferred" is a standing rule for all future signals; and §5's fail-closed rule is stated in code: **absence of a PSC statement is not evidence of independence**.

1. **Example mandate → `geography: [GB]`**; the `[GB, IE]` variant becomes the Phase 0 gate's deliberately broken fixture (W2).
2. **Drop `enterprise_value`** from the example mandate; validator requires unobservable metrics be declared `modelled` (W3).
3. **Two-stage size screening accepted as a consequence of W1**: filed-P&L EBITDA where available; balance-sheet + employees proxies with explicit `on_insufficient_data` policy elsewhere; coverage report added to the Phase 1 gate.
4. **Signal renames/splits**: `recent_debt_raise` → `new_security_registered` with exclusion filters (W4); succession → `psc_age_threshold` + named no-younger-director heuristic, `require_no_successor` dropped (W5).
5. **Ownership**: merge founder/family into `owner_managed`; classification+confidence+evidence with fail-closed `unclassifiable` handling (W7).
6. **Figure = observation + `is_current` selection**; DoD #4 redefined as "zero new rows, zero flag changes on re-run" (C1).
7. **Provenance**: `source_document_id` required iff `basis=filed`, transitive provenance via `derivation` + `provenance_walk` (C2).
8. **Cache keyed on adapter document identity; `content_hash` demoted to integrity field**; content-addressed blob store (C3).
9. **`{fig:ID}` marker-substitution rendering** + typed numeral whitelist; validator is LLM-independent and lands in Phase 0 (C4).
10. **Reword the §1 commercial claim** to the evidence-of-absence formulation (W6).
11. **Adapter golden fixtures move to Phase 1** (C7).
12. **Capability matrix tiers + ERROR/WARNING validation severities** with static Phase 0 declarations (W1, C5).

Silence on any of these blocks the corresponding build step; per §0 I will not work around them.

## 8. Environment prerequisites (revised 2026-08-01)

- **The sandbox network policy is fixed to package managers** (personal
  plan): Companies House hosts are permanently unreachable from the
  sandbox and cannot be allowlisted. This is design input, not a defect —
  Phase 1 splits execution: sandbox = code, parsers, tests over committed
  fixtures; your machine = live fetches (per
  `docs/live-api-verification.md`), fixture capture, and the ingest gate
  run with `CH_API_KEY` in your local `.env` (never committed).
- **PyPI** (`pypi.org`, `files.pythonhosted.org`) is intended to be
  reachable and is required for the Phase 0 gate. As of 2026-08-01 06:01
  UTC both this session and a freshly spawned remote container still
  receive `403 x-deny-reason: host_not_allowed` for pypi.org — the
  allowlist change has not reached this environment. Fallbacks: a fresh
  session on this branch after the policy lands, or run
  `pip install -e ".[dev]" && pytest` locally and paste the output; the
  gate is identical either way.
- **A Companies House API key** (free, registered at the Developer Hub) supplied as `CH_API_KEY`. REST and streaming keys are distinct types; only REST is needed for Phase 1.
- One human read of the CH API terms page at key registration (the page itself was unreachable from here). Caching/storing register data and filed documents is permitted — CH publishes its own bulk products for exactly that — with UK GDPR responsibility for officer/PSC personal data noted in CLAUDE.md.

## 9. Phase 2 queue (approved at the Phase 1 gate review, 2026-08-02)

Recorded from the gate review of ingest runs 30696915083 (baseline) and
30743865139 (post-fix validation) so nothing lives only in conversation
history. Approved for Phase 2; none of it is built yet.

1. **Plausibility layer** (design approved as specified). A
   post-persistence pass of named, tested rules writes
   `plausibility_flags` per figure — annotations, never corrections;
   figures stay verbatim observations. Rules: `unit_concept_mismatch`
   (count concept with a currency unit — observed: Aral Estates
   employees tagged `iso4217:GBP`), `suspicious_scale_attribute` (any
   `scale` on a pure-unit count — observed: Cultura Technologies
   employees filed with `scale="-2"`, 39 → 0.39, spec-correct and
   absurd), `series_discontinuity` (~100× jump vs the company's own
   history, restatement-aware), `cross_filing_disagreement` (same
   concept/period differing across filings). Consumption differs by
   class: the first two exclude the figure from proxy computations
   (dimension records `insufficient_data` unless a clean observation
   exists; composites renormalise); `series_discontinuity` stays IN
   screening and carries the flag into the screen result's evidence — a
   real step change (acquisition, disposal) is signal, not noise. Every
   flagged figure always renders in profiles, flag alongside;
   suppression is never an option.

2. **New invariant — historical zero-yield documents.** Coverage facts
   describe the latest filing, so a machine-readable document that
   yields zero mapped figures needs its own signal, independent of
   whether the company currently parses. Found the hard way: 3
   companies that switched filing software mid-history had their
   Digita-era documents silently yielding nothing while their current
   documents parsed fine — no `parse_failed` fact, no defect bucket,
   invisible to every existing metric, discovered only by diffing two
   runs' figure counts (+80 of the +562 delta). Partial detection
   already exists: `by_production_software.zero_figure` counts these at
   product level across ALL machine-readable documents. Missing: the
   per-company signal (document-level yield recorded on the source
   document row exists via figure counts; the coverage report should
   surface companies carrying any zero-yield machine-readable document
   as their own line, analogous to `parse_failed`).

3. **Minor:** serialize `by_production_software` sorted by document
   count descending — thin-sample products (n≤3) are the statistically
   invisible risk and belong visibly grouped, not alphabetized.

## 10. Scale phase — bulk-first ingest (designed 2026-08-10, approval pending)

200 ingested companies is a gate sample; the product number is the
mandate universe (~906k). The API rate limit (600 req/5 min, ~13 calls
per company) caps API-only ingestion at ~10k companies/day — three
months to the universe. The sanctioned route is Companies House's free
bulk products (download.companieshouse.gov.uk, already allowlisted;
published precisely so consumers stop polling the API):

1. **Basic company data** (monthly, ~5.4M companies): replaces universe
   enumeration and registration facts — zero API calls.
2. **Accounts Monthly Data** (every iXBRL accounts filing, monthly
   ZIPs): the existing parser, concept map and per-product telemetry
   apply unchanged. Twelve months ≈ figures for ~500-600k mandate
   companies at the observed 62% machine-readable rate; the remainder
   are honestly unparseable_format → signal mode.
3. **PSC snapshot** (daily): beneficial owners and birth months for the
   whole register.

The API demotes to **enrichment**: officers, charges, and
filing-history transaction ids (the exact-document trace links),
spent on companies that survive screens or get opened — ~10k/day
budget, prioritised. Un-enriched companies trace to their
filing-history page with a state saying so.

Interim accumulation (live now): the ingest workflow seeds each run
from a rolling `data-store` release (engine.db.gz + checkpoint), runs
nightly at limit 800, and uploads the grown store back — the checkpoint
skips stored companies before any API call, and idempotent re-ingest
makes the accumulation safe by construction. The store stays out of
git history; per-run reports and a capped (400-company, most recently
filed) frontend dataset stay committed.

Frontend at scale: the inline-JSON model dies past a few thousand
companies. Planned replacement: range-request SQLite over static
hosting (browser fetches only the DB pages a query touches — no
server), so the three-way count computes over the actual universe.
All invariants (provenance, absence states, staleness, no LLM
figures) carry over unchanged; bulk documents still provide sha-256,
filed dates and verbatim tags.

Not proposed: multiple API keys to evade the rate limit.
