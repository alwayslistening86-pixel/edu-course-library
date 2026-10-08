# generic-tutor — an adaptive tutoring engine with state you can trust

An engine for teaching any subject from a real, cited source, to one or many learners, and for knowing — reliably — what each learner has and has not learned. It builds the course itself from the specification or syllabus you point it at; nothing is preloaded, and nothing ties it to one country's curriculum. It teaches through Claude (Cowork or Claude Code) today, and is built so the teaching voice is the replaceable part and the record of progress is not.

The idea that shapes everything: **the model talks, scripts decide and write.** Markdown skills tell Claude when to do things and how to teach; stdlib-only Python scripts make every deterministic decision (gates, spaced-review maths, mastery, consent, ordering) and perform every state write. A lesson can go wrong in conversation without corrupting a learner's record.

## There are no courses here, on purpose: the engine builds them
This repository holds the engine only. You will not find a maths or history course in it, and that is by design, not an omission. Courses are built for each learner by the **course compiler** inside the engine, when you set a learner up:
- **`/add-course <subject>` builds a course.** It reads the published specification or syllabus, shows you what it found, and once you choose builds the course from it: a rubric transcribed from the real source (never invented), the specification broken into items, lesson, practice and test for each stage, and a coverage report saying what the course does and does not cover. If it cannot find a real source it stops and says so; it never builds a provisional course.
- **It checks before it builds.** It reuses a course already in your folder rather than making a duplicate, applies the roster and level rules first, and publishes whole or not at all.
- **It keeps courses current.** `/audit` re-checks structure, grounding and coverage and adds question banks and misconceptions, each labelled by where it came from. A live recheck notices when a source changes, and a course whose source can no longer be verified is suspended, never quietly taught.
- **Why courses are not shipped.** A course paraphrases an exam board's specification and mark schemes, which belong to their publishers, and which board and year a learner needs is their own choice. So courses live outside this public repository: each household or school builds its own, keeps its library privately, and can move a verified course between machines as a bundle.

So a first run is `/add-profile` then `/add-course "gcse maths"`: the compiler reads the specification online, builds the course, and the learner is ready to start. A compiled course is only as good as its source and the reading of it, so look at the coverage report it gives you and run `/audit`; learning outcomes have not yet been measured (see the limits below).

## What it does
- **Teaches against a source.** Courses carry a sourced rubric, an itemised specification and a coverage check; a live recheck notices when the source changes. A course that cannot be verified is suspended, never quietly taught.
- **Tracks and adapts.** Per-learner progress, per-item mastery, a diagnosis of *why* an answer was wrong (slip, missing prerequisite, misconception, wrong procedure, misread), worked examples that fade as mastery grows, interleaved practice, spaced review, a hint ladder that keeps the answer for last, and honest "am I ready?" readouts that never pretend to be a grade.
- **Keeps itself honest.** Consent enforced in code, atomic writes and locks, a session ledger that flags a missed bookkeeping step, schema and invariant checks, an injection scanner for web-derived content, checksummed backups and erase-on-request. Optional Claude Code hooks add a second net.
- **Looks after the library.** `/audit` checks structure, grounding and coverage and has an enrichment pass for question banks and misconceptions, each labelled by provenance (board-documented where a board publishes examiner material, learner-observed from the library's own data, or plainly "plausible"); the compile gate refuses leftover template text, and a check flags quotation beyond the paraphrase policy; a course moves between libraries as a verified bundle with no learner data in it; `/doctor` checks a learner's setup; a read-only toolkit shows status without opening a session.
- **Speaks the learner's language.** Spelling follows the learner's locale, and key terms can be glossed in a home language.
- **Measures itself.** A dev-only eval suite (grading, safety, injection, diagnosis, hints, fading, accessibility, gates and more) scores skill changes against reference answers that need no human marker, and three self-authored sample courses mean none of it needs private content.

## Where it is going
Accepted in direction, not yet designed in detail ([ADR 0010](docs/adr/0010-proposed-roles-and-portable-profile.md), tasks B-01 to B-06): a **portable profile** (learner state travels with the learner, so one shared engine serves many people without tenancy), a **local interface** over the scripts, and **role-separated models** (a local tutor voice, a stronger examiner, a staff channel, with Claude as the fallback teacher).

## Honest limits
Learning outcomes have not been measured; that needs real learners over time. Sourced misconceptions exist only where a source publishes them, and courses built before that step need an audit enrichment run. The evals are synthetic and easy. Windows is verified only on CI, and the Cowork surface is untested. The teaching loop is Claude-shaped today.

## Install
```
claude plugin marketplace add alwayslistening86-pixel/edu-course-library
claude plugin install generic-tutor@edu-course-library
```
Each version is also on the [Releases page](https://github.com/alwayslistening86-pixel/edu-course-library/releases) as a `.plugin` zip. In Claude Cowork add the same GitHub repository as a marketplace in the plugin UI, then install `generic-tutor`. Needs Python 3.10+ and a connected folder with an empty `courses/` inside it (the folder starts empty; `/add-course` fills it). Then: `/add-profile <name>` → `/add-course` → `/plan` → each session `/run <name>` and `/continue <course>`. `/help` lists everything; `/doctor` finds problems. Details: [`docs/INSTALL.md`](docs/INSTALL.md), [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md), [`docs/RUNBOOK.md`](docs/RUNBOOK.md).

## Repository map
| Path | What |
|---|---|
| `plugin/generic-tutor/` | the plugin: `skills/`, `commands/`, `scripts/`, `hooks/`, `tests/`, `evals/`, shipped `docs/` |
| `.tutor-scripts/` | deployed copy of the scripts (CI fails if it drifts; never hand-edit) |
| `.claude-plugin/marketplace.json` | makes this repository installable |
| `docs/` | plan, task list, architecture, ADRs, pedagogy, install, user guide, runbook |
| `tools/` | docs lint, build, release notes, context budget, task status |
| `.github/` | CI, release and reusable content-validation workflows |

Courses are data, built by the compiler and kept outside this repository so that licensed or paraphrased source material never lands here; the engine reads them through a defined folder layout ([content contract](plugin/generic-tutor/docs/CONTENT_CONTRACT.md)). Learner data is never committed ([privacy](plugin/generic-tutor/docs/PRIVACY.md)).

## Working on it
Where things stand and what comes next: [`docs/ROADMAP.md`](docs/ROADMAP.md). Tasks and waves: [`docs/TASKS.md`](docs/TASKS.md) against [`docs/PLAN.md`](docs/PLAN.md). Design: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/adr/`](docs/adr/README.md), [`plugin/generic-tutor/docs/DATA_MODEL.md`](plugin/generic-tutor/docs/DATA_MODEL.md). History: [`CHANGELOG.md`](CHANGELOG.md). How to contribute: [`CONTRIBUTING.md`](CONTRIBUTING.md), [`docs/CONTRIBUTING-DEV.md`](docs/CONTRIBUTING-DEV.md) and `CLAUDE.md`. Eval method and baselines: [`plugin/generic-tutor/evals/README.md`](plugin/generic-tutor/evals/README.md).

## License
The plugin (`plugin/generic-tutor/`) is **MIT** — [`plugin/generic-tutor/LICENSE`](plugin/generic-tutor/LICENSE). Course content and learner data are **all rights reserved** and are not in this repository. See [`NOTICE`](NOTICE).
