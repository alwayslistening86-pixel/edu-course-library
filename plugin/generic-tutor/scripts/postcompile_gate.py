#!/usr/bin/env python3
"""
postcompile_gate.py — combines validate_structure.py and coverage_check.py
into one `can_ship` verdict for a just-compiled course, so course-compiler's
Step 8 has a single blocking checkpoint instead of two advisory reports a
model could read past.

WHY THIS EXISTS (v1.5.0)
Before this script, course-compiler's Step 8 ran validate_structure.py and
coverage_check.py, then simply "reported back honestly" — a real structural
problem (a missing test.md, a rubric entry with no source) was disclosed in
prose, but nothing stopped the course from being written and enrolled
anyway. That's an advisory loop: it depends on the model reading its own
report carefully every single time, exactly the kind of small recurring
judgment call this plugin otherwise refuses to leave undecided (the same
reasoning as gate_check.py existing at all instead of trusting the model to
remember gate rules unprompted). This script turns the two checks' outputs
into one deterministic verdict — `can_ship: true|false` — so the compiler
has a fact to act on, not just a report to summarize well.

BLOCKING vs ADVISORY — this distinction is deliberate, not exhaustive-by-
default, because not every rough edge validate_structure.py or
coverage_check.py can name should stop a course a learner could otherwise
be taught right now:

  BLOCKING (can_ship: false unless explicitly overridden):
    - missing_stage_files       a ladder entry with no lesson/practice/test
                                 on disk — course-runner would crash on it.
    - rubric_issue              rubric.json itself unreadable.
    - missing_rubric_entries    a ladder stage with no rubric.json entry at
                                 all — matches the "Hard precondition — no
                                 sourced rubric, no course" rule already
                                 stated in course-compiler's SKILL.md; this
                                 script only enforces what that rule already
                                 says, never invents a stricter one.
    - empty_source_entries      a rubric entry with a citation key present
                                 but blank — same hard precondition, the
                                 citation-shaped-but-empty case.
    - unfilled placeholders      {{COURSE_NAME}}-style template text left in any
                                 course .md or .json file (N-13): the course
                                 would teach or cite the placeholder itself.
    - v13_problems              any structural inconsistency in the 1.3.0
                                 fields (bad practical_stages/learner_notices
                                 references, standalone/level_basis
                                 mismatches, a prerequisite naming a course
                                 folder that doesn't exist) — these are data
                                 integrity bugs, not content-quality gaps.

    - test items in practice/lesson  a graded item from a stage's test.md that appears word for word
                                 in that stage's practice.md or lesson.md (the learner could read the
                                 test beforehand; tutorlib/overlap.py).

  ADVISORY (reported, never blocking):
    - orphaned_stage_dirs       content on disk course.json doesn't know
                                 about — a real thing to clean up, but not a
                                 reason to refuse the ladder that DOES exist.
    - misconceptions_status     already explicitly non-blocking per
                                 validate_structure.py's own docstring and
                                 course-compiler Step 4.75.
    - coverage not "full"       explicitly, deliberately non-blocking — see
                                 course-compiler's `coverage_status` docs:
                                 "thin coverage never suspends a course...
                                 a course that is not full is still built."
                                 This script does not relitigate that
                                 decision; it only makes sure it's still
                                 visible in the same combined verdict rather
                                 than a second, easy-to-skim report.

This script never re-judges anything validate_structure.py or
coverage_check.py already decided — it only classifies their already-
computed fields into blocking/advisory and combines them, the same
division of labour as every other script in this plugin (gate_check.py,
review_math.py): the model diagnoses/authors content, scripts own the
deterministic bookkeeping once the facts are in.

OVERRIDE
A blocking verdict is not an unconditional stop — some real courses will
legitimately need to ship with a known, accepted gap (e.g. a single stage's
source is still being tracked down). Call `override` with a plain-text
reason to explicitly ship anyway; the reason is recorded in the verdict
returned (and should be repeated to the learner in course-compiler's Step 8
report, per that skill's "report back honestly" rule) so the override is
never silent — it just isn't automatically refused by this script alone.

Usage:
    python3 postcompile_gate.py check <course_dir>
    python3 postcompile_gate.py override <course_dir> "<reason>"

Output: JSON to stdout. Read-only — writes nothing, matching
validate_structure.py and coverage_check.py, which this wraps.
"""
import json
import os
import re
import sys

from tutorlib import cli, overlap, untrusted

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import change_log  # noqa: E402
import rubric_lint  # noqa: E402
import validate_structure  # noqa: E402
import coverage_check  # noqa: E402
import verify_sources  # noqa: E402


# N-13: template text that was never filled in, e.g. {{COURSE_NAME}} or {{...}}. Needs 3+ capitals so maths such as {{n}} or x^{{2}} is not caught.
PLACEHOLDER = re.compile(r"\{\{(?:[A-Z][A-Z0-9_]{2,}|\.\.\.)[^{}\n]*\}\}")
PLACEHOLDER_SCAN_SUFFIXES = (".md", ".json")


def _placeholders(course_dir):
    """['<file> line N: <excerpt>', ...] for every unfilled template placeholder in the course's own files."""
    out = []
    for root, dirs, names in os.walk(course_dir):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for n in sorted(names):
            if not n.endswith(PLACEHOLDER_SCAN_SUFFIXES):
                continue
            full = os.path.join(root, n)
            try:
                with open(full, encoding="utf-8", errors="replace") as f:
                    for i, line in enumerate(f, 1):
                        m = PLACEHOLDER.search(line)
                        if m:
                            out.append(f"{os.path.relpath(full, course_dir).replace(os.sep, '/')} line {i}: {m.group(0)[:50]}")
            except OSError:
                continue
    return out


def _integrity(course_dir):
    """A-07: (blocking, advisory) notes on stage tests that the learner could read beforehand."""
    blocking, advisory = [], []
    sdir = os.path.join(course_dir, "stages")
    if not os.path.isdir(sdir):
        return blocking, advisory
    for st in sorted(os.listdir(sdir)):
        try:
            with open(os.path.join(sdir, st, "test.md"), encoding="utf-8") as f:
                items = overlap.test_items(f.read())
        except OSError:
            continue
        for other in ("practice", "lesson"):
            try:
                with open(os.path.join(sdir, st, other + ".md"), encoding="utf-8") as f:
                    text = f.read()
            except OSError:
                continue
            same = overlap.verbatim_items(items, text)
            if same:
                blocking.append(f"stages/{st}: {len(same)} test item(s) appear word for word in {other}.md")
            elif items and overlap.long_runs(" ".join(items), text) > 0:
                advisory.append(f"stages/{st}: test and {other}.md share a run of 20+ words (check it is a template, not the answer)")
    return blocking, advisory


def _gate(course_dir):
    structure = validate_structure.validate(course_dir)
    coverage = coverage_check.check(course_dir)

    if "error" in structure:
        return {
            "course_dir": course_dir,
            "can_ship": False,
            "blocking_reasons": [f"validate_structure.py could not run: {structure['error']}"],
            "advisory_notes": [],
            "structure": structure,
            "coverage": coverage,
        }

    blocking_reasons = []
    if structure.get("missing_stage_files"):
        blocking_reasons.append(f"missing stage files: {structure['missing_stage_files']}")
    if structure.get("rubric_issue"):
        blocking_reasons.append(f"rubric.json unreadable: {structure['rubric_issue']}")
    if structure.get("missing_rubric_entries"):
        blocking_reasons.append(f"stages with no rubric.json entry: {structure['missing_rubric_entries']}")
    if structure.get("empty_source_entries"):
        blocking_reasons.append(f"rubric entries with an empty source citation: {structure['empty_source_entries']}")
    if structure.get("v13_problems"):
        blocking_reasons.append(f"1.3.0 field inconsistencies: {structure['v13_problems']}")

    unfilled = _placeholders(course_dir)
    if unfilled:
        blocking_reasons.append(f"unfilled template placeholders ({len(unfilled)}): " + "; ".join(unfilled[:3]) + (" ..." if len(unfilled) > 3 else ""))

    # X-01/X-02: a web-derived course file that carries instruction-like text must not ship unseen.
    scan = untrusted.scan_path(course_dir)
    injected = {f: [x for x in fs if x["severity"] == untrusted.BLOCKING] for f, fs in scan.items()}
    injected = {f: fs for f, fs in injected.items() if fs}
    if injected:
        blocking_reasons.append(
            "possible embedded instructions in course files (web content must never carry instructions): "
            + "; ".join(f"{f} line {x['line']} [{x['rule']}]" for f, fs in injected.items() for x in fs[:3]))

    rub = rubric_lint.lint(course_dir)
    label_only = [f["stage_id"] for f in rub.get("findings", []) if f["rule"] == "label_only_stage"]
    chg = change_log.read(course_dir)
    leak_block, leak_note = _integrity(course_dir)
    for prob in chg.get("problems", []):
        leak_note.append(f"change.md: {prob['rule']} ({prob.get('detail', '')[:60]})")
    if label_only:
        leak_note.append(f"rubric: {len(label_only)} stage(s) have only topic-label criteria, nothing observable to grade against "
                         f"(first: {label_only[0]}); run rubric_lint.py for detail")
    blocking_reasons.extend(leak_block)

    advisory_notes = list(leak_note)
    for f, fs in scan.items():
        for x in fs:
            if x["severity"] == untrusted.ADVISORY:
                advisory_notes.append(f"{f} line {x['line']}: {x['rule']} - {x['excerpt']}")
    if structure.get("orphaned_stage_dirs"):
        advisory_notes.append(f"orphaned stage dirs not in stage_ladder: {structure['orphaned_stage_dirs']}")
    misc_status = structure.get("misconceptions_status")
    if misc_status:
        covered, total = misc_status.get("stages_covered"), misc_status.get("stages_total")
        advisory_notes.append(f"misconceptions: {covered} of {total} stages have a sourced misconceptions.json"
                              if isinstance(misc_status, dict) and covered is not None else f"misconceptions status: {misc_status}")
    urls = verify_sources.collect_urls(course_dir)
    bad = [u for u in urls if not verify_sources.is_http_url(u)]
    if bad:
        blocking_reasons.append(f"cited source is not an http(s) URL: {bad[0][:80]}" + (f" (+{len(bad) - 1} more)" if len(bad) > 1 else ""))
    if urls:
        snaps = verify_sources.load_snapshots(course_dir)["snapshots"]
        have = [u for u in urls if u in snaps]
        dead = [u for u in have if snaps[u].get("status") == "dead"]
        changed = [u for u in have if snaps[u].get("changed")]
        note = f"sources: {len(have)} of {len(urls)} cited URLs have a snapshot (verify_sources.py --write)"
        if dead:
            note += f"; {len(dead)} dead (first: {dead[0][:60]})"
        if changed:
            note += f"; {len(changed)} changed since the last check"
        advisory_notes.append(note)
    computed_coverage = coverage.get("computed_status")
    if "error" in coverage:
        advisory_notes.append(f"coverage_check.py could not run: {coverage['error']}")
    elif computed_coverage != "full":
        advisory_notes.append(
            f"coverage is {computed_coverage!r}, not 'full' — deliberately non-blocking, "
            f"see course.json.coverage_status docs; uncovered_items: {coverage.get('uncovered_items')}"
        )

    return {
        "course_dir": course_dir,
        "can_ship": not blocking_reasons,
        "blocking_reasons": blocking_reasons,
        "advisory_notes": advisory_notes,
        "structure": structure,
        "coverage": coverage,
    }


def check(course_dir):
    return _gate(course_dir)


def override(course_dir, reason):
    result = _gate(course_dir)
    result["overridden"] = True
    result["override_reason"] = reason
    result["can_ship"] = True
    return result


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "usage: postcompile_gate.py check|override <course_dir> [reason]"}))
        sys.exit(2)
    cmd, course_dir = sys.argv[1], sys.argv[2]
    try:
        if cmd == "check":
            result = check(course_dir)
        elif cmd == "override":
            if len(sys.argv) != 4 or not sys.argv[3].strip():
                print(json.dumps({"error": "usage: postcompile_gate.py override <course_dir> \"<reason>\""}))
                sys.exit(2)
            result = override(course_dir, sys.argv[3])
        else:
            print(json.dumps({"error": f"unknown subcommand {cmd!r}, expected check|override"}))
            sys.exit(2)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
