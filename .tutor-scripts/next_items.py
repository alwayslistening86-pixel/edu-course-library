#!/usr/bin/env python3
"""
next_items.py -- which syllabus items should practice focus on next? (L-07, L-03)

    python3 next_items.py <learner_dir> <courses_dir> <course_id> [--count N]

Uses what the tutor already measures. Before this, item_mastery was read only as a pacing hint; this turns it into a
selection. The practice set is INTERLEAVED on purpose: most items come from the current stage, but a share are the
weakest items from stages already passed, so earlier learning keeps being retrieved and discriminated from the new
(interleaving and retrieval practice are among the better-evidenced study strategies - see docs/PEDAGOGY.md).

  weakness(item) = (1 - p_mastery) + 0.25 * unresolved errors on the item (+ 0.1 if never observed, to get it seen)
                   (unobserved items start at P_INIT = 0.3 like item_mastery.py does)
  mix            ceil(70%) of --count from the current stage's items (weakest first), the rest from earlier stages'
                 weakest items (never fewer than 1 prior item when prior items exist and --count >= 3)
  fallbacks      if one pool is short, the other fills the gap; ties break by item id (stable)

Read-only. Output: {course_id, current_stage, items[{item_id, stage_id, pool: current|prior, weakness, p_mastery, observations,
unresolved_errors, reason}], itemised}. Courses that are not itemised return `itemised: false` and no items (the tutor then
falls back to the stage's own practice file).
"""
import json
import math
import os
import sys

from item_mastery import P_INIT
from tutorlib import cli

CURRENT_SHARE = 0.7
ERROR_WEIGHT = 0.25
UNSEEN_BONUS = 0.1


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def choose(learner_dir, courses_dir, course_id, count=6):
    subj = _load(os.path.join(learner_dir, "subjects", f"{course_id}.json"))
    course = _load(os.path.join(courses_dir, course_id, "course.json"))
    cmap = _load(os.path.join(courses_dir, course_id, "curriculum_map.json"))
    if subj is None or course is None or cmap is None:
        return {"error": f"cannot read subjects/course/curriculum_map for {course_id!r}"}
    ladder, cur = course.get("stage_ladder", []), subj.get("current_stage")
    if cur not in ladder:
        return {"error": f"current_stage {cur!r} is not in the course's stage_ladder"}
    if not cmap.get("_syllabus_items"):
        return {"course_id": course_id, "current_stage": cur, "itemised": False, "items": []}
    status = subj.get("syllabus_status") or {}
    mastery = subj.get("item_mastery") if isinstance(subj.get("item_mastery"), dict) else {}
    unresolved = {}
    for e in subj.get("error_patterns", []):
        if isinstance(e, dict) and not e.get("resolved") and e.get("item_id"):
            unresolved[e["item_id"]] = unresolved.get(e["item_id"], 0) + 1

    def describe(item_id, stage_id, pool):
        m = mastery.get(item_id) if isinstance(mastery.get(item_id), dict) else None
        p = m.get("p_mastery", P_INIT) if m else P_INIT
        n_err = unresolved.get(item_id, 0)
        w = (1 - p) + ERROR_WEIGHT * n_err + (UNSEEN_BONUS if not m else 0.0)
        why = [f"mastery {p:.2f}" + ("" if m else " (not yet observed)")]
        if n_err:
            why.append(f"{n_err} unresolved error(s)")
        return {"item_id": item_id, "stage_id": stage_id, "pool": pool, "weakness": round(w, 4), "p_mastery": round(p, 4),
                "observations": (m or {}).get("observations", 0), "unresolved_errors": n_err, "reason": ", ".join(why)}

    seen, current, prior = set(), [], []
    idx = ladder.index(cur)
    for sid in ladder[: idx + 1]:
        for item_id in (cmap.get(sid) or {}).get("covers_items", []):
            if item_id in seen:
                continue
            seen.add(item_id)
            if sid == cur:
                current.append(describe(item_id, sid, "current"))
            elif status.get(sid) in ("pass", "withheld", "fail"):   # stages the learner has actually worked through
                prior.append(describe(item_id, sid, "prior"))
    key = lambda d: (-d["weakness"], d["item_id"])  # noqa: E731
    current.sort(key=key)
    prior.sort(key=key)
    n_cur = math.ceil(count * CURRENT_SHARE)
    n_prior = count - n_cur
    if prior and count >= 3:
        n_prior = max(n_prior, 1)
        n_cur = count - n_prior
    chosen_cur, chosen_prior = current[:n_cur], prior[:n_prior]
    spare = count - len(chosen_cur) - len(chosen_prior)
    if spare > 0:
        chosen_cur += current[len(chosen_cur): len(chosen_cur) + spare]
        spare = count - len(chosen_cur) - len(chosen_prior)
        chosen_prior += prior[len(chosen_prior): len(chosen_prior) + spare]
    # interleave current / prior in the output so the caller presents them mixed
    items, a, b = [], list(chosen_cur), list(chosen_prior)
    while a or b:
        if a:
            items.append(a.pop(0))
        if b:
            items.append(b.pop(0))
    return {"course_id": course_id, "current_stage": cur, "itemised": True, "count": len(items), "items": items,
            "pools": {"current_available": len(current), "prior_available": len(prior)}}


def main(argv):
    args, count = list(argv), 6
    if "--count" in args:
        i = args.index("--count")
        try:
            count = int(args[i + 1])
        except (IndexError, ValueError):
            print(json.dumps({"error": "--count needs an integer"}))
            return 2
        del args[i:i + 2]
    if len(args) != 3 or count < 1:
        print(json.dumps({"error": "usage: next_items.py <learner_dir> <courses_dir> <course_id> [--count N]"}))
        return 2
    return cli.emit(choose(args[0], args[1], args[2], count))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
