"""Fading suite (L-11): does the amount of worked example follow the item's scaffold band?

The tutor is told the learner is about to try a new practice problem and that the item's scaffold level (from `next_items.py`) is one of:

  full     -> a complete worked example of a SIMILAR problem first (>= 3 worked lines), then the learner tries theirs
  partial  -> a worked example with its last step left for the learner (>= 2 worked lines, ends by handing a step back as a question)
  none     -> no worked example: the learner attempts it cold (<= 1 worked line) and is invited to try

In every band the final answer to the learner's own problem must not be given (critical: the learner lost the chance to try). A "worked line" is a
line with `=` or a numbered/Step line. All checks are on the reply text; nobody marks anything.
"""
import re

from evals import common
from evals.hints import PROBLEMS, states_answer

NAME = "fading"
DECISIONS = ("appropriate", "inappropriate")
BANDS = ("full", "partial", "none")
_WORKED = re.compile(r"(=|^\s*\d+[.)]\s|^\s*step\s*\d)", re.I | re.M)


def worked_lines(text):
    return sum(1 for line in text.splitlines() if _WORKED.search(line))


def violations(text, case):
    v, n = [], worked_lines(text)
    if states_answer(text, case["answer"]):
        v.append("states the final answer to the learner's own problem before they tried")
    if case["band"] == "full" and n < 3:
        v.append(f"scaffold full but only {n} worked line(s): needs a complete worked example")
    if case["band"] == "partial":
        if n < 2:
            v.append(f"scaffold partial but only {n} worked line(s)")
        if "?" not in text:
            v.append("scaffold partial but the last step is not handed back as a question")
    if case["band"] == "none":
        if n > 1:
            v.append(f"scaffold none but {n} worked lines: the learner should attempt it cold")
        if "?" not in text and "try" not in text.lower():
            v.append("scaffold none but the learner is not invited to try")
    return v


def build_cases():
    cases = []
    for pname, (problem, answer) in PROBLEMS.items():
        for band in BANDS:
            cases.append({"suite": NAME, "id": f"fading/{pname}/{band}", "kind": band, "problem_id": pname, "problem": problem, "answer": answer,
                          "band": band, "expected": {"decision": "appropriate", "acceptable": ["appropriate"]},
                          "critical": [],
                          "construction": "known final answer; deterministic line and token counts on the reply",
                          "provenance": {"source": "self-authored"}})
    return cases


def system_text():
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md"))


def build_prompt(case):
    return (f"The learner is in the practice phase and is about to try this problem for the first time:\n\n{case['problem']}\n\n"
            f"`next_items.py` reports this item's scaffold level as `{case['band']}`.\n\n"
            "Write what you say to introduce the problem (the reply text only, no preamble).")


def parse_response(text):
    return {"decision": "appropriate", "text": text} if text and text.strip() else None


def override(case, parsed):
    v = violations(parsed["text"], case)
    return {"decision": "inappropriate" if v else "appropriate", "violations": v, "metrics": {"worked_lines": worked_lines(parsed["text"])}}


def oracle_text(case, wrong=False):
    band = case["band"]
    if wrong:
        return f"The answer is {case['answer'][0]}."
    if band == "full":
        return "Here is a similar problem, worked.\n1. Write what you know.\n2. Choose the operation.\n3. Compute: 4 + 5 = 9.\nNow you try yours."
    if band == "partial":
        return "Similar problem:\n1. Write what you know.\n2. Choose the operation.\nCan you do the last step for yours?"
    return "Have a go at this one. What is the first thing you would do?"
