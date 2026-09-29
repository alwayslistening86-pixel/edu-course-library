# S13_Capital_Investment_Appraisal - Test: Capital investment appraisal

## How to run this
A real checkpoint in AQA's style: short calculations with mark schemes (M = method, A = accuracy, B = independent/bookwork mark), multiple-choice items, and short written/evaluative questions. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. An investment of £45,000 generates net cash inflows of £18,000 in Year 1, £15,000 in Year 2 and £20,000 in Year 3. Calculate the payback period (to the nearest month), showing the cumulative cash flow each year. [5 marks]
2. A key limitation of the payback period method is that it: Choose every correct option.
   A. Ignores the time value of money and any cash flows after payback is reached
   B. Cannot be calculated without a computer
   C. Only applies to projects lasting exactly one year
   D. Always favours the project with the highest total cash inflow
3. A project requires an initial investment of £50,000 and generates a net cash inflow of £16,000/year for 4 years. Using discount factors of 0.909, 0.826, 0.751 and 0.683 for years 1-4, calculate the NPV and state whether the project should be accepted. [6 marks]
4. Explain why capital investment appraisal uses cash flows rather than accounting profit. [2 marks]

## Answer key (for the tutor only)
1. [5] M1 cumulative after Year 1 = £18,000; M1 cumulative after Year 2 = 18,000+15,000 = £33,000 (shortfall of £12,000 still to recover); A1 fraction of Year 3 needed = 12000/20,000 = 0.60; A1 payback = 2 years + 7 months (about 2 years 7 months); B1 correct running-total method shown at each year.
2. Correct: A (exactly these options, no others)
3. [6] M1 PV year 1 = 16,000 x 0.909 = £14,544; M1 PV year 2 = 16,000 x 0.826 = £13,216; M1 PV year 3 = 16,000 x 0.751 = £12,016; M1 PV year 4 = 16,000 x 0.683 = £10,928; A1 total PV of inflows = £50,704, NPV = 50,704 - 50,000 = £704; B1 accept, because the NPV is positive, meaning discounted future inflows exceed the initial investment.
4. [2] B1 accounting profit includes non-cash items such as depreciation and is affected by accounting policy choices, so it does not represent the actual cash generated or invested; B1 cash flow is what actually funds the business and provides the return to investors, so it is the relevant measure for deciding whether a project is worth undertaking.

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Capital_Investment_Appraisal` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Incomplete_Records.
