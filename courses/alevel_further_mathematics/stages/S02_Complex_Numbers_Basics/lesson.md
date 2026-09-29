# S02_Complex_Numbers_Basics - Lesson: Complex numbers: forms, notation and arithmetic

## Goal
The learner works with complex numbers in cartesian and modulus-argument form, uses the standard notation, does arithmetic in both forms, finds square roots, and solves real quadratics with complex roots.

## Syllabus items taught here
- 4.02a - The language of complex numbers: real and imaginary parts, conjugate, modulus, argument
- 4.02b - Cartesian form x + iy and modulus-argument form r(cos θ + i sin θ)
- 4.02c - Notation Re z, Im z, arg z, z*, |z|; principal argument; z = 0 iff Re z = Im z = 0
- 4.02e - Arithmetic with complex numbers in cartesian and modulus-argument forms
- 4.02f - Converting between cartesian and modulus-argument forms
- 4.02h - Square roots of a complex number
- 4.02i - Quadratic equations with real coefficients and complex roots

## How to teach this
Ask what x^2 + 1 = 0 would need for a solution, and what it means to 'invent' a number i with i^2 = -1. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.02a The language of complex numbers: real and imaginary parts, conjugate, modulus, argument
z = x + iy with i^2 = -1: x = Re(z) is the real part and y = Im(z) the imaginary part (a real number). The conjugate z* = x - iy. The modulus |z| = root(x^2 + y^2) is the distance from the origin; the argument arg z is the angle from the positive real axis.

#### 4.02b Cartesian form x + iy and modulus-argument form r(cos θ + i sin θ)
Cartesian form z = x + iy; modulus-argument form z = r(cos θ + i sin θ), with r = |z| ≥ 0 and θ = arg z (also written [r, θ] or r cis θ).

#### 4.02c Notation Re z, Im z, arg z, z*, |z|; principal argument; z = 0 iff Re z = Im z = 0
Re z, Im z, arg z, z*, |z|. The principal argument lies in -π < θ ≤ π (or 0 ≤ θ < 2π; either unless the question specifies). Two complex numbers are equal iff their real parts and imaginary parts are equal: z = 0 iff Re z = 0 and Im z = 0. Equating parts turns one complex equation into two real ones. zz* = |z|^2.

#### 4.02e Arithmetic with complex numbers in cartesian and modulus-argument forms
Add and subtract parts; multiply by expanding with i^2 = -1; divide by multiplying top and bottom by the conjugate of the denominator. *Example:* (3 + 4i)(1 - 2i) = 11 - 2i; (3 + 4i)/(1 - 2i) = (3 + 4i)(1 + 2i)/5 = -1 + 2i. In modulus-argument form, multiply moduli and add arguments; divide moduli and subtract arguments (S03).

#### 4.02f Converting between cartesian and modulus-argument forms
x = r cos θ, y = r sin θ; r = root(x^2 + y^2), θ from tan θ = y/x adjusted for the quadrant (draw it!). *Example:* -1 + i root 3: r = 2, θ = 2π/3, so 2(cos 2π/3 + i sin 2π/3). *Example:* -3 - 4i: r = 5, arg = -(π - arctan(4/3)) = -2.2143 rad.

#### 4.02h Square roots of a complex number
Let (a + ib)^2 = p + iq, then a^2 - b^2 = p and 2ab = q; solve (substitute b = q/(2a)). *Example:* root(5 + 12i): a^2 - b^2 = 5, ab = 6, so a^4 - 5a^2 - 36 = 0, a^2 = 9, a = ±3, b = ±2: the square roots are ±(3 + 2i).

#### 4.02i Quadratic equations with real coefficients and complex roots
If b^2 - 4ac < 0, the formula gives complex roots as a conjugate pair: x^2 - 4x + 13 = 0 gives x = (4 ± root(-36))/2 = 2 ± 3i. Conversely a quadratic with roots α and α* is x^2 - 2Re(α)x + |α|^2 = 0.

## Explicitly not here
Polynomials of higher degree and the Argand diagram are S03.
