# Contributing

Personal project, but changes follow the same rules so the history stays trustworthy.

1. Pick a task from [`docs/TASKS.md`](docs/TASKS.md) (or add one with a new ID first). One task = one PR; prefix the title with the ID.
2. Branch from `main`; short-lived branches, squash merge.
3. Run the suite: `cd plugin/generic-tutor && python3 -m unittest discover tests`.
4. If you touch `plugin/generic-tutor/scripts/`, refresh `.tutor-scripts/` (see `CLAUDE.md`); CI fails on drift.
5. Plugin behaviour change: bump the version in `plugin.json` and record it in `DESIGN_NOTES.md`.
6. Schema change: add a migration and a test; note the rollback path in the PR.
7. No learner data, no copyrighted exam-board text.

Per-artefact checklists (script, schema, skill, command, eval case, task): [`docs/CONTRIBUTING-DEV.md`](docs/CONTRIBUTING-DEV.md).

## Releasing
1. Run `python3 tools/bump_version.py X.Y.Z --changelog "summary"`: it edits `plugin.json`, `marketplace.json` and `pyproject.toml` together (the docs lint fails if they disagree), refreshes `.tutor-scripts/`, and adds the `## [X.Y.Z]` section CI requires to `CHANGELOG.md`.
2. All checks green on `main`: tests (3.10/3.12/3.13), lint, docs-lint, plugin-validate.
3. `claude plugin tag plugin/generic-tutor --push` — validates that `plugin.json` and the marketplace entry agree and pushes `generic-tutor--v<version>`. The `release` workflow then re-checks the version, runs the tests, builds the zip and attaches it to a GitHub release with the changelog section as notes.
