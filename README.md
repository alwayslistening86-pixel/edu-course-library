# generic-tutor — an adaptive tutoring engine with state you can trust

An engine for teaching any subject from a real, cited source, to one or many learners, and for knowing — reliably — what each learner has and has not learned. It builds the course itself from the specification or syllabus you point it at; nothing is preloaded, and nothing ties it to one country's curriculum. It teaches through Claude (Cowork or Claude Code) today, and is built so the teaching voice is the replaceable part and the record of progress is not.

The idea that shapes everything: **the model talks, scripts decide and write.** Markdown skills tell Claude when to do things and how to teach; stdlib-only Python scripts make every deterministic decision (gates, spaced-review maths, mastery, consent, ordering) and perform every state write. A lesson can go wrong in conversation without corrupting a learner's record.

## What it does
- **Teaches against a source.** Courses carry a sourced rubric, an itemised specification and a coverage check; a live recheck notices when the source changes. A course that cannot be verified is suspended, never quietly taught.
- **Tracks and adapts.** Per-learner progress, per-item mastery, a diagnosis of *why* an answer was wrong (slip, missing prerequisite, misconception, wrong procedure, misread), worked examples that fade as mastery grows, interleaved practice, spaced review, a hint ladder that keeps the answer for last, and honest "am I ready?" readouts that never pretend to be a grade.
- **Keeps itself honest.** Consent enforced in code, atomic writes and locks, a session ledger that flags a missed bookkeeping step, schema and invariant checks, an injection scanner for web-derived content, checksummed backups and erase-on-request. Optional Claude Code hooks add a second net.
- **Looks after the library.** `/audit` checks structure, grounding and coverage and has an enrichment pass for question banks and misconceptions; `/doctor` checks a learner's setup; a read-only toolkit shows status without opening a session.
- **Measures itself.** A dev-only eval suite (grading, safety, injection, diagnosis, hints, fading, accessibility, gates and more) scores skill changes against reference answers that need no human marker, and three self-authored sample courses mean none of it needs private content.

## Where it is going
Accepted in direction, not yet designed in detail ([ADR 0010](docs/adr/0010-proposed-roles-and-portable-profile.md), tasks B-01 to B-06): a **portable profile** (learner state travels with the learner, so one shared engine serves many people without tenancy), a **local interface** over the scripts, and **role-separated models** (a local tutor voice, a stronger examiner, a staff channel, with Claude as the fallback teacher).

## Honest limits
Learning outcomes have not been measured; that needs real learners over time. The evals are synthetic and easy. Windows is verified only on CI, and the Cowork surface is untested. The teaching loop is Claude-shaped today.

## Install
```
claude plugin marketplace add alwayslistening86-pixel/edu-course-library
claude plugin install generic-tutor@edu-course-library
```
In Claude Cowork add the same GitHub repository as a marketplace in the plugin UI, then install `generic-tutor`. Needs Python 3.10+ and a connected folder containing `courses/`. Then: `/add-profile <name>` → `/add-course` → `/plan` → each session `/run <name>` and `/continue <course>`. `/help` lists everything; `/doctor` finds problems. Details: [`docs/INSTALL.md`](docs/INSTALL.md), [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md), [`docs/RUNBOOK.md`](docs/RUNBOOK.md).

## Repository map
| Path | What |
|---|---|
| `plugin/generic-tutor/` | the plugin: `skills/`, `commands/`, `scripts/`, `hooks/`, `tests/`, `evals/`, shipped `docs/` |
| `.tutor-scripts/` | deployed copy of the scripts (CI fails if it drifts; never hand-edit) |
| `.claude-plugin/marketplace.json` | makes this repository installable |
| `docs/` | plan, task list, architecture, ADRs, pedagogy, install, user guide, runbook |
| `tools/` | docs lint, build, release notes, context budget, task status |
| `.github/` | CI, release and reusable content-validation workflows |

Courses are data, kept outside this repository so that licensed or paraphrased source material never lands here; the engine reads them through a defined folder layout ([content contract](plugin/generic-tutor/docs/CONTENT_CONTRACT.md)). Learner data is never committed ([privacy](plugin/generic-tutor/docs/PRIVACY.md)).

## Working on it
Tasks and waves: [`docs/TASKS.md`](docs/TASKS.md) against [`docs/PLAN.md`](docs/PLAN.md). Design: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/adr/`](docs/adr/README.md), [`plugin/generic-tutor/docs/DATA_MODEL.md`](plugin/generic-tutor/docs/DATA_MODEL.md). History: [`CHANGELOG.md`](CHANGELOG.md). How to contribute: [`CONTRIBUTING.md`](CONTRIBUTING.md), [`docs/CONTRIBUTING-DEV.md`](docs/CONTRIBUTING-DEV.md) and `CLAUDE.md`. Eval method and baselines: [`plugin/generic-tutor/evals/README.md`](plugin/generic-tutor/evals/README.md).

## License
The plugin (`plugin/generic-tutor/`) is **MIT** — [`plugin/generic-tutor/LICENSE`](plugin/generic-tutor/LICENSE). Course content and learner data are **all rights reserved** and are not in this repository. See [`NOTICE`](NOTICE).
