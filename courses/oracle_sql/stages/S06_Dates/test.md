# S06_Dates - Test: Date arithmetic and date functions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT MONTHS_BETWEEN(DATE '2024-06-30', DATE '2024-02-29') a, ADD_MONTHS(DATE '2024-04-30', -2) b, NEXT_DAY(DATE '2024-07-08', 'MONDAY') c FROM dual;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, TRUNC((DATE '2008-01-01' - hire_date) / 365) yrs FROM employees WHERE employee_id IN (100, 104) ORDER BY 1;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT ROUND(DATE '2024-02-15', 'MONTH') a, ROUND(DATE '2024-02-16', 'MONTH') b, TRUNC(DATE '2024-12-31', 'YEAR') c, ROUND(DATE '2024-06-30', 'YEAR') d FROM dual;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT hire_date - DATE '2003-06-01' FROM employees WHERE employee_id = 100;
SELECT DATE '2024-01-01' - 1 FROM dual;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE EXTRACT(YEAR FROM hire_date) = 2007 AND EXTRACT(MONTH FROM hire_date) < 6 ORDER BY hire_date;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT MONTHS_BETWEEN(hire_date) FROM employees;
```
7. Which expressions are valid? (choose two) Choose every correct option.
   A. `hire_date + 1`
   B. hire_date - hire_date
   C. `hire_date * 2`
   D. `hire_date + hire_date`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
         A B                  C
---------- ------------------ ------------------
         4 29-FEB-24          15-JUL-24
```
2. Actual result (from running it):
```
LAST_NAME           YRS
------------ ----------
Ernst                 0
King                  4
```
3. Actual result (from running it):
```
A                  B                  C                  D
------------------ ------------------ ------------------ ------------------
01-FEB-24          01-MAR-24          01-JAN-24          01-JAN-24
```
4. Actual result (from running it):
```
HIRE_DATE-DATE'2003-06-01'
--------------------------
                        16

DATE'2024-01-01'-1
------------------
31-DEC-23
```
5. Actual result (from running it):
```
LAST_NAME
------------
Ernst
Grant
```
6. Actual result (from running it):
```
(error: ORA-00909: invalid number of arguments)
```
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Dates` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Conversion_and_Conditional.
