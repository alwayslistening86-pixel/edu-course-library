---
description: Drop a course — preserves progress and frees roster capacity. For a suspended (ungrounded) course, use this to discard it entirely with no trace instead.
argument-hint: [course_id]
---

@${CLAUDE_PLUGIN_ROOT}/skills/journey-planner/drop.md
@${CLAUDE_PLUGIN_ROOT}/skills/course-auditor/suspension.md

Run the `/drop` flow described in the Journey Planner skill for course_id: $1. If course_id is at grounding_status suspended_ungrounded, follow the Course Auditor skill's suspension-drop procedure instead.
