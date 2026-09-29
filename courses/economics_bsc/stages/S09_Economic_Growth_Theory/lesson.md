# S09_Economic_Growth_Theory - Lesson: Economic growth theory (the Solow model)

## Goal
The learner sets up the Solow growth model (production function, capital accumulation, steady state), finds the steady-state capital-labour ratio, states the golden rule savings rate, and explains sources of long-run growth including the convergence hypothesis and endogenous growth theory.

## Syllabus items taught here
- D217-28 - The Solow model: production and capital accumulation
- D217-29 - The Solow steady state and the golden rule
- D217-30 - Convergence and endogenous growth theory

## How to teach this
Ask why pouring ever more capital into an economy with a fixed workforce eventually stops raising output per worker much at all. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-28 The Solow model: production and capital accumulation
The Solow model: output per worker y = f(k), where k = K/L is capital per worker, typically y = k^a (a Cobb-Douglas production function in per-worker terms, 0<a<1, exhibiting diminishing marginal product of capital). Capital accumulates as Δk = sy - (d+n)k, where s is the savings rate, d the depreciation rate and n the population growth rate: savings per worker (sy) adds to capital, while depreciation and a growing population both dilute the existing capital stock. *Example:* y = k^0.5, s=0.2, d=0.05, n=0.02: at k=25, sy = 0.2x5 = 1.0, and (d+n)k = 0.07x25 = 1.75, so Δk = -0.75 (capital still rising, not yet at steady state).

#### D217-29 The Solow steady state and the golden rule
The steady state is where Δk = 0: sy* = (d+n)k*, i.e. investment exactly replaces depreciation and dilution, so capital and output per worker stop changing (absent further shocks). With y=k^0.5: s k*^0.5 = (d+n)k*, so k*^0.5 = s/(d+n), k* = (s/(d+n))^2. *Example:* s=0.2, d=0.05, n=0.02: k* = (0.2/0.07)^2 = 8.2, y* = 2.86. The golden rule savings rate maximises steady-state consumption per worker (c* = y*-(d+n)k*); it is found where the marginal product of capital equals (d+n), not simply by maximising output.

#### D217-30 Convergence and endogenous growth theory
In the basic Solow model, sustained long-run growth in output per worker comes only from technological progress (an exogenous shift in the production function), since capital accumulation alone runs into diminishing returns at the steady state. The (conditional) convergence hypothesis: poorer countries with similar savings rates, population growth and technology tend to grow faster (diminishing returns mean capital is more productive where it is scarcer), closing the income gap with richer countries over time -- evidence for convergence is much stronger within similar institutional/policy groups than unconditionally across all countries. Endogenous growth theory (e.g. Romer, Lucas) treats technological progress and human capital as themselves the outcome of economic choices (R&D investment, education), potentially avoiding the diminishing-returns limit and explaining why growth rates can persist or even rise, extending Solow's treatment of technology as an unexplained exogenous input.

## Explicitly not here
Applying growth and macro theory to the open economy is S10.
