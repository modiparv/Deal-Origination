/* Landing renderer: every number comes from window.__SITE__, which the
 * build reads from the manifest the ingest run committed. Nothing here
 * is typed in by hand. */
(function () {
  "use strict";
  const S = window.__SITE__ || {};
  const esc = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[c]);
  const nf = new Intl.NumberFormat("en-GB");

  const stats = document.getElementById("stats");
  if (stats && S.store_present) {
    const m = S.modes || {};
    const total = (m.financial || 0) + (m.signal || 0) + (m.parse_failed || 0);
    const seg = (k) =>
      m[k]
        ? `<span class="seg ${k}" style="width:${(100 * m[k]) / total}%" title="${k}: ${nf.format(m[k])}"></span>`
        : "";
    const t = S.totals || {};
    stats.innerHTML = `
      <div class="stat"><div class="value">${nf.format(S.companies)}</div>
        <div class="label">companies in the store</div>
        <div class="detail">${S.universe_hits ? `of ${nf.format(S.universe_hits)} in the mandate universe · grows nightly` : "mandate universe sample · grows nightly"}</div></div>
      <div class="stat"><div class="value">${nf.format(S.figures)}</div>
        <div class="label">filed figures with full provenance</div>
        <div class="detail">${nf.format(S.documents)} source documents · ${nf.format(t.filings || 0)} filings on record</div></div>
      <div class="stat">
        <div class="value">${nf.format(m.financial ?? 0)}<span class="sep"> / </span><span class="seg-signal">${nf.format(m.signal ?? 0)}</span>${m.parse_failed ? `<span class="sep"> / </span>${nf.format(m.parse_failed)}` : ""}</div>
        <div class="label">screening modes: financial / signal${m.parse_failed ? " / parse_failed" : ""}</div>
        <div class="modebar">${seg("financial")}${seg("signal")}${seg("parse_failed")}</div></div>
      <div class="stat"><div class="value">${nf.format(S.products ?? 0)}</div>
        <div class="label">filing software products observed</div>
        <div class="detail">parse yield tracked per product · ${(S.parse_failures || {}).documents || 0} document(s) on the defect list</div></div>`;
  } else if (stats) {
    stats.innerHTML = `<div class="stat"><div class="value">—</div>
      <div class="label">no store in this deployment</div>
      <div class="detail">run an ingest; this page renders only verified output</div></div>`;
  }

  const foot = document.getElementById("site-footer");
  if (foot) {
    foot.innerHTML =
      `Store: ingest run <code>${esc(S.run_id || "none")}</code>` +
      (S.generated_at ? ` · exported ${esc(String(S.generated_at).replace("T", " ").slice(0, 16))} UTC` : "") +
      (S.commit ? ` · deployed from <code>${esc(String(S.commit).slice(0, 9))}</code>` : "") +
      ` · figures are filed observations from the UK register; the same figure from a later
       filing supersedes deterministically and restatements stay on the record ·
       <a href="https://github.com/modiparv/Deal-Origination" rel="noopener">source repository</a>`;
  }
})();
