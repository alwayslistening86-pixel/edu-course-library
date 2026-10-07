# ADR 0011 — The portable profile: medium, two roots, and what the engine promises

Status: **accepted (design); nothing built** (7 Oct 2026). Micro-task B-01.1 in `docs/WAVE7.md`. The owner accepted the recommendations for D1 and D2 there. Build tasks B-01.2 to B-01.10 follow from this note and no code is written until each is reached.

## Context
Learner state should travel with the learner, not the machine (ADR 0010). Today `profile/<id>/` sits under the same root as `courses/` and `.tutor-scripts/` (`tutorlib/paths.py`), JSON is written atomically, history is SQLite, and locks are files. This note says what a portable profile may live on, how the roots split, what can go wrong, and what the engine does and does not promise.

## Decision

### 1. The medium (D1)
A profile may live on a **plain folder or a removable drive**. It may **not** live in a synced folder (OneDrive, Dropbox, iCloud Drive, Google Drive and the like): a sync client can hold a file open mid-replace, copy half a database, or resurrect an old version, and the engine cannot see any of that. The engine does not forbid it (it cannot reliably tell), but the profile check (B-01.3) warns when the path looks like one, and the install guide says no.

### 2. Two roots
- The **engine root** holds `courses/` and `.tutor-scripts/`: shared, replaceable, not personal.
- The **profile root** holds `profile/<id>/`: personal, belongs to the learner.
By default the profile root is `<engine root>/profile`, so every existing install behaves as before. A separate profile root is set by `--profile-root` or `EDU_PROFILE_ROOT` (B-01.2). Scripts keep taking explicit paths from the caller; only the code that finds the roots changes.

### 3. Multi-user
Many single-user profiles plus one engine. There is no account system, no tenancy and no shared database. A learner is whoever's folder is in use; two profiles on one medium are separate folders that no script can cross (the id and containment guards in `tutorlib/ids.py` and `paths.py`, proved again on the new root in B-01.9).

### 4. Encryption (D2)
The engine does **not** encrypt the profile. Standard-library Python has no real encryption, and a home-made scheme would give false comfort. The supported answer is the operating system's: an encrypted volume (BitLocker, FileVault, LUKS or a VeraCrypt container). The profile check says what it can and cannot tell about the medium, and the install guide tells the adult to encrypt a stick that leaves the house. If a dependency is ever accepted for this, that is a new decision (it is also X-08).

## What can go wrong, and the test each needs

| # | Scenario | What the engine does today | Promise | Test (micro-task) |
|---|---|---|---|---|
| 1 | Stick pulled during a JSON write | Temp file then `os.replace`: old or new, never half (`atomic_io.write_json`) | Never a torn file | Kill at every write point; file is entirely old or new (B-01.4) |
| 2 | Stick pulled during a history insert | SQLite rollback journal; each statement is its own transaction | The row is there or not; the database passes its integrity check | Kill during insert, reopen, `PRAGMA integrity_check` (B-01.4) |
| 3 | Pulled between the JSON write and the history insert | The two are separate writes; JSON is authoritative (ADR 0004) | History may lack a row that JSON implies; it is never the other way round, and nothing is lost that progress depends on | A test that the next session tolerates the gap (B-01.4) |
| 4 | Stick on a file system with weaker rename guarantees (FAT, exFAT) | Not specified | **Not promised.** The check warns and the install guide recommends a journaling file system for the stick | The check reports the file system where the platform exposes it (B-01.3) |
| 5 | Stale temp and lock files after a pull | Temp files remain; a lock is broken after 60 s (`STALE_SECONDS`) | Leftovers are reported, then cleaned, never read as data | Reopen after a kill; leftovers listed and removed by the close step (B-01.6) |
| 6 | Stick moved to another machine with a lock still on it | A lock stores a process id and a time, no machine name | A lock from another machine is reported, not silently broken inside its timeout | Lock written by "another host" (B-01.5) |
| 7 | Engine versions differ between machines | Older engine refuses a newer file (`state.load`); newer migrates after a `.pre-migrate` backup | A clear refusal or a backed-up migration, never silent damage | One test per cell of the version matrix (B-01.7) |
| 8 | Stick lost or stolen | Plain files | Not protected by the engine; the adult encrypts the medium (section 4) | Docs only; the check says what it can tell (B-01.8) |
| 9 | Drive letters and paths differ per machine | No schema has a path field; whether the activity log or any `detail` text ever records one is not yet checked | The profile contains no absolute paths | A scan of a fixture profile after a full session for anything that looks like an absolute path (B-01.2) |
| 10 | Two sessions open the same stick at once | Per-file locks | One writer at a time per file; a second session is told | Concurrency test on the new root (B-01.4) |

## Consequences
- The engine promises **no torn files and no silent version damage**. It does not promise protection of a lost medium, durability on every file system, or safety in a synced folder.
- `profile_check.py` (B-01.3) becomes the gate before a session; `profile_close.py` (B-01.6) is the safe-eject step. Both are read-mostly and say plainly what they found.
- Nothing here changes current behaviour. With no profile root set, every path resolves as today, and the golden tests are the proof.

## Not decided
- Whether a session should refuse to start on a medium it cannot classify, or only warn (start by warning; tighten if the pilot shows trouble).
- Whether the history database should move to write-ahead logging for sturdiness. It would add `-wal` and `-shm` files to a removable medium, which is a worse trade for unplugging, so the default rollback journal stays unless B-01.4 finds a failure.
