#!/usr/bin/env python3
"""
paraphrase_check.py -- does a course copy its sources instead of paraphrasing them? (N-06) Read-only, advisory.

    python3 paraphrase_check.py <course_dir> [--source FILE]... [--min-run N]

Applies the one quotation policy (course-compiler step 4): a quotation is attributed, under 15 words, and at most one per stage;
everything else is the compiler's own words. Findings (advisory; a human or the compiler decides, this never blocks):
  long_quote     a quoted span of 15 or more words (any course text; needs no source)
  many_quotes    more than one quotation of 4 or more words in one stage (any course text; needs no source)
  verbatim_run   with --source: a run of --min-run (default 8) or more consecutive words shared with a source text file,
                 outside quotation marks
Checks the stage .md files, rubric criteria and syllabus item titles. Source files are plain text you supply (the compiler's
extracted excerpts); nothing is fetched. Wording only: a clean report is not proof that a text is original.
"""
import json
import os
import re
import sys

from tutorlib import cli

MAX_SOURCE_BYTES = 5_000_000
QUOTE = re.compile(r'"([^"\n]{1,2000})"|“([^”\n]{1,2000})”')
WORD = re.compile(r"[\w']+")


def words(text):
    return [w.lower() for w in WORD.findall(text)]


def split_quotes(text):
    """(text with every quoted span replaced by a break marker, [quoted spans])."""
    spans = [m.group(1) or m.group(2) for m in QUOTE.finditer(text)]
    return QUOTE.sub(" \x00 ", text), spans


def source_grams(paths, n):
    grams = {}
    for p in paths:
        try:
            if os.path.getsize(p) > MAX_SOURCE_BYTES:
                raise ValueError(f"{p} is over {MAX_SOURCE_BYTES} bytes")
            with open(p, encoding="utf-8", errors="replace") as f:
                ws = words(f.read())
        except (OSError, ValueError) as e:
            return None, str(e)
        for i in range(len(ws) - n + 1):
            grams.setdefault(tuple(ws[i:i + n]), os.path.basename(p))
    return grams, None


def verbatim_runs(text, grams, n):
    """Maximal runs of consecutive words, outside quotes, whose every n-gram occurs in a source."""
    runs = []
    for seg in text.split("\x00"):
        ws = words(seg)
        hit = [tuple(ws[i:i + n]) in grams for i in range(len(ws) - n + 1)]
        i = 0
        while i < len(hit):
            if not hit[i]:
                i += 1
                continue
            j = i
            while j + 1 < len(hit) and hit[j + 1]:
                j += 1
            runs.append((j - i + n, " ".join(ws[i:i + 12]), grams[tuple(ws[i:i + n])]))
            i = j + 1
    return runs


def course_texts(course_dir):
    """Yield (stage_id or '-', location, text)."""
    stages = os.path.join(course_dir, "stages")
    if os.path.isdir(stages):
        for sid in sorted(os.listdir(stages)):
            d = os.path.join(stages, sid)
            for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
                if name.endswith(".md"):
                    with open(os.path.join(d, name), encoding="utf-8", errors="replace") as f:
                        yield sid, f"stages/{sid}/{name}", f.read()
    for fname, key in (("rubric.json", None), ("course.json", "_syllabus_items")):
        try:
            with open(os.path.join(course_dir, fname), encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            continue
        if fname == "rubric.json":
            rubrics = dict(data.get("stage_rubrics") or {})
            if isinstance(data.get("exam_rubric"), dict):
                rubrics["exam"] = data["exam_rubric"]
            for sid, entry in sorted(rubrics.items()):
                crit = entry.get("criteria") if isinstance(entry, dict) else None
                if isinstance(crit, list):
                    yield sid, f"rubric.json:{sid}", "\n".join(c for c in crit if isinstance(c, str))
        else:
            items = data.get(key) if isinstance(data, dict) else None
            if isinstance(items, list):
                yield "-", "course.json:_syllabus_items", "\n".join(str(i.get("title", "")) for i in items if isinstance(i, dict))


def check(course_dir, sources=(), min_run=8):
    if not os.path.isdir(course_dir):
        return {"error": f"FileNotFoundError: {course_dir} is not a directory"}
    grams = None
    if sources:
        grams, err = source_grams(sources, min_run)
        if err:
            return {"error": f"cannot read source: {err}"}
    findings, quotes_by_stage = [], {}
    for sid, loc, text in course_texts(course_dir):
        body, spans = split_quotes(text)
        for s in spans:
            n = len(words(s))
            if n >= 15:
                findings.append({"rule": "long_quote", "where": loc, "detail": f"{n} words: {s[:60]}"})
            if n >= 4:
                quotes_by_stage.setdefault(sid, []).append(loc)
        if grams:
            for length, excerpt, src in verbatim_runs(body, grams, min_run):
                findings.append({"rule": "verbatim_run", "where": loc, "detail": f"{length} words shared with {src}: {excerpt}"})
    for sid, locs in sorted(quotes_by_stage.items()):
        if sid != "-" and len(locs) > 1:
            findings.append({"rule": "many_quotes", "where": f"stage {sid}", "detail": f"{len(locs)} quotations of 4+ words (policy: one)"})
    by_rule = {}
    for f in findings:
        by_rule[f["rule"]] = by_rule.get(f["rule"], 0) + 1
    return {"course_dir": course_dir, "sources_checked": len(sources), "finding_count": len(findings),
            "by_rule": dict(sorted(by_rule.items())), "findings": findings}


def main(argv):
    sources, min_run, rest = [], 8, []
    i = 0
    while i < len(argv):
        if argv[i] == "--source" and i + 1 < len(argv):
            sources.append(argv[i + 1])
            i += 2
        elif argv[i] == "--min-run" and i + 1 < len(argv) and argv[i + 1].isdigit() and int(argv[i + 1]) >= 4:
            min_run = int(argv[i + 1])
            i += 2
        else:
            rest.append(argv[i])
            i += 1
    if len(rest) != 1:
        print(json.dumps({"error": "usage: paraphrase_check.py <course_dir> [--source FILE]... [--min-run N>=4]"}))
        return 2
    return cli.emit(check(rest[0], sources, min_run))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
