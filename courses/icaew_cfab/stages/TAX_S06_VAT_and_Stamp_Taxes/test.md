# TAX_S06_VAT_and_Stamp_Taxes - Test: VAT and stamp taxes

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. For 2026/27, a business must register for VAT if its taxable turnover for the previous 12 months exceeds: Choose every correct option.
   A. £90,000
   B. £50,000
   C. £150,000
   D. There is no registration threshold
2. Explain the difference, for VAT purposes, between a zero-rated supply and an exempt supply, and why the difference matters for input VAT recovery. [4 marks]
3. A business has standard-rated sales (VAT-exclusive) of £95,000 and standard-rated purchases (VAT-exclusive) of £50,000 in a VAT period. Calculate output VAT, input VAT, and the amount payable to or repayable by HMRC. [4 marks]
4. The Cash Accounting Scheme accounts for VAT based on: Choose every correct option.
   A. invoice dates, regardless of when cash moves
   B. when cash is actually received or paid
   C. the company's accounting reference date
   D. the corporation tax accounting period
5. Which tax is charged on the transfer of UK company shares in paperless/electronic form? Choose every correct option.
   A. Stamp Duty Land Tax
   B. Stamp Duty Reserve Tax
   C. Corporation tax
   D. Inheritance tax

## Answer key (for the tutor only)
1. Correct: A (exactly these options, no others)
2. [4] B4 a zero-rated supply is still a taxable supply, just charged at 0%, so the business making it can still register (or must, if it exceeds the threshold, though many zero-rated businesses register voluntarily) and can recover input VAT on related costs; an exempt supply is entirely outside the VAT system on the output side, and input VAT relating to exempt supplies generally cannot be recovered, making it an absolute cost to the exempt business.
3. [4] M1 output VAT = 95,000 x 20% = £19,000; M1 input VAT = 50,000 x 20% = £10,000; A1 VAT payable to HMRC = £9,000; B1 correct method: since output VAT exceeds input VAT, the net amount is payable to HMRC rather than repayable.
4. Correct: B (exactly these options, no others)
5. Correct: B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.TAX_S06_VAT_and_Stamp_Taxes` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (55%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
