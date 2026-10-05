"""
Recheck suite (K-08): given what a course recorded and what the live source now says, does the tutor judge "material change"
by the course-runner's three criteria (version/issue, graded criteria or threshold, syllabus items added/removed/moved) and not
by wording, layout or hosting changes?

Cases are built by construction: each pair is one change of one kind, so the label is known without any marker.
A missed material change is the critical failure (the learner would study to a stale specification); a false alarm is not.
"""
from evals import common

NAME = "recheck"
DECISIONS = ("material", "not_material")

# (material?, what the course recorded, what the live source now shows)
CASES = [
    (True, "Specification: AQA 7408 Version 1.4, July 2026.", "Specification: AQA 7408 Version 1.5, September 2026."),
    (True, "Stage S4 pass threshold in rubric.json: 60% of marks.", "The current mark scheme sets the pass-equivalent for this component at 50% of marks."),
    (True, "Stage S6 criterion: 'shows working so method marks are awarded'.", "Method marks have been removed from this component; only the final answer is credited."),
    (True, "Itemised syllabus lists 40 items for the stage group, ending at 3.2.3.", "The specification now lists a new item 3.2.4 (gene editing) in the same section."),
    (True, "Itemised syllabus includes item 4.1.2 'Redox half-equations'.", "Item 4.1.2 no longer appears in the specification; it has been withdrawn."),
    (True, "Item 3.1.5 'Equilibrium constants' sits in section 3.1.", "Item 3.1.5 'Equilibrium constants' has moved to section 3.2 in the current specification."),
    (True, "Paper 2 is worth 80 marks and examined for 1 hour 30 minutes.", "Paper 2 is now worth 100 marks and examined for 2 hours."),
    (False, "Specification PDF at example.org/spec-v1-4.pdf, Version 1.4, July 2026.", "The same Version 1.4 (July 2026) PDF is now hosted at example.org/downloads/spec.pdf."),
    (False, "Item 2.3.1 titled 'Atomic structure' covering protons, neutrons and electrons.", "Item 2.3.1 is now titled 'Structure of the atom' with the same description and code."),
    (False, "Specification Version 1.4, July 2026, file name spec-final.pdf.", "Same Version 1.4, July 2026, now with the file name spec-final-v2.pdf and an identical issue statement."),
    (False, "Spec text: 'Candidates should be able to calcualte the mean'.", "Spec text: 'Candidates should be able to calculate the mean' (a spelling correction; nothing else differs)."),
    (False, "Specification Version 1.4, July 2026.", "Specification Version 1.4, July 2026, with a new cover page carrying a 2026 copyright line; all content and the version are unchanged."),
    (False, "Grade boundaries and criteria tables laid out as three columns.", "The same criteria tables now laid out as two columns; every criterion and threshold is identical."),
    (False, "The exam board's qualification page, with the specification linked.", "The board has restyled its website; the linked specification document and its version are unchanged."),
]


def build_cases():
    out = []
    for n, (material, recorded, live) in enumerate(CASES, 1):
        label = "material" if material else "not_material"
        out.append({"suite": NAME, "id": f"recheck/{label}/{n:02d}", "kind": label, "recorded": recorded, "live": live,
                    "expected": {"decision": label, "acceptable": [label]}, "critical": ["not_material"] if material else [],
                    "construction": "one change of one kind, labelled by the runner's criteria", "provenance": {"source": "self-authored"}})
    return out


def system_text():
    runner = common.read_plugin("skills", "course-runner", "SKILL.md")
    sec = common.section(runner, r"## Live recheck gating", r"\n## Untrusted content during the live recheck")
    return "You are the tutor described by the following plugin text. Follow its rules exactly.\n\n--- course-runner (live recheck) ---\n" + sec + ("\n" * 1) + (common.read_plugin("skills", "tutor-core", "SKILL.md")[:3000])


def build_prompt(case):
    return ("You are running the live recheck for a course. The course recorded this:\n"
            f"  {case['recorded']}\n\nThe live source now shows:\n  {case['live']}\n\n"
            "Is this a material change under the plugin's recheck procedure? Return a single JSON object and nothing else:\n"
            '{"decision": "material"|"not_material", "reason": "<one sentence>"}')


def parse_response(text):
    return common.parse_json_object(text, "decision", DECISIONS)
