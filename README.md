# EDU course library

A personal, self-hosted tutoring system built on the **generic-tutor** plugin
for Claude/Cowork: a real academic course library (currently 62 courses,
spanning GCSE through degree level and several standalone qualifications),
taught interactively by Claude against sourced rubrics and specifications,
with per-learner progress tracking, spaced-repetition review, and an
adaptive layer that diagnoses *why* an answer was wrong rather than just
whether it was right.

This is a working personal project, not a published product. If you've
ended up here by accident: welcome, feel free to look around, but see
**License** below before reusing anything.

## What's in this repo

```
courses/            62 compiled courses — course.json, rubric.json, curriculum_map.json,
                     stage-by-stage lesson/practice/test content, exam material
plugin/generic-tutor/  Source for the generic-tutor Cowork plugin: the tutor engine itself
                     (skills, scripts, tests) — see its own README/DESIGN_NOTES.md
profile/             Per-learner progress (empty in this repo — see Privacy below)
_staging/            Course zips awaiting install, and an archive of already-installed ones
_historic/           Courses kept for reference, not offered for active study
_archive/            Retired/superseded material
```

## How it works

1. Install the `generic-tutor` plugin (built from `plugin/generic-tutor/` —
   package it with `zip -r generic-tutor.plugin .` from inside that folder,
   or grab a packaged release from this repo's Releases page) into Claude
   Cowork.
2. Connect this folder to a Cowork session ("Work in a folder").
3. `/run <learner_id>` to start or resume a learner profile, then
   `/continue <course_id>` to teach, `/add-course` to compile a new one,
   `/list-courses`, `/review`, `/audit`, and so on — see the plugin's own
   `commands/` and `skills/*/SKILL.md` for the full command surface.

Course content is compiled from real, cited sources (exam board
specifications, mark schemes, examiner reports) — every rubric entry and,
from v1.4.0, every documented misconception carries a source, or is
explicitly marked as unsourced rather than presented as if it were.

## Privacy

`profile/` holds per-learner progress once someone actually studies here —
session state, error history, confidence tracking. That's personal data, so
any real learner subfolder under `profile/` is git-ignored and never
committed (see `.gitignore`); this repo currently ships with no learner data
in it at all.

## License

Split, deliberately:
- **Course content** (`courses/`, and anything under `profile/`) is
  **all rights reserved** — see [`LICENSE`](LICENSE). It paraphrases
  copyrighted exam-board material for personal study use and isn't offered
  for reuse or redistribution.
- **The plugin itself** (`plugin/generic-tutor/` — the tutor engine's code)
  is **MIT-licensed** — see [`plugin/generic-tutor/LICENSE`](plugin/generic-tutor/LICENSE).
  Genuinely reusable if you want to build your own course library on top of
  the same engine.
