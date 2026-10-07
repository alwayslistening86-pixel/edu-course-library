---
description: Read-only health check of the install and the learner's data — reports problems and how to fix them
argument-hint: [user_id]
---

@${CLAUDE_PLUGIN_ROOT}/skills/health-status/SKILL.md

Run the `/doctor` flow described above. Limit the learner checks to user_id: $1 if one was given.

**Arguments:** `$1` (optional) = limit the learner checks to one user id; without it every learner is checked.
