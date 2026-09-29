# S09_Economic_Growth_Theory - Test: Economic growth theory (the Solow model)

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain, using the Solow model's capital-accumulation equation, why an economy with a higher population growth rate has a lower steady-state capital per worker, other things equal. [4 marks]
2. y=k^0.5, s=0.3, d=0.04, n=0.01. Find the steady-state k* and y*. [4 marks]
3. Explain the conditional convergence hypothesis and why unconditional convergence across all countries is not strongly observed in the data. [4 marks]
4. Explain, in your own words, the key difference between the Solow model's treatment of technological progress and endogenous growth theory's. [3 marks]

## Answer key (for the tutor only)
1. [4] B1 Δk = sy - (d+n)k: population growth (n) is part of the 'dilution' term alongside depreciation; B1 a higher n means a given capital stock has to be spread across more workers, requiring more investment just to maintain the same capital per worker; B1 at any k, a higher n raises (d+n)k, so the break-even investment line is steeper; B1 the steady state (where sy meets (d+n)k) therefore occurs at a lower k*.
2. [4] M1 k*^0.5 = 0.3/0.05; A1 k* = 36.0; M1 y* = k*^0.5; A1 y* = 6.0.
3. [4] B1 conditional convergence: countries with similar savings rates, population growth and technology/institutions converge to the same steady state, so poorer ones among them grow faster (diminishing returns to capital); B1 this is 'conditional' on those structural characteristics being similar; B1 countries differ hugely in institutions, human capital, technology access and policy; B1 so unconditional convergence (all poor countries catching up regardless of these differences) is much weaker in the data than convergence within similar groups.
4. [3] B1 Solow treats technological progress as exogenous (unexplained, simply assumed to happen at some rate); B1 endogenous growth theory treats it (and human capital accumulation) as arising from economic decisions, e.g. R&D spending, education; B1 this matters because it means policy (subsidising research, education) can, in endogenous models, affect the long-run growth rate itself, not just the level of output.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Economic_Growth_Theory` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Open_Economy_Macroeconomics.
