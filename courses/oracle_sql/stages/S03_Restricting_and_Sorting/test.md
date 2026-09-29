# S03_Restricting_and_Sorting - Test: WHERE, operator precedence, row limiting and ORDER BY

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE department_id = 80 OR department_id = 60 AND salary > 8000 ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE NOT (salary > 5000 OR department_id = 50) ORDER BY 1;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE salary BETWEEN 10000 AND 7000;
SELECT COUNT(*) FROM employees WHERE commission_pct = NULL;
SELECT COUNT(*) FROM employees WHERE commission_pct IS NULL;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, department_id FROM employees WHERE last_name LIKE '%a%' AND last_name NOT LIKE '_a%' ORDER BY department_id DESC NULLS LAST, last_name;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, salary FROM employees ORDER BY salary DESC OFFSET 1 ROW FETCH NEXT 20 PERCENT ROWS ONLY;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, salary * 12 annual FROM employees WHERE department_id = 90 ORDER BY annual;
```
7. Which comes last in the order of evaluation among these? (choose one) Choose every correct option.
   A. `OR`
   B. `AND`
   C. `NOT`
   D. `BETWEEN`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
LAST_NAME
------------
Abel
Hunold
Zlotkey
```
2. Actual result (from running it):
```
LAST_NAME
------------
Whalen
```
3. Actual result (from running it):
```
no rows selected

  COUNT(*)
----------
         0

  COUNT(*)
----------
         8
```
4. Actual result (from running it):
```
LAST_NAME    DEPARTMENT_ID
------------ -------------
Kochhar                 90
Whalen                  10
Grant        (null)
```
5. Actual result (from running it):
```
LAST_NAME        SALARY
------------ ----------
Kochhar           17000
Hartstein         13000
Abel              11000
```
6. Actual result (from running it):
```
LAST_NAME        ANNUAL
------------ ----------
Kochhar          204000
King             288000
```
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Restricting_and_Sorting` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Substitution_Variables.
