/* COMPANY — deep dive over one company's full record (its bucket shard).
 * Filed observations only; every value links to its provenance trace;
 * derived figures render not_reached until the Phase 2 derive layer
 * exists — nothing is approximated in the meantime.
 */
(async function () {
  "use strict";
  const D = window.DOE;
  const { $, $$, esc, nf, state } = D;
  const root = $("#company-root");
  const cid = new URLSearchParams(location.search).get("id") || "";
  D.shell({ title: "Company", crumb: `<a href="screen.html">screen</a>` });
  if (!D.SITE.store_present) { D.emptyStore(root); return; }

  let ix, rec;
  try { [ix, rec] = await Promise.all([D.data.index(), D.data.company(cid)]); }
  catch (e) { D.loadError(root, e); return; }
  if (!rec) {
    root.innerHTML = `<div class="empty"><strong>Unknown company</strong> <code>${esc(cid)}</code>. <a href="screen.html">Back to the screen.</a></div>`;
    return;
  }
  const c = rec.company;
  const row = ix.byId[cid] || {};
  document.title = `${c.name} — company`;
  $("#page-title").textContent = c.name;
  $("#crumb").innerHTML = `<a href="screen.html">screen</a> / ${esc(c.name)} <span class="co-reg">${esc(c.registration_id)}</span>`;

  const figById = Object.fromEntries(rec.figures.map((f) => [f.id, f]));
  const docById = Object.fromEntries(rec.documents.map((d) => [d.id, d]));
  const doc = (id) => (id ? docById[id] : null);
  const figCell = (f) => `<a href="${D.traceHref(f.id, cid)}" title="period end ${esc(f.period_end)}${doc(f.source_document_id) ? " · filed " + esc(doc(f.source_document_id).filed_date) : ""} — trace to source filing">${esc(D.figDisplay(f))}</a>${D.basisBadge(f)}`;
  const factFor = (concept) => rec.coverage.find((x) => x.concept === concept);
  const coverageState = (concept) => { const f = factFor(concept); return f ? state(f.status, f.detail || undefined) : state("not_captured"); };

  const current = rec.figures.filter((f) => f.is_current && !Object.keys(f.dimensions || {}).length);
  const latest = (concept) => current.filter((f) => f.concept === concept).sort((a, b) => String(b.period_end).localeCompare(String(a.period_end)))[0] || null;
  const rev = latest("revenue"), na = latest("net_assets") || latest("equity"), emp = latest("average_employees");
  const periodsAll = [...new Set(current.map((f) => f.period_end).filter(Boolean))].sort();
  const periods = periodsAll.slice().reverse().slice(0, 6);
  const covPeriod = row.coverage && row.coverage.period_end;
  const fresh = periodsAll.length ? periodsAll[periodsAll.length - 1] : null;
  const oa = D.ownerAge(row);
  const a = c.address || {};

  const cell = (concept, period) => {
    const f = current.find((x) => x.concept === concept && x.period_end === period);
    if (f) return figCell(f);
    if (period === covPeriod) {
      const fact = factFor(concept);
      if (fact && fact.status !== "available") return state(fact.status, fact.detail || undefined);
    }
    return state("not_captured");
  };
  const trend = (concept) => {
    const pts = periodsAll.map((p) => current.find((x) => x.concept === concept && x.period_end === p))
      .filter(Boolean).map((f) => ({ x: f.period_end, y: f.value, label: D.figDisplay(f) }));
    return pts.length >= 2 ? D.sparkline(pts) : `<span class="quiet" title="fewer than two filed periods">·</span>`;
  };
  const PL = ["revenue", "gross_profit", "operating_profit", "profit_before_tax", "profit_for_period", "staff_costs", "depreciation_amortisation", "tax_charge"];
  const BS = ["fixed_assets", "current_assets", "debtors", "cash", "creditors_within_one_year", "creditors_after_one_year", "net_current_assets", "total_assets_less_current_liabilities", "net_assets", "equity", "share_capital", "retained_earnings"];
  const matrixRows = (ks) => ks.map((k) =>
    `<tr><td>${esc(k)}</td>${periods.map((p) => `<td class="num">${cell(k, p)}</td>`).join("")}<td class="trend">${trend(k)}</td></tr>`).join("");

  // Succession read — stated as observations, never inference
  const bos = rec.beneficial_owners, offs = rec.officers;
  const activeBOs = bos.filter((b) => !b.ceased_on);
  const activeOff = offs.filter((o) => !o.resigned_on);
  const youngest = activeOff.filter((o) => o.dob_year).sort((x, y) => y.dob_year - x.dob_year)[0];
  const recentAppt = activeOff.filter((o) => o.appointed_on && o.appointed_on >= `${D.THIS_YEAR - 5}-01-01`);
  const singleBO = activeBOs.length === 1 && (activeBOs[0].control_natures || []).some((n) => String(n).includes("75-to-100"));
  const obs = D.observations(row);

  const peers = ix.companies
    .filter((p) => p.id !== cid && D.divisionsOf(p.sic).some((d) => D.divisionsOf(c.sic).includes(d)))
    .sort((x, y) => {
      const ref = na ? Number(na.value) : 0;
      const dx = x.latest.net_assets ? Math.abs(Number(x.latest.net_assets.value) - ref) : Infinity;
      const dy = y.latest.net_assets ? Math.abs(Number(y.latest.net_assets.value) - ref) : Infinity;
      return dx - dy;
    }).slice(0, 8);

  const chargesOutstanding = rec.charges.filter((r) => ["outstanding", "part-satisfied"].includes(r.status)).length;
  const chargesSatisfied = rec.charges.length - chargesOutstanding;

  // Registry activity: filings (last five years + every accounts filing) and restatement events
  const pretty = (slug) => String(slug || "").replace(/-/g, " ");
  const activity = [
    ...rec.filings.map((f) => ({ date: f.filing_date, kind: "filing", f })),
    ...rec.events.map((e) => ({ date: e.event_date, kind: "event", e })),
  ].sort((x, y) => String(y.date).localeCompare(String(x.date)));
  const ACT_SHOW = 40;

  const pipe = D.pipeline.get(cid);
  const w = D.watch.has(cid);
  const inCmp = D.compareSel.all().includes(cid);

  $("#title-side").innerHTML = `
    <span class="act star ${w ? "on" : ""}" id="watch-toggle" title="watchlist">★</span>
    <span class="act cmp ${inCmp ? "on" : ""}" id="cmp-toggle" title="compare (up to four)">⇄</span>
    <select id="stage" class="stage-select" title="pipeline stage — stored in this browser only">
      <option value="">not in pipeline</option>
      ${D.STAGES.map((s) => `<option value="${s.key}" ${pipe && pipe.stage === s.key ? "selected" : ""}>${esc(s.label)}</option>`).join("")}
    </select>
    <button class="tw" id="export-profile" title="Excel-compatible CSV of every filed figure with its source reference">⬇ figures (CSV)</button>
    <button class="tw" id="print" title="Print-friendly profile">print</button>`;

  root.innerHTML = `
    <div class="fact-strip">
      <span><span class="k">registration</span><a href="${D.companyUrl(c.registration_id)}" rel="noopener">${esc(c.registration_id)}</a> (${esc(c.jurisdiction)})</span>
      <span><span class="k">status</span>${esc(c.status || "unknown")}</span>
      <span><span class="k">incorporated</span>${esc(c.incorporated || "unknown")}${D.companyAgeYears(c.incorporated) !== null ? ` (${D.companyAgeYears(c.incorporated)}y)` : ""}</span>
      <span><span class="k">sector</span>${D.divisionsOf(c.sic).map((d) => esc(D.divName(d))).join("; ")} <span class="sic-code">${c.sic.map(esc).join(" ")}</span></span>
      <span><span class="k">registered office</span>${esc([a.address_line_1, a.locality, a.region, a.postal_code, a.country].filter(Boolean).join(", "))}</span>
      <span><span class="k">mode</span><span class="mode ${esc(c.mode)}">${esc(c.mode)}</span></span>
      <span><span class="k">ownership class</span>${c.ownership_classification ? esc(c.ownership_classification) : state("not_reached", "ownership classification is Phase 2 and fail-closed: absence of a PSC statement is not evidence of independence")}</span>
      <span><span class="k">score</span>${state("not_reached", "screening has not run — Phase 2")}</span>
      ${c.name_variants && c.name_variants.length ? `<span><span class="k">previous names</span>${c.name_variants.map(esc).join("; ")}</span>` : ""}
      ${c.first_seen ? `<span><span class="k">in store since</span><code>${esc(c.first_seen)}</code></span>` : ""}
    </div>
    ${fresh
      ? `<p class="staleness-callout">Freshest machine-readable figures: period end <strong>${esc(fresh)}</strong>
         (${D.ageSpan(fresh)})${row.freshest_filed ? `, filed <strong>${esc(row.freshest_filed)}</strong>` : ""}. Every figure below carries its own period and traces to its filing.</p>`
      : `<p class="staleness-callout">No machine-readable figures on the fetched documents —
         ${rec.coverage.some((f) => f.status === "parse_failed") ? `${state("parse_failed")} a system defect is recorded below, not a data limitation.` : `filings have no iXBRL rendition ${state("unparseable_format")}.`}
         This company screens in signal mode on observable behaviour only.</p>`}

    <div class="tiles">
      <div class="tile"><div class="value">${rev ? figCell(rev) : coverageState("revenue")}</div>
        <div class="label">revenue</div><div class="detail">${rev ? `period end ${esc(rev.period_end)}` : "no current revenue figure"}</div></div>
      <div class="tile"><div class="value">${state("not_reached")}</div>
        <div class="label">EBITDA</div><div class="detail">derived figure — Phase 2</div></div>
      <div class="tile"><div class="value">${state("not_reached")}</div>
        <div class="label">margin</div><div class="detail">derived figure — Phase 2</div></div>
      <div class="tile"><div class="value">${na ? figCell(na) : coverageState("net_assets")}</div>
        <div class="label">${na ? esc(na.concept.replace("_", " ")) : "net assets"}</div><div class="detail">${na ? `period end ${esc(na.period_end)}` : ""}</div></div>
      <div class="tile"><div class="value">${emp ? figCell(emp) : coverageState("average_employees")}</div>
        <div class="label">employees (average)</div><div class="detail">${emp ? `period end ${esc(emp.period_end)}` : ""}</div></div>
      <div class="tile"><div class="value">${oa !== null ? "~" + oa : state("not_observable", "no active individual PSC with a published birth year")}</div>
        <div class="label">owner age</div><div class="detail">${oa !== null ? `PSC born ${row.owner_dob.year}-${String(row.owner_dob.month || "").padStart(2, "0")}` : "from PSC birth month/year"}</div></div>
    </div>

    <section>
      <h2>Financial trajectory</h2>
      <p class="note">Filed observations only, current per deterministic supersession; click any value to trace. The trend
      column plots the filed values as filed (scaling is the only arithmetic). EBITDA, margins and growth are Phase 2 derived
      figures and render ${state("not_reached")} until the derive layer exists.</p>
      ${periods.length ? `<table class="matrix">
        <thead><tr><th>concept</th>${periods.map((p) => `<th class="num">${esc(p)}<br>${D.ageSpan(p)}</th>`).join("")}<th class="trend">trend · ${periodsAll.length} period(s)</th></tr></thead>
        <tbody>
          <tr><th colspan="${periods.length + 2}">income statement</th></tr>${matrixRows(PL)}
          <tr><th colspan="${periods.length + 2}">balance sheet</th></tr>${matrixRows(BS)}
          <tr><th colspan="${periods.length + 2}">other</th></tr>${matrixRows(["average_employees"])}
        </tbody></table>` : `<div class="empty">No figures to tabulate — see coverage below for the recorded causes.</div>`}
    </section>

    <section>
      <h2>Observed on the register · last ${D.OBS_WINDOW} months</h2>
      <p class="note">What the register shows happened, dated. Each observation is named after the event itself — a charge
      registered is a lender taking security, not "a debt raise"; a PSC ceased is a notified change of control, not "a sale".</p>
      ${obs.length ? `<table><thead><tr><th>observation</th><th>date</th><th>what it is</th><th></th></tr></thead><tbody>
        ${obs.map((o) => `<tr><td><span class="obs">${esc(o.label)}</span></td><td>${esc(o.date || "—")}</td><td style="color:var(--ink-2)">${esc(o.title)}</td>
          <td>${o.key === "security_interest_registered" ? `<a href="${D.chargesUrl(c.registration_id)}" rel="noopener">charges ↗</a>`
              : o.key.startsWith("officer") ? `<a href="${D.officersUrl(c.registration_id)}" rel="noopener">officers ↗</a>`
              : o.key.startsWith("psc") ? `<a href="${D.pscUrl(c.registration_id)}" rel="noopener">PSC register ↗</a>` : ""}</td></tr>`).join("")}
        </tbody></table>` : `<p class="note"><span class="quiet">quiet</span> — no charge, officer or PSC event in the window, and no restatement on record.</p>`}
      <p class="note">Why this company surfaced: it matches the mandate's sector and incorporation filters (SIC ${c.sic.map(esc).join(", ")}) and screens in
      <span class="mode ${esc(c.mode)}">${esc(c.mode)}</span> mode. Going-concern language, auditor changes, overdue filings and plausibility flags are Phase 2 detectors: ${state("not_reached")}.</p>
    </section>

    <section>
      <h2>Ownership &amp; control</h2>
      <div class="succession">
        <strong>Succession read</strong> — stated as register observations, not conclusions:
        <ul>
          <li>${oa !== null ? `Oldest active individual beneficial owner born ${row.owner_dob.year} (age ~${oa}).`
                          : `No active individual beneficial owner with a published birth year — owner age ${state("not_observable")}.`}</li>
          <li>${singleBO ? "A single active beneficial owner holds 75–100% of shares." : `${activeBOs.length} active beneficial owner(s) on record.`}</li>
          <li>${youngest && youngest.dob_year ? `Youngest active officer born ${youngest.dob_year}; ${recentAppt.length} officer(s) appointed in the last five years.` : `No active officer with a published birth year.`}</li>
          <li>${rec.ownership_statements.length ? `${rec.ownership_statements.length} PSC statement(s) filed (see below) — an opaque statement makes ownership <em>unclassifiable</em>, never independent.` : "No PSC statements filed."}</li>
          <li>Succession signal scoring is Phase 2: ${state("not_reached")}.</li>
        </ul>
      </div>
      ${bos.length ? `<table>
        <thead><tr><th>beneficial owner</th><th>kind</th><th>born</th><th>natures of control</th><th>notified</th><th>ceased</th></tr></thead>
        <tbody>${bos.map((b) => `<tr>
          <td>${esc(b.name)}</td><td>${esc(b.kind || "")}</td>
          <td class="num">${b.dob_year ? `${b.dob_year} (~${D.THIS_YEAR - b.dob_year})` : `<span class="quiet">corporate / none published</span>`}</td>
          <td>${(b.control_natures || []).map(esc).join("<br>") || state("not_observable")}</td>
          <td>${esc(b.notified_on || "")}</td><td>${esc(b.ceased_on || "active")}</td></tr>`).join("")}</tbody></table>`
      : `<p class="note">No beneficial-owner records — a recorded gap, not evidence of independence. <a href="${D.pscUrl(c.registration_id)}" rel="noopener">PSC register ↗</a></p>`}
      ${rec.ownership_statements.length ? `<table style="margin-top:8px"><thead><tr><th>PSC statement (verbatim)</th><th>notified</th><th>ceased</th></tr></thead>
        <tbody>${rec.ownership_statements.map((s) => `<tr><td><code>${esc(s.statement)}</code></td><td>${esc(s.notified_on || "")}</td><td>${esc(s.ceased_on || "active")}</td></tr>`).join("")}</tbody></table>` : ""}
      ${rec.exemptions.length ? `<p class="note" style="margin-top:8px">Exemptions from PSC disclosure on record: ${rec.exemptions.map((e) => `<code>${esc(e.exemption_type)}</code>`).join(", ")} — typically a regulated-market listing.</p>` : ""}
      ${offs.length ? `<p class="note" style="margin-top:10px">Officers (${activeOff.length} active of ${offs.length}):</p>
        <table><thead><tr><th>officer</th><th>role</th><th>born</th><th>nationality</th><th>appointed</th><th>resigned</th></tr></thead>
        <tbody>${offs.slice().reverse().slice(0, 15).map((o) => `<tr>
          <td>${esc(o.name)}</td><td>${esc(o.role || "")}</td>
          <td class="num">${o.dob_year ? `${o.dob_year} (~${D.THIS_YEAR - o.dob_year})` : ""}</td><td>${esc(o.nationality || "")}</td>
          <td>${esc(o.appointed_on || "")}</td><td>${esc(o.resigned_on || "serving")}</td></tr>`).join("")}
        </tbody></table>${offs.length > 15 ? `<p class="note">Showing latest 15 of ${offs.length}; full roster on the <a href="${D.officersUrl(c.registration_id)}" rel="noopener">register ↗</a>.</p>` : ""}` : ""}
    </section>

    <section>
      <h2>Security &amp; debt</h2>
      ${rec.charges.length ? `
        <p class="note">${chargesOutstanding} outstanding / ${chargesSatisfied} satisfied. <a href="${D.chargesUrl(c.registration_id)}" rel="noopener">register ↗</a></p>
        <table><thead><tr><th>created</th><th>status</th><th>satisfied</th><th>holder(s)</th><th>classification</th></tr></thead>
        <tbody>${rec.charges.map((r) => `<tr>
          <td>${esc(r.created_on || "")}</td><td>${esc(r.status || "")}</td><td>${esc(r.satisfied_on || "—outstanding")}</td>
          <td>${(r.secured_parties || []).map(esc).join("<br>")}</td>
          <td>${esc((r.classification && (r.classification.description || r.classification.type)) || "")}</td></tr>`).join("")}
        </tbody></table>`
      : `<p class="note">No security interests on record — no registered lender to work around.</p>`}
    </section>

    <section>
      <h2>Registry activity</h2>
      <p class="note">${rec.filings.length} filing(s) carried in the record (last five years plus every accounts filing) of
      ${nf.format(c.filings_on_register)} on the register — <a href="${D.filingHistoryUrl(c.registration_id)}" rel="noopener">full history ↗</a>.
      Restatement events (a later filing changing an earlier figure for the same period) appear inline.</p>
      ${activity.length ? `<table class="timeline"><thead><tr><th>date</th><th>type</th><th>filing</th><th>details</th><th></th></tr></thead>
        <tbody id="activity-rows">${activity.slice(0, ACT_SHOW).map(activityRow).join("")}</tbody></table>
        ${activity.length > ACT_SHOW ? `<p class="pager"><button class="tw" id="activity-more">show all ${activity.length}</button></p>` : ""}`
      : `<p class="note">No filings carried in the record.</p>`}
    </section>

    ${rec.events.length ? `<section>
      <h2>Restatements</h2>
      <p class="note">Each item is two filed observations of the same concept and period. Both stay on the record; the later filing is current.</p>
      <table><thead><tr><th>event</th><th>concept</th><th>period</th><th class="num">earlier</th><th class="num">later</th><th>classification</th><th>material</th></tr></thead>
      <tbody>${rec.events.flatMap((e) => ((e.payload && e.payload.restatements) || []).map((r) => `<tr>
        <td>${esc(e.event_date)}</td><td>${esc(r.concept)}</td><td>${esc(r.period_end)}</td>
        <td class="num">${figById[r.old_figure_id] ? `<a href="${D.traceHref(r.old_figure_id, cid)}">${esc(D.figDisplay(figById[r.old_figure_id]))}</a>` : esc(r.old_value)}</td>
        <td class="num">${figById[r.new_figure_id] ? `<a href="${D.traceHref(r.new_figure_id, cid)}">${esc(D.figDisplay(figById[r.new_figure_id]))}</a>` : esc(r.new_value)}</td>
        <td>${esc(r.classification || "")}</td><td>${r.material ? "yes" : "no"}</td></tr>`)).join("")}</tbody></table>
    </section>` : ""}

    <section>
      <h2>Peer set</h2>
      <p class="note">Same SIC division, nearest by net assets across the whole store (mechanical selection — not a curated comp set).</p>
      ${peers.length ? `<table><thead><tr><th>company</th><th>sector</th><th class="num">revenue</th><th class="num">margin</th><th class="num">net assets</th><th class="num">employees</th><th>filed</th></tr></thead>
        <tbody>${peers.map((p) => `<tr>
          <td class="co-name"><a href="${D.companyHref(p.id)}">${esc(p.name)}</a></td>
          <td class="sic-label">${esc(D.divName(D.divisionsOf(p.sic)[0]))}</td>
          <td class="num">${p.latest.revenue ? `<a href="${D.traceHref(p.latest.revenue.figure_id, p.id)}">${esc(D.refDisplay(p.latest.revenue, "revenue"))}</a>` : D.causeFromCounts(p)}</td>
          <td class="num">${state("not_reached")}</td>
          <td class="num">${p.latest.net_assets ? `<a href="${D.traceHref(p.latest.net_assets.figure_id, p.id)}">${esc(D.refDisplay(p.latest.net_assets, "net_assets"))}</a>` : D.causeFromCounts(p)}</td>
          <td class="num">${p.latest.employees ? esc(D.refDisplay(p.latest.employees, "employees")) : D.causeFromCounts(p)}</td>
          <td>${esc(p.freshest_filed || "")}</td>
        </tr>`).join("")}</tbody></table>` : `<p class="note">No peers in this division in the store.</p>`}
    </section>

    <section>
      <h2>Fetched documents</h2>
      <p class="note">The ingest fetches the most recent account documents per company; each is content-hashed and kept.</p>
      <table><thead><tr><th>period end</th><th>filed</th><th>regime</th><th>format</th><th>parse</th><th class="num">figures</th><th>produced by</th><th></th></tr></thead>
      <tbody>${rec.documents.map((d) => `<tr>
          <td>${esc(d.period_end || "")}</td><td>${esc(d.filed_date || "")}</td>
          <td>${esc(d.account_type || "")}</td><td>${esc((d.content_type || "").replace("application/", ""))}</td>
          <td>${d.parse_status === "parsed" ? "parsed" : state(d.parse_status === "pdf_only" ? "unparseable_format" : "parse_failed", d.parse_status)}</td>
          <td class="num">${rec.figures.filter((f) => f.source_document_id === d.id).length}</td>
          <td>${esc(d.production_software || "not declared")}</td>
          <td>${D.filingUrl(c.registration_id, d.transaction_id) ? `<a href="${D.filingUrl(c.registration_id, d.transaction_id)}" rel="noopener">open ↗</a>` : ""}</td>
        </tr>`).join("")}</tbody></table>
    </section>

    <section>
      <h2>Concept coverage at ${esc(covPeriod || "latest period")}</h2>
      <table><thead><tr><th>concept</th><th>status</th><th>recorded cause</th></tr></thead>
      <tbody>${rec.coverage.map((f) => `<tr><td>${esc(f.concept)}</td>
        <td>${f.status === "available" ? `<span class="state st-available">available</span>` : state(f.status)}</td>
        <td style="color:var(--ink-2)">${esc(f.detail || "")}</td></tr>`).join("")}</tbody></table>
      <dl class="legend">${Object.keys(D.STATES).map((k) => `<dt>${state(k)}</dt><dd>${esc(D.STATES[k])}</dd>`).join("")}</dl>
    </section>

    <section id="notes-section">
      <h2>Working notes</h2>
      <p class="note">Stored in this browser only — never synced, never sent. ${pipe ? "" : "Add the company to the pipeline to keep notes."}</p>
      ${pipe ? `<textarea id="notes" class="notes" placeholder="What would need to be true…">${esc(pipe.notes || "")}</textarea>
        <p class="note quiet-note" id="notes-saved">${pipe.updated_at ? `last saved ${esc(D.fmtStamp(pipe.updated_at))}` : ""}</p>` : ""}
    </section>`;

  function activityRow(item) {
    if (item.kind === "event") {
      const n = ((item.e.payload && item.e.payload.restatements) || []).length;
      return `<tr class="ev"><td>${esc(item.date)}</td><td><span class="obs">restated</span></td><td>restatement event</td>
        <td style="color:var(--ink-2)">${n} figure(s) restated by a later filing (see Restatements)</td><td></td></tr>`;
    }
    const f = item.f;
    const dv = f.description_values || {};
    const details = Object.entries(dv).filter(([k]) => k !== "made_up_date").map(([k, v]) => `${esc(pretty(k))}: ${esc(v)}`).join(" · ");
    return `<tr><td>${esc(f.filing_date || "")}</td><td><code>${esc(f.type || "")}</code>${f.paper_filed ? ` <span class="quiet" title="paper filed">paper</span>` : ""}</td>
      <td>${esc(pretty(f.description))}${dv.made_up_date ? ` <span class="quiet">to ${esc(dv.made_up_date)}</span>` : ""}</td>
      <td style="color:var(--ink-2)">${details}</td>
      <td>${D.filingPageUrl(c.registration_id, f.transaction_id) ? `<a href="${D.filingPageUrl(c.registration_id, f.transaction_id)}" rel="noopener">open ↗</a>` : ""}</td></tr>`;
  }
  const more = $("#activity-more");
  if (more) more.addEventListener("click", () => { $("#activity-rows").innerHTML = activity.map(activityRow).join(""); more.remove(); });

  // ---- actions ----
  $("#watch-toggle").addEventListener("click", () => $("#watch-toggle").classList.toggle("on", D.watch.toggle(cid)));
  $("#cmp-toggle").addEventListener("click", () => {
    const r = D.compareSel.toggle(cid);
    if (!r.ok) { D.toast("Compare holds four companies — remove one first"); return; }
    $("#cmp-toggle").classList.toggle("on", r.list.includes(cid)); D.refreshCompareBadge();
    D.toast(r.list.includes(cid) ? `Compare: ${r.list.length} of 4` : "Removed from compare");
  });
  $("#stage").addEventListener("change", (e) => {
    const v = e.target.value;
    if (!v) { D.pipeline.remove(cid); D.toast("Removed from pipeline"); location.reload(); return; }
    if (!D.pipeline.get(cid)) D.pipeline.add(cid, { name: c.name, registration_id: c.registration_id });
    D.pipeline.set(cid, { stage: v });
    D.toast(`Pipeline: ${D.STAGES.find((s) => s.key === v).label}`);
    if (!$("#notes")) location.reload();
  });
  const notes = $("#notes");
  if (notes) {
    let t = null;
    notes.addEventListener("input", () => {
      clearTimeout(t);
      t = setTimeout(() => { D.pipeline.set(cid, { notes: notes.value }); $("#notes-saved").textContent = `saved ${D.fmtStamp(new Date().toISOString())}`; }, 400);
    });
  }
  $("#print").addEventListener("click", () => window.print());
  $("#export-profile").addEventListener("click", () => {
    const header = ["company", "registration", "concept", "value", "unit", "currency", "period_start", "period_end", "basis", "current",
      "source_tag", "raw_text", "accounts_regime", "filed_date", "document_sha256", "producing_software", "filing_url", "figure_id"];
    const rows = [header];
    for (const f of rec.figures.slice().sort((x, y) => (y.is_current - x.is_current) || String(y.period_end).localeCompare(String(x.period_end)))) {
      const d = doc(f.source_document_id);
      rows.push([c.name, c.registration_id, f.concept, f.value, f.unit || "", f.currency || "", f.period_start || "", f.period_end || "",
        f.basis, f.is_current ? "yes" : "no (superseded)", f.source_tag || "", f.raw_text || "",
        d ? d.account_type || "" : "", d ? d.filed_date || "" : "", d ? d.content_hash || "" : "", d ? d.production_software || "" : "",
        d ? D.filingUrl(c.registration_id, d.transaction_id) || "" : "", f.id]);
    }
    D.csvDownload(`${c.registration_id}-figures-${D.SITE.run_id || "run"}.csv`, rows);
  });
})();
