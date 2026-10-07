#!/usr/bin/env python3
"""
roster_apply.py -- the roster and level-ledger changes that used to be hand-edited by the model, as one script (K-19).

    python3 roster_apply.py drop    <profile_dir> <courses_dir> <course_id> [--preview]
    python3 roster_apply.py advance <profile_dir> <courses_dir>
    python3 roster_apply.py lock    <profile_dir> <course_id> [<course_id> ...]

  drop     roster_state -> "dropped" for an active / test_pending_convergence / dormant course (everything else in its file is
           kept), then wakes every dormant course `roster_check.py` lists in `wake_now` (dormant -> active). Refuses a course that is
           complete, already dropped, missing, or grounding-suspended (that case is the auditor's erase flow, not a drop).
           --preview does every check and reports `would_wake` on a scratch copy of the profile; nothing real is written (C-04: show
           the consequence, get a yes, then run it without the flag).
  advance  after a course completes: walks `highest_level_cleared` up as far as `cohort_status.level_walk` allows (it never lowers
           it), writes the new value, then wakes what the higher ledger unlocked. No change when nothing new has cleared.
  lock     marks the listed live courses dormant (the "adding this course locks those" consequence reported by
           `roster_check.py <candidate_level>`); validates all of them first and changes nothing if any is not live.

Taking the decision from roster_check / cohort_status (the same functions the skills already trusted) and doing the writes here means
the level-lock invariants no longer depend on the model repeating a multi-step edit correctly. Progress-class consent; each file is
written atomically under its lock, the whole operation holds the profile file's lock, and every change is ledgered.
"""
import json
import os
import shutil
import sys
import tempfile

import roster_check
from cohort_status import LIVE_STATES, compute_cohorts, is_complete, is_suspended, level_walk
from tutorlib import cli, consent, filelock, ids, ledger, state


def _valid(course_id):
    try:
        ids.validate(course_id, "course id")
        return True
    except ids.InvalidId:
        return False


def _paths(profile_dir):
    return os.path.join(profile_dir, "student_profile.json"), os.path.join(profile_dir, "subjects")


def _set_state(subjects_dir, course_id, new_state):
    path = os.path.join(subjects_dir, f"{course_id}.json")
    with filelock.file_lock(path):
        d = state.load(path, "subjects")
        old = d.get("roster_state")
        d["roster_state"] = new_state
        state.save(path, d, "subjects")
    ledger.record(path, "roster_apply.py", "set_roster_state", course_id, True, None, {"old": old, "new": new_state})
    return old


def _wake(profile_dir, courses_dir):
    r = roster_check.compute(profile_dir, courses_dir)
    woke = list(r.get("wake_now", [])) if "error" not in r else []
    for cid in woke:
        _set_state(_paths(profile_dir)[1], cid, "active")
    return woke


def _guard(profile_dir):
    pp, sd = _paths(profile_dir)
    if not os.path.isfile(pp):
        return {"error": f"FileNotFoundError: no student_profile.json in {profile_dir}"}
    allowed, cstatus = consent.check(pp, consent.PROGRESS)
    if not allowed:
        return {"action": "not_persisted", "written": False, **consent.skipped(cstatus, consent.PROGRESS)}
    return None


def drop(profile_dir, courses_dir, course_id):
    refused = _guard(profile_dir)
    if refused:
        return refused
    pp, sd = _paths(profile_dir)
    if not _valid(course_id):
        return {"error": f"invalid course id {course_id!r}"}
    cpath = os.path.join(sd, f"{course_id}.json")
    if not os.path.isfile(cpath):
        return {"error": f"FileNotFoundError: {course_id} is not enrolled"}
    with filelock.file_lock(pp):
        subj = state.load(cpath, "subjects")
        course_file = os.path.join(courses_dir, course_id, "course.json")
        try:
            with open(course_file, encoding="utf-8") as f:
                course = json.load(f)
        except (OSError, ValueError):
            course = {}
        current = subj.get("roster_state")
        if is_suspended(course.get("grounding_status")):
            return {"error": f"{course_id} is grounding-suspended: use the auditor's erase-enrolment flow, not /drop"}
        if current == "dropped":
            return {"action": "drop", "course_id": course_id, "already_dropped": True, "woke": [], "written": False}
        if course and is_complete(course, subj):
            return {"error": f"{course_id} is complete: nothing to drop"}
        if current not in LIVE_STATES + ("dormant",):
            return {"error": f"cannot drop a course whose roster_state is {current!r}"}
        _set_state(sd, course_id, "dropped")
        woke = _wake(profile_dir, courses_dir)
    return {"action": "drop", "course_id": course_id, "previous_state": current, "woke": woke, "written": True}


def drop_preview(profile_dir, courses_dir, course_id):
    """What `drop` would do, computed by running it on a throwaway copy of the profile (the ledger lives in the copy too)."""
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, "profile")
        shutil.copytree(profile_dir, copy)
        r = drop(copy, courses_dir, course_id)
    if "error" in r or r.get("written") is False:
        return r
    return {"action": "drop_preview", "course_id": course_id, "previous_state": r["previous_state"], "would_wake": r["woke"], "written": False}


def advance(profile_dir, courses_dir):
    refused = _guard(profile_dir)
    if refused:
        return refused
    pp, sd = _paths(profile_dir)
    with filelock.file_lock(pp):
        profile = state.load(pp, "student_profile")
        stored = int(profile.get("highest_level_cleared") or 0)
        cohorts, errors = compute_cohorts(sd, courses_dir)
        walk = level_walk(cohorts, stored)
        out = {"action": "advance", "from": stored, "to": walk["to"], "cleared_cohorts": walk["cleared_cohorts"],
               "skipped_cohorts": walk["skipped_cohorts"], "stopped_at": walk["stopped_at"], "blocking": walk["blocking"]}
        if errors:
            out["warnings"] = errors
        if walk["to"] <= stored:
            return {**out, "woke": [], "written": False}
        profile["highest_level_cleared"] = walk["to"]
        state.save(pp, profile, "student_profile")
        ledger.record(pp, "roster_apply.py", "advance_ledger", None, True, None, {"old": stored, "new": walk["to"]})
        out["woke"] = _wake(profile_dir, courses_dir)
        out["written"] = True
    return out


def lock(profile_dir, course_ids):
    refused = _guard(profile_dir)
    if refused:
        return refused
    pp, sd = _paths(profile_dir)
    if not course_ids:
        return {"error": "name at least one course to lock"}
    with filelock.file_lock(pp):
        problems = []
        for cid in course_ids:
            p = os.path.join(sd, f"{cid}.json") if _valid(cid) else None
            if p is None or not os.path.isfile(p):
                problems.append(f"{cid}: not enrolled")
                continue
            st = state.load(p, "subjects").get("roster_state")
            if st not in LIVE_STATES:
                problems.append(f"{cid}: roster_state is {st!r}, only a live course can be locked")
        if problems:
            return {"error": "; ".join(problems), "written": False}
        for cid in course_ids:
            _set_state(sd, cid, "dormant")
    return {"action": "lock", "locked": list(course_ids), "written": True}


def main(argv):
    try:
        if len(argv) == 5 and argv[0] == "drop" and argv[4] == "--preview":
            return cli.emit(drop_preview(argv[1], argv[2], argv[3]))
        if len(argv) == 4 and argv[0] == "drop":
            return cli.emit(drop(argv[1], argv[2], argv[3]))
        if len(argv) == 3 and argv[0] == "advance":
            return cli.emit(advance(argv[1], argv[2]))
        if len(argv) >= 3 and argv[0] == "lock":
            return cli.emit(lock(argv[1], argv[2:]))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": "usage: roster_apply.py drop <profile_dir> <courses_dir> <course_id> [--preview] | advance <profile_dir> <courses_dir> | lock <profile_dir> <course_id>..."}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
