#!/usr/bin/env node
/**
 * Static site build: assemble dist/ from committed artifacts and the
 * store's web data bundle.
 *
 * Zero dependencies by design — the deal-engine repo has no Node
 * toolchain, and the deploy host runs this script directly with Node's
 * standard library only. What the site shows comes from two places:
 *
 *   artifacts/ingest/<run id>/*.json, spot-check.md   committed run
 *       summaries and review dossiers (the /ops/ viewer)
 *   web/data/manifest.json                            committed by every
 *       ingest run: which bundle the site must carry (run id, totals,
 *       sha-256). The bundle itself — a compact per-company index plus
 *       bucketed full records — is too large for git history and lives
 *       on the repository's rolling "data-store" release. The build
 *       downloads it, verifies its sha-256 against the manifest, and
 *       unpacks it into dist/app/data/.
 *
 * A manifest whose bundle cannot be fetched or does not verify FAILS
 * the build: the previous deployment stays live, nothing stale or
 * partial is ever published as if current. A repository with no
 * manifest builds the empty state (every page says so).
 *
 * Local development: drop a bundle at web/data/local/web-data.jsonl.gz
 * (with its manifest.json beside it) or point DOE_WEB_DATA at one; it
 * is used without download.
 */

import { createHash } from "node:crypto";
import {
  cpSync, createReadStream, createWriteStream, existsSync, mkdirSync,
  readdirSync, readFileSync, rmSync, writeFileSync,
} from "node:fs";
import { mkdtemp } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { createInterface } from "node:readline";
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";
import { fileURLToPath } from "node:url";
import { createGunzip } from "node:zlib";

const here = dirname(fileURLToPath(import.meta.url));
const repo = join(here, "..");
const dist = join(here, "dist");
const artifactsRoot = process.env.ARTIFACTS_DIR || join(repo, "artifacts", "ingest");

function readJson(path) {
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch {
    return null;
  }
}

// ---------------------------------------------------------------- ops data
function collectRuns() {
  if (!existsSync(artifactsRoot)) return [];
  const runs = [];
  for (const entry of readdirSync(artifactsRoot, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const dir = join(artifactsRoot, entry.name);
    const files = readdirSync(dir);
    const summaries = files
      .filter((f) => (f.startsWith("coverage-") || f.startsWith("refresh-")) && f.endsWith(".json"))
      .map((f) => ({ file: f, kind: f.startsWith("refresh-") ? "refresh" : "ingest", data: readJson(join(dir, f)) }))
      .filter((s) => s.data);
    const spotCheck = files.includes("spot-check.md")
      ? readFileSync(join(dir, "spot-check.md"), "utf8")
      : null;
    for (const s of summaries) {
      runs.push({ workflowRun: entry.name, kind: s.kind, file: s.file, summary: s.data, spotCheck });
    }
  }
  // GitHub run ids are monotonically increasing; newest first.
  runs.sort((a, b) => (a.workflowRun < b.workflowRun ? 1 : -1));
  return runs;
}

function collectMandates() {
  const dir = join(repo, "mandates");
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter((f) => f.endsWith(".yaml"))
    .map((f) => ({ name: f, text: readFileSync(join(dir, f), "utf8") }));
}

function goldenInventory() {
  const filings = join(repo, "evals", "golden", "filings");
  const companies = join(repo, "evals", "golden", "companies");
  return {
    filings: existsSync(filings)
      ? readdirSync(filings).filter((f) => f.endsWith(".expected.yaml")).length
      : 0,
    companies: existsSync(companies)
      ? readdirSync(companies, { withFileTypes: true }).filter((e) => e.isDirectory()).length
      : 0,
  };
}

// ---------------------------------------------------------------- bundle
async function locateBundle(committedManifest) {
  const override = process.env.DOE_WEB_DATA;
  if (override) {
    if (!existsSync(override)) throw new Error(`DOE_WEB_DATA points at a missing file: ${override}`);
    return { path: override, source: "DOE_WEB_DATA", verify: false, manifest: committedManifest };
  }
  const localDir = join(repo, "web", "data", "local");
  const local = join(localDir, "web-data.jsonl.gz");
  if (existsSync(local)) {
    return {
      path: local,
      source: "web/data/local (development bundle)",
      verify: false,
      manifest: readJson(join(localDir, "manifest.json")) || committedManifest,
    };
  }
  if (!committedManifest) return null;
  const url = committedManifest.bundle && committedManifest.bundle.url;
  if (!url) throw new Error("web/data/manifest.json has no bundle.url");
  const dir = await mkdtemp(join(tmpdir(), "doe-web-data-"));
  const path = join(dir, "web-data.jsonl.gz");
  const res = await fetch(url, { redirect: "follow" });
  if (!res.ok || !res.body) {
    throw new Error(`bundle download failed: HTTP ${res.status} for ${url}`);
  }
  await pipeline(Readable.fromWeb(res.body), createWriteStream(path));
  return { path, source: url, verify: true, manifest: committedManifest };
}

async function sha256(path) {
  const hash = createHash("sha256");
  for await (const chunk of createReadStream(path)) hash.update(chunk);
  return hash.digest("hex");
}

// One record per line: "<kind>\t<name>\t<json>". Streamed, never held
// whole in memory — the unpacked store is a few hundred megabytes.
async function extractBundle(path, dataDir) {
  mkdirSync(join(dataDir, "c"), { recursive: true });
  const rl = createInterface({
    input: createReadStream(path).pipe(createGunzip()),
    crlfDelay: Infinity,
  });
  let bundleManifest = null;
  let buckets = 0;
  let hasIndex = false;
  for await (const line of rl) {
    if (!line) continue;
    const i = line.indexOf("\t");
    const j = line.indexOf("\t", i + 1);
    if (i < 0 || j < 0) throw new Error("malformed bundle record");
    const kind = line.slice(0, i);
    const name = line.slice(i + 1, j);
    const payload = line.slice(j + 1);
    switch (kind) {
      case "manifest":
        bundleManifest = JSON.parse(payload);
        writeFileSync(join(dataDir, "bundle-manifest.json"), payload);
        break;
      case "index":
        hasIndex = true;
        writeFileSync(join(dataDir, "index.json"), payload);
        break;
      case "ops":
        writeFileSync(join(dataDir, "ops.json"), payload);
        break;
      case "bucket":
        if (!/^[A-Za-z0-9_]{1,3}$/.test(name)) throw new Error(`bad bucket name ${JSON.stringify(name)}`);
        writeFileSync(join(dataDir, "c", `${name}.json`), payload);
        buckets += 1;
        break;
      default:
        throw new Error(`unknown bundle record kind ${JSON.stringify(kind)}`);
    }
  }
  if (!bundleManifest || !hasIndex) throw new Error("bundle is missing its manifest or index record");
  return { bundleManifest, buckets };
}

// ---------------------------------------------------------------- build
const committedManifest = readJson(join(repo, "web", "data", "manifest.json"));
const bundle = await locateBundle(committedManifest);

rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });

let manifest = null;
let store = { present: false, source: null, buckets: 0 };
if (bundle) {
  if (bundle.verify) {
    const got = await sha256(bundle.path);
    const want = bundle.manifest.bundle.sha256;
    if (got !== want) {
      throw new Error(
        `bundle sha-256 mismatch: manifest expects ${want}, downloaded ${got}. ` +
        `The release asset and the committed manifest disagree — refusing to publish.`
      );
    }
  }
  const dataDir = join(dist, "app", "data");
  const { bundleManifest, buckets } = await extractBundle(bundle.path, dataDir);
  if (bundle.verify && bundleManifest.run.run_id !== bundle.manifest.run.run_id) {
    throw new Error(
      `bundle run ${bundleManifest.run.run_id} does not match manifest run ${bundle.manifest.run.run_id}`
    );
  }
  manifest = { ...bundleManifest, bundle: bundle.manifest.bundle };
  store = { present: true, source: bundle.source, buckets };
}

const data = {
  builtAt: new Date().toISOString(),
  commit: process.env.VERCEL_GIT_COMMIT_SHA || process.env.GITHUB_SHA || null,
  branch: process.env.VERCEL_GIT_COMMIT_REF || null,
  repoUrl: "https://github.com/modiparv/Deal-Origination",
  runs: collectRuns(),
  mandates: collectMandates(),
  golden: goldenInventory(),
};
const latestIngest = data.runs.find((r) => r.kind === "ingest");

// What every page can know without fetching anything: the store's
// shape, straight from the manifest the ingest run committed.
const site = {
  commit: data.commit,
  branch: data.branch,
  built_at: data.builtAt,
  store_present: store.present,
  run_id: manifest ? manifest.run.run_id : null,
  generated_at: manifest ? manifest.generated_at : null,
  companies: manifest ? manifest.totals.companies : 0,
  figures: manifest ? manifest.totals.figures : 0,
  documents: manifest ? manifest.totals.documents : 0,
  filings: manifest ? manifest.totals.filings : 0,
  totals: manifest ? manifest.totals : {},
  modes: manifest ? manifest.modes : {},
  products: manifest ? manifest.products : 0,
  coverage_by_status: manifest ? manifest.coverage_by_status : {},
  parse_failures: manifest ? manifest.parse_failures : { documents: 0, companies: 0 },
  runs: manifest ? manifest.runs : [],
  universe_hits: latestIngest ? latestIngest.summary.universe_hits : null,
  latest_ingest: latestIngest
    ? {
        workflow_run: latestIngest.workflowRun,
        run_id: latestIngest.summary.run_id,
        ingested: latestIngest.summary.ingested,
        errors: (latestIngest.summary.errors || []).length,
      }
    : null,
};
const siteJs = `window.__SITE__ = ${JSON.stringify(site)};\n`;

// /ops/ — operations viewer over committed run artifacts + store report
const opsDist = join(dist, "ops");
mkdirSync(opsDist, { recursive: true });
for (const asset of ["index.html", "styles.css", "app.js"]) {
  cpSync(join(here, "src", "ops", asset), join(opsDist, asset));
}
writeFileSync(join(opsDist, "data.js"), `window.__DATA__ = ${JSON.stringify(data)};\n`);
const opsJsonPath = join(dist, "app", "data", "ops.json");
const opsReport = store.present && existsSync(opsJsonPath) ? readFileSync(opsJsonPath, "utf8") : "null";
writeFileSync(join(opsDist, "store.js"), `window.__STORE__ = { manifest: ${JSON.stringify(manifest)}, ops: ${opsReport} };\n`);
writeFileSync(join(opsDist, "site-summary.js"), siteJs);

// / — landing page
for (const asset of ["index.html", "landing.css", "landing.js"]) {
  cpSync(join(here, "src", "landing", asset), join(dist, asset));
}
writeFileSync(join(dist, "site-summary.js"), siteJs);

// /app/ — the product: TODAY, SCREEN, COMPANY, COMPARE, PIPELINE, TRACE
const appDist = join(dist, "app");
mkdirSync(appDist, { recursive: true });
for (const asset of readdirSync(join(here, "src", "app"))) {
  cpSync(join(here, "src", "app", asset), join(appDist, asset));
}
writeFileSync(join(appDist, "site-summary.js"), siteJs);

console.log(
  `built dist: ${data.runs.length} run summaries, ${data.mandates.length} mandate(s), ` +
    `${data.golden.filings} golden filing(s); store ${
      store.present
        ? `${site.companies} companies in ${store.buckets} buckets from ${store.source}`
        : "ABSENT (empty state)"
    }`
);
