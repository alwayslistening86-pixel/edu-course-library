# S14_PC_Inventory_Valuation - Test: Inventory valuation: FIFO, LIFO and AVCO

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Using the same data as the practice question (opening 60 units at £4.00, receive 40 units at £6.00, issue 70 units), calculate the LIFO issue cost and the LIFO closing inventory value. [4 marks]
2. Using the same data (opening 60 units at £4.00, receive 40 units at £6.00, issue 70 units), calculate the AVCO issue cost, showing the average cost per unit. [4 marks]
3. Explain why FIFO, LIFO and AVCO give the same total number of units issued but different total costs. [3 marks]
4. Which inventory valuation method is for internal (management accounting) use only at this level, not for external financial reporting? Choose every correct option.
   A. LIFO
   B. FIFO
   C. AVCO
   D. all three are equally acceptable for external reporting

## Answer key (for the tutor only)
1. [4] M1 40 units at £6.00 = £240; M1 30 units at £4.00 = £120; A1 issue cost = £360; A1 closing inventory = 30 units at £4.00 = £120.
2. [4] M1 total value = (60x4)+(40x6) = 240+240 = £480; M1 total units = 100, average = 480/100 = £4.80 per unit; A1 issue cost = 70 x £4.80 = £336; A1 closing inventory = 30 x £4.80 = £144.
3. [3] B1 all three methods issue the same physical quantity of inventory (the number of units issued doesn't change); B1 they differ only in which unit *prices* are assumed to apply to those units (oldest first, newest first, or a blended average); B1 so the total cost assigned to the issue (and to what remains as closing inventory) differs between methods, especially when prices have changed between receipts.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_PC_Inventory_Valuation` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 9 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_PC_Labour_and_Overheads.
