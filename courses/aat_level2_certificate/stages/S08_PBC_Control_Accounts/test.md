# S08_PBC_Control_Accounts - Test: Control accounts

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A receivables control account opens at £7,500 (debit). During the period: credit sales £22,300, receipts from customers £21,600, discounts allowed £180, sales returns £310. Calculate the closing balance. [4 marks]
2. The receivables control account shows a closing balance of £9,400, but the individual balances on the receivables ledger total £9,250. Explain two possible reasons for this discrepancy. [4 marks]
3. What does the VAT control account's balance represent? Choose every correct option.
   A. the net amount owed to (or reclaimable from) HMRC
   B. the total owed by all credit customers
   C. the total owed to all credit suppliers
   D. the business's total cash balance
4. Explain the purpose of reconciling the payables control account with the payables ledger. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 7,500 + 22,300 - 21,600 - 180 - 310; A1 £7,710; B1 sales added; B1 receipts, discounts allowed and returns all deducted.
2. [4] Award 2 marks per reason (1 for correctly identifying the reason, 1 for a clear explanation of how it causes the discrepancy), for two of: a transaction posted to the control account but not the individual account (or vice versa); a transaction posted to the wrong individual account; an arithmetic/casting error in totalling an individual account; a discount allowed or sales return recorded in one place but not the other.
3. Correct: A (exactly these options, no others)
4. [2] B1 it checks that the control account (part of double-entry) agrees with the sum of the individual supplier balances (memorandum accounts); B1 any difference signals an error that needs investigating and correcting.

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_PBC_Control_Accounts` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 8 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_PBC_Bank_Reconciliation.
