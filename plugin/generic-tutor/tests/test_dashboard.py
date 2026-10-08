"""U-03: the static progress page - content, escaping, privacy of the page itself."""
import html.parser
import json
import os
import re
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import dashboard_html  # noqa: E402
import golden_support as gs  # noqa: E402


class Page(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.L, self.C, self.S = self.fx["L"], self.fx["C"], self.fx["S"]

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)

    def html(self):
        doc, err = dashboard_html.build(self.L, self.C, "2026-10-04")
        self.assertIsNone(err)
        return doc

    def test_contains_the_essentials(self):
        doc = self.html()
        for needle in ("Progress: amy", "Course mathA", "1 of 3 stages passed", "Readiness:", "Not enough evidence yet", "/review", "not a grade"):
            self.assertIn(needle, doc)

    def test_is_self_contained_and_script_free(self):
        doc = self.html()
        self.assertNotRegex(doc, r"<script|https?://|<link|<img|@import|src=")
        self.assertIn("prefers-color-scheme:dark", doc)
        self.assertIn('name="viewport"', doc)

    def test_every_learner_derived_string_is_escaped(self):
        evil = '<script>alert(1)</script>"&'
        self.edit(f"{self.C}/mathA/course.json", lambda d: d.update(name=evil))
        self.edit(f"{self.L}/student_profile.json", lambda d: d.update(learner_id=evil))
        doc = self.html()
        self.assertNotIn("<script>alert", doc)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", doc)

    def test_is_well_formed_enough_to_parse(self):
        class P(html.parser.HTMLParser):
            def __init__(self):
                super().__init__()
                self.stack, self.bad = [], 0
            def handle_starttag(self, tag, attrs):
                if tag not in ("meta", "br"):
                    self.stack.append(tag)
            def handle_endtag(self, tag):
                if self.stack and self.stack[-1] == tag:
                    self.stack.pop()
                else:
                    self.bad += 1
        p = P()
        p.feed(self.html())
        self.assertEqual((p.bad, p.stack), (0, []))

    def test_errors_mocks_and_weak_items_shown_without_grades(self):
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(
            item_mastery={"S1.1": {"p_mastery": 0.2, "observations": 3}, "S2.1": {"p_mastery": 0.9, "observations": 3}, "S3.1": {"p_mastery": 0.8, "observations": 3}},
            error_patterns=[{"id": "e", "stage_id": "S1", "source_phase": "test", "cause": "slip", "slot": 1, "resolved": False}],
            mock_results=[{"date": "2026-10-01", "total_marks": 40, "awarded": 30, "percent": 75.0, "minutes": 45}]))
        doc = self.html()
        for needle in ("Unresolved mistakes by cause", "slip", "Weakest items", "S1.1", "75.0%", "Mock papers are shown beside the band"):
            self.assertIn(needle, doc)
        self.assertIsNone(re.search(r"grade \d|predicted grade|you will get", doc, re.I))

    def test_cli_writes_atomically_outside_the_learner_folder(self):
        out = os.path.join(self.tmp, "exports", "amy.html")
        r = gs.run_step("dashboard_html.py", ["{L}", "{C}", out], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0, r)
        self.assertTrue(os.path.isfile(out))
        self.assertFalse(os.path.exists(out + ".part"))
        inside = os.path.join(self.L, "dash.html")
        self.assertEqual(gs.run_step("dashboard_html.py", ["{L}", "{C}", inside], self.fx, self.tmp)["exit"], 1)
        self.assertFalse(os.path.exists(inside))
        self.assertEqual(gs.run_step("dashboard_html.py", ["{L}", "{C}"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("dashboard_html.py", ["{L}/nope", "{C}", out + "2"], self.fx, self.tmp)["exit"], 1)

    def test_read_only_for_tutor_state(self):
        def snapshot():
            out = {}
            for dp, _dn, fns in os.walk(self.L):
                for fn in fns:
                    with open(os.path.join(dp, fn), "rb") as f:
                        out[os.path.join(dp, fn)] = f.read()
            return out
        before = snapshot()
        self.html()
        self.assertEqual(snapshot(), before)



class Framing(unittest.TestCase):
    """U-05: progress is framed as learning and next steps, never as streaks, points or rankings."""
    BANNED = ("streak", "badge", "leaderboard", "ranking", "points earned", "you are behind", "you're behind", "xp")

    def test_the_dashboard_uses_no_gamified_language(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp, True)
        fx = gs.build_fixture(tmp)
        doc, err = dashboard_html.build(fx["L"], fx["C"], "2026-10-04")
        text = doc.lower()
        for w in self.BANNED:
            self.assertNotIn(w, text, w)

    def test_the_status_skill_states_the_rule(self):
        with open(os.path.join(os.path.dirname(HERE), "skills", "health-status", "SKILL.md"), encoding="utf-8") as f:
            self.assertIn("No streaks", f.read())

class Summary(Page):
    """U-06: the printable summary a learner chooses to share."""

    def add_mistake(self):
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(error_patterns=[{"cause": "misconception", "resolved": False, "note": "x"}]))

    def summary(self, who="Ms Okafor (tutor)"):
        doc, err = dashboard_html.build(self.L, self.C, "2026-10-04", who)
        self.assertIsNone(err)
        return doc

    def test_it_names_its_recipient_and_keeps_the_essentials(self):
        doc = self.summary()
        for needle in ("Progress summary: amy", "Prepared for Ms Okafor (tutor) on 2026-10-04", "Course mathA", "1 of 3 stages passed",
                       "Readiness:", "not a grade", "prepared by the learner to share with Ms Okafor"):
            self.assertIn(needle, doc)

    def test_it_leaves_out_what_the_full_page_shows_about_mistakes_and_next_steps(self):
        self.add_mistake()
        full, short = self.html(), self.summary()
        self.assertIn("Unresolved mistakes by cause", full)
        for hidden in ("Unresolved mistakes by cause", "Next step", "Reviews due", "Weakest items", "Mock paper", "roster", "Session "):
            self.assertNotIn(hidden, short, hidden)

    def test_the_recipient_is_escaped(self):
        doc = self.summary('<script>alert(1)</script> & "co"')
        self.assertNotIn("<script>alert", doc)
        self.assertIn("&lt;script&gt;", doc)

    def test_revoked_consent_refuses_a_summary_but_not_the_private_page(self):
        self.edit(f"{self.L}/student_profile.json", lambda d: d.setdefault("consent", {}).update(status="revoked"))
        doc, err = dashboard_html.build(self.L, self.C, "2026-10-04", "a tutor")
        self.assertIsNone(doc)
        self.assertIn("consent is revoked", err)

    def test_both_forms_have_a_print_stylesheet_and_a_neutral_language_tag(self):
        for doc in (self.html(), self.summary()):
            self.assertIn("@media print", doc)
            self.assertIn('<html lang="en">', doc)
        self.edit(f"{self.L}/student_profile.json", lambda d: d.setdefault("identity", {}).update(locale="en-US"))
        self.assertIn('<html lang="en-US">', self.html())

    def test_cli_needs_a_real_recipient_and_writes_outside_the_learner_folder(self):
        out = os.path.join(self.tmp, "exports", "amy-summary.html")
        self.assertEqual(dashboard_html.main([self.L, self.C, out, "--summary-for", "  "]), 2)
        self.assertEqual(dashboard_html.main([self.L, self.C, out, "--summary-for"]), 2)
        self.assertEqual(dashboard_html.main([self.L, self.C, out, "--summary-for", "a tutor", "--today", "2026-10-04"]), 0)
        with open(out, encoding="utf-8") as f:
            self.assertIn("Prepared for a tutor", f.read())
        inside = os.path.join(self.L, "summary.html")
        self.assertEqual(dashboard_html.main([self.L, self.C, inside, "--summary-for", "a tutor"]), 1)  # same refusal as the full page
        self.assertFalse(os.path.exists(inside))


if __name__ == "__main__":
    unittest.main()
