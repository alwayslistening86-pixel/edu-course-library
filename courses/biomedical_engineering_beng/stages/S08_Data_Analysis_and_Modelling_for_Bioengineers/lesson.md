# S08_Data_Analysis_and_Modelling_for_Bioengineers - Lesson: Data Analysis and Modelling for Bioengineers

## Goal
The learner builds and fits simple compartmental and scaling models of physiological/pharmacokinetic processes to data, and applies dimensional and error analysis to check a biomedical engineering model's validity.

## Syllabus items taught here
- DA-1 - One-compartment pharmacokinetic modelling
- DA-2 - Fitting a compartmental model to data by linearisation
- DA-3 - Paired vs two-sample experimental comparisons
- DA-4 - Dimensional analysis and allometric scaling
- DA-5 - Applied uncertainty propagation through a model
- DA-6 - Model validation with residual plots

## How to teach this
Ask how a single blood sample taken every hour after an injection can be turned into a confident statement of how fast a drug clears the body, complete with a stated uncertainty -- this stage supplies exactly that pipeline. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### DA-1 One-compartment pharmacokinetic modelling
**One-compartment pharmacokinetic model**: the body (or a body region) is modelled as a single well-mixed compartment of volume Vd (the "volume of distribution", an apparent, not necessarily anatomical, volume) from which a drug of amount A(t) is eliminated at a rate proportional to the amount present, dA/dt = -kA, exactly the S02 first-order model. Plasma concentration C(t) = A(t)/Vd, so C(t) = C0 e^(-kt); clearance CL = k x Vd is the volume of plasma effectively cleared of drug per unit time, the standard pharmacokinetic parameter reported for a drug.

#### DA-2 Fitting a compartmental model to data by linearisation
**Fitting the model to real data**: given several (time, concentration) measurements, taking ln(C) and performing linear regression (S02, MM-4) against t recovers ln(C0) as the intercept and -k as the gradient; the R^2 of that linear fit indicates how well the one-compartment assumption describes the data (a poor R^2 signals the process may need a two-compartment model, outside this stage's scope, rather than that the arithmetic was wrong).

#### DA-3 Paired vs two-sample experimental comparisons
**Two-sample and paired comparisons in biomedical experiments**: choosing between a two-sample (independent groups, e.g. drug vs placebo in different patients) and a paired (e.g. before/after measurement in the same patient) statistical comparison matters because a paired test removes between-subject variability that would otherwise inflate the apparent scatter, generally giving more statistical power to detect a real effect from the same number of measurements -- an experimental-design decision as important as the statistical test itself.

#### DA-4 Dimensional analysis and allometric scaling
**Dimensional analysis and scaling**: checking that both sides of a physiological equation have the same physical dimensions (as in S02's homogeneity check) catches many modelling errors before any numbers are plugged in. Allometric scaling relates a physiological quantity Y to body mass M by a power law Y = a M^b (e.g. basal metabolic rate scales roughly as M^0.75, "Kleber's law") -- used to scale a drug dose, or an engineering design load, from an animal model or average adult to an individual patient of different body mass.

#### DA-5 Applied uncertainty propagation through a model
**Uncertainty propagation through a model (applied)**: if clearance CL = k x Vd, and k is known to +/-5% and Vd to +/-8% (both from independent experimental measurements), the percentage uncertainty in CL is found by adding the percentage uncertainties (S02, MM-5, product rule): 5% + 8% = 13%. Reporting a clinical or engineering parameter without its propagated uncertainty (e.g. "clearance is 3.2 L/h" rather than "clearance is 3.2 +/- 0.4 L/h") is treated in this course as an incomplete answer, matching real experimental-science practice.

#### DA-6 Model validation with residual plots
**Model validation and residuals**: after fitting a model, plotting the residuals (measured value minus model-predicted value) against time or against the predicted value reveals systematic problems a single R^2 or correlation coefficient can hide -- e.g. residuals that trend from positive to negative to positive again (rather than scattering randomly around zero) indicate the model form itself is wrong (e.g. a single-exponential model fitted to genuinely two-compartment data), not just measurement noise.

## Explicitly not here
Multi-compartment (two- or three-compartment) pharmacokinetic modelling, non-linear least-squares fitting algorithms and formal statistical software workflows are out of scope; this stage builds the single-compartment, linearised-fitting toolkit by hand.
