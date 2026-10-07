# ADR 0007 — No placement diagnostic and no attestation of prior credit

Status: accepted (recorded retrospectively from `docs/history/DESIGN_NOTES.md`)

## Decision
No placement diagnostic and no attestation of prior credit.

## Why
The system can only trust what it verified itself; a self-declared credit would corrupt the level ledger and lock logic.

## Consequences
Learners start at the course's beginning; `highest_level_cleared` rises only by completed courses here. (Previously recorded in course-compiler Step 0.6.)
