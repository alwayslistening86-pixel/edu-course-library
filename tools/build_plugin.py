#!/usr/bin/env python3
"""
build_plugin.py -- deterministic `generic-tutor.plugin` zip (R-11, P-03).

    python3 tools/build_plugin.py [--out <file>]

Zips plugin/generic-tutor/ with sorted entries and fixed timestamps, so two builds of the same tree are
byte-identical. Excludes what must not ship: tests/, evals/, __pycache__, *.pyc, .DS_Store, local data
folders. Default output: dist/generic-tutor-<version>.plugin (dist/ is git-ignored).
Prints {"output", "version", "files", "bytes", "sha256"}.
"""
import hashlib
import json
import os
import sys
import zipfile

EXCLUDE_DIRS = {"tests", "evals", "__pycache__", ".git"}
EXCLUDE_FILES = {".DS_Store"}
EXCLUDE_SUFFIXES = (".pyc", ".pyo")
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def collect(src):
    out = []
    for dp, dn, fns in os.walk(src):
        dn[:] = sorted(d for d in dn if d not in EXCLUDE_DIRS)
        for fn in sorted(fns):
            if fn in EXCLUDE_FILES or fn.endswith(EXCLUDE_SUFFIXES):
                continue
            full = os.path.join(dp, fn)
            out.append((os.path.relpath(full, src).replace(os.sep, "/"), full))
    return sorted(out)


def build(repo_root, out=None):
    src = os.path.join(repo_root, "plugin", "generic-tutor")
    with open(os.path.join(src, ".claude-plugin", "plugin.json"), encoding="utf-8") as f:
        version = json.load(f)["version"]
    out = out or os.path.join(repo_root, "dist", f"generic-tutor-{version}.plugin")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    files = collect(src)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, full in files:
            info = zipfile.ZipInfo(arc, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if arc.endswith((".py", ".pyw")) and arc.startswith("scripts/") else 0o644) << 16
            with open(full, "rb") as fh:
                z.writestr(info, fh.read())
    with open(out, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    return {"output": out, "version": version, "files": len(files), "bytes": os.path.getsize(out), "sha256": digest}


def main(argv):
    out = None
    if argv[:1] == ["--out"]:
        if len(argv) != 2:
            print("usage: build_plugin.py [--out <file>]", file=sys.stderr)
            return 2
        out = argv[1]
    elif argv:
        print("usage: build_plugin.py [--out <file>]", file=sys.stderr)
        return 2
    print(json.dumps(build(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), out), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
