# S16_FA_Incomplete_Records - Test: Preparing accounting records from incomplete information, mark-up/margin, and reasonableness

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry and financial-statement questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Receivables control account opens at £31,000. During the year: receipts from customers £248,000, discounts allowed £3,100, irrecoverable debts written off £1,900, closing balance £29,600. Calculate credit sales for the year. [3 marks]
2. Revenue is £220,000 and mark-up is 40%. Calculate the cost of sales. [3 marks]
3. Compared with margin, mark-up on the same sale is always: Choose every correct option.
   A. a higher percentage, since it is expressed against the smaller base of cost of sales
   B. a lower percentage
   C. exactly the same percentage
   D. impossible to compare
4. A physical inventory count gives a lower figure than the inventory balance calculated from purchase and sales records. State two possible reasons for this difference. [2 marks]
5. Explain why professional scepticism should be applied to a figure produced automatically by accounting software when records are incomplete. [2 marks]

## Answer key (for the tutor only)
1. [3] M1 total credits = 248,000 + 3,100 + 1,900 + 29,600 = £282,600; M1 credit sales = 282,600 - 31,000; A1 = £251,600.
2. [3] M1 cost of sales x 1.40 = revenue, so cost of sales = 220,000/1.40; A1 = £157,142.86 (or £157,143 to the nearest £); B1 correct method: mark-up is added to cost of sales to reach revenue, not deducted from revenue.
3. Correct: A (exactly these options, no others)
4. [2] B1 theft; B1 loss, breakage or spoilage; B1 a recording/posting error in the purchase or sales records; B1 timing differences between when the count was taken and when records were updated -- any 2 for full marks.
5. [2] B1 software output is only as reliable as the data entered into it; B1 a plausible-looking figure can still be wrong if the underlying data was incomplete, miskeyed or otherwise unreliable, so it should still be critically assessed rather than accepted at face value.

## Grading
Apply `rubric.json`'s `stage_rubrics.S16_FA_Incomplete_Records` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 8 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S17_MA_Purpose_and_Cost_Classification.
