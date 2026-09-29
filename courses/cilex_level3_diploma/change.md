# Change log - cilex_level3_diploma

## 2026-09-27 - built

Built against the CPQ Foundation Stage module specifications F1-F6 (version 2, updated July 2022) and the CPQ Foundation assessment overview, both read from cilex.org.uk. All six Foundation modules are mandatory, so no optional units were excluded. Scope is CPQ Foundation Stage only; CPQ Advanced Stage is a separate, more advanced course this one's syllabus is written to require as complete.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** 9 items across S02, S12, S16, S18, S21, S22, S23, S24 (two items) whose tag sums didn't match their declared marks:
- S02_The_English_Legal_System test.md item 1 (over by 1): removed an extraneous `B1` tag on a supporting-context sentence, folding it into the preceding point as explanatory text rather than a separately-credited mark.
- S12_Consideration_Intention_and_Capacity test.md item 2 (under by 2): the "shield, not a sword" explanation was worth `B2`, raised to `B4` to match its 8-mark total alongside the four `B1` requirement points.
- S16_Property_Foundations test.md item 2 (under by 1): the client due diligence point raised from `B1` to `B2` (it bundles identity verification and beneficial-ownership checking).
- S18_Conveyancing_Start_and_Title test.md item 2 (under by 2): four bundled examples under one `B2` tag expanded to one `B2` each with "-- any 2 examples for full marks".
- S21_Post_Completion, S22_Personal_Impact_and_Teamwork, S24_Client_Communication practice item 1 (each under by 2): "(any two of): <list>" bundled under a single `B2` expanded to one `B2` per listed item with "-- any 2 for full marks".
- S23_Client_Focus_Commercial_Awareness_Technology practice item 1 (under by 2): same pattern, expanded to `B1` per item ("-- any 3 for full marks").
- S24_Client_Communication test.md item 2 (over by 1): a fourth "(or) appropriate empathy..." alternative point was worth `B1` against three `B2` points; raised to `B2` to match the others and reframed as a fourth valid alternative ("-- any 3 for full marks") rather than a bolt-on extra mark.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full 50/50, `mark_scheme_check.py` 0 mismatches.
