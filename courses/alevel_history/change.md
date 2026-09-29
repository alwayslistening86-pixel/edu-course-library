# Change log - alevel_history

## 2026-09-27 - built

Built against Edexcel 9HI0 Issue 3, Route B (1B + 2B.1) and Paper 3 Topic 31 (Pilgrimage of Grace and Kett's Rebellion as the in-depth studies). Requires GCSE History. Coursework/NEA declared out of scope.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** four practice/test items whose tag sums didn't match their declared marks, all "give/explain two/N ways..." style questions where the answer key listed more candidate answers than marks tags credited:
- S01_Monarchy_and_Government practice item 1 ("two ways Parliament's role changed", 4 marks): rewritten as three `B2` alternatives (any 2 developed points for full marks), replacing an inconsistent mix of `B1`/`B1`/`B1`/`B2` tags that summed to 5, not 4.
- S02_Religious_Change_Henry_to_Mary practice item 1 ("two statutes... and what each did", 4 marks): the two statutes were each worth `B1` (summing to 2, not 4); changed to `B2` each to match "name and explain" for 4 marks total.
- S05_Economy_Society_Culture_and_Interpretations practice item 1 ("two effects of the dissolution", 4 marks): same fix, `B1` each raised to `B2` each.
- S10_Breadth_Government_and_Resistance test.md item 1 ("explain two ways... developed", 6 marks): four candidate developments were each worth `B1` (summing to 4, not 6); changed to `B3` each with an explicit "any 2 for full marks" note, since the question only wants two of the four explained.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full 41/41, `mark_scheme_check.py` 0 mismatches.
