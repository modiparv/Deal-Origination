/* SCREEN — thesis builder over the whole store.
 *
 * The URL is the state: every filter change rewrites the query string,
 * so a screen is shareable by link and a saved screen is just a name
 * for a query string. The three-way count rule: when a filter tests a
 * concept a company lacks, that company is neither matched nor failed —
 * it lands in "could not be measured", always shown, one click to view.
 */
(async function () {
  "use strict";
  const D = window.DOE;
  const { $, $$, esc, nf } = D;
  D.shell({ title: "Screen", crumb: "Every figure traces to a filing; unmeasurable companies are counted, never dropped" });

  const results = $("#results");
  if (!D.SITE.store_present) { D.emptyStore(results); $("#countblock").innerHTML = ""; return; }
  let ix;
  try { ix = await D.data.index(); } catch (e) { D.loadError(results, e); return; }
  const ROWS = ix.companies;
  const PAGE = 150;

  // ---- filter panel population (from the data, never typed in) ----
  const divisions = {};
  for (const c of ROWS) for (const d of D.divisionsOf(c.sic)) divisions[d] = (divisions[d] || 0) + 1;
  $("#f-sectors").innerHTML = Object.keys(divisions).sort((a, b) => divisions[b] - divisions[a] || a.localeCompare(b))
    .map((d) => `<label><input type="checkbox" data-div="${d}"> ${esc(D.divName(d))} <span class="sic-code">${d}</span><span class="n">${nf.format(divisions[d])}</span></label>`).join("");
  $("#f-sectors-hint").textContent = `${Object.keys(divisions).length} divisions`;
  const countries = [...new Set(ROWS.map((c) => c.country).filter(Boolean))].sort();
  $("#f-country").innerHTML = `<option value="">any country</option>` + countries.map((x) => `<option>${esc(x)}</option>`).join("");

  // ---- UI ⇄ filter object ----
  function readUI() {
    const p = new URLSearchParams();
    const set = (k, v) => { if (v !== "" && v !== null && v !== undefined) p.set(k, v); };
    set("q", $("#f-q").value.trim());
    set("divs", $$("#f-sectors input:checked").map((i) => i.dataset.div).join(","));
    set("own", $("#f-own").value); set("mode", $("#f-mode").value);
    set("eb_min", $("#f-eb-min").value.trim()); set("eb_max", $("#f-eb-max").value.trim());
    set("rev_min", $("#f-rev-min").value.trim()); set("rev_max", $("#f-rev-max").value.trim());
    set("country", $("#f-country").value); set("loc", $("#f-loc").value.trim());
    set("owner_min", $("#f-owner-min").value.trim()); set("stale", $("#f-stale").value.trim());
    if ($("#chip-nosucc").classList.contains("on")) p.set("nosucc", "1");
    if ($("#chip-single75").classList.contains("on")) p.set("single75", "1");
    const obs = $$(".chip[data-obs].on").map((ch) => ch.dataset.obs);
    if (obs.length) p.set("obs", obs.join(","));
    return D.parseFilters(p);
  }
  function writeUI(f) {
    $("#f-q").value = f.q;
    $$("#f-sectors input").forEach((i) => { i.checked = f.divs.includes(i.dataset.div); });
    $("#f-own").value = f.own; $("#f-mode").value = f.mode;
    $("#f-eb-min").value = f.ebMin ?? ""; $("#f-eb-max").value = f.ebMax ?? "";
    $("#f-rev-min").value = f.revMin ?? ""; $("#f-rev-max").value = f.revMax ?? "";
    $("#f-country").value = countries.includes(f.country) ? f.country : "";
    $("#f-loc").value = f.loc;
    $("#f-owner-min").value = f.ownerMin ?? ""; $("#f-stale").value = f.staleMax ?? "";
    $("#chip-nosucc").classList.toggle("on", f.nosucc);
    $("#chip-single75").classList.toggle("on", f.single75);
    $("#chip-fresh18").classList.toggle("on", f.staleMax === 18);
    $$(".chip[data-obs]").forEach((ch) => ch.classList.toggle("on", f.obs.includes(ch.dataset.obs)));
  }

  // ---- state ----
  let view = "pass";
  let shown = PAGE;
  const sort = { key: "name", dir: 1 };
  let focusIdx = -1;
  let lastRows = [];

  const sortVal = (c, k) => {
    switch (k) {
      case "name": return c.name;
      case "sector": return D.divName(D.divisionsOf(c.sic)[0]);
      case "revenue": return c.latest.revenue ? Number(c.latest.revenue.value) : -Infinity;
      case "net_assets": return c.latest.net_assets ? Number(c.latest.net_assets.value) : -Infinity;
      case "owner": { const a = D.ownerAge(c); return a === null ? -Infinity : a; }
      case "filed": return c.freshest_filed || "";
      case "obs": return D.observations(c).length;
      default: return "";
    }
  };

  function draw() {
    focusIdx = -1; // rows are rebuilt; a stale index must never navigate
    const f = readUI();
    const params = D.filtersToParams(f);
    history.replaceState(null, "", location.pathname + (params.toString() ? "?" + params : ""));
    const b = D.bucketise(ROWS, f);
    const uni = D.SITE.universe_hits;

    const saved = D.screens.all();
    $("#countblock").innerHTML = `
      <div class="headcount"><span class="big">${nf.format(b.pass.length)}</span>
        <span class="of">of ${nf.format(ROWS.length)} companies in the store${uni ? ` · ${nf.format(uni)} in the mandate universe (advanced search)` : ""}</span>
        <span class="filters-desc" title="What this screen tests">${esc(D.describeFilters(f))}</span></div>
      <div class="threeway">
        <button class="tw ${view === "pass" ? "on" : ""}" data-view="pass"><span class="tick">✓</span> ${nf.format(b.pass.length)} matched</button>
        <button class="tw ${view === "fail" ? "on" : ""}" data-view="fail"><span class="cross">✕</span> ${nf.format(b.fail.length)} failed the test</button>
        <button class="tw warn ${view === "unmeasurable" ? "on" : ""}" data-view="unmeasurable"><span class="warnmark">⚠</span> ${nf.format(b.unmeasurable.length)} could not be measured</button>
        <span class="saved">
          <select id="saved-select" title="Saved screens (this browser)"><option value="">saved screens${saved.length ? ` (${saved.length})` : ""}…</option>
            ${saved.map((s) => `<option value="${esc(s.id)}">${esc(s.name)}</option>`).join("")}</select>
          <button class="tw" id="save-screen" title="Name and keep this filter set">save</button>
          ${saved.length ? `<button class="tw" id="del-screen" title="Delete the selected saved screen">delete</button>` : ""}
        </span>
        <button id="export-csv" class="tw" title="Excel-compatible CSV of the current view; every figure column is followed by its source column">⬇ export (Excel CSV)</button>
      </div>`;
    $$(".tw[data-view]").forEach((btn) => btn.addEventListener("click", () => { view = btn.dataset.view; shown = PAGE; draw(); }));
    $("#export-csv").addEventListener("click", () => exportCsv(b[view], f));
    $("#save-screen").addEventListener("click", () => {
      if (D.isEmptyFilters(f)) { D.toast("Set at least one filter before saving"); return; }
      const name = prompt("Name this screen (stored in this browser only):", D.describeFilters(f).slice(0, 60));
      if (!name) return;
      D.screens.save(name.trim(), params.toString());
      D.toast(`Saved “${name.trim()}”`); draw();
    });
    $("#saved-select").addEventListener("change", (e) => {
      const s = saved.find((x) => x.id === e.target.value);
      if (!s) return;
      writeUI(D.parseFilters(s.params)); shown = PAGE; draw();
    });
    const del = $("#del-screen");
    if (del) del.addEventListener("click", () => {
      const sel = $("#saved-select").value;
      if (!sel) { D.toast("Select a saved screen first"); return; }
      D.screens.remove(sel); D.toast("Deleted"); draw();
    });

    const rows = b[view].slice().sort((x, y) => {
      const A = sortVal(x, sort.key), B = sortVal(y, sort.key);
      return (A < B ? -1 : A > B ? 1 : 0) * sort.dir;
    });
    lastRows = rows;
    const page = rows.slice(0, shown);
    const arrow = (k) => (sort.key === k ? `<span class="dir">${sort.dir > 0 ? "▲" : "▼"}</span>` : "");
    const th = (k, label, cls = "", title = "") => k
      ? `<th class="sortable ${cls}" data-key="${k}" title="${esc(title)}">${label} ${arrow(k)}</th>`
      : `<th class="${cls}" title="${esc(title)}">${label}</th>`;
    const w = D.watch.all(), cmp = new Set(D.compareSel.all()), pipe = D.pipeline.all();

    if (!rows.length) {
      results.innerHTML = `<div class="empty">No companies in this bucket for the current filters.</div>`;
      return;
    }
    results.innerHTML = `<table id="rt"><thead><tr>
        <th class="acts"></th>${th("name", "Company")}${th("sector", "Sector")}
        ${th("revenue", "Revenue", "num")}<th class="num" title="Derived figure — Phase 2. Not sortable: no value exists for any company yet.">EBITDA</th>
        <th class="num" title="Derived figure — Phase 2. Not sortable: no value exists for any company yet.">Margin</th>
        ${th("net_assets", "Net assets", "num")}${th("owner", "Owner age", "num", "Oldest active individual PSC, from the register's birth month/year — approximate")}
        ${th("filed", "Filed", "", "Filed date of the document behind the freshest current figure")}
        ${th("obs", "Observed · 12m", "", "Register events observed in the last 12 months — what happened, dated; never what it means")}
      </tr></thead><tbody>${page.map((c, i) => {
        const rev = c.latest.revenue, na = c.latest.net_assets;
        const oa = D.ownerAge(c);
        const fa = D.ageInfo(c.freshest_period);
        const obs = D.observations(c);
        const st = pipe[c.id];
        return `<tr data-cid="${esc(c.id)}" data-i="${i}">
          <td class="acts">
            <span class="act star ${w.has(c.id) ? "on" : ""}" data-star="${esc(c.id)}" title="watchlist (w)">★</span>
            <span class="act cmp ${cmp.has(c.id) ? "on" : ""}" data-cmp="${esc(c.id)}" title="compare, up to four (c)">⇄</span>
            <span class="act pipe ${st ? "on" : ""}" data-pipe="${esc(c.id)}" title="${st ? `in pipeline: ${esc(st.stage)}` : "add to pipeline (p)"}">${st ? "●" : "+"}</span>
          </td>
          <td class="co-name"><a href="${D.companyHref(c.id)}">${esc(c.name)}</a><br><span class="co-reg">${esc(c.registration_id)}</span>${c.mode !== "financial" ? ` <span class="mode ${esc(c.mode)}" title="screening mode">${esc(c.mode)}</span>` : ""}</td>
          <td><span class="sic-label">${esc(D.divName(D.divisionsOf(c.sic)[0]))}${D.divisionsOf(c.sic).length > 1 ? " +" + (D.divisionsOf(c.sic).length - 1) : ""}</span></td>
          <td class="num">${rev ? `<a href="${D.traceHref(rev.figure_id, c.id)}" title="period end ${esc(rev.period_end)} · filed ${esc(rev.filed_date)} — trace to source filing">${esc(D.refDisplay(rev, "revenue"))}</a>` : D.causeFromCounts(c)}</td>
          <td class="num">${D.notDerived()}</td>
          <td class="num">${D.notDerived()}</td>
          <td class="num">${na ? `<a href="${D.traceHref(na.figure_id, c.id)}" title="period end ${esc(na.period_end)} · filed ${esc(na.filed_date)}">${esc(D.refDisplay(na, "net_assets"))}</a>` : D.causeFromCounts(c)}</td>
          <td class="num">${oa !== null ? "~" + oa : `<span class="state st-not_observable" title="not_observable — no active individual PSC with a published birth year">no PSC dob</span>`}</td>
          <td class="filed">${c.freshest_filed ? `<span class="${fa && fa.stale ? "filed-stale" : ""}">${esc(c.freshest_filed)}</span>${fa && fa.stale ? ` <span class="age stale" title="period end ${esc(c.freshest_period)}">stale</span>` : ""}` : D.causeFromCounts(c)}</td>
          <td class="obs-cell">${obs.slice(0, 3).map(D.obsChip).join(" ")}${obs.length > 3 ? ` <span class="obs more">+${obs.length - 3}</span>` : ""}${!obs.length ? `<span class="quiet" title="No register events in the observation window">quiet</span>` : ""}</td>
        </tr>`;
      }).join("")}</tbody></table>
      ${rows.length > shown ? `<div class="pager">Showing ${nf.format(shown)} of ${nf.format(rows.length)} ·
        <button class="tw" id="more">show ${nf.format(Math.min(PAGE, rows.length - shown))} more</button>
        <button class="tw" id="all">show all ${nf.format(rows.length)}</button></div>`
        : `<div class="pager">${nf.format(rows.length)} row(s)</div>`}`;

    $$("#rt th.sortable").forEach((el) => el.addEventListener("click", () => {
      const k = el.dataset.key;
      if (sort.key === k) sort.dir *= -1; else { sort.key = k; sort.dir = k === "name" || k === "sector" ? 1 : -1; }
      draw();
    }));
    const more = $("#more"), all = $("#all");
    if (more) more.addEventListener("click", () => { shown += PAGE; draw(); });
    if (all) all.addEventListener("click", () => { shown = rows.length; draw(); });
    $$("[data-star]").forEach((el) => el.addEventListener("click", (e) => { e.stopPropagation(); el.classList.toggle("on", D.watch.toggle(el.dataset.star)); }));
    $$("[data-cmp]").forEach((el) => el.addEventListener("click", (e) => { e.stopPropagation(); toggleCompare(el.dataset.cmp, el); }));
    $$("[data-pipe]").forEach((el) => el.addEventListener("click", (e) => { e.stopPropagation(); addPipe(el.dataset.pipe, el); }));
    $$("#rt tbody tr").forEach((tr) => tr.addEventListener("click", (e) => {
      if (e.target.closest("a") || e.target.closest(".act")) return;
      location.href = D.companyHref(tr.dataset.cid);
    }));
  }

  function toggleCompare(cid, el) {
    const r = D.compareSel.toggle(cid);
    if (!r.ok) { D.toast("Compare holds four companies — remove one first"); return; }
    if (el) el.classList.toggle("on", r.list.includes(cid));
    D.refreshCompareBadge();
    D.toast(r.list.includes(cid) ? `Compare: ${r.list.length} of 4` : "Removed from compare");
  }
  function addPipe(cid, el) {
    const c = ix.byId[cid];
    if (D.pipeline.get(cid)) { location.href = "pipeline.html"; return; }
    D.pipeline.add(cid, { name: c.name, registration_id: c.registration_id });
    if (el) { el.classList.add("on"); el.textContent = "●"; el.title = "in pipeline: identified"; }
    D.toast(`${c.name} → pipeline (identified)`);
  }

  // Excel-compatible CSV: every figure column is followed by a source
  // column carrying the register document link, filed date and tag —
  // an export that loses provenance defeats the product.
  function exportCsv(rows, f) {
    const src = (ref, c) => ref
      ? `figure ${ref.figure_id} | period end ${ref.period_end} | filed ${ref.filed_date} | ${D.companyUrl(c.registration_id)}/filing-history`
      : "";
    const cause = (c) => {
      const s = (c.coverage && c.coverage.statuses) || {};
      return Object.entries(s).map(([k, v]) => `${k}:${v}`).join(" ") || "not_captured";
    };
    const header = ["company", "registration", "status", "sector (SIC)", "screening_mode", "revenue", "revenue_source",
      "EBITDA", "EBITDA_source", "margin", "margin_source", "net_assets", "net_assets_source", "employees", "employees_source",
      "owner_age_approx", "owner_age_source", "freshest_period_end", "filed_date", "months_old",
      "observed_12m", "charges_outstanding", "officers_active", "active_pscs", "first_seen_run", "register_url", "screen"];
    const lines = [header];
    for (const c of rows) {
      const L = c.latest, oa = D.ownerAge(c), fa = D.ageInfo(c.freshest_period);
      lines.push([
        c.name, c.registration_id, c.status || "", c.sic.join(" "), c.mode,
        L.revenue ? L.revenue.value : cause(c), L.revenue ? src(L.revenue, c) : cause(c),
        "not_reached", "derived figures are Phase 2 — no value exists",
        "not_reached", "derived figures are Phase 2 — no value exists",
        L.net_assets ? L.net_assets.value : cause(c), L.net_assets ? src(L.net_assets, c) : cause(c),
        L.employees ? L.employees.value : cause(c), L.employees ? src(L.employees, c) : cause(c),
        oa !== null ? oa : "not_observable",
        oa !== null ? `PSC register birth ${c.owner_dob.year}-${String(c.owner_dob.month || "").padStart(2, "0")} (approximate)` : "no active individual PSC with published birth year",
        c.freshest_period || "", c.freshest_filed || "", fa ? fa.months : "",
        D.observations(c).map((o) => `${o.key}${o.date ? "@" + o.date : ""}`).join("; ") || "none",
        c.charges_outstanding, c.officers_active, c.active_owners, c.first_seen || "",
        D.companyUrl(c.registration_id), D.describeFilters(f),
      ]);
    }
    D.csvDownload(`screen-${view}-${D.SITE.run_id || "run"}.csv`, lines);
  }

  // ---- controls ----
  $$(".chip[data-toggle], .chip[data-obs]").forEach((ch) => ch.addEventListener("click", () => { ch.classList.toggle("on"); shown = PAGE; draw(); }));
  $("#chip-fresh18").addEventListener("click", () => {
    $("#f-stale").value = $("#f-stale").value === "18" ? "" : "18";
    $("#chip-fresh18").classList.toggle("on", $("#f-stale").value === "18");
    shown = PAGE; draw();
  });
  $$(".fpanel input, .fpanel select").forEach((el) =>
    el.addEventListener(["text", "number", "search"].includes(el.type) ? "input" : "change", () => { shown = PAGE; draw(); }));
  $("#f-clear").addEventListener("click", (e) => { e.preventDefault(); writeUI(D.parseFilters("")); shown = PAGE; draw(); });

  // keyboard: rows
  document.addEventListener("keydown", (e) => {
    if (["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement.tagName)) return;
    const trs = $$("#rt tbody tr");
    if (!trs.length) return;
    const focused = () => (focusIdx >= 0 ? trs[focusIdx] : null);
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      focusIdx = Math.min(trs.length - 1, Math.max(0, focusIdx + (e.key === "ArrowDown" ? 1 : -1)));
      trs.forEach((r) => r.classList.remove("focus"));
      trs[focusIdx].classList.add("focus");
      trs[focusIdx].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter" && focused()) {
      location.href = D.companyHref(focused().dataset.cid);
    } else if (e.key === "w" && focused()) {
      const el = focused().querySelector("[data-star]"); el.classList.toggle("on", D.watch.toggle(el.dataset.star));
    } else if (e.key === "c" && focused()) {
      toggleCompare(focused().dataset.cid, focused().querySelector("[data-cmp]"));
    } else if (e.key === "p" && focused()) {
      addPipe(focused().dataset.cid, focused().querySelector("[data-pipe]"));
    }
  });

  writeUI(D.parseFilters(location.search));
  draw();
})();
