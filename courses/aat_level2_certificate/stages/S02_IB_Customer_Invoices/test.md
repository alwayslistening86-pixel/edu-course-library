# S02_IB_Customer_Invoices - Test: Customer invoices, credit notes and books of prime entry

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A customer orders 25 units at £8 each, with a 4% bulk discount. Calculate the discounted net, VAT at 20% and the invoice total. [4 marks]
2. Explain why trade and bulk discounts are deducted before VAT is calculated, but PPD (at this level) is not shown on the face of the invoice. [3 marks]
3. An invoice shows net £1,500, VAT £300, total £1,800, with a 3% PPD if paid within 7 days. The customer pays within 7 days. Calculate the credit note's discount, its VAT, its total, and the amount the customer actually pays. [4 marks]
4. Which book of prime entry records credit notes issued to customers for returned goods? Choose every correct option.
   A. the sales returns daybook
   B. the sales daybook
   C. the purchases returns daybook
   D. the discounts allowed daybook
5. State the five figures/columns typically entered into the sales daybook for each invoice. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 gross = 25 x 8 = £200; M1 net = 200 x 0.96 = £192; A1 VAT = 192 x 0.2 = £38.40; A1 total = £230.40.
2. [3] B1 VAT is charged on the amount the customer is actually being asked to pay for the goods, i.e. after trade/bulk discount, since these are certain at the point of sale; B1 PPD is uncertain at the point of invoicing (the customer may or may not pay in time); B1 so the invoice is raised at the full amount, and a credit note (with its own VAT adjustment) is issued only if/when the discount is actually taken.
3. [4] M1 discount = 1,500 x 0.03 = £45; M1 VAT on discount = 45 x 0.2 = £9; A1 credit note total = £54; A1 amount paid = 1,800 - 54 = £1,746.
4. Correct: A (exactly these options, no others)
5. [3] B1 customer name and customer account code; B1 total (gross); B1 VAT; B1 net; B1 analysis (e.g. product code) -- any 3 for full marks.

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_IB_Customer_Invoices` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 11 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_IB_Customer_Receipts.
