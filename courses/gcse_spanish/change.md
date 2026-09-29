# Change log - gcse_spanish

## 2026-09-27 - built

Built against AQA 8692, first teaching September 2024. Standalone GCSE; no prerequisite. Built to Higher-tier demand throughout.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** the same systematic pattern independently found and fixed in `gcse_german` (both courses were built from the same lesson template). Most 6-mark three-part (a)/(b)/(c) reading-comprehension items under-tagged one sub-answer at `B1` (1 mark) when AQA's real convention for this question type credits each sub-answer 2 marks; raised to `B2` in exam/exam.md item 1, S02_Vida_sana, S03_Estudios_y_trabajo, S04_Tiempo_libre, S08_Medios_y_tecnologia, S09_Medio_ambiente_y_vivienda (two sub-answers), S10_Futuro_condicional_imperativo, S11_Subjuntivo_y_estructuras_avanzadas (all test.md item 1). Also fixed: S06_Cultura_de_famosos test.md item 3 (8-mark translation, under-tagged by 1 -- added an 8th tag for accurate spelling/word order); S01_Identidad_y_relaciones practice item 2 (declared `[1 mark]` for filling two separate blanks, each correctly tagged `B1` -- the declared-marks bracket itself was wrong, corrected to `[2 marks]`); S03_Estudios_y_trabajo practice item 1 (declared `[2 marks]` for three separate adverb-formation sub-answers, each correctly tagged `B1` -- corrected to `[3 marks]`).

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full 39/39, `mark_scheme_check.py` 0 mismatches.
