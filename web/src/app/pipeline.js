/* PIPELINE — a browser-local board. Stages and notes are the analyst's
 * own working state: stored in localStorage, never synced, never sent.
 * Company facts on each card come from the store index and stay
 * traceable; nothing here mutates a filed figure.
 */
(async function () {
  "use strict";
  const D = window.DOE;
  const { $, $$, esc, nf, state } = D;
  const root = $("#pipeline-root");
  D.shell({ title: "Pipeline", crumb: "Stages and notes live in this browser only — no send capability, no sync" });
  if (!D.SITE.store_present) { D.emptyStore(root); return; }
  let ix;
  try { ix = await D.data.index(); } catch (e) { D.loadError(root, e); return; }

  function draw() {
    const pipe = D.pipeline.all();
    const items = Object.entries(pipe).map(([id, p]) => ({ id, ...p, row: ix.byId[id] }));
    $("#title-side").innerHTML = `
      <span class="quiet">${items.length} compan${items.length === 1 ? "y" : "ies"}</span>
      <button class="tw" id="export-board" title="Excel-compatible CSV of the board with figures and their sources">⬇ board (CSV)</button>
      <button class="tw" id="clear-board" title="Remove every company from the board (this browser)">clear</button>`;
    $("#export-board").addEventListener("click", () => exportBoard(items));
    $("#clear-board").addEventListener("click", () => {
      if (!items.length) return;
      if (confirm(`Remove all ${items.length} companies from the board? Notes are lost.`)) { D.pipeline.clear(); draw(); }
    });

    if (!items.length) {
      root.innerHTML = `<div class="empty"><strong>The board is empty.</strong> Add companies from the <a href="screen.html">screen</a>
        (the <b>+</b> on a row, or <kbd>p</kbd> on a focused row) or from a company page's stage selector. Stages:
        ${D.STAGES.map((s) => `<span class="stage-chip">${esc(s.label)}</span>`).join(" ")}.</div>`;
      return;
    }
    root.innerHTML = `<div class="board">${D.STAGES.map((s) => {
      const cards = items.filter((p) => p.stage === s.key).sort((a, b) => String(b.updated_at || "").localeCompare(String(a.updated_at || "")));
      return `<div class="column" id="${s.key}"><h3>${esc(s.label)} <span class="count">${cards.length}</span></h3>
        ${cards.map(card).join("") || `<div class="drop">—</div>`}</div>`;
    }).join("")}</div>`;

    $$("[data-move]").forEach((el) => el.addEventListener("change", (e) => {
      D.pipeline.set(el.dataset.move, { stage: e.target.value }); D.toast("Moved"); draw();
    }));
    $$("[data-remove]").forEach((el) => el.addEventListener("click", () => {
      D.pipeline.remove(el.dataset.remove); D.toast("Removed from pipeline"); draw();
    }));
    $$("[data-notes]").forEach((el) => {
      let t = null;
      el.addEventListener("input", () => { clearTimeout(t); t = setTimeout(() => D.pipeline.set(el.dataset.notes, { notes: el.value }), 400); });
    });
    $$("[data-star]").forEach((el) => el.addEventListener("click", () => el.classList.toggle("on", D.watch.toggle(el.dataset.star))));
  }

  function card(p) {
    const c = p.row;
    const fa = c ? D.ageInfo(c.freshest_period) : null;
    const obs = c ? D.observations(c) : [];
    return `<div class="pcard">
      <div class="pcard-head">
        <a class="pcard-name" href="${D.companyHref(p.id)}">${esc((c && c.name) || p.name || p.id)}</a>
        <span class="act star ${D.watch.has(p.id) ? "on" : ""}" data-star="${esc(p.id)}" title="watchlist">★</span>
      </div>
      ${c ? `<div class="pcard-meta">${esc(D.divName(D.divisionsOf(c.sic)[0]))} · ${esc(c.locality || c.region || "")} · <span class="mode ${esc(c.mode)}">${esc(c.mode)}</span></div>
      <div class="pcard-figs">
        <span><span class="k">revenue</span>${c.latest.revenue ? `<a href="${D.traceHref(c.latest.revenue.figure_id, c.id)}">${esc(D.refDisplay(c.latest.revenue, "revenue"))}</a>` : D.causeFromCounts(c)}</span>
        <span><span class="k">net assets</span>${c.latest.net_assets ? `<a href="${D.traceHref(c.latest.net_assets.figure_id, c.id)}">${esc(D.refDisplay(c.latest.net_assets, "net_assets"))}</a>` : D.causeFromCounts(c)}</span>
        <span><span class="k">EBITDA</span>${D.notDerived()}</span>
        <span><span class="k">owner</span>${D.ownerAge(c) !== null ? "~" + D.ownerAge(c) : `<span class="state st-not_observable">no dob</span>`}</span>
      </div>
      <div class="pcard-meta">${c.freshest_period ? `figures to ${esc(c.freshest_period)} · ${D.ageSpan(c.freshest_period)}` : state("not_captured")}
        ${obs.length ? " · " + obs.slice(0, 3).map(D.obsChip).join(" ") : ""}</div>`
      : `<div class="pcard-meta">${state("not_captured", "this company is not in the current store export")}</div>`}
      <textarea class="notes small" data-notes="${esc(p.id)}" placeholder="notes (this browser only)">${esc(p.notes || "")}</textarea>
      <div class="pcard-foot">
        <select data-move="${esc(p.id)}" class="stage-select">${D.STAGES.map((s) => `<option value="${s.key}" ${s.key === p.stage ? "selected" : ""}>${esc(s.label)}</option>`).join("")}</select>
        <span class="quiet">${esc(D.fmtDate(p.updated_at || p.added_at))}</span>
        <button class="tw small" data-remove="${esc(p.id)}" title="remove from the board">remove</button>
      </div>
    </div>`;
  }

  function exportBoard(items) {
    const header = ["stage", "company", "registration", "sector (SIC)", "screening_mode", "revenue", "revenue_source", "net_assets", "net_assets_source",
      "EBITDA", "owner_age_approx", "freshest_period_end", "filed_date", "observed_12m", "notes", "added", "updated", "register_url"];
    const src = (ref, c) => (ref ? `figure ${ref.figure_id} | period end ${ref.period_end} | filed ${ref.filed_date} | ${D.filingHistoryUrl(c.registration_id)}` : "");
    const rows = [header];
    for (const s of D.STAGES) for (const p of items.filter((x) => x.stage === s.key)) {
      const c = p.row || {};
      const L = c.latest || {};
      rows.push([s.label, c.name || p.name || p.id, c.registration_id || p.registration_id || "", (c.sic || []).join(" "), c.mode || "",
        L.revenue ? L.revenue.value : "not available", L.revenue ? src(L.revenue, c) : "", L.net_assets ? L.net_assets.value : "not available", L.net_assets ? src(L.net_assets, c) : "",
        "not_reached (Phase 2)", c.owner_dob ? D.ownerAge(c) : "not_observable", c.freshest_period || "", c.freshest_filed || "",
        c.id ? D.observations(c).map((o) => `${o.key}${o.date ? "@" + o.date : ""}`).join("; ") || "none" : "",
        p.notes || "", D.fmtDate(p.added_at), D.fmtDate(p.updated_at), c.registration_id ? D.companyUrl(c.registration_id) : ""]);
    }
    D.csvDownload(`pipeline-${D.SITE.run_id || "run"}.csv`, rows);
  }

  draw();
})();
