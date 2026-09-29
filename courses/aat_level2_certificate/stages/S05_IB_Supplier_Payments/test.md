# S05_IB_Supplier_Payments - Test: Processing payments to suppliers

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A supplier invoice is for net £500, VAT £100 (total £600), with a 4% PPD available. The business pays within the discount period. Calculate the credit note's discount, its VAT, its total, and the amount actually paid. [4 marks]
2. List three types of discrepancy that might be found between a supplier's statement of account and the payables ledger. [3 marks]
3. A business owes a supplier £900 across two invoices and pays £900 in full, referencing both invoices on the remittance advice. How should this payment be allocated? Choose every correct option.
   A. against both named invoices, paying the account in full
   B. as an overpayment
   C. against the opening balance only
   D. as a duplicated transaction

## Answer key (for the tutor only)
1. [4] M1 discount = 500 x 0.04 = £20; M1 VAT on discount = 20 x 0.2 = £4; A1 credit note total = £24; A1 amount paid = 600 - 24 = £576.
2. [3] B1 underpayments; B1 overpayments; B1 incorrect discount taken; B1 incorrect amounts/details; B1 timing differences; B1 missing transactions; B1 duplicated transactions -- any 3 for full marks.
3. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_IB_Supplier_Payments` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 6 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_IB_Cash_Book_and_Petty_Cash.
