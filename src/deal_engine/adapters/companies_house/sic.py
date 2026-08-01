"""SIC 2007 wildcard expansion.

The advanced search API accepts exact 5-digit codes only; mandate
sector patterns like "620*" expand here against the registry's own
condensed code list (sic_2007.yaml, from the official enumeration
source).
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml

_CODES_FILE = Path(__file__).parent / "sic_2007.yaml"


@lru_cache(maxsize=1)
def all_codes() -> tuple[str, ...]:
    data = yaml.safe_load(_CODES_FILE.read_text(encoding="utf-8"))
    return tuple(str(c) for c in data["codes"])


def expand(patterns: list[str]) -> list[str]:
    """Expand wildcard patterns to exact codes; exact codes pass through
    only if they exist in the condensed list."""
    out: list[str] = []
    codes = all_codes()
    for pattern in patterns:
        if pattern.endswith("*"):
            prefix = pattern[:-1]
            out.extend(c for c in codes if c.startswith(prefix))
        elif pattern in codes:
            out.append(pattern)
    seen: set[str] = set()
    unique = [c for c in out if not (c in seen or seen.add(c))]
    return unique


def matches_any(code: str, patterns: list[str]) -> bool:
    for pattern in patterns:
        if pattern.endswith("*"):
            if code.startswith(pattern[:-1]):
                return True
        elif code == pattern:
            return True
    return False
