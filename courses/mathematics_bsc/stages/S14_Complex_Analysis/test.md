# S14_Complex_Analysis - Test: Complex analysis

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Show that f(z) = |z|^2 = x^2+y^2 is complex differentiable only at z=0, using the Cauchy-Riemann equations. [6 marks]
2. Find the radius of convergence of the power series sum_{n=0}^infinity z^n/n^2, and determine convergence at z=1 and z=-1 on the boundary. [5 marks]
3. Use Cauchy's Integral Formula to evaluate integral_{|z|=2} e^z/(z-1) dz. [4 marks]
4. Find the Laurent series of f(z)=1/(z^2(z-1)) about z=0 up to the first two terms, and classify the singularity at z=0. [6 marks]
5. Use the Residue Theorem to evaluate the real integral integral_{-infinity}^{infinity} 1/(x^2+4) dx by relating it to a contour integral in the upper half-plane. [6 marks]
6. Which are true? Choose every correct option.
   A. Every holomorphic function is infinitely differentiable
   B. A pole of order k has finitely many negative-power Laurent terms
   C. The residue at a simple pole z0 equals lim_{z->z0}(z-z0)f(z)
   D. Cauchy's Theorem applies even if f has a pole inside the contour

## Answer key (for the tutor only)
1. [6] M1 identifies u=x^2+y^2, v=0; M1 du/dx=2x, dv/dy=0, needs 2x=0 so x=0; A1 du/dy=2y, -dv/dx=0, needs 2y=0 so y=0; A1 CR equations hold only at (0,0); M1 notes CR holding plus continuous partials at a POINT (not a neighbourhood) means differentiable there but not holomorphic on any open set; A1 correctly distinguishes complex-differentiable-at-a-point from holomorphic.
2. [5] M1 ratio test: |a_(n+1)/a_n| = n^2/(n+1)^2 -> 1, radius R=1; A1 radius of convergence 1; M1 at z=1, series is sum 1/n^2, a convergent p-series (p=2>1); A1 converges at z=1; A1 at z=-1, series is sum (-1)^n/n^2, absolutely convergent (same as above), converges.
3. [4] M1 identifies f(z)=e^z, holomorphic everywhere, a=1 inside |z|=2; M1 applies the formula: integral = 2 pi i f(1); A1 f(1)=e; A1 integral = 2 pi i e.
4. [6] M1 writes 1/(z-1) = -1/(1-z) = -(1+z+z^2+...) for |z|<1 (geometric series); A1 so f(z) = -1/z^2 (1+z+z^2+...) = -1/z^2 - 1/z - 1 - ...; M1 identifies the lowest power is z^{-2}; A2 Laurent series -z^{-2} - z^{-1} - 1 - z - ...; A1 pole of order 2 at z=0 (finitely many negative terms, lowest -2).
5. [6] M1 poles of 1/(z^2+4) at z=2i, z=-2i; only z=2i is in the upper half-plane; M1 residue at z=2i is 1/(4i); A1 residue = -I/4; M1 the semicircular arc contribution vanishes as its radius -> infinity (standard estimate since the integrand decays like 1/R^2); A1 integral = 2 pi i (residue) = pi/2 (real, as expected for a real integral); B1 notes sympy independently confirms integral_{-infinity}^{infinity} 1/(x^2+4)dx = pi/2, matching.
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Complex_Analysis` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 28 marks in all; a pass needs at least 17 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Mathematical_Statistics.
