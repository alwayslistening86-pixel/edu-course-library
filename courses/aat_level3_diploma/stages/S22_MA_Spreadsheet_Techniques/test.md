# S22_MA_Spreadsheet_Techniques - Test: Spreadsheet techniques for management accounting information

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry and financial-statement questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain how the SUMIF function could be used to find total material cost for one specific cost centre out of a large spreadsheet listing many cost centres. [2 marks]
2. State two checks that should be carried out on a spreadsheet before relying on its output for a management report. [2 marks]
3. Which spreadsheet feature would best show total cost by cost centre and by month at a glance, without writing a separate formula for every combination? Choose every correct option.
   A. A pivot table
   B. A single SUM formula
   C. Sorting the data alphabetically
   D. A single VLOOKUP formula
4. Explain why filtering a spreadsheet, rather than sorting it, would be the more appropriate tool to isolate only the variances above a certain size for investigation. [2 marks]

## Answer key (for the tutor only)
1. [2] B1 SUMIF sums a range of values but only for rows meeting a specified criterion; B1 here, the criterion would be the cost centre name/code, so it totals only the material cost figures where the cost centre column matches the one being analysed.
2. [2] B1 formulas reference the correct cells/ranges; B1 totals reconcile to an independent check; B1 no rows or data have been accidentally excluded from a filter, sum range or pivot table; B1 figures are consistent with expectations (reasonableness check) -- any 2 for full marks.
3. Correct: A (exactly these options, no others)
4. [2] B1 sorting reorders all the data (e.g. largest to smallest) but keeps every row visible; B1 filtering narrows the visible data down to only the rows meeting a chosen condition (e.g. variance greater than a set amount), which is more directly suited to isolating specific items for investigation.

## Grading
Apply `rubric.json`'s `stage_rubrics.S22_MA_Spreadsheet_Techniques` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 7 marks in all; a pass needs at least 5 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S23_MA_Short_Term_Decision_Making.
