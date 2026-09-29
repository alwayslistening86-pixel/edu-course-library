# S08_Aggregate_Supply_Expectations_Phillips - Lesson: Aggregate supply, expectations and the Phillips curve

## Goal
The learner distinguishes short-run from long-run aggregate supply, explains the expectations-augmented Phillips curve and NAIRU, contrasts adaptive and rational expectations, and explains the time-inconsistency problem in monetary policy.

## Syllabus items taught here
- D217-25 - Short-run vs long-run aggregate supply
- D217-26 - The expectations-augmented Phillips curve and NAIRU
- D217-27 - Adaptive vs rational expectations; time inconsistency

## How to teach this
Ask why a central bank that repeatedly surprises people with inflation eventually stops being able to boost output at all, even temporarily. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-25 Short-run vs long-run aggregate supply
Short-run aggregate supply (SRAS) slopes upward: with some prices/wages sticky in the short run, a rise in the price level raises firms' profit margins temporarily, so they raise output. Long-run aggregate supply (LRAS) is vertical at potential/natural output: in the long run, wages and prices fully adjust, so output depends only on real factors (capital, labour, technology), not the price level. A demand-side shock moves output away from potential in the short run (along SRAS) but only changes prices, not output, once expectations and contracts adjust (the economy returns to LRAS).

#### D217-26 The expectations-augmented Phillips curve and NAIRU
The original (Phillips) curve showed an apparent stable trade-off between inflation and unemployment. The expectations-augmented Phillips curve (Friedman/Phelps) adds expected inflation: pi = pi^e - a(u - u*), where u* is the natural rate of unemployment (NAIRU). Only unanticipated inflation (actual above expected) is associated with unemployment below the natural rate; if expectations fully adjust (pi^e = pi), unemployment returns to u* regardless of the inflation rate -- the long-run Phillips curve is vertical at NAIRU. *Example:* a=0.5, u*=4.5%, pi^e=2%: if u=3%, pi = 2 + 0.5x(4.5-3) = 2.75%.

#### D217-27 Adaptive vs rational expectations; time inconsistency
Adaptive expectations form expected inflation from past inflation (backward-looking, e.g. pi^e_t = pi_t-1); rational expectations use all available information, including the announced policy rule, to form an unbiased forecast (forward-looking) -- under rational expectations, only unanticipated (surprise) policy can move output/unemployment even temporarily. Time inconsistency: a central bank that promises low inflation has an incentive to renege once wages/expectations are set (surprise inflation temporarily boosts output), but if this is anticipated, the promise isn't credible and expected (and actual) inflation ends up higher with no output gain -- the case for central bank independence and inflation targeting as credible commitment devices.

## Explicitly not here
Long-run growth is S09.
