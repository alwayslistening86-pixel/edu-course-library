# Listing courses (`/list-courses`)

Loaded by `/list-courses` (and read from `SKILL.md` when a learner asks for course status).

## `/list-courses [--status S] [--level N] [--standalone] [--compact]`
Run `python3 /EDU/.tutor-scripts/list_courses.py <the active learner's folder> <the /EDU/courses/ dir> [flags]` and present its rows; do not rebuild the list from files. Flags: `--status` (`active`, `dormant`, `test_pending_convergence`, `dropped`, `complete`, `not_enrolled`), `--level N`, `--standalone`, `--compact` (id, level, state, stages passed of total). Unknown flags or values: say what is accepted and run nothing.

Show, per course: the level, or **standalone** instead; a level whose `level_basis` is `declared` is always labelled "declared", never presented as coming from a framework. The learner's state (a finished theory-only course reads "complete (theory-only)"); stages passed of total; coverage as `full`, `partial` (items taught of itemised) or `unverified`, so it is clear which courses are known to cover their specification; prerequisites (any-of entries as "one of …") and whether each is met; practical stages; `grounding_status` if suspended. End with the counts by state.

Courses in `/EDU/_historic/` are not for learning and are not listed. A natural-language "let's carry on with Contract Law" is redirected to `/continue <course_id>`, not run as a listing.
