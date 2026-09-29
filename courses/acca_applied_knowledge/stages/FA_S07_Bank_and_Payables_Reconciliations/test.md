# FA_S07_Bank_and_Payables_Reconciliations - Test: Bank and payables reconciliations

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. The cash book shows a balance of £5,120 before adjustment. A standing order of £260 and bank interest received of £40, neither yet entered in the cash book, are identified. Calculate the corrected cash book balance. [3 marks]
2. An unpresented cheque, at the reconciliation date, is: Choose every correct option.
   A. recorded in the cash book but not yet cleared by the bank
   B. recorded on the bank statement but not yet in the cash book
   C. always an error requiring correction
   D. the same thing as a dishonoured cheque
3. The bank statement shows a balance of £6,740. Unpresented cheques total £510 and there is one outstanding lodgement of £275. Calculate the balance per the cash book (assuming no other adjustments are needed). [3 marks]
4. Which of these would appear as a reconciling item between a payables ledger balance and a supplier's statement? Choose every correct option.
   A. An invoice recorded by the supplier but not yet entered in the payables ledger
   B. A payment sent by the business but not yet received by the supplier
   C. The trade discount already agreed and applied identically by both parties
   D. Nothing; the two should never differ
5. A payables ledger account shows a balance of £11,200. The supplier's statement shows £12,050. A credit note for £450 issued by the supplier has not yet been recorded in the payables ledger, and the remaining £1,300 difference is found to be a supplier invoice double-counted on their own statement (a supplier error). Reconcile the two balances. [4 marks]
6. Bank charges shown on the bank statement but not yet in the cash book require: Choose every correct option.
   A. no action, since the bank statement is always correct
   B. an entry in the cash book to bring it up to date, reducing the cash book balance
   C. an entry increasing the cash book balance
   D. a correction to the bank statement itself

## Answer key (for the tutor only)
1. [3] M1 deduct the standing order (a payment out): 5,120 - 260 = £4,860; M1 add the interest received: 4,860 + 40; A1 = £4,900.
2. Correct: A (exactly these options, no others)
3. [3] M1 remove unpresented cheques: 6,740 - 510; M1 add the outstanding lodgement: 6,230 + 275; A1 = £6,505.
4. Correct: A, B (exactly these options, no others)
5. [4] M1 payables ledger adjusted for the unrecorded credit note: 11,200 - 450 = £10,750; M1 supplier statement adjusted to remove their duplicated invoice: 12,050 - 1,300 = £10,750; A1 both now agree at £10,750; A1 the business should query the duplicated invoice with the supplier before paying the original (unreconciled) statement figure.
6. Correct: B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.FA_S07_Bank_and_Payables_Reconciliations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 7 (50%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to FA_S08_Trial_Balance_Errors_and_Suspense_Accounts.
