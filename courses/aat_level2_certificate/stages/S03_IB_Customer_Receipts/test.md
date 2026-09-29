# S03_IB_Customer_Receipts - Test: Processing receipts from customers

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. List three types of discrepancy that might be found when checking a customer's receipt against their account. [3 marks]
2. A customer's account shows a balance owed of £2,400 (two invoices: £1,000 and £1,400). They pay £1,000, with a remittance advice stating it is for the first invoice. Explain how this receipt should be allocated, and state the resulting balance owed. [3 marks]
3. A customer's payment arrives for less than the invoice total, with no remittance advice and no explanation. What discrepancy might this indicate? Choose every correct option.
   A. an underpayment
   B. an overpayment
   C. a duplicated transaction
   D. a missing transaction

## Answer key (for the tutor only)
1. [3] B1 underpayment; B1 overpayment; B1 incorrect discount taken; B1 incorrect amounts/details; B1 timing differences; B1 missing transactions; B1 duplicated transactions -- any 3 for full marks.
2. [3] B1 the £1,000 receipt is allocated against the specific invoice named on the remittance advice (the £1,000 invoice), which is now paid in full; B1 the second invoice (£1,400) remains outstanding; B1 balance owed = £1,400.
3. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_IB_Customer_Receipts` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 7 marks in all; a pass needs at least 5 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_IB_Supplier_Invoices.
