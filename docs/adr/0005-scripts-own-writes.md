# ADR 0005 — Deterministic logic and state writes live in scripts, not prose

Status: accepted (recorded retrospectively from `docs/history/DESIGN_NOTES.md`)

## Decision
Deterministic logic and state writes live in scripts, not prose.

## Why
Hand-derived gates and 'write the value back' instructions drifted (cohort scoping v1.0.1; confidence/review fields v1.10.0).

## Consequences
Skills say when to call a script; scripts perform the read-modify-write (`apply` forms). Residual risk is the model *not calling* a script — addressed by ledger + verifier (V-01..V-06).
