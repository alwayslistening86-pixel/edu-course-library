# S04_Groups_and_Subgroups - Test: Groups and subgroups

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Show that the set of 2x2 invertible real matrices under matrix multiplication, GL(2,R), forms a group, checking each axiom. [6 marks]
2. Find the order of the element 4 in (Z_10, +), and list the subgroup it generates. [4 marks]
3. Write the permutation (1 3 5 7)(2 4) as a product of transpositions and determine whether it is even or odd. [5 marks]
4. A group G has order 35 = 5 x 7. Using Lagrange's theorem, list every possible order of a subgroup of G. [3 marks]
5. In (Z_9, +), let H = <3> = {0,3,6}. Find all the left cosets of H and verify they partition Z_9. [5 marks]
6. Which of the following are true? Choose every correct option.
   A. Every subgroup of an abelian group is abelian
   B. Every cyclic group is abelian
   C. The order of every element of a finite group G divides |G|
   D. Every group of order 4 is cyclic

## Answer key (for the tutor only)
1. [6] M1 closure: product of invertible matrices is invertible; M1 associativity: matrix multiplication is associative; A1 identity: the 2x2 identity matrix I; A1 inverses: exist by definition of invertible; B1 notes it is non-abelian (give a counter-example pair); B1 clearly structured verification of all axioms.
2. [4] M1 computes multiples of 4 mod 10: 4,8,2,6,0; A1 order 5 (5 distinct elements before returning to 0); A1 subgroup {0,2,4,6,8}; A1 notes this equals the even residues mod 10.
3. [5] M1 (1 3 5 7) = (1 7)(1 5)(1 3), three transpositions; A1 (2 4) is one transposition; M1 total four transpositions; A1 even number, so the permutation is even; A1 sign = +1.
4. [3] M1 divisors of 35 are 1,5,7,35; A2 possible subgroup orders are exactly 1, 5, 7 and 35 (all divisors, by Lagrange).
5. [5] M1 0+H={0,3,6}; A1 1+H={1,4,7}; A1 2+H={2,5,8}; M1 notes these three cosets are pairwise disjoint; A1 their union is all of Z_9, confirming the partition, with index [Z_9:H]=3.
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Groups_and_Subgroups` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 24 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Homomorphisms_and_Quotient_Groups.
