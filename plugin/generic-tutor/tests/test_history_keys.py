"""History DB v2: ids are per course. v1 let two courses overwrite each other's error events and review cards."""
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
import sqlite_store  # noqa: E402

V1_TABLES = """
CREATE TABLE error_events (id TEXT PRIMARY KEY, course_id TEXT NOT NULL, stage_id TEXT NOT NULL, item_id TEXT, source_phase TEXT NOT NULL,
  cause TEXT NOT NULL, misconception_id TEXT, rubric_criterion TEXT, note TEXT, slot INTEGER NOT NULL, resolved INTEGER NOT NULL DEFAULT 0,
  resolved_at_slot INTEGER, created_at TEXT NOT NULL DEFAULT (datetime('now')));
CREATE INDEX idx_error_events_lookup ON error_events (course_id, stage_id, item_id, cause);
CREATE TABLE review_cards (id TEXT PRIMARY KEY, course_id TEXT NOT NULL, stage_id TEXT NOT NULL, item_id TEXT, criterion TEXT, front TEXT NOT NULL,
  back TEXT NOT NULL, interval_sessions INTEGER NOT NULL, due_at_slot INTEGER NOT NULL, ease REAL NOT NULL, lapses INTEGER NOT NULL DEFAULT 0);
CREATE INDEX idx_review_cards_due ON review_cards (course_id, due_at_slot);
CREATE TABLE review_log (id INTEGER PRIMARY KEY AUTOINCREMENT, card_id TEXT NOT NULL, correct INTEGER NOT NULL, old_interval INTEGER NOT NULL,
  new_interval INTEGER NOT NULL, old_ease REAL NOT NULL, new_ease REAL NOT NULL, slot INTEGER NOT NULL, created_at TEXT NOT NULL DEFAULT (datetime('now')));
"""


def entry(eid="err_2026-10-05_S1_001", stage="S1"):
    return {"id": eid, "stage_id": stage, "item_id": "S1.1", "source_phase": "practice", "cause": "slip", "misconception_id": None,
            "rubric_criterion": None, "note": "n", "slot": 5, "resolved": False}


def card(cid="S1-c1"):
    return {"id": cid, "stage_id": "S1", "front": "f", "back": "b", "interval_sessions": 1, "due_at_slot": 6, "ease": 2.3, "lapses": 0}


class Keys(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.a, self.b = f"{self.fx['S']}/mathA.json", f"{self.fx['S']}/solo.json"
        self.db = f"{self.fx['L']}/tutor.sqlite3"

    def q(self, sql, args=()):
        con = sqlite3.connect(self.db)
        try:
            return con.execute(sql, args).fetchall()
        finally:
            con.close()

    def test_same_ids_in_two_courses_both_survive_and_resolve_independently(self):
        for path in (self.a, self.b):
            self.assertTrue(sqlite_store.log_error_event(path, entry())["ok"])
            self.assertTrue(sqlite_store.upsert_review_card(path.replace(".json", "_review_deck.json"), card())["ok"])
        self.assertEqual(self.q("SELECT course_id FROM error_events ORDER BY 1"), [("mathA",), ("solo",)])
        self.assertEqual(self.q("SELECT course_id FROM review_cards ORDER BY 1"), [("mathA",), ("solo",)])
        sqlite_store.resolve_error_events(self.a, ["err_2026-10-05_S1_001"], 9)
        self.assertEqual(self.q("SELECT course_id, resolved FROM error_events ORDER BY 1"), [("mathA", 1), ("solo", 0)])
        sqlite_store.log_review_pass(self.a.replace(".json", "_review_deck.json"), "S1-c1", True, 1, 2, 2.3, 2.35, 7)
        self.assertEqual(self.q("SELECT course_id, card_id FROM review_log"), [("mathA", "S1-c1")])

    def test_v1_database_is_migrated_in_place_keeping_its_rows(self):
        con = sqlite3.connect(self.db)
        con.executescript(V1_TABLES)
        con.execute("INSERT INTO error_events (id, course_id, stage_id, item_id, source_phase, cause, slot) VALUES ('e1','mathA','S1','S1.1','practice','slip',5)")
        con.execute("INSERT INTO review_cards VALUES ('k1','mathA','S1',NULL,NULL,'f','b',1,6,2.3,0)")
        con.execute("INSERT INTO review_log (card_id, correct, old_interval, new_interval, old_ease, new_ease, slot) VALUES ('k1',1,1,2,2.3,2.35,6)")
        con.commit()
        con.close()
        self.assertTrue(sqlite_store.log_error_event(self.b, entry("e1"))["ok"])               # same id, other course: no longer an overwrite
        self.assertEqual(self.q("PRAGMA user_version"), [(sqlite_store.DB_SCHEMA_VERSION,)])
        self.assertEqual(self.q("SELECT course_id, id FROM error_events ORDER BY 1"), [("mathA", "e1"), ("solo", "e1")])
        self.assertEqual(self.q("SELECT id, course_id FROM review_cards"), [("k1", "mathA")])
        self.assertEqual(self.q("SELECT course_id, card_id FROM review_log"), [("mathA", "k1")])           # backfilled from the card
        self.assertEqual(sqlite_store.check(self.fx["L"])["healthy"], True)
        names = {r[0] for r in self.q("SELECT name FROM sqlite_master WHERE type = 'index'")}
        self.assertTrue({"idx_error_events_lookup", "idx_review_cards_due", "idx_review_log_course"} <= names)
        self.assertFalse({r[0] for r in self.q("SELECT name FROM sqlite_master WHERE name LIKE '%_v1'")})

    def test_migration_is_idempotent(self):
        con = sqlite3.connect(self.db)
        con.executescript(V1_TABLES)
        con.commit()
        con.close()
        for _ in range(3):
            self.assertTrue(sqlite_store.log_error_event(self.a, entry(f"x{_}"))["ok"])
        self.assertEqual(len(self.q("SELECT * FROM error_events")), 3)


if __name__ == "__main__":
    unittest.main()
