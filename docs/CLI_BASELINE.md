# CLI behaviour baseline (E-01 → input for E-09/E-10/E-11)

Observed from the golden snapshots in `plugin/generic-tutor/tests/golden/` (generated, then reviewed). Scripts print JSON on stdout. **Exit codes for errors are inconsistent today**: some scripts return the error as JSON with exit 0, others exit 2. The envelope/exit-code task (E-10, E-11) will normalise this deliberately; until then these snapshots pin the current behaviour.

| Script | Observed (exit, JSON `error` present) | Inconsistency |
|---|---|---|
| `apply_capabilities.py` | [(0, False)] |  |
| `cohort_status.py` | [(0, False)] |  |
| `confidence_update.py` | [(0, False), (2, True)] |  |
| `coverage_check.py` | [(0, False), (0, True)] | error with exit 0 |
| `diagnostic_gate.py` | [(0, False)] |  |
| `erase_profile.py` | [(0, False)] |  |
| `error_log.py` | [(0, False), (2, True)] |  |
| `export_profile.py` | [(0, False)] |  |
| `gate_check.py` | [(0, False)] |  |
| `item_mastery.py` | [(0, False)] |  |
| `migrate_schema.py` | [(0, False)] |  |
| `postcompile_gate.py` | [(0, False)] |  |
| `prereq_check.py` | [(0, False)] |  |
| `record_stage_result.py` | [(0, False)] |  |
| `remediation_state.py` | [(0, False)] |  |
| `resume_enrollment.py` | [(0, False)] |  |
| `review_math.py` | [(0, False), (0, True)] | error with exit 0 |
| `roster_check.py` | [(0, False)] |  |
| `slot_advance.py` | [(0, False)] |  |
| `sqlite_store.py` | [(0, False)] |  |
| `validate_structure.py` | [(0, False), (0, True)] | error with exit 0 |
