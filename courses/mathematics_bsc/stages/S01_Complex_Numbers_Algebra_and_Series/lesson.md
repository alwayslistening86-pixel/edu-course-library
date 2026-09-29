# S01_Complex_Numbers_Algebra_and_Series - Lesson: Complex numbers, algebra and series

## Goal
The learner converts between Cartesian and polar form, applies De Moivre's theorem to find roots and multiple angles, uses Euler's formula, factorises real polynomials over C, and determines convergence of series including Taylor expansions.

## Syllabus items taught here
- 1a - Complex numbers: Cartesian and polar (modulus-argument) form, arithmetic and the Argand diagram
- 1b - De Moivre's theorem; nth roots of a complex number
- 1c - The complex exponential e^{i theta} and Euler's formula; e^{i pi} + 1 = 0
- 1d - The Fundamental Theorem of Algebra; factorising real polynomials over C using conjugate root pairs
- 1e - Sequences and series: convergence, the ratio test, Taylor/Maclaurin series of standard functions

## How to teach this
Ask the learner to plot 1+i on an Argand diagram and read off its modulus and argument before any formula is given. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 1a Complex numbers: Cartesian and polar (modulus-argument) form, arithmetic and the Argand diagram
A complex number z = a + bi has real part a, imaginary part b, modulus |z| = root(a^2+b^2), and argument arg(z) = theta where a = |z|cos(theta), b = |z|sin(theta) (theta in (-pi, pi], the principal value). Polar (modulus-argument) form: z = r(cos theta + i sin theta) = r cis theta. To multiply, multiply moduli and add arguments; to divide, divide moduli and subtract arguments. *Example:* z1 = 1+i has modulus root2 and argument pi/4; z2 = root3 - i has modulus 2 and argument -pi/6. z1 z2 has modulus 2root2 and argument pi/4 - pi/6 = pi/12. On the Argand diagram, the real axis is horizontal and the imaginary axis vertical; multiplication by i rotates a point by pi/2 anticlockwise.

#### 1b De Moivre's theorem; nth roots of a complex number
De Moivre's theorem: (cos theta + i sin theta)^n = cos(n theta) + i sin(n theta) for any integer n. It is used both to expand cos(n theta)/sin(n theta) in terms of powers of cos theta and sin theta (e.g. expanding (cis x)^5 and taking the real part gives cos 5x = 16 cos(x)^5 - 20 cos(x)^3 + 5 cos(x)), and, in reverse, to find the n distinct nth roots of a complex number w = R cis phi: they are R^(1/n) cis((phi + 2k pi)/n) for k = 0, 1, ..., n-1, equally spaced round a circle of radius R^(1/n). *Example:* the cube roots of -8 (modulus 8, argument pi): computing directly with sympy confirms the three roots are ['-2', '1 + sqrt(3)*I', '1 - sqrt(3)*I'] -- one real root -2 and a complex-conjugate pair 1 ± root3 i, each of modulus 2 and arguments pi, pi/3, -pi/3.

#### 1c The complex exponential e^{i theta} and Euler's formula; e^{i pi} + 1 = 0
Euler's formula e^{i theta} = cos theta + i sin theta lets a complex number be written z = r e^{i theta}, which makes multiplication, division and powers (De Moivre) simply arithmetic on the exponent. Setting theta = pi gives Euler's identity e^{i pi} + 1 = 0, linking five fundamental constants. The complex exponential obeys the usual index laws: e^{i(theta1+theta2)} = e^{i theta1} e^{i theta2}. *Example:* solve e^{z} = -1: writing -1 = e^{i pi}, the general solution is z = i(pi + 2k pi) for integer k (since e^x has no real solution making it negative, all solutions are purely imaginary here). *Example:* express 2e^{i pi/3} in Cartesian form: 2cos(pi/3) + 2i sin(pi/3) = 1 + i root3.

#### 1d The Fundamental Theorem of Algebra; factorising real polynomials over C using conjugate root pairs
The Fundamental Theorem of Algebra: every non-constant polynomial with complex coefficients has a root in C, and hence (by repeated factoring) a degree-n polynomial has exactly n roots counted with multiplicity. For a polynomial with **real** coefficients, non-real roots occur in conjugate pairs a ± bi, so every real polynomial factorises into real linear and real irreducible quadratic factors. *Example:* x^3 - x^2 + x - 1 factorises over C as (x - 1)(x - I)(x + I) (roots 1, i, -i, a conjugate pair as expected since the coefficients are real); over R it factorises as (x-1)(x^2+1), since (x-i)(x+i) = x^2+1 is the real quadratic combining the conjugate pair.

#### 1e Sequences and series: convergence, the ratio test, Taylor/Maclaurin series of standard functions
A sequence (a_n) converges if a_n tends to a finite limit as n -> infinity. A series sum a_n converges if its sequence of partial sums converges. The **ratio test**: if |a_(n+1)/a_n| -> L as n -> infinity, the series converges (absolutely) if L < 1, diverges if L > 1, and is inconclusive if L = 1. *Example:* for sum n/2^n, the ratio |a_(n+1)/a_n| -> 1/2 < 1, so it converges. The **Taylor series** of f about 0 (Maclaurin series) is sum f^(k)(0) x^k / k!; standard examples, verified with sympy: cos x = x^4/24 - x^2/2 + 1 + ... and e^x = x^4/24 + x^3/6 + x^2/2 + x + 1 + ..., each valid for all real x.

## Explicitly not here
Complex differentiability and contour integration are S14 (Complex Analysis).
