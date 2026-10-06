# ADR 0008 — No hash-chained audit log

Status: accepted (recorded retrospectively from `docs/history/DESIGN_NOTES.md`)

## Decision
No hash-chained audit log.

## Why
Single-household, trusted-owner tool; tamper evidence adds complexity without a threat model.

## Consequences
Revisit only if fault-injection (V-05) shows silent corruption that a plain ledger can't catch (V-07).
