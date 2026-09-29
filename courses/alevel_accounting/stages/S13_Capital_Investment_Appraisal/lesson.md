# S13_Capital_Investment_Appraisal - Lesson: Capital investment appraisal

## Goal
The learner identifies relevant cash flows for a capital project and calculates and evaluates the payback period and net present value (NPV), including discounting techniques.

## Syllabus items taught here
- 3.13a - Relevant cash flows in investment appraisal
- QS4 - Investment appraisal outcomes
- 3.13b - Payback period
- QS5 - Payback and NPV, including discounting
- 3.13c - Net present value and discounting

## How to teach this
Ask: why does an investment appraisal use cash flows rather than the accounting profit the project is expected to generate? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.13a Relevant cash flows in investment appraisal
**Relevant cash flows**: capital investment appraisal is based on the incremental **cash flows** a project causes - the initial investment (a cash outflow at the start), then net operating cash inflows over the project's life, and any residual/scrap value at the end - not accounting profit, because profit includes non-cash items (depreciation) and is affected by accounting policy choices, whereas cash is what actually funds the business and rewards investors. Only **relevant** (incremental, future) cash flows are included; costs already committed regardless of the decision (sunk costs) are ignored.

#### QS4 Investment appraisal outcomes
QS4: **calculate investment appraisal outcomes and interpret results** - reading a payback period or NPV figure and explaining, in plain terms, what it means for the decision.

#### 3.13b Payback period
**Payback period**: the time taken for a project's cumulative net cash inflows to equal the initial investment - simple to calculate and understand, and favours projects that recover cash sooner (useful where liquidity or risk of obsolescence matters), but ignores both the time value of money and any cash flows after payback is reached, so it says nothing about a project's overall profitability. *Worked example*: initial investment £100,000, constant net cash inflow £30,000/year: payback = 100,000/30,000 = 3.33 years (about 3 years 4 months).

#### QS5 Payback and NPV, including discounting
QS5: **calculate and apply payback and net present value including the use of discounting techniques** - applying discount factors correctly to convert future cash flows to present value, then summing them for NPV.

#### 3.13c Net present value and discounting
**Net present value (NPV)**: recognises the **time value of money** (a £1 received in the future is worth less than £1 now, because money now could earn a return if invested) by multiplying each year's cash flow by a **discount factor** for the cost of capital and the year in question, then summing the discounted cash flows and deducting the initial investment; a **positive NPV** means the project's discounted inflows exceed the investment, so it should be accepted (it adds value); a negative NPV means it should be rejected. *Worked example*: initial investment £100,000; net cash inflow £30,000/year for 5 years; discount rate 10% (discount factors, to 3 d.p.: 0.909, 0.826, 0.751, 0.683, 0.621 for years 1-5). Present values: £27,273, £24,793, £22,539, £20,490, £18,628; total present value of inflows = £113,724; NPV = 113,724 - 100,000 = £13,724, which is positive, so the project should be accepted on financial grounds. **Benefits and limitations**: NPV accounts for the time value of money and all cash flows over the project's life (payback does not), but it needs a reliable estimate of the cost of capital/discount rate and of future cash flows, both of which are uncertain and get harder to forecast the further into the future they are.

## Explicitly not here
Break-even and short-term marginal costing decisions are S10; ratio-based appraisal of a business's overall performance is S08/S17.
