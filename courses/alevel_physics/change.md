# Change log - alevel_physics

## 2026-09-27 - built

Built against AQA 7408 Version 1.4 (July 2026), Astrophysics option. Requires GCSE Physics or Combined Science, and GCSE Mathematics.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** two items using the same "B1 each, up to N:" single-tag shorthand as the alevel_chemistry fix above (S13_Thermal_Physics test.md item 3, "state four assumptions of the kinetic theory", 4 marks; S22_Practical_Skills_and_Data_Analysis test.md item 5, "give three rules for plotting a graph", 3 marks). Both rewritten with one tag per listed item and an explicit "-- any N for full marks" note.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full (140/216 taught, 76 pre-existing declared-out-of-scope items unchanged), `mark_scheme_check.py` 0 mismatches.
