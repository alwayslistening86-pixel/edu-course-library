# Change log - alevel_chemistry

## 2026-09-27 - built

Built against AQA 7405 Version 1.2 (July 2026). Requires GCSE Chemistry or Combined Science, and GCSE Mathematics.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** S25_Practical_Skills_and_Data_Analysis test.md item 5 declared `[3]` for "give three features of a well-plotted graph" but its answer key wrote "B1 each, up to 3:" once, followed by five candidate features, rather than tagging each feature. Rewritten with one `B1` per feature and an explicit "-- any 3 for full marks" note.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full (134/146 taught, 12 pre-existing declared-out-of-scope items unchanged), `mark_scheme_check.py` 0 mismatches.
