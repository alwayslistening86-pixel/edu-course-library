# Suspension handling and revival

Loaded by `/audit` and by `/drop` (for a course at `grounding_status: suspended_ungrounded`). Moved verbatim from `SKILL.md`.

## Suspension handling — held or dropped, learner's free choice, either way at no cost
A course at `grounding_status: suspended_ungrounded` does **not** count against `roster.max_incomplete_courses` from the moment it suspends — the learner isn't at fault for a source disappearing and shouldn't have it occupy the same capacity a real in-progress course would. Present the choice plainly whenever the learner encounters a suspended course (via `course-runner`'s Gate 2, or via `/audit`'s own report):

- **Held** (the default — no action required) — the enrollment sits frozen exactly as it stood, indefinitely. `/audit` keeps opportunistically re-attempting revival on every future run regardless of whether it's held or ignored; there's no forced timeline and no re-prompting the learner about it.
- **Dropped** — the learner may discard it at any time with **genuinely no trace**: delete `subjects/<course_id>.json` outright, rather than setting `roster_state: dropped` (which, everywhere else in this system, means "preserved and resumable"). This is deliberately a different operation from an ordinary `/drop`, because the learner didn't choose to pause something they were doing — content they had no way to evaluate simply stopped existing under them, and the record should reflect that as cleanly as if it had never been added. If the source is later revived, there's no reconnection back to a learner who already dropped it this way — re-enrolling later is an ordinary fresh `/add-course`, subject to the roster cap and level-lock as normal at that time.

## Revival
On each `/audit` pass, re-attempt discovery for every course at `suspended_ungrounded`, incrementing `revival_attempts` regardless of outcome. On success, run the same compare-and-log procedure the live recheck already uses (Tier 3, above) before flipping `grounding_status` back to `verified` — a revival is not exempt from the ordinary "tell the learner what changed" discipline just because it's also good news.
