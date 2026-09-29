---
name: data-export
description: Bundles the active learner's global profile and every subject's progress into one exportable file, on request via /export. Read-only — never modifies anything it reads.
---

# Data Export

## Invocation
`/export`, for the currently active learner only. Never runs on inferred intent, and never bundles another learner's data even if their `user_id` is known.

## What's included
- The full `student_profile.json` (identity, preferences, learning signals, availability, roster settings, `highest_level_cleared`).
- Every `subjects/<course_id>.json` belonging to this learner, including `dropped` ones (preserved history), but not a suspended-and-erased course, which by definition no longer exists to export.
- Review-deck contents (`review-scheduler`'s files), since spaced-repetition scheduling state is part of the learner's own record.

## What's not included
Shared course content (`/EDU/courses/`) — that's the same for every learner and isn't personal data to export. `change.md` entries — those describe the course, not the learner.

## Output
A single structured file (JSON, or handed to the docx/pdf tooling available in this environment if the learner wants something readable rather than raw), delivered as a normal file hand-off. This is a read-only operation — nothing in `/EDU/` is modified by running it.
