#!/usr/bin/env python3
"""
migrate_schema.py — deterministic schema-version migration for course-auditor's Tier 2.

Scope, deliberately narrow: this script performs only the MECHANICAL shape
migration — adding fields whose value is either a fixed default or a pure
structural transform of existing data. It never fills academic_level,
level_source, or grounding_status with anything invented, because those are
sourced/judgment facts (a real regulator's level, a real verified-source
check) that course-compiler's Step 0.25 and course-auditor's Tier 3 own,
never a migration default. Where those fields are missing, this script adds
them as null and reports them in "needs_sourcing" / "needs_verification" so
the calling skill knows exactly what still needs a real answer - it never
guesses on their behalf.

course.json migration (pre-versioning/v0.3.0-shape, schema_version 1 or 2 -> 3, in one hop):
  - schema_version -> 3 (1.2.0: adds coverage_status)
  - coverage_status -> added as "unverified" if absent (never overwritten). This is a stated
    default, not a guess: it says "the syllabus has never been itemised", which is true of any
    course that predates 1.2.0. course-auditor's Tier 3 coverage pass replaces it with the
    value coverage_check.py actually computes ("full" / "partial"); a migration never sets
    "full" itself.
  - academic_level, level_source -> added as null if absent (never overwritten
    if already present, even if this migration runs again)
  - grounding_status -> added as null if absent (course-auditor's Tier 3 sets
    this for real; a fresh compiler build already defaults it to "verified"
    per course-compiler.md, so null here specifically means "never verified
    since migrating")
  - last_live_recheck -> added as null if absent

course.json 3 -> 4 (1.3.0), in the same hop for any older file:
  - standalone -> added as false if absent. The migration NEVER sets it true: making a course
    standalone is a library decision, applied to named courses in a separate reported step.
  - requires_complete -> normalised to a list: null -> [], "id" -> ["id"]. Entries may be ids or
    any-of lists. The migration never ADDS a prerequisite.
  - practical_stages -> added as {} if absent (never guessed).
  - learner_notices -> added as [] if absent; a list of plain strings (pre-1.3.0 hand-written) is
    converted to [{"id": "n1", "text": ..., "stages": null, "since": null}, ...] - course-wide,
    because narrowing a notice to stages is a judgment call; reported so it can be narrowed.
  - level_basis -> inferred only where unambiguous: standalone -> "standalone"; academic_level set
    and level_source mentions "declared" -> "declared"; academic_level set and level_source set
    otherwise -> "framework". Anything else is left null and reported in needs_sourcing.
  - academic_level / level_source are NOT reported as needing a source on a standalone course.

subjects/<course_id>.json migration (schema_version 1 -> 2 -> 3):
  - stage_progress (old flat map) -> renamed to syllabus_status, values
    passed through unchanged (this is a pure rename, not a value transform,
    so it is safe to do mechanically)
  - cohort_id -> can only be set from the course's own academic_level; if
    that is itself still null (unmigrated / unsourced), cohort_id is left
    null and flagged in needs_sourcing rather than guessed
  - schema_version -> 3 (1.3.0): notices_acknowledged added as [] if absent; `withheld` becomes a
    valid syllabus_status value (no data change). A standalone course's enrolment gets
    cohort_id "standalone:<course_id>" (a mechanical fact, not a level).

subjects/<course_id>.json 3 -> 4 (1.4.0, the tutor-core adaptive layer), mechanical only:
  - error_patterns -> added as [] if absent. Owned from here on by error_log.py; this migration only
    guarantees the field exists in the shape that script expects, never invents an entry.
  - confidence -> added as 0.5 (confidence_update.py's DEFAULT_CONFIDENCE) if absent. 0.5 states
    "genuinely unknown, no graded event yet" — never a guess at how the learner is actually doing;
    the first real pass or fail moves it from there.
  - remediation -> added as {} if absent. Owned by remediation_state.py; an empty object means no
    stage has ever needed remediation, not that remediation is unavailable.

Usage:
    python3 migrate_schema.py course <course.json path>
    python3 migrate_schema.py subject <subjects.json path> <matching course.json path>

Writes the file back in place only if something actually changed, and always
prints a JSON report of what changed and what's still open.
"""
import json
import os
import sys

COURSE_SCHEMA_VERSION = 4
SUBJECT_SCHEMA_VERSION = 4
SUBJECT_DEFAULT_CONFIDENCE = 0.5


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def migrate_course(path):
    d = _load(path)
    before = json.dumps(d, sort_keys=True)
    changed_fields = []
    needs_sourcing = []

    old_version = d.get("schema_version")
    if old_version != COURSE_SCHEMA_VERSION:
        d["schema_version"] = COURSE_SCHEMA_VERSION
        changed_fields.append(f"schema_version: {old_version!r} -> {COURSE_SCHEMA_VERSION}")

    if "standalone" not in d:
        d["standalone"] = False
        changed_fields.append("standalone: added as false")
    standalone = bool(d.get("standalone"))

    for field in ("academic_level", "level_source"):
        if field not in d:
            d[field] = None
            changed_fields.append(f"{field}: added as null")
        if d.get(field) is None and not (standalone and field == "academic_level"):
            if not (standalone and field == "level_source"):
                needs_sourcing.append(field)

    req = d.get("requires_complete", None)
    if not isinstance(req, list):
        new_req = [] if req is None else [req]
        d["requires_complete"] = new_req
        changed_fields.append(f"requires_complete: {req!r} -> {new_req!r} (list form)")

    if "practical_stages" not in d:
        d["practical_stages"] = {}
        changed_fields.append("practical_stages: added as {}")

    notices = d.get("learner_notices")
    if notices is None:
        d["learner_notices"] = []
        changed_fields.append("learner_notices: added as []")
    elif isinstance(notices, list) and any(isinstance(n, str) for n in notices):
        converted, k = [], 0
        for n in notices:
            if isinstance(n, str):
                k += 1
                converted.append({"id": f"n{k}", "text": n, "stages": None, "since": None})
            else:
                converted.append(n)
        d["learner_notices"] = converted
        changed_fields.append(f"learner_notices: {k} plain-text notice(s) converted to course-wide objects")
        needs_sourcing.append("learner_notices (converted notices are course-wide; narrow `stages` if they apply to specific stages)")

    if d.get("level_basis") is None:
        src = (d.get("level_source") or "")
        basis = None
        if standalone:
            basis = "standalone"
        elif d.get("academic_level") is not None and "declared" in src.lower():
            basis = "declared"
        elif d.get("academic_level") is not None and src:
            basis = "framework"
        if "level_basis" not in d or basis is not None:
            d["level_basis"] = basis
            changed_fields.append(f"level_basis: {'inferred ' + repr(basis) if basis else 'added as null'}")
        if basis is None:
            needs_sourcing.append("level_basis (framework / declared / standalone - could not be inferred)")
    elif standalone and d.get("level_basis") != "standalone":
        needs_sourcing.append(f"level_basis is {d.get('level_basis')!r} on a standalone course (expected 'standalone')")

    if "grounding_status" not in d:
        d["grounding_status"] = None
        changed_fields.append("grounding_status: added as null")
    if d.get("grounding_status") is None:
        needs_sourcing.append("grounding_status (run Tier 3 grounding verification)")

    if "last_live_recheck" not in d:
        d["last_live_recheck"] = None
        changed_fields.append("last_live_recheck: added as null")

    if "coverage_status" not in d:
        d["coverage_status"] = "unverified"
        changed_fields.append('coverage_status: added as "unverified"')
    if d.get("coverage_status") in (None, "unverified"):
        needs_sourcing.append("coverage_status (run course-auditor's Tier 3 coverage pass: itemise the spec, map stages, run coverage_check.py)")

    after = json.dumps(d, sort_keys=True)
    wrote = False
    if before != after:
        _save(path, d)
        wrote = True

    return {
        "path": path,
        "kind": "course",
        "wrote": wrote,
        "changed_fields": changed_fields,
        "needs_sourcing": needs_sourcing,
    }


def migrate_subject(subj_path, course_path):
    d = _load(subj_path)
    before = json.dumps(d, sort_keys=True)
    changed_fields = []
    needs_sourcing = []

    if "stage_progress" in d and "syllabus_status" not in d:
        d["syllabus_status"] = d.pop("stage_progress")
        changed_fields.append("stage_progress -> syllabus_status (renamed, values unchanged)")

    course = _load(course_path) if os.path.exists(course_path) else {}
    if course.get("standalone"):
        course_id = d.get("course_id") or os.path.basename(subj_path)[:-5]
        want = f"standalone:{course_id}"
        if d.get("cohort_id") != want:
            changed_fields.append(f"cohort_id: {d.get('cohort_id')!r} -> {want!r} (standalone course)")
            d["cohort_id"] = want

    if "notices_acknowledged" not in d:
        d["notices_acknowledged"] = []
        changed_fields.append("notices_acknowledged: added as []")

    if "error_patterns" not in d:
        d["error_patterns"] = []
        changed_fields.append("error_patterns: added as []")

    if "confidence" not in d:
        d["confidence"] = SUBJECT_DEFAULT_CONFIDENCE
        changed_fields.append(f"confidence: added as {SUBJECT_DEFAULT_CONFIDENCE} (unknown, not a guess)")

    if "remediation" not in d:
        d["remediation"] = {}
        changed_fields.append("remediation: added as {}")

    if "cohort_id" not in d or d.get("cohort_id") is None:
        academic_level = course.get("academic_level")
        if academic_level is not None:
            d["cohort_id"] = academic_level
            changed_fields.append(f"cohort_id: set to course's academic_level ({academic_level!r})")
        else:
            d["cohort_id"] = None
            changed_fields.append("cohort_id: added as null (course has no academic_level yet)")
            needs_sourcing.append("cohort_id (blocked on course.json academic_level)")

    old_version = d.get("schema_version")
    if old_version != SUBJECT_SCHEMA_VERSION:
        d["schema_version"] = SUBJECT_SCHEMA_VERSION
        changed_fields.append(f"schema_version: {old_version!r} -> {SUBJECT_SCHEMA_VERSION}")

    after = json.dumps(d, sort_keys=True)
    wrote = False
    if before != after:
        _save(subj_path, d)
        wrote = True

    return {
        "path": subj_path,
        "kind": "subject",
        "wrote": wrote,
        "changed_fields": changed_fields,
        "needs_sourcing": needs_sourcing,
    }


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "usage: migrate_schema.py course <course.json> | migrate_schema.py subject <subjects.json> <course.json>"}))
        sys.exit(2)

    kind = sys.argv[1]
    if kind == "course":
        result = migrate_course(sys.argv[2])
    elif kind == "subject":
        if len(sys.argv) != 4:
            print(json.dumps({"error": "subject mode needs both <subjects.json> and <course.json>"}))
            sys.exit(2)
        result = migrate_subject(sys.argv[2], sys.argv[3])
    else:
        print(json.dumps({"error": f"unknown kind {kind!r}, expected 'course' or 'subject'"}))
        sys.exit(2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
