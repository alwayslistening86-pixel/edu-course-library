# S02_Basic_SELECT - Test: The SELECT statement, aliases, literals, DISTINCT, arithmetic and NULL

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, salary + salary * commission_pct total FROM employees WHERE department_id = 80 OR employee_id = 100 ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT q'<It's >' || last_name || '''s turn' msg FROM employees WHERE employee_id = 200;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, 12 * salary + 1000 / 2 a, (12 * salary + 1000) / 2 b FROM employees WHERE employee_id = 104;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT employee_id, last_name name FROM employees WHERE name = 'King';
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT COUNT(DISTINCT job_id) jobs, COUNT(DISTINCT manager_id) mgrs FROM employees;
```
6. Which SELECT statements run successfully? (choose two) Choose every correct option.
   A. SELECT last_name AS "Last Name" FROM employees;
   B. SELECT last_name AS Last Name FROM employees;
   C. SELECT DISTINCT job_id, department_id FROM employees;
   D. SELECT job_id, DISTINCT department_id FROM employees;
7. What is the result of 100 + NULL * 2 in a SELECT? (choose one) Choose every correct option.
   A. `NULL`
   B. `100`
   C. `102`
   D. An error

## Answer key (for the tutor only)
1. Actual result (from running it):
```
LAST_NAME         TOTAL
------------ ----------
Abel              14300
King         (null)
Zlotkey           12600
```
2. Actual result (from running it):
```
MSG
------------------------
It's Whalen's turn
```
3. Actual result (from running it):
```
LAST_NAME             A          B
------------ ---------- ----------
Ernst             72500      36500
```
4. Actual result (from running it):
```
(error: ORA-00904: "NAME": invalid identifier)
```
5. Actual result (from running it):
```
      JOBS       MGRS
---------- ----------
         9          5
```
6. Correct: A, C (exactly these options, no others)
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Basic_SELECT` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Restricting_and_Sorting.
