"""Content-addressed blob store for fetched documents.

Layout: `<root>/sha256/<first two hex chars>/<full hash>`. The path *is*
the content's identity, which gives three properties for free:

- immutability by construction — the same content always lands at the
  same path, and a store of existing content is a no-op, never an
  overwrite;
- integrity on read — the hash is recomputed and checked, so silent
  corruption fails loudly instead of feeding the parser garbage;
- change detection — if a registry ever serves different bytes for the
  same document ID, the differing hash makes it visible (the source
  document row keeps the hash it was ingested with).

Writes go through a same-directory temp file and `os.replace` so a
crashed run can never leave a half-written blob at a valid path.
"""

from __future__ import annotations

import hashlib
import os
import tempfile
from pathlib import Path


class CacheIntegrityError(Exception):
    """A cached blob's content no longer matches its address."""


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def blob_path(root: Path, sha256_hex: str) -> Path:
    return Path(root) / "sha256" / sha256_hex[:2] / sha256_hex


def has_blob(root: Path, sha256_hex: str) -> bool:
    return blob_path(root, sha256_hex).is_file()


def store_blob(root: Path, content: bytes) -> tuple[str, Path]:
    """Store content, returning (sha256 hex, path). Idempotent."""
    sha = _digest(content)
    path = blob_path(root, sha)
    if path.is_file():
        return sha, path
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".tmp-")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    return sha, path


def read_blob(root: Path, sha256_hex: str) -> bytes:
    """Read a blob, verifying its content still matches its address."""
    path = blob_path(root, sha256_hex)
    content = path.read_bytes()
    actual = _digest(content)
    if actual != sha256_hex:
        raise CacheIntegrityError(
            f"blob {path} content hashes to {actual}, expected {sha256_hex}; "
            f"the cache has been corrupted or tampered with"
        )
    return content
