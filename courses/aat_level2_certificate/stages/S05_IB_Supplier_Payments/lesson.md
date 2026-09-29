# S05_IB_Supplier_Payments - Lesson: Processing payments to suppliers

## Goal
The learner identifies discrepancies between a supplier's statement of account and the payables ledger, calculates payments due (including PPD), and allocates payments correctly.

## Syllabus items taught here
- IB3.3 - Process payments to suppliers: discrepancies, calculating payments due including PPD, allocating payments

## How to teach this
Ask the learner: how would you check that a supplier's monthly statement matches what your own records say you owe them? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### IB3.3 Process payments to suppliers: discrepancies, calculating payments due including PPD, allocating payments
Records/documents used: the **supplier account**, **invoices and credit notes** (including discounts and VAT) and the **statement of account** received from the supplier. The agreed **payment terms** must be taken into account when deciding what and when to pay. Discrepancies between the supplier's statement of account and the business's own payables ledger account for that supplier: **underpayments**, **overpayments**, **incorrect discount taken**, **incorrect amounts**, **incorrect details**, **timing differences**, **missing transactions** and **duplicated transactions** (the same categories as for customer receipts, IB2.3, but checked from the payer's side). Payments due are calculated including any PPD taken (via the credit-note method, IB3.2). Payments are **allocated**: **in full**, **in part**, **against opening balances**, **against invoices**, or **against credit notes**. *Worked example:* a supplier invoice for net £800 has a 3% PPD if paid within the agreed term; VAT at 20% on £800 = £160, so the full invoice total is £960. The business pays within the term, so a credit note is received: discount = £800 x 0.03 = **£24.00**; VAT on the discount = £24.00 x 0.20 = **£4.80**; credit note total = £24.00 + £4.80 = **£28.80**. The amount actually paid = £960 - £28.80 = **£931.20**.

## Explicitly not here
Entering these payments into the cash book is S06.
