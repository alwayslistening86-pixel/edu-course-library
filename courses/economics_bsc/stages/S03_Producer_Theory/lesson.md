# S03_Producer_Theory - Lesson: Intermediate producer theory

## Goal
The learner uses production functions, marginal product and diminishing returns, isoquants and the marginal rate of technical substitution, derives the cost-minimising input mix (MRTS = w/r), and derives profit maximisation formally (MR = MC) via calculus.

## Syllabus items taught here
- D217-6 - Production functions, marginal product and isoquants
- D217-7 - Cost minimisation: MRTS = w/r
- D217-8 - Long-run cost curves and returns to scale
- D217-9 - Profit maximisation via calculus: MR = MC

## How to teach this
Ask why a firm doesn't just keep adding workers to a fixed factory to raise output indefinitely. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-6 Production functions, marginal product and isoquants
A production function Q = f(K,L) maps capital and labour inputs to output. The marginal product of labour MPL = dQ/dL; the law of diminishing marginal returns says MPL eventually falls as more labour is added to fixed capital. An isoquant shows combinations of K and L yielding the same output; its slope is the marginal rate of technical substitution, MRTS = MPL/MPK. *Example:* Q = K^0.5 L^0.5, at K=16, L=9: MPL = 0.5K^0.5L^-0.5 = 0.5 x 4 / 3 = 0.667.

#### D217-7 Cost minimisation: MRTS = w/r
A cost-minimising firm choosing K and L to produce a given output solves min wL + rK s.t. Q = f(K,L); the Lagrange first-order condition gives MRTS = MPL/MPK = w/r -- the same input-mix logic as the consumer's tangency condition, now for a firm. For Cobb-Douglas Q = K^a L^b, cost minimisation gives the cost-minimising labour-to-capital ratio L/K = (b/a)(r/w). *Example:* a = b = 0.5, w = 10, r = 20: L/K = 1.0*2.0 = 2.0.

#### D217-8 Long-run cost curves and returns to scale
The long-run total cost curve is the envelope of many short-run cost curves, one for each fixed level of capital; at each output the firm has chosen the capital stock that minimises cost for that output. Returns to scale determine the shape of long-run average cost: increasing returns to scale (doubling all inputs more than doubles output) give a falling LRAC -- economies of scale; decreasing returns give a rising LRAC -- diseconomies; constant returns give a flat LRAC. This gives a calculus-based derivation of the U-shaped/economies-of-scale story taught descriptively at A-level.

#### D217-9 Profit maximisation via calculus: MR = MC
Profit π(Q) = TR(Q) - TC(Q) is maximised where dπ/dQ = 0, i.e. MR(Q) = MC(Q), and the second-order condition (MR falling faster than MC, or MC rising faster than MR) confirms a maximum rather than a minimum. *Example:* TR = 100Q - Q^2, TC = 20Q + Q^2/2: MR = 100-2Q, MC = 20+Q; setting equal: 100-2Q = 20+Q, so Q = 26.67, giving π = 1066.7.

## Explicitly not here
Applying MR = MC to specific market structures is S04.
