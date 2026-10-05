#!/usr/bin/env python3
"""
session_state.py -- the remaining per-session fields of a progress file, written by script instead of by hand (K-32, V-09 groundwork).

    python3 session_state.py phase  <subjects.json> lesson|practice|test
    python3 session_state.py roster <subjects.json> active|test_pending_convergence
    python3 session_state.py exam   <subjects.json> <course.json> locked|available|passed
    python3 session_state.py notice <subjects.json> <notice_id> <today YYYY-MM-DD>
    python3 session_state.py note   <subjects.json> <today YYYY-MM-DD>          (summary text on stdin, <= 400 characters)

Before this, `current_phase`, the live roster states, `exam_status`, `notices_acknowledged` and `last_session_summary` were written
by the model editing JSON; every other progress field already had a script owner. Rules enforced here:
  phase    only lesson / practice / test; never changes `current_stage` or `syllabus_status`
  roster   only active <-> test_pending_convergence; a dormant / dropped enrolment cannot be moved here (journey-planner and
           resume_enrollment.py own those), and a dropped course stays dropped
  exam     `available` only when the course has an exam and every stage is pass / withheld; `passed` only from `available`;
           `locked` any time (reopening a course); never skips a state
  notice   appends {id, on} once (idempotent for a repeated id)
  note     replaces last_session_summary (progress notes are signal-class: kept under `granted` only)
Everything is atomic, locked, ledgered and consent-aware (phase / roster / exam / notice are progress-class; note is signal-class).
"""
import datetime
import json
import sys

from cohort_status import LIVE_STATES, stage_satisfied
from tutorlib import atomic_io, cli, consent, filelock, ledger, state

PHASES = ("lesson", "practice", "test")
EXAM_ORDER = ("locked", "available", "passed")
NOTE_MAX = 400


def _persist(path, data, kind, result):
    allowed, status = consent.check(path, kind)
    if not allowed:
        return {**result, **consent.skipped(status, kind)}
    atomic_io.write_json(path, data)
    return {**result, "written": True}


@ledger.logged("session_state.py", "subjects_path")
@filelock.locked("subjects_path")
def set_phase(subjects_path, phase):
    if phase not in PHASES:
        return {"error": f"phase must be one of {list(PHASES)}"}
    d = state.load(subjects_path, "subjects")
    old = d.get("current_phase")
    d["current_phase"] = phase
    return _persist(subjects_path, d, consent.PROGRESS, {"action": "phase", "old": old, "new": phase})


@ledger.logged("session_state.py", "subjects_path")
@filelock.locked("subjects_path")
def set_roster(subjects_path, new_state):
    if new_state not in LIVE_STATES:
        return {"error": f"roster state must be one of {list(LIVE_STATES)} here; dormant / dropped are owned by journey-planner and resume_enrollment.py"}
    d = state.load(subjects_path, "subjects")
    old = d.get("roster_state")
    if old not in LIVE_STATES:
        return {"error": f"enrolment is {old!r}; only active / test_pending_convergence can be switched here"}
    d["roster_state"] = new_state
    return _persist(subjects_path, d, consent.PROGRESS, {"action": "roster", "old": old, "new": new_state})


@ledger.logged("session_state.py", "subjects_path")
@filelock.locked("subjects_path")
def set_exam(subjects_path, course_path, new):
    if new not in EXAM_ORDER:
        return {"error": f"exam_status must be one of {list(EXAM_ORDER)}"}
    d = state.load(subjects_path, "subjects")
    course = state.load(course_path, "course")
    old = d.get("exam_status", "locked")
    if new != "locked":
        if not (course.get("exam") or {}).get("enabled"):
            return {"error": "this course has no exam (course.json exam.enabled is false)"}
        status = d.get("syllabus_status") or {}
        open_stages = [s for s in course.get("stage_ladder", []) if not stage_satisfied(course, s, status.get(s))]
        if open_stages:
            return {"error": f"the exam opens only when every stage is passed (or withheld); still open: {open_stages}"}
        if new == "passed" and old != "available":
            return {"error": f"exam_status can become 'passed' only from 'available' (it is {old!r})"}
    d["exam_status"] = new
    return _persist(subjects_path, d, consent.PROGRESS, {"action": "exam", "old": old, "new": new})


@ledger.logged("session_state.py", "subjects_path")
@filelock.locked("subjects_path")
def ack_notice(subjects_path, notice_id, today_iso):
    try:
        datetime.date.fromisoformat(today_iso)
    except ValueError:
        return {"error": "today must be YYYY-MM-DD"}
    d = state.load(subjects_path, "subjects")
    acks = d.setdefault("notices_acknowledged", [])
    if any(isinstance(a, dict) and a.get("id") == notice_id for a in acks):
        return {"action": "notice", "id": notice_id, "already_acknowledged": True, "written": False}
    acks.append({"id": notice_id, "on": today_iso})
    return _persist(subjects_path, d, consent.PROGRESS, {"action": "notice", "id": notice_id, "already_acknowledged": False})


@ledger.logged("session_state.py", "subjects_path")
@filelock.locked("subjects_path")
def write_note(subjects_path, today_iso, text):
    try:
        datetime.date.fromisoformat(today_iso)
    except ValueError:
        return {"error": "today must be YYYY-MM-DD"}
    text = " ".join((text or "").split())
    if not text:
        return {"error": "the summary is empty"}
    if len(text) > NOTE_MAX:
        return {"error": f"the summary is {len(text)} characters; keep it to {NOTE_MAX} or fewer (one or two sentences)"}
    d = state.load(subjects_path, "subjects")
    d["last_session_summary"] = text
    d["last_updated"] = today_iso
    return _persist(subjects_path, d, consent.SIGNAL, {"action": "note", "chars": len(text)})


def main(argv):
    try:
        if len(argv) == 3 and argv[0] == "phase":
            return cli.emit(set_phase(argv[1], argv[2]))
        if len(argv) == 3 and argv[0] == "roster":
            return cli.emit(set_roster(argv[1], argv[2]))
        if len(argv) == 4 and argv[0] == "exam":
            return cli.emit(set_exam(argv[1], argv[2], argv[3]))
        if len(argv) == 4 and argv[0] == "notice":
            return cli.emit(ack_notice(argv[1], argv[2], argv[3]))
        if len(argv) == 3 and argv[0] == "note":
            return cli.emit(write_note(argv[1], argv[2], cli.read_stdin()))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": "usage: session_state.py phase|roster|exam|notice|note ... (see the script header)"}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
