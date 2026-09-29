# S05_Financial_Management - Test: Financial management

## How to run this
A real checkpoint in the style of this stage's real OU module: calculation questions with full working shown (M/A/B mark tags), short explain/apply questions marked by points, and for the capstone stage an extended professional-report question marked by levels. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. D0 = 25p, expected constant growth g = 4%, current share price P0 = 300p. Calculate the cost of equity using the dividend growth model. [3 marks]
2. Market value of equity £8,000,000, market value of debt £2,000,000, Ke = 11%, after-tax cost of debt = 5%. Calculate the WACC. [4 marks]
3. Initial investment £150,000; cash inflows £45,000 a year for 5 years; cost of capital 8%. Calculate the NPV and state whether the project should be accepted. [5 marks]
4. Explain why NPV is regarded as theoretically superior to the payback period as an investment appraisal method, giving two reasons. [4 marks]
5. A UK exporter expecting a US dollar receipt in 6 months wants to remove exchange rate uncertainty. Which is a valid way to do this? Choose every correct option.
   A. Enter a forward contract to sell the expected dollars for sterling at an agreed rate today
   B. Buy a currency option giving the right (not obligation) to sell the dollars at an agreed rate
   C. Do nothing and hope the exchange rate does not move
   D. Increase the company's gearing

## Answer key (for the tutor only)
1. [3] M1 D1 = 25 x 1.04 = 26.0p; M1 Ke = 26.0/300 + 0.04; A1 = 12.67%.
2. [4] M1 equity weight = 8,000,000/10,000,000 = 0.8; M1 debt weight = 0.2; M1 WACC = 0.8x11 + 0.2x5; A1 = 9.80%.
3. [5] M1 annuity factor = (1-1.08^-5)/0.08 = 3.9927; M1 PV of inflows = 45,000 x 3.9927 = £179,672; A1 NPV = 179,672 - 150,000 = £29,672; A1 positive NPV; B1 accept the project, since a positive NPV at the company's cost of capital increases shareholder wealth.
4. [4] B2 any two of: NPV accounts for the time value of money (a pound today is worth more than a pound in the future) while payback does not discount cash flows at all; NPV considers all cash flows over the project's life, while payback ignores everything after the payback date; NPV directly measures the absolute increase in shareholder wealth in present-value terms, which is the finance objective, while payback only measures how quickly cash is recovered, saying nothing about overall profitability; B2 a second distinct valid reason, explained.
5. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Financial_Management` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Management_Accounting_I_Costing_and_Budgeting.
