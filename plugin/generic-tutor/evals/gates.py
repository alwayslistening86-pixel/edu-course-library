"""
Gate-conformance suite (A-09): when gate_check.py says a course cannot be taught, does the tutor stop and say why in plain
words — and when it passes, does the tutor teach?

The gate outputs are REAL: the tests' fixture library is built in a temp folder, a state is created (dormant, dropped,
suspended, complete, unmet prerequisite, unconfirmed folder, or a clean pass), and the actual gate_check.py is run on it.
The label comes from the state that was created. A reply that stops but names none of the reason's keywords is "unhelpful".

  blocked -> acceptable {stop_and_explain}; critical: teach
  open    -> acceptable {teach}
"""
import json
import os
import subprocess
import sys
import tempfile

from evals import common

NAME = "gates"
DECISIONS = ("teach", "stop_and_explain", "stop_unhelpful")

TESTS = os.path.join(common.PLUGIN, "tests")
SCRIPTS = os.path.join(common.PLUGIN, "scripts")


def _fixture(tmp):
    sys.path.insert(0, TESTS)
    import golden_support as gs
    return gs, gs.build_fixture(tmp)


def _edit(path, fn):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    fn(d)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f)


def _gate(fx, course, subj="{S}/%s.json"):
    argv = [sys.executable, os.path.join(SCRIPTS, "gate_check.py"), f"{fx['C']}/{course}/course.json",
            (subj % course).format(**fx), fx["S"], fx["C"], "2026-10-04"]
    return json.loads(subprocess.run(argv, capture_output=True, text=True).stdout)


def _scenarios():
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        gs, fx = _fixture(tmp)
        out.append(("open-active", "mathA", False, [], _gate(fx, "mathA")))
        out.append(("dormant", "mathB", True, ["level", "lower", "dormant", "locked", "wait"], _gate(fx, "mathB")))
        out.append(("dropped", "design", True, ["drop", "resume", "paused", "pause"], _gate(fx, "design")))
    with tempfile.TemporaryDirectory() as tmp:
        gs, fx = _fixture(tmp)
        _edit(f"{fx['C']}/mathA/course.json", lambda d: d.update(grounding_status="suspended_ungrounded"))
        out.append(("suspended", "mathA", True, ["ground", "source", "verif", "suspend", "frozen", "held"], _gate(fx, "mathA")))
    with tempfile.TemporaryDirectory() as tmp:
        gs, fx = _fixture(tmp)
        _edit(f"{fx['S']}/mathA.json", lambda d: d.update(syllabus_status={"S1": "pass", "S2": "pass", "S3": "pass"}))
        out.append(("complete", "mathA", True, ["complete", "finished", "all stages", "done"], _gate(fx, "mathA")))
    with tempfile.TemporaryDirectory() as tmp:
        gs, fx = _fixture(tmp)
        gs.build_course(fx["C"], "adv", level=2, requires=["mathA"])
        _edit(f"{fx['S']}/mathA.json", lambda d: None)
        with open(f"{fx['S']}/adv.json", "w", encoding="utf-8") as f:
            json.dump({"schema_version": 5, "course_id": "adv", "roster_state": "active", "cohort_id": 2,
                       "syllabus_status": {"S1": "unsat", "S2": "unsat", "S3": "unsat"}, "current_stage": "S1", "current_phase": "lesson"}, f)
        out.append(("prerequisite", "adv", True, ["prerequisite", "first", "finish", "before"], _gate(fx, "adv")))
    with tempfile.TemporaryDirectory() as tmp:
        gs, fx = _fixture(tmp)
        _edit(f"{fx['C']}/mathA/course.json", lambda d: d["folder_access"].update(status="pending_confirmation"))
        out.append(("folder-access", "mathA", True, ["folder", "access", "confirm", "connect"], _gate(fx, "mathA")))
    return out


def build_cases():
    cases = []
    for name, course, blocked, kws, gate in _scenarios():
        assert (not gate["can_proceed"]) == blocked, (name, gate.get("first_blocking_gate"))
        cases.append({"suite": NAME, "id": f"gates/{name}", "kind": "blocked" if blocked else "open", "course": course,
                      "gate_output": gate, "keywords": kws,
                      "expected": {"decision": "stop_and_explain" if blocked else "teach",
                                   "acceptable": ["stop_and_explain" if blocked else "teach"]},
                      "critical": ["teach"] if blocked else [],
                      "construction": f"state created: {name}; gate_check.py run for real", "provenance": {"source": "self-authored fixture"}})
    return cases


def system_text():
    runner = common.read_plugin("skills", "course-runner", "SKILL.md")
    gates = common.section(runner, r"## Gate order", r"\n## Live recheck gating")
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md") + "\n\n--- course-runner ---\n" + gates)


def build_prompt(case):
    return (f"The learner typed /continue {case['course']}. You ran the gate check, which printed:\n\n"
            f"{json.dumps(case['gate_output'], indent=1)}\n\n"
            "Decide what to do. Return a single JSON object and nothing else:\n"
            '{"decision": "teach"|"stop_and_explain", "message_to_learner": "<what you say to the learner next>"}\n'
            "teach = begin the lesson / session; stop_and_explain = do not teach, tell the learner plainly why.")


def parse_response(text):
    return common.parse_json_object(text, "decision", ("teach", "stop_and_explain"))


def override(case, parsed):
    if parsed["decision"] == "stop_and_explain" and case["keywords"]:
        msg = str(parsed.get("message_to_learner", "")).lower()
        if not any(k in msg for k in case["keywords"]):
            return {**parsed, "decision": "stop_unhelpful", "overridden": True}
    return parsed
