# S07_Eigenvalues_Diagonalisation_and_Inner_Product_Spaces - Test: Eigenvalues, diagonalisation and inner product spaces

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the eigenvalues and eigenvectors of A=[[2,0,0],[0,3,4],[0,4,9]], then diagonalise A. [8 marks]
2. Use the Gram-Schmidt process to find an orthonormal basis for span{(1,1,1),(0,1,1)}. [6 marks]
3. Prove that eigenvectors corresponding to distinct eigenvalues of a symmetric matrix are orthogonal. [6 marks]
4. Explain why A=[[1,1],[0,1]] is NOT diagonalisable. [4 marks]
5. Which are true of a real symmetric matrix A? Choose every correct option.
   A. All eigenvalues of A are real
   B. A is always diagonalisable
   C. Eigenvectors for distinct eigenvalues are automatically orthogonal
   D. A must be invertible

## Answer key (for the tutor only)
1. [8] M1 expands det(A-lambda I) along first row; A1 (2-lambda)[(3-lambda)(9-lambda)-16]=0; M1 solves the quadratic factor: lambda^2-12lambda+11=0, lambda=1,11; A1 eigenvalues 2,1,11; M1 finds eigenvector for lambda=2: (1,0,0); A1 for lambda=1 and lambda=11 (in the 2x2 block): eigenvectors (0,-2,1) and (0,1,2) respectively (or scalar multiples); A2 P has these as columns, D=diag(2,1,11), and confirms P^{-1}AP=D.
2. [6] M1 u1=(1,1,1)/root3; M1 computes proj of (0,1,1) onto u1: <(0,1,1),u1>u1 = (2/3)(1,1,1) using <.,u1> normalised correctly, i.e. (2/root3)(1,1,1)/root3=(2/3)(1,1,1); A1 (0,1,1)-(2/3,2/3,2/3)=(-2/3,1/3,1/3); M1 normalises: magnitude root(4/9+1/9+1/9)=root(6)/3; A1 u2=(-2,1,1)/root6; A1 orthonormal basis {(1,1,1)/root3, (-2,1,1)/root6}.
3. [6] M1 lets Av1=lambda1 v1, Av2=lambda2 v2, lambda1≠lambda2; M1 considers v2^T A v1 = lambda1 v2^T v1; M1 also v2^T A v1 = (A v2)^T v1 = lambda2 v2^T v1 (using A^T=A); A1 so lambda1 v2^T v1 = lambda2 v2^T v1; M1 so (lambda1-lambda2) v2^T v1 = 0; A1 since lambda1≠lambda2, v2^T v1=0, i.e. orthogonal.
4. [4] M1 char poly (1-lambda)^2=0, repeated eigenvalue lambda=1 (algebraic multiplicity 2); M1 finds eigenvectors: (A-I)v=0 gives [[0,1],[0,0]]v=0, so v=(t,0), a 1-dimensional eigenspace (geometric multiplicity 1); A1 geometric multiplicity (1) < algebraic multiplicity (2); A1 so there are not 2 linearly independent eigenvectors, hence A is not diagonalisable.
5. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Eigenvalues_Diagonalisation_and_Inner_Product_Spaces` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 25 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Sequences_and_Limits.
