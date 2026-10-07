# Runbook

Symptom → meaning → what to do. Start with `/doctor`; it names most of these.

## A command says "can't proceed" (gate messages)
| You see | Meaning | Do |
|---|---|---|
| course is **dormant** / locked behind a lower level | a lower-level course in your roster isn't finished yet | finish or `/drop` the lower one; `/list-courses` shows what it's waiting on |
| course is **dropped** | you paused it | `/add-course` it again — progress is kept |
| source **can't be verified** (suspended) | its rubric source stopped resolving | hold it (no cost) or discard it with no trace; `/audit` retries |
| **prerequisite** not met | a required course isn't complete | complete it first |
| course is **complete** | every stage (and exam) passed | nothing to do |
| **folder access** not confirmed | the course never had its folder confirmed | confirm when asked |
| needs generic-tutor **X.Y.Z or newer** | the library is ahead of your installed plugin | update the plugin (`claude plugin update generic-tutor`, or reinstall) |

## `/doctor` findings
| Check | Likely cause | Fix |
|---|---|---|
| `data-root` fails | wrong folder connected / no `courses/` | connect the folder that holds `courses/` |
| `deployed-scripts` fails | scripts never deployed or files deleted | run `/run <id>`; the bootstrap repairs and redeploys |
| `learner-schema` warns | a file doesn't match its schema or files disagree | take a `/backup`, then `/audit`; if a file is hand-edited, restore it |
| `history-db` fails, "newer" | the database was written by a newer plugin | update the plugin; do not delete it |
| `history-db` fails, integrity | corrupt database | `/restore` the latest backup (or delete `tutor.sqlite3`: JSON progress is unaffected, only history is lost) |
| `last-session` warns | a bookkeeping step was skipped last session | tell the tutor to run the missing step it names; nothing is back-filled automatically |
| `stale-locks` warns | a script crashed mid-write | delete the listed `.lock` files (only when no session is running) |
| `writable` fails | read-only folder or a sync client holding files | fix permissions / pause sync |
| `consent` warns | consent is `limited` or `revoked` | change it with `/profile` if unintended |

## Recovery recipes
- **A learner file is damaged:** `/restore <latest backup>` (dry-run first). `--user-id copy` restores beside the original so you can compare.
- **Lost a backup:** old backups are in `backups/` next to `profile/`; each restore also leaves a `…-pre-restore.zip`.
- **Upgrade went wrong:** scripts are in `.tutor-scripts/` and are rebuilt from the plugin on `/run`; progress files are not touched by upgrades. To roll back, install the previous plugin version; a newer-than-supported progress file is refused rather than rewritten.
- **Two sessions at once:** writes are locked per file; if one waits too long you'll see a lock timeout (it now says which process holds the lock and for how long) — retry. On a slow disk, such as a removable stick, set `EDU_LOCK_TIMEOUT` to a whole number of seconds (1 to 600; the default is 10) to let writers queue for longer.

## Reporting a problem
Include the output of `/doctor`, the plugin version (`.tutor-scripts/.manifest.json`), and what you typed. Never paste your profile folder; it holds personal data.
