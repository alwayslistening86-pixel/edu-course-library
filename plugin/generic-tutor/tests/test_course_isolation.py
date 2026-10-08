"""One course's activity must never change another course's state or history, even when stage, item and card ids coincide.

The same sequence of writes is applied to course B alone, and to B interleaved with course A (which reuses every id). B's progress
file, review deck and history rows must come out identical in both runs.
"""
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402

TABLES = ("error_events", "item_mastery", "item_mastery_log", "review_cards", "review_log", "confidence_events")


def ops(subj, deck, course):
    """A representative sequence of per-course writes; ids deliberately identical across courses."""
    return [
        ("error_log.py", ["append", subj, "S1", "S1.1", "practice", "slip", "NONE", "n", "6"]),
        ("error_log.py", ["append", subj, "S1", "S1.1", "practice", "misconception", "MC-1", "n", "7"]),
        ("item_mastery.py", ["observe", subj, "S1.1", "true", "7"]),
        ("item_mastery.py", ["observe", subj, "S1.1", "false", "8"]),
        ("confidence_update.py", ["apply", subj, "pass_clean", "8"]),
        ("remediation_state.py", ["record", subj, "S1", "slip", "8"]),
        ("deck_add.py", [deck, course, "S1", "--max-per-stage", "3"]),
        ("review_math.py", ["apply", deck, "S1-c1", "9", "true"]),
        ("review_math.py", ["apply", deck, "S1-c1", "10", "false"]),
        ("error_log.py", ["resolve", subj, "S1.1", "11"]),
        ("practice_pick.py", ["used", subj, "S1", "generated"]),
        ("record_grading.py", [subj, f"{{C}}/{course}/course.json", "S1", "9"]),
        ("record_stage_result.py", ["apply", subj, f"{{C}}/{course}/course.json", "S1", "pass"]),
    ]


GRADES = json.dumps([{"criterion": 1, "met": True, "marks": 1, "of": 1}, {"criterion": 2, "met": True, "marks": 1, "of": 1}])
CARDS = json.dumps([{"front": "What is the first fact?", "back": "One."}, {"front": "What is the second fact?", "back": "Two."}])


def run_ops(fx, tmp, course, only=None):
    import subprocess
    subj, deck = f"{fx['S']}/{course}.json", f"{fx['S']}/{course}_review_deck.json"
    results = []
    for script, args in ops(subj, deck, course):
        if only is not None and script not in only:
            continue
        argv = [sys.executable, os.path.join(gs.SCRIPTS, script)] + [a.format(**fx) for a in args]
        p = subprocess.run(argv, input=CARDS if script == "deck_add.py" else GRADES if script == "record_grading.py" else None, capture_output=True, text=True, cwd=tmp)
        results.append((script, p.returncode))
    return results


def snapshot(fx, course):
    out = {}
    for name in (f"{course}.json", f"{course}_review_deck.json"):
        path = f"{fx['S']}/{name}"
        if os.path.exists(path):
            d = gs.read_json(path)
            d.pop("last_updated", None)
            out[name] = d
    con = sqlite3.connect(f"{fx['L']}/tutor.sqlite3")
    try:
        for t in TABLES:
            cols = [r[1] for r in con.execute(f"PRAGMA table_info({t})") if r[1] != "created_at" and not (r[1] == "id" and r[2] == "INTEGER")]
            out[t] = sorted(map(tuple, con.execute(f"SELECT {', '.join(cols)} FROM {t} WHERE course_id = ?", (course,)).fetchall()), key=repr)
    finally:
        con.close()
    return out


class Isolation(unittest.TestCase):
    def world(self):
        tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        fx = gs.build_fixture(tmp)
        # a second course whose stage ids match mathA's, enrolled for the same learner
        gs.build_course(fx["C"], "twin", level=2, stages=("S1", "S2", "S3"))
        d = gs.read_json(f"{fx['S']}/mathA.json")
        d["course_id"], d["syllabus_status"], d["current_stage"], d["error_patterns"], d["item_mastery"], d["remediation"] = (
            "twin", {"S1": "unsat", "S2": "unsat", "S3": "unsat"}, "S1", [], {}, {})
        with open(f"{fx['S']}/twin.json", "w") as f:
            json.dump(d, f)
        return fx, tmp

    def test_interleaved_activity_does_not_change_the_other_course(self):
        solo_fx, solo_tmp = self.world()
        mixed_fx, mixed_tmp = self.world()
        # alone: only 'twin' acts
        r_alone = run_ops(solo_fx, solo_tmp, "twin")
        # interleaved: mathA does the same thing, step by step, between twin's steps (fresh worlds start identical)
        import subprocess
        a_subj, a_deck = f"{mixed_fx['S']}/mathA.json", f"{mixed_fx['S']}/mathA_review_deck.json"
        t_subj, t_deck = f"{mixed_fx['S']}/twin.json", f"{mixed_fx['S']}/twin_review_deck.json"
        r_mixed = []
        for (script, a_args), (_, t_args) in zip(ops(a_subj, a_deck, "mathA"), ops(t_subj, t_deck, "twin"), strict=True):
            for args, course in ((a_args, "mathA"), (t_args, "twin")):
                argv = [sys.executable, os.path.join(gs.SCRIPTS, script)] + [a.format(**mixed_fx) for a in args]
                p = subprocess.run(argv, input=CARDS if script == "deck_add.py" else GRADES if script == "record_grading.py" else None, capture_output=True, text=True, cwd=mixed_tmp)
                if course == "twin":
                    r_mixed.append((script, p.returncode))
        self.assertEqual(r_alone, r_mixed)
        self.assertTrue(all(rc == 0 for _, rc in r_alone), r_alone)
        self.assertEqual(snapshot(mixed_fx, "twin"), snapshot(solo_fx, "twin"))
        self.assertGreater(len(snapshot(mixed_fx, "twin")["error_events"]), 0)
        self.assertEqual(snapshot(mixed_fx, "mathA"), snapshot(mixed_fx, "mathA"))      # sanity: snapshots are deterministic

if __name__ == "__main__":
    unittest.main()
