# EDU course library

A personal, self-hosted tutoring system built on the **generic-tutor** plugin
for Claude/Cowork: a real academic course library (62 courses at last count, kept in a
private companion repo — GCSE through degree level plus several standalone
qualifications),
taught interactively by Claude against sourced rubrics and specifications,
with per-learner progress tracking, spaced-repetition review, and an
adaptive layer that diagnoses *why* an answer was wrong rather than just
whether it was right. It also ships an optional read-only desktop
toolkit — a small GUI/CLI for backup, health and progress checks from
your own machine, without opening a session.

This is a working personal project, not a published product. If you've
ended up here by accident: welcome, feel free to look around, but see
**License** below before reusing anything.

## What's in this repo (and what isn't, anymore)

As of 30 Sep 2026, the actual course content — `courses/`, `_staging/`,
`_historic/` — lives in a **private** companion repo, `edu-courses-private`,
not here. It paraphrases copyrighted exam-board specifications and mark
schemes, which has no good reason to sit in a public repo. This repo is now
just the tutor engine: genuinely reusable code, MIT-licensed, with nothing
copyright-sensitive in it.

```
plugin/generic-tutor/  Source for the generic-tutor Cowork plugin: the tutor engine itself
                     (skills, scripts, tests) — see its own README/DESIGN_NOTES.md
.tutor-scripts/      Deployed runtime copy of plugin/generic-tutor/scripts/, kept in sync
                     by bootstrap_scripts.py — what actually runs against a real install
.github/             CI: runs the plugin's test suite and checks .tutor-scripts/ hasn't
                     drifted from the plugin source. scripts/validate_courses.py is
                     run from the private repo's CI against its own courses/
profile/             Per-learner progress (empty in this repo — see Privacy below)
```

`courses/`, `_staging/`, and `_historic/` still exist locally on a real
install (the plugin reads them straight off disk) — they're just no longer
tracked by *this* repo's git, and their prior history has been removed from
it too. See `edu-courses-private` (private; access on request) if you're
me and need them.

## How it works

1. Install the `generic-tutor` plugin (built from `plugin/generic-tutor/` —
   package it with `zip -r generic-tutor.plugin .` from inside that folder) into Claude
   Cowork.
2. Connect a real course-library folder (containing `courses/` — from the
   private repo, or your own) to a Cowork session ("Work in a folder").
3. `/run <learner_id>` to start or resume a learner profile, then
   `/continue <course_id>` to teach, `/add-course` to compile a new one,
   `/list-courses`, `/review`, `/audit`, and so on — see the plugin's own
   `commands/` and `skills/*/SKILL.md` for the full command surface.
4. Optional: once installed, the toolkit lands at `.tutor-scripts/toolkit/`
   — see that folder's own README for how to use it.

Course content (wherever it lives) is compiled from real, cited sources
(exam board specifications, mark schemes, examiner reports) — every rubric
entry carries a source. A per-item misconceptions layer (schema defined
since v1.4.0, for common wrong-answer patterns with their own sourced
corrections) exists but isn't seeded for any course yet — an open backlog
item, not a claim made about current content.

## Privacy

`profile/` holds per-learner progress once someone actually studies here —
session state, error history, confidence tracking. That's personal data, so
any real learner subfolder under `profile/` is git-ignored and never
committed (see `.gitignore`); this repo currently ships with no learner data
in it at all.

## License

- **The plugin** (`plugin/generic-tutor/` — the tutor engine's code, the
  only content-bearing thing left in this repo) is **MIT-licensed** — see
  [`plugin/generic-tutor/LICENSE`](plugin/generic-tutor/LICENSE). Genuinely
  reusable if you want to build your own course library on top of the same
  engine.
- **Course content** (`courses/`, and anything under `profile/`) was **all
  rights reserved** here and now lives, under the same terms, in the
  private `edu-courses-private` repo — it paraphrases copyrighted
  exam-board material for personal study use and isn't offered for reuse or
  redistribution.
