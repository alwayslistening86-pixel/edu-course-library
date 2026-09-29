# Change log - aat_level2_certificate

## 2026-09-27 - built

Built against AAT Level 2 Certificate in Accounting (603/6338/1) Version 5.6 (published 1 September 2026). Standalone; no prerequisite.

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** the new `.tutor-scripts/mark_scheme_check.py` checker (installed 2026-09-28), run for the first time across the whole library rather than just the course being built. It sums each item's M/A/B mark tags and compares the total to the item's declared `[N marks]`.

**Fixed:** 7 "list/state N of..." items (S02_IB_Customer_Invoices already clean; S03_IB_Customer_Receipts item 1, S04_IB_Supplier_Invoices item 1, S05_IB_Supplier_Payments item 2, S10_PBC_Journal_Transactions item 3, S19_BE_External_Environment practice item 1, S22_BE_Finance_Function practice item 1, S24_BE_Information_and_Security practice item 1) each declared `[N marks]` for "any N of: <list>" but carried only a single `B1` tag (1 mark) rather than one `B1` per list option. Rewritten with one `B1` per option and an explicit "-- any N for full marks" note, matching the flexible-credit convention already used elsewhere in this course (e.g. S02_IB_Customer_Invoices item 5).

**Investigated, not a bug:** S17_PC_Budgets_Variances_Tools test.md item 4 (spreadsheet-formula question) is still flagged by the checker but is confirmed correct by hand -- its two real `B1` tags sum to the declared 2 marks. The checker's tag-detector mistakes the cell references "B2" and "B8" mentioned in the item's own explanatory prose ("...not the whole range B2 to B8") for mark tags; this is a documented, narrow false-positive in the checker itself (see its own docstring), not a defect in this item. No change made.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full 63/63, `mark_scheme_check.py` 0 real mismatches (the one residual flag above is a confirmed checker false positive).
