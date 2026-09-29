# S21_Inheritance - Test: Inheritance and the chi-squared test

## How to run this
A real checkpoint in the style of AQA's papers: structured questions with marks shown (and some multiple choice). Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Haemophilia is caused by a recessive allele on the X chromosome. A carrier woman and an unaffected man have a son. What is the probability he has haemophilia? Explain using genotypes. [3 marks]
2. A dihybrid cross expected to give 9:3:3:1 produced 92, 28, 36 and 4 offspring. Calculate χ^2 and state your conclusion (critical value at p = 0.05 with 3 degrees of freedom = 7.82). [4 marks]
3. Explain why the offspring of a dihybrid cross may not show a 9:3:3:1 ratio when the genes are on the same chromosome. [3 marks]
4. In mice, gene A controls pigment (A pigment, aa albino, epistatic), and gene B colour (B black, bb brown). Give the expected phenotypic ratio from AaBb x AaBb. [2 marks]
5. Explain the difference between a genotype and a phenotype. [2 marks]

## Answer key (for the tutor only)
1. [3] B1 mother X^H X^h, father X^H Y; B1 son receives Y from father and either X from mother; B1 probability 1/2.
2. [4] M1 expected 90.0, 30.0, 30.0, 10.0; M1 Σ(O - E)^2/E; A1 χ^2 = 4.98; B1 less than 7.82: no significant difference; results fit 9:3:3:1.
3. [3] B1 genes are linked (autosomal linkage); B1 inherited together, so parental combinations are more common; B1 recombinant types appear only when crossing over separates the alleles.
4. [2] M1 aa are albino whatever the B genotype; A1 9 black : 3 brown : 4 albino.
5. [2] B1 genotype: the alleles an organism has; B1 phenotype: the characteristics expressed, resulting from the genotype and its interaction with the environment.

## Grading
Apply `rubric.json`'s `stage_rubrics.S21_Inheritance` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S22_Populations_Evolution_Speciation.
