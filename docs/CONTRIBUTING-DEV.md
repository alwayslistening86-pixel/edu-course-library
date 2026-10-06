# Developer checklists

Per-artefact checklists for [CONTRIBUTING.md](../CONTRIBUTING.md). Each item names the check that fails if you skip it. Run the suite from `plugin/generic-tutor`; run `tools/` commands from the repo root.

## Add a script
- [ ] `plugin/generic-tutor/scripts/<name>.py`: stdlib only, Python 3.10 floor, a module docstring that is the `--help` text, `cli.handle_help(__doc__)` before `main`.
- [ ] State goes through `tutorlib.state.load` / `state.save(path, data, kind)` under `filelock.file_lock`; check consent with `consent.check` and ledger changes with `ledger.record`. Never write JSON by hand (`test_idempotency`, `test_windows_hardening`).
- [ ] Output through `cli.emit`; errors as `{"error": ...}` with exit 1, usage errors exit 2.
- [ ] Test file `tests/test_<name>.py`, and a case in `tests/test_golden_cli.py` (`test_every_script_has_a_golden_case` fails without one). Regenerate with `UPDATE_GOLDEN=1 python3 -m unittest tests.test_golden_cli` and read the diff.
- [ ] Name it in the **Contract** `Calls:` line of the skill that uses it (docs lint checks the script exists).
- [ ] `python3 tools/bump_version.py X.Y.Z --changelog "..."` refreshes `.tutor-scripts/`; never hand-edit that folder (CI `deployed-sync`).
- [ ] `ruff check .` and `mypy` clean.

## Change a schema
- [ ] Edit `scripts/tutorlib/schemas/<kind>.json`; keep it permissive for unknown fields.
- [ ] Extend `migrate_schema.py` so old files reach the new shape, with a test on an old-shape fixture.
- [ ] Update `plugin/generic-tutor/docs/DATA_MODEL.md` (and `CONTENT_CONTRACT.md` for course files).
- [ ] State the rollback path in the PR.

## Change a skill
- [ ] Prose says *when* to call a script; deterministic rules go in a script.
- [ ] Keep the **Contract** block (Owns/Reads/Calls/Emits/Never) true; docs lint checks it.
- [ ] No release history in skill prose (that is `DESIGN_NOTES.md`); British "enrolment".
- [ ] `python3 tools/context_budget.py --check`: the budget only goes down unless a new user-facing capability justifies a ratchet raise, stated in the PR.
- [ ] If a suite covers the skill (see `evals/README.md`), compare old and new at the same sample count and attach the result.
- [ ] Version bump plus a `DESIGN_NOTES.md` entry.

## Add or change a command
- [ ] `commands/<name>.md` with `description` and, if it takes arguments, `argument-hint`; `@`-include only the skill files it needs.
- [ ] Add a row to `commands/help.md`; run `python3 tools/gen_commands_doc.py` to refresh `docs/COMMANDS.md`.
- [ ] Add a budget line to `tools/context_budget.json` (`context_budget.py` prints the measured size).
- [ ] A command that changes state ends in a script call, after a stated consequence and a clear yes where the change is hard to undo.

## Add an eval case or suite
- [ ] The reference label comes from construction, a deterministic oracle, or openly licensed data with licence and row recorded; never a human mark.
- [ ] List the acceptable set where more than one action is defensible; name the critical failure.
- [ ] New suite: module in `evals/`, add to `SUITES` in `evals/harness.py`, a row in `evals/README.md`.
- [ ] Offline sanity: `--backend oracle` must score 100% and `--backend always-wrong` must look bad.
- [ ] Record a baseline `evals/results/baseline-<suite>-sonnet.json` only from a run you have read.

## Add a task
- [ ] Row in `docs/TASKS.md` with an ID; one task = one PR, ID in the branch, commit and PR title.
- [ ] Put it in a wave, then `python3 tools/tasks_status.py --write`; `--check` fails if counts or waves are stale.
