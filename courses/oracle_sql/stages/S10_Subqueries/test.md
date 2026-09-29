# S10_Subqueries - Test: Single-row, multiple-row and correlated subqueries

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees) ORDER BY salary;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE department_id = (SELECT department_id FROM departments WHERE location_id = 1700);
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 90) ORDER BY 1;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT COUNT(*) FROM departments WHERE department_id NOT IN (SELECT department_id FROM employees);
SELECT COUNT(*) FROM departments d WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.department_id);
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT e.last_name, e.salary FROM employees e WHERE e.salary = (SELECT MAX(x.salary) FROM employees x WHERE x.department_id = e.department_id) ORDER BY 1;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
UPDATE employees e SET commission_pct = (SELECT MAX(commission_pct) FROM employees x WHERE x.manager_id = e.employee_id) WHERE job_id LIKE '%MAN';
SELECT last_name, commission_pct FROM employees WHERE job_id LIKE '%MAN' ORDER BY 1;
```
7. Which comparison means 'less than the smallest value the subquery returns'? (choose one) Choose every correct option.
   A. `< ALL`
   B. `< ANY`
   C. `> ALL`
   D. `IN`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
LAST_NAME        SALARY
------------ ----------
Zlotkey           10500
Abel              11000
Hartstein         13000
Kochhar           17000
King              24000
```
2. Actual result (from running it):
```
(error: ORA-01427: single-row subquery returns more than one row)
```
3. Actual result (from running it):
```
LAST_NAME
------------
King
```
4. Actual result (from running it):
```
  COUNT(*)
----------
         0

  COUNT(*)
----------
         1
```
5. Actual result (from running it):
```
LAST_NAME        SALARY
------------ ----------
Abel              11000
Hartstein         13000
Hunold             9000
King              24000
Mourgos            5800
Whalen             4400

6 rows selected.
```
6. Actual result (from running it):
```
3 rows updated.

LAST_NAME    COMMISSION_PCT
------------ --------------
Hartstein    (null)
Mourgos      (null)
Zlotkey                  .3

3 rows selected.
```
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Subqueries` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Set_Operators.
