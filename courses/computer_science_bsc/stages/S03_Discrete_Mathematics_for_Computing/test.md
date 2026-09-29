# S03_Discrete_Mathematics_for_Computing - Test: Discrete mathematics for computing

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
def is_bijective(f, domain, codomain):
    images = [f(x) for x in domain]
    injective = len(images) == len(set(images))
    surjective = set(images) == set(codomain)
    return injective and surjective

print(is_bijective(lambda x: x + 1, [1, 2, 3], [2, 3, 4]))
print(is_bijective(lambda x: x * x, [-2, -1, 0, 1, 2], [0, 1, 4]))
```
2. State De Morgan's second law and use it to simplify the condition `not (x < 0 or x > 100)` into an equivalent condition without a leading `not`. [3 marks]
3. Let R = {(a,b) : a,b in Z, a-b is a multiple of 3}. Prove R is an equivalence relation by checking reflexivity, symmetry and transitivity. [6 marks]
4. A tree has 12 vertices. State how many edges it has, and explain why using the definition of a tree. [2 marks]
5. Prove by induction that 2^n > n for all integers n >= 1. [6 marks]
6. Which of the following relations on the integers are equivalence relations? Choose every correct option.
   A. `'is equal to'`
   B. `'is less than or equal to'`
   C. 'has the same remainder as, when divided by 5'
   D. `'is not equal to'`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
True
False
```
2. [3] B1 NOT(A OR B) = (NOT A) AND (NOT B); M1 applies it: not(x<0) and not(x>100); A1 simplifies to x>=0 and x<=100.
3. [6] M1 reflexive: a-a=0, and 0 is a multiple of 3, so (a,a) in R for all a; M1 symmetric: if a-b is a multiple of 3 then b-a=-(a-b) is also a multiple of 3, so (b,a) in R; M1 transitive: if a-b=3m and b-c=3n for integers m,n, then a-c=(a-b)+(b-c)=3(m+n), a multiple of 3, so (a,c) in R; A3 all three properties correctly shown with valid algebra, and the conclusion that R is an equivalence relation stated explicitly (1 mark per property clearly concluded).
4. [2] B1 11 edges; B1 because a tree is defined as a connected acyclic graph on n vertices with exactly n-1 edges, and here n=12.
5. [6] M1 base case n=1: 2^1=2 > 1, true; M1 states the inductive hypothesis: assume 2^k > k for some k>=1; M1 inductive step: 2^(k+1) = 2 x 2^k > 2k (by the hypothesis); A1 since k>=1, 2k = k+k >= k+1; A1 so 2^(k+1) > k+1, completing the inductive step; A1 conclusion: by induction, 2^n > n for all n>=1.
6. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Discrete_Mathematics_for_Computing` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Databases_and_Software_Engineering_Foundations.
