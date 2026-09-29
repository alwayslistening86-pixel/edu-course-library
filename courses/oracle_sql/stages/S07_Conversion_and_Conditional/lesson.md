# S07_Conversion_and_Conditional - Lesson: Conversion functions, NULL functions, CASE and DECODE, nesting

## Goal
The learner predicts implicit conversion, converts explicitly with TO_CHAR, TO_NUMBER and TO_DATE and their format models, handles NULLs with NVL, NVL2, NULLIF and COALESCE, writes CASE and DECODE, and evaluates nested functions from the inside out.

## Syllabus items taught here
- 5.1 - Apply the NVL, NULLIF and COALESCE functions to data
- 5.2 - Understand implicit and explicit data type conversion
- 5.3 - Use the TO_CHAR, TO_NUMBER and TO_DATE conversion functions
- 5.4 - Nest multiple functions

## How to teach this
Ask what `NVL(commission_pct, 'none')` does and why it fails. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 5.1 Apply the NVL, NULLIF and COALESCE functions to data
`NVL(expr, replacement)`: the replacement if expr is NULL (both must be convertible to the same type). `NVL2(expr, if_not_null, if_null)`. `NULLIF(a, b)`: NULL if a = b, otherwise a. `COALESCE(e1, e2, ...)`: the first non-NULL argument (all the same type family).
```sql
SELECT last_name, NVL(commission_pct, 0) nvl_c, NVL2(commission_pct, 'SAL+COMM', 'SAL') nvl2_c,
       NULLIF(LENGTH(first_name), LENGTH(last_name)) nullif_c, COALESCE(commission_pct, manager_id, -1) coal
FROM employees WHERE employee_id IN (100, 149, 104) ORDER BY employee_id;
```
Output:
```
LAST_NAME         NVL_C NVL2_C     NULLIF_C       COAL
------------ ---------- -------- ---------- ----------
King                  0 SAL               6         -1
Ernst                 0 SAL      (null)            103
Zlotkey              .2 SAL+COMM          5         .2
```
```sql
SELECT NVL(commission_pct, 'none') FROM employees;
```
Output:
```
(error: ORA-01722: unable to convert string value containing 'n' to a number:)
```

#### 5.2 Understand implicit and explicit data type conversion
**Implicit conversion:** Oracle converts VARCHAR2/CHAR to NUMBER or DATE when an expression needs it (if the text is valid), and NUMBER or DATE to VARCHAR2 for concatenation and character functions. Relying on it is risky: a string compared with a number column converts the *string*, but a number compared with a character column converts every *column value*, and a date string depends on the session's NLS_DATE_FORMAT. **Explicit conversion** uses TO_CHAR, TO_NUMBER and TO_DATE (or CAST).
```sql
SELECT '10' + 5 a, 10 || 5 b, LENGTH(12345) c, CAST('7.5' AS NUMBER) * 2 d FROM dual;
SELECT last_name FROM employees WHERE salary = '24000';
SELECT last_name FROM employees WHERE hire_date = '17-JUN-03';
```
Output:
```
         A B            C          D
---------- --- ---------- ----------
        15 105          5         15

LAST_NAME
------------
King

LAST_NAME
------------
King
```
```sql
SELECT 'abc' + 1 FROM dual;
```
Output:
```
(error: ORA-01722: unable to convert string value containing 'a' to a number:)
```
(Older releases word ORA-01722 simply as 'invalid number'.)

#### 5.3 Use the TO_CHAR, TO_NUMBER and TO_DATE conversion functions
`TO_CHAR(date, 'fmt')`: `YYYY RR MM MON MONTH DD DY DAY HH HH24 MI SS AM`, text in double quotes, `fm` to strip padding, `th` / `sp` suffixes. `TO_CHAR(number, 'fmt')`: `9` digit, `0` forced digit, `$`, `L` local currency, `.` `,` or `D` `G`, `MI` trailing minus; too few digits shows `#`s. `TO_NUMBER(text, 'fmt')` and `TO_DATE(text, 'fmt')` parse text using the model. **RR** puts a two-digit year in the century nearest the current one (00-49 → 20xx, 50-99 → 19xx in this century), unlike **YY**, which uses the current century.
```sql
SELECT TO_CHAR(DATE '2024-07-04', 'fmDay, Month ddth YYYY') a, TO_CHAR(DATE '2024-07-04', 'DY DD-MON-YY') b,
       TO_CHAR(TO_DATE('04-07-2024 15:05', 'DD-MM-YYYY HH24:MI'), 'HH:MI AM') c, TO_CHAR(DATE '2024-07-04', '"Q"Q YYYY') d
FROM dual;
SELECT TO_CHAR(1234.5, '$99,999.00') a, TO_CHAR(1234.5, '099999') b, TO_CHAR(-12, '999MI') c, TO_CHAR(123456, '9,999') d,
       TO_NUMBER('$1,250.75', '$9,999.99') + 1 e
FROM dual;
SELECT TO_CHAR(TO_DATE('15-MAR-95', 'DD-MON-RR'), 'YYYY') rr, TO_CHAR(TO_DATE('15-MAR-95', 'DD-MON-YY'), 'YYYY') yy,
       TO_CHAR(TO_DATE('15-MAR-25', 'DD-MON-RR'), 'YYYY') rr2
FROM dual;
```
Output:
```
A                       B             C        D
----------------------- ------------- -------- -------
Thursday, July 4th 2024 THU 04-JUL-24 03:05 PM Q3 2024

A           B       C    D               E
----------- ------- ---- ------ ----------
  $1,234.50  001235  12- ######    1251.75

RR   YY   RR2
---- ---- ----
1995 2095 2025
```

#### 5.4 Nest multiple functions
Single-row functions nest to any depth and are evaluated **innermost first**. Group functions nest at most two deep (S08). **Conditional expressions:** the searched `CASE WHEN cond THEN r ... ELSE r END`, the simple `CASE expr WHEN value THEN r ... END` (ANSI; returns NULL if nothing matches and there's no ELSE), and Oracle's `DECODE(expr, search1, result1, ..., default)`, where NULL matches NULL.
```sql
SELECT last_name, UPPER(CONCAT(SUBSTR(last_name, 1, 3), '_')) code, NVL(TO_CHAR(manager_id), 'No manager') mgr,
       CASE WHEN salary >= 15000 THEN 'high' WHEN salary >= 8000 THEN 'mid' ELSE 'low' END band,
       CASE job_id WHEN 'AD_PRES' THEN 'the boss' WHEN 'AD_VP' THEN 'deputy' END simple_case,
       DECODE(department_id, 90, 'Exec', 60, 'IT', NULL, 'none', 'other') dec
FROM employees WHERE employee_id IN (100, 101, 103, 141, 178) ORDER BY employee_id;
SELECT TO_CHAR(NEXT_DAY(ADD_MONTHS(DATE '2024-01-15', 6), 'MONDAY'), 'fmDay DD Month YYYY') nested FROM dual;
```
Output:
```
LAST_NAME    CODE          MGR                                      BAND SIMPLE_C DEC
------------ ------------- ---------------------------------------- ---- -------- -----
King         KIN_          No manager                               high the boss Exec
Kochhar      KOC_          100                                      high deputy   Exec
Hunold       HUN_          101                                      mid  (null)   IT
Rajs         RAJ_          124                                      low  (null)   other
Grant        GRA_          149                                      low  (null)   none

NESTED
-------------------
Monday 22 July 2024
```

## Explicitly not here
Group functions are S08.
