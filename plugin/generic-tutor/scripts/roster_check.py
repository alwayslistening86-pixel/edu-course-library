#!/usr/bin/env python3
"""
roster_check.py — deterministic roster-cap and level-lock computation for
course-compiler.md's Step -1 / Step 0.25 and journey-planner.md's
highest_level_cleared logic.

Definitions (must match profile-kernel.md and course-compiler.md exactly):
  - roster_occupancy = count of subjects/*.json with roster_state in
    {active, test_pending_convergence} AND the bound course is not complete
    (every stage passed, exam passed if enabled - a finished course no longer
    holds an incomplete slot) AND the bound course's
    grounding_status != "suspended_ungrounded" (a suspended course does not
    count against roster.max_incomplete_courses - course-auditor.md, fixed
    for real in v1.0.1 after this exact check was missing in two places).
  - level_lock_floor = the lowest academic_level among the learner's other
    eligible subjects (same eligibility rule as above) whose academic_level
    is strictly greater than highest_level_cleared. None if no such course.
  - A candidate new course at level L:
      - L <= highest_level_cleared, or L >= floor -> joins freely, no lock.
      - L < floor (and L > highest_level_cleared) -> becomes the new floor;
        every other eligible active course above L moves to dormant.

This script never decides whether to actually add a course, and never picks
an academic_level for one - it only computes the arithmetic consequence of a
level once a real, sourced level is already known (course-compiler.md's
Step 0.25 sourcing itself stays entirely a model/research task).

Usage:
    python3 roster_check.py <profile_dir> <courses_dir> [candidate_level [--resume [--course <course_id>]]]

profile_dir must contain student_profile.json and subjects/. candidate_level
is optional - an integer to check the lock consequence of adding a course at
that level, or the literal word `standalone` (v1.3.0) for a standalone course,
which always joins freely, locks nothing and is never itself locked (it still
needs a free roster slot); omit it to just get current occupancy/floor.

v1.3.0: standalone enrolments hold a roster slot while unfinished (decided 26 Sep
2026) but have no academic_level, so they never enter the lock floor, never lock
anything and are never locked.

Output: JSON to stdout.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cohort_status import is_complete, is_standalone  # noqa: E402


def _load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"__error__": f"{type(e).__name__}: {e}"}


def compute(profile_dir, courses_dir, candidate_level=None, resume=False, resume_course_id=None):
    student_path = os.path.join(profile_dir, "student_profile.json")
    student = _load_json(student_path)
    if "__error__" in student:
        return {"error": f"student_profile.json unreadable: {student['__error__']}"}

    max_incomplete = (student.get("roster") or {}).get("max_incomplete_courses")
    highest_cleared = student.get("highest_level_cleared", 0)

    # RESUMING a dropped, unfinished course whose level was already cleared (while it sat out of
    # the count - see cohort_status.py's excluded_members) must not be a free pass: the
    # "at or below highest_level_cleared joins freely" exemption exists for genuinely NEW
    # lower-level courses, and would otherwise let a learner drop a course, clear its level,
    # unlock higher courses, then resume it alongside them with no re-lock. So a resume
    # reopens the level: the lock floor is computed as if highest_level_cleared were one below
    # this course's level, and the caller lowers the stored value to match after the learner
    # confirms. (Only clearing raises the value; only this reopen lowers it.)
    #
    # A course that is already COMPLETE reopens nothing: there is no unfinished work to gate
    # higher courses behind, and clearing only fires when a course *becomes* complete, so a
    # reopened level would stay open until some other course at it finished. When the caller
    # names the course (resume_course_id) the script checks completeness itself; the level
    # number alone cannot tell it.
    reopens_level = False
    already_complete = False
    effective_cleared = highest_cleared
    if resume and resume_course_id:
        _s = _load_json(os.path.join(profile_dir, "subjects", f"{resume_course_id}.json"))
        _c = _load_json(os.path.join(courses_dir, resume_course_id, "course.json"))
        if "__error__" not in _s and "__error__" not in _c:
            already_complete = is_complete(_c, _s)
    if resume and not already_complete and candidate_level is not None and str(candidate_level) != "standalone" and int(candidate_level) <= highest_cleared:
        reopens_level = True
        effective_cleared = int(candidate_level) - 1

    subjects_dir = os.path.join(profile_dir, "subjects")
    eligible = []
    dormant = []   # level-locked, unfinished, non-suspended enrolments (candidates to wake)
    errors = []

    if os.path.isdir(subjects_dir):
        for fn in sorted(os.listdir(subjects_dir)):
            if not fn.endswith(".json") or fn.endswith("_review_deck.json"):
                continue
            subj = _load_json(os.path.join(subjects_dir, fn))
            if "__error__" in subj:
                errors.append(f"{fn}: {subj['__error__']}")
                continue
            course_id = subj.get("course_id") or fn[:-5]
            roster_state = subj.get("roster_state")
            if roster_state not in ("active", "test_pending_convergence", "dormant"):
                continue
            course = _load_json(os.path.join(courses_dir, course_id, "course.json"))
            grounding_status = course.get("grounding_status") if "__error__" not in course else None
            if grounding_status == "suspended_ungrounded":
                continue
            # A finished course no longer holds an "incomplete" slot (the cap is on incomplete courses).
            if "__error__" not in course and is_complete(course, subj):
                continue
            academic_level = course.get("academic_level") if "__error__" not in course else None
            standalone = "__error__" not in course and is_standalone(course)
            if standalone:
                academic_level = None  # never part of the level arithmetic, whatever the file says
            if roster_state == "dormant":
                dormant.append({"course_id": course_id, "academic_level": academic_level, "standalone": standalone})
                continue
            eligible.append({
                "course_id": course_id,
                "roster_state": roster_state,
                "academic_level": academic_level,
                "cohort_id": subj.get("cohort_id"),
            })

    # Dormant (level-locked) courses are still incomplete commitments and hold a slot: the cap is on
    # INCOMPLETE courses. Counting only live ones let above-floor adds (now created dormant, see
    # candidate_state) bypass the cap, and let a drop wake more courses than the cap allows. With
    # dormant counted, locking a course never frees a slot and waking one is occupancy-neutral.
    roster_occupancy = len(eligible) + len(dormant)
    can_add_course = max_incomplete is None or roster_occupancy < max_incomplete

    levels_above_floor = [
        e["academic_level"] for e in eligible
        if e["academic_level"] is not None and e["academic_level"] > effective_cleared
    ]
    level_lock_floor = min(levels_above_floor) if levels_above_floor else None

    # The floor over EVERYTHING still unfinished and above the cleared level - live courses AND
    # dormant ones. This is the level a dormant course must be at to be allowed to wake, and the
    # level a newly added course must not exceed to start live. (Using only the live courses, as
    # level_lock_floor does, would let one drop wake every dormant level at once: with nothing live
    # the floor is None, so a dormant level-3 AND a dormant level-4 course would both wake.)
    pool_levels = [
        c["academic_level"] for c in (eligible + dormant)
        if c["academic_level"] is not None and c["academic_level"] > effective_cleared
    ]
    pool_floor = min(pool_levels) if pool_levels else None

    # Dormant courses that are entitled to wake NOW: at or below the cleared level, or sitting at
    # the lowest unfinished level. Run after any /drop, and after the ledger moves, and wake exactly
    # these - nothing above the floor.
    for d in dormant:
        lvl = d["academic_level"]
        # A standalone course can never be level-locked, so a dormant one (a data error) always wakes.
        d["should_wake"] = d.get("standalone") or (lvl is not None and (lvl <= effective_cleared or (pool_floor is not None and lvl <= pool_floor)))
    wake_now = [d["course_id"] for d in dormant if d["should_wake"]]

    # Everything that holds a slot, in one list, so the "roster is full" message can name it all -
    # `eligible_courses` alone omits the dormant (level-locked) courses that also hold slots.
    occupying = [
        {"course_id": e["course_id"], "roster_state": e["roster_state"], "academic_level": e["academic_level"], "locked": False}
        for e in eligible
    ] + [
        {"course_id": d["course_id"], "roster_state": "dormant", "academic_level": d["academic_level"], "locked": True}
        for d in dormant
    ]

    result = {
        "roster_occupancy": roster_occupancy,
        "occupying_courses": occupying,
        "max_incomplete_courses": max_incomplete,
        "can_add_course": can_add_course,
        "highest_level_cleared": highest_cleared,
        "effective_highest_level_cleared": effective_cleared,
        "reopens_level": reopens_level,
        "already_complete": already_complete,
        "level_lock_floor": level_lock_floor,
        "unfinished_level_floor": pool_floor,
        "dormant_courses": dormant,
        "wake_now": wake_now,
        "eligible_courses": eligible,
        "errors": errors,
    }

    if candidate_level is not None and str(candidate_level) == "standalone":
        result["candidate_level"] = "standalone"
        result["lock_consequence"] = "joins_freely"
        result["courses_that_would_lock"] = []
        result["candidate_state"] = "active"
        result["locked_behind_level"] = None
        return result

    if candidate_level is not None:
        candidate_level = int(candidate_level)
        if reopens_level:
            # Reopening a level re-locks EVERY eligible course above it, whatever else is
            # already active at or below the new floor. (The "candidate < floor" test below is
            # for a genuinely new course: with a same-level course W already active, the floor
            # is W's level, the candidate is not below it, and the check would wrongly report
            # joins_freely with nothing to lock while higher courses stayed live.)
            locks = [
                e["course_id"] for e in eligible
                if e["academic_level"] is not None and e["academic_level"] > candidate_level
            ]
            consequence = "becomes_new_floor" if locks else "joins_freely"
        elif candidate_level <= effective_cleared:
            consequence = "joins_freely"
            locks = []
        elif level_lock_floor is None or candidate_level >= level_lock_floor:
            consequence = "joins_freely"
            locks = []
        else:
            consequence = "becomes_new_floor"
            locks = [
                e["course_id"] for e in eligible
                if e["academic_level"] is not None and e["academic_level"] > candidate_level
            ]
        # Whether the CANDIDATE ITSELF starts live or locked. lock_consequence only says whether it
        # locks OTHER courses; a course added above the lowest unfinished level is itself locked
        # ("dormant: locked behind a lower-level course still incomplete") and must be created that
        # way, or the level-lock silently doesn't hold for anything added later.
        if reopens_level or candidate_level <= effective_cleared or pool_floor is None or candidate_level <= pool_floor:
            candidate_state = "active"
        else:
            candidate_state = "dormant"
        result["candidate_level"] = candidate_level
        result["lock_consequence"] = consequence
        result["courses_that_would_lock"] = locks
        result["candidate_state"] = candidate_state
        result["locked_behind_level"] = pool_floor if candidate_state == "dormant" else None

    return result


def main():
    argv = sys.argv[1:]
    resume = "--resume" in argv
    course_id = None
    if "--course" in argv:
        k = argv.index("--course")
        if k + 1 >= len(argv):
            print(json.dumps({"error": "--course needs a course_id"}))
            sys.exit(2)
        course_id = argv[k + 1]
        del argv[k:k + 2]
    args = [a for a in argv if a != "--resume"]
    if len(args) not in (2, 3) or ((resume or course_id) and len(args) != 3) or (course_id and not resume):
        print(json.dumps({"error": "usage: roster_check.py <profile_dir> <courses_dir> [candidate_level [--resume [--course <course_id>]]]"}))
        sys.exit(2)
    profile_dir, courses_dir = args[0], args[1]
    candidate = args[2] if len(args) == 3 else None
    print(json.dumps(compute(profile_dir, courses_dir, candidate, resume, course_id), indent=2))


if __name__ == "__main__":
    main()
