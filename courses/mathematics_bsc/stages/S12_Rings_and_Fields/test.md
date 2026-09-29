# S12_Rings_and_Fields - Test: Rings and fields

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove that Z_p is a field when p is prime, using the fact that gcd(a,p)=1 for 0<a<p. [6 marks]
2. Find all the ideals of Z_12 and identify the corresponding quotient rings. [6 marks]
3. Show that the map phi: Z -> Z_5, phi(n) = n mod 5, is a ring homomorphism and use the First Isomorphism Theorem to identify Z/5Z. [5 marks]
4. Factorise x^3-8 completely over Q, and state whether each factor is irreducible over Q. [5 marks]
5. Determine whether 6+2i is a unit, a zero divisor, or neither in the ring Z[i] (Gaussian integers), given N(a+bi)=a^2+b^2 is multiplicative and units have norm 1. [4 marks]
6. Which are true? Choose every correct option.
   A. Every field is an integral domain
   B. Every integral domain is a field
   C. Z_n is a field iff n is prime
   D. The kernel of a ring homomorphism is always an ideal

## Answer key (for the tutor only)
1. [6] M1 recalls Z_p is a commutative ring with 1; M1 for nonzero a in Z_p, gcd(a,p)=1 since p prime and 0<a<p; M1 by Bezout's identity, there exist integers s,t with sa+tp=1; A1 so sa ≡ 1 (mod p); A1 s mod p is the multiplicative inverse of a; A1 every nonzero element has an inverse, so Z_p is a field.
2. [6] M1 ideals of Z_12 correspond to subgroups (Z_12 cyclic, all subgroups are ideals here); A2 ideals: {0}, <6>={0,6}, <4>={0,4,8}, <3>={0,3,6,9}, <2>={0,2,4,6,8,10}, Z_12 itself; A1 quotients have order 12/|ideal|: Z_12/{0}≅Z_12, Z_12/<6>≅ ring of order 6, etc.; A2 explicitly identifies Z_12/<3> ≅ Z_3 (index [Z_12:<3>]=12/4=3, correctly matched by order).
3. [5] M1 checks phi(a+b) mod5 = (phi(a)+phi(b)) mod5 and phi(ab) mod5=(phi(a)phi(b)) mod5, both standard modular arithmetic facts; A1 confirmed homomorphism; M1 ker(phi)=5Z; A1 im(phi)=Z_5 (surjective); A1 by the theorem Z/5Z ≅ Z_5.
4. [5] M1 recognises difference of cubes; A2 (x - 2)(x^2 + 2x + 4); A1 (x-2) is linear, irreducible; A1 (x^2+2x+4) has discriminant 4-16=-12<0, no real roots, irreducible over Q (and R).
5. [4] M1 computes N(6+2i)=36+4=40; A1 not 1, so not a unit; M1 Z[i] is an integral domain (subring of C, which has no zero divisors) so no nonzero element is a zero divisor; A1 conclusion: 6+2i is neither a unit nor a zero divisor (an ordinary non-unit element).
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Rings_and_Fields` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 27 marks in all; a pass needs at least 17 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Metric_Spaces_and_Topology.
