# S05_Character_and_Number_Functions - Test: Character functions and ROUND, TRUNC and MOD

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT SUBSTR('DATABASE', 3, 4) a, SUBSTR('DATABASE', -4, 2) b, INSTR('DATABASE', 'A', 3) c, INSTR('DATABASE', 'A', -1) d, LPAD('7', 3, '0') e FROM dual;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT CONCAT(CONCAT(first_name, ' '), UPPER(last_name)) full_name, REPLACE(email, 'K') em, RPAD(job_id, 3) j FROM employees WHERE employee_id IN (100, 124) ORDER BY 1;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT CONCAT(first_name, ' ', last_name) FROM employees WHERE employee_id = 100;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT ROUND(15.5) a, ROUND(-15.5) b, TRUNC(-15.5) c, ROUND(149, -2) d, ROUND(150, -2) e, MOD(15.5, 4) f, TRUNC(1999.99, -3) g FROM dual;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE LOWER(last_name) LIKE '%r%' AND MOD(employee_id, 2) = 1 ORDER BY 1;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT TRIM(BOTH '*' FROM '**x*y**') a, LTRIM('xxyxz', 'xy') b, INITCAP('mcDONALD o''NEIL') c FROM dual;
```
7. Which functions return a number? (choose three) Choose every correct option.
   A. `LENGTH`
   B. `INSTR`
   C. `MOD`
   D. `LPAD`
   E. `INITCAP`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
A    B           C          D E
---- -- ---------- ---------- ---
TABA BA          4          6 007
```
2. Actual result (from running it):
```
FULL_NAME                 EM           J
------------------------- ------------ ------------
Kevin MOURGOS             MOURGOS      ST_
Steven KING               SING         AD_
```
3. Actual result (from running it):
```
CONCAT(FIRST_NAME,'',LAST
-------------------------
Steven King
```
4. Actual result (from running it):
```
         A          B          C          D          E          F          G
---------- ---------- ---------- ---------- ---------- ---------- ----------
        16        -16        -15        100        200        3.5       1000
```
5. Actual result (from running it):
```
LAST_NAME
------------
Hartstein
Kochhar
Rajs
```
6. Actual result (from running it):
```
A   B C
--- - ---------------
x*y z Mcdonald O'Neil
```
7. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Character_and_Number_Functions` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Dates.
