# MA_S03_Materials_Labour_and_Overheads - Test: Materials, labour and overheads

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Opening inventory nil. Purchases: 200 units @ £3.00, then 300 units @ £3.30. 350 units are issued. Calculate the cost of the issue and the value of closing inventory using FIFO. [4 marks]
2. Annual demand is 8,000 units, ordering cost £32/order, holding cost £4/unit/year. Calculate the EOQ. [2 marks]
3. Which inventory valuation method is not permitted under IAS 2 for financial reporting purposes, though it may still be examined in management accounting? Choose every correct option.
   A. FIFO
   B. AVCO
   C. LIFO
   D. Standard cost
4. Budgeted overhead is £84,000 and budgeted labour hours are 12,000. Calculate the overhead absorption rate per labour hour. [1 mark]
5. Using an OAR of £7.00/labour hour, actual labour hours worked are 12,500 and actual overhead incurred is £90,000. Calculate the overhead absorbed and state whether overhead is over- or under-absorbed, and by how much. [4 marks]
6. Which of these would usually be apportioned rather than allocated to a cost centre? Choose every correct option.
   A. A supervisor employed solely in one department
   B. Rent of a shared factory building
   C. Direct material used in one job
   D. Depreciation of a machine owned by one department
7. Which are valid bases for reapportioning a canteen's costs to production departments? Choose every correct option.
   A. Number of employees in each production department
   B. Floor area of each production department
   C. Machine hours in each production department
   D. None; canteen costs cannot be reapportioned

## Answer key (for the tutor only)
1. [4] M1 FIFO issue cost = 200x3.00 + 150x3.30 = £1,095.00; A1 = £1,095.00; M1 closing inventory = 150 units @ £3.30 = £495.00; A1 = £495.00.
2. [2] M1 EOQ = sqrt(2x8,000x32/4); A1 = 358 units.
3. Correct: C (exactly these options, no others)
4. [1] A1 OAR = 84,000/12,000 = £7.00/labour hour.
5. [4] M1 overhead absorbed = 7.00 x 12,500 = £87,500; A1 = £87,500; M1 compare to £90,000 incurred; A1 absorbed exceeds incurred by £-2,500, so overhead is over-absorbed by £-2,500.
6. Correct: B (exactly these options, no others)
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.MA_S03_Materials_Labour_and_Overheads` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 7 (50%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to MA_S04_Costing_Methods_and_Alternative_Principles.
