#!/usr/bin/env python3
"""
doctor.py -- one-shot health check of an install (P-13).

    python3 doctor.py [--root <path>] [--learner <user_id>]

Checks, each reported as {name, status: ok|warn|fail, detail, fix}:

  python            interpreter is 3.10+
  data-root         courses/ profile/ .tutor-scripts/ exist (tutorlib.paths.layout)
  deployed-scripts  manifest present, every listed file/package present, tutorlib importable
  courses           every course passes validate_structure + its schemas (summarised)
  per learner:
    learner-schema  profile / subjects / decks conform to their JSON Schemas, cross-file invariants hold
    history-db      tutor.sqlite3 healthy and not from a newer plugin
    last-session    verify_session.py --previous finds nothing missing
    stale-locks     no leftover .lock files older than a minute
    writable        the learner folder accepts writes (not read-only / synced-and-locked)
    consent         the consent status in force (informational; limited/revoked get a note)

Read-only (the writability probe creates and removes one temp file). Output
{root, ok, summary{ok,warn,fail}, checks[]}; exit 0 when no check failed, 1 otherwise.
"""
import json
import os
import sys
import tempfile
import time

import invariants
import sqlite_store
import validate_structure
import verify_session
from tutorlib import cli, consent, ledger, paths, schema


def _c(name, status, detail, fix=None):
    return {"name": name, "status": status, "detail": detail, "fix": fix}


def check_python():
    v = sys.version_info
    if v >= (3, 10):
        return _c("python", "ok", f"Python {v.major}.{v.minor}.{v.micro}")
    return _c("python", "fail", f"Python {v.major}.{v.minor} is too old", "install Python 3.10 or newer")


def check_root(root):
    lay = paths.layout(root)
    if lay["valid"]:
        return _c("data-root", "ok", root)
    # a missing profile/ is normal before first run; anything else is a real problem
    problems = lay["problems"]
    hard = [p for p in problems if not p.startswith("no profile/")]
    return _c("data-root", "fail" if hard else "warn", "; ".join(problems),
              "connect the folder that holds courses/ (and profile/); /run deploys the scripts" if hard else "run /add-profile to create the first learner")


def check_deployed(root):
    td = os.path.join(root, ".tutor-scripts")
    mf = os.path.join(td, ".manifest.json")
    if not os.path.isfile(mf):
        return _c("deployed-scripts", "fail", "no .manifest.json - scripts not deployed", "run /run so the plugin deploys its scripts")
    try:
        with open(mf, encoding="utf-8") as f:
            m = json.load(f)
    except ValueError:
        return _c("deployed-scripts", "fail", "manifest unreadable", "run /run to redeploy")
    missing = [n for n in m.get("files", []) if not os.path.isfile(os.path.join(td, n))]
    missing += [p + "/" for p in m.get("packages", []) if not os.path.isdir(os.path.join(td, p))]
    if missing:
        return _c("deployed-scripts", "fail", f"missing: {', '.join(missing)}", "run /run - the bootstrap repairs drifted files")
    return _c("deployed-scripts", "ok", f"plugin {m.get('plugin_version')}, {len(m.get('files', []))} scripts")


def check_courses(courses_dir):
    if not os.path.isdir(courses_dir):
        return _c("courses", "warn", "no courses/ folder", None)
    bad, n = [], 0
    for cid in sorted(os.listdir(courses_dir)):
        cdir = os.path.join(courses_dir, cid)
        if not os.path.isfile(os.path.join(cdir, "course.json")):
            continue
        n += 1
        v = validate_structure.validate(cdir)
        errs = schema.validate_file(os.path.join(cdir, "course.json"), "course")
        if "error" in v or not v.get("clean", False) or errs:
            bad.append(cid)
    if bad:
        return _c("courses", "warn", f"{len(bad)} of {n} courses need attention: {', '.join(bad[:10])}", "run /audit")
    return _c("courses", "ok", f"{n} course(s) structurally clean")


def check_learner(ldir, courses_dir):
    uid = os.path.basename(ldir)
    out = []
    inv = invariants.check(ldir, courses_dir)
    if inv["ok"]:
        out.append(_c(f"learner-schema:{uid}", "ok", "files conform, cross-file invariants hold"))
    else:
        first = "; ".join(f"{p['file']}: {p['message']}" for p in inv["problems"][:3])
        out.append(_c(f"learner-schema:{uid}", "warn", f"{inv['problem_count']} problem(s): {first}", "run /audit; keep a backup before repairs"))
    db = sqlite_store.check(ldir)
    if not db.get("exists"):
        out.append(_c(f"history-db:{uid}", "ok", "no history database yet"))
    elif db.get("healthy"):
        out.append(_c(f"history-db:{uid}", "ok", f"v{db['user_version']}, integrity ok"))
    else:
        out.append(_c(f"history-db:{uid}", "fail", f"unhealthy: version {db.get('user_version')}, integrity {db.get('integrity')}",
                      "update the plugin if the database is newer; otherwise restore a backup"))
    try:
        with open(os.path.join(ldir, "student_profile.json"), encoding="utf-8") as f:
            cur = int(json.load(f).get("session_slot", 0))
        if cur >= 1:
            rep = verify_session.verify(ledger.read(ldir), ldir, cur - 1)
            missing = [f for f in rep if f["severity"] == "missing"]
            if missing:
                out.append(_c(f"last-session:{uid}", "warn", f"{len(missing)} write(s) missing: " + "; ".join(f["message"] for f in missing[:2]),
                              "tell the learner; repair by running the missing step"))
            else:
                out.append(_c(f"last-session:{uid}", "ok", "previous session's writes are complete"))
    except (OSError, ValueError):
        pass
    stale = []
    for dp, _dn, fns in os.walk(ldir):
        for fn in fns:
            if fn.endswith(".lock"):
                full = os.path.join(dp, fn)
                if time.time() - os.path.getmtime(full) > 60:
                    stale.append(os.path.relpath(full, ldir))
    out.append(_c(f"stale-locks:{uid}", "warn" if stale else "ok", ", ".join(stale) if stale else "none",
                  "delete the listed .lock files (a script crashed mid-write)" if stale else None))
    try:
        fd, tmp = tempfile.mkstemp(prefix=".doctor-", dir=ldir)
        os.close(fd)
        os.unlink(tmp)
        out.append(_c(f"writable:{uid}", "ok", "learner folder is writable"))
    except OSError as e:
        out.append(_c(f"writable:{uid}", "fail", f"cannot write: {e}", "check folder permissions / sync client locks"))
    status = consent.status_for(os.path.join(ldir, "student_profile.json"))
    note = {"granted": "all learner data is saved", "limited": "only progress and scheduling are saved",
            "revoked": "nothing is saved"}[status]
    out.append(_c(f"consent:{uid}", "ok" if status == "granted" else "warn", f"{status}: {note}",
                  None if status == "granted" else "change with /profile if this is not intended"))
    return out


def run(root, learner=None):
    checks = [check_python(), check_root(root)]
    if os.path.isdir(root):
        checks.append(check_deployed(root))
        checks.append(check_courses(os.path.join(root, "courses")))
        pdir = os.path.join(root, "profile")
        if os.path.isdir(pdir):
            for uid in sorted(os.listdir(pdir)):
                ldir = os.path.join(pdir, uid)
                if os.path.isdir(ldir) and (learner is None or uid == learner):
                    checks.extend(check_learner(ldir, os.path.join(root, "courses")))
    counts = {s: sum(1 for c in checks if c["status"] == s) for s in ("ok", "warn", "fail")}
    return {"root": root, "ok": counts["fail"] == 0, "summary": counts, "checks": checks}


def main(argv):
    args, root, learner = list(argv), None, None
    for flag in ("--root", "--learner"):
        if flag in args:
            i = args.index(flag)
            if i + 1 >= len(args):
                print(json.dumps({"error": f"{flag} needs a value"}))
                return 2
            val = args[i + 1]
            del args[i:i + 2]
            if flag == "--root":
                root = val
            else:
                learner = val
    if args:
        print(json.dumps({"error": "usage: doctor.py [--root <path>] [--learner <user_id>]"}))
        return 2
    resolved = paths.resolve_root(root)
    if resolved is None:
        return cli.emit({"error": "no data root: pass --root, set EDU_ROOT, or run the deployed copy under <root>/.tutor-scripts/"})
    result = run(resolved, learner)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
