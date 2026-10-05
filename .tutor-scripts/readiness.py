#!/usr/bin/env python3
"""
readiness.py -- an honest, bounded answer to "am I ready?" (L-10).

    python3 readiness.py <learner_dir> <courses_dir> <course_id>

NOT a grade prediction. It summarises evidence the tutor really holds, with its limits stated, so the tutor can answer
without bluffing in either direction:

  evidence   stages passed / total; items in the specification that stages teach (coverage); how many of those items the
             learner has actually been observed on; mean BKT mastery over the OBSERVED items; unresolved errors; the weakest
             observed items
  band       not_enough_evidence | early | building | solid   (never a mark, grade or percentage)
               - fewer than 30% of the taught items observed           -> not_enough_evidence
               - mean observed mastery >= 0.80 and >= 75% of stages passed -> solid
               - mean observed mastery >= 0.60                         -> building
               - otherwise                                             -> early
               - a course whose coverage is not `full`, or not itemised, is capped at `building` / `not_enough_evidence`
  strength   low / medium / high - how much evidence stands behind the band (total observations: <10, <40, 40+)
  caveats    always stated: practice conditions are not exam conditions; mastery is an estimate from few observations;
             a specification gap; unobserved items are counted as unknown, not as weak or strong

Read-only. Output: {course_id, band, strength, evidence{...}, weakest_items[], caveats[]}.
"""
import json
import os
import sys

import coverage_check
from tutorlib import cli

OBSERVED_FLOOR = 0.30
SOLID_MASTERY, SOLID_STAGES, BUILDING_MASTERY = 0.80, 0.75, 0.60


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def assess(learner_dir, courses_dir, course_id):
    subj = _load(os.path.join(learner_dir, "subjects", f"{course_id}.json"))
    course = _load(os.path.join(courses_dir, course_id, "course.json"))
    cmap = _load(os.path.join(courses_dir, course_id, "curriculum_map.json"))
    if subj is None or course is None:
        return {"error": f"cannot read subjects/course for {course_id!r}"}
    status = subj.get("syllabus_status") or {}
    ladder = course.get("stage_ladder", list(status))
    passed = sum(1 for s in ladder if status.get(s) in ("pass", "withheld"))
    stages_frac = passed / len(ladder) if ladder else 0.0

    cov = coverage_check.check(os.path.join(courses_dir, course_id))
    itemised = bool(cov.get("items_declared"))
    taught_items = []
    if itemised and cmap:
        for s in ladder:
            taught_items += [i for i in (cmap.get(s) or {}).get("covers_items", [])]
    taught_items = sorted(set(taught_items))
    mastery = subj.get("item_mastery") if isinstance(subj.get("item_mastery"), dict) else {}
    observed = [(i, mastery[i]) for i in taught_items if isinstance(mastery.get(i), dict) and "p_mastery" in mastery[i]]
    obs_frac = len(observed) / len(taught_items) if taught_items else 0.0
    mean_p = sum(m["p_mastery"] for _, m in observed) / len(observed) if observed else None
    total_obs = sum(int(m.get("observations", 0)) for _, m in observed)
    unresolved = sum(1 for e in subj.get("error_patterns", []) if isinstance(e, dict) and not e.get("resolved"))
    weakest = sorted(({"item_id": i, "p_mastery": round(m["p_mastery"], 3), "observations": m.get("observations", 0)}
                      for i, m in observed if m["p_mastery"] < 0.5), key=lambda d: (d["p_mastery"], d["item_id"]))[:5]

    caveats = ["Practice in a session is not exam conditions: timing, pressure and unseen question styles are not measured here.",
               "Mastery is an estimate from the observations so far, not a measurement; unobserved items are unknown, not strong or weak."]
    if not itemised:
        band = "not_enough_evidence"
        caveats.append("This course's specification has not been itemised, so there is no list of items to measure readiness against.")
    elif obs_frac < OBSERVED_FLOOR:
        band = "not_enough_evidence"
        caveats.append(f"Only {len(observed)} of {len(taught_items)} taught items have been observed so far.")
    elif mean_p >= SOLID_MASTERY and stages_frac >= SOLID_STAGES:
        band = "solid"
    elif mean_p >= BUILDING_MASTERY:
        band = "building"
    else:
        band = "early"
    if itemised and cov.get("computed_status") != "full":
        if band == "solid":
            band = "building"
        caveats.append(f"Coverage is {cov.get('computed_status')!r}: some specification items are not taught by any stage, so readiness for the whole specification cannot be claimed.")
    if cov.get("items_excluded"):
        caveats.append("Some specification items were declared out of scope for this learner's selected options.")
    if unresolved:
        caveats.append(f"{unresolved} diagnosed error(s) are still unresolved.")
    strength = "low" if total_obs < 10 else "medium" if total_obs < 40 else "high"
    return {"course_id": course_id, "band": band, "strength": strength,
            "evidence": {"stages_passed": passed, "stages_total": len(ladder), "items_total": cov.get("items_total"),
                         "items_taught": cov.get("items_taught"), "coverage_status": cov.get("computed_status"),
                         "items_observed": len(observed), "items_taught_listed": len(taught_items),
                         "mean_observed_mastery": round(mean_p, 3) if mean_p is not None else None,
                         "total_observations": total_obs, "unresolved_errors": unresolved},
            "weakest_items": weakest, "caveats": caveats}


def main(argv):
    if len(argv) != 3:
        print(json.dumps({"error": "usage: readiness.py <learner_dir> <courses_dir> <course_id>"}))
        return 2
    return cli.emit(assess(*argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
