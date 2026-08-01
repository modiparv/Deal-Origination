"""Content-addressed cache: immutability, idempotency, integrity."""

import pytest

from deal_engine.ingest.cache import (
    CacheIntegrityError,
    blob_path,
    has_blob,
    read_blob,
    store_blob,
)


def test_store_and_read_roundtrip(tmp_path):
    sha, path = store_blob(tmp_path, b"hello accounts")
    assert path == blob_path(tmp_path, sha)
    assert path.parent.name == sha[:2]
    assert has_blob(tmp_path, sha)
    assert read_blob(tmp_path, sha) == b"hello accounts"


def test_store_is_idempotent(tmp_path):
    sha1, path1 = store_blob(tmp_path, b"same bytes")
    mtime = path1.stat().st_mtime_ns
    sha2, path2 = store_blob(tmp_path, b"same bytes")
    assert (sha1, path1) == (sha2, path2)
    assert path1.stat().st_mtime_ns == mtime  # no rewrite of existing content


def test_different_content_different_address(tmp_path):
    sha_a, _ = store_blob(tmp_path, b"a")
    sha_b, _ = store_blob(tmp_path, b"b")
    assert sha_a != sha_b


def test_read_detects_corruption(tmp_path):
    sha, path = store_blob(tmp_path, b"original")
    path.write_bytes(b"tampered")
    with pytest.raises(CacheIntegrityError, match="hashes to"):
        read_blob(tmp_path, sha)


def test_no_partial_blob_on_failed_write(tmp_path):
    sha, path = store_blob(tmp_path, b"x")
    leftovers = [p for p in path.parent.iterdir() if p.name.startswith(".tmp-")]
    assert leftovers == []
