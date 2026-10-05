#!/usr/bin/env python3
"""
invariants.py -- cross-file consistency checks for one learner (V-08).

    python3 invariants.py <learner_dir> <courses_dir>

Schemas catch a malformed file; this catches files that are individually valid but disagree with each
other or with their course -- the damage a skipped or mistaken script call leaves behind:

  schema              file fails its JSON Schema
  ladder-keys         syllabus_status stages != the course's stage_ladder
  current-stage       current_stage not in the ladder
  linear-order        a stage is 'unsat'/'fail' while a LATER stage is 'pass' (linear courses only)
  deck-stage          a review card names a stage not in the course
  deck-duplicate-id   duplicate card ids in a deck
  error-duplicate-id  duplicate error ids
  error-resolved      a resolved error with no resolved_at_slot
  slot-regression     the ledger holds a slot higher than the profile's session_slot
  unknown-course      a subjects file for a course that is not in courses_dir (informational)

Read-only. Output {ok, problems[{check, file, message}]}; exit 0 (it reports, never repairs).
"""
import json
import os
import sys

from tutorlib import cli, ledger, schema


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def check(learner_dir, courses_dir):
    problems = []

    def add(kind, file, message):
        problems.append({"check": kind, "file": file, "message": message})

    prof_path = os.path.join(learner_dir, "student_profile.json")
    profile = _load(prof_path)
    if profile is None:
        add("schema", "student_profile.json", "missing or unreadable")
        profile = {}
    else:
        for e in schema.validate(profile, "student_profile"):
            add("schema", "student_profile.json", e)

    sdir = os.path.join(learner_dir, "subjects")
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if not fn.endswith(".json"):
            continue
        path = os.path.join(sdir, fn)
        data = _load(path)
        rel = f"subjects/{fn}"
        if fn.endswith("_review_deck.json"):
            if data is None:
                add("schema", rel, "unreadable")
                continue
            for e in schema.validate(data, "review_deck"):
                add("schema", rel, e)
            cid = fn[: -len("_review_deck.json")]
            course = _load(os.path.join(courses_dir, cid, "course.json")) or {}
            ladder = set(course.get("stage_ladder", []))
            ids = [c.get("id") for c in data.get("cards", []) if isinstance(c, dict)]
            for dup in sorted({i for i in ids if ids.count(i) > 1}, key=str):
                add("deck-duplicate-id", rel, f"card id {dup!r} appears more than once")
            if ladder:
                for c in data.get("cards", []):
                    if isinstance(c, dict) and c.get("stage_id") and c["stage_id"] not in ladder:
                        add("deck-stage", rel, f"card {c.get('id')!r} names stage {c['stage_id']!r} which is not in the course")
            continue
        if data is None:
            add("schema", rel, "unreadable")
            continue
        for e in schema.validate(data, "subjects"):
            add("schema", rel, e)
        cid = data.get("course_id") or fn[:-5]
        course = _load(os.path.join(courses_dir, cid, "course.json"))
        if course is None:
            add("unknown-course", rel, f"course {cid!r} not found in {courses_dir}")
        else:
            ladder = course.get("stage_ladder", [])
            status = data.get("syllabus_status") or {}
            if isinstance(status, dict) and set(status) != set(ladder):
                add("ladder-keys", rel, f"syllabus_status stages {sorted(status)} != course ladder {sorted(ladder)}")
            if data.get("current_stage") not in ladder and data.get("current_stage") is not None:
                add("current-stage", rel, f"current_stage {data.get('current_stage')!r} not in the ladder")
            if course.get("linear", True) and isinstance(status, dict):
                last_pass = max((i for i, s in enumerate(ladder) if status.get(s) == "pass"), default=-1)
                for s in (ladder[:last_pass] if last_pass >= 0 else []):
                    if status.get(s) in ("unsat", "fail"):
                        add("linear-order", rel, f"stage {s} is {status.get(s)!r} but a later stage ({ladder[last_pass]}) is 'pass'")
        errs = [e for e in data.get("error_patterns", []) if isinstance(e, dict)]
        ids = [e.get("id") for e in errs]
        for dup in sorted({i for i in ids if ids.count(i) > 1}, key=str):
            add("error-duplicate-id", rel, f"error id {dup!r} appears more than once")
        for e in errs:
            if e.get("resolved") and e.get("resolved_at_slot") is None:
                add("error-resolved", rel, f"error {e.get('id')!r} is resolved but has no resolved_at_slot")

    current = profile.get("session_slot", 0) if isinstance(profile.get("session_slot", 0), int) else 0
    top = max((e.get("slot") or 0 for e in ledger.read(learner_dir) if isinstance(e.get("slot"), int)), default=0)
    if top > current:
        add("slot-regression", ".session_ledger.jsonl", f"ledger has slot {top} but session_slot is {current}")
    return {"ok": not problems, "problem_count": len(problems), "problems": problems}


def main(argv):
    if len(argv) != 2:
        print(json.dumps({"error": "usage: invariants.py <learner_dir> <courses_dir>"}))
        return 2
    return cli.emit(check(argv[0], argv[1]))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
