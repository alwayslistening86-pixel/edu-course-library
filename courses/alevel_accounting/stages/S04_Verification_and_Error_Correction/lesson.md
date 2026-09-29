# S04_Verification_and_Error_Correction - Lesson: Verifying records and correcting errors

## Goal
The learner verifies accounting records using the trial balance, bank reconciliation statements, and sales/purchases ledger control accounts, and corrects errors via the general journal and a suspense account.

## Syllabus items taught here
- 3.4a - Bank reconciliation statements
- 3.4b - Sales and purchases ledger control accounts
- 3.4c - Errors that do and do not affect the trial balance
- 3.4d - Correcting errors via the journal and suspense account

## How to teach this
Ask: the cash book shows £5,200 but the bank statement shows £5,450. Does that automatically mean an error has been made? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.4a Bank reconciliation statements
**Bank reconciliation statements**: the cash book (business's own record) and the bank statement (the bank's record) can genuinely differ without either being wrong, because of **timing differences**: unpresented cheques (paid out in the cash book but not yet cleared by the bank) and outstanding lodgements/deposits (banked but not yet credited by the bank). A bank reconciliation starts from one balance, adds/removes these timing differences, and should arrive at the other balance; any remaining difference is a genuine error (in the cash book or the bank's records) needing correction. Items appearing on the bank statement but not yet in the cash book (bank charges, interest, standing orders, direct debits, dishonoured cheques) must first be entered into the cash book itself, updating its balance, before the reconciliation is prepared.

#### 3.4b Sales and purchases ledger control accounts
**Sales and purchases ledger control accounts**: a **sales ledger control account** summarises, in total, everything that has happened to trade receivables in the period (opening balance + credit sales - cash received from customers - discounts allowed - irrecoverable debts written off +/- returns and dishonoured cheques = closing balance); a **purchases ledger control account** does the equivalent for trade payables. Because they are built from the totals in the books of prime entry, comparing the control account balance with the total of the individual (personal) ledger account balances is an independent check that the personal ledger has been posted correctly - a mismatch signals an error in the personal accounts even though the trial balance itself may still balance.

#### 3.4c Errors that do and do not affect the trial balance
**Errors that do and do not affect the trial balance**: an imbalance in the trial balance (one debit/credit entry missing or the wrong amount on one side only) is a genuine one-sided error and is temporarily plugged with a **suspense account** for the amount of the difference, so the accounts can still be drawn up while the cause is found. Six error types do **not** cause an imbalance, because both sides are still affected equally: error of **omission** (a transaction left out completely), error of **commission** (posted to the wrong account of the correct type, e.g. one customer's account instead of another), error of **principle** (posted to the wrong type of account, e.g. a capital item treated as an expense), error of **original entry** (the wrong amount used, but the same wrong amount posted to both sides), **reversal** of entries (debit and credit swapped), and **compensating errors** (two unrelated errors of equal and opposite value).

#### 3.4d Correcting errors via the journal and suspense account
**Correcting errors via the journal**: every correction is made with a **journal entry** (a debit, a credit and a narrative explaining why), then posted to the ledger accounts and, where a suspense account was opened, to clear it. Correcting a one-sided error clears the suspense account; correcting a two-sided error (omission, commission, principle, original entry, reversal, compensating) does not touch the suspense account, because such an error never caused an imbalance in the first place. Where an error has affected the statement of profit or loss (e.g. an expense recorded as the wrong amount, or a capital item wrongly treated as revenue expenditure), correcting it also changes the profit for the year, and a statement adjusting the previously calculated profit to the corrected profit is often required.

## Explicitly not here
The trial balance itself, and posting routine transactions, is S02; period-end adjustments (accruals, depreciation, irrecoverable debts) are S03.
