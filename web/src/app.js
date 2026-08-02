/* Read-only render of committed run artifacts (window.__DATA__).
   No fetches, no computation of financial figures — display only. */
"use strict";

const DATA = window.__DATA__ || { runs: [], mandates: [], golden: {} };

const STATUS_ORDER = [
  "available",
  "not_filed",
  "filed_without_concept",
  "unparseable_format",
  "parse_failed",
];
const STATUS_LABELS = {
  available: "available",
  not_filed: "not filed",
  filed_without_concept: "filed without concept (regime omits)",
  unparseable_format: "unparseable format",
  parse_failed: "parse failed (system defect)",
};

const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

function el(tag, attrs = {}, html = "") {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
  node.innerHTML = html;
  return node;
}

/* ---------------- header meta ---------------- */

(function meta() {
  const parts = [];
  if (DATA.commit) parts.push(`commit ${esc(DATA.commit.slice(0, 7))}`);
  if (DATA.branch) parts.push(esc(DATA.branch));
  if (DATA.builtAt) parts.push(`built ${esc(DATA.builtAt.replace("T", " ").slice(0, 16))} UTC`);
  document.getElementById("build-meta").innerHTML = parts.join(" · ");
  const g = DATA.golden || {};
  document.getElementById("golden-inventory").innerHTML =
    `Golden sets: ${g.filings || 0} hand-verified filing(s), ${g.companies || 0} recorded company surface(s). ` +
    `Source: <a href="${esc(DATA.repoUrl)}">modiparv/Deal-Origination</a>.`;
})();

/* ---------------- latest run ---------------- */

const latest = DATA.runs[0] || null;

(function latestSection() {
  const root = document.getElementById("latest");
  root.appendChild(el("h2", {}, "Latest run"));
  if (!latest) {
    root.appendChild(
      el(
        "div",
        { class: "empty" },
        `<h3>No ingest runs recorded yet</h3>
         <p>The pipeline is built and gated in CI, but no real-registry run has been
         published. To produce the first coverage report and spot-check dossier:</p>
         <ol>
           <li>Merge the Phase 1 pull request so the workflows land on the default branch.</li>
           <li>GitHub → Actions → <code>ingest</code> → Run workflow (defaults: 200 companies).</li>
           <li>The run commits its outputs to <code>artifacts/ingest/&lt;run id&gt;/</code>; this site rebuilds and renders them.</li>
         </ol>`
      )
    );
    return;
  }
  const s = latest.summary;
  const c = s.counts || {};
  const modes = (s.coverage || {}).screening_modes || {};
  root.appendChild(
    el(
      "p",
      { class: "section-note" },
      `run <code>${esc(s.run_id || "?")}</code>` +
        `<span class="run-badge">${esc(latest.kind)}</span>` +
        `<span class="run-badge">workflow ${esc(latest.workflowRun)}</span>`
    )
  );
  const tiles = el("div", { class: "tiles" });
  const tile = (value, label, detail = "") =>
    tiles.appendChild(
      el(
        "div",
        { class: "tile" },
        `<div class="value">${esc(value)}</div><div class="label">${esc(label)}</div>` +
          (detail ? `<div class="detail">${esc(detail)}</div>` : "")
      )
    );
  if (latest.kind === "ingest") {
    tile(s.ingested ?? 0, "companies ingested", `of ${s.examined ?? "?"} examined`);
    tile(s.universe_hits ?? 0, "universe hits", "advanced search, mandate sectors");
    const skipped = s.skipped || {};
    tile(
      Object.values(skipped).reduce((a, b) => a + b, 0),
      "skipped at triage",
      Object.entries(skipped).map(([k, v]) => `${k}: ${v}`).join(", ") || "—"
    );
  } else {
    tile(s.refreshed ?? 0, "companies refreshed", `${c.companies_changed || 0} changed, ${c.companies_unchanged || 0} unchanged`);
    tile(c.new_transactions || 0, "new filing transactions");
  }
  tile(c.figures_new ?? 0, "figures persisted", "filed observations with provenance");
  tile(
    `${modes.financial ?? 0} / ${modes.signal ?? 0}`,
    "screening modes (financial / signal)",
    "machine-readable accounts vs observable behaviour"
  );
  if (modes.parse_failed) {
    tile(
      modes.parse_failed,
      "parse failed",
      "system defect, not a data limitation — excluded from signal count"
    );
  }
  tile(c.coverage_facts ?? 0, "coverage facts", "absence carries a cause");
  tile((s.errors || []).length, "errors", (s.errors || []).length ? "see run log" : "clean run");
  root.appendChild(tiles);
})();

/* ---------------- coverage ---------------- */

(function coverageSection() {
  const root = document.getElementById("coverage");
  if (!latest || !latest.summary.coverage) return;
  const coverage = latest.summary.coverage;
  const byCode = coverage.by_classification_code || {};
  if (!Object.keys(byCode).length) return;

  root.appendChild(el("h2", {}, "Concept coverage by classification code"));
  root.appendChild(
    el(
      "p",
      { class: "section-note" },
      "Share of companies per concept and coverage outcome, within the mandate's " +
        "filtered universe. A company is counted under every mandate-matching code it declares."
    )
  );
  const legend = el("div", { class: "legend" });
  for (const status of STATUS_ORDER) {
    legend.appendChild(
      el(
        "span",
        {},
        `<span class="swatch st-${status}"></span>${esc(STATUS_LABELS[status])}`
      )
    );
  }
  root.appendChild(legend);

  const tooltip = document.getElementById("tooltip");
  for (const [code, bucket] of Object.entries(byCode)) {
    const card = el("div", { class: "card code-card" });
    card.appendChild(el("h3", {}, `Classification ${esc(code)}`));
    card.appendChild(
      el("p", { class: "companies" }, `${bucket.companies} compan${bucket.companies === 1 ? "y" : "ies"}`)
    );
    const concepts = bucket.concepts || {};
    const tableRows = [];
    for (const [concept, statuses] of Object.entries(concepts)) {
      const total = Object.values(statuses).reduce((a, b) => a + b, 0);
      const row = el("div", { class: "concept-row" });
      row.appendChild(el("span", { class: "name", title: concept }, esc(concept)));
      const bar = el("div", { class: "bar", role: "img", "aria-label": `${concept} coverage` });
      for (const status of STATUS_ORDER) {
        const n = statuses[status] || 0;
        if (!n) continue;
        const seg = el("span", {
          class: `seg st-${status}`,
          style: `width:${(100 * n) / total}%`,
        });
        seg.addEventListener("mousemove", (e) => {
          tooltip.hidden = false;
          tooltip.textContent = `${concept} — ${STATUS_LABELS[status]}: ${n} of ${total} (${Math.round((100 * n) / total)}%)`;
          tooltip.style.left = Math.min(e.clientX + 12, window.innerWidth - 330) + "px";
          tooltip.style.top = e.clientY + 14 + "px";
        });
        seg.addEventListener("mouseleave", () => (tooltip.hidden = true));
        bar.appendChild(seg);
      }
      row.appendChild(bar);
      row.appendChild(el("span", { class: "count" }, String(total)));
      card.appendChild(row);
      tableRows.push(
        `<tr><td>${esc(concept)}</td>` +
          STATUS_ORDER.map((st) => `<td class="num">${statuses[st] || 0}</td>`).join("") +
          `</tr>`
      );
    }
    const details = el(
      "details",
      { class: "table-view" },
      `<summary>Table view</summary>
       <table><thead><tr><th>concept</th>${STATUS_ORDER.map((st) => `<th class="num">${esc(STATUS_LABELS[st])}</th>`).join("")}</tr></thead>
       <tbody>${tableRows.join("")}</tbody></table>`
    );
    card.appendChild(details);
    root.appendChild(card);
  }
})();

/* ---------------- runs table ---------------- */

(function runsSection() {
  const root = document.getElementById("runs");
  if (!DATA.runs.length) return;
  root.appendChild(el("h2", {}, "Run history"));
  root.appendChild(
    el("p", { class: "section-note" }, "Every unattended run is logged; artifacts are committed to the repository.")
  );
  const branch = DATA.branch || "main";
  const rows = DATA.runs
    .map((r) => {
      const s = r.summary;
      const link = `${DATA.repoUrl}/tree/${encodeURIComponent(branch)}/artifacts/ingest/${encodeURIComponent(r.workflowRun)}`;
      const companies = r.kind === "ingest" ? s.ingested ?? "—" : s.refreshed ?? "—";
      return `<tr>
        <td><a href="${esc(link)}">${esc(r.workflowRun)}</a></td>
        <td>${esc(r.kind)}</td>
        <td><code>${esc(s.run_id || "?")}</code></td>
        <td class="num">${esc(companies)}</td>
        <td class="num">${(s.errors || []).length}</td>
      </tr>`;
    })
    .join("");
  root.appendChild(
    el(
      "div",
      { class: "card" },
      `<table><thead><tr><th>workflow run</th><th>kind</th><th>run id</th>
       <th class="num">companies</th><th class="num">errors</th></tr></thead><tbody>${rows}</tbody></table>`
    )
  );
})();

/* ---------------- spot-check dossier (markdown, escape-first) ------------ */

function renderMarkdown(md) {
  const lines = md.split(/\r?\n/);
  const out = [];
  let list = false;
  let table = [];
  const flushTable = () => {
    if (!table.length) return;
    const header = table[0];
    const body = table.slice(2); // row 1 is the |---| separator
    const cells = (row) => row.split("|").slice(1, -1).map((c) => c.trim());
    out.push(
      "<table><thead><tr>" +
        cells(header).map((c) => `<th>${inline(c)}</th>`).join("") +
        "</tr></thead><tbody>" +
        body
          .map((row) => "<tr>" + cells(row).map((c) => `<td>${inline(c)}</td>`).join("") + "</tr>")
          .join("") +
        "</tbody></table>"
    );
    table = [];
  };
  const inline = (s) =>
    esc(s)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/_([^_]+)_/g, "<em>$1</em>");
  const closeList = () => {
    if (list) {
      out.push("</ul>");
      list = false;
    }
  };
  for (const line of lines) {
    if (/^\s*\|/.test(line)) {
      closeList();
      table.push(line.trim());
      continue;
    }
    flushTable();
    if (/^##\s/.test(line)) {
      closeList();
      out.push(`<h2>${inline(line.slice(3))}</h2>`);
    } else if (/^#\s/.test(line)) {
      closeList();
      out.push(`<h1>${inline(line.slice(2))}</h1>`);
    } else if (/^-\s/.test(line)) {
      if (!list) {
        out.push("<ul>");
        list = true;
      }
      out.push(`<li>${inline(line.slice(2))}</li>`);
    } else if (line.trim() === "") {
      closeList();
    } else {
      closeList();
      out.push(`<p>${inline(line)}</p>`);
    }
  }
  flushTable();
  closeList();
  return out.join("\n");
}

(function spotCheckSection() {
  const root = document.getElementById("spot-check");
  const withDossier = DATA.runs.find((r) => r.spotCheck);
  if (!withDossier) return;
  root.appendChild(el("h2", {}, "Spot-check dossier"));
  root.appendChild(
    el(
      "p",
      { class: "section-note" },
      `Deterministic review sample from workflow run ${esc(withDossier.workflowRun)} — the human gate input.`
    )
  );
  root.appendChild(el("div", { class: "card md" }, renderMarkdown(withDossier.spotCheck)));
})();

/* ---------------- mandates ---------------- */

(function mandatesSection() {
  const root = document.getElementById("mandates");
  if (!DATA.mandates.length) return;
  root.appendChild(el("h2", {}, "Mandate configuration"));
  root.appendChild(
    el("p", { class: "section-note" }, "Mandates are versioned YAML; screening criteria live here, never in code.")
  );
  for (const m of DATA.mandates) {
    root.appendChild(el("h3", {}, esc(m.name)));
    root.appendChild(el("pre", { class: "yaml" }, esc(m.text)));
  }
})();
