#!/usr/bin/env python3
"""
cohort_status.py — deterministic cohort/convergence grouping for generic-tutor.

Why this exists: DESIGN_NOTES.md (v1.0.0 -> v1.0.1) documents that this exact
grouping logic, left as prose re-derived by the model on every /continue and
/plan call, silently drifted: cohort_id existed in the schema but the actual
convergence check pooled every active course globally instead of grouping by
cohort_id, and grounding_status was supposed to (but didn't) exclude a
suspended course from the cohort in two separate places. This script is the
single source of truth for "what is this learner's cohort picture right now" -
course-runner and journey-planner both call it instead of each re-deriving
their own copy of the same rule.

Definitions (must match course-runner.md's Phase-convergence section exactly):
  - A cohort = every subjects/<id>.json sharing the same cohort_id.
  - Eligible member = roster_state in {active, test_pending_convergence} AND
    the bound course.json's grounding_status != "suspended_ungrounded" AND the
    course is not complete (see is_complete). A complete course is still listed
    in `members` (flagged complete: true) so journey-planner's
    highest_level_cleared check can see the whole cohort.
  - Converged = every eligible member in the cohort is at
    roster_state == "test_pending_convergence" simultaneously.
  - all_complete (level clearing) = at least one member is complete and no member
    is blocking. Unfinished dropped / suspended members are listed in
    `excluded_members` and do not block; anything else unfinished (active,
    test_pending_convergence, dormant) is in `blocking_members`.
  - Bottleneck = the eligible, not-yet-ready member with the most remaining
    stages (len(stage_ladder) - count(syllabus_status == "pass")), ties
    broken by course_id for determinism.

This script never decides pedagogy, never grades anything, never invents a
value. It only reads what's already on disk and reports it.

Usage:
    python3 cohort_status.py <profile_subjects_dir> <courses_dir>

Output: JSON to stdout, one object per cohort_id found, plus a flat summary.
"""
import json
import os
import sys

from tutorlib import cli


def _load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"__error__": f"{type(e).__name__}: {e}"}


def is_standalone(course_json):
    """v1.3.0: a standalone course has no academic level and takes no part in the level-lock, cohort
    convergence across courses, or the level ledger. It still holds a roster slot while unfinished."""
    return isinstance(course_json, dict) and bool(course_json.get("standalone"))


def standalone_cohort_id(course_id):
    """Each standalone enrolment is its own cohort: it tests when it alone is ready, and its
    non-numeric id means level_walk() never treats it as a level."""
    return f"standalone:{course_id}"


def practical_stages(course_json):
    ps = course_json.get("practical_stages") if isinstance(course_json, dict) else None
    return ps if isinstance(ps, dict) else {}


def stage_satisfied(course_json, stage_id, value):
    """A stage counts as done when it is `pass`, or (v1.3.0) when it is `withheld` AND the course really
    marks it practical - a learner without the capability completes the course theory-only. `withheld`
    on a non-practical stage is a data error and never counts."""
    if value == "pass":
        return True
    return value == "withheld" and stage_id in practical_stages(course_json)


def withheld_stages(course_json, subject_json):
    ladder = course_json.get("stage_ladder", []) if isinstance(course_json, dict) else []
    ss = subject_json.get("syllabus_status", {}) if isinstance(subject_json, dict) else {}
    return [s for s in ladder if ss.get(s) == "withheld" and s in practical_stages(course_json)]


def _remaining_stage_count(course_json, subject_json):
    ladder = course_json.get("stage_ladder", []) if isinstance(course_json, dict) else []
    syllabus_status = subject_json.get("syllabus_status", {}) if isinstance(subject_json, dict) else {}
    done = sum(1 for s in ladder if stage_satisfied(course_json, s, syllabus_status.get(s)))
    return max(0, len(ladder) - done)


# Single definition of "who may hold or draw a slot" (E-17); every script that asks goes through these.
SUSPENDED = "suspended_ungrounded"
TEST_PENDING = "test_pending_convergence"                    # live course waiting for its cohort to converge
LIVE_STATES = ("active", TEST_PENDING)          # may be taught / draw slots
SLOT_STATES = LIVE_STATES + ("dormant",)                       # hold a roster slot while unfinished


def is_suspended(grounding_status):
    """A grounding-suspended course is frozen, draws no slots and is free of roster cost."""
    return grounding_status == SUSPENDED


def is_complete(course_json, subject_json):
    """A course is complete when every stage_ladder entry is `pass` in syllabus_status (or, v1.3.0,
    `withheld` on a stage the course marks practical - a theory-only completion) and, if
    course.json.exam.enabled, exam_status is `passed` (journey-planner's own definition).

    Derived from data on every call rather than stored as a roster_state value, so there is no
    transition for a skill to forget to write (the same drift class as DESIGN_NOTES v1.0.1).
    An empty stage_ladder is never complete - that is a broken course, not a finished one.
    """
    if not isinstance(course_json, dict) or not isinstance(subject_json, dict):
        return False
    ladder = course_json.get("stage_ladder", [])
    if not ladder:
        return False
    syllabus_status = subject_json.get("syllabus_status", {})
    if any(not stage_satisfied(course_json, s, syllabus_status.get(s)) for s in ladder):
        return False
    exam_enabled = bool((course_json.get("exam") or {}).get("enabled"))
    return (not exam_enabled) or subject_json.get("exam_status") == "passed"


def compute_cohorts(subjects_dir, courses_dir):
    """Returns (cohorts: dict[str, dict], errors: list[str])."""
    errors = []
    cohorts = {}

    if not os.path.isdir(subjects_dir):
        return {}, [f"subjects_dir does not exist: {subjects_dir}"]

    subject_files = sorted(
        fn for fn in os.listdir(subjects_dir)
        if fn.endswith(".json") and not fn.endswith("_review_deck.json")
    )

    for fn in subject_files:
        subj_path = os.path.join(subjects_dir, fn)
        subj = _load_json(subj_path)
        if "__error__" in subj:
            errors.append(f"{fn}: {subj['__error__']}")
            continue

        course_id = subj.get("course_id") or fn[:-5]
        cohort_id = subj.get("cohort_id")
        roster_state = subj.get("roster_state")

        course_path = os.path.join(courses_dir, course_id, "course.json")
        course = _load_json(course_path)
        if "__error__" in course:
            errors.append(f"{course_id}: course.json unreadable ({course['__error__']})")
            grounding_status = None
        else:
            grounding_status = course.get("grounding_status")

        if "__error__" not in course and is_standalone(course):
            # Standalone: always its own cohort, whatever the file says (never grouped with a level).
            cohort_id = standalone_cohort_id(course_id)
        if cohort_id is None:
            errors.append(f"{course_id}: no cohort_id on subjects file — cannot group, excluded from all cohorts")
            continue

        cohort_key = str(cohort_id)
        cohorts.setdefault(cohort_key, {"cohort_id": cohort_id, "members": []})

        complete = is_complete(course, subj) if "__error__" not in course else False
        # A finished course has nothing left to test-gate on: it must not sit in the cohort as a
        # permanent "not ready" bottleneck (it stays in `members` so highest_level_cleared can
        # still see the whole cohort).
        eligible = roster_state in LIVE_STATES and not is_suspended(grounding_status) and not complete
        remaining = _remaining_stage_count(course, subj) if "__error__" not in course else None

        cohorts[cohort_key]["members"].append({
            "course_id": course_id,
            "roster_state": roster_state,
            "grounding_status": grounding_status,
            "complete": complete,
            "theory_only": complete and bool(withheld_stages(course, subj)),
            "standalone": "__error__" not in course and is_standalone(course),
            "eligible": eligible,
            "test_ready": roster_state == TEST_PENDING,
            "remaining_stage_count": remaining,
        })

    # finalize each cohort: convergence + bottleneck
    for data in cohorts.values():
        eligible_members = [m for m in data["members"] if m["eligible"]]
        not_ready = [m for m in eligible_members if not m["test_ready"]]

        data["eligible_count"] = len(eligible_members)

        # Level-clearing view (journey-planner's highest_level_cleared check). A dropped or
        # grounding-suspended member that is NOT complete is excluded rather than blocking:
        # a course the learner set down (or whose source vanished under them - not their fault,
        # see course-auditor) must not hold every higher-level course dormant forever, and
        # roster_check.py already ignores such courses when computing the lock floor. A complete
        # member always counts, whatever its state. Exclusions are reported, never silent.
        excluded = []
        blocking = []
        for m in data["members"]:
            if m["complete"]:
                continue
            if m["roster_state"] == "dropped":
                excluded.append({"course_id": m["course_id"], "reason": "dropped, unfinished"})
            elif is_suspended(m["grounding_status"]):
                excluded.append({"course_id": m["course_id"], "reason": "suspended (ungrounded), unfinished"})
            else:
                blocking.append(m["course_id"])
        data["excluded_members"] = excluded
        data["blocking_members"] = blocking
        data["all_complete"] = (
            any(m["complete"] for m in data["members"]) and not blocking
        )
        # A level whose members are ALL excluded (only dropped / suspended, unfinished) has
        # nothing that could ever clear it and nothing blocking it: it is vacuously clear, exactly
        # like a level with no course at all. level_walk() must step over it, not stop at it.
        data["vacuously_clear"] = (
            bool(data["members"]) and not blocking and not any(m["complete"] for m in data["members"])
        )
        data["converged"] = len(eligible_members) > 0 and len(not_ready) == 0
        data["waiting_on"] = [m["course_id"] for m in not_ready]

        if not_ready:
            # bottleneck = furthest from ready (most remaining stages), tie-break by course_id
            ranked = sorted(
                not_ready,
                key=lambda m: (-(m["remaining_stage_count"] or 0), m["course_id"]),
            )
            data["bottleneck"] = ranked[0]["course_id"]
        else:
            data["bottleneck"] = None

    return cohorts, errors


def normalise_prerequisites(requires):
    """v1.3.0: requires_complete is a list. Each entry is a course_id (must be complete) or a list of
    course_ids (any one of them complete). Accepts the pre-1.3.0 single string and null."""
    if requires is None:
        return []
    if isinstance(requires, str):
        return [requires]
    out = []
    for e in requires if isinstance(requires, list) else []:
        if isinstance(e, str):
            out.append(e)
        elif isinstance(e, list) and e and all(isinstance(x, str) for x in e):
            out.append(list(e))
    return out


def prerequisites_status(course_json, subjects_dir, courses_dir):
    """Which of a course's prerequisites the learner has completed. A course counts as complete for a
    prerequisite exactly as is_complete() says - including a theory-only completion (decided 26 Sep
    2026: the theory is the examined content). Returns {"met", "required", "unmet"}; each unmet entry
    is the original entry (a string, or the any-of list)."""
    required = normalise_prerequisites(course_json.get("requires_complete") if isinstance(course_json, dict) else None)

    def _done(cid):
        subj = _load_json(os.path.join(subjects_dir, f"{cid}.json")) if subjects_dir else {"__error__": "no dir"}
        c = _load_json(os.path.join(courses_dir, cid, "course.json"))
        return "__error__" not in subj and "__error__" not in c and is_complete(c, subj)

    unmet = []
    for entry in required:
        options = entry if isinstance(entry, list) else [entry]
        if not any(_done(cid) for cid in options):
            unmet.append(entry)
    return {"met": not unmet, "required": required, "unmet": unmet}


def level_walk(cohorts, current_ledger):
    """Walk highest_level_cleared upward as far as the cohorts allow.

    Starting from the stored ledger, repeatedly take the next cohort_id above it (in numeric order):
      - `all_complete`      -> the ledger advances to it;
      - `vacuously_clear`   -> (every member is an excluded dropped/suspended course: nothing could
                               clear it and nothing blocks it) it is stepped over, like a level with
                               no cohort at all - reported in `skipped_cohorts`, ledger unchanged
                               by it, walk continues;
      - anything else       -> it has a blocking member, so the walk stops there.
    Levels with no cohort at all are skipped for free. This is what lets a ledger that was
    deliberately LOWERED by a resume (resume_enrollment.py --reopen-*) climb back to where it was,
    without a level of abandoned courses becoming a wall (the v1.1.3 trap). It never lowers the
    ledger. Invariant: `stopped_at` is None or `blocking` is non-empty.

    Returns {"from", "to", "cleared_cohorts", "skipped_cohorts", "stopped_at", "blocking"}.
    """
    def _num(x):
        try:
            return int(x)
        except (TypeError, ValueError):
            return None

    by_level = {}
    for data in cohorts.values():
        n = _num(data.get("cohort_id"))
        if n is not None:
            by_level[n] = data
    ledger = int(current_ledger or 0)
    start = ledger
    cleared, skipped = [], []
    stopped_at = None
    blocking = []
    for n in sorted(k for k in by_level if k > start):
        data = by_level[n]
        if data.get("all_complete"):
            ledger = n
            cleared.append(n)
        elif data.get("vacuously_clear"):
            skipped.append({"cohort_id": n, "excluded_members": [e["course_id"] for e in data.get("excluded_members", [])]})
        else:
            stopped_at = n
            blocking = data.get("blocking_members", [])
            break
    return {"from": start, "to": ledger, "cleared_cohorts": cleared, "skipped_cohorts": skipped,
            "stopped_at": stopped_at, "blocking": blocking}


def main():
    if len(sys.argv) != 3:
        print(json.dumps({"error": "usage: cohort_status.py <profile_subjects_dir> <courses_dir>"}))
        sys.exit(2)
    subjects_dir, courses_dir = sys.argv[1], sys.argv[2]
    cohorts, errors = compute_cohorts(subjects_dir, courses_dir)
    out = {"cohorts": cohorts, "errors": errors}
    # student_profile.json sits beside subjects/; if readable, also report how far the level
    # ledger can climb (journey-planner writes `suggested_highest_level_cleared` when it is higher
    # than the stored value).
    profile = _load_json(os.path.join(os.path.dirname(os.path.abspath(subjects_dir)), "student_profile.json"))
    if "__error__" not in profile:
        stored = profile.get("highest_level_cleared", 0)
        walk = level_walk(cohorts, stored)
        out["level_ledger"] = dict(walk, stored=stored, suggested_highest_level_cleared=max(int(stored or 0), walk["to"]))
    sys.exit(cli.emit(out))


if __name__ == "__main__":
    main()
