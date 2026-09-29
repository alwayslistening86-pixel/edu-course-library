# S26_Dimensional_Analysis - Lesson: Dimensional analysis

## Goal
The learner finds the dimensions of quantities, relates units and dimensions, checks equations for dimensional consistency, finds unknown indices by dimensional analysis, and builds models from dimensional arguments.

## Syllabus items taught here
- 6.01a - Dimensions of quantities in terms of M, L and T; dimensionless quantities
- 6.01b - The relationship between units and dimensions
- 6.01c - Dimensional analysis as an error check
- 6.01d - Dimensional analysis to find unknown indices in a proposed formula
- 6.01e - Formulating models using a dimensional argument

## How to teach this
Ask whether the formula 'distance = speed x time^2' could possibly be right. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 6.01a Dimensions of quantities in terms of M, L and T; dimensionless quantities
Dimensions in terms of mass M, length L and time T: velocity [L T^-1]; acceleration [L T^-2]; force [M L T^-2]; energy and work [M L^2 T^-2]; power [M L^2 T^-3]; density [M L^-3]; momentum [M L T^-1]. Angles, ratios, coefficients of friction and restitution are dimensionless.

#### 6.01b The relationship between units and dimensions
Units mirror dimensions: newton = kg m s^-2, joule = kg m^2 s^-2, watt = kg m^2 s^-3. A constant's dimensions follow from the equation it appears in (e.g. G in F = Gm1m2/r^2 has dimensions M^-1 L^3 T^-2).

#### 6.01c Dimensional analysis as an error check
Every term in a valid equation has the same dimensions (and arguments of exp, sin, ln are dimensionless). *Example:* s = ut + (1/2)at^2: [L] = [L T^-1][T] + [L T^-2][T^2], consistent. Consistency doesn't prove a formula correct (dimensionless constants like 1/2 are invisible) but inconsistency proves it wrong.

#### 6.01d Dimensional analysis to find unknown indices in a proposed formula
*Example:* the period of a pendulum t = k m^α l^β g^γ: T = M^α L^β (L T^-2)^γ, so α = 0, β + γ = 0, -2γ = 1: γ = -1/2, β = 1/2, t = k root(l/g). The mass doesn't matter.

#### 6.01e Formulating models using a dimensional argument
Use dimensional reasoning to propose a model, then find the constant by experiment. *Example:* the speed of waves on deep water depends on wavelength λ and g: v = k λ^a g^b gives a = b = 1/2, v = k root(gλ). Predict the effect of changes: quadrupling λ doubles v.

## Explicitly not here
Work and energy are S27.
