#!/usr/bin/env python3
"""
plan_estimate.py -- how much is left, and (optionally) is it feasible before a target date? (K-20, L-12)

    python3 plan_estimate.py <learner_dir> <courses_dir> [--today YYYY-MM-DD]

Replaces the planner's "sum the per-stage estimates by hand" (a field the compiler never actually wrote) with a script.

  per course   stages remaining (not pass / withheld) and estimated SLOTS remaining
               = sum over remaining stages of the stage's estimate. Estimate source, in order: course.json `slot_estimates`
               {stage: n}; course.json `slots_per_stage`; the default of 3 (one lesson, one practice, one test slot).
               Add 10% (rounded up) for the review sessions the schedule will also hold.
  rate         availability.sessions_per_week from the profile -> `weeks_remaining` (a rough projection, never a date)
  deadline     only for courses with a learner-set `target` (plan_target.py): days left, slots available at the stated rate,
               `feasibility`: on_track (available >= 1.25 x needed) | tight (>= needed) | short (< needed) | expired.
               When `short`, `shortfall_slots` and the options that would close it are listed - the choice is the learner's.
  all courses  sessions_per_week shared across courses is NOT assumed here: `combined` sums needs so the caller can compare.

Estimates are rough by design (stated in the output); nothing here writes, schedules, or promises a date.
"""
import datetime
import json
import math
import os
import sys

from cohort_status import LIVE_STATES, is_complete, is_suspended
from tutorlib import cli

DEFAULT_SLOTS_PER_STAGE = 3
REVIEW_OVERHEAD = 0.10
ON_TRACK_MARGIN = 1.25
EXPIRY_GRACE_DAYS = 14


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def stage_estimate(course, stage_id):
    est = course.get("slot_estimates")
    if isinstance(est, dict) and isinstance(est.get(stage_id), int) and est[stage_id] > 0:
        return est[stage_id]
    per = course.get("slots_per_stage")
    return per if isinstance(per, int) and per > 0 else DEFAULT_SLOTS_PER_STAGE


def estimate(learner_dir, courses_dir, today=None):
    profile = _load(os.path.join(learner_dir, "student_profile.json"))
    if profile is None:
        return {"error": f"no readable student_profile.json in {learner_dir}"}
    spw = (profile.get("availability") or {}).get("sessions_per_week")
    spw = spw if isinstance(spw, int) and spw > 0 else None
    today_d = None
    if today:
        try:
            today_d = datetime.date.fromisoformat(today)
        except ValueError:
            return {"error": f"--today must be YYYY-MM-DD, got {today!r}"}
    sdir = os.path.join(learner_dir, "subjects")
    courses, total = [], 0
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if not fn.endswith(".json") or fn.endswith("_review_deck.json"):
            continue
        subj = _load(os.path.join(sdir, fn))
        if not isinstance(subj, dict):
            continue
        cid = subj.get("course_id") or fn[:-5]
        course = _load(os.path.join(courses_dir, cid, "course.json")) or {}
        if subj.get("roster_state") not in LIVE_STATES or is_suspended(course.get("grounding_status")) or (course and is_complete(course, subj)):
            continue
        status = subj.get("syllabus_status") or {}
        remaining = [s for s in course.get("stage_ladder", list(status)) if status.get(s) not in ("pass", "withheld")]
        base = sum(stage_estimate(course, s) for s in remaining)
        slots = base + math.ceil(base * REVIEW_OVERHEAD)
        row = {"course_id": cid, "stages_remaining": len(remaining), "slots_remaining_estimate": slots,
               "weeks_remaining_estimate": round(slots / spw, 1) if spw else None}
        tgt = subj.get("target") if isinstance(subj.get("target"), dict) else None
        if tgt and today_d:
            try:
                due = datetime.date.fromisoformat(tgt.get("date"))
            except (TypeError, ValueError):
                due = None
            if due is not None:
                days = (due - today_d).days
                row["target"] = {"date": tgt["date"], "days_left": days}
                if days < -EXPIRY_GRACE_DAYS:
                    row["target"]["feasibility"] = "expired"
                elif spw is None:
                    row["target"]["feasibility"] = "unknown"
                    row["target"]["note"] = "no availability.sessions_per_week in the profile, so no rate to project"
                else:
                    available = max(0, math.floor(max(days, 0) / 7 * spw))
                    row["target"]["slots_available"] = available
                    if available >= slots * ON_TRACK_MARGIN:
                        row["target"]["feasibility"] = "on_track"
                    elif available >= slots:
                        row["target"]["feasibility"] = "tight"
                    else:
                        short = slots - available
                        row["target"]["feasibility"] = "short"
                        row["target"]["shortfall_slots"] = short
                        weeks = max(days, 1) / 7
                        row["target"]["options"] = [
                            f"raise sessions per week to about {math.ceil(slots / weeks)} until the date",
                            "accept that some remaining stages will not be reached before the date (choose which, with the coverage report)",
                            "move the target date later",
                        ]
        courses.append(row)
        total += slots
    return {"sessions_per_week": spw, "courses": courses,
            "combined": {"slots_remaining_estimate": total, "weeks_remaining_estimate": round(total / spw, 1) if spw else None},
            "assumptions": {"default_slots_per_stage": DEFAULT_SLOTS_PER_STAGE, "review_overhead": REVIEW_OVERHEAD,
                            "on_track_margin": ON_TRACK_MARGIN,
                            "note": "rough estimates: no dates are promised and nothing is scheduled"}}


def main(argv):
    args, today = list(argv), None
    if "--today" in args:
        i = args.index("--today")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--today needs a date"}))
            return 2
        today = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        print(json.dumps({"error": "usage: plan_estimate.py <learner_dir> <courses_dir> [--today YYYY-MM-DD]"}))
        return 2
    return cli.emit(estimate(args[0], args[1], today))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
