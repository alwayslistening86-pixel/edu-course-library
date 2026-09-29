# S09_PBC_Bank_Reconciliation - Lesson: Bank reconciliation

## Goal
The learner understands how different payment methods affect the bank balance, updates the cash book from the bank statement, and completes bank reconciliation statements.

## Syllabus items taught here
- PBC2.1 - Payment methods and how they affect the bank balance
- PBC2.2 - Use the bank statement to update the cash book: unrecorded and duplicated items
- PBC2.3 - Complete bank reconciliation statements: unpresented cheques and outstanding lodgements

## How to teach this
Ask the learner: if you write a cheque today, does your bank balance change today, or only once the person you paid pays it in? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PBC2.1 Payment methods and how they affect the bank balance
Payment methods -- **cash**, **cheque**, **debit card**, **credit card**, **bank draft**, **standing order**, **direct debit**, **BACS** (Bankers' Automated Clearing Services), **direct credit**, **CHAPS** (Clearing House Automated Payment System) and **Faster Payments** -- affect the bank balance differently: some **reduce funds on the date of payment** (e.g. a debit card payment, Faster Payments, CHAPS), some **reduce funds at a later date** (e.g. a cheque, which may not clear for several days -- an **unpresented cheque**), and some **have no effect** until they are actually processed by the bank.

#### PBC2.2 Use the bank statement to update the cash book: unrecorded and duplicated items
The **cash book is updated using the bank statement** to catch items the business has not yet recorded itself -- typically automated payments/receipts (e.g. bank charges, interest, direct debits/standing orders) that appear on the statement before the business enters them, or genuinely **unrecorded** items. The cash book is *not* adjusted for genuine timing differences (unpresented cheques, outstanding lodgements) -- those are dealt with in the reconciliation statement (PBC2.3), not by changing the cash book. Any **duplicated** entries found are also corrected. After updating, the cash book is totalled and balanced (a credit or debit balance carried/brought down). *Worked example:* a cash book shows a balance of £1,500.00; the bank statement reveals bank charges of £25.00 (not yet in the cash book) and interest received of £12.40 (also not yet in the cash book). Updated cash book balance = £1,500.00 - £25.00 + £12.40 = **£1,487.40**.

#### PBC2.3 Complete bank reconciliation statements: unpresented cheques and outstanding lodgements
A **bank reconciliation statement** explains any remaining difference between the (now updated) cash book balance and the bank statement's closing balance, caused only by genuine **timing differences**: **unpresented cheques** (paid out by the business, not yet cleared by the bank -- deducted from the bank statement balance to reconcile to the cash book) and **outstanding lodgements** (paid in by the business, not yet showing on the statement -- added to the bank statement balance). *Worked example:* the bank statement's closing balance is £2,744.75; there is an unpresented cheque of £240.00 and an outstanding lodgement of £615.75. Reconciled balance = £2,744.75 - £240.00 + £615.75 = **£3,120.50**, which should now match the (updated) cash book balance.

## Explicitly not here
Reconciling control accounts (a different kind of reconciliation, for receivables/payables) was S08.
