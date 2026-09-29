# S14_Complex_Analysis - Lesson: Complex analysis

## Goal
The learner applies the Cauchy-Riemann equations to test holomorphicity, works with complex power series, evaluates contour integrals via Cauchy's Theorem/Integral Formula, classifies isolated singularities via Laurent series, and uses the Residue Theorem to evaluate real integrals.

## Syllabus items taught here
- 14a - Complex differentiability and the Cauchy-Riemann equations; holomorphic functions
- 14b - Power series and elementary functions (exp, sin, cos, log branches) as complex functions
- 14c - Contour integration; Cauchy's Theorem and Cauchy's Integral Formula
- 14d - Taylor and Laurent series; classification of singularities (removable, pole, essential)
- 14e - The Residue Theorem and its use in evaluating real integrals

## How to teach this
Ask what it means for a limit to exist in the complex plane, where 'direction of approach' is not just left/right but every angle -- motivating why complex differentiability is a much stronger condition than real differentiability. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 14a Complex differentiability and the Cauchy-Riemann equations; holomorphic functions
f = u+iv (u,v real functions of x,y, z=x+iy) is **holomorphic** (complex differentiable) at a point iff the **Cauchy-Riemann equations** hold there: du/dx = dv/dy and du/dy = -dv/dx (together with u,v having continuous partials). *Example:* for f(z)=z^2 = (x+iy)^2, u = x^2 - y^2, v = 2xy; du/dx=2x=dv/dy=2x (matches), du/dy=-2y=-dv/dx=-2y (matches) -- Cauchy-Riemann holds everywhere, confirming f(z)=z^2 is holomorphic on all of C (entire), with f'(z)=2z as expected. *Example (fails):* f(z) = z-bar = x-iy has u=x, v=-y; du/dx=1 but dv/dy=-1 -- Cauchy-Riemann fails everywhere, so z-bar is nowhere holomorphic.

#### 14b Power series and elementary functions (exp, sin, cos, log branches) as complex functions
Complex power series sum a_n(z-z_0)^n converge inside a disc of some **radius of convergence** R (found, as for real series, via the ratio or root test) and diverge outside it; behaviour on the boundary |z-z_0|=R varies case by case. The standard real functions extend to entire (holomorphic everywhere) complex functions via their power series: e^z = sum z^n/n!, sin z = sum (-1)^n z^{2n+1}/(2n+1)!, cos z similarly. The complex **logarithm** log z = ln|z| + i arg(z) is multi-valued (arg z is only defined mod 2pi); a **branch** fixes a single-valued choice (e.g. the principal branch restricts arg to (-pi,pi]), and log z is holomorphic away from its branch cut.

#### 14c Contour integration; Cauchy's Theorem and Cauchy's Integral Formula
A **contour integral** integral_C f(z) dz is defined via a parametrisation, exactly like a real line integral of a vector field. **Cauchy's Theorem**: if f is holomorphic throughout a simply connected region containing closed contour C, then integral_C f(z) dz = 0. **Cauchy's Integral Formula**: if f is holomorphic inside and on simple closed C, and a is inside C, f(a) = (1/(2 pi i)) integral_C f(z)/(z-a) dz. *Example:* integral_{|z|=1} 1/z dz = 2 pi i (direct parametrisation z=e^{i theta}, dz=ie^{i theta}d theta gives integral_0^{2pi} i d theta = 2 pi i) -- this nonzero value is consistent with Cauchy's Theorem NOT applying, since f(z)=1/z is not holomorphic at z=0, which is inside the contour.

#### 14d Taylor and Laurent series; classification of singularities (removable, pole, essential)
Near an **isolated singularity** z_0, f has a **Laurent series** sum_{n=-infinity}^{infinity} a_n(z-z_0)^n (allowing negative powers). The singularity is: **removable** if all a_n=0 for n<0 (f extends holomorphically); a **pole of order k** if a_{-k}≠0 but a_n=0 for n<-k (finitely many negative-power terms); **essential** if infinitely many negative-power terms occur. *Example:* f(z)=sin(z)/z has Laurent series 1 - z^2/6 + z^4/120 - ... (no negative powers, since sin z ~ z near 0 cancels the pole) -- a **removable** singularity at z=0. f(z)=1/z^3 has a **pole of order 3** at z=0. f(z)=e^{1/z} = sum z^{-n}/n! has infinitely many negative powers -- an **essential** singularity at z=0.

#### 14e The Residue Theorem and its use in evaluating real integrals
The **residue** of f at an isolated singularity z_0 is the coefficient a_{-1} in its Laurent series (for a simple pole, residue = lim_{z->z_0} (z-z_0)f(z)). **Residue Theorem**: integral_C f(z) dz = 2 pi i (sum of residues at poles enclosed by C). This evaluates many real integrals: close the real line with a large semicircular arc in the upper half-plane (which contributes 0 in the limit, for suitable f), reducing integral_{-infinity}^{infinity} f(x) dx to 2 pi i times the residues in the upper half-plane. *Example:* residues of f(z)=1/(z(z-2)) are -1/2 at z=0 and 1/2 at z=2 (computed with sympy); for a contour enclosing both, the integral is 2 pi i(-1/2+1/2) = 0.

## Explicitly not here
Conformal mapping and the Riemann Mapping Theorem are beyond this stage's scope.
