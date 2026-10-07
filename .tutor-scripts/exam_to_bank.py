#!/usr/bin/env python3
"""
exam_to_bank.py -- turn a course's own `exam/exam.md` ready-made items and answer key into a `question_bank.json` proposal (N-07, audit enrichment).

    python3 exam_to_bank.py <course_dir> [--write]

Only items that convert cleanly are proposed: a numbered prompt ending `[N marks]` (or a multiple-choice item keyed `Correct: X`, one mark) whose answer-key line starts `[N]` and whose scheme is either
mark points (`B1`/`M2`/`A1`/`C1` ... separated by `;`) or a levels / "mark out of N" marking guide. Everything else is listed under `skipped` with the reason (a code-output item, an
instruction to the tutor such as "Set a ... problem", a key line whose marks do not add up). Nothing is invented: prompt
and scheme text are the course's own, so `source` says so. All proposed questions get `stage_id: "exam"` because exam.md items are not tied to one stage.
Without `--write` it only prints the proposal; with it, it writes `<course_dir>/question_bank.json` and refuses to overwrite an existing one.
"""
import json
import os
import re
import sys

from tutorlib import atomic_io, cli, schema

SOURCE = "this course's own exam/exam.md (original, tutor-authored; not a board paper)"
POINT = re.compile(r"\b([MABC])(\d+)\b\s+")


def _section(text, pattern):
    m = re.search(r"(?mi)^##[^\n]*" + pattern + r"[^\n]*\n(.*?)(?=^## |\Z)", text, re.S)
    return m.group(1) if m else ""


def _numbered(block):
    """{number: text} for top-level numbered entries, continuation lines folded in."""
    out, cur = {}, None
    for line in block.splitlines():
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            cur = int(m.group(1))
            out[cur] = m.group(2)
        elif cur is not None:
            out[cur] += "\n" + line
    return out


def _scheme(key_text, marks):
    body = re.sub(r"^\[\d+\]\s*", "", key_text.strip())
    parts = [p.strip() for p in re.split(r";\s*(?=[MABC]\d+\b)", body)]
    pts = []
    for p in parts:
        m = POINT.match(p + " ")
        if not m:
            pts = []
            break
        pts.append({"id": f"{len(pts) + 1}", "marks": int(m.group(2)), "type": m.group(1), "descriptor": p[m.end():].strip() or p})
    if pts and sum(p["marks"] for p in pts) >= marks:
        return pts
    if pts:
        return None                                          # points that do not reach the marks: do not guess
    if re.search(r"(?i)\blevels?\b", body) or re.match(r"(?i)mark (out of|by)\b", body):
        return [{"id": "levels", "marks": marks, "type": "other", "descriptor": body}]
    return None


def propose(course_dir):
    path = os.path.join(course_dir, "exam", "exam.md")
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return {"error": f"FileNotFoundError: no exam/exam.md in {course_dir}"}
    items = _numbered(_section(text, r"\d+ ready-made items"))
    keys = _numbered(_section(text, "answer key"))
    qs, skipped = [], []
    for n, raw in sorted(items.items()):
        m = re.search(r"\[(\d+)\s*marks?\]\s*$", raw.strip(), re.I)
        mc = re.match(r"Correct:\s*([A-Z](?:\s*,\s*[A-Z])*)\b", (keys.get(n) or "").strip())
        if not m and mc and re.search(r"(?m)^\s+A\.\s", raw):          # multiple choice: one mark, exactly the listed options
            qs.append({"id": f"exam-{n}", "stage_id": "exam", "marks": 1, "prompt": re.sub(r"^\[[^\]]+\]\s*", "", raw.strip()),
                       "mark_scheme": [{"id": "1", "marks": 1, "type": "B", "descriptor": f"selects exactly option(s) {mc.group(1)} and no others"}],
                       "source": SOURCE})
            continue
        if raw.lstrip().startswith("```") or "\n```" in raw:
            skipped.append({"item": n, "reason": "contains a code block"})
            continue
        if re.search(r"(?i)\bset a\b|\bwrite (a|an|fresh)\b", raw[:80]):
            skipped.append({"item": n, "reason": "an instruction to the tutor, not a question"})
            continue
        if not m:
            skipped.append({"item": n, "reason": "no [N marks] on the prompt"})
            continue
        marks = int(m.group(1))
        key = keys.get(n)
        kh = re.match(r"\[(\d+)\]", (key or "").strip())
        if not key or not kh or int(kh.group(1)) != marks:
            skipped.append({"item": n, "reason": "answer key missing or its marks differ from the prompt"})
            continue
        scheme = _scheme(key, marks)
        if not scheme:
            skipped.append({"item": n, "reason": "mark scheme not in B1/M1/A1 points or levels form"})
            continue
        prompt = re.sub(r"\s*\[(\d+)\s*marks?\]\s*$", "", raw.strip(), flags=re.I)
        prompt = re.sub(r"^\[[^\]]+\]\s*", "", prompt)
        qs.append({"id": f"exam-{n}", "stage_id": "exam", "marks": marks, "prompt": prompt, "mark_scheme": scheme, "source": SOURCE})
    bank = {"schema_version": 1, "source_note": "starter bank converted from exam/exam.md; extend through the audit's enrichment pass", "questions": qs}
    errs = schema.validate(bank, "question_bank") if qs else []
    return {"proposed": len(qs), "marks": sum(q["marks"] for q in qs), "skipped": skipped, "schema_errors": errs[:3], "bank": bank if qs else None}


def main(argv):
    write = "--write" in argv
    args = [a for a in argv if a != "--write"]
    if len(args) != 1:
        print(json.dumps({"error": "usage: exam_to_bank.py <course_dir> [--write]"}))
        return 2
    r = propose(args[0])
    if "error" in r:
        return cli.emit(r)
    if write:
        dest = os.path.join(args[0], "question_bank.json")
        if os.path.exists(dest):
            return cli.emit({"error": "question_bank.json already exists; not overwritten", "written": False})
        if not r["bank"] or r["schema_errors"]:
            return cli.emit({**r, "written": False, "error": "nothing valid to write"})
        atomic_io.write_json(dest, r["bank"])
        r["written"] = True
    return cli.emit({k: v for k, v in r.items() if k != "bank"} if not write and "--show" not in argv else r)


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
