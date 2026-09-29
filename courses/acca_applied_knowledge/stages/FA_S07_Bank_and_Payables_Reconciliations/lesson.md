# FA_S07_Bank_and_Payables_Reconciliations - Lesson: Bank and payables reconciliations

## Goal
The learner prepares a bank reconciliation between the cash book and the bank statement, and reconciles a supplier's statement to the payables ledger account.

## Syllabus items taught here
- FA.E1 - Bank reconciliations
- FA.E2 - Payables account reconciliations

## How to teach this
Ask: 'A business's own cash book shows £4,200 in the bank; the bank statement shows £4,650. Are the books wrong?' Use the answer to introduce timing differences. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### FA.E1 Bank reconciliations
A **bank reconciliation** explains the difference between the cash book balance and the bank statement balance at a given date, which usually arises from **timing differences**: **unpresented cheques** (paid out and recorded in the cash book, but not yet cleared through the bank) and **outstanding/uncleared lodgements** (deposits recorded in the cash book but not yet showing on the statement), plus items the bank has processed that the business has not yet recorded (bank charges, interest, standing orders/direct debits, dishonoured cheques) - these must first be entered into the cash book, updating it to a corrected balance. *Worked example*: cash book balance (before adjustment) £3,850; bank charges of £45 and a dishonoured customer cheque of £220 have not yet been entered in the cash book. Corrected cash book balance = 3,850 - 45 - 220 = £{3850 - 45 - 220:,}. The bank statement shows £4,300; unpresented cheques total £680 and an outstanding lodgement is £695. Reconciliation: 4,300 - 680 + 695 = £{4300 - 680 + 695:,}, which should equal the corrected cash book balance of £{3850 - 45 - 220:,} once both sides are fully worked through (any remaining difference signals an error requiring investigation).

#### FA.E2 Payables account reconciliations
A **payables (supplier statement) reconciliation** compares the balance on a supplier's statement with the balance on the business's own payables ledger account for that supplier, to explain any difference before payment - typically **timing differences** (an invoice or credit note issued by the supplier not yet recorded by the business, or a payment made by the business not yet received/processed by the supplier) or **genuine errors** on either side (a duplicated or mis-posted invoice, an arithmetic error). *Worked example*: the payables ledger shows a balance owed of £8,400; the supplier's statement shows £9,150. Investigation finds an invoice for £630 recorded by the supplier but not yet entered in the payables ledger, and a payment of £120 sent by the business but not yet received by the supplier. Reconciled payables ledger balance = 8,400 + 630 = £{8400 + 630:,}; reconciled supplier statement = 9,150 - 120 = £{9150 - 120:,}, confirming both now agree at £{8400 + 630:,}.

## Explicitly not here
Correction of errors more broadly, and the suspense account, are FA_S08.
