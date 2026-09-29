# S16_Time_Zones_and_Intervals - Practice: Time zones, timestamps and INTERVAL types

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT INTERVAL '2-3' YEAR TO MONTH + INTERVAL '10' MONTH total FROM dual;
```
2. Which returns a value in the session time zone? (choose one) Choose every correct option.
   A. `CURRENT_TIMESTAMP`
   B. `SYSTIMESTAMP`
   C. `SYSDATE`
   D. `DBTIMEZONE`

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
TOTAL
---------------------------------------------------------------------------
+000000003-01
```
2. Correct: A (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
