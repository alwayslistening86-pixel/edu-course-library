# S04_Substitution_Variables - Test: Substitution variables, DEFINE and VERIFY

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
DEFINE j = SA_REP
SET VERIFY OFF
SELECT last_name FROM employees WHERE job_id = '&j' ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
DEFINE tab = job_grades
DEFINE cond = "lowest_sal > 5000"
SET VERIFY OFF
SELECT grade_level FROM &tab WHERE &cond ORDER BY 1;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
DEFINE n = 3
SELECT &n * 2 AS twice FROM dual;
```
4. Which are true of substitution variables? (choose two) Choose every correct option.
   A. They are replaced by the client tool before the statement is sent
   B. They can replace a table name
   C. They are evaluated by the database server
   D. A value defined with DEFINE is stored as a NUMBER
5. Which command stops SQL*Plus showing the old and new lines of a statement? (choose one) Choose every correct option.
   A. SET VERIFY OFF
   B. SET DEFINE OFF
   C. `UNDEFINE`
   D. SET ECHO ON
6. A job id is to be supplied at run time. Which WHERE clauses work if the user types IT_PROG without quotes? (choose one) Choose every correct option.
   A. `WHERE job_id = '&job'`
   B. `WHERE job_id = &job`
   C. `WHERE job_id = "&job"`
   D. `WHERE job_id = &&'job'`
7. Which command removes a substitution variable's value? (choose one) Choose every correct option.
   A. UNDEFINE var
   B. `DEFINE var = NULL`
   C. SET VERIFY OFF
   D. DROP var

## Answer key (for the tutor only)
1. Actual result (from running it):
```
LAST_NAME
------------
Abel
Grant
```
2. Actual result (from running it):
```
G
-
C
D
E
```
3. Actual result (from running it):
```
old   1: SELECT &n * 2 AS twice FROM dual
new   1: SELECT 3 * 2 AS twice FROM dual

     TWICE
----------
         6
```
4. Correct: A, B (exactly these options, no others)
5. Correct: A (exactly these options, no others)
6. Correct: A (exactly these options, no others)
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Substitution_Variables` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Character_and_Number_Functions.
