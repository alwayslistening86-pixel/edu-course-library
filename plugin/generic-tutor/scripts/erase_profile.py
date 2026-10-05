#!/usr/bin/env python3
"""
erase_profile.py -- irreversible deletion of one learner's data (K-27, C-05).

Replaces model-driven deletion with a deterministic, checkable procedure.

    python3 erase_profile.py <profile_root> <user_id> [--confirm "ERASE <user_id>"] [--dry-run]

Without --confirm (or with --dry-run) nothing is deleted: the script reports
exactly what WOULD be removed so the learner can be shown it first. Deletion
requires the exact phrase `ERASE <user_id>` -- typed by the learner, never
inferred. Removes the whole <profile_root>/<user_id>/ tree: student_profile.json,
subjects/ (progress + review decks), tutor.sqlite3 (+ -wal/-shm), any .lock/.bak
files. Refuses a user_id that is not a valid id, a learner folder that is a
symlink, or a path that resolves outside <profile_root>. Shared course content
is never touched. Backups or exports the learner saved elsewhere are theirs.

Exit 0 on success / dry-run, 1 on refusal or error.
"""
import json
import os
import shutil
import sys

from tutorlib import cli, paths


def _inventory(d):
    files = []
    for dp, _dn, fn in os.walk(d):
        for f in fn:
            full = os.path.join(dp, f)
            files.append({"path": os.path.relpath(full, d), "bytes": os.path.getsize(full) if not os.path.islink(full) else 0})
    return sorted(files, key=lambda x: x["path"])


def erase(profile_root, user_id, confirm=None, dry_run=False):
    try:
        d = paths.learner_dir(profile_root, user_id)
    except ValueError as e:
        return {"erased": False, "error": str(e)}
    if not os.path.isdir(d):
        return {"erased": False, "error": f"no profile folder for {user_id!r}"}
    inventory = _inventory(d)
    report = {"user_id": user_id, "files": inventory, "file_count": len(inventory),
              "has_history_db": any(f["path"].startswith("tutor.sqlite3") for f in inventory)}
    expected = f"ERASE {user_id}"
    if dry_run or confirm is None:
        return {**report, "erased": False, "dry_run": True, "required_confirmation": expected}
    if confirm != expected:
        return {**report, "erased": False, "error": f"confirmation must be exactly {expected!r}"}
    shutil.rmtree(d)
    return {**report, "erased": True}


def main(argv):
    args = [a for a in argv if a != "--dry-run"]
    dry = "--dry-run" in argv
    confirm = None
    if "--confirm" in args:
        i = args.index("--confirm")
        if i + 1 >= len(args):
            print(json.dumps({"erased": False, "error": "--confirm needs a value"}))
            return 1
        confirm = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        print(json.dumps({"error": 'usage: erase_profile.py <profile_root> <user_id> [--confirm "ERASE <user_id>"] [--dry-run]'}))
        return 1
    result = erase(args[0], args[1], confirm, dry)
    print(json.dumps(result, indent=2))
    return 0 if "error" not in result else 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
