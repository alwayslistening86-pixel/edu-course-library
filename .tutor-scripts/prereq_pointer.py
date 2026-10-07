#!/usr/bin/env python3
"""
prereq_pointer.py -- when the cause is `missing_prerequisite`, where should the learner go back to? (L-21) Read-only.

    python3 prereq_pointer.py <learner_dir> <courses_dir> <course_id> <stage_id>

Candidates, most useful first, at most 3, each with the command the learner can type:
  earlier_stage         a stage before <stage_id> in the same course that the learner's own record says is weak: a `fail` or `withheld` result,
                        low `p_mastery` on its items, or unresolved errors. `/review <course_id> <stage_id>`.
  prerequisite_course   a course this one `requires_complete`, taken from the learner's enrolments: finished ones point at their weakest stage
                        (`/review <course> <stage>`); unfinished ones at `/continue <course>`; one the learner has no enrolment for is named with
                        `/add-course`. Any-of lists use whichever alternative the learner has actually started.
Weakness = (1 - mean observed p_mastery) + 0.25 per unresolved error, 0.5 for a fail; stages with no evidence are only offered when nothing else is
(the stage just before). It points; it never moves the learner, rewrites state or decides the cause (that stays the tutor's judgment).
Item-level prerequisite links (N-08) would sharpen this; until then the evidence is the learner's own record.
"""
import json
import os
import sys

from cohort_status import is_complete, normalise_prerequisites
from tutorlib import cli, ids

MAX = 3


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def stage_weakness(subj, cmap, stage_id):
    """(score, why) for one stage from the learner's record, or (0, None) when there is no evidence."""
    items = (cmap.get(stage_id) or {}).get("covers_items", []) if isinstance(cmap, dict) else []
    mastery = subj.get("item_mastery") if isinstance(subj.get("item_mastery"), dict) else {}
    ps = [m["p_mastery"] for i in items for m in [mastery.get(i)] if isinstance(m, dict) and isinstance(m.get("p_mastery"), (int, float))]
    unresolved = sum(1 for e in subj.get("error_patterns", []) if isinstance(e, dict) and e.get("stage_id") == stage_id and not e.get("resolved"))
    status = (subj.get("syllabus_status") or {}).get(stage_id)
    score, why = 0.0, []
    if ps:
        score += 1 - sum(ps) / len(ps)
        why.append(f"mastery {sum(ps) / len(ps):.2f} on its items")
    if unresolved:
        score += 0.25 * unresolved
        why.append(f"{unresolved} unresolved error(s)")
    if status == "fail":
        score += 0.5
        why.append("a failed test")
    elif status == "withheld":
        score += 0.25
        why.append("withheld (theory only)")
    return round(score, 3), ", ".join(why) or None


def weakest_stage(learner_dir, courses_dir, course_id, stages=None):
    subj = _load(os.path.join(learner_dir, "subjects", f"{course_id}.json")) or {}
    cmap = _load(os.path.join(courses_dir, course_id, "curriculum_map.json")) or {}
    course = _load(os.path.join(courses_dir, course_id, "course.json")) or {}
    best = None
    for sid in (stages if stages is not None else course.get("stage_ladder", [])):
        score, why = stage_weakness(subj, cmap, sid)
        if why and (best is None or score > best[0]):
            best = (score, sid, why)
    return best


def point(learner_dir, courses_dir, course_id, stage_id):
    try:
        ids.validate(course_id, "course id")
        ids.validate(stage_id, "stage id")
    except ids.InvalidId as e:
        return {"error": str(e)}
    course = _load(os.path.join(courses_dir, course_id, "course.json"))
    if course is None:
        return {"error": f"FileNotFoundError: no course {course_id!r}"}
    ladder = course.get("stage_ladder", [])
    if stage_id not in ladder:
        return {"error": f"{stage_id!r} is not a stage of {course_id}"}
    subj = _load(os.path.join(learner_dir, "subjects", f"{course_id}.json")) or {}
    cmap = _load(os.path.join(courses_dir, course_id, "curriculum_map.json")) or {}
    earlier = ladder[:ladder.index(stage_id)]
    cands = []
    for sid in earlier:
        score, why = stage_weakness(subj, cmap, sid)
        if why:
            cands.append((score, {"kind": "earlier_stage", "course_id": course_id, "stage_id": sid, "why": why, "command": f"/review {course_id} {sid}"}))
    for entry in normalise_prerequisites(course.get("requires_complete")):
        options = entry if isinstance(entry, list) else [entry]
        started = [c for c in options if os.path.isfile(os.path.join(learner_dir, "subjects", f"{c}.json"))]
        cid = (started or options)[0]
        psubj = _load(os.path.join(learner_dir, "subjects", f"{cid}.json"))
        pcourse = _load(os.path.join(courses_dir, cid, "course.json"))
        if psubj is None or pcourse is None:
            cands.append((0.05, {"kind": "prerequisite_course", "course_id": cid, "why": "a prerequisite the learner has no enrolment for", "command": f"/add-course {cid}"}))
        elif is_complete(pcourse, psubj):
            w = weakest_stage(learner_dir, courses_dir, cid)
            if w:
                cands.append((w[0], {"kind": "prerequisite_course", "course_id": cid, "stage_id": w[1], "why": f"completed prerequisite, weakest stage: {w[2]}",
                                     "command": f"/review {cid} {w[1]}"}))
        else:
            cands.append((0.4, {"kind": "prerequisite_course", "course_id": cid, "why": "a prerequisite not yet finished", "command": f"/continue {cid}"}))
    cands.sort(key=lambda c: -c[0])
    out = [c for _, c in cands[:MAX]]
    if not out and earlier:
        out = [{"kind": "earlier_stage", "course_id": course_id, "stage_id": earlier[-1], "why": "no record points anywhere: the stage just before",
                "command": f"/review {course_id} {earlier[-1]}"}]
    return {"course_id": course_id, "stage_id": stage_id, "candidates": out}


def main(argv):
    if len(argv) != 4:
        print(json.dumps({"error": "usage: prereq_pointer.py <learner_dir> <courses_dir> <course_id> <stage_id>"}))
        return 2
    return cli.emit(point(*argv))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
