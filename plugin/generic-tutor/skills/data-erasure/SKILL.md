---
name: data-erasure
description: Permanently deletes the active learner's data on request via /erase, giving real effect to consent.status "revoked" rather than leaving it as a flag nothing acts on. Deletion is done by erase_profile.py after the learner types an exact confirmation phrase — irreversible.
---

# Data Erasure

**Contract**
- **Owns:** deletion of `/EDU/profile/<user_id>/` (nothing else).
- **Calls:** `erase_profile.py`.
- **Never:** deletes on an inferred or one-word request; touches `/EDU/courses/`; touches another learner; deletes by any means other than the script.

## Invocation
`/erase`, for the currently active learner only. Never runs on inferred intent.

## Procedure
1. **Show what will go.** Run the script in dry-run mode and read the result to the learner in plain words (profile, N progress files, review decks, and the history database if `has_history_db`):
   ```
   python3 /EDU/.tutor-scripts/erase_profile.py <the /EDU/profile/ dir> <active user_id> --dry-run
   ```
2. **Ask for the phrase.** The learner must type exactly `ERASE <user_id>` (the script returns it as `required_confirmation`). A "yes", "ok" or any near-miss is not confirmation — say so and ask again; do not proceed.
3. **Erase** only after the exact phrase arrives:
   ```
   python3 /EDU/.tutor-scripts/erase_profile.py <the /EDU/profile/ dir> <active user_id> --confirm "ERASE <user_id>"
   ```
4. Report the result from the script's output (`erased: true`, file count). If it returns an `error`, say what it said and that nothing was deleted.

## What is removed / kept
Removed: the learner's entire folder — `student_profile.json`, every `subjects/<course_id>.json`, every review deck, `tutor.sqlite3` (the history database) and any lock/backup files in it. This is stronger than `consent.status: "revoked"`, which only stops future writes (enforced in code by every script).

Kept: shared course content under `/EDU/courses/` (it belongs to no single learner; a course with no remaining enrolments is surfaced by `course-auditor`, not deleted). Backups or exports the learner saved elsewhere are theirs to delete — mention this.

## After erasure
There is no active profile; the learner starts again with `/add-profile`. Nothing treats an erased profile as recoverable, by design.
