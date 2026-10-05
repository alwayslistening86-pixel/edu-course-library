# EDU course library

A personal, self-hosted tutoring system: the **generic-tutor** plugin for Claude (Cowork / Claude Code) teaches real academic courses — GCSE through degree level and standalone qualifications — against sourced rubrics and specifications, tracks each learner's progress, schedules spaced review, and diagnoses *why* an answer was wrong, not just whether it was.

This repository is the **engine** (MIT-licensed, nothing copyright-sensitive). The course content paraphrases exam-board material and lives in a private companion repository, `edu-courses-private`. See [`plugin/generic-tutor/docs/CONTENT_CONTRACT.md`](plugin/generic-tutor/docs/CONTENT_CONTRACT.md) for the interface between the two.

## Install
```
claude plugin marketplace add alwayslistening86-pixel/edu-course-library
claude plugin install generic-tutor@edu-course-library
```
In Claude Cowork add the same GitHub repository as a marketplace in the plugin UI, then install `generic-tutor`. Needs Python 3.10+ on the machine (the plugin's scripts do the bookkeeping) and a connected folder containing `courses/`. Or build the zip yourself: `python3 tools/build_plugin.py`.

Then: `/add-profile <name>` → `/add-course` → `/plan` → each session `/run <name>` and `/continue <course>`. `/help` lists everything; `/doctor` tells you if anything is wrong. Full walk-through: [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md); when something breaks: [`docs/RUNBOOK.md`](docs/RUNBOOK.md).

## How it works, in one paragraph
Markdown **skills and commands** tell Claude *when* to do things and *how to talk*; stdlib-only Python **scripts** make every deterministic decision and perform every state write (gates, spaced-repetition maths, mastery, consent, backups). State is plain JSON per learner plus an append-only SQLite history. Safety nets that don't depend on the model remembering: atomic writes and file locks, consent enforced in code, a session ledger that flags a missed bookkeeping step, schema and invariant checks, an injection scanner for web-derived content, and checksummed backups. Details: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`plugin/generic-tutor/docs/DATA_MODEL.md`](plugin/generic-tutor/docs/DATA_MODEL.md), decisions in [`docs/adr/`](docs/adr/README.md).

## Is it any good? (evidence, not claims)
Behaviour is checked by a dev-only eval suite (`plugin/generic-tutor/evals/`): grading, safety, injection-resistance, error diagnosis and gate conformance, with reference answers that need no human marker. Current baselines and their limits are in [`plugin/generic-tutor/evals/README.md`](plugin/generic-tutor/evals/README.md). Learning *outcomes* have not been measured yet — that needs real learner data.

## Repository map
| Path | What |
|---|---|
| `plugin/generic-tutor/` | the plugin: `skills/`, `commands/`, `scripts/`, `tests/`, `evals/`, shipped `docs/` |
| `.tutor-scripts/` | deployed copy of the scripts (CI fails if it drifts; never hand-edit) |
| `.claude-plugin/marketplace.json` | makes this repository installable |
| `docs/` | plan, task list, architecture, ADRs, pedagogy rationale, user guide, runbook |
| `tools/` | docs lint, build, release notes, context budget, generated command reference |
| `.github/` | CI, release and reusable content-validation workflows |

## Contributing / status
Work is tracked in [`docs/TASKS.md`](docs/TASKS.md) against [`docs/PLAN.md`](docs/PLAN.md); history in [`CHANGELOG.md`](CHANGELOG.md); how to work on it in [`CONTRIBUTING.md`](CONTRIBUTING.md) and `CLAUDE.md`. Learner data (`profile/<id>/`) is never committed — see [`plugin/generic-tutor/docs/PRIVACY.md`](plugin/generic-tutor/docs/PRIVACY.md).

## License
The plugin (`plugin/generic-tutor/`) is **MIT** — [`plugin/generic-tutor/LICENSE`](plugin/generic-tutor/LICENSE). Course content (`courses/`) and learner data are **all rights reserved** and are not in this repository. See [`NOTICE`](NOTICE) for attributions.
