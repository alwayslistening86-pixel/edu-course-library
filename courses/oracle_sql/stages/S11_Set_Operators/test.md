# S11_Set_Operators - Test: UNION, UNION ALL, INTERSECT and MINUS

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT manager_id FROM employees INTERSECT SELECT employee_id FROM employees WHERE salary > 12000 ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT department_id, job_id FROM employees WHERE department_id = 80
UNION
SELECT department_id, 'NONE' FROM departments WHERE department_id IN (80, 110)
ORDER BY 1, 2;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE department_id = 60
UNION
SELECT department_name FROM departments WHERE department_id = 60
ORDER BY department_name;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT employee_id, hire_date FROM employees WHERE employee_id = 100
UNION
SELECT department_id, location_id FROM departments;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
(SELECT department_id FROM employees UNION ALL SELECT department_id FROM employees) MINUS SELECT department_id FROM departments WHERE department_id > 20 ORDER BY 1;
```
6. Which set operators remove duplicate rows? (choose three) Choose every correct option.
   A. `UNION`
   B. UNION ALL
   C. `INTERSECT`
   D. `MINUS`
7. Where may ORDER BY appear in a compound query? (choose one) Choose every correct option.
   A. Only once, at the end
   B. In each component query
   C. Only in the first query
   D. `Nowhere`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
MANAGER_ID
----------
       100
       101
```
2. Actual result (from running it):
```
DEPARTMENT_ID JOB_ID
------------- ----------
           80 NONE
           80 SA_MAN
           80 SA_REP
          110 NONE
```
3. Actual result (from running it):
```
(error: ORA-00904: "DEPARTMENT_NAME": invalid identifier)
```
4. Actual result (from running it):
```
(error: ORA-01790: expression must have same datatype as corresponding expression)
```
5. Actual result (from running it):
```
DEPARTMENT_ID
-------------
           10
           20
(null)
```
6. Correct: A, C, D (exactly these options, no others)
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Set_Operators` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_DML_and_Transactions.
