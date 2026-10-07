#!/usr/bin/env python3
"""
restore_profile.py -- put a learner back from a backup_profile.py zip (E-24, C-08).

    python3 restore_profile.py <profile_root> <backup.zip> [--user-id <id>] [--replace] [--dry-run]

Safe by construction:
  1. Everything is verified BEFORE anything on disk changes: manifest present and supported, every listed
     file present with the recorded sha256, no unlisted members, no absolute or `..` paths (zip-slip).
  2. By default it refuses to touch an existing learner folder. With --replace it first takes a safety
     backup of the current folder (`<id>-backup-<ts>-pre-restore.zip` in the backups folder), then swaps
     the restored copy in; if anything fails midway the original is still there.
  3. The restored copy is built in a temporary sibling folder and renamed into place, so a crash never
     leaves a half-restored learner.
  --dry-run verifies and reports what would happen without writing.
  --user-id restores under a different id (e.g. to inspect a backup beside the live profile).

A backup written by a NEWER plugin (format_version above what this script knows) is refused.
"""
import hashlib
import json
import os
import shutil
import sys
import zipfile

import backup_profile
from tutorlib import atomic_io, cli, ids, paths

SUPPORTED_FORMAT = backup_profile.FORMAT_VERSION


def verify_zip(zip_path):
    """Return (manifest, error). Checks structure and checksums without extracting anything."""
    try:
        z = zipfile.ZipFile(zip_path)
    except (OSError, zipfile.BadZipFile) as e:
        return None, f"cannot open backup: {e}"
    with z:
        try:
            manifest = json.loads(z.read("manifest.json"))
        except (KeyError, ValueError):
            return None, "backup has no readable manifest.json"
        if manifest.get("kind") != "learner-backup":
            return None, "not a learner backup (wrong manifest kind)"
        if not isinstance(manifest.get("format_version"), int) or manifest["format_version"] > SUPPORTED_FORMAT:
            return None, f"backup format {manifest.get('format_version')!r} is newer than this plugin understands ({SUPPORTED_FORMAT}); update the plugin"
        try:
            ids.validate(manifest.get("user_id"), "user_id in backup")
        except ValueError as e:
            return None, str(e)
        listed = {f["name"]: f for f in manifest.get("files", [])}
        members = {n for n in z.namelist() if n != "manifest.json" and not n.endswith("/")}
        for n in members | set(listed):
            parts = n.split("/")
            if n.startswith("/") or ".." in parts or "\\" in n or parts[0] != "learner":
                return None, f"unsafe or unexpected path in backup: {n!r}"
        if members != set(listed):
            return None, f"backup contents do not match its manifest (extra: {sorted(members - set(listed))[:3]}, missing: {sorted(set(listed) - members)[:3]})"
        for n, f in sorted(listed.items()):
            data = z.read(n)
            if hashlib.sha256(data).hexdigest() != f.get("sha256") or len(data) != f.get("bytes"):
                return None, f"checksum mismatch for {n} - the backup is damaged or was modified"
    return manifest, None


def restore(profile_root, zip_path, user_id=None, replace=False, dry_run=False, backups_dir=None):
    manifest, err = verify_zip(zip_path)
    if err:
        return {"restored": False, "error": err}
    target_id = user_id or manifest["user_id"]
    try:
        target = paths.learner_dir(profile_root, target_id)
    except ValueError as e:
        return {"restored": False, "error": str(e)}
    exists = os.path.exists(target)
    plan = {"user_id": target_id, "from_user_id": manifest["user_id"], "backup_created_at": manifest.get("created_at"),
            "file_count": len(manifest["files"]), "target_exists": exists}
    if exists and not replace:
        return {**plan, "restored": False, "error": f"learner {target_id!r} already exists; use --replace (a safety backup is taken first) or --user-id to restore beside it"}
    if dry_run:
        return {**plan, "restored": False, "dry_run": True}

    safety = None
    if exists:
        safety = backup_profile.backup(profile_root, target_id, backups_dir, label="pre-restore")
        if not safety.get("backed_up"):
            return {**plan, "restored": False, "error": f"could not take the safety backup, nothing changed: {safety.get('error')}"}

    tmp = os.path.join(profile_root, f".restore-{target_id}.tmp")
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)
    try:
        with zipfile.ZipFile(zip_path) as z:
            for f in manifest["files"]:
                dest = os.path.join(tmp, *f["name"].split("/")[1:])
                paths.ensure_within(tmp, dest)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as out:
                    out.write(z.read(f["name"]))
        for f in manifest["files"]:  # re-verify what actually landed on disk
            with open(os.path.join(tmp, *f["name"].split("/")[1:]), "rb") as fh:
                if hashlib.sha256(fh.read()).hexdigest() != f["sha256"]:
                    raise OSError(f"{f['name']} did not write correctly")
        aside = None
        if exists:  # move the live folder aside (atomic) instead of deleting it first, so a failed swap can be undone
            aside = target + ".replaced.tmp"
            if os.path.exists(aside):
                shutil.rmtree(aside)
            atomic_io.replace(target, aside)
        try:
            atomic_io.replace(tmp, target)
        except Exception:
            if aside:
                atomic_io.replace(aside, target)
            raise
        if aside:
            shutil.rmtree(aside, ignore_errors=True)
    except Exception as e:  # noqa: BLE001 - report, the original is still in place
        shutil.rmtree(tmp, ignore_errors=True)
        return {**plan, "restored": False, "error": f"{type(e).__name__}: {e}", "safety_backup": (safety or {}).get("zip_path")}
    return {**plan, "restored": True, "safety_backup": (safety or {}).get("zip_path")}


def main(argv):
    args = list(argv)
    flags = {"--replace": False, "--dry-run": False}
    for f in flags:
        if f in args:
            args.remove(f)
            flags[f] = True
    uid = None
    if "--user-id" in args:
        i = args.index("--user-id")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--user-id needs a value"}))
            return 2
        uid = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        print(json.dumps({"error": "usage: restore_profile.py <profile_root> <backup.zip> [--user-id <id>] [--replace] [--dry-run]"}))
        return 2
    return cli.emit(restore(args[0], args[1], uid, flags["--replace"], flags["--dry-run"]))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
