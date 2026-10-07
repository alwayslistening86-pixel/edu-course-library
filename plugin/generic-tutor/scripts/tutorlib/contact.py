"""
Free text a script is about to store must not carry a way to contact someone (ADR 0012, scenario S5).

This catches the obvious forms only: an email address, a web address, and a phone-style number (a run of nine or more digits that
starts with 0 or +, spaces and hyphens allowed). It cannot catch a name, a school, an address or a disclosure; those remain a
matter for the rules the tutor is given (tutor-core's wellbeing rule). It exists to stop the most direct leak and to give the
caller a plain reason, not to promise that stored text is free of personal data.
"""
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
URL = re.compile(r"(?:https?://|www\.)\S+", re.I)
PHONE = re.compile(r"(?<![\w.])(?:\+|0)\d[\d\s-]{7,}\d(?!\w)")


def contact_details(text):
    """Kinds of contact detail found in `text`: any of "email address", "web address", "phone number" (never the value itself)."""
    found = []
    if EMAIL.search(text):
        found.append("email address")
    if URL.search(text):
        found.append("web address")
    if any(len(re.sub(r"\D", "", m.group(0))) >= 9 for m in PHONE.finditer(text)):
        found.append("phone number")
    return found
