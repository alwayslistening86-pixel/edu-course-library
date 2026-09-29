# FA_S08_Trial_Balance_Errors_and_Suspense_Accounts - Lesson: Trial balance, correction of errors and suspense accounts

## Goal
The learner prepares a trial balance, classifies and corrects errors (including those a trial balance would and would not reveal), and clears a suspense account via journal entries.

## Syllabus items taught here
- FA.F1 - Trial balance
- FA.F2 - Correction of errors
- FA.F3 - Suspense accounts

## How to teach this
Ask: 'A trial balance balances perfectly. Does that prove there are no errors in the accounts?' Use the answer to separate errors that unbalance a trial balance from those that don't. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### FA.F1 Trial balance
The **trial balance** lists every ledger account's closing debit or credit balance, and total debits must equal total credits (since every transaction was posted as an equal debit and credit) - it is a mechanical check on the double entry, and the source data for preparing the financial statements, not itself a financial statement.

#### FA.F2 Correction of errors
**Correction of errors**. Some errors do **not** cause the trial balance to disagree: **error of omission** (a transaction left out entirely), **error of commission** (posted to the wrong account of the correct type, e.g. one payable's account instead of another's), **error of principle** (posted to the wrong *type* of account, e.g. a repair expensed as if it were a non-current asset), **compensating errors** (two unrelated errors of equal and opposite value cancel out), **error of original entry** (the wrong amount was used for both the debit and credit, so it still balances), and a **complete reversal of entries** (debit and credit swapped, which still balances since both sides moved by the same amount, doubled). Errors that **do** cause a trial balance to disagree include: a one-sided entry (posted as a debit or credit only), unequal debit/credit amounts, an arithmetic error in a ledger account balance, or a balance omitted from/duplicated in the trial balance. *Worked example*: a business posted a £1,200 cash sale correctly to Cash but debited (instead of credited) Sales revenue - both entries were made, but on the wrong side, so debits exceed credits by 2 x £1,200 = £{2 * 1200:,}.

#### FA.F3 Suspense accounts
A **suspense account** is a temporary holding account opened when the trial balance does not balance (the difference is posted there so the trial balance balances provisionally), or when a transaction's correct treatment is not yet known. Once each error is found, a **journal entry** corrects it, and if the error affected the imbalance, the correction also clears part or all of the suspense account; once every error is corrected, the suspense account balance should be nil. *Worked example*: a trial balance fails to balance, debits being £850 short; a suspense account of £850 (debit) is opened. Investigation finds a £850 electricity payment was posted to Cash (correctly) but never posted to the Electricity expense account at all (a one-sided entry). Correcting journal: Dr Electricity expense £850, Cr Suspense account £850 - this clears the £850 suspense balance and corrects the omitted debit.

## Explicitly not here
Preparing the financial statements themselves from the trial balance is FA_S09.
