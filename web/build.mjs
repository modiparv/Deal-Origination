#!/usr/bin/env node
/**
 * Static site build: aggregate committed run artifacts into dist/.
 *
 * Zero dependencies by design — the deal-engine repo has no Node
 * toolchain, and the deploy host runs this script directly. Everything
 * the site shows comes from files committed to the repository:
 *
 *   artifacts/ingest/<run id>/coverage-*.json   ingest run summaries
 *   artifacts/ingest/<run id>/refresh-*.json    refresh run summaries
 *   artifacts/ingest/<run id>/spot-check.md     review dossiers
 *   mandates/*.yaml                             mandate configuration
 *   evals/golden/filings/*.expected.yaml        golden eval inventory
 *
 * The site is therefore a read-only view of verified, committed
 * outputs — it computes nothing financial and renders nothing that is
 * not already in the repository's audit trail.
 */

import { cpSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

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
      runs.push({
        workflowRun: entry.name,
        kind: s.kind,
        file: s.file,
        summary: s.data,
        spotCheck,
      });
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

const data = {
  builtAt: new Date().toISOString(),
  commit: process.env.VERCEL_GIT_COMMIT_SHA || process.env.GITHUB_SHA || null,
  branch: process.env.VERCEL_GIT_COMMIT_REF || null,
  repoUrl: "https://github.com/modiparv/Deal-Origination",
  runs: collectRuns(),
  mandates: collectMandates(),
  golden: goldenInventory(),
};

rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });
for (const asset of ["index.html", "styles.css", "app.js"]) {
  cpSync(join(here, "src", asset), join(dist, asset));
}
writeFileSync(join(dist, "data.js"), `window.__DATA__ = ${JSON.stringify(data)};\n`);
console.log(
  `built dist: ${data.runs.length} run summaries, ${data.mandates.length} mandate(s), ` +
    `${data.golden.filings} golden filing(s)`
);
