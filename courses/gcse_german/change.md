# Change log - gcse_german

## 2026-09-27 - built

Built against AQA 8662, first teaching September 2024. Standalone GCSE; no prerequisite. Built to Higher-tier demand throughout.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** a systematic pattern across the three-part (a)/(b)/(c) reading-comprehension items, mirroring the same pattern independently found and fixed in `gcse_spanish` (both courses were built from the same lesson template). Most 6-mark three-part items under-tagged one sub-answer at `B1` (1 mark) when AQA's real convention for this question type credits each sub-answer 2 marks; raised to `B2` in exam/exam.md item 1, S02_Gesundes_Leben, S03_Schule_und_Arbeit, S04_Freizeit, S08_Medien_und_Technologie, S09_Umwelt_und_Wohnen (two sub-answers), S10_Vergangenheit_und_Imperativ, S11_Hoehere_Strukturen (all test.md item 1). Also fixed: exam/exam.md item 4 (10-mark translation, under-tagged by 1 -- the closing "natural, accurate German overall" mark raised from `B1` to `B2`); S06_Promikultur test.md item 3 (8-mark translation, under-tagged by 1 -- added an 8th tag for accurate spelling/word order); S01_Identitaet_und_Beziehungen practice item 2 (declared `[1 mark]` for filling two separate blanks, each correctly tagged `B1` -- the declared-marks bracket itself was wrong, corrected to `[2 marks]`, matching the identical fix in `gcse_spanish`).

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full 39/39, `mark_scheme_check.py` 0 mismatches.
