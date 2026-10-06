# EDU course library — notes for Claude sessions

Public repo holding the **generic-tutor** engine only. Course content lives in the private `edu-courses-private` repo (never add `courses/`, `_staging/`, `_historic/` or real `profile/<id>/` data here).

## Layout
- `plugin/generic-tutor/` — source of truth: `skills/`, `commands/`, `scripts/` (stdlib-only Python), `tests/`, `_template/`.
- `.tutor-scripts/` — deployed runtime copy of `plugin/generic-tutor/scripts/`. **Never hand-edit.** Regenerate with `bootstrap_scripts.py` (CI diffs the two and fails on drift).
- `.github/` — CI and `scripts/validate_courses.py` (run from the private repo's CI).
- `docs/` — repo-level: `PLAN.md` (redesign plan, decisions), `TASKS.md` (numbered task list; one task = one PR), architecture, ADRs, glossary, pedagogy.
- `plugin/generic-tutor/docs/` — docs the *shipped plugin* refers to (`DATA_MODEL.md`, `PRIVACY.md`, `UNTRUSTED_CONTENT.md`); they live inside the plugin so references from skills resolve after install.
- `.claude-plugin/marketplace.json` — makes the repo installable: `claude plugin marketplace add alwayslistening86-pixel/edu-course-library`.

## Commands
```
cd plugin/generic-tutor && python3 -m unittest discover tests      # full suite, ~10 s, stdlib only
python3 plugin/generic-tutor/scripts/bootstrap_scripts.py plugin/generic-tutor/scripts plugin/generic-tutor/.claude-plugin/plugin.json .tutor-scripts   # refresh deployed copy
```

Golden CLI snapshots: `tests/golden/*.json` pin every script's output. If a change to script output is intended, regenerate with `cd plugin/generic-tutor && UPDATE_GOLDEN=1 python3 -m unittest tests.test_golden_cli`, then review the diff.

Evals (dev-only, manual): `cd plugin/generic-tutor && python3 -m evals run --suite all --backend claude --samples 3 --out /tmp/run` then `python3 -m evals check /tmp/run/<suite>.json`; offline sanity: `--backend oracle`. See `plugin/generic-tutor/evals/README.md`. Skill-text changes should come with a fresh `check`.

## Rules
- Python floor is 3.10; no third-party runtime dependencies.
- Deterministic logic belongs in scripts, not skill prose. Skills say *when* to call a script; scripts own state writes.
- Behaviour change ⇒ `python3 tools/bump_version.py X.Y.Z --changelog "summary"` (edits every version carrier, refreshes `.tutor-scripts/`, adds the CHANGELOG heading). The CHANGELOG entry carries the why; a lasting decision also gets an ADR in `docs/adr/`. `docs/history/DESIGN_NOTES.md` is frozen history (to v1.61.0): don't add to it.
- Schema change ⇒ migration in `migrate_schema.py` plus a test.
- Reference tasks by ID from `docs/TASKS.md` in branch names, commits and PR titles (e.g. `E-03: atomic JSON writes`).
- Never put learner data or real exam-board material in this repo.
