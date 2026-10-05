#!/usr/bin/env python3
"""
rubric_lint.py -- are a course's rubric criteria observable enough to grade against? (A-11) Read-only.

    python3 rubric_lint.py <course_dir>

For every stage entry in `rubric.json` it reports, as advisory findings (this never blocks shipping; a human or the compiler decides):
  few_criteria / many_criteria   fewer than 2 or more than 8 criteria (a single criterion cannot separate a pass from a near miss)
  short_criterion                fewer than 6 words (usually a spec-point label such as "3.1.1: Monomers and polymers")
  label_only_stage               EVERY criterion of the stage is short: the stage has no observable criteria at all
  vague_criterion                built on "understands", "is aware of", "has a good grasp of" and similar, which a test answer cannot show
  duplicate_criterion            the same criterion text twice in one stage
  no_pass_threshold              missing or under 6 words
  no_source_locator              the source names no URL and no document reference
Criteria in the real library are descriptive sentences (not M/A mark tags), so the checks are about wording, not mark allocation.
"""
import json
import os
import re
import sys

from tutorlib import cli

VAGUE = re.compile(r"\b(understand(s|ing)?|is aware of|are aware of|awareness of|has a (good|basic|sound|general) (grasp|understanding|knowledge)|"
                   r"knows? about|is familiar with|appreciates?|gains? (an )?insight)\b", re.I)


def lint_stage(stage_id, entry):
    out = []
    crit = entry.get("criteria") if isinstance(entry, dict) else None
    if not isinstance(crit, list):
        return [{"stage_id": stage_id, "rule": "few_criteria", "detail": "criteria is not a list"}]
    texts = [c if isinstance(c, str) else json.dumps(c) for c in crit]
    if len(texts) < 2:
        out.append({"stage_id": stage_id, "rule": "few_criteria", "detail": f"{len(texts)} criterion"})
    if len(texts) > 8:
        out.append({"stage_id": stage_id, "rule": "many_criteria", "detail": f"{len(texts)} criteria"})
    if texts and all(len(t.split()) < 6 for t in texts):
        out.append({"stage_id": stage_id, "rule": "label_only_stage", "detail": "; ".join(t[:30] for t in texts[:3])})
    seen = set()
    for t in texts:
        if len(t.split()) < 6:
            out.append({"stage_id": stage_id, "rule": "short_criterion", "detail": t[:80]})
        if VAGUE.search(t):
            out.append({"stage_id": stage_id, "rule": "vague_criterion", "detail": t[:80]})
        key = re.sub(r"\W+", " ", t.lower()).strip()
        if key in seen:
            out.append({"stage_id": stage_id, "rule": "duplicate_criterion", "detail": t[:80]})
        seen.add(key)
    if len(str(entry.get("pass_threshold") or "").split()) < 6:
        out.append({"stage_id": stage_id, "rule": "no_pass_threshold", "detail": str(entry.get("pass_threshold"))[:60]})
    src = entry.get("source") or {}
    if not (src.get("urls") or src.get("reference") or src.get("document")):
        out.append({"stage_id": stage_id, "rule": "no_source_locator", "detail": ""})
    return out


def lint(course_dir):
    try:
        with open(os.path.join(course_dir, "rubric.json"), encoding="utf-8") as f:
            rubric = json.load(f)
    except (OSError, ValueError) as e:
        return {"error": f"FileNotFoundError: cannot read rubric.json in {course_dir}: {e}"}
    findings = []
    stages = rubric.get("stage_rubrics") or {}
    for sid in sorted(stages):
        findings += lint_stage(sid, stages[sid])
    if isinstance(rubric.get("exam_rubric"), dict):
        findings += lint_stage("exam", rubric["exam_rubric"])
    by_rule = {}
    for f in findings:
        by_rule[f["rule"]] = by_rule.get(f["rule"], 0) + 1
    return {"course_dir": course_dir, "stages_checked": len(stages), "finding_count": len(findings), "by_rule": dict(sorted(by_rule.items())), "findings": findings}


def main(argv):
    if len(argv) != 1:
        print(json.dumps({"error": "usage: rubric_lint.py <course_dir>"}))
        return 2
    return cli.emit(lint(argv[0]))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
