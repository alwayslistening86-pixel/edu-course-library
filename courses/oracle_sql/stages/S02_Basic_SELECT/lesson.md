# S02_Basic_SELECT - Lesson: The SELECT statement, aliases, literals, DISTINCT, arithmetic and NULL

## Goal
The learner writes SELECT statements with column lists, * , aliases, arithmetic, concatenation, literals, the q-quote operator and DISTINCT, and predicts how NULL behaves in expressions.

## Syllabus items taught here
- 2.1 - Use column aliases
- 2.2 - Use the SQL SELECT statement
- 2.3 - Use the concatenation operator, literal character strings, the alternative quote operator and the DISTINCT keyword
- 2.4 - Use arithmetic expressions and NULL values in the SELECT statement

## How to teach this
Ask what `salary * 12 + commission_pct` gives for an employee whose commission_pct is NULL. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 2.1 Use column aliases
A **column alias** renames a heading: `salary*12 AS annual` or `salary*12 annual` (AS is optional). Unquoted aliases are shown in upper case and can't contain spaces; a **double-quoted** alias keeps case, spaces and special characters. Aliases can be used in ORDER BY but **not** in WHERE (the WHERE clause is evaluated before the SELECT list).
```sql
SELECT last_name AS name, salary * 12 annual, salary "Monthly Pay"
FROM   employees WHERE department_id = 60 ORDER BY annual DESC;
```
Output:
```
NAME             ANNUAL Monthly Pay
------------ ---------- -----------
Hunold           108000        9000
Ernst             72000        6000
```
```sql
SELECT last_name, salary * 12 annual FROM employees WHERE annual > 100000;
```
Output:
```
(error: ORA-00904: "ANNUAL": invalid identifier)
```

#### 2.2 Use the SQL SELECT statement
`SELECT * | {[DISTINCT] column | expression [alias], ...} FROM table;`. `*` selects every column in table order. Clauses can span lines; keywords can't be abbreviated or split. `DESCRIBE table` shows the structure. The `DUAL` table (one row, one column) is used to evaluate expressions.
```sql
SELECT * FROM job_grades WHERE grade_level IN ('A', 'E');
SELECT 7 * 6 AS answer, 'text' AS lit FROM dual;
```
Output:
```
G LOWEST_SAL HIGHEST_SAL
- ---------- -----------
A       1000        2999
E      15000       24999

    ANSWER LIT
---------- ----
        42 text
```

#### 2.3 Use the concatenation operator, literal character strings, the alternative quote operator and the DISTINCT keyword
`||` concatenates (numbers and dates are converted to text; concatenating NULL just adds nothing). **Literals**: character and date literals go in single quotes; numbers don't. An apostrophe inside a literal is written twice (`'O''Hara'`), or use the **alternative quote operator** `q'[...]'` with any delimiter pair (`[]`, `{}`, `()`, `<>`) or a repeated character (`q'!...!'`). **DISTINCT** removes duplicate rows across the **whole** select list, and must come straight after SELECT.
```sql
SELECT first_name || ' ' || last_name || q'['s job is ]' || job_id || NULL AS info
FROM   employees WHERE department_id = 60;
SELECT DISTINCT job_id FROM employees WHERE department_id IN (50, 80) ORDER BY job_id;
SELECT DISTINCT department_id, job_id FROM employees WHERE department_id = 80;
```
Output:
```
INFO
---------------------------------------------
Alexander Hunold's job is IT_PROG
Bruce Ernst's job is IT_PROG

JOB_ID
----------
SA_MAN
SA_REP
ST_CLERK
ST_MAN

DEPARTMENT_ID JOB_ID
------------- ----------
           80 SA_MAN
           80 SA_REP
```

#### 2.4 Use arithmetic expressions and NULL values in the SELECT statement
Arithmetic operators `* / + -` follow normal precedence (`*` and `/` before `+` and `-`, left to right, parentheses first) and work on numbers and dates. **NULL** means unknown or not applicable: it isn't zero or a space. Any arithmetic with NULL gives NULL (and SQL*Plus here displays NULL as `(null)`). Division by zero raises ORA-01476.
```sql
SELECT last_name, salary, commission_pct, 12 * salary + 100 a, 12 * (salary + 100) b, salary * 12 * commission_pct c
FROM   employees WHERE employee_id IN (149, 200);
```
Output:
```
LAST_NAME        SALARY COMMISSION_PCT          A          B          C
------------ ---------- -------------- ---------- ---------- ----------
Zlotkey           10500             .2     126100     127200      25200
Whalen             4400 (null)              52900      54000 (null)
```
```sql
SELECT salary / 0 FROM employees WHERE employee_id = 100;
```
Output:
```
(error: ORA-01476: divisor is equal to zero)
```

## Explicitly not here
WHERE and ORDER BY are S03; NVL is S07.
