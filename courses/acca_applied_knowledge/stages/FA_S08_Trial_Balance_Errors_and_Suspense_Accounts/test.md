# FA_S08_Trial_Balance_Errors_and_Suspense_Accounts - Test: Trial balance, correction of errors and suspense accounts

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which type of error would NOT cause a trial balance to disagree? Choose every correct option.
   A. A transaction posted as a debit only, with no corresponding credit
   B. An error of commission (posted to the wrong account of the correct class)
   C. An arithmetic error totalling a ledger account
   D. A balance omitted entirely from the trial balance
2. A trial balance fails to balance, with credits exceeding debits by £340. A suspense account is opened. It is then found that a £170 discount allowed to a customer was correctly recorded in the receivables ledger but was omitted entirely from the discounts allowed expense account. Explain how this correction affects the suspense account, and state whether it fully clears it. [4 marks]
3. A payment of £500 was correctly entered in the cash book but posted to the payables ledger as £50. This is: Choose every correct option.
   A. a compensating error
   B. an error of original entry (transposition)
   C. an error of principle
   D. an error of omission
4. A sale of £2,400 was completely omitted from the accounting records (no entry made anywhere). State whether the trial balance would balance, and name this type of error. [2 marks]
5. Which of these is the correct definition of a suspense account? Choose every correct option.
   A. A permanent ledger account for unresolved disputes with customers
   B. A temporary account opened when a trial balance fails to balance, or a transaction's treatment is unclear, cleared once errors are corrected
   C. An account used only for cash transactions
   D. A synonym for the trial balance itself
6. A business's trial balance shows debits of £186,400 and credits of £185,900. Calculate the amount, and the side, of the suspense account balance needed to make the trial balance balance. [2 marks]

## Answer key (for the tutor only)
1. Correct: B (exactly these options, no others)
2. [4] M1 the £170 omission is a one-sided entry, understating debits by £170; M1 correcting it: Dr Discounts allowed £170, Cr Suspense £170, which reduces the suspense account debit balance by £170; A1 the suspense account is not fully cleared: 340 - 170 = £170 remains, so at least one further error must be found; B1 correct direction of the suspense balance: since credits exceeded debits by £340, the suspense account opens with a debit balance of £340.
3. Correct: B (exactly these options, no others)
4. [2] A1 the trial balance would still balance, because neither a debit nor a credit was made, so both sides remain equal (just both £2,400 short of what they should be); B1 this is an error of omission.
5. Correct: B (exactly these options, no others)
6. [2] M1 difference = 186,400 - 185,900 = £500, with debits exceeding credits; A1 a suspense account credit balance of £500 is needed to balance the trial balance.

## Grading
Apply `rubric.json`'s `stage_rubrics.FA_S08_Trial_Balance_Errors_and_Suspense_Accounts` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 6 (50%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to FA_S09_Statement_of_Financial_Position_and_Profit_or_Loss.
