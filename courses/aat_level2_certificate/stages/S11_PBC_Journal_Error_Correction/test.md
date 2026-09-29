# S11_PBC_Journal_Error_Correction - Test: The journal: correcting errors, with and without a suspense account

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A payment for stationery was correctly entered in the cash book but posted to the Office Equipment account instead of the Stationery Expense account, for the correct amount. Identify the type of error, and explain why it is not disclosed by the trial balance. [3 marks]
2. A trial balance's debit column totals £61,400 and its credit column totals £61,900. Calculate the difference and state which side the suspense account balance is opened on. [2 marks]
3. The £500 difference in the previous question was caused by a sales invoice of £500 being entered correctly in the sales daybook but never posted to the receivables control account. Write the journal entry to correct this and clear the suspense account. [3 marks]
4. Explain the difference between an error of omission and a compensating error. [3 marks]
5. Which type of error IS disclosed by the trial balance? Choose every correct option.
   A. only one side of a transaction being posted
   B. an error of commission
   C. a reversal of entries
   D. a compensating error

## Answer key (for the tutor only)
1. [3] B1 error of principle (posted to the wrong type/class of account -- an expense treated as an asset); B1 an equal debit and credit were still posted (just to the wrong account); B1 so total debits still equal total credits and the trial balance still balances.
2. [2] M1 difference = £500; A1 debit (since credits currently exceed debits, a debit balance in suspense is needed to make them agree).
3. [3] B1 debit Receivables Control Account £500 (the missing entry); B1 credit Suspense Account £500 (clearing it to nil); B1 both entries for £500, correctly on the debit/credit sides shown.
4. [3] B1 an error of omission: a transaction is left out entirely (neither side posted), so the trial balance still balances since nothing was posted at all; B1 a compensating error: two separate, unrelated errors happen to be of equal and opposite size; B1 so their effects cancel out in the trial balance totals, even though each individual account is wrong.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_PBC_Journal_Error_Correction` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 9 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_PBC_Trial_Balances.
