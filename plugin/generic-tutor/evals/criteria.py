"""
Criteria suite (A-03 expansion): marking extended answers against published-style criteria, with no human marker.

Each task has a rubric of discrete criteria (each a statement the answer must make correctly) and a pass threshold. A learner
answer is ASSEMBLED from sentence blocks: for every criterion the block is either the correct statement, a plausible-but-wrong
statement (a classic error), or left out; padding sentences are true but credit nothing. Because the answer is built from known
parts, which criteria it earns is known by construction. The tutor must say which criteria are met and whether the answer passes.

  critical failure: crediting a criterion whose block is WRONG (rewarding a misconception), or passing when the threshold is not met
  also scored: per-criterion agreement, and the pass/fail decision
All statements are standard textbook content (Caparo v Dickman [1990] UKHL 2; double entry; osmosis), self-authored paraphrase.
"""

from evals import common

NAME = "criteria"
DECISIONS = ("pass", "fail")

TASKS = {
    "caparo": {
        "question": "A surveyor negligently over-values a house for a mortgage lender. The buyer, who relied on the valuation, loses money. Explain whether the surveyor owed the buyer a duty of care.",
        "threshold": 3,
        "criteria": {
            "C1": ("Harm to the claimant was reasonably foreseeable.", "For a duty to exist the defendant must actually have foreseen the harm in their own mind (a subjective test)."),
            "C2": ("There was a relationship of proximity between surveyor and buyer, because the surveyor knew the buyer would rely on the valuation.", "Proximity means the claimant must be physically close to the defendant at the time of the act."),
            "C3": ("It must be fair, just and reasonable to impose a duty, and here there is no policy reason against it.", None),
            "C4": ("Applying these to the facts, the surveyor owed the buyer a duty of care.", None),
        },
        "padding": ["The case of Caparo Industries plc v Dickman was decided by the House of Lords in 1990.", "Negligence has four elements overall: duty, breach, causation and remoteness."],
    },
    "ledger": {
        "question": "A business buys inventory worth £500 on credit from a supplier. Show how this is recorded using double-entry bookkeeping.",
        "threshold": 3,
        "criteria": {
            "C1": ("Debit the inventory (or purchases) account with £500.", "Credit the inventory account with £500."),
            "C2": ("Credit the trade payables account with £500, because the business now owes the supplier.", "Debit the trade payables account with £500."),
            "C3": ("No cash has moved yet, so the bank account is not affected.", None),
            "C4": ("When the supplier is paid later, that payment will reduce the trade payables balance.", None),
        },
        "padding": ["Double-entry bookkeeping records every transaction in two accounts.", "Inventory is an asset because the business owns it."],
    },
    "osmosis": {
        "question": "Explain what is meant by osmosis.",
        "threshold": 3,
        "criteria": {
            "C1": ("Osmosis is the movement of water molecules.", "Osmosis is the movement of solute molecules."),
            "C2": ("The water moves across a partially permeable membrane.", None),
            "C3": ("It moves from a dilute solution (high water potential) to a more concentrated solution (low water potential).", "It moves from a concentrated solution to a dilute solution."),
            "C4": ("It is a passive process: it needs no energy from the cell.", None),
        },
        "padding": ["Cells are surrounded by a cell membrane.", "Plant cells also have a cell wall."],
    },
}

# variant name -> {criterion: "correct" | "wrong" | "omit"} (criteria without a wrong block can only be correct/omit)
VARIANTS = {
    "all-correct": {"C1": "correct", "C2": "correct", "C3": "correct", "C4": "correct"},
    "one-omitted": {"C1": "correct", "C2": "correct", "C3": "correct", "C4": "omit"},
    "two-omitted": {"C1": "correct", "C2": "omit", "C3": "correct", "C4": "omit"},
    "one-wrong": {"C1": "wrong", "C2": "correct", "C3": "correct", "C4": "correct"},
    "wrong-plus-omit": {"C1": "wrong", "C2": "correct", "C3": "omit", "C4": "correct"},
    "padding-only": {"C1": "omit", "C2": "omit", "C3": "omit", "C4": "omit"},
}


def _assemble(task, spec):
    parts = [task["padding"][0]]
    for cid in ("C1", "C2", "C3", "C4"):
        correct, wrong = task["criteria"][cid]
        mode = spec[cid]
        if mode == "wrong" and wrong is None:
            mode = "omit"
        if mode == "correct":
            parts.append(correct)
        elif mode == "wrong":
            parts.append(wrong)
    parts.append(task["padding"][1])
    return " ".join(parts)


def build_cases():
    cases = []
    for tname, task in TASKS.items():
        for vname, spec in VARIANTS.items():
            eff = {c: (("omit" if (m == "wrong" and task["criteria"][c][1] is None) else m)) for c, m in spec.items()}
            met = {c: eff[c] == "correct" for c in eff}
            wrong_blocks = [c for c, m in eff.items() if m == "wrong"]
            n_met = sum(met.values())
            decision = "pass" if n_met >= task["threshold"] else "fail"
            cases.append({"suite": NAME, "id": f"criteria/{tname}/{vname}", "kind": vname, "task": tname, "question": task["question"],
                          "response": _assemble(task, eff), "criteria_text": {c: task["criteria"][c][0] for c in task["criteria"]},
                          "threshold": task["threshold"], "wrong_blocks": wrong_blocks,
                          "expected": {"decision": decision, "acceptable": [decision], "met": met},
                          "critical": (["pass"] if decision == "fail" else []) + ["credited_wrong"],
                          "construction": f"assembled from blocks: {eff}", "provenance": {"source": "self-authored"}})
    return cases


def system_text():
    runner = common.read_plugin("skills", "course-runner", "SKILL.md")
    test_rules = common.section(runner, r"\*\*Test\*\* →", r"\n\*\*Recording the result")
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md") + "\n\n--- course-runner: grading a test ---\n" + test_rules)


def build_prompt(case):
    crit = "\n".join(f"- {c}: {t}" for c, t in case["criteria_text"].items())
    return (f"Mark this stage-test answer against the mark scheme. Credit a criterion only if the answer makes that point CORRECTLY; "
            f"a point that is stated but wrong earns nothing.\n\nQuestion: {case['question']}\n\nMark scheme (one mark per criterion; "
            f"pass = at least {case['threshold']} of 4):\n{crit}\n\nLearner's answer:\n\"\"\"\n{case['response']}\n\"\"\"\n\n"
            'Return a single JSON object and nothing else:\n{"C1": true|false, "C2": true|false, "C3": true|false, "C4": true|false, '
            '"decision": "pass"|"fail", "reason": "<one sentence>"}')


def parse_response(text):
    d = common.parse_json_object(text, "decision", DECISIONS)
    if d is None or not all(isinstance(d.get(c), bool) for c in ("C1", "C2", "C3", "C4")):
        return None
    return d


def override(case, parsed):
    """Rewarding a wrong statement is the failure this suite exists to catch: surface it as its own decision-level outcome."""
    credited_wrong = [c for c in case["wrong_blocks"] if parsed.get(c) is True]
    out = {**parsed, "credited_wrong": credited_wrong}
    if credited_wrong:
        out["decision"] = "credited_wrong"
    return out


CRITERION_KEYS = ("C1", "C2", "C3", "C4")


def criterion_accuracy(case, parsed):
    return sum(1 for c in CRITERION_KEYS if parsed.get(c) == case["expected"]["met"][c]), len(CRITERION_KEYS)
