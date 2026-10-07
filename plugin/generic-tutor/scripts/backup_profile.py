#!/usr/bin/env python3
"""
backup_profile.py -- full physical backup of one learner (E-24, C-08).

    python3 backup_profile.py <profile_root> <user_id> [--out <dir>]

Writes `<out>/<user_id>-backup-<UTC timestamp>.zip` (default `<profile_root>/../backups/`, i.e. OUTSIDE
the learner's folder, so `/erase` cannot delete the backups and a backup can never contain a backup).

Contents: manifest.json (format_version, user_id, created_at, plugin version, sha256 + size per file) and
every file of the learner folder under `learner/` -- profile, progress, review decks, session ledger -- with
`tutor.sqlite3` copied through SQLite's online-backup API so the copy is consistent even if a script is
writing. Lock files and partial writes are skipped. Restore with restore_profile.py, which verifies every
checksum before touching anything.

This is a COPY of the same personal data it protects: store it as carefully as the original (docs/PRIVACY.md).
Unlike export_profile.py (a readable, logical bundle for the learner), a backup is for putting the system
back exactly as it was.
"""
import datetime
import hashlib
import json
import os
import sqlite3
import sys
import tempfile
import zipfile

from tutorlib import atomic_io, cli, paths

FORMAT_VERSION = 1
SKIP_SUFFIXES = (".lock", ".part", ".tmp")


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _read_file(full):
    if os.path.basename(full) == "tutor.sqlite3":
        fd, tmp = tempfile.mkstemp(suffix=".sqlite3")
        os.close(fd)
        try:
            src = sqlite3.connect(f"file:{full}?mode=ro", uri=True)
            dst = sqlite3.connect(tmp)
            try:
                src.backup(dst)
            finally:
                dst.close()
                src.close()
            with open(tmp, "rb") as f:
                return f.read()
        finally:
            os.unlink(tmp)
    with open(full, "rb") as f:
        return f.read()


def _plugin_version():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".manifest.json"), encoding="utf-8") as f:
            return json.load(f).get("plugin_version")
    except (OSError, ValueError):
        return None


def default_out_dir(profile_root):
    return os.path.join(os.path.dirname(os.path.abspath(profile_root)), "backups")


def backup(profile_root, user_id, out_dir=None, now=None, label=None):
    try:
        d = paths.learner_dir(profile_root, user_id)
    except ValueError as e:
        return {"backed_up": False, "error": str(e)}
    if not os.path.isdir(d):
        return {"backed_up": False, "error": f"no profile folder for {user_id!r}"}
    out_dir = os.path.abspath(out_dir or default_out_dir(profile_root))
    real_d = os.path.realpath(d)
    if os.path.realpath(out_dir) == real_d or os.path.realpath(out_dir).startswith(real_d + os.sep):
        return {"backed_up": False, "error": "backup folder must be outside the learner's folder"}
    os.makedirs(out_dir, exist_ok=True)

    entries = {}
    for dp, dn, fns in os.walk(d):
        dn.sort()
        for fn in sorted(fns):
            full = os.path.join(dp, fn)
            if fn.endswith(SKIP_SUFFIXES) or os.path.islink(full):
                continue
            entries["learner/" + os.path.relpath(full, d).replace(os.sep, "/")] = _read_file(full)
    if not entries:
        return {"backed_up": False, "error": "learner folder is empty"}

    now = now or datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    name = f"{user_id}-backup-{stamp}{('-' + label) if label else ''}.zip"
    manifest = {"format_version": FORMAT_VERSION, "kind": "learner-backup", "user_id": user_id,
                "created_at": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"), "plugin_version": _plugin_version(),
                "files": [{"name": n, "bytes": len(b), "sha256": _sha(b)} for n, b in sorted(entries.items())]}
    zip_path = os.path.join(out_dir, name)
    n = 1
    while os.path.exists(zip_path):  # never overwrite an existing backup (it may be the very file being restored)
        n += 1
        zip_path = os.path.join(out_dir, name[:-4] + f"-{n}.zip")
    tmp = zip_path + ".part"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("manifest.json", json.dumps(manifest, indent=2) + "\n")
        for n, b in sorted(entries.items()):
            z.writestr(n, b)
    atomic_io.replace(tmp, zip_path)
    return {"backed_up": True, "user_id": user_id, "zip_path": zip_path, "file_count": len(entries),
            "bytes": os.path.getsize(zip_path), "created_at": manifest["created_at"]}


def main(argv):
    args, out = list(argv), None
    if "--out" in args:
        i = args.index("--out")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--out needs a folder"}))
            return 2
        out = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        print(json.dumps({"error": "usage: backup_profile.py <profile_root> <user_id> [--out <dir>]"}))
        return 2
    r = backup(args[0], args[1], out)
    if "error" in r:
        return cli.emit(r)
    print(json.dumps(r, indent=2))
    return 0


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
