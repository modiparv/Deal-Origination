#!/usr/bin/env python3
"""PreToolUse guard hook (§3.3).

Reads the hook input JSON on stdin and denies:

- WebFetch/WebSearch outside the source-domain allowlist
- Bash commands invoking network clients against non-allowlisted hosts
- Write/Edit to data/** from a subagent (agent_id present) — pipeline
  writes happen inside the deal-engine CLI, invoked via Bash by the main
  agent
- any tool call whose arguments touch .env or credential-like files
  (.env.example is allowed: it holds no secrets by definition)

A deny holds regardless of permission mode. Honesty note (documented in
CLAUDE.md): this hook pattern-matches tool-call ARGUMENTS. It is a
guardrail, not a network egress sandbox — a subprocess spawned by an
allowed command can reach any domain.

Stdlib only: this script must run with no installed dependencies.
"""

from __future__ import annotations

import json
import re
import sys

ALLOWED_HOSTS = (
    "api.company-information.service.gov.uk",
    "document-api.company-information.service.gov.uk",
    "download.companieshouse.gov.uk",
    "stream.companieshouse.gov.uk",
    "developer.company-information.service.gov.uk",
    "developer-specs.company-information.service.gov.uk",
)

# Build/packaging infrastructure, permitted for shell commands only (pip,
# uv). These are NOT data sources: nothing fetched from them can become a
# figure — provenance is enforced at the schema layer, where a filed
# figure must cite a SourceDocument from a registry adapter.
BUILD_HOSTS = (
    "pypi.org",
    "files.pythonhosted.org",
)

_NETWORK_CMD_RE = re.compile(r"\b(curl|wget|httpx|http|nc|ncat|telnet)\b")
_URL_HOST_RE = re.compile(r"https?://([A-Za-z0-9.-]+)")
_CREDENTIAL_RE = re.compile(
    r"(?<![\w.-])\.env(?!\.example)(?![\w])|\.pem\b|secrets?\.(json|ya?ml|toml)\b|id_rsa\b"
)


def _deny(reason: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def _host_allowed(host: str, extra: tuple[str, ...] = ()) -> bool:
    host = host.lower().rstrip(".")
    return any(host == allowed for allowed in (*ALLOWED_HOSTS, *extra))


def decide(payload: dict) -> dict | None:
    """Return a deny decision, or None to defer to normal permission flow.

    The credential check applies to the file PATH for file tools and to
    the command string for Bash — never to file CONTENT, so documentation
    and code may mention credential filenames without tripping the guard.
    (The guard denied its own first edit before this scoping was added.)
    """
    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {}) or {}
    is_subagent = bool(payload.get("agent_id"))

    if tool in ("WebFetch", "WebSearch"):
        url = str(tool_input.get("url", "") or tool_input.get("query", ""))
        hosts = _URL_HOST_RE.findall(url)
        if tool == "WebFetch" and not hosts:
            return _deny("WebFetch without a parseable URL host")
        for host in hosts:
            if not _host_allowed(host):
                return _deny(
                    f"host {host!r} is outside the source allowlist "
                    f"{list(ALLOWED_HOSTS)}"
                )
        return None

    if tool == "Bash":
        command = str(tool_input.get("command", ""))
        if _CREDENTIAL_RE.search(command):
            return _deny("command references credential files (.env/keys/secrets)")
        if _NETWORK_CMD_RE.search(command):
            hosts = _URL_HOST_RE.findall(command)
            if not hosts:
                return _deny(
                    "network command without a parseable URL — name the host "
                    "explicitly so the allowlist can check it"
                )
            for host in hosts:
                if not _host_allowed(host, extra=BUILD_HOSTS):
                    return _deny(
                        f"network command targets {host!r}, outside the source "
                        f"allowlist"
                    )
        return None

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = str(tool_input.get("file_path", "") or tool_input.get("path", ""))
        if _CREDENTIAL_RE.search(path):
            return _deny("file path references credential files (.env/keys/secrets)")
        normalised = path.replace("\\", "/")
        if is_subagent and ("/data/" in f"/{normalised}" or normalised.startswith("data/")):
            return _deny(
                "subagents may not write to data/ — pipeline writes happen "
                "inside the deal-engine CLI"
            )
        return None

    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        # Malformed input: fail closed for safety.
        print(json.dumps(_deny("guard hook received malformed input")))
        return 0
    decision = decide(payload)
    if decision is not None:
        print(json.dumps(decision))
    return 0


if __name__ == "__main__":
    sys.exit(main())
