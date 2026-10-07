# S1_Adding_Fractions - Test: Adding fractions with different denominators

## How to run this
A real checkpoint. Give the whole test at once, with no hints, then mark against the answer key and this stage's entry in `rubric.json`.

## Test items
1. Work out 2/3 + 1/4. [3 marks]
2. Work out 5/6 + 1/3 and give the answer in simplest form. [4 marks]
3. Explain in one sentence why 1/2 + 1/3 is not 2/5. [2 marks]

## Answer key (for the tutor only)
1. [3] M1 common denominator 12 shown (8/12 and 3/12); M1 numerators added; A1 11/12
2. [4] M1 common denominator 6 (5/6 + 2/6); M1 7/6; A1 simplest form 1 1/6 (accept 7/6); B1 nothing left to cancel
3. [2] B1 the pieces are different sizes so the denominators cannot be ignored; B1 a common denominator is needed first

## Grading
Apply `rubric.json`'s `stage_rubrics.S1_Adding_Fractions` exactly. 9 marks in all; a pass needs at least 6 (60%, rounded up).

## Recording the result
```
python3 /EDU/.tutor-scripts/record_stage_result.py apply <subjects.json> <course.json> S1_Adding_Fractions pass|fail
```

## If fail
Name the weak criterion, offer to revisit practice, then re-test with a new scenario of the same type.

## On pass
Record the pass and move on.
