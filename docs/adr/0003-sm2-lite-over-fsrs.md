# ADR 0003 — Keep SM-2-lite for review; do not adopt FSRS

Status: accepted (recorded retrospectively from `docs/history/DESIGN_NOTES.md`)

## Decision
Keep SM-2-lite for review; do not adopt FSRS.

## Why
FSRS models real elapsed time (conflicts with ADR 0002), needs a 4-grade recall judgment per review, and its advantage comes from fitting parameters to large review histories this single-household system will never have.

## Consequences
`review_math.py` stays simple, deterministic and tested. Revisit with real `review_log` data (L-14).
