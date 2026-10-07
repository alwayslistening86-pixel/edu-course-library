"""
Test-integrity overlap checks (A-07, K-26): a stage's test must not be available to the learner beforehand.

`test_items` pulls the graded items out of a stage's test.md (a "Test items" list, or a single "Test scenario"/"Test question").
`verbatim_items` reports which of them appear, whole, in other text (practice, lesson, a take-home worksheet). `long_runs` reports
shared runs of N consecutive words, an advisory signal only: templated stems and shared data tables legitimately repeat.
Whole-item matching is exact after lower-casing and dropping punctuation; on the 1,253 real stages it finds none, so a hit is real.
"""
import re

MIN_ITEM_CHARS = 25
_SECTIONS = r"(?:Test items|Test scenario|Test question|Scenario)"


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def _section(text):
    m = re.search(r"^##\s+" + _SECTIONS + r"[^\n]*\n(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def test_items(test_md_text):
    """Normalised text of each graded item (numbered items, else the whole scenario)."""
    sec = _section(test_md_text)
    parts = re.split(r"^\s*\d+[.)]\s", sec, flags=re.M)[1:]
    items = [norm(p) for p in parts if len(norm(p)) >= MIN_ITEM_CHARS]
    if not items and len(norm(sec)) >= MIN_ITEM_CHARS:
        items = [norm(sec)]
    return items


def verbatim_items(items, other_text):
    """Items (normalised) that appear whole inside `other_text`."""
    hay = norm(other_text)
    return [it for it in items if it in hay]


def long_runs(a_text, b_text, n=20):
    """Number of distinct n-word runs shared by the two texts."""
    def grams(t):
        w = norm(t).split()
        return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}
    return len(grams(a_text) & grams(b_text))
