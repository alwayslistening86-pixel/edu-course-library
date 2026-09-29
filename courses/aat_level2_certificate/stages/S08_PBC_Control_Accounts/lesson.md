# S08_PBC_Control_Accounts - Lesson: Control accounts

## Goal
The learner produces the receivables, payables and VAT control accounts, and reconciles the receivables and payables control accounts with the individual ledger balances, identifying reasons for discrepancies.

## Syllabus items taught here
- PBC1.1 - Produce control accounts: receivables, payables and VAT control accounts
- PBC1.2 - Reconcile control accounts with the receivables and payables ledgers, and identify reasons for discrepancies

## How to teach this
Ask the learner: if you added up every individual customer's balance in the receivables ledger, what single general ledger figure should that total match? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PBC1.1 Produce control accounts: receivables, payables and VAT control accounts
The **receivables ledger control account**, **payables ledger control account** and **VAT control account** are general ledger accounts, part of the double-entry system, summarising totals from the books of prime entry. *Worked example -- receivables control account:* opening balance £6,200 (debit); during the period, credit sales £18,500 (debit, increasing what's owed), receipts from customers £17,900 (credit, reducing what's owed), discounts allowed £250 (credit) and sales returns £180 (credit). Closing balance = £6,200 + £18,500 - £17,900 - £250 - £180 = **£6,370** (debit balance carried/brought down). *Worked example -- payables control account:* opening balance £5,200 (credit); credit purchases £21,000 (credit), payments to suppliers £19,400 (debit), discounts received £210 (debit), purchases returns £340 (debit). Closing balance = £5,200 + £21,000 - £19,400 - £210 - £340 = **£6,250** (credit balance carried/brought down). The **VAT control account** collects output VAT (charged on sales, a credit -- money owed to HMRC) and input VAT (paid on purchases, a debit -- reclaimable from HMRC); its balance is the net amount owed to (or reclaimable from) HMRC.

#### PBC1.2 Reconcile control accounts with the receivables and payables ledgers, and identify reasons for discrepancies
**Reconciliation** compares the receivables (or payables) control account balance with the sum of the individual balances on the matching ledger, to check they agree and to catch errors. Method: total the individual debit/credit balances of every account in the receivables (or payables) ledger, then compare that total with the control account balance. If they don't agree, **discrepancies** are investigated -- e.g. a transaction posted to the control account but not to the individual customer/supplier account (or vice versa), a transaction posted to the wrong individual account, an arithmetic error in an individual account, or a discount/return recorded in one place but not the other. Once found, the cause is corrected in whichever record was wrong.

## Explicitly not here
Reconciling the bank account (a different kind of reconciliation) is S09.
