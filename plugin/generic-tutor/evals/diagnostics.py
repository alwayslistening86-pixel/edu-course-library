"""
Diagnostic suite (A-04): given a learner's wrong answer and what they said when asked how they got it, does the tutor
classify the cause the way tutor-core and course-runner define it?

Authoring note: a first draft had two `misapplied_procedure` scenarios ("(x+3)^2 -> x^2+9, I squared each term" and "20% of 150 -> 0.2,
I didn't know what to do next") that the model classified, unanimously, as a misconception and a missing prerequisite. Both readings
are defensible, so the SCENARIOS were wrong, not the model: each was replaced with one where the learner states a single mechanism
(a named procedure with a stated omitted/wrong step). The rule going forward (A-06): when samples agree with each other against the
label, re-read the scenario for ambiguity before blaming the tutor; never tune a scenario toward the model's answer without that reason.

Scenarios are written by construction: each one is built to embody exactly one cause (the explanation the learner gives is
the mechanism), so the label is known without any marker. Three scenarios per cause; the five causes are the plugin's own
taxonomy (error_log.CAUSES).

  slip                   knew it, wrote/typed something else
  missing_prerequisite   cannot do an earlier skill the step needs
  misconception          a systematic wrong belief about how something works
  misapplied_procedure   right idea, wrong or incomplete algorithm
  comprehension          misread or misunderstood what was asked
"""
from evals import common

NAME = "diagnostics"
DECISIONS = ("slip", "missing_prerequisite", "misconception", "misapplied_procedure", "comprehension")

SCENARIOS = [
    ("slip", "Solve 4x = 36.", "x = 8", "Oh no, I did 36 divided by 4 in my head and got 9, I just wrote 8 by mistake. I know it's 9."),
    ("slip", "Add 47 and 38.", "75", "I carried the one but forgot to add it. I do this all the time, I know how to add."),
    ("slip", "Write 3/4 as a decimal.", "0.57", "I meant 0.75, my finger hit the wrong number - I know 3 divided by 4 is 0.75."),
    ("missing_prerequisite", "Solve 2/3 + 1/4.", "3/7", "I just added the tops and added the bottoms. Actually I never understood how to find a common denominator."),
    ("missing_prerequisite", "Find the gradient of the line through (1, 2) and (3, 8).", "6", "I'm not sure how you subtract negative numbers or even what gradient means; we hadn't done fractions of change before this."),
    ("missing_prerequisite", "Factorise x^2 + 5x + 6.", "x(x + 5) + 6", "I don't really know my times tables so I couldn't find numbers that multiply to 6 and add to 5."),
    ("misconception", "Which is bigger, 0.8 or 0.65?", "0.65", "0.65 has more digits so it must be the bigger number."),
    ("misconception", "What is 3 x 1/2?", "6", "Multiplying always makes the number bigger so it has to be more than 3 - I did 3 times 2."),
    ("misconception", "Is the sum of two odd numbers odd or even?", "odd", "Odd plus odd is odd because odd numbers are odd, so adding them keeps them odd."),
    ("misapplied_procedure", "Expand (x + 3)(x + 2).", "x^2 + 6", "I used the FOIL method but only did the first terms and the last terms, x times x and 3 times 2, and skipped the outside and inside ones."),
    ("misapplied_procedure", "Find the mean of 4, 8 and 12.", "2", "I added them up to get 24 and then divided by the biggest number, 12, instead of by how many numbers there are."),
    ("misapplied_procedure", "Solve 3x + 5 = 20.", "x = 25/3", "I added 5 to both sides to get 3x = 25, then divided by 3. That's the balancing method."),
    ("comprehension", "A shop sells pens at 3 for £1.20. How much do 12 pens cost?", "£0.40", "I thought it was asking for the price of one pen."),
    ("comprehension", "Find the perimeter of a square with area 49 cm^2.", "49", "I read it as 'find the area' because the number 49 is in the question."),
    ("comprehension", "Give your answer to 2 decimal places: 7 / 3.", "2", "I didn't see where it said how many decimals, I just rounded to the nearest whole number."),
]


def build_cases():
    out = []
    for n, (cause, q, ans, expl) in enumerate(SCENARIOS, 1):
        out.append({"suite": NAME, "id": f"diagnostics/{cause}/{n:02d}", "kind": cause, "question": q, "answer": ans, "explanation": expl,
                    "expected": {"decision": cause, "acceptable": [cause]}, "critical": [],
                    "construction": "scenario written to embody exactly this cause", "provenance": {"source": "self-authored"}})
    return out


def system_text():
    runner = common.read_plugin("skills", "course-runner", "SKILL.md")
    diag = common.section(runner, r"## Diagnosing during practice", r"\n## What this costs")
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md") + "\n\n--- course-runner ---\n" + diag)


def build_prompt(case):
    return (f"During practice a learner answered a question wrongly. You asked how they got their answer (elicit before explaining).\n\n"
            f"Question: {case['question']}\nLearner's answer: {case['answer']}\nLearner's explanation: \"{case['explanation']}\"\n\n"
            "Classify the cause using the plugin's taxonomy. Return a single JSON object and nothing else:\n"
            '{"decision": "slip"|"missing_prerequisite"|"misconception"|"misapplied_procedure"|"comprehension", "reason": "<one sentence>"}')


def parse_response(text):
    return common.parse_json_object(text, "decision", DECISIONS)
