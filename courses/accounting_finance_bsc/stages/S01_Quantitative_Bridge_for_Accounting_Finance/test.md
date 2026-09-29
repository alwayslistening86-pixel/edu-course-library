# S01_Quantitative_Bridge_for_Accounting_Finance - Test: Quantitative bridge for accounting and finance

## How to run this
A real checkpoint in the style of this stage's real OU module: calculation questions with full working shown (M/A/B mark tags), short explain/apply questions marked by points, and for the capstone stage an extended professional-report question marked by levels. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A population of receivables balances has standard deviation £90. An auditor samples n=25 balances. Calculate the standard error of the sample mean, and explain what would happen to it if the sample size were increased to n=100. [3 marks]
2. A sample of 40 payables balances has mean £560 and standard deviation £110. Construct a 95% confidence interval for the true population mean. [3 marks]
3. Regression of monthly production cost (y, £000) on units produced (x, 000s) gives y = 12 + 2.5x. Forecast the cost at 6,000 units, and state one caution about using this forecast at 40,000 units. [3 marks]
4. Which correctly describes Pearson's correlation coefficient r? Choose every correct option.
   A. It ranges from -1 to +1
   B. A value near 0 means no linear relationship
   C. A strong correlation proves one variable causes the other
   D. It measures only the strength/direction of a linear relationship
5. Revenue was £450,000 in the base year (index = 100) and is £504,000 this year. Calculate the current index number and the percentage change. [2 marks]

## Answer key (for the tutor only)
1. [3] M1 SE = 90/sqrt(25) = 18.00; A1 = £18.00; B1 at n=100, SE = 90/sqrt(100) = £9.00, smaller -- SE falls with sqrt(n), so quadrupling the sample only halves the standard error.
2. [3] M1 SE = 110/sqrt(40) = 17.39; M1 margin = 1.96 x 17.39 = 34.09; A1 CI = (525.91, 594.09).
3. [3] M1 y = 12 + 2.5x6 = 27; A1 = £27k; B1 40,000 units is far outside the range of data the regression was fitted on, so extrapolating that far risks a materially wrong forecast (the relationship may not stay linear, e.g. fixed costs step up at higher volumes).
4. Correct: A, B, D (exactly these options, no others)
5. [2] M1 index = 504,000/450,000 x 100 = 112.0; A1 percentage change = 12.0%.

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Quantitative_Bridge_for_Accounting_Finance` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Financial_Reporting_Standards_I.
