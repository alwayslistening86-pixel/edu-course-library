"""A-11: rubric wording lint (advisory)."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import postcompile_gate  # noqa: E402
import rubric_lint  # noqa: E402

GOOD = {"criteria": ["Finds a percentage of an amount using a clearly shown method", "Applies a percentage change using a single multiplier"],
        "pass_threshold": "Correct on percentage of an amount and percentage change questions.",
        "source": {"issuing_body": "Board", "document": "Specification section 2", "urls": ["https://example.org/spec"]}}


def rules(entry):
    return sorted({f["rule"] for f in rubric_lint.lint_stage("S1", entry)})


class Lint(unittest.TestCase):
    def test_a_good_entry_is_clean(self):
        self.assertEqual(rubric_lint.lint_stage("S1", GOOD), [])

    def test_each_rule(self):
        self.assertIn("few_criteria", rules({**GOOD, "criteria": ["Finds a percentage of an amount using a clearly shown method"]}))
        self.assertIn("many_criteria", rules({**GOOD, "criteria": [f"Performs distinct skill number {i} correctly every time" for i in range(9)]}))
        self.assertIn("vague_criterion", rules({**GOOD, "criteria": GOOD["criteria"] + ["Has a good understanding of percentages in general"]}))
        self.assertIn("duplicate_criterion", rules({**GOOD, "criteria": GOOD["criteria"] + [GOOD["criteria"][0].upper()]}))
        self.assertIn("no_pass_threshold", rules({**GOOD, "pass_threshold": "pass"}))
        self.assertIn("no_source_locator", rules({**GOOD, "source": {"issuing_body": "Board"}}))

    def test_label_only_stage(self):
        r = rules({**GOOD, "criteria": ["3.1.1: Monomers and polymers", "3.1.2: Carbohydrates"]})
        self.assertIn("label_only_stage", r)
        self.assertIn("short_criterion", r)
        self.assertNotIn("label_only_stage", rules({**GOOD, "criteria": GOOD["criteria"] + ["WACC"]}))          # one label among real criteria is not the same

    def test_course_level_and_gate_note(self):
        tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        fx = gs.build_fixture(tmp)
        path = f"{fx['C']}/mathA/rubric.json"
        rub = gs.read_json(path)
        for sid in rub["stage_rubrics"]:
            rub["stage_rubrics"][sid]["criteria"] = list(GOOD["criteria"])
        rub["stage_rubrics"]["S1"]["criteria"] = ["3.1.1: Topic", "3.1.2: Topic two"]
        with open(path, "w") as f:
            json.dump(rub, f)
        out = rubric_lint.lint(f"{fx['C']}/mathA")
        self.assertEqual(out["by_rule"].get("label_only_stage"), 1)
        gate = postcompile_gate._gate(f"{fx['C']}/mathA")
        self.assertTrue(gate["can_ship"])                                              # advisory only
        self.assertTrue(any("only topic-label criteria" in n for n in gate["advisory_notes"]))
        self.assertIn("error", rubric_lint.lint(tmp + "/missing"))


if __name__ == "__main__":
    unittest.main()
