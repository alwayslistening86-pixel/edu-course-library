# Listing courses (`/list-courses`)

Loaded by `/list-courses` (and read from `SKILL.md` when a learner asks for course status).

## `/list-courses [--status S] [--level N] [--standalone] [--compact]`
Run `python3 /EDU/.tutor-scripts/list_courses.py <the active learner's folder> <the /EDU/courses/ dir> [flags]` and present its rows; do not rebuild the list from files. Flags: `--status` (`active`, `dormant`, `test_pending_convergence`, `dropped`, `complete`, `not_enrolled`), `--level N`, `--standalone`, `--compact` (id, level, state, stages passed of total). Unknown flags or values: say what is accepted and run nothing.

Show, per course: the level, or **standalone** instead; a `declared` `level_basis` is always labelled "declared", never as coming from a framework. The learner's state (a finished theory-only course reads "complete (theory-only)"); stages passed of total; coverage as `full`, `partial` (items taught of itemised) or `unverified`; prerequisites (any-of entries as "one of …") and whether each is met; practical stages; `grounding_status` if suspended; one provenance line (`provenance`: source and version, built on, last change with its title, last live recheck; skip nulls). End with the counts by state.

A `retiring` course is labelled so. `/EDU/_historic/` courses are not listed. "Let's carry on with Contract Law" is redirected to `/continue <course_id>`, not run as a listing.
