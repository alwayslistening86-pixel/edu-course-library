---
description: Activate a learner's profile for this session
argument-hint: [user_id]
---

@${CLAUDE_PLUGIN_ROOT}/skills/profile-kernel/SKILL.md

Run the `/run` behavior described above for user_id: $1

**Arguments:** `$1` = the learner's user id (1–64 letters, digits, `_`, `.` or `-`, starting with a letter or digit). If it is missing, list the folder names under `/EDU/profile/` and ask which one — never guess or pick a close match. An id that breaks the rule above is refused with that rule stated.
