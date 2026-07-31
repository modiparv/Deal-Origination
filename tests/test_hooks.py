"""Guard hook tests: hooks are code, so they get tests like code.

Each case pipes a PreToolUse payload into the real script via subprocess
and asserts the decision. Empty stdout means the hook defers to the
normal permission flow; a deny decision arrives as JSON.
"""

import json
import subprocess
import sys
from pathlib import Path

GUARD = Path(__file__).resolve().parent.parent / ".claude" / "hooks" / "guard.py"


def run_guard(payload: dict) -> dict | None:
    proc = subprocess.run(
        [sys.executable, str(GUARD)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout.strip()
    return json.loads(out) if out else None


def decision(payload: dict) -> str | None:
    result = run_guard(payload)
    if result is None:
        return None
    return result["hookSpecificOutput"]["permissionDecision"]


ALLOWED_URL = "https://api.company-information.service.gov.uk/company/00000006"


class TestNetworkAllowlist:
    def test_webfetch_allowed_host(self):
        assert decision({"tool_name": "WebFetch", "tool_input": {"url": ALLOWED_URL}}) is None

    def test_webfetch_disallowed_host(self):
        assert (
            decision({"tool_name": "WebFetch", "tool_input": {"url": "https://example.com/x"}})
            == "deny"
        )

    def test_webfetch_no_host(self):
        assert decision({"tool_name": "WebFetch", "tool_input": {"url": "not a url"}}) == "deny"

    def test_bash_curl_allowed_host(self):
        assert (
            decision({"tool_name": "Bash", "tool_input": {"command": f"curl -sS {ALLOWED_URL}"}})
            is None
        )

    def test_bash_curl_disallowed_host(self):
        assert (
            decision(
                {"tool_name": "Bash", "tool_input": {"command": "curl https://evil.example.com/"}}
            )
            == "deny"
        )

    def test_bash_network_command_without_url(self):
        assert (
            decision({"tool_name": "Bash", "tool_input": {"command": "curl $SOME_HOST"}}) == "deny"
        )

    def test_bash_non_network_command_passes(self):
        assert (
            decision({"tool_name": "Bash", "tool_input": {"command": "pytest -q"}}) is None
        )

    def test_bash_pip_install_from_pypi_allowed(self):
        # Build infrastructure is not a data source; pip must work.
        assert (
            decision(
                {
                    "tool_name": "Bash",
                    "tool_input": {
                        "command": "curl -sS https://pypi.org/simple/pydantic/"
                    },
                }
            )
            is None
        )

    def test_webfetch_build_host_still_denied(self):
        # BUILD_HOSTS applies to Bash only; WebFetch stays source-scoped.
        assert (
            decision({"tool_name": "WebFetch", "tool_input": {"url": "https://pypi.org/x"}})
            == "deny"
        )


class TestCredentialGuard:
    def test_bash_touching_env_denied(self):
        assert (
            decision({"tool_name": "Bash", "tool_input": {"command": "cat .env"}}) == "deny"
        )

    def test_bash_env_example_allowed(self):
        assert (
            decision({"tool_name": "Bash", "tool_input": {"command": "cat .env.example"}}) is None
        )

    def test_write_to_env_denied(self):
        assert (
            decision({"tool_name": "Write", "tool_input": {"file_path": "/repo/.env"}}) == "deny"
        )

    def test_write_content_mentioning_env_allowed(self):
        # Content is not scanned — only the target path. Documentation may
        # mention credential files.
        assert (
            decision(
                {
                    "tool_name": "Write",
                    "tool_input": {"file_path": "/repo/README.md", "content": "Copy .env into place"},
                }
            )
            is None
        )

    def test_bash_id_rsa_denied(self):
        assert (
            decision({"tool_name": "Bash", "tool_input": {"command": "cat ~/.ssh/id_rsa"}})
            == "deny"
        )


class TestDataWriteGuard:
    def test_subagent_write_to_data_denied(self):
        assert (
            decision(
                {
                    "tool_name": "Write",
                    "tool_input": {"file_path": "data/cache/x.html"},
                    "agent_id": "subagent-1",
                }
            )
            == "deny"
        )

    def test_main_agent_write_to_data_allowed(self):
        assert (
            decision({"tool_name": "Write", "tool_input": {"file_path": "data/cache/x.html"}})
            is None
        )

    def test_subagent_write_elsewhere_allowed(self):
        assert (
            decision(
                {
                    "tool_name": "Write",
                    "tool_input": {"file_path": "src/deal_engine/x.py"},
                    "agent_id": "subagent-1",
                }
            )
            is None
        )


def test_malformed_input_fails_closed():
    proc = subprocess.run(
        [sys.executable, str(GUARD)],
        input="not json",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert proc.returncode == 0
    assert json.loads(proc.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny"
