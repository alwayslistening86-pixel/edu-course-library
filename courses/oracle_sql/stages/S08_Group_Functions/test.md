# S08_Group_Functions - Test: Group functions, GROUP BY and HAVING

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT job_id, SUM(salary) total FROM employees WHERE salary > 5000 GROUP BY job_id HAVING SUM(salary) > 10000 ORDER BY total DESC;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT ROUND(AVG(commission_pct), 2) a, ROUND(SUM(commission_pct) / COUNT(*), 2) b, MAX(commission_pct) c, MIN(NVL(commission_pct, 0)) d FROM employees;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT department_id, MAX(salary) FROM employees;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT MAX(COUNT(*)) FROM employees GROUP BY job_id;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT manager_id, COUNT(*) reports FROM employees WHERE manager_id IS NOT NULL GROUP BY manager_id HAVING COUNT(*) >= 2 ORDER BY reports DESC, manager_id;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT COUNT(*) FROM employees WHERE department_id = 999;
SELECT SUM(salary) FROM employees WHERE department_id = 999;
```
7. Which are true? (choose two) Choose every correct option.
   A. `WHERE can't contain a group function`
   B. HAVING must come before GROUP BY in the statement
   C. COUNT(*) counts rows including those with NULLs
   D. AVG counts NULL values as zero

## Answer key (for the tutor only)
1. Actual result (from running it):
```
JOB_ID          TOTAL
---------- ----------
AD_PRES         24000
SA_REP          18000
AD_VP           17000
IT_PROG         15000
MK_MAN          13000
SA_MAN          10500

6 rows selected.
```
2. Actual result (from running it):
```
         A          B          C          D
---------- ---------- ---------- ----------
       .22        .06         .3          0
```
3. Actual result (from running it):
```
(error: ORA-00937: not a single-group group function)
```
4. Actual result (from running it):
```
MAX(COUNT(*))
-------------
            2
```
5. Actual result (from running it):
```
MANAGER_ID    REPORTS
---------- ----------
       100          4
       101          2
       149          2
```
6. Actual result (from running it):
```
  COUNT(*)
----------
         0

SUM(SALARY)
-----------
(null)
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Group_Functions` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Joins.
