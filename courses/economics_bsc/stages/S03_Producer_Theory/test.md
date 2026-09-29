# S03_Producer_Theory - Test: Intermediate producer theory

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Q = K^0.4 L^0.6. Find MPL as a function of K and L, and state what the law of diminishing marginal returns implies about the sign of d(MPL)/dL. [3 marks]
2. Explain the cost-minimisation condition MRTS = w/r in words, and what a firm should do if MPL/w > MPK/r. [4 marks]
3. TR = 80Q - 2Q^2, TC = 100 + 8Q + Q^2. Find the profit-maximising Q, the resulting price (from TR/Q if demand is P = 80-2Q), and maximum profit. [5 marks]
4. Explain, using returns to scale, why long-run average cost might fall as a firm expands, then eventually rise. [3 marks]

## Answer key (for the tutor only)
1. [3] M1 MPL = 0.6 K^0.4 L^-0.4; A1 correctly differentiated; B1 diminishing returns implies d(MPL)/dL < 0 (MPL falls as L rises, holding K fixed).
2. [4] B1 MRTS = w/r means the rate at which the firm can technically substitute labour for capital equals the rate the market allows via relative factor prices; B1 at this point no cheaper input combination can produce the same output; B1 if MPL/w > MPK/r, the last pound spent on labour buys more output than the last pound spent on capital; B1 so the firm should use more labour and less capital, moving toward the tangency point.
3. [5] M1 MR = 80-4Q, MC = 8+2Q; M1 equate: 80-4Q=8+2Q; A1 Q = 12; A1 P = 80-2x12 = 56; A1 profit = TR-TC = 672 - 340 = 332.
4. [3] B1 initially increasing returns to scale: doubling inputs more than doubles output, so LRAC falls (economies of scale); B1 at very large scale, coordination/communication problems set in (decreasing returns/diseconomies); B1 giving LRAC a U-shape, with minimum efficient scale at its lowest point.

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Producer_Theory` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Market_Structures_with_Calculus.
