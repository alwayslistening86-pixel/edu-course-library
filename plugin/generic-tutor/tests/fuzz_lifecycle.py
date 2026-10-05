"""
fuzz_lifecycle.py - composition fuzz for generic-tutor's level-lock / roster / ledger logic.

Drives the REAL scripts (roster_check, resume_enrollment, cohort_status) in the order the skill prose
prescribes for /add-course, /drop, resume and level-clearing, over random action sequences, and asserts
after every step:
  I1  every live course above the cleared level sits at the lowest unfinished level
  I2  roster_check reports nothing that should already have woken (wake_now == [])
  I3  roster occupancy never exceeds the cap (adds/resumes are cap-checked)
  I4  the ledger only falls on a resume (the one deliberate lowering)
  I5  no dormant course sits at or below the cleared level

Usage (from the plugin root):   python3 tests/fuzz_lifecycle.py [num_sequences=3000] [steps=25]
(test_fuzz.py runs a fixed-seed subset of this under `unittest discover`; file handling was tidied there so it
is clean under -W error::ResourceWarning - logic is unchanged from the reviewer's original.)
Env: TUTOR_SCRIPTS=<dir> to point at another scripts/ folder; NO_WAKE_ON_DROP=1 to drop the /drop wake step
(a deliberate sensitivity check - the run should then FAIL).
Covers: one stage ladder, no exams, no suspension, no consent modes, no convergence testing, one learner.
It exercises the scripts as I read the prose; it cannot show that Claude follows the prose.
"""
import sys
import json
import os
import tempfile
import random
import shutil
S = os.environ.get("TUTOR_SCRIPTS", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
sys.path.insert(0, S)
from roster_check import compute as roster
from resume_enrollment import resume as resume_enr
from cohort_status import compute_cohorts, level_walk, is_complete

def _rj(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _wj(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


class World:
    def __init__(self, cap):
        self.root = tempfile.mkdtemp()
        self.P = f"{self.root}/p"; self.C = f"{self.root}/c"
        os.makedirs(f"{self.P}/subjects"); os.makedirs(self.C)
        self.prof = f"{self.P}/student_profile.json"
        _wj(self.prof, {"roster": {"max_incomplete_courses": cap}, "highest_level_cleared": 0})
        self.n = 0; self.cap = cap
    def cleanup(self): shutil.rmtree(self.root, ignore_errors=True)
    # -- file helpers
    def subj_path(self, cid): return f"{self.P}/subjects/{cid}.json"
    def course_path(self, cid): return f"{self.C}/{cid}/course.json"
    def subj(self, cid): return _rj(self.subj_path(cid))
    def save_subj(self, cid, s): _wj(self.subj_path(cid), s)
    def ledger(self): return _rj(self.prof)["highest_level_cleared"]
    def set_ledger(self, v):
        p = _rj(self.prof); p["highest_level_cleared"] = v; _wj(self.prof, p)
    def state(self, cid): return self.subj(cid)["roster_state"]
    def set_state(self, cid, st):
        s = self.subj(cid); s["roster_state"] = st; self.save_subj(cid, s)
    def ids(self): return sorted(f[:-5] for f in os.listdir(f"{self.P}/subjects"))
    def level(self, cid): return _rj(self.course_path(cid))["academic_level"]
    def complete(self, cid): return is_complete(_rj(self.course_path(cid)), self.subj(cid))
    def rc(self, *a, **k): return roster(self.P, self.C, *a, **k)

    # -- actions, following the skills' prose
    def add(self, level):
        r0 = self.rc()
        if not r0["can_add_course"]: return "add refused (roster full)"
        r = self.rc(level)
        self.n += 1; cid = f"C{self.n}"
        os.makedirs(f"{self.C}/{cid}")
        _wj(self.course_path(cid), {"schema_version": 2, "folder_access": {"status": "isolated_confirmed"}, "currency": "historical",
                   "academic_level": level, "stage_ladder": ["S1", "S2"], "grounding_status": "verified", "exam": {"enabled": False}})
        _wj(self.subj_path(cid), {"course_id": cid, "roster_state": r["candidate_state"], "cohort_id": level,
                   "syllabus_status": {"S1": "unsat", "S2": "unsat"}, "current_stage": "S1"})
        for c in r["courses_that_would_lock"]: self.set_state(c, "dormant")
        return f"add {cid}@L{level} -> {r['candidate_state']}, locks {r['courses_that_would_lock']}"

    def drop(self, cid):
        self.set_state(cid, "dropped")
        w = [] if os.environ.get("NO_WAKE_ON_DROP") else self.rc()["wake_now"]
        for c in w: self.set_state(c, "active")
        return f"drop {cid}, woke {w}"

    def resume(self, cid):
        r0 = self.rc()
        if not r0["can_add_course"]: return f"resume {cid} refused (roster full)"
        lvl = self.level(cid)
        r = self.rc(lvl, resume=True, resume_course_id=cid)
        if r["already_complete"]:
            res = resume_enr(self.subj_path(cid), self.course_path(cid), "active", "2026-09-18")
            return f"resume {cid} (already complete) -> {res['roster_state']}"
        kw = {}
        if r["reopens_level"]:
            kw = dict(reopen_profile=self.prof, reopen_to=r["effective_highest_level_cleared"])
        res = resume_enr(self.subj_path(cid), self.course_path(cid), r["candidate_state"], "2026-09-18", **kw)
        if not res["resumed"]: return f"resume {cid} FAILED {res}"
        for c in r["courses_that_would_lock"]: self.set_state(c, "dormant")
        return f"resume {cid}@L{lvl} -> {r['candidate_state']}, reopen {res['reopened_level']}, locks {r['courses_that_would_lock']}"

    def finish(self, cid):
        s = self.subj(cid); s["syllabus_status"] = {"S1": "pass", "S2": "pass"}; self.save_subj(cid, s)
        cohorts, _ = compute_cohorts(f"{self.P}/subjects", self.C)
        stored = self.ledger()
        walk = level_walk(cohorts, stored)
        note = f"finish {cid}@L{self.level(cid)}"
        if walk["to"] > stored:
            self.set_ledger(walk["to"])
            w = self.rc()["wake_now"]
            for c in w: self.set_state(c, "active")
            note += f", ledger {stored}->{walk['to']}, woke {w}"
        return note

    # -- invariants
    def check(self, before_ledger, last):
        errs = []
        r = self.rc()
        led = self.ledger()
        live = [c for c in self.ids() if self.state(c) in ("active", "test_pending_convergence") and not self.complete(c)]
        dorm = [c for c in self.ids() if self.state(c) == "dormant" and not self.complete(c)]
        pool = [self.level(c) for c in live + dorm if self.level(c) > led]
        floor = min(pool) if pool else None
        for c in live:
            if self.level(c) > led and self.level(c) != floor:
                errs.append(f"I1 live {c}@L{self.level(c)} above unfinished floor L{floor} (ledger {led})")
        if r["wake_now"]: errs.append(f"I2 dormant course(s) {r['wake_now']} should be awake")
        for c in dorm:
            if self.level(c) <= led: errs.append(f"I5 dormant {c}@L{self.level(c)} at/below ledger {led}")
        if r["roster_occupancy"] > self.cap: errs.append(f"I3 occupancy {r['roster_occupancy']} > cap {self.cap}")
        if led < before_ledger and not last.startswith("resume"): errs.append(f"I4 ledger fell {before_ledger}->{led} on '{last}'")
        return errs

def run(seed, steps):
    rnd = random.Random(seed)
    w = World(rnd.choice([2, 3, 4]))
    trace = []
    try:
        for _ in range(steps):
            ids = w.ids()
            live = [c for c in ids if w.state(c) in ("active", "test_pending_convergence") and not w.complete(c)]
            dropped = [c for c in ids if w.state(c) == "dropped"]
            notdropped = [c for c in ids if w.state(c) in ("active", "test_pending_convergence", "dormant")]
            choices = ["add"] * 4
            if notdropped: choices += ["drop"] * 2
            if dropped: choices += ["resume"] * 2
            if live: choices += ["finish"] * 3
            act = rnd.choice(choices)
            before = w.ledger()
            if act == "add": note = w.add(rnd.randint(1, 5))
            elif act == "drop": note = w.drop(rnd.choice(notdropped))
            elif act == "resume": note = w.resume(rnd.choice(dropped))
            else: note = w.finish(rnd.choice(live))
            trace.append(note)
            errs = w.check(before, note)
            if errs: return trace, errs
        return None, None
    finally:
        w.cleanup()

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    fails = {}
    for seed in range(N):
        tr, errs = run(seed, int(sys.argv[2]) if len(sys.argv) > 2 else 25)
        if errs:
            key = errs[0].split()[0]
            fails.setdefault(key, []).append((seed, tr, errs))
    print(f"sequences run: {N}; sequences with a violation: {sum(len(v) for v in fails.values())}")
    for k, lst in sorted(fails.items()):
        seed, tr, errs = min(lst, key=lambda x: len(x[1]))
        print(f"\n== {k}: {len(lst)} sequences; shortest ({len(tr)} steps, seed {seed}):")
        for i, t in enumerate(tr, 1): print(f"   {i:>2}. {t}")
        print("   VIOLATION:", errs)
    sys.exit(1 if fails else 0)
