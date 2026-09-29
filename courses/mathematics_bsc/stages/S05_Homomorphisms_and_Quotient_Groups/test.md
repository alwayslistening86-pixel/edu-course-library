# S05_Homomorphisms_and_Quotient_Groups - Test: Homomorphisms and quotient groups

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Let phi: GL(2,R) -> (R\{0}, x) be phi(A) = det(A). Show phi is a homomorphism and find its kernel (name it). [5 marks]
2. Prove that the kernel of any group homomorphism phi: G -> H is a normal subgroup of G. [6 marks]
3. Given N=4Z ◁ (Z,+), list the elements of Z/4Z and write out its Cayley table (addition of cosets). [5 marks]
4. Use the First Isomorphism Theorem to identify the quotient group R/Z, given the homomorphism phi: (R,+) -> (S^1, x) (the unit circle under multiplication), phi(t) = e^{2 pi i t}. [5 marks]
5. Which are true of a group homomorphism phi: G -> H? Choose every correct option.
   A. `ker(phi) is always a subgroup of G`
   B. `im(phi) is always a subgroup of H`
   C. `phi is injective iff ker(phi)={e_G}`
   D. `ker(phi) need not be normal in G`

## Answer key (for the tutor only)
1. [5] M1 det(AB)=det(A)det(B) (standard determinant property); A1 so phi is a homomorphism; M1 ker(phi)={A: det(A)=1}; A1 this is the special linear group SL(2,R); A1 im(phi)=R\{0} since any nonzero determinant is achievable.
2. [6] M1 shows ker(phi) is a subgroup (contains e, closed, has inverses, using homomorphism properties); M1 takes g in G, k in ker(phi); M1 computes phi(gkg^{-1}) = phi(g)phi(k)phi(g^{-1}) = phi(g) e_H phi(g)^{-1}; A1 = e_H; A1 so gkg^{-1} in ker(phi) for all g, k; A1 conclusion: ker(phi) is normal.
3. [5] M1 four cosets 0+4Z, 1+4Z, 2+4Z, 3+4Z; A1 clearly listed; M1 Cayley table built using (a+4Z)+(b+4Z)=(a+b)+4Z; A2 fully correct table (isomorphic to Z_4's addition table).
4. [5] M1 checks phi(s+t)=e^{2 pi i(s+t)}=e^{2 pi i s}e^{2 pi i t}=phi(s)phi(t); A1 homomorphism confirmed; M1 ker(phi)={t: e^{2 pi i t}=1}=Z; A1 im(phi)=S^1 (all of it, since every point on the unit circle is e^{2 pi i t} for some real t); A1 by the theorem R/Z ≅ S^1.
5. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Homomorphisms_and_Quotient_Groups` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 22 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Vector_Spaces_and_Linear_Maps.
