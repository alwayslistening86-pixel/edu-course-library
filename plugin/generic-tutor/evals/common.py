"""Helpers shared by eval suites."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(HERE)


def read_plugin(*parts):
    with open(os.path.join(PLUGIN, *parts), encoding="utf-8") as f:
        return f.read()


def section(text, start_pattern, end_pattern=None):
    """Return the text from `start_pattern` up to (not including) `end_pattern` (regex), or "" if not found."""
    m = re.search(start_pattern + (r".*?(?=" + end_pattern + ")" if end_pattern else r".*"), text, re.S)
    return m.group(0) if m else ""


def parse_json_object(text, allowed_key, allowed_values):
    """First {...} in a reply whose `allowed_key` holds one of `allowed_values`; else None."""
    for m in re.finditer(r"\{.*?\}", text, re.S):
        try:
            d = json.loads(m.group(0))
        except ValueError:
            continue
        if d.get(allowed_key) in allowed_values:
            return d
    return None


def fixture_courses_dir():
    """The self-authored sample courses (A-02): a library any suite can point the real scripts at, with no private content."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "courses")
