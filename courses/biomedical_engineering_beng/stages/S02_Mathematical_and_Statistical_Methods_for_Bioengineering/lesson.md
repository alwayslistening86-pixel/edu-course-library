# S02_Mathematical_and_Statistical_Methods_for_Bioengineering - Lesson: Mathematical and Statistical Methods for Bioengineering

## Goal
The learner applies first-order differential equations, descriptive and inferential statistics, linear regression and error propagation to physiological and experimental biomedical data.

## Syllabus items taught here
- MM-1 - First-order exponential models (clearance, decay, diffusion)
- MM-2 - Descriptive statistics: mean, standard deviation, standard error
- MM-3 - The normal distribution and confidence intervals
- MM-4 - Linear regression, curve fitting and linearising exponential data
- MM-5 - Propagation of uncertainty
- MM-6 - Hypothesis testing basics and the meaning of a p-value
- MM-7 - Vectors, forces and moments

## How to teach this
Show a raw scatter of drug-concentration-versus-time data and ask: without any statistics, can you tell whether this drug clears the body faster in one patient than another? Then build the tools that make the comparison rigorous. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### MM-1 First-order exponential models (clearance, decay, diffusion)
**First-order exponential models**: many physiological and pharmacokinetic processes follow dC/dt = -kC, solved by C(t) = C0 e^(-kt), where k is a rate constant. This models first-order drug clearance, radioactive decay used in tracer dosimetry, and passive diffusion across a membrane driven by concentration difference. The half-life t(1/2) = ln(2)/k is the time for the quantity to halve, independent of the starting value -- the standard way clinicians and engineers compare clearance rates.

#### MM-2 Descriptive statistics: mean, standard deviation, standard error
**Descriptive statistics**: mean (x-bar = sum(x)/n), sample standard deviation (s = root(sum((x - x-bar)^2)/(n-1))), and standard error of the mean (SEM = s/root(n)) summarise a data set and its uncertainty in the mean. In biomedical measurement, SEM (not s) is quoted alongside a mean when comparing group averages, because it shrinks as more subjects/repeats are added, reflecting increasing confidence in the estimate of the true mean.

#### MM-3 The normal distribution and confidence intervals
**The normal distribution and confidence intervals**: many physiological measurements (height, blood pressure in a population) are approximately normally distributed. For a normal distribution, about 68% of values lie within 1 standard deviation of the mean, 95% within about 1.96 standard deviations. A 95% confidence interval for a mean is x-bar +/- 1.96 x SEM (large-sample approximation) -- the standard way to report an experimental result with its uncertainty.

#### MM-4 Linear regression, curve fitting and linearising exponential data
**Linear regression and curve fitting**: for paired data (x_i, y_i), the least-squares line y = mx + c minimises the sum of squared vertical residuals; the gradient m = sum((x_i - x-bar)(y_i - y-bar)) / sum((x_i - x-bar)^2). The coefficient of determination R^2 measures how much of the variance in y is explained by the linear fit (R^2 = 1 is a perfect fit). Non-linear relationships (e.g. the exponential clearance of MM-1) are commonly linearised by taking logs: ln(C) = ln(C0) - kt is a straight line of gradient -k, letting standard linear regression recover the rate constant from real, noisy data.

#### MM-5 Propagation of uncertainty
**Propagation of uncertainty**: for z = x + y or z = x - y, absolute uncertainties add: delta-z = delta-x + delta-y. For z = xy or z = x/y, percentage (fractional) uncertainties add: delta-z/z = delta-x/x + delta-y/y. For z = x^n, the percentage uncertainty multiplies by n: delta-z/z = n(delta-x/x). This is used throughout biomechanics (e.g. combining an uncertain force measurement with an uncertain lever-arm measurement to get an uncertain moment) exactly as in any experimental science.

#### MM-6 Hypothesis testing basics and the meaning of a p-value
**Hypothesis testing basics**: a two-sample t-test compares the means of two groups (e.g. implant material A vs material B, measured fatigue life) and returns a p-value, the probability of seeing a difference this large (or larger) if there were truly no difference. By convention p < 0.05 is treated as statistically significant. A p-value is not the probability the null hypothesis is true, and statistical significance is not the same as clinical/engineering significance -- a small, real difference can be statistically significant in a large sample without being practically important.

#### MM-7 Vectors, forces and moments
**Vectors and moments (mathematical basis for S05)**: a force is a vector, with magnitude and direction; resultant forces combine by vector (component) addition, Fx = F cos(theta), Fy = F sin(theta). A moment (torque) about a point is M = F x d, where d is the perpendicular distance from the point to the line of action of the force; for equilibrium, the sum of moments about any point is zero as well as the sum of forces in each direction (Sum F = 0, Sum M = 0) -- the two equations solved repeatedly in musculoskeletal biomechanics.

## Explicitly not here
Multivariable calculus, matrix eigenvalue methods and formal proof-based statistics (beyond the A-level Mathematics prerequisite) are out of scope; this stage teaches the specific quantitative toolkit biomedical engineering applies, not mathematics as a subject in its own right.
