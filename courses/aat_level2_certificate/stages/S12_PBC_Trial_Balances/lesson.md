# S12_PBC_Trial_Balances - Lesson: Trial balances

## Goal
The learner extracts an initial trial balance from the general ledger, and redrafts the trial balance following adjusting journal entries.

## Syllabus items taught here
- PBC4.1 - Extract an initial trial balance
- PBC4.2 - Redraft the trial balance following adjustments

## How to teach this
Ask the learner: once every ledger account has been balanced, what single check confirms the double entry has (probably) been done correctly? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PBC4.1 Extract an initial trial balance
An **initial trial balance** is extracted by transferring every general ledger account's balance (see IB5.2) into a debit or credit column, according to whether it is a debit or credit balance -- assets and expenses are normally debit balances; liabilities, income and capital are normally credit balances. The two columns are then totalled: if they agree, this supports (but does not prove) that double entry has been correctly applied for the period.

#### PBC4.2 Redraft the trial balance following adjustments
After journal entries are posted to correct errors (S11) or record adjustments, the general ledger account balances are **recalculated**, and the trial balance is **redrafted**: the adjusted balances replace the original ones, and the debit and credit columns are re-totalled and re-balanced. *Worked example:* a Rent expense account had a debit balance of £4,000 before adjustment; a journal entry adds a further £250 of rent (debit Rent Expense £250, credit accrued expenses/payables £250 -- a typical period-end adjustment). The redrafted Rent Expense balance = £4,000 + £250 = **£4,250** (debit), and the trial balance's totals are recalculated to include this change (and its matching credit entry) so both columns still agree.

## Explicitly not here
This is the last Principles of Bookkeeping Controls stage; producing full financial statements from the trial balance is beyond Level 2.
