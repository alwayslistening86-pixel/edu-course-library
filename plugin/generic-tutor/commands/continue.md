---
description: Resume a course — check grounding/level-lock/convergence gates, run any due spaced review, then teach the current stage/phase
argument-hint: [course_id]
---

@${CLAUDE_PLUGIN_ROOT}/skills/course-runner/SKILL.md
@${CLAUDE_PLUGIN_ROOT}/skills/tutor-core/SKILL.md
@${CLAUDE_PLUGIN_ROOT}/skills/review-scheduler/SKILL.md
@${CLAUDE_PLUGIN_ROOT}/skills/stage-recap/SKILL.md

Run the `/continue` behavior described above for course_id: $1

**Arguments:** `$1` = a course id. If it is missing, show the learner's live courses (from `/list-courses`) and ask which; if exactly one is live, confirm it rather than assuming. An unknown course id gets the list of valid ones.
