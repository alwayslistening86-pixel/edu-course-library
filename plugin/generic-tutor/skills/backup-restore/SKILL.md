---
name: backup-restore
description: Makes a full backup of the active learner (/backup) or puts a learner back from a backup (/restore), using backup_profile.py and restore_profile.py. Backups are checksummed and stored outside the learner's folder; restore verifies before changing anything and never overwrites without a safety backup.
---

# Backup & Restore

**Contract**
- **Owns:** creating backup zips; replacing a learner folder from a verified backup.
- **Calls:** `backup_profile.py`, `restore_profile.py`.
- **Emits:** the backup's path and size; for restore, exactly what was (or would be) replaced.
- **Never:** restores over an existing learner without `--replace` and the learner's explicit yes; restores without `--dry-run` first; tells the learner a backup is "safe" without saying where it is and that it holds personal data; stores a backup inside the learner's folder.
- **Failure modes:** a script `error` (checksum mismatch, newer format, unknown learner) is shown verbatim and nothing has changed — say so.

## `/backup`
For the active learner. Run:
```
python3 /EDU/.tutor-scripts/backup_profile.py <the /EDU/profile/ dir> <active user_id>
```
Tell the learner where the zip is (`zip_path`), how many files and how big. Explain in one sentence that it is a full copy of their progress and history (personal data), kept **outside** their learner folder by design so `/erase` does not delete it, and that for real protection they should copy it somewhere off this machine/folder (another drive or cloud storage they trust). Suggest a backup before `/audit` repairs, before upgrading the plugin, and now and then.

## `/restore <path-to-backup.zip>`
1. **Dry run first**, always:
   ```
   python3 /EDU/.tutor-scripts/restore_profile.py <the /EDU/profile/ dir> <backup.zip> --dry-run
   ```
   Read it back plainly: which learner, when the backup was made, how many files, and whether that learner already exists.
2. If the learner **does not exist**, restore: same command without `--dry-run`.
3. If the learner **exists**, restoring replaces their current progress with the backup's. Explain that, say a safety backup of the current state is taken automatically first, and ask for an explicit yes. Only then run with `--replace`. Report the `safety_backup` path so they can undo it.
4. To look at a backup without touching the live profile: `--user-id <other-id>` restores it beside the original.
5. After a successful restore run `/doctor` for that learner and report the result.
Learner-supplied paths and ids are passed as separate arguments to the script, never assembled from their message into a shell string.
