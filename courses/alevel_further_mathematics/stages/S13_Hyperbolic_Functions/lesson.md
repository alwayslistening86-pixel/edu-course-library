# S13_Hyperbolic_Functions - Lesson: Hyperbolic functions

## Goal
The learner defines, sketches, differentiates and integrates the hyperbolic functions, uses cosh^2 x - sinh^2 x = 1 and other identities, and works with the inverse hyperbolic functions and their logarithmic forms.

## Syllabus items taught here
- 4.07a - Definitions of sinh, cosh and tanh in terms of exponentials
- 4.07b - Graphs of the hyperbolic functions
- 4.07c - The identity cosh^2 x - sinh^2 x = 1 and other identities
- 4.07d - Differentiating and integrating hyperbolic functions
- 4.07e - Inverse hyperbolic functions: definitions, domains and ranges
- 4.07f - Logarithmic forms of the inverse hyperbolic functions

## How to teach this
Ask what shape a hanging chain makes, and show that it's cosh, not a parabola. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.07a Definitions of sinh, cosh and tanh in terms of exponentials
sinh x = (e^x - e^(-x))/2; cosh x = (e^x + e^(-x))/2; tanh x = sinh x/cosh x = (e^(2x) - 1)/(e^(2x) + 1).

#### 4.07b Graphs of the hyperbolic functions
sinh x: odd, passes through O, increasing, range all reals. cosh x: even, minimum (0, 1), range ≥ 1. tanh x: odd, through O, horizontal asymptotes y = ±1.

#### 4.07c The identity cosh^2 x - sinh^2 x = 1 and other identities
cosh^2 x - sinh^2 x = 1 (from the definitions). Others follow: sinh 2x = 2sinh x cosh x; cosh 2x = cosh^2 x + sinh^2 x = 2cosh^2 x - 1 = 1 + 2sinh^2 x. (Osborn's rule: a trig identity becomes a hyperbolic one if you change the sign of every product of two sines.) *Example:* solve 2cosh x - sinh x = 2. In exponentials: (e^x + e^(-x)) - (e^x - e^(-x))/2 = 2, so e^x + 3e^(-x) = 4, e^(2x) - 4e^x + 3 = 0, e^x = 1 or 3, giving x = 0 or x = ln 3.

#### 4.07d Differentiating and integrating hyperbolic functions
d/dx sinh x = cosh x; d/dx cosh x = sinh x; d/dx tanh x = sech^2 x. So ∫cosh x dx = sinh x + c, ∫sinh x dx = cosh x + c. *Example:* ∫ (0 to ln 2) cosh 2x dx = [sinh 2x/2] = sinh(2 ln 2)/2 = (4 - 1/4)/4 = 15/16.

#### 4.07e Inverse hyperbolic functions: definitions, domains and ranges
arsinh x (all real x, all real outputs); arcosh x (x ≥ 1, output ≥ 0, the principal value); artanh x (-1 < x < 1, all real outputs).

#### 4.07f Logarithmic forms of the inverse hyperbolic functions
arsinh x = ln(x + root(x^2 + 1)); arcosh x = ln(x + root(x^2 - 1)) (x ≥ 1); artanh x = (1/2) ln((1 + x)/(1 - x)) (|x| < 1). Derivation: y = arsinh x, x = sinh y, e^(2y) - 2xe^y - 1 = 0, e^y = x + root(x^2 + 1) (the positive root). *Example:* arcosh 2 = ln(2 + root3) = 1.3170.

## Explicitly not here
Integrals leading to inverse hyperbolic functions are S15.
