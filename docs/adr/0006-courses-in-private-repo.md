# ADR 0006 — Course content lives in a private companion repo

Status: accepted (recorded retrospectively from `docs/history/DESIGN_NOTES.md`)

## Decision
Course content lives in a private companion repo.

## Why
Courses paraphrase copyrighted exam-board specifications and mark schemes; the engine is generic and MIT-licensed.

## Consequences
This repo ships engine only. `validate_courses.py` is run from the private repo's CI. A content contract (N-01) and reusable action (N-03) formalise the interface.
