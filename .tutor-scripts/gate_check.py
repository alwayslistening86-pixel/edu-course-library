#!/usr/bin/env python3
"""
gate_check.py — deterministic evaluation of course-runner.md's 5 ordered gates.

Gates 1-3 are hard stop/continue gates ("refuse to proceed at all" per
course-runner.md): folder_access, grounding, level_lock. Gate 4 (live recheck)
is not a stop gate — it's a "do this housekeeping step before continuing"
signal; the actual web research it may trigger is real-world lookup, correctly
left to the model, not this script. Gate 5 (phase-convergence) governs
whether *testing* is allowed right now, not whether the session can continue
at all, so it's reported separately from can_proceed rather than folded into
it — a course can still teach lesson/practice while its cohort hasn't
converged.

This script makes no pedagogical decision and runs no research. It only
reads fields that already exist and applies the rule stated in
course-runner.md exactly as written, so gate order and gate logic are never
something the model has to re-derive from prose under load.

Usage:
    python3 gate_check.py <course_json_path> <subjects_json_path_or_NONE> \
        <profile_subjects_dir> <courses_dir> <today_iso_date>

subjects_json_path may be the literal string NONE if the enrollment file
doesn't exist yet (course-runner.md's defensive-create case) - gates 3 and 5
then report accordingly rather than erroring.

Output: JSON to stdout.
"""
import json
import os
import sys

from tutorlib import cli, version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cohort_status import (  # noqa: E402
    LIVE_STATES, compute_cohorts, is_complete, is_standalone, is_suspended, practical_stages,
    prerequisites_status, standalone_cohort_id, withheld_stages,
)
import coverage_check  # noqa: E402


def _load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"__error__": f"{type(e).__name__}: {e}"}


def _current_slot(profile_subjects_dir):
    """The learner's persistent session-slot counter (student_profile.json.session_slot; 0 if never advanced)."""
    profile_dir = os.path.dirname(os.path.abspath(profile_subjects_dir))
    profile = _load_json(os.path.join(profile_dir, "student_profile.json"))
    if "__error__" in profile:
        return None
    return int(profile.get("session_slot", 0))


def _evaluate_gates(course_json_path, subjects_json_path, profile_subjects_dir, courses_dir, today_iso):
    course = _load_json(course_json_path)
    if "__error__" in course:
        return {
            "can_proceed": False,
            "first_blocking_gate": "read_error",
            "detail": f"course.json unreadable: {course['__error__']}",
            "gates": {},
        }

    course_id = os.path.basename(os.path.dirname(os.path.abspath(course_json_path)))

    subj = None
    if subjects_json_path and subjects_json_path != "NONE":
        subj = _load_json(subjects_json_path)
        if "__error__" in subj:
            subj = None  # treat unreadable as missing -> defensive-create case, not a hard error

    gates = {}

    # Gate 0 (N-02): the course declares a minimum engine version this install does not meet. Only present when declared.
    if course.get("min_engine_version"):
        ok, have = version.check_min(course["min_engine_version"])
        if not ok:
            gates["0_engine_version"] = {
                "status": "blocked", "value": have,
                "detail": f"this course needs generic-tutor {course['min_engine_version']} or newer; this install is {have} - update the plugin"}
            return {"can_proceed": False, "first_blocking_gate": "0_engine_version", "gates": gates}

    # Gate 1: folder_access
    folder_status = (course.get("folder_access") or {}).get("status")
    g1_pass = folder_status in ("isolated_confirmed", "shared_confirmed")
    gates["1_folder_access"] = {
        "status": "pass" if g1_pass else "blocked",
        "value": folder_status,
        "detail": "folder_access.status must be isolated_confirmed or shared_confirmed"
                   if not g1_pass else "confirmed",
    }
    if not g1_pass:
        return {"can_proceed": False, "first_blocking_gate": "1_folder_access", "gates": gates}

    # Gate 2: grounding
    grounding_status = course.get("grounding_status")
    g2_pass = not is_suspended(grounding_status)
    gates["2_grounding"] = {
        "status": "pass" if g2_pass else "blocked",
        "value": grounding_status,
        "detail": "course is suspended_ungrounded — route to course-auditor's held/dropped choice"
                   if not g2_pass else "grounded",
    }
    if not g2_pass:
        return {"can_proceed": False, "first_blocking_gate": "2_grounding", "gates": gates}

    # Gate 3: enrollment state (level-lock, dropped, complete). Allowlist, not blocklist:
    # only active / test_pending_convergence may be taught. No enrollment file yet (None)
    # is the defensive-create case and passes.
    roster_state = subj.get("roster_state") if subj else None
    if roster_state == "dormant":
        g3 = ("blocked", "course is dormant, locked behind a lower-level course still incomplete")
    elif subj and is_complete(course, subj):
        g3 = ("blocked", "course is complete - every stage passed (and exam passed, if enabled)")
    elif roster_state == "dropped":
        g3 = ("blocked", "course is dropped - progress is preserved; resume it via /add-course (re-enters the roster cap)")
    elif roster_state is not None and roster_state not in LIVE_STATES:
        g3 = ("blocked", f"unrecognised roster_state {roster_state!r} - refusing to teach")
    else:
        g3 = ("pass", "eligible to teach")
    # v1.3.0: prerequisites (requires_complete as a list; any-of entries allowed). /add-course already
    # refuses an unmet prerequisite - this is the belt-and-braces check before any teaching.
    prereq = None
    if g3[0] == "pass":
        prereq = prerequisites_status(course, profile_subjects_dir, courses_dir)
        if not prereq["met"]:
            g3 = ("blocked", f"prerequisites not complete: {prereq['unmet']}")
    gates["3_level_lock"] = {"status": g3[0], "value": roster_state, "detail": g3[1]}
    if prereq is not None:
        gates["3_level_lock"]["prerequisites"] = prereq
    if g3[0] == "blocked":
        return {"can_proceed": False, "first_blocking_gate": "3_level_lock", "gates": gates}

    # Gate 4: live recheck gating (housekeeping signal, not a stop gate)
    currency = course.get("currency", "live")
    last_check = course.get("last_live_recheck")
    if currency == "historical":
        needs_recheck = False
        recheck_reason = "currency is historical — skipped permanently"
    elif last_check == today_iso:
        needs_recheck = False
        recheck_reason = "already checked today"
    else:
        needs_recheck = True
        recheck_reason = "not checked today (or never) — run the live recheck before proceeding"
    gates["4_live_recheck"] = {"needs_recheck": needs_recheck, "detail": recheck_reason}

    # Gate 5: phase-convergence (governs testing eligibility, not general continuation)
    cohort_id = subj.get("cohort_id") if subj else None
    if subj and is_standalone(course):
        cohort_id = standalone_cohort_id(course_id)  # v1.3.0: a standalone course is its own cohort
    convergence = None
    if cohort_id is not None:
        cohorts, errors = compute_cohorts(profile_subjects_dir, courses_dir)
        cohort = cohorts.get(str(cohort_id))
        if cohort:
            convergence = {
                "cohort_id": cohort_id,
                "converged": cohort["converged"],
                "waiting_on": cohort["waiting_on"],
                "bottleneck": cohort["bottleneck"],
                "this_course_is_bottleneck": cohort["bottleneck"] == course_id,
            }
    gates["5_phase_convergence"] = convergence or {"detail": "no cohort data available yet (no enrollment or empty cohort)"}

    return {"can_proceed": True, "first_blocking_gate": None, "current_slot": _current_slot(profile_subjects_dir),
            "standalone": is_standalone(course), "gates": gates,
            "notices": _notices_block(course, subj),
            "practical": _practical_block(course, subj, os.path.dirname(os.path.abspath(course_json_path)))}


def _notices_block(course, subj):
    """v1.3.0 learner notices. course.json.learner_notices = [{"id", "text", "stages": [ids] | null, "since"}].
    Returns the notices that apply to the learner's current stage (a null `stages` = course-wide) and that
    the learner has not yet acknowledged (subjects.notices_acknowledged = [{"id", "on"}]). The runner reads
    each one out at the start of the session, then records the acknowledgement. Non-blocking."""
    notices = course.get("learner_notices") or []
    current = (subj or {}).get("current_stage")
    acked = {a.get("id") for a in ((subj or {}).get("notices_acknowledged") or []) if isinstance(a, dict)}
    due = []
    for n in notices:
        if not isinstance(n, dict) or not n.get("id") or not n.get("text"):
            continue  # malformed (or a pre-1.3.0 plain string): validate_structure.py reports it
        stages = n.get("stages")
        if stages is not None and current not in stages:
            continue
        if n["id"] in acked:
            continue
        due.append({"id": n["id"], "text": n["text"], "stages": stages})
    return {"due": due, "count": len(due)}


def _practical_block(course, subj, course_dir):
    """v1.3.0 practical units by declaration: which practical stages are withheld for THIS learner, and the
    syllabus items that are therefore not taught to them (from curriculum_map covers_items). Coverage stays a
    fact about the course; this is the per-learner view the runner discloses. Non-blocking."""
    ps = practical_stages(course)
    if not ps:
        return {"has_practical_stages": False}
    withheld = withheld_stages(course, subj) if subj else []
    cmap = _load_json(os.path.join(course_dir, "curriculum_map.json"))
    items = []
    if "__error__" not in cmap:
        taught_elsewhere = set()
        for stage, entry in cmap.items():
            if stage.startswith("_") or not isinstance(entry, dict):
                continue
            if stage not in withheld:
                taught_elsewhere.update(entry.get("covers_items") or [])
        for stage in withheld:
            entry = cmap.get(stage) if isinstance(cmap.get(stage), dict) else {}
            for it in entry.get("covers_items") or []:
                if it not in taught_elsewhere and it not in items:
                    items.append(it)
    current = (subj or {}).get("current_stage")
    return {
        "has_practical_stages": True,
        "practical_stages": ps,
        "withheld_stages": withheld,
        "theory_only": bool(withheld),
        "items_withheld_for_learner": items,
        "current_stage_is_practical": current in ps,
        "detail": "practical stages are offered only to a learner who has declared the capabilities they need "
                  "(student_profile.json capabilities); a passed practical stage is practice against the board's "
                  "criteria, not certified coursework",
    }


COVERAGE_DETAIL = {
    "full": "every itemised specification item is mapped to a stage whose lesson names it (declared coverage; see coverage_check.py)",
    "partial": "the syllabus has been itemised and some items are not taught by any stage, or a stage claims items its lesson never names - "
               "this course does NOT cover the whole specification; run coverage_check.py for the exact list",
    "unverified": "the syllabus has never been itemised for this course, so whether the whole specification is taught is unknown - "
                  "it teaches a representative selection of each area, not a verified whole syllabus",
}


def _coverage_block(course_json_path):
    """Non-blocking disclosure (v1.2.0; exclusion disclosure added v1.11.0). Computed from the files, not trusted
    from the stored field: the stored coverage_status is only what the last audit wrote, and a stale 'full' must
    not silence the disclosure.

    v1.11.0 fix: 'full' used to suppress disclosure outright, even when that 'full' only holds because some items
    were declared out of scope (e.g. exam-board options the learner didn't select) - a real course could show
    174/298 items taught, 124 excluded, computed_status 'full', and disclose_to_learner False, so the learner was
    never told anything was left out. Declared-and-reasoned exclusions are legitimate (that's what makes 'full'
    meaningful for a course scoped to selected options), but the learner still needs to be told the scope was
    narrowed and what was narrowed out - disclosure is about whether something is being withheld from them, not
    only about whether coverage_check.py found a problem."""
    course = _load_json(course_json_path)
    declared = course.get("coverage_status") if isinstance(course, dict) else None
    cc = coverage_check.check(os.path.dirname(os.path.abspath(course_json_path)))
    computed = cc.get("computed_status", "unverified")
    effective = "full" if (declared == "full" and computed == "full") else (
        "partial" if "partial" in (declared, computed) else "unverified")
    items_excluded = cc.get("items_excluded") or 0 if cc.get("items_declared") else 0

    detail = COVERAGE_DETAIL[effective]
    if effective == "full" and items_excluded:
        detail = (
            f"every itemised specification item is taught, or is one of {items_excluded} item"
            f"{'s' if items_excluded != 1 else ''} explicitly declared out of scope with a reason (e.g. an "
            "unselected option) - this is declared coverage of the SELECTED scope, not automatically the whole "
            "specification; see excluded_items for what and why"
        )

    block = {
        "declared_status": declared,
        "computed_status": computed,
        "effective_status": effective,
        "disclose_to_learner": effective != "full" or bool(items_excluded),
        "detail": detail,
    }
    if cc.get("items_declared"):
        block["items_total"] = cc.get("items_total")
        block["items_taught"] = cc.get("items_taught")
        block["items_excluded"] = items_excluded
        block["uncovered_items"] = cc.get("uncovered_items")
        block["excluded_items"] = cc.get("declared_exclusions")
    return block


def evaluate(course_json_path, subjects_json_path, profile_subjects_dir, courses_dir, today_iso):
    """The five gates, plus a non-blocking `coverage` block (never affects can_proceed: an unaudited course is still
    teachable, but must not be presented as the whole specification - see course-runner)."""
    result = _evaluate_gates(course_json_path, subjects_json_path, profile_subjects_dir, courses_dir, today_iso)
    if result.get("first_blocking_gate") != "read_error":
        result["coverage"] = _coverage_block(course_json_path)
    return result


def main():
    if len(sys.argv) != 6:
        print(json.dumps({"error": "usage: gate_check.py <course.json> <subjects.json|NONE> <profile_subjects_dir> <courses_dir> <today_iso_date>"}))
        sys.exit(2)
    result = evaluate(*sys.argv[1:6])
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
