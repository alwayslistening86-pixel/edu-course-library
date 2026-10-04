# ADR 0004 — JSON is authoritative; SQLite is append-only history

Status: accepted (recorded retrospectively from `plugin/generic-tutor/DESIGN_NOTES.md`)

## Decision
JSON is authoritative; SQLite is append-only history.

## Why
Current state must be human-readable, diffable and recoverable without tools. Trends (mastery over time, ease drift) need history that snapshots cannot give.

## Consequences
`tutor.sqlite3` is written by `sqlite_store.py`, never read back into teaching decisions; failures never block the JSON write. Gaps: consent, export, schema version (E-06, K-28, E-15).
