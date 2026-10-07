#!/usr/bin/env python3
"""
apply_capabilities.py - v1.3.0 practical units by declaration.

A course marks practical stages in course.json:
    "practical_stages": {"<stage_id>": ["share_images", ...]}
A learner declares capabilities once, in student_profile.json:
    "capabilities": {"share_images": {"declared": true, "on": "2026-09-26"}}

This script brings ONE enrolment into line with the learner's current declarations. Run it:
  - right after an enrolment file is created (course-compiler, both paths), and
  - for every enrolment of the learner whenever a capability is declared or withdrawn
    (profile-kernel), and
  - defensively on /continue (course-runner) - it is idempotent.

Rules, per practical stage:
  - capability missing, stage not `pass`  -> `withheld` (theory-only for this learner)
  - capability missing, stage `pass`      -> left `pass` (withdrawing never erases a real pass)
  - capability present, stage `withheld`  -> `unsat` (the stage is now offered)
Non-practical stages are never touched. A stage needing several capabilities needs all of them.

Because `withheld` counts as satisfied for completion, unlocking stages can REOPEN a completed
course. The report says so (`reopens_completed_course: true`); the caller must warn the learner
and get a yes before writing (pass --dry-run first). Nothing else is changed in the file.

Usage:
    python3 apply_capabilities.py <student_profile.json> <course.json> <subjects.json> [--dry-run]

Output: JSON report {"changed": {stage: [old, new]}, "withheld_now": [...], "theory_only": bool,
"reopens_completed_course": bool, "wrote": bool}.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cohort_status import is_complete, practical_stages  # noqa: E402
from tutorlib import cli, consent, state


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def declared_capabilities(profile):
    caps = profile.get("capabilities") if isinstance(profile, dict) else None
    out = set()
    for name, v in (caps or {}).items():
        if (isinstance(v, dict) and v.get("declared") is True) or v is True:
            out.add(name)
    return out


def apply(profile, course, subj):
    """Pure function: returns (new_subj, report)."""
    caps = declared_capabilities(profile)
    ps = practical_stages(course)
    ladder = course.get("stage_ladder", [])
    new = json.loads(json.dumps(subj))
    ss = new.setdefault("syllabus_status", {})
    changed = {}
    for stage in ladder:
        if stage not in ps:
            continue
        needed = set(ps.get(stage) or [])
        has = needed <= caps
        cur = ss.get(stage, "unsat")
        if not has and cur != "pass" and cur != "withheld":
            ss[stage] = "withheld"
            changed[stage] = [cur, "withheld"]
        elif has and cur == "withheld":
            ss[stage] = "unsat"
            changed[stage] = [cur, "unsat"]
    was_complete = is_complete(course, subj)
    now_complete = is_complete(course, new)
    withheld_now = [s for s in ladder if ss.get(s) == "withheld" and s in ps]
    report = {
        "changed": changed,
        "withheld_now": withheld_now,
        "theory_only": bool(withheld_now),
        "reopens_completed_course": was_complete and not now_complete,
    }
    return new, report


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv[1:]
    if len(args) != 3:
        print(json.dumps({"error": "usage: apply_capabilities.py <student_profile.json> <course.json> <subjects.json> [--dry-run]"}))
        sys.exit(2)
    profile_path, course_path, subj_path = args
    try:
        profile, course, subj = _load(profile_path), _load(course_path), _load(subj_path)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    new, report = apply(profile, course, subj)
    wrote = False
    if report["changed"] and not dry:
        allowed, cstatus = consent.check(subj_path, consent.PROGRESS)
        if allowed:
            state.save(subj_path, new, "subjects")
            wrote = True
        else:
            report["skipped"] = f"consent {cstatus}: progress writes are not persisted"
    report["wrote"] = wrote
    report["dry_run"] = dry
    sys.exit(cli.emit(report))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
