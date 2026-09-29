# Change log - gcse_computer_science

## 2026-09-27 - built

Built against AQA GCSE Computer Science (8525) Version 1.2 (29 November 2022). Standalone; no prerequisite.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** S19_Hardware_Software_Classification test.md item 3 ("describe two functions of an operating system", 4 marks) listed five candidate functions under a single `B2` tag rather than crediting each candidate its own tag. Rewritten with one `B2` per function and an explicit "-- any 2 for full marks (2 marks each: named function plus brief explanation)" note.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full 41/41, `mark_scheme_check.py` 0 mismatches.
