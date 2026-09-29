# S05_Exponential_Form_and_de_Moivre - Lesson: Exponential form, de Moivre's theorem and roots of unity

## Goal
The learner uses the exponential form and Euler's formula, proves and applies de Moivre's theorem (multiple angles, powers and series), and finds nth roots including roots of unity in geometric problems.

## Syllabus items taught here
- 4.02d - Exponential form re^(iθ)
- 4.02n - Euler's formula e^(iθ) = cos θ + i sin θ
- 4.02q - De Moivre's theorem: multiple-angle formulae and sums of trigonometric or exponential series
- 4.02r - The n distinct nth roots of re^(iθ); vertices of a regular n-gon
- 4.02s - Complex roots of unity in geometric problems

## How to teach this
Ask what (cos θ + i sin θ)^2 simplifies to, and what that suggests about (cos θ + i sin θ)^n. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.02d Exponential form re^(iθ)
z = re^(iθ) is shorthand for r(cos θ + i sin θ). Products and quotients follow the index laws: r1e^(iθ1) x r2e^(iθ2) = r1 r2 e^(i(θ1 + θ2)). z* = re^(-iθ).

#### 4.02n Euler's formula e^(iθ) = cos θ + i sin θ
Euler's formula e^(iθ) = cos θ + i sin θ (from Maclaurin series, S14). Consequences: e^(iπ) + 1 = 0; cos θ = (e^(iθ) + e^(-iθ))/2 and sin θ = (e^(iθ) - e^(-iθ))/(2i).

#### 4.02q De Moivre's theorem: multiple-angle formulae and sums of trigonometric or exponential series
De Moivre: (cos θ + i sin θ)^n = cos nθ + i sin nθ (proved by induction for positive n). **Multiple angles:** expand (c + is)^3 = c^3 + 3ic^2 s - 3cs^2 - is^3 and compare parts: cos 3θ = 4cos^3 θ - 3cos θ, sin 3θ = 3sin θ - 4sin^3 θ. **Powers of sin and cos:** with z = e^(iθ), z^n + z^(-n) = 2cos nθ and z^n - z^(-n) = 2i sin nθ; (z + 1/z)^4 = 16cos^4 θ gives cos^4 θ = (cos 4θ + 4cos 2θ + 3)/8. **Series:** sum geometric series of e^(ikθ) and take real parts, e.g. C + iS = Σ e^(ikθ). **Powers:** (1 + i)^8 = (root2 e^(iπ/4))^8 = 16e^(2πi) = 16.

#### 4.02r The n distinct nth roots of re^(iθ); vertices of a regular n-gon
z^n = re^(iθ) has n roots: z = r^(1/n) e^(i(θ + 2πk)/n), k = 0, 1, ..., n - 1, equally spaced on a circle of radius r^(1/n): the vertices of a regular n-gon. *Example:* z^3 = 8i = 8e^(iπ/2): z = 2e^(iπ/6), 2e^(i5π/6), 2e^(-iπ/2), i.e. root3 + i, -root3 + i, -2i.

#### 4.02s Complex roots of unity in geometric problems
The nth roots of unity are 1, ω, ω^2, ..., ω^(n-1) with ω = e^(2πi/n); their sum is 0 (for n > 1). They are useful in geometry: rotating a vertex of a regular polygon about its centre by multiplying by ω. *Example:* if one vertex of a square centred at the origin is 2 + i, the others are i(2 + i) = -1 + 2i, -2 - i and 1 - 2i. For an equilateral triangle centred at c with vertex a: c + (a - c)ω, c + (a - c)ω^2 with ω = e^(2πi/3).

## Explicitly not here
Matrices are S06.
