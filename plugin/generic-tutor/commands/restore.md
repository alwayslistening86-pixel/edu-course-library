---
description: Put a learner back from a backup zip — verified first, with a safety backup before anything is replaced
argument-hint: [path-to-backup.zip]
---

@${CLAUDE_PLUGIN_ROOT}/skills/backup-restore/SKILL.md

Run the `/restore` flow described above for the backup file: $1

**Arguments:** `$1` = path to a backup zip made by `/backup`. If it is missing, list the zips in `<root>/backups/` (newest first) and ask which. Always dry-run first.
