"""
Golden-output harness (E-01): runs each script's real CLI against a deterministic on-disk
fixture and compares stdout (+ selected resulting files) with a committed snapshot.

Purpose: pin down CLI behaviour byte-for-byte BEFORE refactoring scripts onto tutorlib
(argparse, envelopes, path handling), so any change in output is an explicit, reviewed diff.

Update snapshots deliberately:   UPDATE_GOLDEN=1 python3 -m unittest tests.test_golden_cli
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
GOLDEN = os.path.join(HERE, "golden")

_TS = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?")
_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(obj, str):
            f.write(obj)
        else:
            json.dump(obj, f, indent=2)


def build_course(courses, cid, *, level=2, stages=("S1", "S2", "S3"), standalone=False, requires=(),
                 practical=None, exam=False, grounding="verified", coverage="full"):
    base = os.path.join(courses, cid)
    ladder = list(stages)
    _w(os.path.join(base, "course.json"), {
        "schema_version": 4, "name": f"Course {cid}", "requires_complete": list(requires), "standalone": standalone,
        "folder_access": {"status": "isolated_confirmed"}, "currency": "live", "material_vintage": "2026 spec",
        "academic_level": None if standalone else level, "level_source": "RQF Level, per Ofqual register",
        "level_basis": "standalone" if standalone else "framework", "grounding_status": grounding,
        "last_live_recheck": "2026-10-03", "coverage_status": coverage, "stage_ladder": ladder, "linear": True,
        "framework": None, "practical_stages": practical or {}, "learner_notices": [],
        "exam": {"enabled": exam, "requires_all_stage_tests_passed": True}})
    items = [{"id": f"{s}.1", "title": f"Item {s}", "topic_area": "T"} for s in ladder]
    cmap = {"_meta": {"purpose": "instructional_index_plus_itemised_coverage"},
            "_items_source": {"document": "Spec", "url": "https://example.org/spec", "version": "1", "itemised_on": "2026-09-01"},
            "_syllabus_items": items, "_declared_exclusions": []}
    rub = {"stage_rubrics": {}}
    for s in ladder:
        cmap[s] = {"covers_syllabus_refs": [s], "syllabus_topic": f"Topic {s}", "covers_items": [f"{s}.1"]}
        rub["stage_rubrics"][s] = {"criteria": ["M1", "A1"], "pass_threshold": "70%",
                                   "source": {"issuing_body": "Board", "document": "Mark scheme", "reference": s}}
        for ph in ("lesson", "practice", "test"):
            _w(os.path.join(base, "stages", s, f"{ph}.md"), f"# {s} {ph}\n\nCovers {s}.1: Item {s}\n")
    if exam:
        rub["exam_rubric"] = {"criteria": ["E1"], "pass_threshold": "50%", "source": {"issuing_body": "Board", "document": "d", "reference": "r"}}
        _w(os.path.join(base, "exam", "exam.md"), "# exam\n")
    _w(os.path.join(base, "curriculum_map.json"), cmap)
    _w(os.path.join(base, "rubric.json"), rub)


def build_fixture(tmp):
    courses = os.path.join(tmp, "courses")
    learner = os.path.join(tmp, "profile", "amy")
    subjects = os.path.join(learner, "subjects")
    build_course(courses, "mathA", level=2)
    _w(os.path.join(courses, "mathA", "stages", "S1", "misconceptions.json"), [
        {"pattern": "Thinks multiplying always makes a number bigger, so 3 x 1/2 is greater than 3.",
         "correction": "Multiplying by a fraction below 1 makes the result smaller: 3 x 1/2 = 1 1/2.",
         "source": "plausible, not board-documented"}])
    build_course(courses, "mathB", level=3)
    build_course(courses, "solo", standalone=True, stages=("S1", "S2"))
    build_course(courses, "design", level=2, stages=("S1", "S2"), practical={"S2": ["share_images"]})
    build_course(courses, "broken", level=2)
    os.remove(os.path.join(courses, "broken", "stages", "S2", "test.md"))  # structural fault for validate_structure
    _w(os.path.join(courses, "old", "course.json"), {"name": "Old shape", "academic_level": 2, "stage_ladder": ["S1"],
                                                   "currency": "live", "stages": {"S1": {}}})
    _w(os.path.join(learner, "student_profile.json"), {
        "schema_version": 2, "learner_id": "amy", "consent": {"status": "granted"},
        "roster": {"max_incomplete_courses": 3}, "highest_level_cleared": 1, "session_slot": 5,
        "session_slot_advanced_at": "2026-10-01T09:00:00Z", "capabilities": {}})

    def enrol(cid, state, status, cur, cohort=2):
        _w(os.path.join(subjects, f"{cid}.json"), {
            "schema_version": 5, "course_id": cid, "roster_state": state, "cohort_id": cohort, "syllabus_status": status,
            "notices_acknowledged": [], "current_stage": cur, "current_phase": "practice", "exam_status": "locked",
            "confidence": 0.5, "error_patterns": [], "item_mastery": {}, "remediation": {},
            "last_session_summary": "", "last_updated": "2026-10-01"})
    enrol("mathA", "active", {"S1": "pass", "S2": "unsat", "S3": "unsat"}, "S2")
    enrol("mathB", "dormant", {"S1": "unsat", "S2": "unsat", "S3": "unsat"}, "S1", cohort=3)
    enrol("solo", "active", {"S1": "unsat", "S2": "unsat"}, "S1", cohort="standalone:solo")
    enrol("design", "dropped", {"S1": "pass", "S2": "unsat"}, "S2")
    _w(os.path.join(subjects, "mathA_review_deck.json"), {"schema_version": 1, "course_id": "mathA", "cards": [
        {"id": "k1", "stage_id": "S1", "item_id": "S1.1", "criterion": "M1", "front": "f", "back": "b",
         "interval_sessions": 1, "ease": 2.3, "lapses": 0, "due_at_slot": 5}]})
    return {"T": tmp, "C": courses, "P": os.path.join(tmp, "profile", "amy"), "S": subjects,
            "L": learner, "R": os.path.join(tmp, "profile")}


def normalise(value, tmp):
    if isinstance(value, dict):
        return {k: normalise(v, tmp) for k, v in value.items()}
    if isinstance(value, list):
        return [normalise(v, tmp) for v in value]
    if isinstance(value, str):
        s = value.replace(os.path.realpath(tmp), "<TMP>").replace(tmp, "<TMP>")
        s = _TS.sub("<TS>", s)
        return _DATE.sub("<DATE>", s)
    return value


def run_step(script, args, fx, tmp):
    argv = [sys.executable, os.path.join(SCRIPTS, script)] + [a.format(**fx) for a in args]
    p = subprocess.run(argv, capture_output=True, text=True, cwd=tmp)
    try:
        out = json.loads(p.stdout)
    except ValueError:
        out = p.stdout
    err = p.stderr.strip().splitlines()[-1:] if p.returncode not in (0, 1) else []
    return normalise({"exit": p.returncode, "stdout": out, "stderr_tail": err}, tmp)


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def snapshot_files(paths, fx, tmp):
    out = {}
    for p in paths:
        full = p.format(**fx)
        rel = os.path.relpath(full, tmp)
        out[rel] = normalise(read_json(full), tmp) if os.path.isfile(full) else None
    return out


def compare(case, actual, update):
    path = os.path.join(GOLDEN, f"{case}.json")
    text = json.dumps(actual, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if update:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return None
    if not os.path.exists(path):
        return ("<missing golden file; run with UPDATE_GOLDEN=1 and review it>", text)
    with open(path, encoding="utf-8") as f:
        expected = f.read()
    return None if expected == text else (expected, text)
