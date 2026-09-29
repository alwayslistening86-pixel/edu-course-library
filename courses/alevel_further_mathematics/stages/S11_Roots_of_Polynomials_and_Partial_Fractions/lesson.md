# S11_Roots_of_Polynomials_and_Partial_Fractions - Lesson: Roots of polynomials and further partial fractions

## Goal
The learner uses relationships between roots and coefficients of polynomials up to quartics, forms equations with transformed roots by substitution, and splits rational functions with quadratic factors or improper numerators into partial fractions.

## Syllabus items taught here
- 4.05a - Relationships between the roots and coefficients of polynomial equations (up to quartic)
- 4.05b - Substitutions to form an equation with roots related to those of a given equation
- 4.05c - Partial fractions with quadratic factors ax^2 + c, and improper fractions

## How to teach this
Ask what the sum and product of the roots of x^2 - 7x + 10 = 0 are, and whether you needed to solve it. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.05a Relationships between the roots and coefficients of polynomial equations (up to quartic)
For az^2 + bz + c = 0: α + β = -b/a, αβ = c/a. Cubic az^3 + bz^2 + cz + d = 0: Σα = -b/a, Σαβ = c/a, αβγ = -d/a. Quartic: Σα = -b/a, Σαβ = c/a, Σαβγ = -d/a, αβγδ = e/a. Useful identity: α^2 + β^2 + γ^2 = (Σα)^2 - 2Σαβ. *Example:* 2x^3 - 3x^2 + 4x - 5 = 0: Σα = 3/2, Σαβ = 2, αβγ = 5/2; Σα^2 = 9/4 - 4 = -7/4 (so not all roots are real).

#### 4.05b Substitutions to form an equation with roots related to those of a given equation
To find an equation with roots 2α, 2β, 2γ: substitute w = 2x, i.e. x = w/2, into the original. For roots α + 1: x = w - 1. For roots α^2: x = root w, then rearrange to remove the root. *Example:* x^3 - 3x + 1 = 0 with roots α, β, γ; for roots 3α etc.: (w/3)^3 - 3(w/3) + 1 = 0, i.e. w^3 - 27w + 27 = 0.

#### 4.05c Partial fractions with quadratic factors ax^2 + c, and improper fractions
A quadratic factor ax^2 + c (c > 0) takes a numerator Bx + C. *Example:* (5x^2 + 2x + 3)/((x + 1)(x^2 + 1)) = A/(x + 1) + (Bx + C)/(x^2 + 1): 2x/(x^2 + 1) + 3/(x + 1). If the numerator's degree ≥ the denominator's, divide first: (x^3 + 2)/(x^2 - 1) = x + (x + 2)/(x^2 - 1) = x - 1/(2(x + 1)) + 3/(2(x - 1)).

## Explicitly not here
Integrating these partial fractions is S15.
