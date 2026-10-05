#!/usr/bin/env python3
"""
worksheet_check.py -- does a take-home worksheet give away the stage test? (K-26, A-07) Read-only.

    python3 worksheet_check.py <stage test.md> <<'EOF'
    ...the worksheet text, with its answer key...
    EOF

Exit 0 and {"ok": true} when no graded test item appears word for word in the worksheet; exit 1 and the offending item
numbers when one does (rewrite those worksheet questions with different numbers or a different context, then check again).
`similar_runs` counts shared 20-word runs and is advisory. The worksheet is read from stdin so course-derived text never travels
on a command line.
"""
import json
import sys

from tutorlib import cli, overlap


def check(test_md_path, worksheet_text):
    try:
        with open(test_md_path, encoding="utf-8") as f:
            test_text = f.read()
    except OSError as e:
        return {"error": f"FileNotFoundError: cannot read {test_md_path}: {e.strerror}"}
    items = overlap.test_items(test_text)
    if not items:
        return {"ok": True, "test_items_found": 0, "copied_items": [], "similar_runs": 0,
                "note": "no graded items could be read from test.md, so nothing was compared"}
    hay = overlap.norm(worksheet_text)
    copied = [i + 1 for i, it in enumerate(items) if it in hay]
    runs = overlap.long_runs(" ".join(items), worksheet_text)
    out = {"ok": not copied, "test_items_found": len(items), "copied_items": copied, "similar_runs": runs}
    if copied:
        out["error"] = f"worksheet reproduces test item(s) {copied}: rewrite those questions with different values or context"
    return out


def main(argv):
    if len(argv) != 1:
        print(json.dumps({"error": "usage: worksheet_check.py <stage test.md>  (worksheet text on stdin)"}))
        return 2
    return cli.emit(check(argv[0], sys.stdin.read()))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
