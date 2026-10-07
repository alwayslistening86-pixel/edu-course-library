# CLI conventions and observed baseline (E-01, E-10, E-11)

Every script prints one JSON document on stdout (`tutorlib/cli.py`). Exit codes:

| Code | Meaning |
|---|---|
| 0 | success, including a *decision* the caller must read (`can_proceed: false`, consent skipped, dry run) |
| 1 | operation failed — the JSON has an `error` key |
| 2 | usage error — wrong arguments / unknown subcommand |

Before v1.16.0, `coverage_check.py`, `review_math.py apply` and `validate_structure.py` returned `{"error": …}` with exit 0; that is fixed. The table below is generated from the golden snapshots (`plugin/generic-tutor/tests/golden/`), which pin this behaviour.

| Script | Observed (exit, has `error`) |
|---|---|
| `apply_capabilities.py` | [(0, False)] |
| `cohort_status.py` | [(0, False)] |
| `confidence_update.py` | [(0, False), (2, True)] |
| `coverage_check.py` | [(0, False), (1, True)] |
| `diagnostic_gate.py` | [(0, False)] |
| `erase_profile.py` | [(0, False)] |
| `error_log.py` | [(0, False), (2, True)] |
| `export_profile.py` | [(0, False)] |
| `gate_check.py` | [(0, False)] |
| `item_mastery.py` | [(0, False)] |
| `migrate_schema.py` | [(0, False)] |
| `postcompile_gate.py` | [(0, False)] |
| `prereq_check.py` | [(0, False)] |
| `record_stage_result.py` | [(0, False)] |
| `remediation_state.py` | [(0, False)] |
| `resume_enrollment.py` | [(0, False)] |
| `review_math.py` | [(0, False), (1, True)] |
| `roster_check.py` | [(0, False)] |
| `slot_advance.py` | [(0, False)] |
| `sqlite_store.py` | [(0, False)] |
| `validate_structure.py` | [(0, False), (1, True)] |

Not yet done (E-09/E-10 remainder): argparse `--help` on every script; the optional `{ok,data,error{code,message}}` envelope; stable error-code enum.

## Envelope and error codes (E-10, E-11; v1.32.0)

Default output is unchanged. Add `--envelope` to any script (any position) to get
`{"ok": bool, "data": <legacy document or null>, "warnings": [..], "error": null | {"code", "message"}}`; the exit status is unchanged.
`data` is null only when the legacy output was an `{"error": ...}`; a non-zero exit with a normal result (e.g. `resolve_root.py` reporting `valid: false`) keeps its `data`.

| Code | Meaning | Typical exit |
|---|---|---|
| `E_USAGE` | wrong arguments / unknown subcommand | 2 |
| `E_CONSENT` | refused by the consent gate | 1 |
| `E_LOCKED` | another process holds the file lock | 1 |
| `E_NOT_FOUND` | file, stage, course or item missing | 1 |
| `E_SCHEMA` | file unreadable, wrong shape or newer `schema_version` | 1 |
| `E_INVALID_INPUT` | any other rejected value | 1 |
| `E_INTERNAL` | non-JSON output with a failing exit (a crash) | non-zero |

Codes are derived from the message by `tutorlib.cli.error_code` (first match wins, in the table's order of precedence: usage, consent, locked, not found, schema). Making each script name its own code is deferred; the legacy message text is pinned by the golden files.
