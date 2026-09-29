# S01_Quantitative_Tools_for_Economics - Lesson: Quantitative bridge: calculus and optimisation for economics

## Goal
The learner uses derivatives to find marginal functions and optima, partial derivatives and the Lagrange-multiplier method for constrained optimisation, compound/percentage growth, and the point (calculus) definition of elasticity -- the mathematical toolkit intermediate economics assumes beyond A-level.

## Syllabus items taught here
- MQ1 - Marginal functions via differentiation
- MQ2 - Constrained optimisation and the Lagrange multiplier
- MQ3 - Compound growth and logarithmic growth rates
- MQ4 - Point (calculus) elasticity

## How to teach this
Ask what 'marginal' meant at A-level (the next unit), then show that it is exactly the derivative of the corresponding total function. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### MQ1 Marginal functions via differentiation
A-level economics defines marginal cost/utility/revenue as the change from one more unit; degree-level economics treats output as continuous and uses calculus: marginal cost MC(Q) = dTC/dQ. *Example:* TC(Q) = Q^3 - 6Q^2 + 15Q + 10 gives MC(Q) = 3Q^2 - 12Q + 15; at Q = 4, MC = 15. A total function is minimised/maximised where its derivative is zero and the second derivative has the appropriate sign (positive = minimum, negative = maximum): AC(Q) = TC/Q is minimised where MC = AC, found by setting d(AC)/dQ = 0.

#### MQ2 Constrained optimisation and the Lagrange multiplier
Constrained optimisation (e.g. a consumer maximising utility subject to a budget, or a firm minimising cost subject to an output target) is solved with the Lagrange-multiplier method: form L = f(x,y) + lambda(constraint), set every partial derivative to zero, and solve. *Example:* maximise U(x,y) = xy subject to Pxx + Pyy = I. The first-order conditions give y/Px = x/Py = lambda, so Pxx = Pyy, and substituting into the budget constraint gives x* = I/(2Px), y* = I/(2Py). With Px = 2, Py = 4, I = 100: x* = 25.0, y* = 12.5.

#### MQ3 Compound growth and logarithmic growth rates
Percentage growth over several periods compounds rather than adds: a variable growing at rate g for n periods becomes (1+g)^n times its start value. *Example:* GDP growing at 2.5% a year for 10 years rises by a factor of 1.280, i.e. by 28.0%, not 10 x 2.5% = 25%. For small growth rates, ln(1+g) is approximately g, which is why economists often work in logs: the growth rate between two periods is approximately the difference in their logs, ln(Y_t) - ln(Y_t-1).

#### MQ4 Point (calculus) elasticity
A-level's arc elasticity (using %ΔQ and %ΔP over a finite change) approximates the point elasticity used at degree level: e = (dQ/dP) x (P/Q), the derivative of the demand function times the price-to-quantity ratio at that exact point. *Example:* Q = 100 - 2P; dQ/dP = -2. At P = 20 (so Q = 60), point PED = -0.667. Point elasticity is exact at a point, unlike the arc method's average over a range; the two converge as the price change shrinks toward zero.

## Explicitly not here
Applying these tools to consumer choice is S02.
