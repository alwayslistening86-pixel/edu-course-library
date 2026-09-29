# S05_Financial_Management - Lesson: Financial management

## Goal
The learner compares sources of finance and gearing, calculates the cost of equity (CAPM and the dividend growth model), the cost of debt and the WACC, manages working capital via the cash operating cycle, appraises investments with payback/ARR/NPV/IRR, values a business by several methods, and explains basic FX and interest-rate risk management -- matching Financial Management (B252).

## Syllabus items taught here
- B252-1 - Sources of finance and gearing
- B252-2 - Cost of equity (CAPM, dividend growth model) and cost of debt
- B252-3 - WACC
- B252-4 - Working capital management and the cash operating cycle
- B252-5 - Investment appraisal: payback, ARR, NPV, IRR
- B252-6 - Business valuation methods
- B252-7 - FX and interest rate risk management

## How to teach this
Ask: why might a company prefer to raise £5m by issuing new shares rather than borrowing it, even though debt is usually cheaper? Teach each topic by building on what A-level Accounting and A-level Mathematics already gave the learner: name the A-level idea it extends (e.g. A-level Accounting's basic financial statements, before IAS 2/IAS 16/IFRS 15/IFRS 16 formalise specific standards), then show the IFRS-specific technical treatment or quantitative technique degree-level accounting/finance adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. UK tax figures (S13) are the 2026/27 tax year; always check HMRC's current published rates before relying on a real-world tax calculation, since UK tax rates/thresholds/allowances change at least annually.

#### B252-1 Sources of finance and gearing
**Sources of finance**: short-term (overdraft, trade credit) versus long-term (ordinary shares, preference shares, debt -- bank loans, bonds/debentures, finance leases). Equity carries no obligation to pay a fixed return and no repayment date, but dilutes ownership/control and is the most expensive form of finance (shareholders bear the most risk, so require the highest return); debt is cheaper (interest is tax-deductible, and lenders rank ahead of shareholders on a winding-up) but adds a fixed obligation (interest, and usually repayment) and financial risk. **Gearing** = debt/(debt + equity), by book or market value: higher gearing raises the fixed interest burden relative to earnings, increasing the risk that a downturn leaves too little profit to cover interest (and, in the extreme, the risk of insolvency) -- but for a stable, profitable company can also raise the return to shareholders (financial leverage) when the return on the borrowed funds exceeds its after-tax cost.

#### B252-2 Cost of equity (CAPM, dividend growth model) and cost of debt
**Cost of equity** can be estimated with the **Capital Asset Pricing Model (CAPM)**: Ke = Rf + beta x (Rm - Rf), where Rf is the risk-free rate, Rm the expected market return and beta the share's systematic (market) risk relative to the market. *Example*: Rf = 4%, Rm = 9%, beta = 1.2: Ke = 4% + 1.2 x (9%-4%) = 10.0%. Alternatively the **dividend growth model** estimates Ke = D1/P0 + g (next year's dividend over current share price, plus the assumed constant dividend growth rate). *Example*: D0 = 20p, growth g = 3%, P0 = 250p: D1 = 20 x 1.03 = 20.6p; Ke = 20.6/250 + 0.03 = 0.1124, i.e. 11.24%. The **cost of debt** (irredeemable, after tax) = interest rate x (1 - tax rate); e.g. 8% debt with a 25% corporation tax rate costs 6.0% after tax, since interest is a tax-deductible expense.

#### B252-3 WACC
The **weighted average cost of capital (WACC)** blends the cost of each finance source by its proportion of total (market value) finance: WACC = (E/(E+D)) x Ke + (D/(E+D)) x Kd(1-T). *Example*: market value of equity £6,000,000, market value of debt £4,000,000, Ke = 12%, after-tax Kd = 6%: WACC = (6000000/10000000) x 12% + (4000000/10000000) x 6% = 9.60%. WACC is the discount rate normally used to appraise a new project of similar risk to the company's existing operations (a project of materially different risk needs its own project-specific discount rate, since it does not share the same systematic risk as the rest of the firm).

#### B252-4 Working capital management and the cash operating cycle
**Working capital management**: the **cash operating cycle** = inventory holding period + receivables collection period - payables payment period (in days), measuring how long cash is tied up before it is recovered from customers. *Example*: inventory period 60 days, receivables period 45 days, payables period 30 days: cash operating cycle = 60+45-30 = 75 days. A shorter cycle frees up cash (e.g. negotiating faster receivables collection, slower supplier payment within agreed terms, or tighter inventory control), but pushing too hard (e.g. very tight credit terms) risks losing customers or supplier goodwill -- working capital policy is a trade-off between liquidity/risk and profitability, not a pure minimisation exercise.

#### B252-5 Investment appraisal: payback, ARR, NPV, IRR
**Investment appraisal**: **payback period** = time for cumulative cash inflows to recover the initial investment (simple, ignores the time value of money and cash flows after payback); **accounting rate of return (ARR)** = average annual accounting profit/average (or initial) investment, expressed as a percentage (uses accounting profit, not cash flow, and also ignores the time value of money); **net present value (NPV)** discounts each year's cash flow at the cost of capital and sums them, less the initial outlay -- accept if NPV > 0 (it is the theoretically preferred method: it uses cash flows, the time value of money, and directly measures the increase in shareholder wealth); **internal rate of return (IRR)** is the discount rate at which NPV = 0. *Worked example, NPV*: initial outlay £200,000, cash inflow £70,000 a year for 4 years, cost of capital 10%: annuity factor = (1-1.1^-4)/0.10 = 3.1699; NPV = 70,000 x 3.1699 - 200,000 = £21,891 -- positive, so the project is worth accepting at this cost of capital.

#### B252-6 Business valuation methods
**Business valuation methods**: **asset-based** (net assets at book or, better, fair/realisable value -- a floor value, ignoring the business's earning potential as a going concern); **P/E-based** (value = earnings x a comparable listed company's price/earnings multiple); **dividend valuation model** (for a minority shareholding, value per share = D1/(Ke-g), the Gordon growth/perpetuity model); **discounted cash flow (DCF)** (present value of the business's projected future free cash flows -- most theoretically sound for a controlling interest, but highly sensitive to the growth and discount-rate assumptions). *Worked example, dividend valuation*: D1 = 15p, Ke = 11%, g = 3%: value per share = 15/(0.11-0.03) = 187.5p.

#### B252-7 FX and interest rate risk management
**FX and interest rate risk management**: **transaction risk** (an FX-denominated receivable/payable's home-currency value changes before settlement) can be hedged with a **forward contract** (locking today the exchange rate for a future date) or, for more flexibility at a premium cost, a **currency option**. *Example*: a UK exporter expects to receive $500,000 in 3 months and locks a forward rate of $1.25/£1: guaranteed sterling receipt = 500,000/1.25 = £400,000, removing the uncertainty of the spot rate on the payment date (at the cost of giving up any upside if sterling weakens instead). **Interest rate risk** (on variable-rate borrowing) can similarly be hedged with an interest rate swap (exchanging variable for fixed interest payments) or a forward rate agreement, converting uncertain future interest cost into a known, fixed cost.

## Explicitly not here
Costing methods, budgeting and variance analysis (Intermediate Management Accounting) are S06-S07.
