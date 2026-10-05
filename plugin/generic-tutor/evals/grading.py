"""
Grading suite (A-03): does the tutor grade a test answer the way its own rules say it should?

Cases are built deterministically from evals/data/gsm8k_sample.json (MIT-licensed GSM8K questions, reference
solutions and gold answers). The learner response is synthetic and the reference label comes from HOW it was
built, so no human ever marks anything:

  correct          reference solution                              -> M1 true , A1 true , decision pass
  slip             reference solution, final number replaced      -> M1 true , A1 false, decision fail
  answer_only      only the gold final number                      -> M1 null , A1 true , decision needs_reasoning
  wrong_method     hand-built flawed working (labelled when built) -> M1 false, A1 false (or true by
                   coincidence for the one case where the answer happens to match), decision fail

The model under test is given the plugin's own text (tutor-core + the Test paragraph of course-runner), so a
change to those skills changes the prompt, and the skill hash recorded in every report shows which version a
result belongs to.
"""
import hashlib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(HERE)
DATA = os.path.join(HERE, "data", "gsm8k_sample.json")

NAME = "grading"
DECISIONS = ("pass", "fail", "needs_reasoning")


def _read(*p):
    with open(os.path.join(PLUGIN, *p), encoding="utf-8") as f:
        return f.read()


def system_text():
    """The plugin text the grader is held to: tutor-core in full plus the Test / recording paragraphs of course-runner."""
    runner = _read("skills", "course-runner", "SKILL.md")
    m = re.search(r"\*\*Test\*\* →.*?(?=\n\*\*Recording the result)", runner, re.S)
    test_rules = m.group(0) if m else ""
    diag = re.search(r"\*\*When it fires:\*\*.*?(?=\n\*\*Log what you found)", runner, re.S)
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + _read("skills", "tutor-core", "SKILL.md") + "\n\n--- course-runner: grading a test ---\n" + test_rules
            + ("\n\n--- course-runner: when answers do not support the reasoning ---\n" + diag.group(0) if diag else ""))


def skill_hash():
    return hashlib.sha256(system_text().encode("utf-8")).hexdigest()[:12]


def _replace_last_number(text, number, new):
    matches = list(re.finditer(r"(?<![\d.,])" + re.escape(number) + r"(?![\d])", text))
    if not matches:  # gold may be written with a thousands separator, e.g. 57,500
        alt = f"{int(number):,}" if number.isdigit() else number
        matches = list(re.finditer(re.escape(alt), text))
    m = matches[-1]
    return text[:m.start()] + new + text[m.end():]


def build_cases():
    data = json.load(open(DATA, encoding="utf-8"))
    prov = data["_provenance"]
    cases = []
    for it in data["items"]:
        row, q, sol, gold = it["row"], it["question"], it["solution"], it["gold"]
        base = {"suite": "grading", "item_row": row, "question": q, "gold": gold,
                "provenance": {"source": prov["dataset"], "licence": prov["licence"], "row": row}}

        def mk(kind, response, m1, a1, decision, note="", acceptable=None, base=base, row=row):
            cases.append({**base, "id": f"grading/gsm8k-{row}/{kind}", "kind": kind, "response": response,
                          "expected": {"M1": m1, "A1": a1, "decision": decision,
                                       "acceptable": sorted(acceptable or [decision])},
                          "critical": [] if decision == "pass" else ["pass"], "construction": note})
        mk("correct", sol, True, True, "pass", "reference solution")
        slip = data["slips"][str(row)]
        # The working computes the right answer but a different number is reported: the plugin's rules say to run the
        # diagnostic exchange when the working does not support the answer, so recording a fail OR asking first are both
        # correct; recording a PASS is the only wrong outcome.
        mk("slip", _replace_last_number(sol, gold, slip), True, False, "fail", f"final number replaced by {slip}",
           acceptable={"fail", "needs_reasoning"})
        mk("answer_only", f"The answer is {gold}.", None, True, "needs_reasoning", "no working shown")
        wm = data["wrong_methods"].get(str(row))
        if wm:
            mk("wrong_method", wm["text"], False, wm["final"] == gold, "fail", wm["note"], acceptable={"fail", "needs_reasoning"})
    return cases


RUBRIC = ("- M1: a valid method is shown (the working supports the answer).\n"
          "- A1: the final answer is correct.")


def build_prompt(case):
    return (f"A learner has just answered a stage-test question. Apply the plugin's grading rules to this answer.\n\n"
            f"Question: {case['question']}\n\nMark scheme (from the source):\n{RUBRIC}\n"
            f"The correct final answer is {case['gold']}.\n\nLearner's response:\n\"\"\"\n{case['response']}\n\"\"\"\n\n"
            "Reply with a single JSON object and nothing else:\n"
            '{"M1": true|false|null, "A1": true|false, "decision": "pass"|"fail"|"needs_reasoning", "reason": "<one sentence>"}\n'
            "where M1 is null if the method cannot be judged, and decision is the action the tutor should take "
            "before recording a grade (pass = record a genuine pass; fail = record a fail; needs_reasoning = ask the "
            "learner to explain before any grade is recorded).")


def parse_response(text):
    """Pull the first JSON object out of a model reply; None if there isn't a usable one."""
    m = re.search(r"\{.*?\}", text, re.S)
    if not m:
        return None
    try:
        d = json.loads(m.group(0))
    except ValueError:
        return None
    if d.get("decision") not in DECISIONS:
        return None
    return d
