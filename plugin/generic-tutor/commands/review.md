---
description: Run any due spaced-repetition flashcards on demand, across all active courses
argument-hint: [course_id] [stage_id]
---

@${CLAUDE_PLUGIN_ROOT}/skills/review-scheduler/SKILL.md

Run the `/review` flow described above.

**Arguments:** `$1` (optional) = limit the session to one course; `$2` (optional) = one stage of it. Without arguments the session covers every course that may draw slots, interleaved.
