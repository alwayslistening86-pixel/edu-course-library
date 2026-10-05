# Install, permissions, upgrade, uninstall

For day-to-day use see [`USER_GUIDE.md`](USER_GUIDE.md); for fixing things see [`RUNBOOK.md`](RUNBOOK.md).

## Where it works
What has actually been exercised, not what is hoped for.

| Surface | Install | Slash commands | Optional hooks | Status |
|---|---|---|---|---|
| Claude Code CLI | `claude plugin marketplace add alwayslistening86-pixel/edu-course-library`, then `claude plugin install generic-tutor@edu-course-library` | yes | possible (not shipped; see ADR 0001) | install, validate (`--strict`), update and uninstall run against the real CLI |
| Claude Code desktop / web | same marketplace | yes | possible | not separately tested |
| Claude Cowork | add the repository as a marketplace in the plugin UI, install `generic-tutor` | expected | **not available** (Cowork has no hooks) | **not tested by the maintainer**; everything the plugin needs from hooks is also done by scripts, so a missing hook costs nothing but the optional safety nets |
| Anywhere else | — | — | — | unsupported |

Needs **Python 3.10 or newer** on the machine that runs the session; the scripts use only the standard library.
Check with `python3 --version` (Windows: `py -3 --version`). `/doctor` reports the Python version it is running under and flags one that is too old; if `python3` cannot be found at all nothing can run, and the session will report the failed command: install Python from python.org (or your package manager) and start a new session.
If your system only has `py -3`, tell the session once ("use py -3 for python3"); the commands name `python3` because that is the common case.

## Windows notes
The full test suite runs on `windows-latest` in CI and passes (since v1.45.2); legacy console code pages and briefly locked files are covered by simulated tests. It has not been exercised on your actual machine, a synced folder, or a very long path. Keep the data folder (the one holding `profile/`) **outside** OneDrive, Dropbox and similar synced folders where you can: a sync client holding files open slows or fails saves, and SQLite history files can be damaged by sync. Backups are best kept in a synced or off-machine location only if you accept that they contain personal data. Paths with spaces are fine.

## Permissions
The plugin runs its scripts from the data folder's `.tutor-scripts/`. In Claude Code, to stop a prompt for every script call, allow that one directory rather than all of Python:

```json
{ "permissions": { "allow": [ "Bash(python3 <your-edu-folder>/.tutor-scripts/*)" ] } }
```

in `.claude/settings.json` (replace `<your-edu-folder>` with the real path, not `/EDU`). Do **not** allow `Bash(python3 *)` or `Bash(*)`. `erase_profile.py` refuses to act without the typed phrase `ERASE <user_id>`, and `restore_profile.py` refuses to touch an existing learner without `--replace` (and then takes a safety backup first), so an allowlist does not remove those checks; you may still prefer to leave those two prompting. Cowork asks through its own permission UI; approve the folder connection once.

## Upgrade
```
claude plugin marketplace update edu-course-library
claude plugin update generic-tutor
```
then restart the session. Scripts in the data folder are refreshed on the next `/run`; progress files are not rewritten by an upgrade. If a newer plugin changes a file's format, a migration runs once and keeps a `.pre-migrate-v<N>.bak` beside the file (run `migrate_schema.py … --dry-run` first to see what it would change). A progress file written by a *newer* plugin than the one installed is refused, never overwritten.

## Roll back
Install the previous version (`claude plugin install generic-tutor@edu-course-library` after checking out the earlier tag, or install from the tagged release zip), restart, `/run`. Files already migrated forward keep the `.pre-migrate` backup; `/restore` a backup taken before the upgrade if the older plugin refuses a newer file.

## Uninstall
`claude plugin uninstall generic-tutor`. This removes the plugin only. **Your data folder stays exactly as it is**: `profile/` (learner progress), `courses/`, `.tutor-scripts/`, `backups/`. Delete those yourself if you want them gone; to remove one learner properly use `/erase` (which also clears that learner's history database) rather than deleting files by hand. Backups may contain personal data: keep them outside any synced or shared folder.
