"""N-13: the shipped course template stays a skeleton that, once filled, passes every course gate."""
import json
import os
import re
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import coverage_check  # noqa: E402
import postcompile_gate  # noqa: E402
import validate_schema  # noqa: E402
import validate_structure  # noqa: E402

TEMPLATE = os.path.join(ROOT, "_template")
PLACEHOLDER = re.compile(r"\{\{.*?\}\}", re.S)
_n = [0]


def fill_text(text):
    """Every placeholder becomes distinct words, as real content would be (identical lines in lesson and test would trip the gate's overlap check)."""
    def one(_):
        _n[0] += 1
        return f"filled content number {_n[0]} written for the template check"
    return PLACEHOLDER.sub(one, text)


def fill(o):
    if isinstance(o, dict):
        return {k: fill(v) for k, v in o.items()}
    if isinstance(o, list):
        return [fill(v) for v in o]
    return fill_text(o) if isinstance(o, str) else o


def rw(path, edit):
    with open(path, encoding="utf-8") as f:
        data = edit(json.load(f))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def filled_copy(dest):
    """What a compiler does: copy the template, replace every placeholder, add the stages and items the ladder names."""
    d = os.path.join(dest, "tpl")
    shutil.copytree(TEMPLATE, d, ignore=shutil.ignore_patterns("optional"))

    def course(c):
        c = fill(c)
        c.update(currency="live", level_basis="declared", academic_level=2, framework=None)
        c.pop("selected_options", None)
        return c
    rw(os.path.join(d, "course.json"), course)

    def cmap(m):
        m = fill(m)
        m["_items_source"]["url"] = "https://example.org/spec"
        m["_syllabus_items"] = [{"id": f"T{i}", "title": f"Item {i}", "topic_area": "A"} for i in (1, 2, 3)]
        m["_declared_exclusions"] = []
        for i, s in enumerate(("S1", "S2", "S3"), 1):
            m[s]["covers_items"] = [f"T{i}"]
        return m
    rw(os.path.join(d, "curriculum_map.json"), cmap)

    def rubric(r):
        r = fill(r)
        for e in list(r["stage_rubrics"].values()) + [r["exam_rubric"]]:
            e["source"]["reference"] = "https://example.org/spec"
        return r
    rw(os.path.join(d, "rubric.json"), rubric)
    exam = os.path.join(d, "exam", "exam.md")
    with open(exam, encoding="utf-8") as f:
        text = fill_text(f.read())
    with open(exam, "w", encoding="utf-8") as f:
        f.write(text)
    for s in ("S2", "S3"):
        shutil.copytree(os.path.join(d, "stages", "S1"), os.path.join(d, "stages", s))
    for i, s in enumerate(("S1", "S2", "S3"), 1):
        sd = os.path.join(d, "stages", s)
        for n in ("lesson.md", "practice.md", "test.md"):
            with open(os.path.join(sd, n), encoding="utf-8") as f:
                text = fill_text(f.read())
            with open(os.path.join(sd, n), "w", encoding="utf-8") as f:
                f.write(text + (f"\n- T{i}: covered\n" if n == "lesson.md" else ""))
        rw(os.path.join(sd, "misconceptions.json"), fill)
    return d


class Template(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.addCleanup(self._t.cleanup)

    def test_a_filled_template_passes_every_gate(self):
        d = filled_copy(self._t.name)
        self.assertTrue(validate_structure.validate(d)["clean"], validate_structure.validate(d))
        self.assertEqual(validate_schema.check_course_dir(d)["invalid"], [])
        self.assertEqual(coverage_check.check(d)["computed_status"], "full")
        gate = postcompile_gate.check(d)
        self.assertTrue(gate["can_ship"], gate["blocking_reasons"])

    def test_an_unfilled_template_cannot_ship(self):
        d = os.path.join(self._t.name, "raw")
        shutil.copytree(TEMPLATE, d, ignore=shutil.ignore_patterns("optional"))
        gate = postcompile_gate.check(d)
        self.assertFalse(gate["can_ship"])
        self.assertTrue(any("unfilled template placeholders" in r for r in gate["blocking_reasons"]), gate["blocking_reasons"])

    def test_one_leftover_placeholder_blocks_a_filled_course(self):
        d = filled_copy(self._t.name)
        with open(os.path.join(d, "stages", "S2", "lesson.md"), "a", encoding="utf-8") as f:
            f.write("\nNext: {{NEXT_STAGE_TOPICS_TO_AVOID}}\n")
        reasons = postcompile_gate.check(d)["blocking_reasons"]
        self.assertTrue(any("stages/S2/lesson.md" in r for r in reasons), reasons)

    def test_maths_braces_are_not_placeholders(self):
        d = filled_copy(self._t.name)
        with open(os.path.join(d, "stages", "S1", "lesson.md"), "a", encoding="utf-8") as f:
            f.write("\nWrite x^{{2}} and {{n}} and \\frac{{a}}{{b}} as code, not as template text.\n")
        self.assertTrue(postcompile_gate.check(d)["can_ship"])

    def test_option_lists_are_placeholders_not_invalid_values(self):
        with open(os.path.join(TEMPLATE, "course.json"), encoding="utf-8") as f:
            c = json.load(f)
        for key in ("currency", "level_basis"):
            self.assertTrue(c[key].startswith("{{"), f"{key} must be a placeholder so a leftover is caught")

    def test_optional_layers_are_stubs_outside_the_course_root(self):
        opt = os.path.join(TEMPLATE, "optional")
        self.assertTrue(os.path.isfile(os.path.join(opt, "exam_technique.md")))
        with open(os.path.join(opt, "command_words.json"), encoding="utf-8") as f:
            self.assertIn("command_words", json.load(f))
        self.assertFalse(os.path.exists(os.path.join(TEMPLATE, "exam_technique.md")), "a stub at the root would block every course")


if __name__ == "__main__":
    unittest.main()
