#!/usr/bin/env python3
"""
mark_scheme_check.py - deterministic mark-scheme arithmetic check for one course (v1.3.0).

WHAT THIS ESTABLISHES, AND WHAT IT DOES NOT
Every graded item in this library declares its marks in square brackets - "[3]" - and
its answer key spells out how those marks are earned with M (method), A (accuracy) and
B (independent) tags, each carrying its own point value - "M1", "B2", etc. Nothing in
this library's existing tooling checks that the two numbers actually agree: that a "[3]"
item's tags actually sum to 3. They didn't, repeatedly, across builds (ICAEW, ACCA, GCSE
Economics, Economics BSc, Accounting & Finance BSc and others each shipped at least one
mismatch before independent review caught it by hand). This script automates that one
check across the whole library, not just the course being built at the time.

It reads every markdown file in the course that has an "## Answer key" or "## Answers"
section, and for every numbered item in that section that declares "[N marks]" and at
least one M/A/B tag, sums the tag values and compares the total to N.

WHAT IT DELIBERATELY DOES NOT FLAG AS "mismatch"
  * Either/or fallback tags. Some items score "B2 primary mark, explained (B1 if named
    but not explained)" - the parenthesised tag is an ALTERNATIVE score, not an
    additional one. This script only strips a parenthesis whose content itself starts
    with a tag ("(B1 ...)", "(M1 ...)", "(A1 ...)") - never parentheses in general.
    An earlier version of this script stripped ALL parenthesised text, which silently
    ate everything after a half-open interval like "(0,1]" (one real paren, one bracket,
    so a naive depth counter never returns to zero) and lost real tags after it. Fixed
    by only ever removing spans that are unambiguously a fallback-tag parenthetical.
  * "Any N of: ..." flexible-credit items. Some items list more scoring options than
    marks available - "B1 X; B1 Y; B1 Z; B1 W -- any 3 for full marks" - where the raw
    tag sum legitimately exceeds the declared marks by design. When the raw sum is
    OVER the declared total and the item text contains a case-insensitive "any <N>"
    phrase, this is reported separately as "flexible_credit", not "mismatch" - it is
    very likely fine, but is still surfaced so a human can confirm the cap makes sense.
    An UNDER-count is never reclassified this way, on the reasoning that "any N of"
    explains why a sum could run high, never why it could run short.
  * Items with no [N] declaration at all (multiple-choice single-mark items, usually
    marked "Correct: X" with no explicit bracket - out of scope for this check).
  * Items with a [N] declaration but no M/A/B tags found at all (almost always a
    levels-marked essay/extended-response item, e.g. Edexcel-style "Level 1 (1-4) ...
    Level 5 (17-20)" bands - marked holistically by design, not by summed tags).
    Reported as "unverified", never as a mismatch.

KNOWN LIMITATION: the tag pattern (a single letter M/A/B immediately followed by a
digit) can in principle collide with other domain content of the same shape - a
spreadsheet cell reference such as "B2" or "M5" is the one collision actually found in
this library (AAT). Two tightly-scoped exclusions catch the formula-shaped instances
of this - a tag is not counted when it is directly preceded by "(" (as in "(B2,B8)")
or directly followed by ":" "," ")" or "." (as in "B2:B8" or "...B8)"). Real tags in
this corpus are always followed by a space and explanatory text, so this costs nothing
real. It deliberately does NOT require a tag to follow ";" or "." specifically - real
tags are also written back-to-back with no separator ("B1 B1 two of: ..."), after a
comma ("x* = 15.0, A1 y* = 7.5"), or after a connecting word ("... or B1 s1(1)(b) ...")
- an earlier, stricter version of this script excluded all of those as a side effect
and produced far more false negatives than it fixed. One narrow case still gets
through: a cell reference used in ordinary prose rather than a formula, e.g. "not the
whole range B2 to B8" (AAT again) - "B2" there is locally indistinguishable from a
real tag by adjacent punctuation alone. This is a heuristic, not a guarantee. Treat
every "mismatch" this script reports as a lead to read by eye, not as a confirmed bug
- exactly as course-auditor's Tier 3 findings are already treated.

This script never edits a course file. It only reports; a human (or the model, on
request) decides what a flagged item actually needs.

Usage:
    python3 mark_scheme_check.py <course_dir>
Output: JSON to stdout. Exit code is always 0 for a readable course (the status is in
the output).
"""
import json
import os
import re
import sys

# A real tag is never the first character after "(" (that shape belongs to a fallback
# tag, already stripped by FALLBACK_PAREN_RE before this runs, or to a spreadsheet
# formula argument) and never immediately followed by ":" "," ")" or "." (a real tag is
# always followed by a space then explanatory text). See the KNOWN LIMITATION note above.
TAG_RE = re.compile(r"(?<!\()\b([MAB])(\d+)\b(?![:,.)])")
FALLBACK_PAREN_RE = re.compile(r"\([MAB]\d+[^()]*\)")
ANY_N_RE = re.compile(r"\bany\s+\d+\b", re.IGNORECASE)
ITEM_MARKS_RE = re.compile(r"^\s*(\d+)\.\s*\[(\d+)(?:\s*marks?)?\]")
SECTION_HEADING_RE = re.compile(r"^##\s+(Answer key|Answers)\b", re.IGNORECASE)
ANY_HEADING_RE = re.compile(r"^##\s+")
ITEM_START_RE = re.compile(r"^\s*(\d+)\.\s")


def _strip_fallback_tags(text):
    """Remove only '(B1 ...)'-style fallback-tag parentheticals, nothing else."""
    prev = None
    while prev != text:
        prev = text
        text = FALLBACK_PAREN_RE.sub(" ", text)
    return text


def _answer_sections(text):
    """Yield the body text of every '## Answer key' / '## Answers' section in the file."""
    lines = text.splitlines()
    i, n = 0, len(lines)
    while i < n:
        if SECTION_HEADING_RE.match(lines[i]):
            i += 1
            start = i
            while i < n and not ANY_HEADING_RE.match(lines[i]):
                i += 1
            yield "\n".join(lines[start:i])
        else:
            i += 1


def _items_in_section(section_text):
    """Split a section's text into (item_number, item_text) chunks by leading 'N. '."""
    lines = section_text.splitlines()
    items = []
    cur_num, cur_lines = None, []
    for line in lines:
        m = ITEM_START_RE.match(line)
        if m:
            if cur_num is not None:
                items.append((cur_num, "\n".join(cur_lines)))
            cur_num = m.group(1)
            cur_lines = [line]
        elif cur_num is not None:
            cur_lines.append(line)
    if cur_num is not None:
        items.append((cur_num, "\n".join(cur_lines)))
    return items


def _check_file(path, rel_path):
    findings = []
    had_section = False
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        return [{"file": rel_path, "error": f"{type(e).__name__}: {e}"}], False

    for section in _answer_sections(text):
        had_section = True
        for item_num, item_text in _items_in_section(section):
            m = ITEM_MARKS_RE.match(item_text)
            if not m:
                continue  # no "[N]" declaration on this item - out of scope
            declared = int(m.group(2))
            remainder = _strip_fallback_tags(item_text[m.end():])
            tags = TAG_RE.findall(remainder)
            if not tags:
                findings.append({
                    "file": rel_path,
                    "item": item_num,
                    "declared_marks": declared,
                    "status": "unverified",
                    "note": "no M/A/B tags found - likely levels-marked",
                })
                continue
            tag_sum = sum(int(v) for _, v in tags)
            if tag_sum == declared:
                status = "ok"
            elif tag_sum > declared and ANY_N_RE.search(item_text):
                status = "flexible_credit"
            else:
                status = "mismatch"
            entry = {
                "file": rel_path,
                "item": item_num,
                "declared_marks": declared,
                "tag_sum": tag_sum,
                "tags": [f"{letter}{val}" for letter, val in tags],
                "status": status,
            }
            if status != "ok":
                findings.append(entry)
    return findings, had_section


def check_course(course_dir):
    if not os.path.isdir(course_dir):
        return {"__error__": f"not a directory: {course_dir}"}

    all_findings = []
    unverified_count = 0
    checked_files = 0

    for root, _dirs, files in os.walk(course_dir):
        for fname in files:
            if not fname.lower().endswith(".md"):
                continue
            path = os.path.join(root, fname)
            rel_path = os.path.relpath(path, course_dir)
            file_findings, had_section = _check_file(path, rel_path)
            if had_section or file_findings:
                checked_files += 1
            for f in file_findings:
                if f.get("status") == "unverified":
                    unverified_count += 1
                else:
                    all_findings.append(f)

    mismatches = [f for f in all_findings if f.get("status") == "mismatch"]
    flexible = [f for f in all_findings if f.get("status") == "flexible_credit"]
    errors = [f for f in all_findings if "error" in f]

    return {
        "course_dir": os.path.basename(os.path.normpath(course_dir)),
        "files_with_answer_sections": checked_files,
        "mismatch_count": len(mismatches),
        "flexible_credit_count": len(flexible),
        "unverified_count": unverified_count,
        "status": "clean" if not mismatches and not errors else "mismatches_found",
        "mismatches": mismatches,
        "flexible_credit": flexible,
        "errors": errors,
    }


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"__error__": "usage: mark_scheme_check.py <course_dir>"}))
        sys.exit(0)
    result = check_course(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
