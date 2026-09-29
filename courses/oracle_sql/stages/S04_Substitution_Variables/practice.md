# S04_Substitution_Variables - Practice: Substitution variables, DEFINE and VERIFY

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does `&&col` do in SQL*Plus? (choose one) Choose every correct option.
   A. Prompts once and keeps the value defined for the session
   B. Prompts every time it appears
   C. Refers to a bind variable
   D. Escapes the & character
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
DEFINE d = 20
SET VERIFY OFF
SELECT department_name FROM departments WHERE department_id = &d;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Correct: A (exactly these options, no others)
2. Actual result (from running it):
```
DEPARTMENT_NAME
--------------------
Marketing
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
