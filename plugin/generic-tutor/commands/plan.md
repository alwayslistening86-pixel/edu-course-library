---
description: Compute or recompute the slot-based (non-calendar) session plan across all unlocked, active courses
argument-hint: [course_id] [target_date]
---

@${CLAUDE_PLUGIN_ROOT}/skills/journey-planner/SKILL.md

Run the `/plan` flow described above.

**Arguments:** none needed. If the learner names a real deadline for a course (`$1` = course id, `$2` = date as YYYY-MM-DD), offer to record it as an optional target and show whether the plan can meet it; otherwise plan without any date.
