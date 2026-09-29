# S11_PBC_Journal_Error_Correction - Lesson: The journal: correcting errors, with and without a suspense account

## Goal
The learner distinguishes errors disclosed and not disclosed by the trial balance, corrects each type using the journal, and opens and clears a suspense account.

## Syllabus items taught here
- PBC3.2 - Produce journal entries to correct errors not disclosed by the trial balance
- PBC3.3 - Produce journal entries to correct errors disclosed by the trial balance, using a suspense account

## How to teach this
Ask the learner: if a bookkeeper posts a payment to the wrong expense account, but for the right amount, will the trial balance still balance? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PBC3.2 Produce journal entries to correct errors not disclosed by the trial balance
Errors **not disclosed by the trial balance** are ones where total debits still equal total credits, so the trial balance still balances despite the mistake: an **error of commission** (posted to the wrong account, but of the correct type, e.g. one expense account instead of another), an **error of omission** (a transaction left out entirely -- both sides missing, so it still balances), an **error of original entry** (the wrong amount used, but the same wrong amount on both sides), an **error of principle** (posted to the wrong *type* of account, e.g. an expense treated as an asset), a **reversal of entries** (the debit and credit swapped -- debits and credits still total the same either way), and **compensating errors** (two unrelated errors of equal and opposite size, cancelling out in the totals). These are corrected using the journal, adjusting the accounts actually affected (no suspense account is needed, since the trial balance already balances).

#### PBC3.3 Produce journal entries to correct errors disclosed by the trial balance, using a suspense account
Errors **disclosed by the trial balance** are ones that make total debits and total credits *not* agree -- e.g. only one side of an entry posted, or unequal amounts posted to each side. Where this happens, a **suspense account** is opened for the difference so the trial balance balances (a temporary holding account), and the journal is used to correct the underlying error(s) and clear the suspense account to nil. *Worked example:* a trial balance's debit column totals £48,250 and its credit column totals £48,100 -- a difference of **£150** is posted to the suspense account (as a credit, since debits currently exceed credits) so the trial balance balances while the cause is investigated; once found, the correcting journal entry both fixes the real account and clears the suspense account.

## Explicitly not here
Extracting and redrafting the trial balance itself (before and after these corrections) is S12.
