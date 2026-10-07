#!/usr/bin/env python3
"""
course_bundle.py -- move a course between libraries as one verified zip, with no learner data in it (N-12).

    python3 course_bundle.py export <course_dir> <out.zip>
    python3 course_bundle.py import <courses_root> <bundle.zip> [--course-id <id>] [--replace] [--dry-run]

export  refuses a course that fails validate_structure, packs only course files (never profile, progress, history or lock
        files), and writes a deterministic zip: sorted entries, fixed timestamps, a manifest with a sha256 per file.
import  treats the bundle as untrusted content. Before anything is written it checks: manifest kind and format (a bundle from a
        NEWER plugin is refused), every listed file present with the recorded hash, no unlisted members, no absolute, `..` or
        backslash paths, size and count caps, and no learner-data file names. The course is then built in a staging folder
        beside the live ones, must pass validate_structure and have no BLOCKING scan_untrusted finding, and only then is it
        renamed into place. An existing course of the same id is refused unless --replace, which moves it aside first so a
        failure leaves it untouched. --dry-run reports without writing. --course-id imports under a different id.
Imported prose is still content from outside: the tutor treats it under docs/UNTRUSTED_CONTENT.md like any other source.
"""
import hashlib
import json
import os
import shutil
import sys
import zipfile
from datetime import datetime, timezone

import validate_structure
from tutorlib import atomic_io, cli, ids, paths, untrusted

FORMAT_VERSION = 1
KIND = "course-bundle"
MAX_FILES = 5000
MAX_TOTAL_BYTES = 200_000_000
SKIP_SUFFIXES = (".lock", ".part", ".tmp", ".pyc")
SKIP_NAMES = {".DS_Store", "Thumbs.db"}
LEARNER_NAMES = {"micro_profile.json", "subjects.json", "history.db", "history.sqlite", "learner.json", "profile.json",
                 "progress.json", "item_mastery.json", "calibration.json", "error_log.jsonl"}
EPOCH = (2020, 1, 1, 0, 0, 0)


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _plugin_version():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".manifest.json"), encoding="utf-8") as f:
            return json.load(f).get("plugin_version")
    except (OSError, ValueError):
        return None


def _bad_path(n):
    parts = n.split("/")
    return n.startswith("/") or "\\" in n or any(p in ("", "..", ".") for p in parts) or parts[0] != "course" or len(parts) < 2 \
        or ":" in parts[0]


def export(course_dir, out_zip, now=None):
    if not os.path.isfile(os.path.join(course_dir, "course.json")):
        return {"exported": False, "error": f"{course_dir} has no course.json"}
    try:
        course_id = ids.validate(os.path.basename(os.path.abspath(course_dir)), "course id")
    except ValueError as e:
        return {"exported": False, "error": str(e)}
    report = validate_structure.validate(course_dir)
    if report.get("error") or not report.get("clean"):
        return {"exported": False, "error": "course fails validate_structure; fix it before bundling", "validate": report}
    files, skipped = [], []
    for root, dirs, names in os.walk(course_dir):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__" and not os.path.islink(os.path.join(root, d)))
        for n in sorted(names):
            full = os.path.join(root, n)
            rel = os.path.relpath(full, course_dir).replace(os.sep, "/")
            if os.path.islink(full) or n.endswith(SKIP_SUFFIXES) or n in SKIP_NAMES:
                skipped.append(rel)
                continue
            if n in LEARNER_NAMES:
                return {"exported": False, "error": f"{rel} looks like learner data; a course bundle never carries it"}
            with open(full, "rb") as fh:
                data = fh.read()
            files.append((f"course/{rel}", data))
    if len(files) > MAX_FILES or sum(len(d) for _, d in files) > MAX_TOTAL_BYTES:
        return {"exported": False, "error": f"course is over the bundle limits ({MAX_FILES} files, {MAX_TOTAL_BYTES} bytes)"}
    stamp = (now or datetime.now(timezone.utc)).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    manifest = {"kind": KIND, "format_version": FORMAT_VERSION, "course_id": course_id, "created_at": stamp,
                "plugin_version": _plugin_version(), "learner_data": False,
                "files": [{"name": n, "sha256": _sha(d), "bytes": len(d)} for n, d in files]}
    os.makedirs(os.path.dirname(os.path.abspath(out_zip)), exist_ok=True)
    tmp = out_zip + ".part"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in [("manifest.json", json.dumps(manifest, indent=2, sort_keys=True).encode())] + files:
            z.writestr(zipfile.ZipInfo(name, EPOCH), data, zipfile.ZIP_DEFLATED)
    atomic_io.replace(tmp, out_zip)
    return {"exported": True, "course_id": course_id, "zip_path": out_zip, "file_count": len(files), "skipped": skipped}


def verify_zip(zip_path):
    """Return (manifest, error). Checks structure and checksums without extracting anything."""
    try:
        z = zipfile.ZipFile(zip_path)
    except (OSError, zipfile.BadZipFile) as e:
        return None, f"cannot open bundle: {e}"
    with z:
        try:
            manifest = json.loads(z.read("manifest.json"))
        except (KeyError, ValueError):
            return None, "bundle has no readable manifest.json"
        if not isinstance(manifest, dict) or manifest.get("kind") != KIND:
            return None, "not a course bundle (wrong manifest kind)"
        if not isinstance(manifest.get("format_version"), int) or manifest["format_version"] > FORMAT_VERSION:
            return None, f"bundle format {manifest.get('format_version')!r} is newer than this plugin understands ({FORMAT_VERSION}); update the plugin"
        try:
            ids.validate(manifest.get("course_id"), "course_id in bundle")
        except ValueError as e:
            return None, str(e)
        listed = manifest.get("files")
        if not isinstance(listed, list) or not all(isinstance(f, dict) and isinstance(f.get("name"), str) for f in listed):
            return None, "bundle manifest has no valid file list"
        by_name = {f["name"]: f for f in listed}
        if len(by_name) != len(listed):
            return None, "bundle manifest lists a file twice"
        infos = {i.filename: i for i in z.infolist() if not i.filename.endswith("/")}
        members = set(infos) - {"manifest.json"}
        if len(listed) > MAX_FILES or sum(i.file_size for i in infos.values()) > MAX_TOTAL_BYTES:
            return None, f"bundle is over the limits ({MAX_FILES} files, {MAX_TOTAL_BYTES} bytes)"
        for n in members | set(by_name):
            if _bad_path(n):
                return None, f"unsafe or unexpected path in bundle: {n!r}"
            if n.rsplit("/", 1)[-1] in LEARNER_NAMES:
                return None, f"bundle carries a learner-data file name: {n!r}"
        if members != set(by_name):
            return None, f"bundle contents do not match its manifest (extra: {sorted(members - set(by_name))[:3]}, missing: {sorted(set(by_name) - members)[:3]})"
        for n, f in sorted(by_name.items()):
            data = z.read(n)
            if _sha(data) != f.get("sha256") or len(data) != f.get("bytes"):
                return None, f"checksum mismatch for {n} - the bundle is damaged or was modified"
    return manifest, None


def import_bundle(courses_root, zip_path, course_id=None, replace=False, dry_run=False):
    manifest, err = verify_zip(zip_path)
    if err:
        return {"imported": False, "error": err}
    target_id = course_id or manifest["course_id"]
    try:
        ids.validate(target_id, "course id")
        target = os.path.join(courses_root, target_id)
        paths.ensure_within(courses_root, target)
        if os.path.islink(target):
            raise ValueError(f"{target!r} is a symlink")
    except (ValueError, paths.OutsideRoot) as e:
        return {"imported": False, "error": str(e)}
    exists = os.path.exists(target)
    plan = {"course_id": target_id, "from_course_id": manifest["course_id"], "bundle_created_at": manifest.get("created_at"),
            "file_count": len(manifest["files"]), "target_exists": exists}
    if exists and not replace:
        return {**plan, "imported": False, "error": f"course {target_id!r} already exists; use --replace or --course-id"}
    stage = os.path.join(courses_root, f".import-{target_id}.tmp")
    if os.path.exists(stage):
        shutil.rmtree(stage)
    os.makedirs(stage)
    aside = None
    try:
        with zipfile.ZipFile(zip_path) as z:
            for f in manifest["files"]:
                dest = os.path.join(stage, *f["name"].split("/")[1:])
                paths.ensure_within(stage, dest)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as out:
                    out.write(z.read(f["name"]))
        report = validate_structure.validate(stage)
        if report.get("error") or not report.get("clean"):
            return {**plan, "imported": False, "error": "the bundled course fails validate_structure", "validate": report}
        findings = untrusted.scan_path(stage)
        blocking = {p: [x for x in fs if x["severity"] == untrusted.BLOCKING] for p, fs in findings.items()}
        blocking = {p: fs for p, fs in blocking.items() if fs}
        if blocking:
            return {**plan, "imported": False, "error": "the bundle contains instruction-like text (BLOCKING scan_untrusted findings)",
                    "findings": blocking}
        advisory = sum(len(fs) for fs in findings.values())
        if dry_run:
            return {**plan, "imported": False, "dry_run": True, "advisory_findings": advisory}
        if exists:
            aside = target + ".replaced.tmp"
            if os.path.exists(aside):
                shutil.rmtree(aside)
            atomic_io.replace(target, aside)
        try:
            atomic_io.replace(stage, target)
        except Exception:
            if aside:
                atomic_io.replace(aside, target)
                aside = None
            raise
    except Exception as e:  # noqa: BLE001 - report; any existing course is still in place
        return {**plan, "imported": False, "error": f"{type(e).__name__}: {e}"}
    finally:
        shutil.rmtree(stage, ignore_errors=True)
        if aside:
            shutil.rmtree(aside, ignore_errors=True)
    return {**plan, "imported": True, "advisory_findings": advisory}


def main(argv):
    args = list(argv)
    flags = {"--replace": False, "--dry-run": False}
    for f in flags:
        if f in args:
            args.remove(f)
            flags[f] = True
    cid = None
    if "--course-id" in args:
        i = args.index("--course-id")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--course-id needs a value"}))
            return 2
        cid = args[i + 1]
        del args[i:i + 2]
    if len(args) == 3 and args[0] == "export" and not (cid or flags["--replace"] or flags["--dry-run"]):
        return cli.emit(export(args[1], args[2]))
    if len(args) == 3 and args[0] == "import":
        return cli.emit(import_bundle(args[1], args[2], cid, flags["--replace"], flags["--dry-run"]))
    print(json.dumps({"error": "usage: course_bundle.py export <course_dir> <out.zip> | import <courses_root> <bundle.zip> [--course-id ID] [--replace] [--dry-run]"}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
