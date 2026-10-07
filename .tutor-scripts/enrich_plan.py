#!/usr/bin/env python3
"""
enrich_plan.py -- what each course still lacks of the optional content layers, and where the audit's enrichment pass should look (read-only).

    python3 enrich_plan.py <courses_dir> [--course <course_id>]

Per course: `misconceptions` (stages with / without a file, entries that are board-documented vs "plausible, not board-documented"),
`question_bank` (absent, or question and mark totals), `exam_technique` and `command_words` (present or not), `ready_made_items` (numbered items in
`exam/exam.md` that a bank could be built from, which still need mark schemes), and `source_urls` (the URLs the course's own rubric cites: the
starting point for finding examiner reports). `todo` lists the layers worth a pass, most useful first. The numbers decide where to look; writing
the content is the model's job under course-auditor's enrichment tier, reported before anything is written.
"""
import json
import os
import re
import sys

from tutorlib import cli

PLAUSIBLE = "plausible, not board-documented"


def _json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def plan_course(course_dir):
    course = _json(os.path.join(course_dir, "course.json")) or {}
    ladder = course.get("stage_ladder") or []
    if not ladder:                                    # older shape: the ladder lives in the stages folder
        sd = os.path.join(course_dir, "stages")
        ladder = sorted(os.listdir(sd)) if os.path.isdir(sd) else []
    with_file, without, documented, plausible = [], [], 0, 0
    for st in ladder:
        data = _json(os.path.join(course_dir, "stages", st, "misconceptions.json"))
        if not isinstance(data, list):
            without.append(st)
            continue
        with_file.append(st)
        for e in data:
            if isinstance(e, dict) and e.get("source") == PLAUSIBLE:
                plausible += 1
            elif isinstance(e, dict) and e.get("source"):
                documented += 1
    qb = _json(os.path.join(course_dir, "question_bank.json"))
    bank = {"present": False}
    if isinstance(qb, dict) and isinstance(qb.get("questions"), list):
        qs = qb["questions"]
        bank = {"present": True, "questions": len(qs), "marks": sum(q.get("marks", 0) for q in qs if isinstance(q, dict)),
                "stages_covered": len({q.get("stage_id") for q in qs if isinstance(q, dict)}), "stages_total": len(ladder)}
    ready = 0
    try:
        with open(os.path.join(course_dir, "exam", "exam.md"), encoding="utf-8") as f:
            m = re.search(r"(?mi)^##[^\n]*ready-made[^\n]*\n(.*?)(?=^## |\Z)", f.read(), re.S)
            ready = len(re.findall(r"(?m)^\s*\d+\.\s", m.group(1))) if m else 0
    except OSError:
        pass
    rub = _json(os.path.join(course_dir, "rubric.json")) or {}
    urls = rub.get("source_urls") if isinstance(rub.get("source_urls"), list) else []
    out = {
        "stages": len(ladder),
        "misconceptions": {"stages_with_file": len(with_file), "stages_without": len(without), "documented_entries": documented,
                           "plausible_entries": plausible},
        "question_bank": bank,
        "exam_technique": os.path.isfile(os.path.join(course_dir, "exam_technique.md")),
        "command_words": os.path.isfile(os.path.join(course_dir, "command_words.json")),
        "ready_made_items": ready,
        "source_urls": [u for u in urls if isinstance(u, str)][:10],
    }
    todo = []
    if not bank["present"]:
        todo.append("question_bank")
    if without:
        todo.append("misconceptions")
    if not out["exam_technique"]:
        todo.append("exam_technique")
    out["todo"] = todo
    return out


def run(courses_dir, only=None):
    if not os.path.isdir(courses_dir):
        return {"error": f"FileNotFoundError: no courses folder at {courses_dir}"}
    ids = sorted(d for d in os.listdir(courses_dir) if os.path.isfile(os.path.join(courses_dir, d, "course.json")))
    if only:
        if only not in ids:
            return {"error": f"unknown course {only!r}"}
        ids = [only]
    courses = {cid: plan_course(os.path.join(courses_dir, cid)) for cid in ids}
    tot = {"courses": len(courses),
           "without_question_bank": sum(1 for c in courses.values() if not c["question_bank"]["present"]),
           "stages_without_misconceptions": sum(c["misconceptions"]["stages_without"] for c in courses.values()),
           "stages": sum(c["stages"] for c in courses.values()),
           "without_exam_technique": sum(1 for c in courses.values() if not c["exam_technique"])}
    return {"totals": tot, "courses": courses}


def main(argv):
    only = None
    if "--course" in argv:
        i = argv.index("--course")
        if i + 1 >= len(argv):
            print(json.dumps({"error": "--course needs a course id"}))
            return 2
        only = argv[i + 1]
        del argv[i:i + 2]
    if len(argv) != 1:
        print(json.dumps({"error": "usage: enrich_plan.py <courses_dir> [--course <course_id>]"}))
        return 2
    return cli.emit(run(argv[0], only))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
