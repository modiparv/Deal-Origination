/* TODAY — the morning page: what the store holds, what entered it since
 * this browser last looked, what is on the watchlist and where it has
 * gone stale, the pipeline at a glance, saved screens with live counts,
 * coverage by sector, and the run history behind all of it.
 */
(async function () {
  "use strict";
  const D = window.DOE;
  const { $, $$, esc, nf, state } = D;
  const root = $("#today-root");
  const S = D.SITE;
  D.shell({ title: "Today", crumb: "The store, your watchlist and pipeline, and what changed" });
  if (!S.store_present) { D.emptyStore(root); return; }
  let ix;
  try { ix = await D.data.index(); } catch (e) { D.loadError(root, e); return; }
  const ROWS = ix.companies;

  // ---- store status ----
  const m = S.modes || {};
  const modeTotal = (m.financial || 0) + (m.signal || 0) + (m.parse_failed || 0);
  const seg = (k) => (m[k] ? `<span class="seg ${k}" style="width:${(100 * m[k]) / modeTotal}%" title="${k}: ${nf.format(m[k])}"></span>` : "");
  const runs = (S.runs || []).slice().reverse();
  const lastRun = runs[0] || null;
  const runHealth = !lastRun ? `<span class="state st-not_reached">no runs</span>`
    : lastRun.exit_status === 0 ? `<span class="state st-available">clean</span>`
    : `<span class="state st-parse_failed" title="the run recorded per-company errors; progress was persisted">${lastRun.errors ?? "?"} error(s)</span>`;
  const gen = D.ageInfo(S.generated_at);

  // ---- since last visit ----
  const lv = D.lastVisit.get();
  const newRows = lv ? ROWS.filter((c) => c.first_seen && c.first_seen > lv.run_id) : [];
  newRows.sort((a, b) => String(b.freshest_filed || "").localeCompare(String(a.freshest_filed || "")));

  // ---- watchlist ----
  const watched = [...D.watch.all()].map((id) => ix.byId[id]).filter(Boolean)
    .sort((a, b) => a.name.localeCompare(b.name));
  const alertsFor = (c) => {
    const out = [];
    const fa = D.ageInfo(c.freshest_period);
    if (!fa) out.push(`<span class="state st-unparseable_format" title="no machine-readable figures">no figures</span>`);
    else if (fa.stale) out.push(`<span class="age stale" title="freshest period end ${esc(c.freshest_period)}">stale · ${fa.label}</span>`);
    if ((c.coverage.statuses || {}).parse_failed) out.push(state("parse_failed"));
    for (const o of D.observations(c)) out.push(D.obsChip(o));
    return out.join(" ");
  };

  // ---- pipeline ----
  const pipe = D.pipeline.all();
  const pipeRows = Object.entries(pipe).map(([id, p]) => ({ id, ...p, row: ix.byId[id] }));
  const stageCounts = Object.fromEntries(D.STAGES.map((s) => [s.key, pipeRows.filter((p) => p.stage === s.key).length]));
  const recent = pipeRows.slice().sort((a, b) => String(b.updated_at || "").localeCompare(String(a.updated_at || ""))).slice(0, 6);

  // ---- saved screens (live counts) ----
  const saved = D.screens.all().map((s) => { const f = D.parseFilters(s.params); return { ...s, f, b: D.bucketise(ROWS, f) }; });

  // ---- coverage by division ----
  const byDiv = {};
  for (const c of ROWS) for (const d of D.divisionsOf(c.sic)) {
    const e = (byDiv[d] ||= { companies: 0, financial: 0, signal: 0, parse_failed: 0, revenue: 0, fresh: 0 });
    e.companies += 1; e[c.mode] = (e[c.mode] || 0) + 1;
    if (c.latest.revenue) e.revenue += 1;
    const fa = D.ageInfo(c.freshest_period); if (fa && !fa.stale) e.fresh += 1;
  }

  root.innerHTML = `
    <div class="today-grid">
      <div class="col">
        <section class="card">
          <h2>Store</h2>
          <div class="tiles tiles-4">
            <div class="tile"><div class="value">${nf.format(S.companies)}</div><div class="label">companies</div><div class="detail">${S.universe_hits ? `of ${nf.format(S.universe_hits)} in the mandate universe` : "mandate universe sample"}</div></div>
            <div class="tile"><div class="value">${nf.format(S.figures)}</div><div class="label">filed figures</div><div class="detail">${nf.format(S.documents)} source documents</div></div>
            <div class="tile"><div class="value">${nf.format(S.filings || 0)}</div><div class="label">filings on record</div><div class="detail">${nf.format((S.totals || {}).officers || 0)} officers · ${nf.format((S.totals || {}).beneficial_owners || 0)} PSCs</div></div>
            <div class="tile"><div class="value">${nf.format(m.financial || 0)}<span class="sep"> / </span><span class="seg-signal">${nf.format(m.signal || 0)}</span>${m.parse_failed ? `<span class="sep"> / </span>${nf.format(m.parse_failed)}` : ""}</div>
              <div class="label">financial / signal${m.parse_failed ? " / parse_failed" : ""}</div><div class="modebar">${seg("financial")}${seg("signal")}${seg("parse_failed")}</div></div>
          </div>
          <p class="note">Store exported <strong>${esc(D.fmtStamp(S.generated_at))}</strong>${gen ? ` (${gen.label} ago)` : ""} from ingest run <code>${esc(S.run_id)}</code>.
            Last run: ${runHealth}${lastRun ? ` — ${nf.format(lastRun.ingested ?? 0)} companies ingested, started ${esc(D.fmtStamp(lastRun.started_at))}` : ""}.
            ${(S.parse_failures || {}).documents ? `<span class="state st-parse_failed">${S.parse_failures.documents} document(s) failed to parse</span> across ${S.parse_failures.companies} companies — a defect list, on the <a href="../ops/">operations page</a>.` : "No parse failures in the store."}</p>
        </section>

        <section class="card">
          <h2>Since your last visit</h2>
          ${!lv ? `<p class="note">First visit in this browser. From now on, companies that enter the store after run <code>${esc(S.run_id)}</code> are listed here.</p>`
            : lv.run_id === S.run_id ? `<p class="note">The store has not changed since your last visit (${esc(D.fmtStamp(lv.at))}, run <code>${esc(lv.run_id)}</code>).</p>`
            : `<p class="note"><strong>${nf.format(newRows.length)}</strong> compan${newRows.length === 1 ? "y" : "ies"} entered the store after run <code>${esc(lv.run_id)}</code> (your last visit ${esc(D.fmtStamp(lv.at))}).
               <a href="screen.html" class="tw" style="margin-left:8px">open the screen</a></p>
              ${newRows.length ? `<table><thead><tr><th>company</th><th>sector</th><th class="num">revenue</th><th class="num">net assets</th><th>filed</th><th>observed</th></tr></thead>
              <tbody>${newRows.slice(0, 12).map(rowLine).join("")}</tbody></table>${newRows.length > 12 ? `<p class="note">Showing 12 of ${newRows.length}.</p>` : ""}` : ""}`}
          <p class="note"><button class="tw" id="mark-seen">mark the current store as seen</button></p>
        </section>

        <section class="card">
          <h2>Coverage by sector division</h2>
          <p class="note">How much of each division the register lets us measure. "With revenue" counts companies whose latest filed accounts carry a machine-readable revenue figure; "fresh" counts figures under 24 months old.</p>
          <table><thead><tr><th>division</th><th class="num">companies</th><th class="num">financial</th><th class="num">signal</th><th class="num">parse failed</th><th class="num">with revenue</th><th class="num">fresh</th></tr></thead>
          <tbody>${Object.keys(byDiv).sort((a, b) => byDiv[b].companies - byDiv[a].companies).map((d) => { const e = byDiv[d]; return `<tr>
            <td><a href="screen.html?divs=${d}">${esc(D.divName(d))}</a> <span class="sic-code">${d}</span></td>
            <td class="num">${nf.format(e.companies)}</td><td class="num">${nf.format(e.financial)}</td><td class="num">${nf.format(e.signal)}</td>
            <td class="num">${e.parse_failed ? `<span class="state st-parse_failed">${e.parse_failed}</span>` : "0"}</td>
            <td class="num">${nf.format(e.revenue)}</td><td class="num">${nf.format(e.fresh)}</td></tr>`; }).join("")}</tbody></table>
        </section>
      </div>

      <div class="col">
        <section class="card">
          <h2>Watchlist <span class="count">${watched.length}</span></h2>
          ${watched.length ? `<table><thead><tr><th>company</th><th>freshest</th><th class="num">revenue</th><th>stage</th><th>alerts</th></tr></thead>
            <tbody>${watched.map((c) => `<tr>
              <td class="co-name"><a href="${D.companyHref(c.id)}">${esc(c.name)}</a><br><span class="sic-label">${esc(D.divName(D.divisionsOf(c.sic)[0]))}</span></td>
              <td>${c.freshest_period ? `${esc(c.freshest_period)}<br>${D.ageSpan(c.freshest_period)}` : state("not_captured")}</td>
              <td class="num">${c.latest.revenue ? `<a href="${D.traceHref(c.latest.revenue.figure_id, c.id)}">${esc(D.refDisplay(c.latest.revenue, "revenue"))}</a>` : D.causeFromCounts(c)}</td>
              <td>${pipe[c.id] ? `<span class="stage-chip">${esc(D.STAGES.find((s) => s.key === pipe[c.id].stage).label)}</span>` : `<span class="quiet">—</span>`}</td>
              <td class="obs-cell">${alertsFor(c) || `<span class="quiet">quiet</span>`}</td></tr>`).join("")}</tbody></table>`
          : `<p class="note">Nothing watched yet. Star a company on the <a href="screen.html">screen</a> (or press <kbd>w</kbd> on a focused row) and it shows up here with its staleness and register events.</p>`}
        </section>

        <section class="card">
          <h2>Pipeline <span class="count">${pipeRows.length}</span></h2>
          <div class="stagebar">${D.STAGES.map((s) => `<a href="pipeline.html#${s.key}" class="stage"><span class="n">${stageCounts[s.key]}</span>${esc(s.label)}</a>`).join("")}</div>
          ${recent.length ? `<table><thead><tr><th>company</th><th>stage</th><th>updated</th></tr></thead><tbody>${recent.map((p) => `<tr>
            <td class="co-name"><a href="${D.companyHref(p.id)}">${esc((p.row && p.row.name) || p.name || p.id)}</a></td>
            <td><span class="stage-chip">${esc((D.STAGES.find((s) => s.key === p.stage) || {}).label || p.stage)}</span></td>
            <td>${esc(D.fmtDate(p.updated_at))}</td></tr>`).join("")}</tbody></table>`
          : `<p class="note">Empty. Add companies from the screen (<kbd>p</kbd> or the + on a row); stages and notes live in this browser only.</p>`}
        </section>

        <section class="card">
          <h2>Saved screens <span class="count">${saved.length}</span></h2>
          ${saved.length ? `<table><thead><tr><th>screen</th><th class="num">matched</th><th class="num">failed</th><th class="num">unmeasured</th></tr></thead>
            <tbody>${saved.map((s) => `<tr>
              <td><a href="screen.html?${esc(s.params)}"><strong>${esc(s.name)}</strong></a><br><span class="sic-label">${esc(D.describeFilters(s.f))}</span></td>
              <td class="num">${nf.format(s.b.pass.length)}</td><td class="num">${nf.format(s.b.fail.length)}</td><td class="num">${nf.format(s.b.unmeasurable.length)}</td></tr>`).join("")}</tbody></table>`
          : `<p class="note">No saved screens. Build one on the <a href="screen.html">screen</a> and press <em>save</em>; counts here are live against the current store.</p>`}
        </section>

        <section class="card">
          <h2>Run history</h2>
          <table><thead><tr><th>run</th><th>started</th><th class="num">ingested</th><th class="num">new figures</th><th>outcome</th></tr></thead>
          <tbody>${runs.slice(0, 10).map((r) => `<tr>
            <td><code>${esc(r.run_id)}</code></td><td>${esc(D.fmtStamp(r.started_at))}</td>
            <td class="num">${r.ingested != null ? nf.format(r.ingested) : ""}</td><td class="num">${r.figures_new != null ? nf.format(r.figures_new) : ""}</td>
            <td>${r.exit_status === 0 ? `<span class="state st-available">clean</span>` : r.exit_status == null ? `<span class="state st-not_reached">unfinished</span>` : `<span class="state st-parse_failed">${r.errors ?? "?"} error(s)</span>`}</td></tr>`).join("")}</tbody></table>
          <p class="note">Every unattended run is logged; the coverage report and spot-check dossier for each are on the <a href="../ops/">operations page</a>.</p>
        </section>
      </div>
    </div>`;

  function rowLine(c) {
    return `<tr>
      <td class="co-name"><a href="${D.companyHref(c.id)}">${esc(c.name)}</a><br><span class="co-reg">${esc(c.registration_id)}</span></td>
      <td class="sic-label">${esc(D.divName(D.divisionsOf(c.sic)[0]))}</td>
      <td class="num">${c.latest.revenue ? `<a href="${D.traceHref(c.latest.revenue.figure_id, c.id)}">${esc(D.refDisplay(c.latest.revenue, "revenue"))}</a>` : D.causeFromCounts(c)}</td>
      <td class="num">${c.latest.net_assets ? `<a href="${D.traceHref(c.latest.net_assets.figure_id, c.id)}">${esc(D.refDisplay(c.latest.net_assets, "net_assets"))}</a>` : D.causeFromCounts(c)}</td>
      <td>${esc(c.freshest_filed || "")}</td>
      <td class="obs-cell">${D.observations(c).slice(0, 2).map(D.obsChip).join(" ") || `<span class="quiet">quiet</span>`}</td></tr>`;
  }
  $("#mark-seen").addEventListener("click", () => { D.lastVisit.set(S.run_id); D.toast("Marked as seen"); location.reload(); });
  if (!lv) D.lastVisit.set(S.run_id);
})();
