#!/usr/bin/env python3
"""
coverage_check.py - deterministic syllabus-coverage check for one course (v1.2.0).

WHAT THIS ESTABLISHES, AND WHAT IT DOES NOT
A course is only worth giving a learner if it teaches the whole declared specification.
Until 1.2.0 nothing checked that: curriculum_map.json only said which broad syllabus area
a stage sat in. From 1.2.0 a course can carry an itemised syllabus and a stage-to-item map,
and this script computes, from those files alone, whether every itemised syllabus item is
taught by some stage. It reports DECLARED coverage:

  * every itemised spec item is either mapped to at least one stage, or explicitly
    declared out of scope with a reason (e.g. an option the learner did not select);
  * every stage's claim to teach an item is at least visible in that stage's lesson.md
    (the item's id must appear there) - so a map cannot claim what a lesson never mentions.

It does NOT establish that the items list is a faithful copy of the live specification
(that is course-auditor's Tier 3, a real-world lookup left to the model), that a lesson
explains an item well, or what Claude actually teaches in a session. "full" means
"declared, mapped and visible in the lesson", nothing stronger.

curriculum_map.json layout it reads (all coverage keys are optional; a map without them
is simply "unverified"):
  top-level keys starting with "_" are metadata, never stages
  "_syllabus_items":     [{"id": "7.01a", "title": "paraphrase of the item", "topic_area": "OCR 7", ...}]
  "_items_source":       {"document": "...", "url": "...", "version": "...", "itemised_on": "ISO date"}
  "_declared_exclusions": [{"id": "8.02c", "reason": "not examinable at Foundation / unselected option / ..."}]
  "<stage_id>": {"covers_items": ["7.01a", ...], ...existing covers_syllabus_refs / syllabus_topic...}

Usage:
    python3 coverage_check.py <course_dir>
Output: JSON to stdout. Exit code is always 0 for a readable course (the status is in the output).
"""
import json
import os
import re
import sys

from tutorlib import cli

STATUS_FULL, STATUS_PARTIAL, STATUS_UNVERIFIED = "full", "partial", "unverified"


def _load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"__error__": f"{type(e).__name__}: {e}"}


def _read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def _id_in_text(item_id, text):
    """Whole-token match, case-insensitive. '7.01' must not match inside '7.01a' or '7.01.2'."""
    pat = r"(?<![A-Za-z0-9])" + re.escape(str(item_id)) + r"(?![A-Za-z0-9]|\.[A-Za-z0-9])"
    return re.search(pat, text, re.IGNORECASE) is not None


def _words(text):
    return len(text.split()) if text else 0


def check(course_dir):
    course = _load_json(os.path.join(course_dir, "course.json"))
    if "__error__" in course:
        return {"course_dir": course_dir, "error": f"course.json unreadable: {course['__error__']}"}
    cmap = _load_json(os.path.join(course_dir, "curriculum_map.json"))
    ladder = course.get("stage_ladder", [])
    declared_status = course.get("coverage_status")

    out = {
        "course_dir": course_dir,
        "stage_ladder_length": len(ladder),
        "declared_status": declared_status,
    }

    if "__error__" in cmap or not isinstance(cmap, dict):
        out.update({"items_declared": False, "computed_status": STATUS_UNVERIFIED,
                    "reason": "curriculum_map.json unreadable or not an object",
                    "status_mismatch": declared_status not in (None, STATUS_UNVERIFIED), "clean": False})
        return out

    items = cmap.get("_syllabus_items")
    if not isinstance(items, list) or not items:
        out.update({"items_declared": False, "computed_status": STATUS_UNVERIFIED,
                    "reason": "no _syllabus_items: the syllabus has never been itemised for this course, "
                              "so nothing can be said about whether the whole specification is taught",
                    "status_mismatch": declared_status not in (None, STATUS_UNVERIFIED), "clean": False})
        return out

    problems = {}

    # --- the items list itself
    ids, dupes, bad_items = [], [], []
    for it in items:
        if not isinstance(it, dict) or not it.get("id") or not it.get("title"):
            bad_items.append(it if isinstance(it, dict) else str(it))
            continue
        if it["id"] in ids:
            dupes.append(it["id"])
        ids.append(it["id"])
    idset = set(ids)
    if dupes:
        problems["duplicate_item_ids"] = sorted(set(dupes))
    if bad_items:
        problems["items_missing_id_or_title"] = len(bad_items)

    src = cmap.get("_items_source")
    if not isinstance(src, dict) or not src.get("document") or not src.get("itemised_on"):
        problems["items_source_missing"] = "_items_source needs at least document and itemised_on (provenance for drift checks)"

    # --- exclusions
    excl = cmap.get("_declared_exclusions") or []
    excluded, excl_no_reason, excl_unknown = {}, [], []
    for e in excl:
        if not isinstance(e, dict) or not e.get("id"):
            continue
        if e["id"] not in idset:
            excl_unknown.append(e["id"])
            continue
        if not str(e.get("reason", "")).strip():
            excl_no_reason.append(e["id"])
            continue
        excluded[e["id"]] = e["reason"]
    if excl_no_reason:
        problems["exclusions_without_reason"] = sorted(excl_no_reason)
    if excl_unknown:
        problems["exclusions_of_unknown_item"] = sorted(excl_unknown)

    # --- stage -> items
    stage_items, stages_without, unknown_refs, not_in_lesson = {}, [], {}, {}
    lesson_words = {}
    really_covered = set()  # claimed by a stage AND named in that stage's lesson.md
    for stage in ladder:
        entry = cmap.get(stage)
        claimed = entry.get("covers_items") if isinstance(entry, dict) else None
        lesson = _read_text(os.path.join(course_dir, "stages", stage, "lesson.md"))
        lesson_words[stage] = _words(lesson)
        if not isinstance(claimed, list) or not claimed:
            stages_without.append(stage)
            continue
        stage_items[stage] = claimed
        for iid in claimed:
            if iid not in idset:
                unknown_refs.setdefault(stage, []).append(iid)
                continue
            if lesson is None or not _id_in_text(iid, lesson):
                not_in_lesson.setdefault(stage, []).append(iid)
            else:
                really_covered.add(iid)
    if stages_without:
        problems["stages_without_covers_items"] = stages_without
    if unknown_refs:
        problems["unknown_item_refs"] = unknown_refs
    if not_in_lesson:
        problems["claimed_but_not_in_lesson"] = not_in_lesson

    uncovered = [i for i in ids if i not in really_covered and i not in excluded]
    multi = {i: [s for s, l in stage_items.items() if i in l] for i in ids}
    multi = {i: s for i, s in multi.items() if len(s) > 1}

    clean = not problems and not uncovered
    computed = STATUS_FULL if clean else STATUS_PARTIAL

    out.update({
        "items_declared": True,
        "items_total": len(ids),
        "items_taught": len([i for i in ids if i in really_covered]),
        "items_excluded": len(excluded),
        "uncovered_items": uncovered,
        "declared_exclusions": excluded,
        "items_in_multiple_stages": multi,
        "lesson_words_per_stage": lesson_words,
        "problems": problems,
        "computed_status": computed,
        "status_mismatch": declared_status != computed,
        "clean": clean,
        "note": "computed_status 'full' means every itemised item is mapped to a stage whose lesson.md names it, or is "
                "declared out of scope with a reason. It does not verify that the items match the live specification "
                "(course-auditor Tier 3) or how well any lesson teaches an item.",
    })
    return out


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: coverage_check.py <course_dir>"}))
        sys.exit(2)
    sys.exit(cli.emit(check(sys.argv[1])))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
