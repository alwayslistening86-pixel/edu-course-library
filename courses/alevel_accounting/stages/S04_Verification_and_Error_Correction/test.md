# S04_Verification_and_Error_Correction - Test: Verifying records and correcting errors

## How to run this
A real checkpoint in AQA's style: short calculations with mark schemes (M = method, A = accuracy, B = independent/bookwork mark), multiple-choice items, and short written/evaluative questions. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The cash book shows a balance of £4,100. The bank statement shows £4,600. There is one unpresented cheque of £700 and one deposit of £200 not yet credited by the bank. Prepare a reconciliation starting from the bank statement balance to reach the cash book balance, and state whether any further investigation is needed. [3 marks]
2. Which error would cause the trial balance to fail to balance? Choose every correct option.
   A. A sale correctly recorded but posted to the wrong customer's account
   B. A transaction omitted entirely from the books
   C. A cheque payment debited to the payables account but with no credit entry made anywhere
   D. Both sides of a transaction posted with the same wrong amount
3. The trial balance fails to balance because total debits exceed total credits by £340. A suspense account is opened. It is then found that a purchase of £340 was correctly entered in the purchases account but was never posted to the payables (supplier) account. Prepare the correcting journal entry and state the suspense account balance after posting. [3 marks]
4. A sales ledger control account is built up from which source? Choose every correct option.
   A. The totals in the books of prime entry (sales day book, cash book, journal etc.)
   B. A physical count of unsold inventory
   C. The bank statement only
   D. The statement of financial position of the prior year
5. A business's sales ledger control account shows a closing balance of £18,500, but the total of the individual customer balances in the sales ledger is £18,200. Explain what this £300 difference suggests, and name one specific error that could cause it. [3 marks]
6. Explain why correcting an error of principle (a £2,000 non-current asset purchase wrongly debited to repairs expense) changes the profit for the year, and state the effect. [3 marks]

## Answer key (for the tutor only)
1. [3] M1 bank statement balance £4,600 less unpresented cheque £700 = £3,900; A1 plus outstanding deposit £200 = £4,100; B1 this equals the cash book balance of £4,100, so no further error needs investigating.
2. Correct: C (exactly these options, no others)
3. [3] M1 Debit Suspense £340 (clears the credit balance that was opened on the suspense account to plug the credit-side shortfall caused by the missing entry); A1 Credit Payables £340 (records the missing entry); B1 the suspense account balance is then nil.
4. Correct: A (exactly these options, no others)
5. [3] B1 it suggests an error has been made in posting to the individual (personal) customer accounts, even though the trial balance itself may still balance; B1 the control account, built independently from the day books, is unaffected by errors made only in the personal ledger; B1 example: a credit note of £300 was recorded in the sales returns day book (affecting the control account total) but never posted to that customer's individual account.
6. [3] B1 repairs expense is currently £2,000 too high, so profit is currently understated by £2,000; B1 the correction removes the £2,000 from expenses (debiting non-current assets, crediting repairs expense), so corrected profit increases by £2,000; B1 the £2,000 should instead appear in the statement of financial position as a non-current asset, not as an expense in the statement of profit or loss.

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Verification_and_Error_Correction` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Accounting_Concepts.
