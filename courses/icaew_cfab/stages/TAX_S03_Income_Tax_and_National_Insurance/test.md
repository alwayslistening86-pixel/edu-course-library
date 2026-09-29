# TAX_S03_Income_Tax_and_National_Insurance - Test: Income tax and national insurance contributions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. An individual has total income of £130,000 in 2026/27. Calculate their tapered personal allowance. [3 marks]
2. Calculate the 2026/27 income tax liability for an individual with total income of £75,000 (below the taper threshold). [6 marks]
3. An employee earns £60,000 in 2026/27. Calculate their employee Class 1 NIC and their employer's Class 1 secondary NIC. [4 marks]
4. A self-employed individual has trading profits of £55,000. Calculate their Class 4 NIC. [4 marks]
5. Compulsory Class 2 NIC for the self-employed was: Choose every correct option.
   A. increased in 2024
   B. abolished from 6 April 2024, though voluntary Class 2 remains available
   C. never charged in the UK
   D. replaced by VAT
6. For 2026/27, the personal allowance is fully withdrawn once total income reaches: Choose every correct option.
   A. £100,000
   B. £50,270
   C. £125,140
   D. £125,140

## Answer key (for the tutor only)
1. [3] M1 excess over £100,000 = 30,000; M1 reduction = 30,000/2 = £15,000; A1 since the reduction (15,000) exceeds the full allowance (12,570), the personal allowance is fully withdrawn to £0 (fully gone once income reaches 125,140).
2. [6] M1 personal allowance £12,570 (full); M1 taxable income = 75,000-12,570 = £62,430; M1 basic rate band 37,700 taxed at 20% = £7,540; M1 remainder = 24,730 taxed at 40% = £9,892; A1 total tax = £17,432; B1 correct method: since total income is below the £100,000 taper threshold, the full personal allowance is available before applying the basic and higher rate bands in turn.
3. [4] M1 employee NIC = (60,000-12,570) x 8%; A1 = £3,794; M1 employer NIC = (60,000-5,000) x 15%; A1 = £8,250.
4. [4] M1 6% band: (50,270-12,570) x 6% = £2,262; M1 2% band: (55,000-50,270) x 2% = £95; A1 total Class 4 NIC = £2,357; B1 correct method: profits between the lower and upper limits are charged at the main rate, and only the excess above the upper limit at the additional rate (Class 2 is no longer compulsory).
5. Correct: B (exactly these options, no others)
6. Correct: C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.TAX_S03_Income_Tax_and_National_Insurance` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 11 (55%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to TAX_S04_Capital_Gains_Tax_and_Inheritance_Tax.
