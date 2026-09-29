# S07_National_Income_and_IS_LM - Lesson: National income accounting and the IS-LM model

## Goal
The learner uses the three approaches to measuring GDP, distinguishes nominal from real GDP via the GDP deflator, derives the Keynesian multiplier, and derives and solves the IS and LM curves for equilibrium income and the interest rate.

## Syllabus items taught here
- D217-21 - GDP measurement, nominal vs real GDP, the GDP deflator
- D217-22 - The Keynesian multiplier
- D217-23 - Deriving the IS curve
- D217-24 - Deriving the LM curve and IS-LM equilibrium

## How to teach this
Ask why a £10bn rise in government spending typically raises GDP by more than £10bn. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-21 GDP measurement, nominal vs real GDP, the GDP deflator
GDP can be measured by expenditure (C+I+G+NX), income (sum of factor incomes: wages, profits, rent, interest) or output (value added across all industries); all three give the same total by construction. Nominal GDP values output at current prices; real GDP values it at constant (base-year) prices, removing the effect of inflation. The GDP deflator = (nominal GDP / real GDP) x 100 measures economy-wide price change. *Example:* nominal GDP £2,200bn, real GDP £2,000bn: deflator = 110, i.e. prices have risen 10% since the base year.

#### D217-22 The Keynesian multiplier
The Keynesian income-expenditure model: equilibrium output is where planned aggregate expenditure equals output, Y = C+I+G+NX, with consumption C = C0 + cY (c = the marginal propensity to consume, MPC). An autonomous spending injection ΔA raises equilibrium income by more than itself: the multiplier k = 1/(1-MPC) (or 1/MPS, since MPS = 1-MPC in the simplest closed model), because the initial spending becomes someone else's income, part of which is re-spent, and so on. *Example:* MPC = 0.75: multiplier = 1/(1-0.75) = 4; a £10bn rise in G raises equilibrium Y by £40bn.

#### D217-23 Deriving the IS curve
The IS curve plots combinations of the interest rate (r) and income (Y) at which the goods market clears (planned spending = output). Investment is decreasing in r (I(r) = I0 - br); a higher interest rate lowers planned investment, lowering equilibrium income via the multiplier -- so IS slopes downward. Anything that shifts autonomous spending (fiscal policy, consumer/business confidence, net exports) shifts the whole IS curve; a movement along IS is caused only by a change in r.

#### D217-24 Deriving the LM curve and IS-LM equilibrium
The LM curve plots combinations of r and Y at which the money market clears: real money supply (M/P) equals real money demand, which rises with income (transactions demand) and falls with the interest rate (opportunity cost of holding money) -- so LM slopes upward. IS-LM equilibrium is the (r, Y) pair solving both equations simultaneously. *Example:* IS: Y = 500 - 20r; LM: Y = 300 + 10r. Setting equal: 500-20r = 300+10r, r = 6.67, Y = 366.7. Expansionary monetary policy shifts LM right (lower r, higher Y); expansionary fiscal policy shifts IS right (higher r, higher Y) -- the interest-rate rise from fiscal expansion partly crowds out private investment.

## Explicitly not here
Aggregate supply and expectations are S08.
