# S11_Advanced_Financial_Management - Test: Advanced financial management

## How to run this
A real checkpoint in the style of this stage's real OU module: calculation questions with full working shown (M/A/B mark tags), short explain/apply questions marked by points, and for the capstone stage an extended professional-report question marked by levels. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A project's NPV is £30,000 at a 12% cost of capital; the present value of its cash inflows at 12% is £180,000. Calculate the percentage fall in cash inflows that would reduce NPV to zero, and explain what this figure tells a decision-maker. [3 marks]
2. Explain, in your own words, MM's no-tax capital structure irrelevance proposition and the intuition behind 'homemade leverage'. [4 marks]
3. Target's standalone value is £4,000,000; Acquirer pays £5,200,000 for it. Combined post-merger value is £11,500,000; Acquirer's own standalone value is £5,500,000. Calculate the synergy created and the net value created for the Acquirer's shareholders after the premium paid. [5 marks]
4. Which real-world factors qualify MM's no-tax capital structure irrelevance result in practice? Choose every correct option.
   A. Bankruptcy/financial distress costs rising with gearing
   B. The tax deductibility of debt interest creating a genuine tax shield
   C. Agency costs between shareholders and debt holders
   D. Perfect, frictionless capital markets with no transaction costs
5. Explain the signalling theory of dividend policy: why might a company cutting its dividend cause its share price to fall by more than the cash value of the missed dividend itself? [3 marks]

## Answer key (for the tutor only)
1. [3] M1 sensitivity = 30,000/180,000; A1 = 16.7%; B1 it tells the decision-maker how much 'headroom' the project has on this variable -- a small percentage means the project's viability is highly sensitive to (say) a sales-volume forecast being even slightly optimistic, and warrants closer scrutiny of that assumption before the project is approved.
2. [4] B2 in a perfect capital market with no taxes, no bankruptcy costs and no transaction costs, a company's overall value depends only on the cash flows its assets generate, not on how those cash flows are divided between debt holders and shareholders; B2 'homemade leverage': an individual investor can replicate any level of personal financial leverage the company itself might choose (e.g. by personally borrowing to buy shares in an ungeared company, mimicking a geared company's risk/return profile), so the company gearing up (or not) adds nothing an investor could not already achieve alone -- which is why, in this idealised setting, capital structure cannot affect value.
3. [5] M1 premium = 5,200,000-4,000,000 = £1,200,000; M1 synergy = 11,500,000-(5,500,000+4,000,000); A1 = £2,000,000; M1 net value created = synergy - premium; A1 = 2,000,000 - 1,200,000 = £800,000.
4. Correct: A, B, C (exactly these options, no others)
5. [3] B1 investors interpret management actions (which have inside knowledge of the company's true prospects) as a costly, hard-to-fake signal, since a company would not cut a dividend lightly if prospects were genuinely fine; B1 a dividend cut is therefore read as bad news about future prospects (e.g. anticipated lower future profits/cash flow), not just the immediate cash forgone; B1 the share price falls to reflect the market's revised, more pessimistic expectation of the company's future cash flows, which can be a far larger effect than the value of the single dividend payment missed.

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Advanced_Financial_Management` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Advanced_Management_Accounting.
