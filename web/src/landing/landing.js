/* Landing renderer: every number comes from window.__SITE__, which the
 * build computes mechanically from the committed run dataset. Nothing
 * here is typed in by hand. */
(function () {
  "use strict";
  const S = window.__SITE__ || {};
  const esc = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[c]);
  const nf = new Intl.NumberFormat("en-GB");

  const stats = document.getElementById("stats");
  if (stats && S.companies) {
    const m = S.modes || {};
    const total = (m.financial || 0) + (m.signal || 0) + (m.parse_failed || 0);
    const seg = (k) =>
      m[k]
        ? `<span class="seg ${k}" style="width:${(100 * m[k]) / total}%" title="${k}: ${m[k]}"></span>`
        : "";
    stats.innerHTML = `
      <div class="stat"><div class="value">${nf.format(S.companies)}</div>
        <div class="label">companies in the current store</div>
        <div class="detail">mandate universe sample, sectors per mandate YAML</div></div>
      <div class="stat"><div class="value">${nf.format(S.figures)}</div>
        <div class="label">filed figures with full provenance</div>
        <div class="detail">${nf.format(S.documents)} source documents</div></div>
      <div class="stat">
        <div class="value">${m.financial ?? 0}<span class="sep"> / </span><span class="seg-signal">${m.signal ?? 0}</span>${m.parse_failed ? `<span class="sep"> / </span>${m.parse_failed}` : ""}</div>
        <div class="label">screening modes: financial / signal${m.parse_failed ? " / parse_failed" : ""}</div>
        <div class="modebar">${seg("financial")}${seg("signal")}${seg("parse_failed")}</div></div>
      <div class="stat"><div class="value">${S.products ?? 0}</div>
        <div class="label">filing software products observed</div>
        <div class="detail">parse yield tracked per product, every run</div></div>`;
  } else if (stats) {
    stats.innerHTML = `<div class="stat"><div class="value">—</div>
      <div class="label">no run data in this deployment</div>
      <div class="detail">run an ingest; this page renders only verified output</div></div>`;
  }

  const foot = document.getElementById("site-footer");
  if (foot) {
    foot.innerHTML =
      `Dataset: ingest run <code>${esc(S.run_id || "none")}</code>` +
      (S.commit ? ` · deployed from <code>${esc(String(S.commit).slice(0, 9))}</code>` : "") +
      ` · figures are filed observations from the UK register; the same figure from a later
       filing supersedes deterministically and restatements stay on the record ·
       <a href="https://github.com/modiparv/Deal-Origination" rel="noopener">source repository</a>`;
  }
})();
