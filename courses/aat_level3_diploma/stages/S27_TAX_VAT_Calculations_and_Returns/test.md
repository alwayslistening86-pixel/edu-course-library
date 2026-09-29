# S27_TAX_VAT_Calculations_and_Returns - Test: Calculating VAT and preparing/submitting the VAT return

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry and financial-statement questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A business has standard-rated sales (excl VAT) of £62,000 and standard-rated purchases (excl VAT) of £27,000, all input VAT recoverable, in a VAT period. Calculate the output tax, input tax, and the VAT payable to HMRC (or repayable, if negative). [4 marks]
2. A business has output tax of £4,200 for a period and input tax of £5,900 (all recoverable). Calculate the net VAT position, stating whether the business pays HMRC or is due a repayment. [2 marks]
3. A business issues a credit note for £800 (net) for goods returned by a customer, on top of standard-rated sales (excl VAT) of £50,000 for the period. Calculate the net output tax for the period after accounting for the credit note. [3 marks]
4. What is the normal deadline for submitting and paying a VAT return? Choose every correct option.
   A. One calendar month and 7 days after the end of the VAT period
   B. 14 days after the end of the VAT period
   C. 3 months after the end of the VAT period
   D. The last day of the VAT period itself
5. State which VAT return box shows the net VAT to pay or reclaim, and explain how it is calculated. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 output tax = 62,000 x 20% = £12,400; M1 input tax = 27,000 x 20% = £5,400; A1 VAT payable = 12,400 - 5,400 = £7,000; B1 correctly stating this is payable to HMRC, since output tax exceeds input tax.
2. [2] M1 4,200 - 5,900 = -£1,700; A1 the business is due a VAT repayment of £1,700 from HMRC, since input tax exceeds output tax.
3. [3] M1 output tax on sales = 50,000 x 20% = £10,000; M1 VAT on the credit note = 800 x 20% = £160, deducted from output tax; A1 net output tax = 10,000 - 160 = £9,840.
4. Correct: A (exactly these options, no others)
5. [2] B1 Box 5; B1 it is the difference between Box 3 (total VAT due, i.e. output tax) and Box 4 (VAT reclaimed on purchases, i.e. input tax).

## Grading
Apply `rubric.json`'s `stage_rubrics.S27_TAX_VAT_Calculations_and_Returns` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 9 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S28_TAX_Documentation_and_Communication.
