#!/usr/bin/env python3
"""
dashboard_html.py -- a self-contained progress page for one learner (U-03, U-01).

    python3 dashboard_html.py <learner_dir> <courses_dir> <output.html> [--today YYYY-MM-DD]

Writes ONE static HTML file: no JavaScript, no network requests, no external fonts or images, light/dark aware, readable at phone
width. It shows, from the same scripts the tutor itself uses (status.py, readiness.py): per-course stage progress, reviews due,
the readiness band with its evidence and caveats (never a grade), the weakest items, unresolved errors by cause, recent mock
papers (percentages), and the suggested next step. Every learner-derived string is HTML-escaped.

The page contains personal data about the learner: it is written where you tell it (refused if inside the learner's own folder, so
`/erase` and backups never get confused), and `/erase` does not delete it. Read-only with respect to all tutor state.
"""
import datetime
import html
import json
import os
import sys

import readiness
import status
from cohort_status import LIVE_STATES
from tutorlib import atomic_io, cli, paths

BAND_TEXT = {"not_enough_evidence": "Not enough evidence yet", "early": "Early", "building": "Building", "solid": "Solid"}

CSS = """
:root{--bg:#fff;--fg:#1b1f23;--muted:#586069;--card:#f6f8fa;--line:#d0d7de;--bar:#2f6feb;--barbg:#e6ebf1;--warn:#9a6700}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--muted:#9da7b3;--card:#161b22;--line:#30363d;--bar:#58a6ff;--barbg:#21262d;--warn:#d29922}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:16px}h1{font-size:1.5rem;margin:.2rem 0}h2{font-size:1.15rem;margin:0 0 .5rem}
.sub{color:var(--muted);margin:0 0 1rem}.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;margin:0 0 14px}
.bar{height:12px;background:var(--barbg);border-radius:6px;overflow:hidden;margin:.3rem 0}.bar>span{display:block;height:100%;background:var(--bar)}
table{border-collapse:collapse;width:100%}th,td{text-align:left;padding:4px 8px;border-bottom:1px solid var(--line);vertical-align:top}
.k{color:var(--muted)}.caveat{color:var(--warn);font-size:.92rem}ul{margin:.3rem 0 0 1.1rem;padding:0}
"""


def e(x):
    return html.escape("" if x is None else str(x), quote=True)


def bar(done, total):
    pct = 0 if not total else round(100 * done / total)
    return f'<div class="bar" role="img" aria-label="{e(done)} of {e(total)} stages passed"><span style="width:{pct}%"></span></div>'


def build(learner_dir, courses_dir, today=None):
    st = status.build(learner_dir, courses_dir)
    if "error" in st:
        return None, st["error"]
    parts = [f"<h1>Progress: {e(st['learner'])}</h1>",
             f'<p class="sub">Session {e(st["session_slot"])} · roster {e(st["roster"]["occupancy"])} of {e(st["roster"]["max"])} course slots'
             + (f" · generated {e(today)}" if today else "") + "</p>"]
    nxt = st["next_action"]
    parts.append(f'<section class="card"><h2>Next step</h2><p><strong>{e(nxt["command"])}</strong> <span class="k">— {e(nxt["reason"])}</span></p>'
                 f'<p class="k">Reviews due: {e(st["due_reviews_total"])}</p></section>')
    for c in st["courses"]:
        cid = c["course_id"]
        parts.append(f'<section class="card"><h2>{e(c["name"] or cid)}</h2>'
                     f'<p class="k">{e(c["roster_state"])}{" · standalone" if c["standalone"] else (" · level " + e(c["level"]) if c["level"] is not None else "")}'
                     f'{" · complete" if c["complete"] else ""}{" (theory-only)" if c["theory_only"] else ""}</p>'
                     f'{bar(c["stages_passed"], c["stages_total"])}<p>{e(c["stages_passed"])} of {e(c["stages_total"])} stages passed'
                     f'{"; now at " + e(c["current_stage"]) + " (" + e(c["current_phase"]) + ")" if not c["complete"] and c["current_stage"] else ""}.</p>')
        if c["coverage_status"] and c["coverage_status"] != "full":
            parts.append(f'<p class="caveat">This course does not yet cover the whole specification (coverage: {e(c["coverage_status"])}).</p>')
        if c["roster_state"] in LIVE_STATES and not c["complete"]:
            r = readiness.assess(learner_dir, courses_dir, cid)
            if "error" not in r:
                ev = r["evidence"]
                parts.append(f'<h3 style="font-size:1rem;margin:.6rem 0 .2rem">Readiness: {e(BAND_TEXT.get(r["band"], r["band"]))}</h3>'
                             f'<p class="k">Evidence strength: {e(r["strength"])} · {e(ev["items_observed"])} of {e(ev["items_taught_listed"])} taught items observed'
                             + (f" · mean mastery {e(ev['mean_observed_mastery'])}" if ev["mean_observed_mastery"] is not None else "") + "</p>")
                if r["weakest_items"]:
                    parts.append("<p>Weakest items:</p><ul>" + "".join(f"<li>{e(w['item_id'])} <span class='k'>(mastery {e(w['p_mastery'])})</span></li>" for w in r["weakest_items"]) + "</ul>")
                if ev["recent_mocks"]:
                    parts.append("<table><tr><th>Mock paper</th><th>Marks</th><th>Minutes</th></tr>" + "".join(
                        f"<tr><td>{e(m['date'])}</td><td>{e(m['percent'])}%</td><td>{e(m['minutes'])}</td></tr>" for m in ev["recent_mocks"]) + "</table>")
                parts.append("<ul>" + "".join(f'<li class="caveat">{e(x)}</li>' for x in r["caveats"]) + "</ul>")
        parts.append("</section>")
    causes = {}
    sdir = os.path.join(learner_dir, "subjects")
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if fn.endswith(".json") and not fn.endswith("_review_deck.json"):
            try:
                with open(os.path.join(sdir, fn), encoding="utf-8") as f:
                    for er in json.load(f).get("error_patterns", []):
                        if isinstance(er, dict) and not er.get("resolved"):
                            causes[er.get("cause", "unknown")] = causes.get(er.get("cause", "unknown"), 0) + 1
            except (OSError, ValueError):
                pass
    if causes:
        top = max(causes.values())
        parts.append('<section class="card"><h2>Unresolved mistakes by cause</h2><table>' + "".join(
            f'<tr><td>{e(k)}</td><td style="width:60%"><div class="bar"><span style="width:{round(100 * v / top)}%"></span></div></td><td>{e(v)}</td></tr>'
            for k, v in sorted(causes.items(), key=lambda kv: (-kv[1], kv[0]))) + "</table></section>")
    parts.append('<p class="k">This page is a summary of practice evidence, not a grade or a prediction. It contains personal data — keep it private.</p>')
    doc = ("<!doctype html><html lang=\"en-GB\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
           f"<title>Progress: {e(st['learner'])}</title><style>{CSS}</style></head><body><main>" + "\n".join(parts) + "</main></body></html>\n")
    return doc, None


def main(argv):
    args, today = list(argv), None
    if "--today" in args:
        i = args.index("--today")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--today needs a date"}))
            return 2
        today = args[i + 1]
        del args[i:i + 2]
    if len(args) != 3:
        print(json.dumps({"error": "usage: dashboard_html.py <learner_dir> <courses_dir> <output.html> [--today YYYY-MM-DD]"}))
        return 2
    learner_dir, courses_dir, out = args
    try:
        paths.ensure_within(os.path.dirname(os.path.abspath(out)), out)
        real_out, real_l = os.path.realpath(out), os.path.realpath(learner_dir)
        if real_out.startswith(real_l + os.sep):
            return cli.emit({"error": "output must be outside the learner's folder"})
        if today:
            datetime.date.fromisoformat(today)
    except ValueError as ex:
        return cli.emit({"error": str(ex)})
    doc, err = build(learner_dir, courses_dir, today)
    if err:
        return cli.emit({"error": err})
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tmp = out + ".part"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(doc)
    atomic_io.replace(tmp, out)
    return cli.emit({"written": True, "output": out, "bytes": len(doc.encode("utf-8"))})


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
