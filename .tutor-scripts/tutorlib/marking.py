"""
Script marking of keyed items (B-02.3, ADR 0012 class 1). A pure function: the same key and answer always give the same verdict,
and nothing here reads a file, the clock or a model.

A question in question_bank.json may carry an optional `key`:

  {"kind": "mcq",     "options": ["...", "..."], "correct": "B"}
  {"kind": "numeric", "value": "9.81", "tolerance": {"abs": "0.05"}  (or {"rel": "0.01"}; omitted = exact), "units": ["m/s^2", "m s^-2"]}
  {"kind": "short",   "accepted": ["photosynthesis"], "case_sensitive": false}

`mark(key, answer)` returns {"correct": True | False | None, "reason": code}. None means "cannot be marked by script" (empty or
ambiguous answer, such as "1,000" which is one thousand or one point zero); the caller asks the learner to rewrite it and records
nothing in the meantime. It never guesses.

Edge cases, each pinned by tests/test_marking.py:
  * numbers use Decimal, so 0.1 + 0.2 style drift cannot flip a verdict; the bounds are inclusive.
  * decimal comma ("9,81") and a unicode minus are accepted; "1,000" (one comma, three digits after) is ambiguous -> None.
  * a single dot is always a decimal point ("1.000" is one, as in UK notation); thousands separators are accepted when unambiguous
    ("1,000,000", "1.000.000", "1.000,5", "1,000.5"); a space between digit groups is not
    read as a separator (-> None) because "2 5" could be two answers.
  * units are matched exactly and case-sensitively (mA is not MA); a key with units needs one of them, a key without units
    refuses a trailing unit (-> None) rather than ignoring what the learner wrote. No unit conversion.
  * significant figures and rounding rules are not interpreted: a rounding requirement is expressed as a tolerance.
  * short answers: Unicode NFKC, case-folded unless case_sensitive, whitespace collapsed, surrounding quotes and trailing
    . , ; : ! ? removed; compared to each accepted answer the same way. No fuzzy matching: a near-miss spelling is False.
  * mcq: a letter (A, b, "(c)", "D.") or the exact option text, case-insensitive; more than one letter is False.
"""
import re
import unicodedata
from decimal import Decimal, InvalidOperation

KINDS = ("mcq", "numeric", "short")
LETTERS = "ABCDEFGHIJ"
MAX_OPTIONS = len(LETTERS)
_MINUS = "−‒–"
_NUM = re.compile(r"^([+-]?)((?:\d+[.,]?\d*|[.,]\d+)(?:[.,]\d+)*)(?:[eE]([+-]?\d+))?(.*)$")


def _dec(value):
    try:
        d = Decimal(str(value).strip())
    except InvalidOperation:
        return None
    return d if d.is_finite() else None


def check_key(key):
    """Problems with a key (empty list = well formed). Used by the course validators so a malformed key never reaches a learner."""
    if not isinstance(key, dict):
        return ["key must be an object"]
    kind = key.get("kind")
    if kind not in KINDS:
        return [f"key.kind must be one of {list(KINDS)}"]
    out = []
    if kind == "mcq":
        opts = key.get("options")
        if not isinstance(opts, list) or not 2 <= len(opts) <= MAX_OPTIONS or not all(isinstance(o, str) and o.strip() for o in opts):
            return [f"mcq needs 2 to {MAX_OPTIONS} non-empty text options"]
        if len({_norm_text(o, False) for o in opts}) != len(opts):
            out.append("two options read the same")
        if key.get("correct") not in list(LETTERS[:len(opts)]):
            out.append(f"mcq correct must be one of {list(LETTERS[:len(opts)])}")
    elif kind == "numeric":
        if _dec(key.get("value")) is None:
            out.append("numeric value must be a number (give it as text, e.g. \"9.81\")")
        tol = key.get("tolerance")
        if tol is not None:
            if not isinstance(tol, dict) or len(tol) != 1 or next(iter(tol)) not in ("abs", "rel"):
                out.append("tolerance must be {\"abs\": n} or {\"rel\": n}")
            else:
                t = _dec(next(iter(tol.values())))
                if t is None or t < 0:
                    out.append("tolerance must be a number of zero or more")
        units = key.get("units", [])
        if not isinstance(units, list) or not all(isinstance(u, str) and u.strip() and u == u.strip() for u in units):
            out.append("units must be a list of non-empty texts without outer spaces")
    else:
        acc = key.get("accepted")
        if not isinstance(acc, list) or not acc or not all(isinstance(a, str) and _norm_text(a, True) for a in acc):
            out.append("short needs a non-empty list of accepted answers")
        if "case_sensitive" in key and not isinstance(key["case_sensitive"], bool):
            out.append("case_sensitive must be true or false")
    return out


def _norm_text(text, case_sensitive):
    s = unicodedata.normalize("NFKC", str(text))
    s = " ".join(s.split())
    s = s.strip(" \"'“”‘’").rstrip(".,;:!? ")
    return s if case_sensitive else s.casefold()


def _result(correct, reason):
    return {"correct": correct, "reason": reason}


def mark(key, answer):
    problems = check_key(key)
    if problems:
        raise ValueError("; ".join(problems))
    if not isinstance(answer, str) or not answer.strip():
        return _result(None, "empty_answer")
    return {"mcq": _mark_mcq, "numeric": _mark_numeric, "short": _mark_short}[key["kind"]](key, answer)


def _mark_mcq(key, answer):
    opts, letters = key["options"], LETTERS[:len(key["options"])]
    text = unicodedata.normalize("NFKC", answer).strip()
    m = re.fullmatch(r"\(?\s*([A-Za-z])\s*[).:]?", text)
    if m and m.group(1).upper() in letters:
        return _result(m.group(1).upper() == key["correct"], "letter")
    folded = _norm_text(text, False)
    for letter, opt in zip(letters, opts, strict=True):
        if folded == _norm_text(opt, False):
            return _result(letter == key["correct"], "option_text")
    return _result(False, "not_an_option")


def _parse_number(text):
    """(Decimal, unit_text) or (None, reason)."""
    s = unicodedata.normalize("NFKC", text).strip()
    for ch in _MINUS:
        s = s.replace(ch, "-")
    m = _NUM.match(s)
    if not m:
        return None, "unparseable"
    sign, body, exp, rest = m.groups()
    if rest[:1].isspace() and rest.strip()[:1].isdigit():             # "1 000": digit groups split by a space
        return None, "ambiguous_separator"
    commas, dots = body.count(","), body.count(".")
    if commas and dots:
        dec_sep = "," if body.rfind(",") > body.rfind(".") else "."
        thou = "." if dec_sep == "," else ","
        head, _, tail = body.rpartition(dec_sep)
        if dec_sep in head or not all(len(g) == 3 for g in head.split(thou)[1:]) or not 1 <= len(head.split(thou)[0]) <= 3:
            return None, "ambiguous_separator"
        body = head.replace(thou, "") + "." + tail
    elif commas or dots:
        sep = "," if commas else "."
        parts = body.split(sep)
        if len(parts) > 2:                                           # 1,000,000 or 1.000.000: grouping, every later group of three
            if not all(len(g) == 3 for g in parts[1:]) or not 1 <= len(parts[0]) <= 3:
                return None, "ambiguous_separator"
            body = "".join(parts)
        elif sep == "," and len(parts[1]) == 3 and 1 <= len(parts[0]) <= 3 and parts[0].isdigit():
            return None, "ambiguous_separator"                       # "1,000": a thousand or one point zero
        else:
            body = parts[0] + "." + parts[1]
    d = _dec(sign + body + ("e" + exp if exp else ""))
    if d is None:
        return None, "unparseable"
    return d, rest.strip()


def _mark_numeric(key, answer):
    num, rest = _parse_number(answer)
    if num is None:
        return _result(None, rest)
    units = key.get("units", [])
    if units:
        if not rest:
            return _result(False, "missing_unit")
        if rest not in units:
            return _result(False, "wrong_unit")
    elif rest:
        return _result(None, "unexpected_text")
    target = _dec(key["value"])
    tol = key.get("tolerance")
    allowed = Decimal(0)
    if tol:
        kind, raw = next(iter(tol.items()))
        allowed = _dec(raw) * (abs(target) if kind == "rel" else 1)
    return _result(abs(num - target) <= allowed, "within_tolerance" if abs(num - target) <= allowed else "outside_tolerance")


def _mark_short(key, answer):
    cs = key.get("case_sensitive", False)
    given = _norm_text(answer, cs)
    if not given:
        return _result(None, "empty_answer")
    ok = any(given == _norm_text(a, cs) for a in key["accepted"])
    return _result(ok, "accepted" if ok else "no_match")
