# FA_S04_Inventories - Test: Inventories

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Opening inventory nil. Purchases: 300 units @ £8.00, then 500 units @ £8.60. 600 units are sold, leaving 200. Calculate the closing inventory value using (a) FIFO and (b) periodic AVCO. [5 marks]
2. Under IAS 2, inventory is valued at: Choose every correct option.
   A. cost, always
   B. net realisable value, always
   C. the lower of cost and net realisable value
   D. the higher of cost and net realisable value
3. 300 units of inventory cost £12.00 each. Due to a market downturn they are now expected to sell for £10.50 each, with selling costs of £0.80 per unit. Calculate the value at which this inventory should be reported. [4 marks]
4. Which inventory valuation method is not permitted under IAS 2? Choose every correct option.
   A. FIFO
   B. AVCO (weighted average cost)
   C. LIFO
   D. Lower of cost and NRV
5. If closing inventory is accidentally overstated at the year end, the effect on that period's reported figures is: Choose every correct option.
   A. cost of sales overstated and profit understated
   B. cost of sales understated and profit overstated
   C. no effect on profit, only on the statement of financial position
   D. revenue overstated
6. Explain why carriage inwards (the cost of delivering purchased goods to the business) is included in the cost of inventory, while carriage outwards (delivering goods to customers) is not. [3 marks]

## Answer key (for the tutor only)
1. [5] M1 (a) FIFO closing inventory = 200 units at £8.60 (the most recent price); A1 = £1,720.00; M1 (b) AVCO price = (300x8.00 + 500x8.60)/800 = £8.38/unit; A1 AVCO closing inventory = 200 x 8.38 = £1,675.00; B1 FIFO and AVCO give different closing values because FIFO uses only the most recent purchase price while AVCO blends all purchase prices.
2. Correct: C (exactly these options, no others)
3. [4] M1 NRV/unit = 10.50 - 0.80 = £9.70; M1 cost/unit = £12.00; A1 lower of the two is NRV, £9.70/unit; A1 total inventory value = 300 x 9.70 = £2,910.00.
4. Correct: C (exactly these options, no others)
5. Correct: B (exactly these options, no others)
6. [3] B3 IAS 2 defines cost as including costs incurred in bringing inventory to its present location and condition, so carriage inwards is a direct cost of acquiring the inventory and is included in its cost; carriage outwards is a selling/distribution cost incurred after the sale is made, not a cost of getting inventory ready for sale, so it is expensed as a selling and distribution expense rather than included in inventory cost.

## Grading
Apply `rubric.json`'s `stage_rubrics.FA_S04_Inventories` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 8 (50%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to FA_S05_Non_Current_Assets_Depreciation_and_Intangibles.
