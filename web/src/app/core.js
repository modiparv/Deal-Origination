/* Product surface — shared core.
 *
 * Data: the build unpacks the store's web bundle into ./data/ — a
 * per-company INDEX (data/index.json, every company at once, what the
 * screen needs) and BUCKETED full records (data/c/<key>.json, fetched on
 * demand by the company, trace and compare pages). Every value rendered
 * anywhere is a verbatim register field, a mechanical aggregate, or
 * date arithmetic (ages, staleness, "within the last N months"). Nothing
 * financial is computed in the browser: EBITDA, margins, growth, gearing
 * and scores are Phase 2 derived figures and render as not_reached.
 *
 * Browser-local state (watchlist, pipeline board, saved screens, last
 * visit) lives in localStorage — this browser only, never synced, never
 * sent anywhere; the pages say so wherever it appears.
 */
(function () {
  "use strict";

  const SITE = window.__SITE__ || {};
  const DIV = window.__SIC_DIVISIONS__ || {};
  const $ = (s, root) => (root || document).querySelector(s);
  const $$ = (s, root) => [...(root || document).querySelectorAll(s)];
  const THIS_YEAR = new Date().getFullYear();
  const nf = new Intl.NumberFormat("en-GB");

  const esc = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[c]);

  // ---- absence states: five different things, never one dash ----
  const STATES = {
    filed_without_concept: "The filed accounts regime legitimately omits this concept (e.g. micro-entity accounts carry no P&L).",
    unparseable_format: "A filing exists but the registry offers no machine-readable rendition (PDF only).",
    parse_failed: "A machine-readable document exists but failed to parse — a system defect, never a data limitation.",
    not_reached: "Not yet computed: screening scores, flags and derived metrics (EBITDA, margin, growth, gearing) are Phase 2 and have not run.",
    not_captured: "Outside the fetched window — ingest retrieves the three most recent account documents per company.",
    skipped_mode: "Rubric dimension skipped: requires financial mode; this company screens in signal mode.",
    not_observable: "Not observable from public registry data for this company.",
    not_filed: "No filing of this kind exists on the register for the period.",
  };
  const state = (code, extra) =>
    `<span class="state st-${esc(code)}" title="${esc(extra || STATES[code] || "")}">${esc(code)}</span>`;
  const notDerived = () =>
    `<span class="state st-not_reached" title="not_reached — ${esc(STATES.not_reached)}">not derived · P2</span>`;

  // Short cause word for an absent concept — the canonical code stays in the tooltip.
  function causeChip(fact) {
    if (!fact) return `<span class="state st-not_captured" title="not_captured — ${esc(STATES.not_captured)}">not filed</span>`;
    if (fact.status === "filed_without_concept") {
      const m = /regime '([^']+)'/.exec(fact.detail || "");
      return `<span class="state st-filed_without_concept" title="filed_without_concept — ${esc(fact.detail || "")}">${esc(m ? m[1] : "regime omits")}</span>`;
    }
    if (fact.status === "unparseable_format")
      return `<span class="state st-unparseable_format" title="unparseable_format — ${esc(fact.detail || "")}">pdf only</span>`;
    if (fact.status === "parse_failed")
      return `<span class="state st-parse_failed" title="parse_failed — ${esc(fact.detail || "")}">parse failed</span>`;
    return state(fact.status, fact.detail || undefined);
  }
  // Index rows carry status COUNTS, not per-concept facts; the cause
  // shown for a missing headline figure is the dominant recorded cause.
  function causeFromCounts(row) {
    const s = (row.coverage && row.coverage.statuses) || {};
    if (s.parse_failed) return causeChip({ status: "parse_failed", detail: "see coverage on the company page" });
    if (s.unparseable_format && !s.available) return causeChip({ status: "unparseable_format" });
    if (s.filed_without_concept) return causeChip({ status: "filed_without_concept", detail: "regime omits this concept" });
    return causeChip(null);
  }

  // ---- formatting (display only) ----
  function money(fig) {
    const cur = fig.currency || (String(fig.unit || "").endsWith("GBP") ? "GBP" : null);
    const sym = cur === "GBP" ? "£" : cur ? cur + " " : "";
    const v = Number(fig.value), neg = v < 0, abs = Math.abs(v);
    return (neg ? "−" : "") + sym + (Number.isInteger(abs) ? nf.format(abs) : String(abs));
  }
  const plain = (f) => (Number.isInteger(Number(f.value)) ? nf.format(Number(f.value)) : String(f.value));
  const figDisplay = (f) => (f.concept === "average_employees" || String(f.unit || "").includes("pure") ? plain(f) : money(f));
  // Index references carry no unit; the concept name decides the format.
  const refDisplay = (ref, concept) =>
    concept === "employees" ? plain(ref) : money({ value: ref.value, currency: "GBP" });

  const MONTH_MS = 2629800000;
  function ageInfo(dateStr) {
    if (!dateStr) return null;
    const months = Math.max(0, Math.round((Date.now() - new Date(dateStr).getTime()) / MONTH_MS));
    const y = Math.floor(months / 12), m = months % 12;
    return { months, label: y ? `${y}y ${m}m` : `${m}m`, stale: months > 24 };
  }
  const monthsSince = (d) => (d ? Math.round((Date.now() - new Date(d).getTime()) / MONTH_MS) : null);
  const within = (d, months) => { const m = monthsSince(d); return m !== null && m <= months; };
  const ageSpan = (d) => {
    const a = ageInfo(d);
    if (!a) return state("not_captured");
    return `<span class="age${a.stale ? " stale" : ""}">${a.label}<span class="unit"> old${a.stale ? " · stale" : ""}</span></span>`;
  };
  const basisBadge = (f) => `<span class="basis" title="basis: ${esc(f.basis)} — stored verbatim">${esc(f.basis)}</span>`;
  const fmtDate = (d) => (d ? String(d).slice(0, 10) : "");
  const fmtStamp = (d) => (d ? String(d).replace("T", " ").slice(0, 16) + " UTC" : "");

  // ---- register links (the public register is the source of truth) ----
  const CH = "https://find-and-update.company-information.service.gov.uk";
  const companyUrl = (reg) => `${CH}/company/${encodeURIComponent(reg)}`;
  const filingHistoryUrl = (reg) => `${companyUrl(reg)}/filing-history`;
  const officersUrl = (reg) => `${companyUrl(reg)}/officers`;
  const pscUrl = (reg) => `${companyUrl(reg)}/persons-with-significant-control`;
  const chargesUrl = (reg) => `${companyUrl(reg)}/charges`;
  const filingUrl = (reg, txn) => (txn ? `${filingHistoryUrl(reg)}/${encodeURIComponent(txn)}/document?format=xhtml` : null);
  const filingPageUrl = (reg, txn) => (txn ? `${filingHistoryUrl(reg)}/${encodeURIComponent(txn)}` : null);

  const companyHref = (cid) => `company.html?id=${encodeURIComponent(cid)}`;
  const traceHref = (figId, cid) => `trace.html?fig=${encodeURIComponent(figId)}&c=${encodeURIComponent(cid)}`;
  const compareHref = (ids) => `compare.html?ids=${ids.map(encodeURIComponent).join(",")}`;

  // ---- classification ----
  const divisionsOf = (sic) => [...new Set((sic || []).map((s) => String(s).slice(0, 2)))];
  const divName = (d) => DIV[d] || `division ${d}`;

  // ---- mechanical register facts (date arithmetic only) ----
  const ownerAge = (row) => (row.owner_dob && row.owner_dob.year ? THIS_YEAR - row.owner_dob.year : null);
  const companyAgeYears = (inc) => (inc ? Math.floor((Date.now() - new Date(inc).getTime()) / 31557600000) : null);

  // Observed-in-window signals. Named after what the register shows,
  // dated, and never inferred beyond the observation itself.
  const OBS_WINDOW = 12;
  const OBSERVATIONS = [
    { key: "security_interest_registered", field: "last_charge_created", label: "charge registered", title: "A security interest (charge) was registered within the last 12 months — a lender took security; the register does not say why." },
    { key: "officer_resigned", field: "last_officer_resigned", label: "officer resigned", title: "An officer resignation was filed within the last 12 months." },
    { key: "officer_appointed", field: "last_officer_appointed", label: "officer appointed", title: "An officer was appointed within the last 12 months (active appointments only)." },
    { key: "psc_ceased", field: "last_psc_ceased", label: "PSC ceased", title: "A person with significant control ceased within the last 12 months — a change of control was notified." },
    { key: "psc_notified", field: "last_psc_notified", label: "PSC notified", title: "A new person with significant control was notified within the last 12 months." },
  ];
  function observations(row) {
    const out = [];
    for (const o of OBSERVATIONS) {
      const d = row[o.field];
      if (d && within(d, OBS_WINDOW)) out.push({ ...o, date: d, months: monthsSince(d) });
    }
    if (row.restatements) out.push({ key: "restatement", label: "restated", date: null, months: null,
      title: `${row.restatements} restatement event(s): a later filing changed a previously filed figure for the same period. The earlier observation stays on the record.` });
    return out;
  }
  const obsChip = (o) =>
    `<span class="obs" title="${esc(o.title)}">${esc(o.label)}${o.months !== null ? ` <span class="when">${o.months}m</span>` : ""}</span>`;

  // ---- data access ----
  let indexPromise = null;
  const bucketCache = new Map();
  const bucketKey = (reg) => (String(reg || "").slice(-3) || "_").replace(/[^A-Za-z0-9]/g, "_");
  async function getJson(path) {
    const res = await fetch(path, { cache: "default" });
    if (!res.ok) throw new Error(`${path}: HTTP ${res.status}`);
    return res.json();
  }
  const data = {
    index() {
      if (!indexPromise) {
        indexPromise = getJson("data/index.json").then((ix) => {
          ix.byId = Object.fromEntries(ix.companies.map((c) => [c.id, c]));
          return ix;
        });
      }
      return indexPromise;
    },
    async company(cid) {
      const reg = String(cid).split(":").slice(1).join(":");
      const key = bucketKey(reg);
      if (!bucketCache.has(key)) bucketCache.set(key, getJson(`data/c/${key}.json`));
      const bucket = await bucketCache.get(key);
      return bucket[cid] || null;
    },
    ops: () => getJson("data/ops.json"),
  };

  // ---- browser-local state ----
  const LS = {
    get(key, fallback) {
      try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch { return fallback; }
    },
    set(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* private mode: state is per-session */ } },
  };
  const watch = {
    all: () => new Set(LS.get("doe.watchlist", [])),
    has: (cid) => watch.all().has(cid),
    toggle(cid) { const w = watch.all(); w.has(cid) ? w.delete(cid) : w.add(cid); LS.set("doe.watchlist", [...w]); return w.has(cid); },
  };
  const STAGES = [
    { key: "identified", label: "Identified" },
    { key: "reviewed", label: "Reviewed" },
    { key: "prioritised", label: "Prioritised" },
    { key: "in_contact", label: "In contact" },
    { key: "parked", label: "Parked" },
    { key: "passed", label: "Passed" },
  ];
  const pipeline = {
    all: () => LS.get("doe.pipeline", {}),
    get: (cid) => pipeline.all()[cid] || null,
    add(cid, meta) {
      const p = pipeline.all();
      if (!p[cid]) p[cid] = { stage: "identified", notes: "", added_at: new Date().toISOString(), ...meta };
      p[cid].updated_at = new Date().toISOString();
      LS.set("doe.pipeline", p); return p[cid];
    },
    set(cid, patch) { const p = pipeline.all(); if (!p[cid]) return null; Object.assign(p[cid], patch, { updated_at: new Date().toISOString() }); LS.set("doe.pipeline", p); return p[cid]; },
    remove(cid) { const p = pipeline.all(); delete p[cid]; LS.set("doe.pipeline", p); },
    clear() { LS.set("doe.pipeline", {}); },
  };
  const screens = {
    all: () => LS.get("doe.screens", []),
    save(name, params) {
      const list = screens.all().filter((s) => s.name !== name);
      list.push({ id: `${Date.now().toString(36)}`, name, params, saved_at: new Date().toISOString() });
      LS.set("doe.screens", list); return list;
    },
    remove(id) { LS.set("doe.screens", screens.all().filter((s) => s.id !== id)); },
  };
  const lastVisit = {
    get: () => LS.get("doe.last_visit", null),
    set: (runId) => LS.set("doe.last_visit", { run_id: runId, at: new Date().toISOString() }),
  };
  const compareSel = {
    all: () => LS.get("doe.compare", []),
    toggle(cid) {
      let s = compareSel.all();
      if (s.includes(cid)) s = s.filter((x) => x !== cid); else if (s.length < 4) s.push(cid); else return { ok: false, list: s };
      LS.set("doe.compare", s); return { ok: true, list: s };
    },
    set: (list) => LS.set("doe.compare", list.slice(0, 4)),
  };

  // ---- screen filters: one definition, shared by SCREEN and TODAY ----
  const FILTER_KEYS = ["q", "divs", "own", "mode", "eb_min", "eb_max", "rev_min", "rev_max", "country", "loc", "owner_min", "stale", "nosucc", "single75", "obs"];
  function parseFilters(params) {
    const p = params instanceof URLSearchParams ? params : new URLSearchParams(params || "");
    const num = (k) => (p.has(k) && p.get(k).trim() !== "" && Number.isFinite(Number(p.get(k))) ? Number(p.get(k)) : null);
    return {
      q: (p.get("q") || "").trim().toLowerCase(),
      divs: (p.get("divs") || "").split(",").filter((d) => /^\d{2}$/.test(d)),
      own: p.get("own") || "",
      mode: ["financial", "signal", "parse_failed"].includes(p.get("mode")) ? p.get("mode") : "",
      ebMin: num("eb_min"), ebMax: num("eb_max"),
      revMin: num("rev_min"), revMax: num("rev_max"),
      country: (p.get("country") || "").trim(),
      loc: (p.get("loc") || "").trim().toLowerCase(),
      ownerMin: num("owner_min"),
      staleMax: num("stale"),
      nosucc: p.has("nosucc"),
      single75: p.has("single75"),
      obs: (p.get("obs") || "").split(",").filter((k) => OBSERVATIONS.some((o) => o.key === k) || k === "restatement"),
    };
  }
  function filtersToParams(f) {
    const p = new URLSearchParams();
    if (f.q) p.set("q", f.q);
    if (f.divs.length) p.set("divs", f.divs.join(","));
    if (f.own) p.set("own", f.own);
    if (f.mode) p.set("mode", f.mode);
    for (const [k, v] of [["eb_min", f.ebMin], ["eb_max", f.ebMax], ["rev_min", f.revMin], ["rev_max", f.revMax], ["owner_min", f.ownerMin], ["stale", f.staleMax]])
      if (v !== null && v !== undefined) p.set(k, String(v));
    if (f.country) p.set("country", f.country);
    if (f.loc) p.set("loc", f.loc);
    if (f.nosucc) p.set("nosucc", "1");
    if (f.single75) p.set("single75", "1");
    if (f.obs.length) p.set("obs", f.obs.join(","));
    return p;
  }
  function describeFilters(f) {
    const parts = [];
    if (f.q) parts.push(`"${f.q}"`);
    if (f.divs.length) parts.push(`${f.divs.length} sector division(s)`);
    if (f.own) parts.push(`ownership ${f.own}`);
    if (f.mode) parts.push(`${f.mode} mode`);
    if (f.ebMin !== null || f.ebMax !== null) parts.push(`EBITDA ${f.ebMin ?? "…"}–${f.ebMax ?? "…"}`);
    if (f.revMin !== null || f.revMax !== null) parts.push(`revenue £${f.revMin !== null ? nf.format(f.revMin) : "…"}–${f.revMax !== null ? nf.format(f.revMax) : "…"}`);
    if (f.country) parts.push(f.country);
    if (f.loc) parts.push(`locality "${f.loc}"`);
    if (f.ownerMin !== null) parts.push(`owner ≥ ${f.ownerMin}`);
    if (f.staleMax !== null) parts.push(`≤ ${f.staleMax} months old`);
    if (f.nosucc) parts.push("no officer appointed in 5y");
    if (f.single75) parts.push("single PSC 75–100%");
    if (f.obs.length) parts.push(`observed: ${f.obs.join(", ")}`);
    return parts.length ? parts.join(" · ") : "no filters — the whole store";
  }
  const isEmptyFilters = (f) => describeFilters(f).startsWith("no filters");

  // Each active test: 'pass' | 'fail' | 'unmeasurable'. A test over a
  // concept the store cannot measure (EBITDA, ownership class) still
  // runs and honestly floods the third bucket until Phase 2 lands.
  function evaluate(c, f) {
    const t = [];
    if (f.q) t.push(c.name.toLowerCase().includes(f.q) || c.registration_id.toLowerCase().includes(f.q) ? "pass" : "fail");
    if (f.divs.length) t.push(divisionsOf(c.sic).some((d) => f.divs.includes(d)) ? "pass" : "fail");
    if (f.own) t.push(c.ownership_classification ? (c.ownership_classification === f.own ? "pass" : "fail") : "unmeasurable");
    if (f.ebMin !== null || f.ebMax !== null) t.push("unmeasurable");
    if (f.revMin !== null || f.revMax !== null) {
      const g = c.latest && c.latest.revenue;
      if (!g) t.push("unmeasurable");
      else { const v = Number(g.value); t.push((f.revMin === null || v >= f.revMin) && (f.revMax === null || v <= f.revMax) ? "pass" : "fail"); }
    }
    if (f.country) t.push(!c.country ? "unmeasurable" : c.country === f.country ? "pass" : "fail");
    if (f.loc) t.push(!c.locality ? "unmeasurable" : String(c.locality).toLowerCase().includes(f.loc) ? "pass" : "fail");
    if (f.ownerMin !== null) { const a = ownerAge(c); t.push(a === null ? "unmeasurable" : a >= f.ownerMin ? "pass" : "fail"); }
    if (f.nosucc) {
      if (!c.officers_total) t.push("unmeasurable");
      else t.push(c.last_officer_appointed && c.last_officer_appointed >= `${THIS_YEAR - 5}-01-01` ? "fail" : "pass");
    }
    if (f.single75) t.push(c.active_owners ? (c.single_owner_75 ? "pass" : "fail") : "unmeasurable");
    if (f.staleMax !== null) { const a = ageInfo(c.freshest_period); t.push(!a ? "unmeasurable" : a.months <= f.staleMax ? "pass" : "fail"); }
    if (f.mode) t.push(c.mode === f.mode ? "pass" : "fail");
    if (f.obs.length) {
      const have = new Set(observations(c).map((o) => o.key));
      t.push(f.obs.every((k) => have.has(k)) ? "pass" : "fail");
    }
    if (t.includes("fail")) return "fail";
    if (t.includes("unmeasurable")) return "unmeasurable";
    return "pass";
  }
  function bucketise(rows, f) {
    const b = { pass: [], fail: [], unmeasurable: [] };
    for (const c of rows) b[evaluate(c, f)].push(c);
    return b;
  }

  // ---- CSV (Excel-compatible; provenance travels in adjacent columns) ----
  function csvDownload(name, rows) {
    // Quote every cell; prefix ' when text begins with a formula trigger
    // (= + - @) so a spreadsheet treats it as text, never executes it.
    const q = (s) => {
      let v = String(s ?? "");
      if (/^[=+\-@]/.test(v) && !/^-?\d/.test(v)) v = "'" + v;
      return `"${v.replace(/"/g, '""')}"`;
    };
    const text = rows.map((r) => r.map(q).join(",")).join("\r\n");
    const blob = new Blob(["﻿" + text], { type: "text/csv;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  // ---- sparkline: filed values plotted as filed; scaling is the only arithmetic ----
  function sparkline(points, opts) {
    // points: [{x: period_end, y: value}] oldest → newest
    const w = (opts && opts.width) || 96, h = (opts && opts.height) || 22, pad = 2;
    const ys = points.map((p) => Number(p.y)).filter((v) => Number.isFinite(v));
    if (points.length < 2 || !ys.length) return "";
    const min = Math.min(...ys, 0), max = Math.max(...ys, 0);
    const span = max - min || 1;
    const sx = (i) => pad + (i * (w - 2 * pad)) / (points.length - 1);
    const sy = (v) => h - pad - ((v - min) * (h - 2 * pad)) / span;
    const d = points.map((p, i) => `${i ? "L" : "M"}${sx(i).toFixed(1)},${sy(Number(p.y)).toFixed(1)}`).join(" ");
    const zero = min < 0 && max > 0 ? `<line x1="${pad}" x2="${w - pad}" y1="${sy(0).toFixed(1)}" y2="${sy(0).toFixed(1)}" class="zero"/>` : "";
    const last = points[points.length - 1];
    const title = points.map((p) => `${p.x}: ${p.label ?? p.y}`).join("\n");
    return `<svg class="spark" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img" aria-label="${esc(title)}"><title>${esc(title)}</title>${zero}<path d="${d}"/><circle cx="${sx(points.length - 1).toFixed(1)}" cy="${sy(Number(last.y)).toFixed(1)}" r="1.8"/></svg>`;
  }

  // ---- shell: header, nav, footer, shortcuts, toast ----
  const NAV = [
    ["today", "Today", "today.html"],
    ["screen", "Screen", "screen.html"],
    ["pipeline", "Pipeline", "pipeline.html"],
    ["ops", "Operations", "../ops/"],
  ];
  function shell(opts) {
    const page = document.body.dataset.page;
    const header = $("#app-header");
    if (header) {
      const cmp = compareSel.all();
      header.innerHTML = `
        <div class="brandrow">
          <a class="brand" href="../">Deal Origination Engine</a>
          <nav class="top-nav">${NAV.map(([k, label, href]) =>
            `<a href="${href}" class="${k === page ? "here" : ""}" data-nav="${k}">${label}</a>`).join("")}
            <a href="compare.html" class="${page === "compare" ? "here" : ""}" id="nav-compare" title="Side-by-side, up to four companies">Compare${cmp.length ? ` <b>${cmp.length}</b>` : ""}</a>
            <a href="#" id="nav-help" title="Keyboard shortcuts (?)">?</a>
          </nav>
        </div>
        <div class="titlerow">
          <div><h1 id="page-title">${esc(opts.title || "")}</h1><p class="crumb" id="crumb">${opts.crumb || ""}</p></div>
          <div class="titleside" id="title-side">${opts.side || ""}</div>
        </div>`;
      $("#nav-help").addEventListener("click", (e) => { e.preventDefault(); helpOverlay(); });
    }
    const foot = $("#app-footer");
    if (foot) {
      foot.innerHTML =
        `Store: ingest run <code>${esc(SITE.run_id || "none")}</code>${SITE.generated_at ? ` · exported ${esc(fmtStamp(SITE.generated_at))}` : ""}` +
        (SITE.commit ? ` · deployed from <code>${esc(String(SITE.commit).slice(0, 9))}</code>` : "") +
        ` · every figure is a filed observation citing its source document, period end and filed date; nothing on this
         surface is computed by a language model. Filed registry data is 9–21 months stale by construction; each figure
         shows its own age. Owner and officer ages are approximate (the register publishes birth month/year only).
         Watchlist, pipeline and saved screens are stored in this browser only.
         <a href="../">engine home</a> · <a href="../ops/">operations</a> ·
         <a href="https://github.com/modiparv/Deal-Origination" rel="noopener">source</a>`;
    }
    document.addEventListener("keydown", globalKeys);
  }
  function refreshCompareBadge() {
    const el = $("#nav-compare");
    if (!el) return;
    const n = compareSel.all().length;
    el.innerHTML = `Compare${n ? ` <b>${n}</b>` : ""}`;
  }
  let pendingG = false;
  function globalKeys(e) {
    const typing = ["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement.tagName);
    if (e.key === "Escape") { const o = $("#help-overlay"); if (o) o.remove(); document.activeElement.blur(); return; }
    if (typing) return;
    if (e.key === "?") { e.preventDefault(); helpOverlay(); return; }
    if (e.key === "/") { const s = $("#f-q"); if (s) { e.preventDefault(); s.focus(); s.select(); } return; }
    if (e.key === "g") { pendingG = true; setTimeout(() => { pendingG = false; }, 900); return; }
    if (pendingG) {
      const map = { t: "today.html", s: "screen.html", p: "pipeline.html", c: "compare.html", o: "../ops/" };
      if (map[e.key]) { e.preventDefault(); location.href = map[e.key]; }
      pendingG = false;
    }
  }
  function helpOverlay() {
    if ($("#help-overlay")) { $("#help-overlay").remove(); return; }
    const o = document.createElement("div");
    o.id = "help-overlay";
    o.innerHTML = `<div class="help"><h2>Keyboard</h2>
      <dl>
        <dt><kbd>g</kbd> <kbd>t</kbd></dt><dd>Today</dd>
        <dt><kbd>g</kbd> <kbd>s</kbd></dt><dd>Screen</dd>
        <dt><kbd>g</kbd> <kbd>p</kbd></dt><dd>Pipeline</dd>
        <dt><kbd>g</kbd> <kbd>c</kbd></dt><dd>Compare</dd>
        <dt><kbd>/</kbd></dt><dd>Focus search (Screen)</dd>
        <dt><kbd>↑</kbd> <kbd>↓</kbd> <kbd>Enter</kbd></dt><dd>Move through results, open company</dd>
        <dt><kbd>w</kbd></dt><dd>Watch / unwatch the focused row</dd>
        <dt><kbd>c</kbd></dt><dd>Add / remove the focused row from Compare</dd>
        <dt><kbd>p</kbd></dt><dd>Add the focused row to the Pipeline</dd>
        <dt><kbd>Esc</kbd></dt><dd>Close this, leave a field</dd>
      </dl><p class="note">Press <kbd>?</kbd> or <kbd>Esc</kbd> to close.</p></div>`;
    o.addEventListener("click", (e) => { if (e.target === o) o.remove(); });
    document.body.appendChild(o);
  }
  let toastTimer = null;
  function toast(msg) {
    let t = $("#toast");
    if (!t) { t = document.createElement("div"); t.id = "toast"; document.body.appendChild(t); }
    t.textContent = msg; t.classList.add("on");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove("on"), 1800);
  }
  function emptyStore(root) {
    root.innerHTML = `<div class="empty"><strong>No store in this deployment.</strong>
      This surface renders only verified ingest output. Run an ingest (Actions → ingest) — it publishes the
      web data bundle and commits the manifest, and the site rebuilds with the whole store.</div>`;
  }
  function loadError(root, err) {
    root.innerHTML = `<div class="empty"><strong>Could not load the store.</strong> ${esc(err && err.message ? err.message : err)}.
      If this page was opened from the file system, serve <code>web/dist/</code> over HTTP — the data is fetched, not inlined.</div>`;
  }

  window.DOE = {
    SITE, DIV, $, $$, THIS_YEAR, nf, esc,
    STATES, state, notDerived, causeChip, causeFromCounts,
    money, plain, figDisplay, refDisplay, ageInfo, ageSpan, monthsSince, within, basisBadge, fmtDate, fmtStamp,
    CH, companyUrl, filingHistoryUrl, officersUrl, pscUrl, chargesUrl, filingUrl, filingPageUrl,
    companyHref, traceHref, compareHref,
    divisionsOf, divName, ownerAge, companyAgeYears,
    OBSERVATIONS, OBS_WINDOW, observations, obsChip,
    data, watch, STAGES, pipeline, screens, lastVisit, compareSel,
    FILTER_KEYS, parseFilters, filtersToParams, describeFilters, isEmptyFilters, evaluate, bucketise,
    csvDownload, sparkline,
    shell, refreshCompareBadge, toast, helpOverlay, emptyStore, loadError,
  };
})();
