# TAX_S05_Corporation_Tax - Test: Corporation tax

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. A company has taxable total profits of £400,000 for 2026/27. Calculate its corporation tax liability, stating which rate applies and why. [3 marks]
2. A company has taxable total profits of £200,000 for 2026/27, a single company with no associates. Using the standard marginal relief fraction of 3/200, calculate its corporation tax liability. [5 marks]
3. Client entertaining costs are generally, for corporation tax purposes: Choose every correct option.
   A. fully tax-deductible, like any other trading expense
   B. disallowable, added back when computing adjusted trading profit
   C. only deductible for companies with a single director
   D. always exempt from corporation tax
4. A company has an accounting profit of £95,000, including £4,000 of disallowable donations and £10,000 of depreciation (replaced by capital allowances of £8,000). Calculate the adjusted trading profit. [3 marks]
5. Marginal relief for corporation tax applies: Choose every correct option.
   A. to every company regardless of profit level
   B. only where taxable total profits fall between the small profits limit and the main rate threshold
   C. only to companies with losses
   D. only to companies with profits above £250,000

## Answer key (for the tutor only)
1. [3] M1 profits exceed the main rate threshold of £250,000, so the main rate of 25% applies to the whole amount; A1 tax = 400,000 x 25% = £100,000; B1 no marginal relief applies here since profits exceed the upper threshold entirely.
2. [5] M1 profits are between the small profits limit and the main rate threshold, so marginal relief applies; M1 tax at main rate on full profits = 200,000 x 25% = £50,000; M1 marginal relief = (250,000-200,000) x 3/200 = £750; A1 corporation tax payable = 50,000 - 750 = £49,250; B1 correct reasoning: marginal relief tapers the tax charge between the small profits and main rate thresholds so it doesn't jump abruptly.
3. Correct: B (exactly these options, no others)
4. [3] M1 add back donations and depreciation: 95,000+4,000+10,000; M1 deduct capital allowances: -8,000; A1 adjusted trading profit = £101,000.
5. Correct: B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.TAX_S05_Corporation_Tax` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (55%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to TAX_S06_VAT_and_Stamp_Taxes.
