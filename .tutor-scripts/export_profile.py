#!/usr/bin/env python3
"""
export_profile.py -- bundle one learner's data into a single zip (K-28, K-29).

    python3 export_profile.py <profile_root> <user_id> <output.zip>

Contents (format_version 1):
  manifest.json              what is inside, with sha256 per file, plugin/format version
  student_profile.json       as stored
  subjects/<course>.json     progress, incl. dropped courses
  subjects/<course>_review_deck.json
  history/<table>.json       every row of every table in tutor.sqlite3 (if present)
  session_ledger.jsonl       the write ledger (if present)

Read-only with respect to /EDU/: the output zip must NOT be inside the learner's
folder or profile root (refused), so an export can never be swept up by /erase or
nest inside itself. Shared course content is not included. Another learner's
data is unreachable by construction (user_id is validated, symlinks refused).
Exports contain personal data; see docs/PRIVACY.md.
"""
import hashlib
import json
import os
import sqlite3
import sys
import zipfile

from tutorlib import cli, paths

FORMAT_VERSION = 1


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _history(db_path):
    out = {}
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        con.row_factory = sqlite3.Row
        tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
        for t in tables:
            out[t] = [dict(r) for r in con.execute(f'SELECT * FROM "{t}"')]
    finally:
        con.close()
    return out


def export(profile_root, user_id, out_zip, plugin_version=None):
    try:
        d = paths.learner_dir(profile_root, user_id)
    except ValueError as e:
        return {"exported": False, "error": str(e)}
    if not os.path.isdir(d):
        return {"exported": False, "error": f"no profile folder for {user_id!r}"}
    real_out = os.path.realpath(out_zip)
    if real_out == os.path.realpath(profile_root) or real_out.startswith(os.path.realpath(profile_root) + os.sep):
        return {"exported": False, "error": "output file must be outside the profile folder"}

    entries = {}  # name -> bytes
    pp = os.path.join(d, "student_profile.json")
    if os.path.isfile(pp):
        with open(pp, "rb") as f:
            entries["student_profile.json"] = f.read()
    sd = os.path.join(d, "subjects")
    if os.path.isdir(sd):
        for name in sorted(os.listdir(sd)):
            full = os.path.join(sd, name)
            if name.endswith(".json") and os.path.isfile(full) and not os.path.islink(full):
                with open(full, "rb") as f:
                    entries[f"subjects/{name}"] = f.read()
    lg = os.path.join(d, ".session_ledger.jsonl")
    if os.path.isfile(lg) and not os.path.islink(lg):
        with open(lg, "rb") as f:
            entries["session_ledger.jsonl"] = f.read()
    db = os.path.join(d, "tutor.sqlite3")
    history_tables = []
    if os.path.isfile(db):
        for table, rows in _history(db).items():
            entries[f"history/{table}.json"] = (json.dumps(rows, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
            history_tables.append({"table": table, "rows": len(rows)})
    if not entries:
        return {"exported": False, "error": "nothing to export"}

    manifest = {"format_version": FORMAT_VERSION, "plugin_version": plugin_version, "user_id": user_id,
                "files": [{"name": n, "bytes": len(b), "sha256": _sha(b)} for n, b in sorted(entries.items())],
                "history_tables": history_tables}
    tmp = out_zip + ".part"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("manifest.json", json.dumps(manifest, indent=2) + "\n")
        for n, b in sorted(entries.items()):
            z.writestr(n, b)
    os.replace(tmp, out_zip)
    return {"exported": True, "output": out_zip, "file_count": len(entries), "history_tables": history_tables}


def _deployed_version():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".manifest.json"), encoding="utf-8") as f:
            return json.load(f).get("plugin_version")
    except (OSError, ValueError):
        return None


def main(argv):
    if len(argv) != 3:
        print(json.dumps({"error": "usage: export_profile.py <profile_root> <user_id> <output.zip>"}))
        return 1
    result = export(argv[0], argv[1], argv[2], _deployed_version())
    print(json.dumps(result, indent=2))
    return 0 if result.get("exported") else 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
