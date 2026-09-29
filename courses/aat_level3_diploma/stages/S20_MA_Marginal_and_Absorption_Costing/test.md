# S20_MA_Marginal_and_Absorption_Costing - Test: Marginal vs absorption costing and reconciling reported profit

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry and financial-statement questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Selling price £70/unit, variable cost £42/unit, fixed production overhead £24,000 for budgeted output of 2,000 units, fixed selling/admin costs £8,000. 2,000 units are produced and 1,850 are sold. Calculate the profit under marginal costing. [4 marks]
2. Using the same figures (selling price £70/unit, variable cost £42/unit, fixed production OAR = 24,000/2,000 = £12/unit, fixed selling/admin £8,000, 2,000 produced, 1,850 sold), calculate the profit under absorption costing. [4 marks]
3. Reconcile the two profit figures from the previous two questions (marginal £19,800, absorption £21,600), explaining the £1,800 difference. [2 marks]
4. If sales exceed production in a period (inventory falls), which costing method reports the higher profit? Choose every correct option.
   A. Marginal costing
   B. Absorption costing
   C. Both report identical profit
   D. Neither -- profit cannot be compared

## Answer key (for the tutor only)
1. [4] M1 contribution = 1,850 x (70-42) = 1,850 x 28 = £51,800; M1 fixed costs = 24,000 + 8,000 = £32,000; A1 profit = 51,800 - 32,000 = £19,800; B1 correctly excluding fixed production overhead from the unit contribution calculation.
2. [4] M1 cost of sales = 1,850 x (42+12) = 1,850 x 54 = £99,900; M1 gross profit = (1,850 x 70) - 99,900 = 129,500 - 99,900 = £29,600; A1 profit after fixed selling/admin = 29,600 - 8,000 = £21,600; B1 correct treatment: fixed production overhead is absorbed into unit cost, but fixed selling/admin remains a period cost deducted separately.
3. [2] M1 closing inventory = 2,000 produced - 1,850 sold = 150 units, fixed overhead carried forward = 150 x £12 OAR = £1,800; A1 this matches the difference (21,600 - 19,800 = £1,800), which is higher under absorption costing because production exceeded sales, deferring fixed overhead into closing inventory.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S20_MA_Marginal_and_Absorption_Costing` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 8 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S21_MA_Budgeting_and_Variance_Analysis.
