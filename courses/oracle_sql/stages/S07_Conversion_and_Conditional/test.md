# S07_Conversion_and_Conditional - Test: Conversion functions, NULL functions, CASE and DECODE, nesting

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, NVL(TO_CHAR(commission_pct), 'none') comm, NVL2(commission_pct, salary * commission_pct, 0) bonus FROM employees WHERE employee_id IN (149, 201) ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT TO_CHAR(0.5, '0.99') a, TO_CHAR(0.5, '9.99') b, TO_CHAR(12345.678, '99,999.9') c, TO_CHAR(12345, '999') d FROM dual;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT TO_CHAR(TO_DATE('10-DEC-49', 'DD-MON-RR'), 'YYYY') a, TO_CHAR(TO_DATE('10-DEC-50', 'DD-MON-RR'), 'YYYY') b, TO_CHAR(DATE '2024-03-05', 'fmDDth "of" MONTH') c FROM dual;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, CASE WHEN commission_pct > .2 THEN 'top tier' WHEN commission_pct > 0 THEN 'standard' END c, DECODE(job_id, 'SA_REP', salary * 1.1, salary) new_sal FROM employees WHERE department_id = 80 OR employee_id = 100 ORDER BY 1;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT COALESCE(commission_pct, 'n/a') FROM employees;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT TO_NUMBER('1,234.50', '9,999.99') * 2 a, TO_DATE('2024/07/04', 'YYYY/MM/DD') + 1 b, LENGTH(TO_CHAR(SYSDATE, 'YYYY')) c FROM dual;
```
7. Which expressions return 'YES'? (choose two) Choose every correct option.
   A. `NVL(NULL, 'YES')`
   B. `NULLIF('YES', 'YES')`
   C. `COALESCE(NULL, 'YES', 'NO')`
   D. `NVL2('X', NULL, 'YES')`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
LAST_NAME    COMM                                          BONUS
------------ ---------------------------------------- ----------
Hartstein    none                                              0
Zlotkey      .2                                             2100
```
2. Actual result (from running it):
```
A     B     C         D
----- ----- --------- ----
 0.50   .50  12,345.7 ####
```
3. Actual result (from running it):
```
A    B    C
---- ---- ------------
2049 1950 5TH of MARCH
```
4. Actual result (from running it):
```
LAST_NAME    C           NEW_SAL
------------ -------- ----------
Abel         top tier      12100
King         (null)        24000
Zlotkey      standard      10500
```
5. Actual result (from running it):
```
(error: ORA-00932: expression ('n/a') is of data type CHAR, which is incompatible with expected data type NUMBER)
```
6. Actual result (from running it):
```
         A B                           C
---------- ------------------ ----------
      2469 05-JUL-24                   4
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Conversion_and_Conditional` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Group_Functions.
