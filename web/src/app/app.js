/* Product surface: SCREEN (thesis builder), COMPANY (deep dive), TRACE.
 *
 * Read-only over the exported run dataset (window.__DEMO__). Every value
 * rendered is a verbatim field, a mechanical aggregate, or mechanical
 * date arithmetic (ages, staleness) over public register facts. Nothing
 * financial is computed here: EBITDA, margins, growth, gearing and
 * scores are Phase 2 derived figures — until they exist they render as
 * not_reached, and filters that would need them are shown inert.
 *
 * The three-way count rule: when a filter tests a concept a company
 * lacks, that company is neither matched nor failed — it lands in
 * "could not be measured", always shown, one click to view. A filter
 * that silently drops unmeasurable companies lies by omission.
 */
(function () {
  "use strict";

  const DATA = window.__DEMO__;
  const DIV = window.__SIC_DIVISIONS__ || {};
  const $ = (s) => document.querySelector(s);
  const THIS_YEAR = new Date().getFullYear();

  const esc = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[c]);

  const STATES = {
    filed_without_concept: "The filed accounts regime legitimately omits this concept (e.g. micro-entity accounts carry no P&L).",
    unparseable_format: "A filing exists but the registry offers no machine-readable rendition (PDF only).",
    parse_failed: "A machine-readable document exists but failed to parse — a system defect, never a data limitation.",
    not_reached: "Not yet computed: screening scores, flags and derived metrics (EBITDA, margin, growth, gearing) are Phase 2 and have not run.",
    not_captured: "Outside the fetched window — ingest retrieves the three most recent account documents per company.",
    skipped_mode: "Rubric dimension skipped: requires financial mode; this company screens in signal mode.",
    not_observable: "Not observable from public registry data for this company.",
  };
  const state = (code, extra) =>
    `<span class="state st-${esc(code)}" title="${esc(extra || STATES[code] || "")}">${esc(code)}</span>`;

  const nf = new Intl.NumberFormat("en-GB");
  function money(fig) {
    const cur = fig.currency || (fig.unit === "GBP" ? "GBP" : null);
    const sym = cur === "GBP" ? "£" : cur ? cur + " " : "";
    const v = Number(fig.value), neg = v < 0, abs = Math.abs(v);
    return (neg ? "−" : "") + sym + (Number.isInteger(v) ? nf.format(abs) : String(abs));
  }
  const plain = (f) => (Number.isInteger(Number(f.value)) ? nf.format(Number(f.value)) : String(f.value));
  const figDisplay = (f) => (f.concept === "average_employees" ? plain(f) : money(f));

  function ageInfo(dateStr) {
    if (!dateStr) return null;
    const months = Math.max(0, Math.round((Date.now() - new Date(dateStr).getTime()) / 2629800000));
    const y = Math.floor(months / 12), m = months % 12;
    return { months, label: y ? `${y}y ${m}m` : `${m}m`, stale: months > 24 };
  }
  const ageSpan = (d) => {
    const a = ageInfo(d);
    if (!a) return state("not_captured");
    return `<span class="age${a.stale ? " stale" : ""}">${a.label}<span class="unit"> old${a.stale ? " · stale" : ""}</span></span>`;
  };
  const basisBadge = (f) => `<span class="basis" title="basis: ${esc(f.basis)} — stored verbatim">${esc(f.basis)}</span>`;

  const CH = "https://find-and-update.company-information.service.gov.uk";
  const companyUrl = (reg) => `${CH}/company/${encodeURIComponent(reg)}`;
  const filingHistoryUrl = (reg) => `${companyUrl(reg)}/filing-history`;
  const documentUrl = (reg, txn) =>
    txn ? `${filingHistoryUrl(reg)}/${encodeURIComponent(txn)}/document?format=xhtml` : null;

  const companiesById = Object.fromEntries(DATA.companies.map((c) => [c.id, c]));
  const figuresOf = (cid) => (DATA.figures_by_company[cid] || []).map((id) => DATA.figures[id]);
  const coverageOf = (cid) => DATA.coverage[cid] || [];
  const doc = (id) => DATA.documents[id];
  const fig = (id) => (id ? DATA.figures[id] : null);
  const traceHref = (id) => `trace.html?fig=${encodeURIComponent(id)}`;
  const companyHref = (cid) => `company.html?id=${encodeURIComponent(cid)}`;
  const figCell = (f) => `<a href="${traceHref(f.id)}" title="trace to source filing">${esc(figDisplay(f))}</a>${basisBadge(f)}`;

  // Mechanical register facts (date arithmetic only — no financials)
  function ownerAge(c) {
    // Oldest ACTIVE individual beneficial owner with a published birth
    // year (PSC data carries month/year only). Approximate by year.
    const years = (c.beneficial_owners || [])
      .filter((b) => !b.ceased_on && b.dob_year)
      .map((b) => THIS_YEAR - b.dob_year);
    return years.length ? Math.max(...years) : null;
  }
  const outstandingCharges = (c) =>
    (c.charges["outstanding"] || 0) + (c.charges["part-satisfied"] || 0);
  const companyAgeYears = (c) =>
    c.incorporated ? Math.floor((Date.now() - new Date(c.incorporated).getTime()) / 31557600000) : null;
  const region = (c) => c.address || {};
  const divisionsOf = (c) => [...new Set(c.sic.map((s) => String(s).slice(0, 2)))];
  const divName = (d) => DIV[d] || `division ${d}`;

  function coverageState(cid, concept) {
    const f = coverageOf(cid).find((x) => x.concept === concept);
    return f ? state(f.status, f.detail || undefined) : state("not_captured");
  }

  // watchlist (local, this browser only)
  const WATCH_KEY = "doe.watchlist";
  const watch = () => new Set(JSON.parse(localStorage.getItem(WATCH_KEY) || "[]"));
  const toggleWatch = (cid) => {
    const w = watch();
    w.has(cid) ? w.delete(cid) : w.add(cid);
    localStorage.setItem(WATCH_KEY, JSON.stringify([...w]));
    return w.has(cid);
  };

  function footer() {
    const el = $("#app-footer");
    if (!el) return;
    el.innerHTML =
      `Dataset: ingest run <code>${esc(DATA.run.run_id || "?")}</code> · every figure is a filed
       observation citing its source document, period end and filed date; nothing on this surface is
       computed by a language model. Filed registry data is 9–21 months stale by construction; each
       figure shows its own age. Owner and officer ages are approximate (the register publishes
       birth month/year only). <a href="../">engine home</a> · <a href="../ops/">operations</a>`;
  }

  // ====================================================================
  // SCREEN — thesis builder
  // ====================================================================
  function renderScreen() {
    if (!DATA.companies.length) {
      $("#results").innerHTML = `<div class="empty"><strong>No companies in the store.</strong>
        This surface renders only verified ingest output. Run an ingest (Actions → ingest) and redeploy.</div>`;
      return;
    }

    // ---- filter rail ----
    const divisions = {};
    for (const c of DATA.companies)
      for (const d of divisionsOf(c)) divisions[d] = (divisions[d] || 0) + 1;
    $("#f-sectors").innerHTML = Object.keys(divisions).sort()
      .map((d) => `<label><input type="checkbox" data-div="${d}"> ${esc(divName(d))}
                   <span class="n">${divisions[d]}</span></label>`).join("");

    const countries = [...new Set(DATA.companies.map((c) => region(c).country).filter(Boolean))].sort();
    $("#f-country").innerHTML = `<option value="">any country</option>` +
      countries.map((x) => `<option>${esc(x)}</option>`).join("");

    const F = () => ({
      q: $("#f-q").value.trim().toLowerCase(),
      divs: [...document.querySelectorAll("#f-sectors input:checked")].map((i) => i.dataset.div),
      revMin: num("#f-rev-min"), revMax: num("#f-rev-max"),
      empMin: num("#f-emp-min"), empMax: num("#f-emp-max"),
      naMin: num("#f-na-min"), naMax: num("#f-na-max"),
      country: $("#f-country").value, locality: $("#f-locality").value.trim().toLowerCase(),
      ageMin: num("#f-age-min"), ageMax: num("#f-age-max"),
      ownerMin: num("#f-owner-min"),
      mode: $("#f-mode").value,
      chargesSel: $("#f-charges").value,
      staleMax: num("#f-stale"),
      watchOnly: $("#f-watch").checked,
    });
    const num = (sel) => { const v = $(sel).value.trim(); return v === "" ? null : Number(v); };

    // Each active test returns 'pass' | 'fail' | 'unmeasurable'.
    function evaluate(c, f) {
      const tests = [];
      if (f.q) tests.push(c.name.toLowerCase().includes(f.q) || c.registration_id.toLowerCase().includes(f.q) ? "pass" : "fail");
      if (f.divs.length) tests.push(divisionsOf(c).some((d) => f.divs.includes(d)) ? "pass" : "fail");
      const band = (figId, min, max) => {
        if (min === null && max === null) return null;
        const g = fig(figId);
        if (!g) return "unmeasurable";
        const v = Number(g.value);
        return (min === null || v >= min) && (max === null || v <= max) ? "pass" : "fail";
      };
      const t1 = band(c.latest_revenue_fig, f.revMin, f.revMax); if (t1) tests.push(t1);
      const t2 = band(c.latest_employees_fig, f.empMin, f.empMax); if (t2) tests.push(t2);
      const t3 = band(c.latest_net_assets_fig, f.naMin, f.naMax); if (t3) tests.push(t3);
      if (f.country || f.locality) {
        const a = region(c);
        if (!a.country && !a.locality) tests.push("unmeasurable");
        else tests.push(
          (!f.country || a.country === f.country) &&
          (!f.locality || String(a.locality || "").toLowerCase().includes(f.locality)) ? "pass" : "fail");
      }
      if (f.ageMin !== null || f.ageMax !== null) {
        const y = companyAgeYears(c);
        tests.push(y === null ? "unmeasurable"
          : (f.ageMin === null || y >= f.ageMin) && (f.ageMax === null || y <= f.ageMax) ? "pass" : "fail");
      }
      if (f.ownerMin !== null) {
        const a = ownerAge(c);
        tests.push(a === null ? "unmeasurable" : a >= f.ownerMin ? "pass" : "fail");
      }
      if (f.mode) tests.push(c.mode === f.mode ? "pass" : "fail");
      if (f.chargesSel) {
        const n = outstandingCharges(c);
        tests.push(f.chargesSel === "yes" ? (n > 0 ? "pass" : "fail") : (n === 0 ? "pass" : "fail"));
      }
      if (f.staleMax !== null) {
        const a = ageInfo(c.freshest_period);
        tests.push(!a ? "unmeasurable" : a.months <= f.staleMax ? "pass" : "fail");
      }
      if (f.watchOnly) tests.push(watch().has(c.id) ? "pass" : "fail");
      if (tests.includes("fail")) return "fail";
      if (tests.includes("unmeasurable")) return "unmeasurable";
      return "pass";
    }

    let view = "pass"; // pass | fail | unmeasurable
    const sort = { key: "name", dir: 1 };
    const sortVal = (c, k) => {
      switch (k) {
        case "name": return c.name;
        case "revenue": { const g = fig(c.latest_revenue_fig); return g ? Number(g.value) : -Infinity; }
        case "employees": { const g = fig(c.latest_employees_fig); return g ? Number(g.value) : -Infinity; }
        case "net_assets": { const g = fig(c.latest_net_assets_fig); return g ? Number(g.value) : -Infinity; }
        case "owner": { const a = ownerAge(c); return a === null ? -Infinity : a; }
        case "fresh": return c.freshest_period || "";
        case "mode": return c.mode;
        case "coverage": return c.coverage.statuses.available || 0;
        default: return "";
      }
    };

    let focusIdx = -1;
    function draw() {
      const f = F();
      const buckets = { pass: [], fail: [], unmeasurable: [] };
      for (const c of DATA.companies) buckets[evaluate(c, f)].push(c);
      const uni = window.__SITE__ && window.__SITE__.universe_hits;

      $("#countbar").innerHTML = `
        <span class="big">${nf.format(buckets.pass.length)}</span>
        <span class="of">matched of ${nf.format(DATA.companies.length)} ingested${uni ? ` (universe ${nf.format(uni)})` : ""}</span>
        <span class="split"><b>${nf.format(buckets.fail.length)}</b> failed filters ·
          <b>${nf.format(buckets.unmeasurable.length)}</b> could not be measured</span>
        <button class="viewtab ${view === "pass" ? "on" : ""}" data-view="pass">matched</button>
        <button class="viewtab ${view === "fail" ? "on" : ""}" data-view="fail">failed</button>
        <button class="viewtab ${view === "unmeasurable" ? "on" : ""}" data-view="unmeasurable">not measurable</button>
        <span class="saved">
          <select id="saved-list"><option value="">saved screens…</option>${savedNames()
            .map((n) => `<option>${esc(n)}</option>`).join("")}</select>
          <input id="saved-name" placeholder="name this screen" size="14">
          <button id="saved-save">save</button>
        </span>`;
      document.querySelectorAll(".viewtab").forEach((b) =>
        b.addEventListener("click", () => { view = b.dataset.view; focusIdx = -1; draw(); }));
      $("#saved-save").addEventListener("click", saveScreen);
      $("#saved-list").addEventListener("change", (e) => loadScreen(e.target.value));

      const rows = buckets[view].slice().sort((a, b) => {
        const A = sortVal(a, sort.key), B = sortVal(b, sort.key);
        return (A < B ? -1 : A > B ? 1 : 0) * sort.dir;
      });
      const arrow = (k) => (sort.key === k ? `<span class="dir">${sort.dir > 0 ? "▲" : "▼"}</span>` : "");
      const th = (k, label, cls = "") => `<th class="sortable ${cls}" data-key="${k}">${label} ${arrow(k)}</th>`;
      const w = watch();

      $("#results").innerHTML = `<table id="rt"><thead><tr>
          <th></th>${th("name", "Company")}<th>Sector</th><th>Region</th>
          ${th("revenue", "Revenue", "num")}<th class="num">EBITDA</th><th class="num">Margin</th>
          ${th("employees", "Empl.", "num")}${th("net_assets", "Net assets", "num")}
          ${th("owner", "Owner age", "num")}<th class="num">Score</th>${th("mode", "Mode")}
          ${th("fresh", "Freshest")}${th("coverage", "Cov.", "num")}
        </tr></thead><tbody>${rows.map((c, i) => {
          const rev = fig(c.latest_revenue_fig), emp = fig(c.latest_employees_fig), na = fig(c.latest_net_assets_fig);
          const oa = ownerAge(c), a = region(c);
          const d0 = divisionsOf(c);
          return `<tr data-cid="${esc(c.id)}" data-i="${i}">
            <td><span class="star ${w.has(c.id) ? "on" : ""}" data-star="${esc(c.id)}" title="watchlist">★</span></td>
            <td class="co-name"><a href="${companyHref(c.id)}">${esc(c.name)}</a><br><span class="co-reg">${esc(c.registration_id)}</span></td>
            <td><span class="sic-label">${esc(divName(d0[0]))}${d0.length > 1 ? ` +${d0.length - 1}` : ""}</span><br><span class="sic-code">${c.sic.map(esc).join(" ")}</span></td>
            <td>${esc(a.locality || "")}${a.country ? `<br><span class="sic-code">${esc(a.country)}</span>` : state("not_observable", "no registered address recorded")}</td>
            <td class="num">${rev ? figCell(rev) : coverageState(c.id, "revenue")}</td>
            <td class="num">${state("not_reached")}</td>
            <td class="num">${state("not_reached")}</td>
            <td class="num">${emp ? figCell(emp) : coverageState(c.id, "average_employees")}</td>
            <td class="num">${na ? figCell(na) : coverageState(c.id, "net_assets")}</td>
            <td class="num">${oa !== null ? `~${oa}` : state("not_observable", "no active individual beneficial owner with a published birth year")}</td>
            <td class="num">${state("not_reached")}</td>
            <td><span class="mode ${esc(c.mode)}">${esc(c.mode)}</span></td>
            <td>${c.freshest_period ? `${esc(c.freshest_period)}<br>${ageSpan(c.freshest_period)}` : state("unparseable_format", "no machine-readable figures")}</td>
            <td class="num">${c.coverage.statuses.available || 0}/21</td>
          </tr>`;
        }).join("")}</tbody></table>`;

      document.querySelectorAll("#rt th.sortable").forEach((el) =>
        el.addEventListener("click", () => {
          const k = el.dataset.key;
          if (sort.key === k) sort.dir *= -1; else { sort.key = k; sort.dir = 1; }
          draw();
        }));
      document.querySelectorAll("[data-star]").forEach((el) =>
        el.addEventListener("click", (e) => {
          e.stopPropagation();
          el.classList.toggle("on", toggleWatch(el.dataset.star));
        }));
    }

    // saved screens (local, this browser only)
    const SAVE_KEY = "doe.screens";
    const savedAll = () => JSON.parse(localStorage.getItem(SAVE_KEY) || "{}");
    const savedNames = () => Object.keys(savedAll()).sort();
    function currentInputs() {
      const o = {};
      document.querySelectorAll(".rail input, .rail select").forEach((el) => {
        if (el.type === "checkbox") o[el.dataset.div ? "d:" + el.dataset.div : el.id] = el.checked;
        else o[el.id] = el.value;
      });
      return o;
    }
    function saveScreen() {
      const name = $("#saved-name").value.trim();
      if (!name) return;
      const all = savedAll(); all[name] = currentInputs();
      localStorage.setItem(SAVE_KEY, JSON.stringify(all));
      draw();
    }
    function loadScreen(name) {
      const s = savedAll()[name]; if (!s) return;
      document.querySelectorAll(".rail input, .rail select").forEach((el) => {
        const k = el.dataset.div ? "d:" + el.dataset.div : el.id;
        if (el.type === "checkbox") el.checked = !!s[k];
        else if (k in s) el.value = s[k];
      });
      draw();
    }

    // keyboard navigation on results
    document.addEventListener("keydown", (e) => {
      if (["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement.tagName)) return;
      const rows = [...document.querySelectorAll("#rt tbody tr")];
      if (!rows.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        focusIdx = Math.min(rows.length - 1, Math.max(0, focusIdx + (e.key === "ArrowDown" ? 1 : -1)));
        rows.forEach((r) => r.classList.remove("focus"));
        rows[focusIdx].classList.add("focus");
        rows[focusIdx].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && focusIdx >= 0) {
        location.href = companyHref(rows[focusIdx].dataset.cid);
      }
    });

    document.querySelectorAll(".rail input, .rail select").forEach((el) =>
      el.addEventListener(el.type === "text" || el.type === "number" || el.type === "search" ? "input" : "change", draw));
    $("#f-clear").addEventListener("click", (e) => {
      e.preventDefault();
      document.querySelectorAll(".rail input, .rail select").forEach((el) => {
        if (el.type === "checkbox") el.checked = false; else el.value = "";
      });
      draw();
    });
    draw();
  }

  // ====================================================================
  // COMPANY — deep dive
  // ====================================================================
  const PL = ["revenue", "gross_profit", "operating_profit", "profit_before_tax", "profit_for_period", "staff_costs", "depreciation_amortisation", "tax_charge"];
  const BS = ["fixed_assets", "current_assets", "debtors", "cash", "creditors_within_one_year", "creditors_after_one_year", "net_current_assets", "total_assets_less_current_liabilities", "net_assets", "equity", "share_capital", "retained_earnings"];

  function renderCompany() {
    const cid = new URLSearchParams(location.search).get("id");
    const c = companiesById[cid];
    const root = $("#company-root");
    if (!c) {
      root.innerHTML = `<div class="empty"><strong>Unknown company.</strong> <a href="screen.html">Back to the screen.</a></div>`;
      return;
    }
    document.title = `${c.name} — company`;
    $("#page-title").textContent = c.name;
    $("#crumb").innerHTML = `<a href="screen.html">screen</a> / ${esc(c.name)}`;

    const figs = figuresOf(cid).filter((f) => f.is_current && !Object.keys(f.dimensions || {}).length);
    const periods = [...new Set(figs.map((f) => f.period_end).filter(Boolean))].sort().reverse().slice(0, 6);
    const covPeriod = c.coverage.period_end;
    const cell = (concept, period) => {
      const f = figs.find((x) => x.concept === concept && x.period_end === period);
      if (f) return figCell(f);
      if (period === covPeriod) {
        const fact = coverageOf(cid).find((x) => x.concept === concept);
        if (fact && fact.status !== "available") return state(fact.status, fact.detail || undefined);
      }
      return state("not_captured");
    };
    const matrixRows = (ks) => ks.map((k) =>
      `<tr><td>${esc(k)}</td>${periods.map((p) => `<td class="num">${cell(k, p)}</td>`).join("")}</tr>`).join("");

    const rev = fig(c.latest_revenue_fig), emp = fig(c.latest_employees_fig), na = fig(c.latest_net_assets_fig);
    const oa = ownerAge(c);
    const a = region(c);
    const fresh = c.freshest_period;
    const freshA = ageInfo(fresh);
    const w = watch();

    // Succession read — stated as observations, never inference
    const activeBOs = (c.beneficial_owners || []).filter((b) => !b.ceased_on);
    const activeOff = (c.officers || []).filter((o) => !o.resigned_on);
    const youngest = activeOff.filter((o) => o.dob_year).sort((x, y) => y.dob_year - x.dob_year)[0];
    const recentAppt = activeOff.filter((o) => o.appointed_on && o.appointed_on >= `${THIS_YEAR - 5}-01-01`);
    const singleBO = activeBOs.length === 1 && (activeBOs[0].natures || []).some((n) => String(n).includes("75-to-100"));

    const peerRows = DATA.companies
      .filter((p) => p.id !== cid && divisionsOf(p).some((d) => divisionsOf(c).includes(d)))
      .map((p) => ({ p, na: fig(p.latest_net_assets_fig), rev: fig(p.latest_revenue_fig) }))
      .sort((x, y) => {
        const ref = na ? Number(na.value) : 0;
        const dx = x.na ? Math.abs(Number(x.na.value) - ref) : Infinity;
        const dy = y.na ? Math.abs(Number(y.na.value) - ref) : Infinity;
        return dx - dy;
      }).slice(0, 8);

    root.innerHTML = `
      <div class="fact-strip">
        <span><span class="k">registration</span><a href="${companyUrl(c.registration_id)}">${esc(c.registration_id)}</a> (${esc(c.jurisdiction)})</span>
        <span><span class="k">status</span>${esc(c.status || "unknown")}</span>
        <span><span class="k">incorporated</span>${esc(c.incorporated || "unknown")} (${companyAgeYears(c) ?? "?"}y)</span>
        <span><span class="k">sector</span>${divisionsOf(c).map((d) => esc(divName(d))).join("; ")} <span class="sic-code">${c.sic.map(esc).join(" ")}</span></span>
        <span><span class="k">region</span>${esc(a.locality || "")}${a.country ? ", " + esc(a.country) : ""}</span>
        <span><span class="k">score</span>${state("not_reached", "screening has not run — Phase 2")}</span>
        <span><span class="k">watchlist</span><span class="star ${w.has(cid) ? "on" : ""}" id="watch-toggle">★</span></span>
      </div>
      ${fresh
        ? `<p class="staleness-callout">Freshest machine-readable figures: period end <strong>${esc(fresh)}</strong>
           (${ageSpan(fresh)}). Every figure below carries its own period and traces to its filing.</p>`
        : `<p class="staleness-callout">No machine-readable figures — filings have no iXBRL rendition
           ${state("unparseable_format")}. This company screens in signal mode on observable behaviour only.</p>`}

      <div class="tiles">
        <div class="tile"><div class="value">${rev ? figCell(rev) : coverageState(cid, "revenue")}</div>
          <div class="label">revenue</div><div class="detail">${rev ? esc(rev.period_end) : ""}</div></div>
        <div class="tile"><div class="value">${state("not_reached")}</div>
          <div class="label">EBITDA</div><div class="detail">derived figure — Phase 2</div></div>
        <div class="tile"><div class="value">${state("not_reached")}</div>
          <div class="label">margin</div><div class="detail">derived figure — Phase 2</div></div>
        <div class="tile"><div class="value">${emp ? figCell(emp) : coverageState(cid, "average_employees")}</div>
          <div class="label">employees</div><div class="detail">${emp ? esc(emp.period_end) : ""}</div></div>
        <div class="tile"><div class="value">${oa !== null ? "~" + oa : state("not_observable", "no active individual BO with published birth year")}</div>
          <div class="label">owner age</div><div class="detail">from PSC birth month/year</div></div>
        <div class="tile"><div class="value">${c.ownership_classification ? esc(c.ownership_classification) : state("not_reached")}</div>
          <div class="label">ownership class</div><div class="detail">fail-closed — Phase 2</div></div>
      </div>

      <section>
        <h2>Financial trajectory</h2>
        <p class="note">Filed observations only, current per deterministic supersession; click any value to trace.
        EBITDA, margins and growth are Phase 2 derived figures and render ${state("not_reached")} until the
        derive layer exists — nothing here is approximated in the meantime.</p>
        ${periods.length ? `<table class="matrix">
          <thead><tr><th>concept</th>${periods.map((p) => `<th class="num">${esc(p)}<br>${ageSpan(p)}</th>`).join("")}</tr></thead>
          <tbody>
            <tr><th colspan="${periods.length + 1}">income statement</th></tr>${matrixRows(PL)}
            <tr><th colspan="${periods.length + 1}">balance sheet</th></tr>${matrixRows(BS)}
            <tr><th colspan="${periods.length + 1}">other</th></tr>${matrixRows(["average_employees"])}
          </tbody></table>` : `<div class="empty">No figures to tabulate — see coverage below for recorded causes.</div>`}
      </section>

      <section>
        <h2>Ownership &amp; control</h2>
        <div class="succession">
          <strong>Succession read</strong> — stated as register observations, not conclusions:
          <ul>
            <li>${oa !== null
              ? `Oldest active individual beneficial owner born ${THIS_YEAR - oa} (age ~${oa}).`
              : `No active individual beneficial owner with a published birth year — owner age ${state("not_observable")}.`}</li>
            <li>${singleBO
              ? "A single active beneficial owner holds 75–100% of shares."
              : `${activeBOs.length} active beneficial owner(s) on record.`}</li>
            <li>${youngest && youngest.dob_year
              ? `Youngest active officer born ${youngest.dob_year}; ${recentAppt.length} officer(s) appointed in the last five years.`
              : `No active officer with a published birth year.`}</li>
            <li>Succession signal scoring is Phase 2: ${state("not_reached")}.</li>
          </ul>
        </div>
        ${(c.beneficial_owners || []).length ? `<table>
          <thead><tr><th>beneficial owner</th><th>kind</th><th>born</th><th>natures of control</th><th>notified</th><th>ceased</th></tr></thead>
          <tbody>${c.beneficial_owners.map((b) => `<tr>
            <td>${esc(b.name)}</td><td>${esc(b.kind || "")}</td>
            <td class="num">${b.dob_year ? `${b.dob_year} (~${THIS_YEAR - b.dob_year})` : esc("—corporate")}</td>
            <td>${(b.natures || []).map(esc).join("<br>") || state("not_observable")}</td>
            <td>${esc(b.notified_on || "")}</td><td>${esc(b.ceased_on || "active")}</td></tr>`).join("")}</tbody></table>`
        : `<p class="note">No beneficial-owner records — a recorded gap, not evidence of independence.</p>`}
        ${(c.officers || []).length ? `<p class="note" style="margin-top:10px">Officers (${activeOff.length} active of ${c.officers.length}):</p>
          <table><thead><tr><th>officer</th><th>role</th><th>born</th><th>appointed</th><th>resigned</th></tr></thead>
          <tbody>${c.officers.slice().reverse().slice(0, 15).map((o) => `<tr>
            <td>${esc(o.name)}</td><td>${esc(o.role || "")}</td>
            <td class="num">${o.dob_year ? `${o.dob_year} (~${THIS_YEAR - o.dob_year})` : ""}</td>
            <td>${esc(o.appointed_on || "")}</td><td>${esc(o.resigned_on || "serving")}</td></tr>`).join("")}
          </tbody></table>${c.officers.length > 15 ? `<p class="note">Showing latest 15 of ${c.officers.length}; full roster on the <a href="${companyUrl(c.registration_id)}/officers">register</a>.</p>` : ""}` : ""}
      </section>

      <section>
        <h2>Security &amp; debt</h2>
        ${(c.recent_charges || []).length ? `
          <p class="note">${outstandingCharges(c)} outstanding / ${(c.charges["fully-satisfied"] || 0) + (c.charges["satisfied"] || 0)} satisfied.</p>
          <table><thead><tr><th>created</th><th>status</th><th>satisfied</th><th>holder(s)</th><th>classification</th></tr></thead>
          <tbody>${c.recent_charges.map((r) => `<tr>
            <td>${esc(r.created_on || "")}</td><td>${esc(r.status || "")}</td><td>${esc(r.satisfied_on || "—outstanding")}</td>
            <td>${(r.secured_parties || []).map(esc).join("<br>")}</td>
            <td>${esc((r.classification && (r.classification.description || r.classification.type)) || "")}</td></tr>`).join("")}
          </tbody></table>`
        : `<p class="note">No security interests on record — no registered lender to work around.</p>`}
      </section>

      <section>
        <h2>Signals &amp; flags</h2>
        <p class="note">Why this company surfaced: it matches the mandate's sector and incorporation filters
        (SIC ${c.sic.map(esc).join(", ")}) and screens in <span class="mode ${esc(c.mode)}">${esc(c.mode)}</span> mode.
        Named signal detectors, red-flag extraction (auditor changes, going-concern language, overdue filings)
        and plausibility flags are Phase 2: ${state("not_reached")}. What exists today is above:
        filed figures, ownership records, security interests — each traceable.</p>
      </section>

      <section>
        <h2>Peer set</h2>
        <p class="note">Same SIC division, nearest by net assets (mechanical selection — not a curated comp set).</p>
        ${peerRows.length ? `<table><thead><tr><th>company</th><th>sector</th><th class="num">revenue</th><th class="num">margin</th><th class="num">net assets</th><th class="num">employees</th></tr></thead>
          <tbody>${peerRows.map(({ p, na: pna, rev: prev }) => `<tr>
            <td class="co-name"><a href="${companyHref(p.id)}">${esc(p.name)}</a></td>
            <td class="sic-label">${esc(divName(divisionsOf(p)[0]))}</td>
            <td class="num">${prev ? figCell(prev) : coverageState(p.id, "revenue")}</td>
            <td class="num">${state("not_reached")}</td>
            <td class="num">${pna ? figCell(pna) : coverageState(p.id, "net_assets")}</td>
            <td class="num">${fig(p.latest_employees_fig) ? figCell(fig(p.latest_employees_fig)) : coverageState(p.id, "average_employees")}</td>
          </tr>`).join("")}</tbody></table>` : `<p class="note">No peers in this division within the ingested sample.</p>`}
      </section>

      <section>
        <h2>Filing history — fetched documents</h2>
        <p class="note">The ingest fetches the ${c.counts.documents} most recent account documents
        (of ${c.counts.filings} filings on the register — <a href="${filingHistoryUrl(c.registration_id)}">full history ↗</a>).</p>
        <table><thead><tr><th>period end</th><th>filed</th><th>regime</th><th>format</th><th>parse</th><th>produced by</th><th></th></tr></thead>
        <tbody>${Object.values(DATA.documents).filter((d) => d.company_id === cid)
          .sort((x, y) => String(y.filed_date).localeCompare(String(x.filed_date)))
          .map((d) => `<tr>
            <td>${esc(d.period_end || "")}</td><td>${esc(d.filed_date || "")}</td>
            <td>${esc(d.account_type || "")}</td><td>${esc((d.content_type || "").replace("application/", ""))}</td>
            <td>${d.parse_status === "parsed" ? "parsed" : state(d.parse_status === "pdf_only" ? "unparseable_format" : "parse_failed")}</td>
            <td>${esc(d.production_software || "not declared")}</td>
            <td>${documentUrl(c.registration_id, d.transaction_id) ? `<a href="${documentUrl(c.registration_id, d.transaction_id)}">open ↗</a>` : ""}</td>
          </tr>`).join("")}</tbody></table>
      </section>

      <section>
        <h2>Concept coverage at ${esc(covPeriod || "latest period")}</h2>
        <table><thead><tr><th>concept</th><th>status</th><th>recorded cause</th></tr></thead>
        <tbody>${coverageOf(cid).map((f) => `<tr><td>${esc(f.concept)}</td>
          <td>${f.status === "available" ? `<span class="state" style="border-color:var(--good)">available</span>` : state(f.status)}</td>
          <td style="color:var(--ink-2)">${esc(f.detail || "")}</td></tr>`).join("")}</tbody></table>
        <dl class="legend">${Object.keys(STATES).map((k) => `<dt>${state(k)}</dt><dd>${esc(STATES[k])}</dd>`).join("")}</dl>
      </section>`;

    $("#watch-toggle").addEventListener("click", () =>
      $("#watch-toggle").classList.toggle("on", toggleWatch(cid)));
  }

  // ====================================================================
  // TRACE
  // ====================================================================
  function renderTrace() {
    const figId = new URLSearchParams(location.search).get("fig");
    const f = DATA.figures[figId];
    const root = $("#trace-root");
    if (!f) {
      root.innerHTML = `<div class="empty"><strong>Unknown figure.</strong> <a href="screen.html">Back to the screen.</a></div>`;
      return;
    }
    const c = companiesById[f.company_id];
    const d = f.source_document_id ? doc(f.source_document_id) : null;
    document.title = `${f.concept} — trace`;
    $("#crumb").innerHTML = `<a href="screen.html">screen</a> / <a href="${companyHref(c.id)}">${esc(c.name)}</a> / ${esc(f.concept)}`;

    const dims = Object.entries(f.dimensions || {});
    const dimsKey = JSON.stringify(f.dimensions || {});
    const history = figuresOf(f.company_id)
      .filter((x) => x.concept === f.concept && x.period_end === f.period_end &&
                     JSON.stringify(x.dimensions || {}) === dimsKey)
      .map((x) => ({ f: x, d: x.source_document_id ? doc(x.source_document_id) : null }))
      .sort((a, b) => String((b.d && b.d.filed_date) || "").localeCompare(String((a.d && a.d.filed_date) || "")));

    root.innerHTML = `
      <div class="value-block">
        <div class="figure-value">${esc(figDisplay(f))}${basisBadge(f)}</div>
        <div class="figure-meta">${esc(f.concept)} · ${f.period_start ? esc(f.period_start) + " → " : "at "}${esc(f.period_end)} ·
          ${f.is_current ? "current observation" : "<strong>superseded</strong> — a later filing restates this period (see history)"}
          · unit <code>${esc(f.unit || "unspecified")}</code>
          ${dims.length ? `· ${dims.map(([k, v]) => `<code>${esc(k)}=${esc(v)}</code>`).join(" ")}` : ""}</div>
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
        </li>
        <li><span class="step">FILING</span>
          <div class="kv"><span class="k">filed date</span><span class="v plain"><strong>${esc(d.filed_date || "?")}</strong> · period end ${esc(d.period_end || f.period_end || "?")} · ${ageSpan(f.period_end)}</span></div>
          <div class="kv"><span class="k">registry transaction</span><span class="v">${esc(d.transaction_id || "unknown")}</span></div>
        </li>
        <li><span class="step">REGISTRY</span>
          <div class="kv registry-links">
            ${documentUrl(c.registration_id, d.transaction_id) ? `<a href="${documentUrl(c.registration_id, d.transaction_id)}" target="_blank" rel="noopener">Open this filing (iXBRL) ↗</a>` : ""}
            <a href="${filingHistoryUrl(c.registration_id)}" target="_blank" rel="noopener">Filing history ↗</a>
            <a href="${companyUrl(c.registration_id)}" target="_blank" rel="noopener">Register entry ↗</a>
          </div>
        </li>` : ""}
      </ol>
      <section><h2>Derivation</h2>
        ${f.derivation_function
          ? `<div class="kv"><span class="k">function</span><span class="v">${esc(f.derivation_function)}</span></div>
             <ul>${(f.derivation_inputs || []).map((id) => {
               const inp = DATA.figures[id];
               return `<li>${inp ? `<a href="${traceHref(id)}">${esc(inp.concept)} ${esc(figDisplay(inp))} (${esc(inp.period_end)})</a>` : `<code>${esc(id)}</code>`}</li>`;
             }).join("")}</ul>`
          : `<div class="derivation-note">Filed observation — no computation was performed. The value above is
             the tagged fact exactly as filed. A derived figure (EBITDA, margin, growth) would show its named,
             tested function here and walk back through every input to its own source filing. No language
             model touches any figure at any point.</div>`}
      </section>
      <section><h2>Observation history for this concept and period</h2>
        <table><thead><tr><th>value</th><th>filed date</th><th>regime</th><th>current</th><th></th></tr></thead>
        <tbody>${history.map((h) => `<tr>
          <td class="num">${esc(figDisplay(h.f))}</td><td>${esc((h.d && h.d.filed_date) || "?")}</td>
          <td>${esc((h.d && h.d.account_type) || "")}</td><td>${h.f.is_current ? "yes" : "no"}</td>
          <td>${h.f.id === f.id ? "← this figure" : `<a href="${traceHref(h.f.id)}">trace</a>`}</td></tr>`).join("")}
        </tbody></table>
      </section>`;
  }

  footer();
  const page = document.body.dataset.page;
  if (page === "screen") renderScreen();
  else if (page === "company") renderCompany();
  else if (page === "trace") renderTrace();
})();
