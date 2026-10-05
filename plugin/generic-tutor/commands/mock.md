---
description: A timed-style practice paper from the course's question bank, marked honestly; recorded as practice, never as a grade prediction
argument-hint: [course_id] [marks] [minutes]
---

@${CLAUDE_PLUGIN_ROOT}/skills/exam-simulator/SKILL.md

Run the `/mock` flow described above for the course: $1 (marks: $2, minutes: $3)

**Arguments:** `$1` = a course id the learner is enrolled in (if missing, list their courses and ask); `$2` (optional) = target marks, default 40; `$3` (optional) = minutes allowed, default about 1.2 minutes per mark.
