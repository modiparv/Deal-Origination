/* Demo surface renderers: SCREEN (list), COMPANY (profile), TRACE.
 *
 * Read-only by construction: everything rendered is a verbatim field or
 * a mechanical aggregate of the exported run dataset (window.__DEMO__),
 * which is itself exported from the committed engine.db of a logged
 * ingest run. Nothing financial is computed here — absent derived
 * metrics render as absence states, never as blanks or approximations.
 */
(function () {
  "use strict";

  const DATA = window.__DEMO__;
  const $ = (sel) => document.querySelector(sel);

  const esc = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[c]);

  // ----- absence / process states -------------------------------------
  // Five distinct absence states plus parse_failed; each carries a text
  // code and an explanation. Never a bare em-dash.
  const STATES = {
    filed_without_concept: "The filed accounts regime legitimately omits this concept (e.g. micro-entity accounts carry no P&L).",
    unparseable_format: "A filing exists but the registry offers no machine-readable rendition (PDF only).",
    parse_failed: "A machine-readable document exists but failed to parse — a system defect, tracked and fixed, never presented as a data limitation.",
    not_reached: "Not yet computed: screening scores, flags and derived metrics are Phase 2 and have not run. No value exists to show.",
    not_captured: "Outside the fetched window — ingest retrieves the three most recent account documents per company; older periods appear only where those documents carry comparatives.",
    skipped_mode: "Rubric dimension skipped: it requires financial mode and this company screens in signal mode. Recorded, and composites over partial dimensions are renormalised.",
    not_observable: "Not observable from public registry data for this company; the rubric records the gap rather than guessing.",
  };
  const state = (code, extra) =>
    `<span class="state st-${esc(code)}" title="${esc(extra || STATES[code] || "")}">${esc(code)}</span>`;

  // ----- formatting ---------------------------------------------------
  const nf = new Intl.NumberFormat("en-GB");
  function money(fig) {
    const cur = fig.currency || (fig.unit === "GBP" ? "GBP" : null);
    const sym = cur === "GBP" ? "£" : cur ? cur + " " : "";
    const v = Number(fig.value);
    const neg = v < 0;
    const abs = Math.abs(v);
    const body = Number.isInteger(v) ? nf.format(abs) : String(abs);
    return (neg ? "−" : "") + sym + body;
  }
  function plain(fig) {
    const v = Number(fig.value);
    return Number.isInteger(v) ? nf.format(v) : String(fig.value);
  }
  const isCount = (f) => f.concept === "average_employees";
  const figDisplay = (f) => (isCount(f) ? plain(f) : money(f));

  function ageInfo(dateStr) {
    if (!dateStr) return null;
    const then = new Date(dateStr);
    const months = Math.max(0, Math.round((Date.now() - then.getTime()) / 2629800000));
    const y = Math.floor(months / 12), m = months % 12;
    const label = y ? `${y}y ${m}m` : `${m}m`;
    return { months, label, stale: months > 24 };
  }
  const ageSpan = (dateStr) => {
    const a = ageInfo(dateStr);
    if (!a) return state("not_captured");
    return `<span class="age${a.stale ? " stale" : ""}">${esc(a.label)}<span class="unit"> old${a.stale ? " · stale" : ""}</span></span>`;
  };

  const basisBadge = (f) => `<span class="basis" title="basis: ${esc(f.basis)} — stored verbatim from the source document">${esc(f.basis)}</span>`;

  // ----- registry links -----------------------------------------------
  const CH = "https://find-and-update.company-information.service.gov.uk";
  const companyUrl = (reg) => `${CH}/company/${encodeURIComponent(reg)}`;
  const filingHistoryUrl = (reg) => `${companyUrl(reg)}/filing-history`;
  const documentUrl = (reg, txn) =>
    txn ? `${filingHistoryUrl(reg)}/${encodeURIComponent(txn)}/document?format=xhtml` : null;

  // ----- data access --------------------------------------------------
  const companiesById = Object.fromEntries(DATA.companies.map((c) => [c.id, c]));
  const figuresOf = (cid) => (DATA.figures_by_company[cid] || []).map((id) => DATA.figures[id]);
  const coverageOf = (cid) => DATA.coverage[cid] || [];
  const doc = (id) => DATA.documents[id];

  const traceHref = (figId) => `trace.html?fig=${encodeURIComponent(figId)}`;
  const companyHref = (cid) => `company.html?id=${encodeURIComponent(cid)}`;

  function figCellHtml(f) {
    return `<a href="${traceHref(f.id)}" title="trace to source filing">${esc(figDisplay(f))}</a>${basisBadge(f)}`;
  }

  function coverageState(cid, concept) {
    const fact = coverageOf(cid).find((x) => x.concept === concept);
    if (!fact) return state("not_captured");
    return state(fact.status, fact.detail || undefined);
  }

  function runFooter() {
    const el = $("#run-footer");
    if (!el) return;
    el.innerHTML =
      `Dataset: ingest run <code>${esc(DATA.run.run_id || "?")}</code>` +
      (DATA.run.git_sha ? ` at <code>${esc(String(DATA.run.git_sha).slice(0, 9))}</code>` : "") +
      ` · every figure is a filed observation citing its source document, period end and filed date;` +
      ` nothing on this surface is computed by a language model. Filed registry data is 9–21 months` +
      ` stale by construction; each figure shows its own age. ` +
      `<a href="../index.html">operations viewer</a>`;
  }

  function legendHtml(codes) {
    return (
      `<dl class="legend">` +
      codes.map((c) => `<dt>${state(c)}</dt><dd>${esc(STATES[c])}</dd>`).join("") +
      `</dl>`
    );
  }

  // ====================================================================
  // SCREEN — list
  // ====================================================================
  function renderList() {
    const root = $("#list-root");
    if (!DATA.companies.length) {
      root.innerHTML = `<div class="empty"><strong>No companies in the store.</strong>
        This surface renders only verified ingest output; run an ingest and redeploy.</div>`;
      return;
    }

    const sics = [...new Set(DATA.companies.flatMap((c) => c.sic))].sort();
    $("#f-sic").innerHTML =
      `<option value="">all sectors</option>` +
      sics.map((s) => `<option value="${esc(s)}">${esc(s)}</option>`).join("");

    const sortState = { key: "name", dir: 1 };

    const val = (c, key) => {
      switch (key) {
        case "name": return c.name;
        case "mode": return c.mode;
        case "revenue": { const f = c.latest_revenue_fig && DATA.figures[c.latest_revenue_fig]; return f ? Number(f.value) : -Infinity; }
        case "net_assets": { const f = c.latest_net_assets_fig && DATA.figures[c.latest_net_assets_fig]; return f ? Number(f.value) : -Infinity; }
        case "employees": { const f = c.latest_employees_fig && DATA.figures[c.latest_employees_fig]; return f ? Number(f.value) : -Infinity; }
        case "fresh": return c.freshest_period || "";
        case "coverage": return (c.coverage.statuses.available || 0);
        default: return "";
      }
    };

    function draw() {
      const sic = $("#f-sic").value, mode = $("#f-mode").value,
        q = $("#f-q").value.trim().toLowerCase();
      let rows = DATA.companies.filter(
        (c) =>
          (!sic || c.sic.includes(sic)) &&
          (!mode || c.mode === mode) &&
          (!q || c.name.toLowerCase().includes(q) || c.registration_id.toLowerCase().includes(q))
      );
      rows = rows.slice().sort((a, b) => {
        const A = val(a, sortState.key), B = val(b, sortState.key);
        return (A < B ? -1 : A > B ? 1 : 0) * sortState.dir;
      });
      $("#f-count").textContent = `${rows.length} of ${DATA.companies.length} companies`;

      const arrow = (k) => (sortState.key === k ? `<span class="dir">${sortState.dir > 0 ? "▲" : "▼"}</span>` : "");
      const th = (k, label, cls = "") =>
        `<th class="sortable ${cls}" data-key="${k}">${label} ${arrow(k)}</th>`;

      const body = rows.map((c) => {
        const rev = c.latest_revenue_fig ? DATA.figures[c.latest_revenue_fig] : null;
        const na = c.latest_net_assets_fig ? DATA.figures[c.latest_net_assets_fig] : null;
        const emp = c.latest_employees_fig ? DATA.figures[c.latest_employees_fig] : null;
        const avail = c.coverage.statuses.available || 0;
        return `<tr>
          <td><a href="${companyHref(c.id)}">${esc(c.name)}</a><br>
              <span style="color:var(--muted);font-size:11px;font-family:var(--mono)">${esc(c.registration_id)}</span></td>
          <td>${c.sic.map(esc).join(", ")}</td>
          <td><span class="mode ${esc(c.mode)}">${esc(c.mode)}</span></td>
          <td class="num">${rev ? figCellHtml(rev) : coverageState(c.id, "revenue")}</td>
          <td class="num">${state("not_reached")}</td>
          <td class="num">${na ? figCellHtml(na) : coverageState(c.id, "net_assets")}</td>
          <td class="num">${emp ? figCellHtml(emp) : coverageState(c.id, "average_employees")}</td>
          <td>${c.freshest_period ? `${esc(c.freshest_period)} · ${ageSpan(c.freshest_period)}` : state("unparseable_format", "no machine-readable figures for this company")}</td>
          <td class="num">${avail}/21</td>
          <td class="num">${state("not_reached")}</td>
        </tr>`;
      }).join("");

      $("#list-table").innerHTML =
        `<thead><tr>
           ${th("name", "Company")}${th("", "SIC")}${th("mode", "Mode")}
           ${th("revenue", "Latest revenue", "num")}<th class="num">Margin</th>
           ${th("net_assets", "Net assets", "num")}${th("employees", "Employees", "num")}
           ${th("fresh", "Freshest period")}${th("coverage", "Coverage", "num")}
           <th class="num">Score / flags</th>
         </tr></thead><tbody>${body}</tbody>`;

      document.querySelectorAll("#list-table th.sortable").forEach((el) =>
        el.addEventListener("click", () => {
          const k = el.dataset.key;
          if (!k) return;
          if (sortState.key === k) sortState.dir *= -1;
          else { sortState.key = k; sortState.dir = 1; }
          draw();
        })
      );
    }

    ["#f-sic", "#f-mode"].forEach((s) => $(s).addEventListener("change", draw));
    $("#f-q").addEventListener("input", draw);
    $("#list-legend").innerHTML = legendHtml(Object.keys(STATES));
    draw();
  }

  // ====================================================================
  // COMPANY — profile
  // ====================================================================
  const PL_CONCEPTS = ["revenue", "gross_profit", "operating_profit", "profit_before_tax",
    "profit_for_period", "staff_costs", "depreciation_amortisation", "tax_charge"];
  const BS_CONCEPTS = ["fixed_assets", "current_assets", "debtors", "cash",
    "creditors_within_one_year", "creditors_after_one_year", "net_current_assets",
    "total_assets_less_current_liabilities", "net_assets", "equity", "share_capital",
    "retained_earnings"];
  const OTHER_CONCEPTS = ["average_employees"];

  function renderCompany() {
    const cid = new URLSearchParams(location.search).get("id");
    const c = companiesById[cid];
    const root = $("#profile-root");
    if (!c) {
      root.innerHTML = `<div class="empty"><strong>Unknown company.</strong>
        No company with id <code>${esc(cid || "(none)")}</code> exists in this run's store.
        <a href="index.html">Back to the list.</a></div>`;
      return;
    }
    document.title = `${c.name} — profile`;
    $("#company-name").textContent = c.name;
    $("#crumb").innerHTML = `<a href="index.html">screen results</a> / ${esc(c.name)}`;

    const figs = figuresOf(cid).filter((f) => f.is_current && !Object.keys(f.dimensions || {}).length);
    const periods = [...new Set(figs.map((f) => f.period_end).filter(Boolean))].sort().reverse().slice(0, 6);
    const covPeriod = c.coverage.period_end;

    const cell = (concept, period) => {
      const f = figs.find((x) => x.concept === concept && x.period_end === period);
      if (f) return figCellHtml(f);
      if (period === covPeriod) {
        const fact = coverageOf(cid).find((x) => x.concept === concept);
        if (fact && fact.status !== "available") return state(fact.status, fact.detail || undefined);
      }
      return state("not_captured");
    };

    const matrixRows = (concepts) => concepts.map((k) =>
      `<tr><td>${esc(k)}</td>${periods.map((p) => `<td class="num">${cell(k, p)}</td>`).join("")}</tr>`
    ).join("");

    const fresh = c.freshest_period;
    const freshDoc = (() => {
      const withDates = figs
        .filter((f) => f.period_end === fresh && f.source_document_id)
        .map((f) => doc(f.source_document_id)).filter(Boolean);
      return withDates[0] || null;
    })();

    const avail = c.coverage.statuses.available || 0;

    root.innerHTML = `
      <div class="fact-strip">
        <span><span class="k">registration</span><span class="v"><a href="${companyUrl(c.registration_id)}">${esc(c.registration_id)}</a> (${esc(c.jurisdiction)})</span></span>
        <span><span class="k">status</span><span class="v">${esc(c.status || "unknown")}</span></span>
        <span><span class="k">incorporated</span><span class="v">${esc(c.incorporated || "unknown")}</span></span>
        <span><span class="k">SIC (sic_2007)</span><span class="v">${c.sic.map(esc).join(", ")}</span></span>
        <span><span class="k">mode</span><span class="v"><span class="mode ${esc(c.mode)}">${esc(c.mode)}</span></span></span>
        <span><span class="k">concept coverage</span><span class="v">${avail}/21 at ${esc(covPeriod || "?")}</span></span>
      </div>
      ${fresh
        ? `<p class="staleness-callout">Freshest machine-readable figures: period end <strong>${esc(fresh)}</strong>
           (${ageSpan(fresh)}${freshDoc ? `, filed ${esc(freshDoc.filed_date)}` : ""}).
           Every figure below carries its own period and links to its source filing.</p>`
        : `<p class="staleness-callout">No machine-readable figures exist for this company —
           its filings have no iXBRL rendition ${state("unparseable_format")}. Screening for this
           company proceeds in signal mode on observable behaviour only.</p>`}

      <section>
        <h2>Financial trajectory</h2>
        <p class="note">Filed observations only, current per deterministic supersession (latest filed date wins);
        click any value to trace it to the filing. Derived metrics (margins, growth) are Phase 2 and
        render ${state("not_reached")} until the derive layer exists.</p>
        ${periods.length ? `<table class="matrix">
          <thead><tr><th>concept</th>${periods.map((p) => `<th class="num">${esc(p)}<br>${ageSpan(p)}</th>`).join("")}</tr></thead>
          <tbody>
            <tr><th colspan="${periods.length + 1}">income statement</th></tr>${matrixRows(PL_CONCEPTS)}
            <tr><th colspan="${periods.length + 1}">balance sheet</th></tr>${matrixRows(BS_CONCEPTS)}
            <tr><th colspan="${periods.length + 1}">other</th></tr>${matrixRows(OTHER_CONCEPTS)}
          </tbody></table>`
        : `<div class="empty">No figures to tabulate — see the coverage panel below for the recorded reasons.</div>`}
      </section>

      <section>
        <h2>Ownership &amp; succession</h2>
        <p class="note">Ownership classification is Phase 2 and fail-closed:
        ${c.ownership_classification ? esc(c.ownership_classification) : state("not_reached", "classification module not yet built")} —
        absence of a beneficial-ownership statement is <em>not</em> evidence of independence.
        Succession signals (director tenure/age detectors) are Phase 2: ${state("not_reached")}.</p>
        ${c.beneficial_owners.length ? `<table>
          <thead><tr><th>beneficial owner on record</th><th>kind</th><th>natures of control</th><th>notified</th><th>ceased</th></tr></thead>
          <tbody>${c.beneficial_owners.map((b) => `<tr>
            <td>${esc(b.name)}</td><td>${esc(b.kind || "")}</td>
            <td>${(b.natures || []).map(esc).join("<br>") || state("not_observable", "no control natures recorded")}</td>
            <td>${esc(b.notified_on || "")}</td><td>${esc(b.ceased_on || "— active")}</td></tr>`).join("")}
          </tbody></table>`
        : `<p class="note">No beneficial-owner records. ${c.ownership_statements.length ? "" : "No ownership statements either — this is a recorded gap, not evidence of anything."}</p>`}
        ${c.ownership_statements.length ? `<p class="note">Ownership statements on record:</p><table>
          <thead><tr><th>statement</th><th>notified</th><th>ceased</th></tr></thead>
          <tbody>${c.ownership_statements.map((s) => `<tr><td><code>${esc(s.statement)}</code></td>
            <td>${esc(s.notified_on || "")}</td><td>${esc(s.ceased_on || "— active")}</td></tr>`).join("")}</tbody></table>` : ""}
        <p class="note">Officers on record: ${c.counts.officers_active} active of ${c.counts.officers_total} total ·
        exemptions: ${c.counts.exemptions} · filings: ${c.counts.filings} · source documents: ${c.counts.documents}</p>
      </section>

      <section>
        <h2>Risk flags</h2>
        <p class="note">Plausibility flags (unit mismatches, suspicious scale attributes, series discontinuities)
        are Phase 2: ${state("not_reached")}. Security interests below are filed registry records.</p>
        ${Object.keys(c.charges).length ? `<p class="note">Charges: ${Object.entries(c.charges).map(([k, v]) => `${esc(k)}: ${v}`).join(" · ")}</p>
          <table><thead><tr><th>created</th><th>status</th><th>satisfied</th><th>classification</th></tr></thead>
          <tbody>${c.recent_charges.map((r) => `<tr><td>${esc(r.created_on || "")}</td><td>${esc(r.status || "")}</td>
            <td>${esc(r.satisfied_on || "—")}</td><td>${esc(r.classification && (r.classification.description || r.classification.type) || "")}</td></tr>`).join("")}</tbody></table>`
        : `<p class="note">No security interests on record for this company.</p>`}
      </section>

      <section>
        <h2>Concept coverage at ${esc(covPeriod || "latest period")}</h2>
        <p class="note">What fraction of the 21 canonical concepts was observable, and the recorded
        cause for each absence. This panel is the honesty statement for the profile above.</p>
        <table><thead><tr><th>concept</th><th>status</th><th>recorded cause</th></tr></thead>
        <tbody>${coverageOf(cid).map((f) => `<tr><td>${esc(f.concept)}</td>
          <td>${f.status === "available" ? `<span class="state" style="border-color:#0ca30c">available</span>` : state(f.status)}</td>
          <td style="color:var(--ink-2)">${esc(f.detail || "")}</td></tr>`).join("")}</tbody></table>
      </section>

      <section><h2>State vocabulary</h2>${legendHtml(Object.keys(STATES))}</section>`;
  }

  // ====================================================================
  // TRACE — provenance
  // ====================================================================
  function renderTrace() {
    const figId = new URLSearchParams(location.search).get("fig");
    const f = DATA.figures[figId];
    const root = $("#trace-root");
    if (!f) {
      root.innerHTML = `<div class="empty"><strong>Unknown figure.</strong>
        No figure with id <code>${esc(figId || "(none)")}</code> exists in this run's store.
        <a href="index.html">Back to the list.</a></div>`;
      return;
    }
    const c = companiesById[f.company_id];
    const d = f.source_document_id ? doc(f.source_document_id) : null;
    document.title = `${f.concept} — trace`;
    $("#crumb").innerHTML =
      `<a href="index.html">screen results</a> / <a href="${companyHref(c.id)}">${esc(c.name)}</a> / ${esc(f.concept)}`;

    const dims = Object.entries(f.dimensions || {});
    const periodLabel = f.period_start ? `${f.period_start} → ${f.period_end}` : `at ${f.period_end}`;

    // Observation history: every stored observation of the same
    // (company, concept, period, dimensions) — supersession made visible.
    const dimsKey = JSON.stringify(f.dimensions || {});
    const history = figuresOf(f.company_id)
      .filter((x) => x.concept === f.concept && x.period_end === f.period_end &&
                     JSON.stringify(x.dimensions || {}) === dimsKey)
      .map((x) => ({ fig: x, d: x.source_document_id ? doc(x.source_document_id) : null }))
      .sort((a, b) => ((b.d && b.d.filed_date) || "").localeCompare((a.d && a.d.filed_date) || ""));

    root.innerHTML = `
      <div class="value-block">
        <div class="figure-value">${esc(figDisplay(f))}${basisBadge(f)}</div>
        <div class="figure-meta">${esc(f.concept)} · ${esc(periodLabel)} ·
          ${f.is_current ? "current observation" : "<strong>superseded</strong> — a later filing restates this period (see observation history)"}
          · unit <code>${esc(f.unit || "unspecified")}</code>
          ${dims.length ? `· dimensions: ${dims.map(([k, v]) => `<code>${esc(k)}=${esc(v)}</code>`).join(" ")}` : ""}
        </div>
      </div>

      <ol class="chain">
        <li><span class="step">FIGURE</span>
          <div class="kv"><span class="k">figure id</span><span class="v">${esc(f.id)}</span></div>
          <div class="kv"><span class="k">basis</span><span class="v">${esc(f.basis)}</span></div>
          <div class="kv"><span class="k">raw text as filed</span><span class="v">${esc(f.raw_text)}</span></div>
          ${f.decimals != null ? `<div class="kv"><span class="k">decimals attribute</span><span class="v">${esc(f.decimals)}</span></div>` : ""}
        </li>
        <li><span class="step">TAG</span>
          <div class="kv"><span class="k">source tag</span><span class="v">${esc(f.source_tag)}</span></div>
          <div class="kv"><span class="k">read as</span><span class="v plain">inline-XBRL fact, value taken verbatim — no transformation beyond the document's own scale/sign attributes</span></div>
        </li>
        ${d ? `<li><span class="step">DOCUMENT</span>
          <div class="kv"><span class="k">accounts regime</span><span class="v plain">${esc(d.account_type || "unknown")}</span></div>
          <div class="kv"><span class="k">content type</span><span class="v">${esc(d.content_type || "")}</span></div>
          <div class="kv"><span class="k">produced by</span><span class="v plain">${esc(d.production_software || "not declared in filing")}</span></div>
          <div class="kv"><span class="k">sha-256</span><span class="v" title="${esc(d.content_hash || "")}">${esc((d.content_hash || "").slice(0, 20))}…</span></div>
          <div class="kv"><span class="k">retrieved</span><span class="v plain">${esc((d.retrieved_at || "").slice(0, 19))}Z</span></div>
        </li>
        <li><span class="step">FILING</span>
          <div class="kv"><span class="k">filed date</span><span class="v plain"><strong>${esc(d.filed_date || "unknown")}</strong> · period end ${esc(d.period_end || f.period_end || "?")} · ${ageSpan(f.period_end)}</span></div>
          <div class="kv"><span class="k">registry transaction</span><span class="v">${esc(d.transaction_id || "unknown")}</span></div>
        </li>
        <li><span class="step">REGISTRY</span>
          <div class="kv registry-links">
            ${documentUrl(c.registration_id, d.transaction_id)
              ? `<a href="${documentUrl(c.registration_id, d.transaction_id)}" target="_blank" rel="noopener">Open this filing (iXBRL) ↗</a>` : ""}
            <a href="${filingHistoryUrl(c.registration_id)}" target="_blank" rel="noopener">Filing history ↗</a>
            <a href="${companyUrl(c.registration_id)}" target="_blank" rel="noopener">Register entry ↗</a>
          </div>
        </li>` : `<li><span class="step">DOCUMENT</span>
          <div class="kv"><span class="k">source document</span><span class="v plain">none recorded — this violates the provenance invariant for filed figures and would fail persistence; report if seen.</span></div></li>`}
      </ol>

      <section>
        <h2>Derivation</h2>
        ${f.derivation_function
          ? `<div class="kv"><span class="k">function</span><span class="v">${esc(f.derivation_function)}</span></div>
             <p class="note">Inputs:</p><ul>
             ${(f.derivation_inputs || []).map((id) => {
               const inp = DATA.figures[id];
               return `<li>${inp ? `<a href="${traceHref(id)}">${esc(inp.concept)} ${esc(figDisplay(inp))} (${esc(inp.period_end)})</a>` : `<code>${esc(id)}</code> (not in export)`}</li>`;
             }).join("")}</ul>`
          : `<div class="derivation-note">Filed observation — no computation was performed.
             The value above is the tagged fact exactly as filed. A derived figure (margin, growth,
             ratio) would show its named, tested function here and walk back through every input
             figure to its own source filing. No language model touches any figure at any point.</div>`}
      </section>

      <section>
        <h2>Observation history for this concept and period</h2>
        <p class="note">Figures are observations: the same (company, concept, period) from different
        filings coexists, and the latest filed date wins the <code>current</code> flag. Restatements
        stay on the record.</p>
        <table><thead><tr><th>value</th><th>filed date</th><th>regime</th><th>current</th><th></th></tr></thead>
        <tbody>${history.map((h) => `<tr>
          <td class="num">${esc(figDisplay(h.fig))}</td>
          <td>${esc((h.d && h.d.filed_date) || "?")}</td>
          <td>${esc((h.d && h.d.account_type) || "")}</td>
          <td>${h.fig.is_current ? "yes" : "no"}</td>
          <td>${h.fig.id === f.id ? "← this figure" : `<a href="${traceHref(h.fig.id)}">trace</a>`}</td></tr>`).join("")}
        </tbody></table>
      </section>`;
  }

  // ----- dispatch -----------------------------------------------------
  runFooter();
  const page = document.body.dataset.page;
  if (page === "list") renderList();
  else if (page === "company") renderCompany();
  else if (page === "trace") renderTrace();
})();
