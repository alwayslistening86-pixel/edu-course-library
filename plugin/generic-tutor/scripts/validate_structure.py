#!/usr/bin/env python3
"""
validate_structure.py — deterministic Tier 1 structural + Tier 3 sourcing-
completeness checks for course-auditor.md.

This is the same logic used by hand during the 2026-09-18 audit of this
learner's course library, formalized. It checks, for one course folder:
  1. Every stage_ladder entry has lesson.md/practice.md/test.md on disk
     (a stage_ladder implying files that don't exist - Tier 1, auto-fixable
     by course-auditor once this script names the gap).
  2. Every stage folder that exists on disk but isn't in stage_ladder
     (the reverse case - orphaned content, never auto-fixed, always
     reported: this is what caught latin's unwired Livy/Virgil stages).
  3. Every stage_ladder entry has a rubric.json entry with a non-empty,
     specific source citation (Tier 3 grounding-completeness). Handles the
     three real rubric.json shapes found in this corpus: a top-level
     "stage_rubrics" dict, a "stages" dict, and a "stages" list - each
     stage entry's source is looked for under any of several real key
     names actually used across these courses (source, sources,
     sourced_from, source_url, sra_source_url, sourceUrl). This script
     never judges whether a cited source is CORRECT or still resolves live
     - that's real-world verification, properly left to the model with
     WebFetch/WebSearch. It only checks that a source citation exists and
     is non-empty for every stage that's actually being taught.

  4. (v1.3.0) The 1.3.0 course fields are internally consistent - `v13_problems`:
     practical_stages keys that aren't in stage_ladder; learner_notices that are
     malformed (not {id, text, stages?}), have duplicate ids, or name stages not
     in the ladder; a standalone course carrying an academic_level or a
     level_basis other than "standalone"; a non-standalone course whose
     level_basis is "standalone"; a requires_complete that isn't a list of ids /
     any-of lists; and prerequisites naming a course folder that does not exist
     next to this one (`missing_prerequisite_courses` - the course is
     unreachable until they are built).

This script never invents or edits a rubric, and never decides whether a gap
found here should be auto-fixed - course-auditor's own tier rules (Tier 1
auto-fixable vs. Tier 3 never-auto-patched) still govern what happens with
what this script reports.

Usage:
    python3 validate_structure.py <course_dir>

<course_dir> must contain course.json and rubric.json directly, and a
stages/ subdirectory. Output: JSON to stdout.
"""
import json
import os
import sys


def _load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"__error__": f"{type(e).__name__}: {e}"}


SOURCE_KEYS = ["source", "sources", "sourced_from", "source_url", "sra_source_url", "sourceUrl"]


def _extract_rubric_map(rubric_json):
    """Returns {stage_id: source_value_or_None}, handling the real shape variants found in this corpus."""
    ids = {}
    container = None
    if isinstance(rubric_json, dict):
        if isinstance(rubric_json.get("stage_rubrics"), dict):
            container = rubric_json["stage_rubrics"]
        elif "stages" in rubric_json:
            container = rubric_json["stages"]

    if isinstance(container, dict):
        for k, v in container.items():
            src = None
            if isinstance(v, dict):
                for sk in SOURCE_KEYS:
                    if v.get(sk):
                        src = v[sk]
                        break
            ids[k] = src
    elif isinstance(container, list):
        for item in container:
            if not isinstance(item, dict):
                continue
            sid = item.get("stage") or item.get("stage_id") or item.get("id")
            src = None
            for sk in SOURCE_KEYS:
                if item.get(sk):
                    src = item[sk]
                    break
            if sid:
                ids[sid] = src
    return ids


def validate(course_dir):
    course_path = os.path.join(course_dir, "course.json")
    rubric_path = os.path.join(course_dir, "rubric.json")
    stages_dir = os.path.join(course_dir, "stages")

    course = _load_json(course_path)
    if "__error__" in course:
        return {"course_dir": course_dir, "error": f"course.json unreadable: {course['__error__']}"}

    ladder = course.get("stage_ladder", [])

    # files-on-disk vs. ladder
    missing_files = []
    for stage in ladder:
        for kind in ("lesson.md", "practice.md", "test.md"):
            p = os.path.join(stages_dir, stage, kind)
            if not os.path.isfile(p):
                missing_files.append(f"{stage}/{kind}")

    stage_dirs_on_disk = set()
    if os.path.isdir(stages_dir):
        stage_dirs_on_disk = {d for d in os.listdir(stages_dir) if os.path.isdir(os.path.join(stages_dir, d))}
    orphaned_stage_dirs = sorted(stage_dirs_on_disk - set(ladder))

    # rubric coverage
    rubric = _load_json(rubric_path)
    rubric_issue = None
    missing_rubric_entries = []
    empty_source_entries = []
    if "__error__" in rubric:
        rubric_issue = f"rubric.json unreadable: {rubric['__error__']}"
    else:
        rubric_map = _extract_rubric_map(rubric)
        for stage in ladder:
            if stage not in rubric_map:
                missing_rubric_entries.append(stage)
            elif not rubric_map[stage]:
                empty_source_entries.append(stage)

    v13 = _v13_problems(course, ladder, os.path.dirname(os.path.abspath(course_dir)))
    misconceptions = _misconceptions_status(course_dir, ladder)

    clean = not (missing_files or orphaned_stage_dirs or missing_rubric_entries or empty_source_entries or rubric_issue or v13)

    return {
        "course_dir": course_dir,
        "stage_ladder_length": len(ladder),
        "clean": clean,
        "missing_stage_files": missing_files,
        "orphaned_stage_dirs": orphaned_stage_dirs,
        "rubric_issue": rubric_issue,
        "missing_rubric_entries": missing_rubric_entries,
        "empty_source_entries": empty_source_entries,
        "v13_problems": v13,
        "misconceptions_status": misconceptions,
    }


def _v13_problems(course, ladder, courses_dir):
    problems = {}
    ladder_set = set(ladder)

    ps = course.get("practical_stages", {})
    if ps is not None and not isinstance(ps, dict):
        problems["practical_stages_not_a_dict"] = True
    elif ps:
        bad = sorted(k for k in ps if k not in ladder_set)
        if bad:
            problems["practical_stages_not_in_ladder"] = bad
        bad_caps = sorted(k for k, v in ps.items() if not (isinstance(v, list) and v and all(isinstance(x, str) for x in v)))
        if bad_caps:
            problems["practical_stages_without_capabilities"] = bad_caps

    notices = course.get("learner_notices", [])
    if notices is not None:
        malformed, seen, dup, bad_stage = [], set(), [], []
        for i, n in enumerate(notices if isinstance(notices, list) else []):
            if not (isinstance(n, dict) and n.get("id") and n.get("text")):
                malformed.append(i)
                continue
            if n["id"] in seen:
                dup.append(n["id"])
            seen.add(n["id"])
            st = n.get("stages")
            if st is not None and (not isinstance(st, list) or any(s not in ladder_set for s in st)):
                bad_stage.append(n["id"])
        if not isinstance(notices, list):
            problems["learner_notices_not_a_list"] = True
        if malformed:
            problems["learner_notices_malformed"] = malformed
        if dup:
            problems["learner_notices_duplicate_ids"] = dup
        if bad_stage:
            problems["learner_notices_bad_stages"] = bad_stage

    standalone = bool(course.get("standalone"))
    basis = course.get("level_basis")
    if standalone:
        if course.get("academic_level") is not None:
            problems["standalone_has_academic_level"] = course.get("academic_level")
        if basis not in (None, "standalone"):
            problems["standalone_level_basis_mismatch"] = basis
    elif basis == "standalone":
        problems["level_basis_standalone_but_course_not_standalone"] = True
    if basis is not None and basis not in ("framework", "declared", "standalone"):
        problems["level_basis_unknown_value"] = basis

    req = course.get("requires_complete")
    if req is not None and not isinstance(req, (list, str)):
        problems["requires_complete_bad_shape"] = True
    else:
        entries = [req] if isinstance(req, str) else (req or [])
        ids = set()
        for e in entries:
            if isinstance(e, str):
                ids.add(e)
            elif isinstance(e, list) and e and all(isinstance(x, str) for x in e):
                ids.update(e)
            else:
                problems["requires_complete_bad_shape"] = True
        missing = sorted(i for i in ids if not os.path.isfile(os.path.join(courses_dir, i, "course.json")))
        if missing:
            problems["missing_prerequisite_courses"] = missing
    return problems


def _misconceptions_status(course_dir, ladder):
    """v1.4.0, non-blocking (never affects `clean`): misconceptions.json is new, optional content — a course
    predating it, or one whose stages just haven't been backfilled yet, is not a validation failure. This
    only reports what exists and whether what exists is well-formed, so course-auditor's coverage-style pass
    has a starting point without re-deriving the shape check itself. Per-stage file: stages/<id>/misconceptions.json,
    a list of 2-4 entries, each {"pattern", "correction", "source"} where source is a real citation or the
    literal string "plausible, not board-documented" (see tutor-core adaptive-teaching-gap scoping note)."""
    per_stage = {}
    for stage in ladder:
        p = os.path.join(course_dir, "stages", stage, "misconceptions.json")
        if not os.path.isfile(p):
            per_stage[stage] = {"present": False}
            continue
        data = _load_json(p)
        if "__error__" in data:
            per_stage[stage] = {"present": True, "well_formed": False, "problem": data["__error__"]}
            continue
        if not isinstance(data, list):
            per_stage[stage] = {"present": True, "well_formed": False, "problem": "not a JSON list"}
            continue
        bad = [i for i, e in enumerate(data)
               if not (isinstance(e, dict) and e.get("pattern") and e.get("correction") and e.get("source"))]
        per_stage[stage] = {
            "present": True,
            "well_formed": not bad,
            "entry_count": len(data),
            "malformed_entry_indices": bad,
        }
    stages_with_file = sum(1 for v in per_stage.values() if v.get("present"))
    return {
        "stages_covered": stages_with_file,
        "stages_total": len(ladder),
        "per_stage": per_stage,
    }


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: validate_structure.py <course_dir>"}))
        sys.exit(2)
    print(json.dumps(validate(sys.argv[1]), indent=2))


if __name__ == "__main__":
    main()
