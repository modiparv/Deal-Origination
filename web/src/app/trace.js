/* TRACE — one figure, walked back to the register:
 * FIGURE → TAG → DOCUMENT → FILING → REGISTRY. Derived figures (Phase 2)
 * walk through every input; a filed figure states that no computation
 * was performed.
 */
(async function () {
  "use strict";
  const D = window.DOE;
  const { $, esc, state } = D;
  const root = $("#trace-root");
  const qp = new URLSearchParams(location.search);
  const figId = qp.get("fig") || "", cid = qp.get("c") || "";
  D.shell({ title: "Provenance trace", crumb: `<a href="screen.html">screen</a>` });
  if (!D.SITE.store_present) { D.emptyStore(root); return; }

  let rec;
  try { rec = await D.data.company(cid); } catch (e) { D.loadError(root, e); return; }
  const f = rec && rec.figures.find((x) => x.id === figId);
  if (!f) {
    root.innerHTML = `<div class="empty"><strong>Unknown figure</strong> <code>${esc(figId)}</code>${cid ? ` for <code>${esc(cid)}</code>` : ""}.
      A trace link carries both the figure id and its company. <a href="screen.html">Back to the screen.</a></div>`;
    return;
  }
  const c = rec.company;
  const docById = Object.fromEntries(rec.documents.map((d) => [d.id, d]));
  const d = f.source_document_id ? docById[f.source_document_id] : null;
  document.title = `${f.concept} — trace`;
  $("#crumb").innerHTML = `<a href="screen.html">screen</a> / <a href="${D.companyHref(cid)}">${esc(c.name)}</a> / ${esc(f.concept)}`;

  const dims = Object.entries(f.dimensions || {});
  const dimsKey = JSON.stringify(f.dimensions || {});
  const history = rec.figures
    .filter((x) => x.concept === f.concept && x.period_end === f.period_end && JSON.stringify(x.dimensions || {}) === dimsKey)
    .map((x) => ({ f: x, d: x.source_document_id ? docById[x.source_document_id] : null }))
    .sort((p, q) => String((q.d && q.d.filed_date) || "").localeCompare(String((p.d && p.d.filed_date) || "")));
  const url = d ? D.filingUrl(c.registration_id, d.transaction_id) : null;
  const citation = `${c.name} (${c.registration_id}) — ${f.concept} ${D.figDisplay(f)}; period end ${f.period_end}` +
    (d ? `; filed ${d.filed_date} (${d.account_type || "accounts"}); tag ${f.source_tag}; document sha-256 ${d.content_hash}` : "") +
    (url ? `; ${url}` : "") + `; figure ${f.id}; basis ${f.basis}`;

  $("#title-side").innerHTML = `<button class="tw" id="copy-cite" title="Copy a one-line citation with the register link">copy citation</button>`;
  $("#copy-cite").addEventListener("click", async () => {
    try { await navigator.clipboard.writeText(citation); D.toast("Citation copied"); }
    catch { prompt("Citation:", citation); }
  });

  root.innerHTML = `
    <div class="value-block">
      <div class="figure-value">${esc(D.figDisplay(f))}${D.basisBadge(f)}</div>
      <div class="figure-meta">${esc(f.concept)} · ${f.period_start && f.period_start !== f.period_end ? esc(f.period_start) + " → " : "at "}${esc(f.period_end)} ·
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
        <div class="kv"><span class="k">sha-256</span><span class="v" title="${esc(d.content_hash || "")}">${esc(d.content_hash || "")}</span></div>
        <div class="kv"><span class="k">retrieved</span><span class="v plain">${esc(D.fmtStamp(d.retrieved_at))}</span></div>
      </li>
      <li><span class="step">FILING</span>
        <div class="kv"><span class="k">filed date</span><span class="v plain"><strong>${esc(d.filed_date || "?")}</strong> · period end ${esc(d.period_end || f.period_end || "?")} · ${D.ageSpan(f.period_end)}</span></div>
        <div class="kv"><span class="k">registry transaction</span><span class="v">${esc(d.transaction_id || "unknown")}</span></div>
        <div class="kv"><span class="k">document id</span><span class="v">${esc(d.external_document_id || "")}</span></div>
      </li>
      <li><span class="step">REGISTRY</span>
        <div class="kv registry-links">
          ${url ? `<a href="${url}" target="_blank" rel="noopener">Open this filing (iXBRL) ↗</a>` : ""}
          <a href="${D.filingHistoryUrl(c.registration_id)}" target="_blank" rel="noopener">Filing history ↗</a>
          <a href="${D.companyUrl(c.registration_id)}" target="_blank" rel="noopener">Register entry ↗</a>
        </div>
      </li>` : `<li><span class="step">DOCUMENT</span><div class="kv"><span class="k">source document</span><span class="v plain">${state("not_reached", "a derived or modelled figure cites its inputs instead of a document")}</span></div></li>`}
    </ol>
    <section><h2>Derivation</h2>
      ${f.derivation_function
        ? `<div class="kv"><span class="k">function</span><span class="v">${esc(f.derivation_function)}</span></div>
           <ul>${(f.derivation_inputs || []).map((id) => {
             const inp = rec.figures.find((x) => x.id === id);
             return `<li>${inp ? `<a href="${D.traceHref(id, cid)}">${esc(inp.concept)} ${esc(D.figDisplay(inp))} (${esc(inp.period_end)})</a>` : `<code>${esc(id)}</code>`}</li>`;
           }).join("")}</ul>`
        : `<div class="derivation-note">Filed observation — no computation was performed. The value above is the tagged fact
           exactly as filed. A derived figure (EBITDA, margin, growth) would show its named, tested function here and walk
           back through every input to its own source filing. No language model touches any figure at any point.</div>`}
    </section>
    <section><h2>Observation history for this concept and period</h2>
      <table><thead><tr><th>value</th><th>filed date</th><th>regime</th><th>current</th><th></th></tr></thead>
      <tbody>${history.map((h) => `<tr>
        <td class="num">${esc(D.figDisplay(h.f))}</td><td>${esc((h.d && h.d.filed_date) || "?")}</td>
        <td>${esc((h.d && h.d.account_type) || "")}</td><td>${h.f.is_current ? "yes" : "no"}</td>
        <td>${h.f.id === f.id ? "← this figure" : `<a href="${D.traceHref(h.f.id, cid)}">trace</a>`}</td></tr>`).join("")}
      </tbody></table>
      ${history.length > 1 ? `<p class="note">More than one observation exists for this concept and period: a later filing restated it.
        The latest filed date wins deterministically; the earlier observation stays on the record.</p>` : ""}
    </section>
    <section><h2>Citation</h2><p class="cite"><code>${esc(citation)}</code></p></section>`;
})();
