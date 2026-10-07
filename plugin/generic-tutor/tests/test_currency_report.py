"""N-10: the currency report reads snapshots and says what needs a look."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import currency_report as cr  # noqa: E402
import postcompile_gate  # noqa: E402
import verify_sources as vs  # noqa: E402


class Report(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def course(self, cid, snaps=None, recheck="2026-10-01"):
        d = os.path.join(self.tmp, cid)
        os.makedirs(d)
        with open(os.path.join(d, "course.json"), "w") as f:
            json.dump({"stage_ladder": [], "last_live_recheck": recheck}, f)
        if snaps is not None:
            with open(os.path.join(d, vs.SNAP), "w") as f:
                json.dump({"schema_version": 1, "snapshots": snaps}, f)
        return d

    def run_(self, **kw):
        return cr.run(self.tmp, "2026-10-07", **kw)

    def test_flags_and_ordering(self):
        ok = {"status": "ok", "checked_on": "2026-10-05", "sha256": "a" * 64}
        self.course("fine", {"u": ok})
        self.course("dead", {"u": {**ok, "status": "dead"}})
        self.course("changed", {"u": {**ok, "changed": True}})
        self.course("never")
        self.course("old", {"u": {**ok, "checked_on": "2026-01-01"}})
        self.course("blocked", {"u": {"status": "blocked", "checked_on": "2026-10-05"}})
        r = self.run_()
        self.assertEqual([x["course_id"] for x in r["courses"]], ["dead", "changed", "never", "old", "blocked"])
        self.assertEqual(r["counts"], {"dead": 1, "changed": 1, "never": 1, "stale": 1, "blocked": 1})
        self.assertNotIn("fine", [x["course_id"] for x in r["courses"]])

    def test_a_missing_or_old_live_recheck_counts_as_stale(self):
        ok = {"status": "ok", "checked_on": "2026-10-05"}
        self.course("a", {"u": ok}, recheck=None)
        self.course("b", {"u": ok}, recheck="2025-01-01")
        self.assertEqual([x["flags"] for x in self.run_()["courses"]], [["stale"], ["stale"]])
        self.assertEqual(self.run_(stale_days=10000)["courses"][0]["flags"], ["stale"])          # missing recheck is stale whatever the limit

    def test_report_only_and_errors(self):
        self.course("x")
        before = sorted(os.listdir(os.path.join(self.tmp, "x")))
        self.run_()
        self.assertEqual(sorted(os.listdir(os.path.join(self.tmp, "x"))), before)
        self.assertIn("error", cr.run(os.path.join(self.tmp, "none")))
        self.assertEqual(cr.main([]), 2)
        self.assertEqual(cr.main([self.tmp, "--stale-days", "x"]), 2)


class SourceGate(unittest.TestCase):
    """K-10: the compile gate reads the same evidence."""
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        fx = os.path.join(os.path.dirname(HERE), "evals", "fixtures", "courses", "fx_maths_fractions")
        self.cd = os.path.join(self.tmp, "c")
        shutil.copytree(fx, self.cd)

    def test_a_clean_course_has_an_advisory_and_no_block(self):
        g = postcompile_gate._gate(self.cd)
        self.assertTrue(g["can_ship"])
        self.assertTrue(any(n.startswith("sources: 0 of") for n in g["advisory_notes"]))

    def test_dead_and_changed_sources_are_reported_not_blocking(self):
        url = "https://example.org/generic-tutor-fixtures"
        with open(os.path.join(self.cd, vs.SNAP), "w") as f:
            json.dump({"schema_version": 1, "snapshots": {url: {"status": "dead", "checked_on": "2026-10-07", "changed": True}}}, f)
        g = postcompile_gate._gate(self.cd)
        note = next(n for n in g["advisory_notes"] if n.startswith("sources:"))
        self.assertIn("1 dead", note)
        self.assertIn("1 changed", note)
        self.assertTrue(g["can_ship"])

    def test_a_cited_source_that_is_not_an_http_url_blocks(self):
        rp = os.path.join(self.cd, "rubric.json")
        with open(rp) as f:
            rub = json.load(f)
        rub["source_urls"].append("ftp://example.org/spec")
        with open(rp, "w") as f:
            json.dump(rub, f)
        g = postcompile_gate._gate(self.cd)
        self.assertFalse(g["can_ship"])
        self.assertTrue(any("not an http(s) URL" in b for b in g["blocking_reasons"]))


if __name__ == "__main__":
    unittest.main()
