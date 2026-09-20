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

  const numbers = document.getElementById("numbers");
  if (numbers && S.store_present) {
    const t = S.totals || {}, m = S.modes || {}, pf = S.parse_failures || {};
    numbers.innerHTML = `
      <div><div class="value">${nf.format(S.companies)}</div><div class="label">companies in the store</div></div>
      <div><div class="value">${nf.format(S.figures)}</div><div class="label">filed figures, each with its source</div></div>
      <div><div class="value">${nf.format(S.documents)}</div><div class="label">accounts documents parsed</div></div>
      <div><div class="value">${nf.format(t.filings || 0)}</div><div class="label">register filings on record</div></div>
      <p class="note">
        Screening modes: <b>${nf.format(m.financial || 0)}</b> financial · <b>${nf.format(m.signal || 0)}</b> signal
        ${m.parse_failed ? ` · <span class="bad" title="a machine-readable document failed to parse — a defect, listed on the operations page">${nf.format(m.parse_failed)} parse failed</span>` : ""}
        · ${nf.format(S.products || 0)} filing-software products observed
        ${S.universe_hits ? ` · ${nf.format(S.universe_hits)} companies in the mandate universe, growing nightly` : ""}
      </p>`;
  } else if (numbers) {
    numbers.innerHTML = `<div><div class="value">—</div><div class="label">no store in this deployment; the page renders only verified output</div></div>`;
  }

  const foot = document.getElementById("site-footer");
  if (foot) {
    foot.innerHTML =
      `Store from ingest run <code>${esc(S.run_id || "none")}</code>` +
      (S.generated_at ? `, exported ${esc(String(S.generated_at).replace("T", " ").slice(0, 16))} UTC` : "") +
      (S.commit ? ` · deployed from <code>${esc(String(S.commit).slice(0, 9))}</code>` : "") +
      `. Figures are filed observations from the UK register; a later filing supersedes deterministically and
       restatements stay on the record. Watchlist, pipeline and saved screens live in your browser only.
       <a href="https://github.com/modiparv/Deal-Origination" rel="noopener">Source repository</a>`;
  }
})();
