# S02_Financial_Reporting_Standards_I - Test: Financial reporting standards I (inventories, PPE, intangibles, impairment)

## How to run this
A real checkpoint in the style of this stage's real OU module: calculation questions with full working shown (M/A/B mark tags), short explain/apply questions marked by points, and for the capstone stage an extended professional-report question marked by levels. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A machine cost £50,000 with a 10-year useful life and nil residual value, depreciated straight-line, is revalued after 4 years to £40,000. Calculate the carrying amount immediately before the revaluation and the revaluation surplus recognised. [4 marks]
2. Under IAS 38, which development expenditure may be capitalised as an intangible asset? Choose every correct option.
   A. Expenditure incurred before technical feasibility is established
   B. Expenditure meeting all six IAS 38 development criteria, incurred after they are first met
   C. Internally generated goodwill
   D. Research expenditure aimed at gaining new knowledge
3. An asset's carrying amount is £120,000. Fair value less costs of disposal is £95,000; value in use (discounted future cash flows) is £102,000. Calculate the impairment loss, if any. [3 marks]
4. Explain why LIFO is not permitted under IAS 2, and state one practical difference between the FIFO and weighted average cost (AVCO) methods when unit costs are rising. [3 marks]
5. State the qualitative characteristic(s) of useful financial information a set of accounts would breach if management deliberately delayed recognising a large known loss until a later period to smooth reported profit. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 annual depreciation = 50,000/10 = £5,000; M1 carrying amount after 4 years = 50,000 - (4x5,000) = £30,000; A1 revaluation surplus = 40,000 - 30,000 = £10,000; B1 the surplus is recognised in other comprehensive income, not profit or loss.
2. Correct: B (exactly these options, no others)
3. [3] M1 recoverable amount = higher of 95,000 and 102,000 = £102,000; M1 recoverable amount (102,000) is less than carrying amount (120,000); A1 impairment loss = 120,000 - 102,000 = £18,000.
4. [3] B1 LIFO is prohibited under IFRS because it does not reflect the actual physical flow of most inventory and can understate inventory value / overstate cost of sales in a way IFRS does not consider faithfully representative; B1 with rising costs, FIFO values closing inventory closer to current (higher) replacement cost and reports a lower cost of sales/higher profit than AVCO; B1 AVCO smooths cost fluctuations across units by using a weighted average, giving a cost of sales and inventory value between FIFO's and (a prohibited) LIFO's.
5. [3] B1 faithful representation (the information is not neutral -- it is deliberately biased to a preferred outcome, and not free from error); B1 relevance (a large loss withheld from the period it relates to would not be capable of influencing a user's decisions in that period); B1 comparability (period-on-period figures are distorted, making trend analysis unreliable).

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Financial_Reporting_Standards_I` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Financial_Reporting_Standards_II_and_Analysis.
