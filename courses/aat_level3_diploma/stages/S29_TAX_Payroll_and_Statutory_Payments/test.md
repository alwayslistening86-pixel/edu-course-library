# S29_TAX_Payroll_and_Statutory_Payments - Test: Payroll, statutory payments and RTI

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry and financial-statement questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. An employee's gross monthly pay is £3,000 (2026/27 monthly personal allowance £1,047.50, monthly NIC primary threshold £1,047.50, both income tax and NIC bands assumed to apply entirely at basic/8% rates for this employee). Calculate their income tax (20%), employee NIC (8%) and net pay before any voluntary deductions. [5 marks]
2. An employee normally works 4 qualifying days a week and is off sick for 2 of them. Calculate their SSP for that week (2026/27 rate £123.25/week). [2 marks]
3. An employee's average weekly earnings are £250. Calculate their SMP for (a) weeks 1-6 and (b) week 7 onwards (2026/27 standard rate £194.32/week). [3 marks]
4. Under RTI, when must an employer submit a Full Payment Submission (FPS) to HMRC? Choose every correct option.
   A. On or before each payday
   B. Only once a year, at the tax year end
   C. Only when an employee leaves
   D. Only when a new employee joins
5. Explain why an employee's average weekly earnings, rather than a single fixed rate, are relevant to calculating their SMP for the first 6 weeks. [2 marks]

## Answer key (for the tutor only)
1. [5] M1 taxable pay = 3,000-1,047.50 = £1,952.50; M1 income tax = 1,952.50 x 20% = £390.50; M1 employee NIC = 1,952.50 x 8% = £156.20; A1 total deductions = 390.50+156.20 = £546.70; A1 net pay = 3,000-546.70 = £2,453.30.
2. [2] M1 daily rate = 123.25/4 = £30.8125; A1 SSP for 2 days = 30.8125 x 2 = £61.63 (to the nearest penny).
3. [3] M1 (a) weeks 1-6: 250 x 90% = £225.00/week; M1 (b) week 7 onwards: lower of £194.32 and (250 x 90% = £225.00); A1 = £194.32/week.
4. Correct: A (exactly these options, no others)
5. [2] B1 for the first 6 weeks, SMP is paid at 90% of the employee's own average weekly earnings, uncapped -- not the flat standard rate; B1 this means higher earners receive more than the standard weekly rate during those first 6 weeks, before the lower-of-standard-rate-or-90% rule applies for the remaining weeks.

## Grading
Apply `rubric.json`'s `stage_rubrics.S29_TAX_Payroll_and_Statutory_Payments` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 10 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
