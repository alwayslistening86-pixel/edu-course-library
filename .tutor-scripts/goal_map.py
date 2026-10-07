#!/usr/bin/env python3
"""
goal_map.py -- turn a learner's stated goals into prioritised syllabus items, and show progress against them (L-22).

    python3 goal_map.py items  <learner_dir> <courses_dir> <course_id> [--area <topic_area>]
    python3 goal_map.py set    <subjects.json> <course_dir> "<goal>" '<["item id", ...]>' <today YYYY-MM-DD>
    python3 goal_map.py clear  <subjects.json> ["<goal>"]
    python3 goal_map.py report <learner_dir> <courses_dir> <course_id>

Deciding which syllabus items a goal such as "get comfortable with fractions" means is a judgement, so the tutor proposes it (from the
learner's `goals` and this course's itemised specification) and the learner confirms; this script validates, stores and measures it.

items   the course's topic areas with item counts, the learner's goals, and (with --area, or when the course has 80 items or fewer)
        the items themselves: id, title, topic area, and the stage that teaches each. Read-only.
set     store the items for one goal in the learner's `subjects/<course>.json` as `goal_map` (replacing any earlier entry for the same
        goal text). Refuses unknown item ids, an empty goal, more than 60 items. Progress-class write, atomic, locked, ledgered.
clear   remove one goal's mapping, or all of them. Same write rules.
report  per mapped goal: items mapped; how many sit in stages the learner has PASSED (taught, not the same as learned); which remain,
        in the order the course teaches them, with the stage to do next; the mean observed mastery of the taught items and how many
        have been observed at all; the weakest taught items; and items no stage teaches (a specification gap, never a claim). Goals
        with no mapping are listed as such. Read-only.

Every figure counts evidence the tutor holds. A mapping is the tutor's reading of the goal, so the report says so and nothing in it is a
grade or a forecast.
"""
import json
import os
import sys

from tutorlib import cli, consent, filelock, ledger, state

MAX_ITEMS_PER_GOAL = 60
LIST_ALL_UP_TO = 80
WEAK_BELOW = 0.6


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _course(courses_dir, course_id):
    cdir = os.path.join(courses_dir, course_id)
    course, cmap = _load(os.path.join(cdir, "course.json")), _load(os.path.join(cdir, "curriculum_map.json"))
    if not isinstance(course, dict) or not isinstance(cmap, dict):
        return None
    ladder = course.get("stage_ladder") or []
    items = {i["id"]: i for i in (cmap.get("_syllabus_items") or []) if isinstance(i, dict) and isinstance(i.get("id"), str)}
    stage_of = {}
    for s in ladder:
        for item in (cmap.get(s) or {}).get("covers_items", []):
            stage_of.setdefault(item, s)
    return {"ladder": ladder, "items": items, "stage_of": stage_of}


def _goals(learner_dir):
    prof = _load(os.path.join(learner_dir, "student_profile.json")) or {}
    goals = prof.get("goals")
    return [g for g in goals if isinstance(g, str)] if isinstance(goals, list) else []


def list_items(learner_dir, courses_dir, course_id, area=None):
    c = _course(courses_dir, course_id)
    if c is None:
        return {"error": f"cannot read {course_id!r}: it needs a course.json and an itemised curriculum_map.json"}
    areas = {}
    for i in c["items"].values():
        areas[i.get("topic_area") or ""] = areas.get(i.get("topic_area") or "", 0) + 1
    out = {"course_id": course_id, "goals": _goals(learner_dir), "item_count": len(c["items"]), "topic_areas": dict(sorted(areas.items()))}
    subj = _load(os.path.join(learner_dir, "subjects", f"{course_id}.json")) or {}
    out["goal_map"] = subj.get("goal_map", [])
    if area is not None or len(c["items"]) <= LIST_ALL_UP_TO:
        out["items"] = [{"id": i["id"], "title": i.get("title"), "topic_area": i.get("topic_area"), "stage": c["stage_of"].get(i["id"])}
                        for i in c["items"].values() if area is None or i.get("topic_area") == area]
    else:
        out["note"] = f"{len(c['items'])} items: ask again with --area <topic_area> for one area's items"
    return out


@ledger.logged("goal_map.py", "subjects_path")
@filelock.locked("subjects_path")
def set_goal(subjects_path, course_dir, goal, item_ids, today_iso):
    goal = (goal or "").strip()
    if not goal or len(goal) > 120:
        return {"error": "goal must be 1-120 characters"}
    if not (isinstance(item_ids, list) and item_ids and all(isinstance(i, str) for i in item_ids)):
        return {"error": "items must be a non-empty JSON list of item id strings"}
    ids = list(dict.fromkeys(item_ids))
    if len(ids) > MAX_ITEMS_PER_GOAL:
        return {"error": f"at most {MAX_ITEMS_PER_GOAL} items per goal: map a narrower goal, or a topic area at a time"}
    cmap = _load(os.path.join(course_dir, "curriculum_map.json"))
    known = {i.get("id") for i in (cmap or {}).get("_syllabus_items", []) if isinstance(i, dict)}
    if not known:
        return {"error": f"{course_dir} has no itemised curriculum_map.json to map goals onto"}
    unknown = [i for i in ids if i not in known]
    if unknown:
        return {"error": f"not syllabus items of this course: {unknown[:5]}"}
    data = state.load(subjects_path, "subjects")
    mapping = [m for m in data.get("goal_map", []) if isinstance(m, dict) and m.get("goal") != goal]
    mapping.append({"goal": goal, "items": ids, "set_on": today_iso})
    data["goal_map"] = mapping
    allowed, status = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"action": "set", "goal": goal, "items": ids, **consent.skipped(status, consent.PROGRESS)}
    state.save(subjects_path, data, "subjects")
    return {"action": "set", "goal": goal, "item_count": len(ids), "written": True}


@ledger.logged("goal_map.py", "subjects_path")
@filelock.locked("subjects_path")
def clear_goal(subjects_path, goal=None):
    data = state.load(subjects_path, "subjects")
    before = data.get("goal_map", [])
    after = [] if goal is None else [m for m in before if isinstance(m, dict) and m.get("goal") != goal.strip()]
    if len(after) == len(before):
        return {"action": "clear", "removed": 0, "written": False}
    if after:
        data["goal_map"] = after
    else:
        data.pop("goal_map", None)
    allowed, status = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"action": "clear", "removed": len(before) - len(after), **consent.skipped(status, consent.PROGRESS)}
    state.save(subjects_path, data, "subjects")
    return {"action": "clear", "removed": len(before) - len(after), "written": True}


def report(learner_dir, courses_dir, course_id):
    c = _course(courses_dir, course_id)
    subj = _load(os.path.join(learner_dir, "subjects", f"{course_id}.json"))
    if c is None or subj is None:
        return {"error": f"cannot read subjects/course for {course_id!r}"}
    status = subj.get("syllabus_status") or {}
    mastery = subj.get("item_mastery") if isinstance(subj.get("item_mastery"), dict) else {}
    order = {s: n for n, s in enumerate(c["ladder"])}
    mapped = [m for m in subj.get("goal_map", []) if isinstance(m, dict) and isinstance(m.get("items"), list)]
    goals_out = []
    for m in mapped:
        taught, remaining, untaught = [], [], []
        for item in m["items"]:
            stage = c["stage_of"].get(item)
            if stage is None:
                untaught.append(item)
            elif status.get(stage) == "pass":
                taught.append(item)
            else:
                remaining.append(item)
        remaining.sort(key=lambda i: (order.get(c["stage_of"][i], 10 ** 6), i))
        observed = [(i, mastery[i]["p_mastery"]) for i in taught if isinstance(mastery.get(i), dict) and "p_mastery" in mastery[i]]
        weak = sorted((x for x in observed if x[1] < WEAK_BELOW), key=lambda x: (x[1], x[0]))
        goals_out.append({
            "goal": m.get("goal"), "items_mapped": len(m["items"]), "taught": len(taught), "remaining": len(remaining),
            "not_taught_by_this_course": untaught,
            "next_stage": c["stage_of"][remaining[0]] if remaining else None,
            "remaining_in_teaching_order": [{"item": i, "stage": c["stage_of"][i], "title": (c["items"].get(i) or {}).get("title")} for i in remaining[:12]],
            "observed": len(observed),
            "mean_observed_mastery": round(sum(p for _, p in observed) / len(observed), 2) if observed else None,
            "weakest_taught": [{"item": i, "p_mastery": round(p, 2), "title": (c["items"].get(i) or {}).get("title")} for i, p in weak[:5]],
        })
    names = {g["goal"] for g in goals_out}
    unmapped = [g for g in _goals(learner_dir) if g not in names]
    caveats = ["'Taught' means the stage that teaches an item has been passed, not that the item is learned; mastery figures use only items the learner has been observed on.",
               "Which items a goal covers is the tutor's reading of its wording, confirmed with the learner; change it any time."]
    if any(g["not_taught_by_this_course"] for g in goals_out):
        caveats.append("Some mapped items are not taught by any stage of this course, so this course alone cannot meet those parts of the goal.")
    return {"course_id": course_id, "goals": goals_out, "unmapped_goals": unmapped, "caveats": caveats}


def main(argv):
    args = list(argv)
    area = None
    if "--area" in args:
        i = args.index("--area")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--area needs a topic area name"}))
            return 2
        area = args[i + 1]
        del args[i:i + 2]
    try:
        if len(args) == 4 and args[0] == "items":
            return cli.emit(list_items(args[1], args[2], args[3], area))
        if len(args) == 4 and args[0] == "report" and area is None:
            return cli.emit(report(args[1], args[2], args[3]))
        if len(args) == 6 and args[0] == "set" and area is None:
            try:
                ids = json.loads(args[4])
            except ValueError:
                print(json.dumps({"error": "items must be a JSON list of item id strings"}))
                return 1
            return cli.emit(set_goal(args[1], args[2], args[3], ids, args[5]))
        if args and args[0] == "clear" and len(args) in (2, 3) and area is None:
            return cli.emit(clear_goal(args[1], args[2] if len(args) == 3 else None))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": "usage: goal_map.py items <learner> <courses> <course> [--area A] | set <subjects.json> <course_dir> \"<goal>\" '<[ids]>' <today> | clear <subjects.json> [\"<goal>\"] | report <learner> <courses> <course>"}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
