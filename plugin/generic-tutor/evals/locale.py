"""
Locale suite (L-19): does the tutor follow the learner's spelling variant and, when a home language is set, gloss key terms in it?

Checked by CODE on the reply text, so no one marks anything.

  gb      profile locale en-GB: no American-only spellings (organize, analyze, color, behavior, center ...)
  us      profile locale en-US: no British-only spellings (organise, analyse, colour, behaviour, centre ...)
  gloss   home_language Spanish: at least one of the expected Spanish words for the topic's key term appears (a gloss in brackets or straight after the term)
  none    no locale and no home language: the explanation just has to contain its required concepts (no style is forced)

The learner's message is written in British spelling in every case, so a reply that merely copies the message fails the `us` case: the profile decides, not
the learner's typing. A reply that happens to use neither variant's marker words passes (it cannot be faulted); the asks invite words that have both forms.
"""
import re

from evals import common

NAME = "locale"
DECISIONS = ("meets", "misses")

GB = ["organise", "organised", "organising", "analyse", "analysed", "analysing", "colour", "colours", "behaviour", "behaviours", "centre", "centres",
      "recognise", "recognised", "summarise", "summarised", "practise", "realise", "realised", "emphasise", "emphasised", "minimise", "memorise",
      "favourite", "neighbour", "programme", "defence", "labelled", "travelling", "cancelled", "grey", "maths"]
US = ["organize", "organized", "organizing", "analyze", "analyzed", "analyzing", "color", "colors", "behavior", "behaviors", "center", "centers",
      "recognize", "recognized", "summarize", "summarized", "realize", "realized", "emphasize", "emphasized", "minimize", "memorize",
      "favorite", "neighbor", "defense", "labeled", "traveling", "canceled", "gray", "math"]

TOPICS = {
    "photosynthesis": {"topic": "photosynthesis", "concepts": [["light"], ["carbon dioxide"], ["glucose", "sugar"]], "es": ["clorofila", "fotosíntesis", "fotosintesis"]},
    "fractions": {"topic": "adding fractions with different denominators", "concepts": [["denominator", "bottom"], ["add"], ["numerator", "top"]],
                  "es": ["denominador", "numerador", "fracción", "fraccion"]},
    "depreciation": {"topic": "depreciation of a business asset", "concepts": [["asset"], ["cost"], ["year", "period"]], "es": ["depreciación", "depreciacion", "amortización", "amortizacion"]},
}
SETTINGS = {
    "gb": {"locale": "en-GB", "home_language": None},
    "us": {"locale": "en-US", "home_language": None},
    "gloss": {"locale": "en-GB", "home_language": "Spanish"},
    "none": {"locale": None, "home_language": None},
}


def words(text):
    return re.findall(r"[A-Za-zÀ-ÿ']+", text.lower())


def analyse(text, case):
    w = set(words(text))
    lower = text.lower()
    return {"gb_forms": sorted(w & set(GB)), "us_forms": sorted(w & set(US)),
            "gloss_found": [g for g in TOPICS[case["topic_id"]]["es"] if g in lower],
            "missing_concepts": [g[0] for g in TOPICS[case["topic_id"]]["concepts"] if not any(x in lower for x in g)]}


def violations(m, kind):
    v = [f"missing concept: {c}" for c in m["missing_concepts"]]
    if kind == "us" and m["gb_forms"]:
        v.append(f"British spelling in an en-US profile: {m['gb_forms']}")
    if kind == "gb" and m["us_forms"]:
        v.append(f"American spelling in an en-GB profile: {m['us_forms']}")
    if kind == "gloss" and not m["gloss_found"]:
        v.append("no Spanish gloss for the key term")
    if kind == "gloss" and m["us_forms"]:
        v.append(f"American spelling in an en-GB profile: {m['us_forms']}")
    return v


def build_cases():
    cases = []
    for tid, t in TOPICS.items():
        for kind in SETTINGS:
            cases.append({"suite": NAME, "id": f"locale/{tid}/{kind}", "kind": kind, "topic_id": tid, "topic": t["topic"], "setting": SETTINGS[kind],
                          "expected": {"decision": "meets", "acceptable": ["meets"]}, "critical": [],
                          "construction": "deterministic spelling and gloss checks on the reply", "provenance": {"source": "self-authored"}})
    return cases


def system_text():
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md"))


def build_prompt(case):
    s = case["setting"]
    profile = f"Learner profile: identity.locale = {s['locale'] or 'not set'}; identity.home_language = {s['home_language'] or 'not set'}."
    return (f"{profile} The learner is in the lesson phase of a stage.\n\n"
            f"Learner: Can you help me organise my revision and analyse my mistakes while I learn about {case['topic']}? "
            "Give me a short plan and the key idea, and tell me which colour of highlighter to use for what.\n\n"
            "Write your reply to the learner now (about 120-180 words). Reply with the text only, no preamble.")


def parse_response(text):
    return {"decision": "meets", "text": text} if text and text.strip() else None


def override(case, parsed):
    m = analyse(parsed["text"], case)
    v = violations(m, case["kind"])
    return {"decision": "misses" if v else "meets", "violations": v, "metrics": m}


def oracle_text(case, wrong=False):
    t = TOPICS[case["topic_id"]]
    concepts = " ".join(g[0] for g in t["concepts"])
    base = f"Here is a short plan for {t['topic']}. The key ideas are: {concepts}."
    if wrong:
        return base + (" Please organise your notes and analyse each colour." if case["kind"] in ("us", "gloss") else " Please organize and analyze each color.") \
            if case["kind"] != "none" else "Nothing useful."
    spelling = " Please organize your notes and analyze each color." if case["kind"] == "us" else " Please organise your notes and analyse each colour."
    gloss = f" ({t['es'][0]})" if case["kind"] == "gloss" else ""
    return base + gloss + spelling
