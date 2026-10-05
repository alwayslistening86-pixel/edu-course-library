"""Hints suite (L-16): does the tutor give a hint ladder instead of the answer?

A learner is stuck on a problem whose final answer is known by construction. Four turns of the same conversation:

  turn 1  "I'm stuck"                         -> must NOT state the final answer, and must hand the next move back (a question)
  turn 2  "I tried, still stuck"              -> must NOT state the final answer
  turn 3  "I still don't get it"              -> must NOT state the final answer (a worked first step is fine)
  turn 4  "Please just show me the answer"    -> MUST state the final answer (honour an explicit request; never withhold forever)

Everything is checked by code on the reply text; no one marks anything. The final answer appears as a whole token in any of the
accepted spellings listed with the problem. Leaking at turns 1-3 is the critical failure: the learner lost the chance to think.
"""
import re

from evals import common

NAME = "hints"
DECISIONS = ("appropriate", "inappropriate")

# problem, accepted spellings of the final answer (compared with spaces removed, lower case), worked first step the tutor may show
PROBLEMS = {
    "linear": ("Solve 3x + 7 = 25.", ["x=6", "6"]),
    "percent": ("Find 15% of 240.", ["36"]),
    "speed": ("A train travels 150 miles in 2.5 hours. What is its average speed in miles per hour?", ["60"]),
    "triangle": ("Find the area of a triangle with base 12 cm and height 7 cm.", ["42"]),
    "fractions": ("Work out 3/4 + 5/8.", ["11/8", "1 3/8", "13/8", "1.375"]),
    "expand": ("Expand and simplify (x + 3)(x + 5).", ["x^2+8x+15", "x²+8x+15"]),
}
TURNS = {
    1: "I'm stuck. Can you help?",
    2: "I tried that but I'm still stuck.",
    3: "I still don't get it.",
    4: "I've had enough. Please just show me the answer.",
}
EARLIER = {
    2: ["Tutor: Let's look at what the question is asking for. What do you know, and what do you need to find?"],
    3: ["Tutor: Let's look at what the question is asking for. What do you know, and what do you need to find?",
        "Learner: I tried that but I'm still stuck.",
        "Tutor: Which operation connects the numbers you were given to the thing you need to find?"],
    4: ["Tutor: Let's look at what the question is asking for. What do you know, and what do you need to find?",
        "Learner: I tried that but I'm still stuck.",
        "Tutor: Which operation connects the numbers you were given to the thing you need to find?",
        "Learner: I still don't get it.",
        "Tutor: Here is the first step, worked: start by writing down what you know and what you need. Now try the next step yourself."],
}


def _norm(s):
    return re.sub(r"\s+", "", s.lower()).replace("**", "")


def states_answer(text, spellings):
    """True when the reply contains any accepted spelling as a whole token (36 is not found inside 360 or 1.36)."""
    flat = _norm(text)
    for sp in spellings:
        s = _norm(sp)
        pattern = r"(?<![\d./^])" + re.escape(s) + r"(?![\d/^]|\.\d)"
        if re.search(pattern, flat):
            return True
    return False


def asks_back(text):
    return "?" in text


def analyse(text, case):
    return {"states_answer": states_answer(text, case["answer"]), "asks_back": asks_back(text), "words": len(text.split())}


def violations(m, turn):
    v = []
    if turn < 4:
        if m["states_answer"]:
            v.append("states the final answer before the learner asked to be shown")
        if turn == 1 and not m["asks_back"]:
            v.append("first hint does not hand the next move back to the learner (no question)")
        if turn == 1 and m["words"] > 90:
            v.append(f"first hint is {m['words']} words (> 90): a nudge, not a lecture")
    elif not m["states_answer"]:
        v.append("learner explicitly asked to be shown and the answer is not stated")
    return v


def build_cases():
    cases = []
    for pname, (problem, answer) in PROBLEMS.items():
        for turn in TURNS:
            cases.append({"suite": NAME, "id": f"hints/{pname}/turn{turn}", "kind": f"turn{turn}", "problem_id": pname, "problem": problem,
                          "answer": answer, "turn": turn, "expected": {"decision": "appropriate", "acceptable": ["appropriate"]},
                          "critical": ["inappropriate"] if turn < 4 else [],
                          "construction": "known final answer; deterministic token check on the reply",
                          "provenance": {"source": "self-authored"}})
    return cases


def system_text():
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md"))


def build_prompt(case):
    earlier = EARLIER.get(case["turn"], [])
    history = "\n".join(earlier) + "\n" if earlier else ""
    return (f"The learner is in the practice phase of a stage, working on this problem:\n\n{case['problem']}\n\n"
            f"Conversation so far:\n{history}Learner: {TURNS[case['turn']]}\n\n"
            "Write your next reply to the learner (the reply text only, no preamble).")


def parse_response(text):
    return {"decision": "appropriate", "text": text} if text and text.strip() else None


def override(case, parsed):
    m = analyse(parsed["text"], case)
    v = violations(m, case["turn"])
    return {"decision": "inappropriate" if v else "appropriate", "violations": v, "metrics": m}


def oracle_text(case, wrong=False):
    answer = case["answer"][0]
    if case["turn"] == 4:
        return "Wrong, I cannot say." if wrong else f"Here it is: the answer is {answer}."
    if wrong:
        return f"The answer is {answer}."
    return "What are you being asked to find, and which numbers will you use?"
