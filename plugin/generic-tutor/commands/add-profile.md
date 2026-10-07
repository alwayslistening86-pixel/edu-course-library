---
description: Create a new learner profile alongside existing ones, then activate it
argument-hint: [user_id]
---

@${CLAUDE_PLUGIN_ROOT}/skills/profile-kernel/SKILL.md
@${CLAUDE_PLUGIN_ROOT}/skills/profile-kernel/intake.md
@${CLAUDE_PLUGIN_ROOT}/skills/profile-kernel/profile-schema.md

Run the `/add-profile` behavior described above for user_id: $1

**Arguments:** `$1` = the new learner's id (1–64 letters, digits, `_`, `.` or `-`, starting with a letter or digit). If it is missing, ask what short id to use. If a folder with that id already exists, say so and offer `/run` instead of overwriting.
