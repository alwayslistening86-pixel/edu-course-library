"""
Accessibility suite (K-04 / L-18): do the profile's accessibility modes actually change how the tutor writes?

Checked by CODE on the reply text, so no one marks anything. A reply `meets` when every measurable rule of the active mode holds
AND the explanation still contains its required concepts (simplifying must not make it wrong or empty). Rules (see the mode
definitions in tutor-core):

  dyslexia_mode         average sentence <= 15 words, longest <= 25, paragraphs <= 3 sentences, no italics/underline markers,
                        no ALL-CAPS words (acronyms from the case's allow-list excepted), at least one numbered/bulleted step list
                        or short labelled chunks
  plain_language_mode   average sentence <= 18 words, longest <= 30, every technical term from the case's list is explained at
                        first use (a bracket or "which means/is" within 90 characters after it)
  both                  both sets
  screen_reader_mode    no tables, no emoji or decorative symbols or box-drawing/rules, no colour-only references ("the red part")
  none (control)        only the concept check - the tutor must not be forced into a style the learner did not ask for

Metrics are deliberately simple and transparent (they are proxies for readability, not clinical standards).
"""
import re

from evals import common

NAME = "accessibility"
DECISIONS = ("meets", "misses")

TOPICS = {
    "photosynthesis": {
        "ask": "Explain how photosynthesis works.",
        "concepts": [["light"], ["carbon dioxide"], ["glucose", "sugar"], ["oxygen"]],
        "terms": ["chlorophyll"], "acronyms": [],
    },
    "contract": {
        "ask": "Explain what makes a contract legally binding.",
        "concepts": [["offer"], ["acceptance", "accepts", "accepted", "agrees to", "agree to"], ["consideration"], ["intention"]],
        "terms": ["consideration"], "acronyms": [],
    },
    "fractions": {
        "ask": "Explain how to add two fractions with different denominators.",
        "concepts": [["common denominator", "same denominator", "common multiple", "bottom numbers match", "same bottom number", "bottom number the same", "same number on the bottom"], ["numerator", "top number", "top part", "tops"], ["add"]],
        "terms": ["denominator"], "acronyms": [],
    },
    "mitosis": {
        "ask": "Compare mitosis and meiosis.",
        "concepts": [["mitosis"], ["meiosis"], ["two"], ["four"]],
        "terms": [], "acronyms": [],
    },
}
MODES = {
    "dyslexia": {"dyslexia_mode": True, "plain_language_mode": False, "screen_reader_mode": False},
    "plain": {"dyslexia_mode": False, "plain_language_mode": True, "screen_reader_mode": False},
    "both": {"dyslexia_mode": True, "plain_language_mode": True, "screen_reader_mode": False},
    "reader": {"dyslexia_mode": False, "plain_language_mode": False, "screen_reader_mode": True},
    "none": {"dyslexia_mode": False, "plain_language_mode": False, "screen_reader_mode": False},
}
_TABLE = re.compile(r"^\s*\|.*\|\s*$|^\s*\|?\s*:?-{3,}:?\s*\|", re.M)
_DECOR = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2190-\u21FF\u2500-\u259F]|^\\s*(?:[-_*=]{3,})\\s*$", re.M)
_COLOUR = re.compile(r"\b(?:red|green|blue|yellow|orange|purple|pink)\s+(?:line|text|part|box|arrow|bar|section|word|area)s?\b|\b(?:highlighted|shown|marked) in (?:red|green|blue|yellow|orange|purple|pink)\b", re.I)


def sentences(text):
    flat = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s+", "", text, flags=re.M)        # list markers are not sentence words
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+|\n+", flat) if p.strip()]
    return [p for p in parts if re.search(r"[A-Za-z]", p)]


def words(s):
    return re.findall(r"[A-Za-z0-9'£%-]+", s)


def analyse(text, case):
    sents = sentences(text)
    counts = [len(words(s)) for s in sents] or [0]
    units = []                                              # every blank-line block, and every list item inside it, is a "paragraph"
    for block in re.split(r"\n\s*\n", text.strip()):
        items = re.split(r"\n(?=\s*(?:[-*•]|\d+[.)])\s)", block)
        units += [i for i in items if i.strip()]
    para_sents = [len(sentences(u)) for u in units] or [0]
    caps = [w for w in re.findall(r"\b[A-Z]{4,}\b", text) if w not in case["acronyms"]]
    italics = len(re.findall(r"(?<!\*)\*(?!\*)[^*\n]+\*(?!\*)|(?<!_)_(?!_)[^_\n]+_(?!_)|<u>|<em>|<i>", text))
    has_steps = bool(re.search(r"^\s*(?:\d+[.)]|[-*•])\s+", text, re.M))
    plain = re.sub(r"(\*\*|__)", "", text)               # bold markers must not hide "Term** (explanation)"
    lower = text.lower()
    missing = [group[0] for group in case["concepts"] if not any(g in lower for g in group)]
    unexplained = []
    for term in case["terms"]:
        m = re.search(re.escape(term), plain, re.I)
        if m:
            after = plain[m.end(): m.end() + 90]
            before = plain[max(0, m.start() - 90): m.start()]
            if not (re.match(r"\s*[\(,:—-]", after) or re.search(r"\b(which|that|this)\s+(is|means|are)\b|\bmeans\b|\bis (the|a|an)\b", after, re.I)
                    or re.search(r"\bcalled\s*$|\bknown as\s*$|\(\s*$", before, re.I)):
                unexplained.append(term)
    return {"avg_sentence_words": round(sum(counts) / len(counts), 1), "max_sentence_words": max(counts),
            "max_paragraph_sentences": max(para_sents), "caps_words": caps, "italic_markers": italics, "has_steps": has_steps,
            "missing_concepts": missing, "unexplained_terms": unexplained,
            "table_lines": len(_TABLE.findall(text)), "decorative": len(_DECOR.findall(text)), "colour_only": len(_COLOUR.findall(text))}


def violations(m, mode):
    flags = MODES[mode]
    v = [f"missing concept: {c}" for c in m["missing_concepts"]]
    if flags["dyslexia_mode"]:
        if m["avg_sentence_words"] > 15:
            v.append(f"average sentence {m['avg_sentence_words']} words (> 15)")
        if m["max_sentence_words"] > 25:
            v.append(f"longest sentence {m['max_sentence_words']} words (> 25)")
        if m["max_paragraph_sentences"] > 3:
            v.append(f"paragraph of {m['max_paragraph_sentences']} sentences (> 3)")
        if m["italic_markers"]:
            v.append("italics/underline used")
        if m["caps_words"]:
            v.append(f"ALL-CAPS words: {m['caps_words']}")
        if not m["has_steps"]:
            v.append("no numbered/bulleted steps")
    if flags["screen_reader_mode"]:
        if m["table_lines"]:
            v.append("table used (a screen reader reads it cell by cell)")
        if m["decorative"]:
            v.append("emoji, decorative symbol, arrow or rule line used")
        if m["colour_only"]:
            v.append("something identified by colour alone")
    if flags["plain_language_mode"]:
        if m["avg_sentence_words"] > 18:
            v.append(f"average sentence {m['avg_sentence_words']} words (> 18)")
        if m["max_sentence_words"] > 30:
            v.append(f"longest sentence {m['max_sentence_words']} words (> 30)")
        if m["unexplained_terms"]:
            v.append(f"technical term not explained at first use: {m['unexplained_terms']}")
    return v


def build_cases():
    cases = []
    for tname, t in TOPICS.items():
        for mname in MODES:
            cases.append({"suite": NAME, "id": f"accessibility/{tname}/{mname}", "kind": mname, "topic": tname, "mode": mname,
                          "ask": t["ask"], "concepts": t["concepts"], "terms": t["terms"], "acronyms": t["acronyms"],
                          "expected": {"decision": "meets", "acceptable": ["meets"]}, "critical": [],
                          "construction": "deterministic text metrics on the reply", "provenance": {"source": "self-authored"}})
    return cases


def system_text():
    return ("You are the tutor described by the following plugin text. Follow its rules exactly.\n\n"
            + common.read_plugin("skills", "tutor-core", "SKILL.md"))


def build_prompt(case):
    flags = MODES[case["mode"]]
    return (f"Learner profile (preferences.accessibility): dyslexia_mode = {str(flags['dyslexia_mode']).lower()}, "
            f"plain_language_mode = {str(flags['plain_language_mode']).lower()}, screen_reader_mode = {str(flags['screen_reader_mode']).lower()}. The learner is in the lesson phase of a stage.\n\n"
            f"Learner: {case['ask']}\n\nWrite your reply to the learner now (the lesson explanation only, about 120-200 words). "
            "Reply with the explanation text only, with no preamble.")


def parse_response(text):
    # filled in per case by override(); a non-empty reply is "parsed"
    return {"decision": "meets", "text": text} if text and text.strip() else None


def override(case, parsed):
    m = analyse(parsed["text"], case)
    v = violations(m, case["mode"])
    return {"decision": "misses" if v else "meets", "violations": v, "metrics": m}


GOLD = {
    "photosynthesis": ("Plants make their own food. This is called photosynthesis.\n\n"
                       "1. The leaf takes in carbon dioxide from the air.\n2. The roots take in water from the soil.\n"
                       "3. Chlorophyll (the green stuff in leaves) catches light.\n"
                       "4. The plant uses the light to make glucose, a sugar.\n5. It gives out oxygen."),
    "contract": ("A contract is a promise the law will enforce. It needs four things.\n\n"
                 "1. An offer: one person says what they will do.\n2. Acceptance: the other person agrees to it.\n"
                 "3. Consideration (something of value each side gives, such as money) must pass between them.\n"
                 "4. Intention: both sides mean it to be legally binding."),
    "fractions": ("To add fractions, the bottom numbers must match.\n\n"
                  "1. Find a common denominator (a number both bottom numbers go into).\n"
                  "2. Change each fraction to use that bottom number.\n3. Keep the bottom number the same.\n"
                  "4. Add the numerator (the top number) of each fraction.\n5. Simplify the answer if you can."),
}
GOLD["mitosis"] = ("Mitosis and meiosis are two ways a cell divides.\n\n"
                   "1. Mitosis makes two identical cells. It is used for growth and repair.\n"
                   "2. Meiosis makes four different cells. They are the sex cells (gametes).\n"
                   "3. Mitosis divides once. Meiosis divides twice.")
WRONG = ("PHOTOSYNTHESIS is *fundamentally* a multi-stage biochemical process by which autotrophic organisms, encompassing terrestrial and aquatic "
         "plants as well as certain bacteria, transduce electromagnetic radiation into chemical potential energy stored in carbohydrate molecules, "
         "a phenomenon that requires consideration of numerous interacting variables and that is discussed at length in advanced texts, "
         "including the role of various pigments, enzymes and membrane-bound complexes within specialised organelles, and the net result is that "
         "organisms produce sugars while releasing a gaseous by-product into the surrounding atmosphere in a manner that sustains most life on earth.")


def oracle_text(case, wrong=False):
    return WRONG if wrong else GOLD[case["topic"]]
