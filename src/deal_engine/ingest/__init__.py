"""Ingest: registry adapters in, canonical rows out.

The pipeline is deterministic and idempotent by construction — every
persisted row carries a deterministic identifier derived from registry
identity, so re-running an ingest inserts zero new rows and flips zero
`is_current` flags (DoD #4). Fetched documents live in a
content-addressed cache; the database stores paths and hashes, never
blobs.
"""
