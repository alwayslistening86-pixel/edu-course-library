# ICAEW CFAB: Accounting, Assurance, Business Technology and Finance, Law, Management Information, Principles of Taxation - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
Six mini-papers in sequence, one per module, each in the module's own real proportions: Accounting items from ACC_S01-ACC_S05; Assurance items from ASR_S01-ASR_S04; Business Technology and Finance items from BTF_S01-BTF_S05; Law items from LAW_S01-LAW_S05; Management Information items from MI_S01-MI_S05; Principles of Taxation items from TAX_S01-TAX_S06. Mix single-select, multiple-response and short-calculation/number-entry/scenario items reflecting each module's real question mix, in non-sequential order within each module. The ready-made questions below are a starter bank across all six modules; the tutor writes further items in the same proportions and style to build a complete set of six mini-papers.

## 14 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Accounting] Which are the two fundamental qualitative characteristics of useful financial information under the Conceptual Framework? Choose every correct option.
   A. Relevance
   B. Comparability
   C. Faithful representation
   D. Timeliness
2. [Accounting] A machine costs £20,000, has a residual value of £2,000, and a 4-year useful life. Calculate the annual straight-line depreciation charge. [2 marks]
3. [Assurance] Which distinguishes fraud from error? Choose every correct option.
   A. Fraud is always larger in value than error
   B. Fraud is intentional; error is unintentional
   C. Only error is a misstatement; fraud is not
   D. Error is always committed by management
4. [Assurance] Profit before tax is £600,000. Using a benchmark of 5% of profit before tax, calculate materiality. [2 marks]
5. [Business Technology and Finance] Using Mendelow's power/interest matrix, a stakeholder with high power and high interest should be: Choose every correct option.
   A. given minimal effort
   B. kept informed only
   C. kept satisfied only
   D. managed closely as a key player
6. [Business Technology and Finance] A business borrows £400,000 at a variable rate that rises from 4% to 6.5%. Calculate the extra annual interest cost. [2 marks]
7. [Law] The principle that a registered company is a legal person separate from its shareholders was established in: Choose every correct option.
   A. Donoghue v Stevenson
   B. Salomon v Salomon & Co Ltd
   C. Caparo Industries v Dickman
   D. R v Ghosh
8. [Law] Under the Bribery Act 2010, the only defence to the corporate offence of failing to prevent bribery is: Choose every correct option.
   A. that the organisation did not personally benefit
   B. that the organisation had adequate procedures in place to prevent bribery
   C. that the bribery occurred outside the UK
   D. there is no defence available
9. [Management Information] Selling price is £45/unit, variable cost is £27/unit, and fixed costs are £54,000. Calculate the contribution per unit and the breakeven point in units. [3 marks]
10. [Management Information] Which investment appraisal method(s) account for the time value of money? Choose every correct option.
   A. Payback period
   B. Net present value
   C. Accounting rate of return
   D. None of these
11. [Principles of Taxation] Calculate the 2026/27 income tax liability for an individual with total income of £48,000 (below the personal allowance taper threshold). [4 marks]
12. [Principles of Taxation] An employee earns £52,000 in 2026/27. Calculate their employee Class 1 NIC (8% between £12,570 and £50,270, 2% above). [3 marks]
13. [Principles of Taxation] A business has standard-rated sales (VAT-exclusive) of £70,000 and standard-rated purchases (VAT-exclusive) of £30,000 in a VAT period. Calculate the VAT payable to HMRC (standard rate 20%). [3 marks]
14. [Principles of Taxation] A company has taxable total profits of £45,000 for 2026/27. Calculate its corporation tax liability (small profits rate 19% up to £50,000). [2 marks]

## Answer key for the ready-made items (tutor only)
1. Correct: A, C (exactly these options, no others)
2. [2] M1 (20,000-2,000)/4; A1 = £4,500/year.
3. Correct: B (exactly these options, no others)
4. [2] M1 600,000 x 0.05; A1 = £30,000.
5. Correct: D (exactly these options, no others)
6. [2] M1 400,000 x (0.065-0.04); A1 = £10,000.
7. Correct: B (exactly these options, no others)
8. Correct: B (exactly these options, no others)
9. [3] M1 contribution = 45-27 = £18/unit; A1 breakeven = 54,000/18; A1 = 3,000 units.
10. Correct: B (exactly these options, no others)
11. [4] M1 personal allowance = £12,570 (full); M1 taxable income = 48,000-12,570 = £35,430; M1 this is within the £37,700 basic rate band, taxed at 20%; A1 tax = 35,430 x 20% = £7,086.
12. [3] M1 8% band: (50,270-12,570) x 8% = £3,016; M1 2% band: (52,000-50,270) x 2% = £35; A1 total = £3,051.
13. [3] M1 output VAT = 70,000 x 20% = £14,000; M1 input VAT = 30,000 x 20% = £6,000; A1 VAT payable = £8,000.
14. [2] M1 profits are within the small profits limit; A1 tax = 45,000 x 19% = £8,550.

## Grading
Mark each module separately against `rubric.json`'s `exam_rubric`, then report an overall percentage. A pass needs at least 55% on each of the six modules individually AND at least 55% overall - mirroring ICAEW's real, uniform 55% pass mark, which applies per module (each CFAB module is itself separately pass/fail at 55%), not a lower per-component minimum.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest module and topic areas, offer targeted review, and retry with fresh papers.
