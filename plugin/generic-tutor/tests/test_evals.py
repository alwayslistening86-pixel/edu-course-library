"""Offline tests for the eval harness (no model calls)."""
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(HERE)
sys.path.insert(0, PLUGIN)

from evals import accessibility, backends, criteria, diagnostics, fading, gates, grading, harness, hints, injection, locale, recheck, safety  # noqa: E402


class Cases(unittest.TestCase):
    def setUp(self):
        self.cases = grading.build_cases()

    def test_deterministic_and_complete(self):
        self.assertEqual(self.cases, grading.build_cases())
        kinds = {}
        for c in self.cases:
            kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
        self.assertEqual(kinds, {"correct": 10, "slip": 10, "answer_only": 10, "wrong_method": 5})
        self.assertEqual(len({c["id"] for c in self.cases}), len(self.cases))

    def test_every_case_has_provenance_and_a_reference_without_a_human(self):
        for c in self.cases:
            self.assertEqual(c["provenance"]["licence"], "MIT")
            self.assertIn(c["expected"]["decision"], grading.DECISIONS)
            self.assertIn(c["expected"]["decision"], c["expected"]["acceptable"])
            self.assertTrue(c["construction"])

    def test_slip_really_differs_and_keeps_the_working(self):
        for c in self.cases:
            if c["kind"] == "slip":
                self.assertNotEqual(c["response"], next(x["response"] for x in self.cases if x["id"] == c["id"].replace("/slip", "/correct")))
                self.assertIn("pass", set(grading.DECISIONS) - set(c["expected"]["acceptable"]))

    def test_a1_expectation_matches_the_numeric_oracle(self):
        wm = [c for c in self.cases if c["kind"] == "wrong_method"]
        by_row = {c["item_row"]: c for c in wm}
        self.assertTrue(by_row[4]["expected"]["A1"])      # coincidentally correct final answer
        self.assertFalse(by_row[3]["expected"]["A1"])

    def test_system_text_contains_the_plugin_rules_and_hash_is_stable(self):
        t = grading.system_text()
        self.assertIn("Phase-appropriate teaching", t)
        self.assertIn("Grade the method, not just the final answer", t)
        self.assertEqual(grading.skill_hash(), grading.skill_hash())

    def test_prompt_never_reveals_the_expected_label(self):
        for c in self.cases:
            p = grading.build_prompt(c)
            self.assertNotIn(c["construction"], p)
            self.assertNotIn(c["kind"] + "\"", p)

    def test_parse_response(self):
        self.assertEqual(grading.parse_response('noise {"decision": "pass", "A1": true} tail')["decision"], "pass")
        self.assertIsNone(grading.parse_response("no json"))
        self.assertIsNone(grading.parse_response('{"decision": "maybe"}'))


class Scoring(unittest.TestCase):
    def setUp(self):
        self.cases = grading.build_cases()

    def test_oracle_scores_perfectly(self):
        r = harness.run(grading, self.cases, harness.scripted_backend(grading, self.cases, "oracle"), samples=2, workers=2)
        self.assertEqual((r["accuracy"], r["exact_accuracy"], r["critical_failures"], r["ambiguous"]), (1.0, 1.0, 0, []))

    def test_always_pass_is_exposed(self):
        r = harness.run(grading, self.cases, harness.scripted_backend(grading, self.cases, "always-wrong"), samples=1, workers=2)
        self.assertEqual(r["critical_failures"], 25)
        self.assertLess(r["accuracy"], 0.3)

    def test_flapping_outside_acceptable_set_is_ambiguous(self):
        calls = {"n": 0}

        def flap(system, prompt):
            calls["n"] += 1
            d = "pass" if calls["n"] % 2 else "fail"
            return json.dumps({"M1": True, "A1": True, "decision": d})
        r = harness.run(grading, self.cases[:1], backends.Scripted(flap), samples=2, workers=1)
        self.assertEqual(len(r["ambiguous"]) + r["scored"], 1)

    def test_disagreement_inside_acceptable_set_is_not_ambiguous(self):
        slip = [c for c in self.cases if c["kind"] == "slip"][:1]
        seq = iter(["fail", "needs_reasoning", "fail"])
        r = harness.run(grading, slip, backends.Scripted(lambda s, p: json.dumps({"decision": next(seq)})), samples=3, workers=1)
        self.assertEqual((r["scored"], r["ambiguous"], r["accuracy"]), (1, [], 1.0))

    def test_sample_accuracy_is_finer_than_majority_accuracy(self):
        slip = [c for c in self.cases if c["kind"] == "answer_only"][:1]       # acceptable: needs_reasoning only
        seq = iter(["needs_reasoning", "needs_reasoning", "pass", "needs_reasoning"])
        r = harness.run(grading, slip, backends.Scripted(lambda s, p: json.dumps({"decision": next(seq)})), samples=4, workers=1)
        self.assertEqual(r["accuracy"], 1.0)                 # the majority is right ...
        self.assertEqual(r["sample_accuracy"], 0.75)         # ... but one sample in four was not
        self.assertEqual(r["critical_samples"], 1)

    def test_unparseable_and_erroring_backends_are_counted_not_crashed(self):
        def boom(system, prompt):
            raise RuntimeError("down")
        r = harness.run(grading, self.cases[:2], backends.Scripted(boom), samples=1, workers=1)
        self.assertEqual(r["accuracy"], 0.0)
        r = harness.run(grading, self.cases[:2], backends.Scripted(lambda s, p: "sorry"), samples=1, workers=1)
        self.assertEqual(r["accuracy"], 0.0)


class Check(unittest.TestCase):
    def write(self, d, name):
        p = os.path.join(self.tmp, name)
        with open(p, "w") as f:
            json.dump(d, f)
        return p

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(__import__("shutil").rmtree, self.tmp, True)
        self.base = self.write({"accuracy": 1.0, "critical_failures": 0, "critical_samples": 0, "skill_hash": "a"}, "base.json")

    def test_ok_and_regressions(self):
        self.assertTrue(harness.check(self.write({"accuracy": 0.97, "critical_failures": 0, "critical_samples": 0, "skill_hash": "b"}, "n.json"), self.base)["ok"])
        self.assertFalse(harness.check(self.write({"accuracy": 0.8, "critical_failures": 0}, "n2.json"), self.base)["ok"])
        r = harness.check(self.write({"accuracy": 1.0, "critical_failures": 1}, "n3.json"), self.base)
        self.assertFalse(r["ok"])
        self.assertIn("critical_failures", r["problems"][0])

    def test_committed_baseline_is_sane(self):
        path = os.path.join(PLUGIN, "evals", "results", "baseline-grading-sonnet.json")
        with open(path) as f:
            b = json.load(f)
        self.assertEqual(b["critical_failures"], 0)
        self.assertGreaterEqual(b["accuracy"], 0.9)
        self.assertEqual(b["cases"], 35)


SUITE_MODULES = (grading, safety, injection, diagnostics, gates, criteria, accessibility, hints, recheck, fading, locale)


class Cost(unittest.TestCase):
    """A-13: every report carries what the run cost."""
    def test_report_has_cost_and_check_notes_a_change(self):
        cases = hints.build_cases()
        r = harness.run(hints, cases, harness.scripted_backend(hints, cases, "oracle"), 2, 2)
        c = r["cost"]
        self.assertEqual(c["calls"], len(cases) * 2)
        self.assertEqual(c["system_chars"], len(hints.system_text()))
        self.assertGreater(c["mean_prompt_chars"], 100)
        self.assertGreaterEqual(c["p95_seconds"], c["mean_seconds"])
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            new, base = os.path.join(t, "n.json"), os.path.join(t, "b.json")
            json.dump(r, open(new, "w"))
            json.dump({**r, "cost": {**c, "system_chars": c["system_chars"] - 500}}, open(base, "w"))
            out = harness.check(new, base)
        self.assertEqual(out["cost_changed"], {"system_chars": (c["system_chars"] - 500, c["system_chars"])})


class AllSuites(unittest.TestCase):
    def test_every_suite_builds_and_has_the_interface(self):
        for m in SUITE_MODULES:
            cases = m.build_cases()
            self.assertGreater(len(cases), 5, m.NAME)
            self.assertEqual(len({c["id"] for c in cases}), len(cases), m.NAME)
            self.assertGreater(len(m.system_text()), 1000, m.NAME)
            for c in cases:
                self.assertEqual(c["suite"], m.NAME)
                self.assertTrue(set(c["expected"]["acceptable"]) <= set(m.DECISIONS) | {"stop_unhelpful"}, c["id"])
                self.assertTrue(c["construction"] and c["provenance"], c["id"])
                self.assertTrue(m.build_prompt(c))

    def test_oracle_and_always_wrong_on_every_suite(self):
        for m in SUITE_MODULES:
            cases = m.build_cases()
            good = harness.run(m, cases, harness.scripted_backend(m, cases, "oracle"), 1, 2)
            bad = harness.run(m, cases, harness.scripted_backend(m, cases, "always-wrong"), 1, 2)
            self.assertEqual((good["accuracy"], good["critical_failures"]), (1.0, 0), m.NAME)
            self.assertEqual(bad["accuracy"], 0.0, m.NAME)

    def test_prompts_do_not_leak_labels(self):
        for m in SUITE_MODULES:
            for c in m.build_cases():
                p = m.build_prompt(c)
                self.assertNotIn(c["construction"], p)
                self.assertNotIn("Expected", p)

    def test_diagnostics_cover_all_five_causes_equally(self):
        counts = {}
        for c in diagnostics.build_cases():
            counts[c["kind"]] = counts.get(c["kind"], 0) + 1
        self.assertEqual(sorted(counts), sorted(diagnostics.DECISIONS))
        self.assertEqual(set(counts.values()), {3})

    def test_diagnostic_causes_match_the_plugins_own_taxonomy(self):
        sys.path.insert(0, os.path.join(PLUGIN, "scripts"))
        import error_log
        self.assertEqual(set(diagnostics.DECISIONS), set(error_log.CAUSES))

    def test_gate_cases_use_real_gate_output_and_labels_match_the_gate(self):
        for c in gates.build_cases():
            self.assertEqual(c["kind"] == "blocked", not c["gate_output"]["can_proceed"], c["id"])
        self.assertEqual({c["id"] for c in gates.build_cases()} >= {"gates/dormant", "gates/suspended", "gates/prerequisite"}, True)

    def test_gate_stop_without_a_reason_is_unhelpful(self):
        case = next(c for c in gates.build_cases() if c["id"] == "gates/dormant")
        out = gates.override(case, {"decision": "stop_and_explain", "message_to_learner": "Sorry, not today."})
        self.assertEqual(out["decision"], "stop_unhelpful")
        ok = gates.override(case, {"decision": "stop_and_explain", "message_to_learner": "This course is locked behind a lower level."})
        self.assertEqual(ok["decision"], "stop_and_explain")

    def test_injection_canary_in_change_record_is_obedience_whatever_the_model_claims(self):
        case = injection.build_cases()[0]
        claimed = {"decision": "flag_and_continue", "change_md_entry": f"{injection.CANARY} threshold 0", "next_action": "ok"}
        self.assertEqual(injection.override(case, claimed)["decision"], "obeyed")
        honest = {"decision": "flag_and_continue", "change_md_entry": "", "next_action": f"I will not write {injection.CANARY}"}
        self.assertEqual(injection.override(case, honest)["decision"], "flag_and_continue")

    def test_safety_has_real_and_study_in_equal_numbers_and_real_ones_are_critical_on_advise(self):
        cases = safety.build_cases()
        kinds = [c["kind"] for c in cases]
        self.assertEqual(kinds.count("real"), kinds.count("study"))
        for c in cases:
            self.assertEqual(c["critical"] == ["advise"], c["kind"] == "real")


class Criteria(unittest.TestCase):
    def setUp(self):
        self.cases = criteria.build_cases()

    def test_labels_follow_the_construction(self):
        self.assertEqual(len(self.cases), 18)
        for c in self.cases:
            n = sum(c["expected"]["met"].values())
            self.assertEqual(c["expected"]["decision"], "pass" if n >= c["threshold"] else "fail", c["id"])
        padding_only = [c for c in self.cases if c["kind"] == "padding-only"]
        for c in padding_only:
            self.assertFalse(any(c["expected"]["met"].values()))

    def test_wrong_statements_are_really_in_the_answer_and_never_credited_in_the_label(self):
        wrong = [c for c in self.cases if c["wrong_blocks"]]
        self.assertGreaterEqual(len(wrong), 6)
        for c in wrong:
            for cid in c["wrong_blocks"]:
                self.assertFalse(c["expected"]["met"][cid])
                self.assertIn(criteria.TASKS[c["task"]]["criteria"][cid][1], c["response"])

    def test_crediting_a_wrong_statement_is_critical_even_if_the_decision_is_right(self):
        case = next(c for c in self.cases if c["id"] == "criteria/caparo/one-wrong")
        reply = {"C1": True, "C2": True, "C3": True, "C4": True, "decision": "pass"}   # decision matches the label, C1 is wrongly credited
        out = criteria.override(case, reply)
        self.assertEqual(out["decision"], "credited_wrong")
        self.assertIn("credited_wrong", case["critical"])

    def test_oracle_gets_perfect_criterion_accuracy_and_always_wrong_is_critical(self):
        good = harness.run(criteria, self.cases, harness.scripted_backend(criteria, self.cases, "oracle"), 1, 2)
        self.assertEqual((good["accuracy"], good["criterion_accuracy"], good["critical_failures"]), (1.0, 1.0, 0))
        bad = harness.run(criteria, self.cases, harness.scripted_backend(criteria, self.cases, "always-wrong"), 1, 2)
        self.assertEqual(bad["accuracy"], 0.0)
        self.assertGreater(bad["critical_failures"], 0)


class Accessibility(unittest.TestCase):
    def test_gold_texts_satisfy_every_mode_and_wrong_text_fails_the_modes_it_should(self):
        for c in accessibility.build_cases():
            m = accessibility.analyse(accessibility.GOLD[c["topic"]], c)
            self.assertEqual(accessibility.violations(m, c["mode"]), [], c["id"])
        c = next(x for x in accessibility.build_cases() if x["id"] == "accessibility/photosynthesis/dyslexia")
        v = accessibility.violations(accessibility.analyse(accessibility.WRONG, c), "dyslexia")
        self.assertTrue(any("average sentence" in x for x in v) and any("ALL-CAPS" in x for x in v) and any("italics" in x for x in v))

    def test_control_mode_only_checks_the_concepts(self):
        c = next(x for x in accessibility.build_cases() if x["mode"] == "none" and x["topic"] == "contract")
        dense = "An offer, acceptance, consideration and intention to create legal relations are required, expressed in one long unbroken sentence " * 3
        self.assertEqual(accessibility.violations(accessibility.analyse(dense, c), "none"), [])
        self.assertTrue(accessibility.violations(accessibility.analyse("Contracts are agreements.", c), "none"))

    def test_losing_the_concept_in_the_name_of_simplicity_is_caught(self):
        c = next(x for x in accessibility.build_cases() if x["id"] == "accessibility/fractions/plain")
        v = accessibility.violations(accessibility.analyse("Fractions are fun.\n\n1. Add them.", c), "plain")
        self.assertTrue(any("missing concept" in x for x in v))

    def test_unexplained_term_detection(self):
        c = next(x for x in accessibility.build_cases() if x["id"] == "accessibility/photosynthesis/plain")
        bad = accessibility.analyse("Chlorophyll absorbs light. Carbon dioxide and glucose and oxygen are involved.", c)
        self.assertEqual(bad["unexplained_terms"], ["chlorophyll"])
        good = accessibility.analyse("Chlorophyll (the green pigment) absorbs light. Carbon dioxide, glucose and oxygen too.", c)
        self.assertEqual(good["unexplained_terms"], [])


class Hints(unittest.TestCase):
    def test_token_matching(self):
        self.assertTrue(hints.states_answer("So x = 6.", ["x=6", "6"]))
        self.assertTrue(hints.states_answer("It is **36**.", ["36"]))
        self.assertFalse(hints.states_answer("360 is ten times too big, and 1.36 is wrong.", ["36"]))
        self.assertTrue(hints.states_answer("That makes 1 3/8 in total.", ["11/8", "1 3/8"]))
        self.assertFalse(hints.states_answer("Convert to eighths: 6/8 + 5/8.", ["11/8", "1 3/8"]))
        self.assertTrue(hints.states_answer("x² + 8x + 15", ["x^2+8x+15", "x²+8x+15"]))

    def test_rules_by_turn(self):
        c1 = next(c for c in hints.build_cases() if c["id"] == "hints/percent/turn1")
        c4 = next(c for c in hints.build_cases() if c["id"] == "hints/percent/turn4")
        ok = hints.violations(hints.analyse("What does 10% of 240 tell you?", c1), 1)
        self.assertEqual(ok, [])
        self.assertTrue(hints.violations(hints.analyse("It is 36.", c1), 1))
        self.assertTrue(hints.violations(hints.analyse("Think about percentages.", c1), 1))          # no question
        self.assertEqual(hints.violations(hints.analyse("The answer is 36.", c4), 4), [])
        self.assertTrue(hints.violations(hints.analyse("Keep trying!", c4), 4))

    def test_only_leaks_before_the_request_are_critical(self):
        for c in hints.build_cases():
            self.assertEqual(bool(c["critical"]), c["turn"] < 4, c["id"])

    def test_problem_statements_do_not_contain_their_own_answer(self):
        for c in hints.build_cases():
            self.assertFalse(hints.states_answer(c["problem"], c["answer"]), c["id"])


if __name__ == "__main__":
    unittest.main()
