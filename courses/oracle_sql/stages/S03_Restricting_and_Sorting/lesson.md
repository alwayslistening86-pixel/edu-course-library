# S03_Restricting_and_Sorting - Lesson: WHERE, operator precedence, row limiting and ORDER BY

## Goal
The learner filters rows with comparison, BETWEEN, IN, LIKE, IS NULL and logical operators in the right precedence, limits rows with FETCH/OFFSET, and sorts with ORDER BY, including NULL ordering and positional or alias sorting.

## Syllabus items taught here
- 3.1 - Apply the rules of precedence for operators in an expression
- 3.2 - Limit the rows returned in a SQL statement
- 3.5 - Sort data

## How to teach this
Ask what `WHERE job_id = 'SA_REP' OR job_id = 'AD_PRES' AND salary > 15000` returns, then add parentheses and ask again. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 3.1 Apply the rules of precedence for operators in an expression
WHERE conditions use `= <> != ^= < > <= >=`, `BETWEEN low AND high` (inclusive; low must come first), `IN (list)`, `LIKE` with `%` (any string) and `_` (one character) and an optional `ESCAPE` character, and `IS [NOT] NULL` (never `= NULL`). **Precedence:** arithmetic, then concatenation, then comparison, then `IS NULL`/`LIKE`/`IN`, then `BETWEEN`, then `<>`, then **NOT**, then **AND**, then **OR**. Use parentheses to override. `NOT IN` a list containing NULL returns no rows.
```sql
SELECT last_name, job_id, salary FROM employees
WHERE  job_id = 'SA_REP' OR job_id = 'AD_PRES' AND salary > 15000 ORDER BY last_name;
SELECT last_name, job_id, salary FROM employees
WHERE  (job_id = 'SA_REP' OR job_id = 'AD_PRES') AND salary > 15000 ORDER BY last_name;
SELECT last_name FROM employees WHERE last_name LIKE '_a%' OR job_id LIKE 'AD\_%' ESCAPE '\' ORDER BY 1;
SELECT COUNT(*) FROM employees WHERE department_id NOT IN (10, NULL);
SELECT last_name FROM employees WHERE commission_pct IS NOT NULL AND salary BETWEEN 7000 AND 10500 ORDER BY 1;
```
Output:
```
LAST_NAME    JOB_ID         SALARY
------------ ---------- ----------
Abel         SA_REP          11000
Grant        SA_REP           7000
King         AD_PRES         24000

LAST_NAME    JOB_ID         SALARY
------------ ---------- ----------
King         AD_PRES         24000

LAST_NAME
------------
Hartstein
King
Kochhar
Rajs
Whalen

  COUNT(*)
----------
         0

LAST_NAME
------------
Grant
Zlotkey
```

#### 3.2 Limit the rows returned in a SQL statement
**Row limiting** (12c+) comes after ORDER BY: `OFFSET n ROWS FETCH {FIRST|NEXT} n [PERCENT] ROWS {ONLY | WITH TIES}`. WITH TIES also returns rows that tie with the last one (it needs ORDER BY). Without ORDER BY, which rows you get is undefined. The older **ROWNUM** pseudocolumn is assigned *before* ORDER BY, so `WHERE ROWNUM <= 3 ORDER BY salary` doesn't give the top 3 (use an inline view), and `WHERE ROWNUM > 1` never returns anything.
```sql
SELECT last_name, salary FROM employees ORDER BY salary DESC FETCH FIRST 3 ROWS ONLY;
SELECT last_name, salary FROM employees ORDER BY salary DESC OFFSET 3 ROWS FETCH NEXT 2 ROWS ONLY;
SELECT last_name, hire_date FROM employees ORDER BY EXTRACT(YEAR FROM hire_date) FETCH FIRST 1 ROWS WITH TIES;
SELECT COUNT(*) FROM employees WHERE ROWNUM > 1;
```
Output:
```
LAST_NAME        SALARY
------------ ----------
King              24000
Kochhar           17000
Hartstein         13000

LAST_NAME        SALARY
------------ ----------
Abel              11000
Zlotkey           10500

LAST_NAME    HIRE_DATE
------------ ------------------
King         17-JUN-03
Rajs         17-OCT-03
Whalen       17-SEP-03

  COUNT(*)
----------
         0
```

#### 3.5 Sort data
`ORDER BY` is the last clause and sorts by columns, expressions, aliases, or select-list positions (`ORDER BY 2`), ASC (the default) or DESC per column. NULLs sort **last** in ascending order and **first** in descending order, unless you say `NULLS FIRST` or `NULLS LAST`. You can sort by a column not in the select list (except with DISTINCT or set operators).
```sql
SELECT last_name, department_id dept, salary FROM employees
WHERE  employee_id IN (100, 104, 141, 178, 201)
ORDER  BY dept DESC, 3;
SELECT last_name, commission_pct FROM employees WHERE department_id = 80 OR department_id IS NULL ORDER BY commission_pct NULLS FIRST;
```
Output:
```
LAST_NAME          DEPT     SALARY
------------ ---------- ----------
Grant        (null)           7000
King                 90      24000
Ernst                60       6000
Rajs                 50       3500
Hartstein            20      13000

LAST_NAME    COMMISSION_PCT
------------ --------------
Grant                   .15
Zlotkey                  .2
Abel                     .3
```

## Explicitly not here
Substitution variables are S04.
