/* COMPARE — up to four companies side by side. Same rules as everywhere:
 * filed figures with their periods and filed dates, derived figures
 * not_reached, absence with its cause. The selection is the browser's
 * (⇄ on the screen or a company page) or an ?ids= link.
 */
(async function () {
  "use strict";
  const D = window.DOE;
  const { $, $$, esc, nf, state } = D;
  const root = $("#compare-root");
  D.shell({ title: "Compare", crumb: "Side by side — every value keeps its period, filed date and trace" });
  if (!D.SITE.store_present) { D.emptyStore(root); return; }

  const qp = new URLSearchParams(location.search);
  let ids = (qp.get("ids") || "").split(",").filter(Boolean).slice(0, 4);
  if (ids.length) D.compareSel.set(ids); else ids = D.compareSel.all();

  let ix, recs;
  try {
    ix = await D.data.index();
    recs = await Promise.all(ids.map((id) => D.data.company(id)));
  } catch (e) { D.loadError(root, e); return; }
  const items = ids.map((id, i) => ({ id, rec: recs[i], row: ix.byId[id] })).filter((x) => x.rec && x.row);
  if (!items.length) {
    root.innerHTML = `<div class="empty"><strong>Nothing to compare.</strong> Pick up to four companies on the
      <a href="screen.html">screen</a> with the ⇄ control (or <kbd>c</kbd> on a focused row), then come back here.</div>`;
    return;
  }
  history.replaceState(null, "", "compare.html?ids=" + items.map((x) => encodeURIComponent(x.id)).join(","));
  $("#title-side").innerHTML = `<button class="tw" id="export-cmp" title="Excel-compatible CSV of this comparison with sources">⬇ comparison (CSV)</button>`;

  const cur = (rec, concept) => rec.figures.filter((f) => f.is_current && f.concept === concept && !Object.keys(f.dimensions || {}).length)
    .sort((a, b) => String(b.period_end).localeCompare(String(a.period_end)))[0] || null;
  const figCell = (x, f, fallbackConcept) => f
    ? `<a href="${D.traceHref(f.id, x.id)}">${esc(D.figDisplay(f))}</a><div class="sub">${esc(f.period_end)}${docOf(x, f) ? ` · filed ${esc(docOf(x, f).filed_date)}` : ""}</div>`
    : (() => { const fact = x.rec.coverage.find((c) => c.concept === fallbackConcept); return fact ? state(fact.status, fact.detail || undefined) : state("not_captured"); })();
  const docOf = (x, f) => x.rec.documents.find((d) => d.id === f.source_document_id);
  const oa = (x) => D.ownerAge(x.row);

  const LINES = [
    ["Registration", (x) => `<a href="${D.companyUrl(x.rec.company.registration_id)}" rel="noopener">${esc(x.rec.company.registration_id)}</a> · ${esc(x.rec.company.status || "")}`],
    ["Incorporated", (x) => `${esc(x.rec.company.incorporated || "")} (${D.companyAgeYears(x.rec.company.incorporated) ?? "?"}y)`],
    ["Sector", (x) => D.divisionsOf(x.rec.company.sic).map((d) => esc(D.divName(d))).join("; ") + ` <span class="sic-code">${x.rec.company.sic.map(esc).join(" ")}</span>`],
    ["Region", (x) => esc([x.row.locality, x.row.region, x.row.country].filter(Boolean).join(", "))],
    ["Screening mode", (x) => `<span class="mode ${esc(x.row.mode)}">${esc(x.row.mode)}</span>`],
    ["Ownership class", (x) => x.row.ownership_classification ? esc(x.row.ownership_classification) : state("not_reached", "Phase 2, fail-closed")],
    ["Freshest figures", (x) => x.row.freshest_period ? `${esc(x.row.freshest_period)}<div class="sub">${D.ageSpan(x.row.freshest_period)}${x.row.freshest_filed ? ` · filed ${esc(x.row.freshest_filed)}` : ""}</div>` : state("not_captured")],
    ["Revenue", (x) => figCell(x, cur(x.rec, "revenue"), "revenue")],
    ["Gross profit", (x) => figCell(x, cur(x.rec, "gross_profit"), "gross_profit")],
    ["Operating profit", (x) => figCell(x, cur(x.rec, "operating_profit"), "operating_profit")],
    ["EBITDA", () => `${state("not_reached")}<div class="sub">derived — Phase 2</div>`],
    ["Margin", () => `${state("not_reached")}<div class="sub">derived — Phase 2</div>`],
    ["Net assets", (x) => figCell(x, cur(x.rec, "net_assets") || cur(x.rec, "equity"), "net_assets")],
    ["Cash", (x) => figCell(x, cur(x.rec, "cash"), "cash")],
    ["Creditors > 1y", (x) => figCell(x, cur(x.rec, "creditors_after_one_year"), "creditors_after_one_year")],
    ["Employees (avg)", (x) => figCell(x, cur(x.rec, "average_employees"), "average_employees")],
    ["Owner age", (x) => oa(x) !== null ? `~${oa(x)}<div class="sub">PSC born ${x.row.owner_dob.year}</div>` : state("not_observable", "no active individual PSC with a published birth year")],
    ["Active PSCs", (x) => `${x.row.active_owners}${x.row.single_owner_75 ? `<div class="sub">single holder 75–100%</div>` : ""}`],
    ["Officers", (x) => `${x.row.officers_active} active of ${x.row.officers_total}<div class="sub">last appointed ${esc(x.row.last_officer_appointed || "—")}</div>`],
    ["Charges", (x) => `${x.row.charges_outstanding} outstanding of ${x.row.charges_total}<div class="sub">last created ${esc(x.row.last_charge_created || "—")}</div>`],
    ["Observed · 12m", (x) => D.observations(x.row).map(D.obsChip).join(" ") || `<span class="quiet">quiet</span>`],
    ["Coverage", (x) => Object.entries(x.row.coverage.statuses || {}).map(([k, v]) => `${k === "available" ? `<span class="state st-available">available</span>` : state(k)} ${v}`).join("<br>")],
    ["Produced by", (x) => esc(x.row.software || "not declared")],
    ["Pipeline", (x) => { const p = D.pipeline.get(x.id); return p ? `<span class="stage-chip">${esc(D.STAGES.find((s) => s.key === p.stage).label)}</span>` : `<span class="quiet">—</span>`; }],
  ];

  root.innerHTML = `<table class="cmp"><thead><tr><th></th>${items.map((x) => `<th>
      <a class="cmp-name" href="${D.companyHref(x.id)}">${esc(x.rec.company.name)}</a>
      <div class="sub"><span class="act star ${D.watch.has(x.id) ? "on" : ""}" data-star="${esc(x.id)}" title="watchlist">★</span>
      <a href="#" data-remove="${esc(x.id)}" class="quiet" title="remove from compare">remove</a></div></th>`).join("")}</tr></thead>
    <tbody>${LINES.map(([label, fn]) => `<tr><th>${esc(label)}</th>${items.map((x) => `<td>${fn(x)}</td>`).join("")}</tr>`).join("")}</tbody></table>
    <p class="note">${items.length < 4 ? `Room for ${4 - items.length} more — add from the <a href="screen.html">screen</a>.` : "Four is the limit: a comparison wider than a page stops being one."}</p>`;

  $$("[data-star]").forEach((el) => el.addEventListener("click", () => el.classList.toggle("on", D.watch.toggle(el.dataset.star))));
  $$("[data-remove]").forEach((el) => el.addEventListener("click", (e) => {
    e.preventDefault(); D.compareSel.toggle(el.dataset.remove);
    location.href = "compare.html";
  }));
  $("#export-cmp").addEventListener("click", () => {
    const strip = (html) => html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    const rows = [["line", ...items.map((x) => x.rec.company.name)]];
    for (const [label, fn] of LINES) rows.push([label, ...items.map((x) => strip(fn(x)))]);
    for (const concept of ["revenue", "gross_profit", "operating_profit", "net_assets", "cash", "creditors_after_one_year", "average_employees"]) {
      rows.push([`${concept} source`, ...items.map((x) => { const f = cur(x.rec, concept); const d = f && docOf(x, f);
        return f ? `${f.source_tag} | period end ${f.period_end} | filed ${d ? d.filed_date : "?"} | ${d ? D.filingUrl(x.rec.company.registration_id, d.transaction_id) : ""} | ${f.id}` : "no current figure"; })]);
    }
    rows.push(["register", ...items.map((x) => D.companyUrl(x.rec.company.registration_id))]);
    D.csvDownload(`compare-${D.SITE.run_id || "run"}.csv`, rows);
  });
})();
