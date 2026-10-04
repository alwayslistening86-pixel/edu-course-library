# Contributing

Personal project, but changes follow the same rules so the history stays trustworthy.

1. Pick a task from [`docs/TASKS.md`](docs/TASKS.md) (or add one with a new ID first). One task = one PR; prefix the title with the ID.
2. Branch from `main`; short-lived branches, squash merge.
3. Run the suite: `cd plugin/generic-tutor && python3 -m unittest discover tests`.
4. If you touch `plugin/generic-tutor/scripts/`, refresh `.tutor-scripts/` (see `CLAUDE.md`); CI fails on drift.
5. Plugin behaviour change: bump the version in `plugin.json` and record it in `DESIGN_NOTES.md`.
6. Schema change: add a migration and a test; note the rollback path in the PR.
7. No learner data, no copyrighted exam-board text.
