#!/usr/bin/env python3
"""
toolkit/backup.py — snapshot a learner's profile folder to a timestamped
zip. This is the toolkit's highest-priority module, not a convenience: the
plugin's own .gitignore deliberately excludes profile/*/ from version
control (so no real learner data ever lands in a repo that might be shared
or made public), which means there is currently no backup path at all for
the one thing in this whole system that's genuinely irreplaceable — a
learner's actual history, mastery, and error patterns. Course content can
always be recompiled; this can't be.

Writes only a zip file (plus one line to its own toolkit_log — see
core.py's docstring on the one exception to "read-only"). Never modifies,
deletes, or renames anything under profile/ or courses/.

Usage:
    python3 -m toolkit backup <learner_id> [--out DIR] [--include-courses id1,id2]
"""
import datetime
import json
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402


def create_backup(learner_id, root=None, out_dir=None, include_courses=None):
    root = root or core.edu_root()
    pdir = core.profile_dir(learner_id, root)
    if not os.path.isdir(pdir):
        return {"error": f"no such learner profile: {pdir}"}

    out_dir = out_dir or os.path.join(pdir, "exports")
    os.makedirs(out_dir, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_path = os.path.join(out_dir, f"{learner_id}_backup_{stamp}.zip")

    files_written = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for dirpath, dirnames, filenames in os.walk(pdir):
            # never re-zip a previous backup that happens to live under exports/
            dirnames[:] = [d for d in dirnames if not os.path.join(dirpath, d) == out_dir]
            if os.path.abspath(dirpath) == os.path.abspath(out_dir):
                continue
            for fn in filenames:
                full = os.path.join(dirpath, fn)
                arcname = os.path.join("profile", learner_id, os.path.relpath(full, pdir))
                zf.write(full, arcname)
                files_written += 1

        included_courses = []
        for course_id in (include_courses or []):
            cdir = core.course_dir_path(course_id, root)
            if not os.path.isdir(cdir):
                continue
            for dirpath, _, filenames in os.walk(cdir):
                for fn in filenames:
                    full = os.path.join(dirpath, fn)
                    arcname = os.path.join("courses", course_id, os.path.relpath(full, cdir))
                    zf.write(full, arcname)
                    files_written += 1
            included_courses.append(course_id)

    size_bytes = os.path.getsize(zip_path)
    result = {
        "learner_id": learner_id,
        "zip_path": zip_path,
        "files_written": files_written,
        "size_bytes": size_bytes,
        "included_courses": included_courses if include_courses else [],
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    _log_backup(learner_id, root, result)
    return result


def _log_backup(learner_id, root, result):
    log_dir = core.toolkit_log_dir(learner_id, root)
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "backups.jsonl")
    entry = {k: result[k] for k in ("zip_path", "files_written", "size_bytes", "created_at")}
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: backup.py <learner_id> [--out DIR] [--include-courses id1,id2]"}))
        sys.exit(2)
    learner_id = sys.argv[1]
    out_dir = None
    include_courses = None
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            out_dir = args[i + 1]
            i += 2
        elif args[i] == "--include-courses" and i + 1 < len(args):
            include_courses = [c for c in args[i + 1].split(",") if c]
            i += 2
        else:
            i += 1
    result = create_backup(learner_id, out_dir=out_dir, include_courses=include_courses)
    print(json.dumps(result, indent=2))
    sys.exit(1 if "error" in result else 0)


if __name__ == "__main__":
    main()
