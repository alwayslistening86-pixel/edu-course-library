# S04_IB_Supplier_Invoices - Test: Supplier invoices, credit notes and books of prime entry

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. List three documents used to check the accuracy of a supplier invoice before it is processed. [3 marks]
2. A supplier invoice shows net £600, with a 5% trade discount already applied, plus VAT at 20%. On checking, the trade discount agreed on the quotation was actually 8%. Explain what discrepancy this is and what should happen next. [3 marks]
3. Which book of prime entry records credit notes received from suppliers for goods returned? Choose every correct option.
   A. the purchases returns daybook
   B. the purchases daybook
   C. the sales returns daybook
   D. the discounts received daybook

## Answer key (for the tutor only)
1. [3] B1 quotations (including discounts); B1 purchase orders; B1 goods received notes; B1 delivery notes; B1 goods returned notes -- any 3 for full marks.
2. [3] B1 this is an incorrect discount (trade discount applied is lower than agreed); B1 the invoice should be queried with the supplier rather than processed as received; B1 once corrected, the invoice can be entered in the purchases daybook at the correct (8%) discounted amount.
3. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_IB_Supplier_Invoices` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 7 marks in all; a pass needs at least 5 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_IB_Supplier_Payments.
