# S08_Group_Functions - Lesson: Group functions, GROUP BY and HAVING

## Goal
The learner uses AVG, SUM, MIN, MAX, COUNT, LISTAGG and friends with DISTINCT and NULL handling, groups rows with GROUP BY, filters groups with HAVING, and spots illegal mixes of grouped and ungrouped columns.

## Syllabus items taught here
- 6.3 - Use group functions
- 6.2 - Create groups of data
- 6.1 - Restrict group results

## How to teach this
Ask why `SELECT department_id, AVG(salary) FROM employees;` fails, and how many rows `COUNT(commission_pct)` counts. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 6.3 Use group functions
**Group (aggregate) functions** return one result per group: `AVG`, `SUM` (numbers), `MIN`, `MAX` (numbers, text, dates), `COUNT(*)` (all rows), `COUNT(expr)` (non-null values), `COUNT(DISTINCT expr)`, `STDDEV`, `VARIANCE`, `LISTAGG(expr, sep) WITHIN GROUP (ORDER BY ...)`. All except `COUNT(*)` **ignore NULLs**, so `AVG(commission_pct)` averages only the non-null values; use `AVG(NVL(commission_pct, 0))` to count NULLs as zero. Group functions can be nested **two** deep (with GROUP BY).
```sql
COLUMN it_staff FORMAT A30
SELECT COUNT(*) all_rows, COUNT(commission_pct) with_comm, COUNT(DISTINCT department_id) depts, ROUND(AVG(commission_pct), 3) avg_c,
       ROUND(AVG(NVL(commission_pct, 0)), 3) avg_all, MIN(hire_date) earliest, MAX(last_name) last_alpha, SUM(salary) total
FROM employees;
SELECT LISTAGG(last_name, ', ') WITHIN GROUP (ORDER BY last_name) it_staff FROM employees WHERE department_id = 60;
SELECT MAX(AVG(salary)) best_avg FROM employees GROUP BY department_id;
```
Output:
```
  ALL_ROWS  WITH_COMM      DEPTS      AVG_C    AVG_ALL EARLIEST           LAST_ALPHA        TOTAL
---------- ---------- ---------- ---------- ---------- ------------------ ------------ ----------
        11          3          6       .217       .059 17-JUN-03          Zlotkey          111200

IT_STAFF
------------------------------
Ernst, Hunold

  BEST_AVG
----------
     20500
```

#### 6.2 Create groups of data
`GROUP BY` divides rows into groups. Every column or expression in the SELECT list that isn't inside a group function **must** be in the GROUP BY clause (the reverse needn't hold). You can group by several columns. NULL forms its own group. WHERE filters **rows before** grouping, and can't contain group functions. (In the release used here, and in the exam, you can't GROUP BY a column alias.)
```sql
SELECT department_id, job_id, COUNT(*) n, SUM(salary) total
FROM employees WHERE department_id IN (50, 60, 80) OR department_id IS NULL
GROUP BY department_id, job_id ORDER BY department_id, job_id;
SELECT AVG(salary) FROM employees GROUP BY department_id HAVING COUNT(*) > 1 ORDER BY 1;
```
Output:
```
DEPARTMENT_ID JOB_ID              N      TOTAL
------------- ---------- ---------- ----------
           50 ST_CLERK            1       3500
           50 ST_MAN              1       5800
           60 IT_PROG             2      15000
           80 SA_MAN              1      10500
           80 SA_REP              1      11000
(null)        SA_REP              1       7000

6 rows selected.

AVG(SALARY)
-----------
       4650
       7500
      10750
      20500
```
```sql
SELECT department_id, last_name, AVG(salary) FROM employees GROUP BY department_id;
```
Output:
```
(error: ORA-00979: "LAST_NAME": must appear in the GROUP BY clause or be used in an aggregate function)
```

#### 6.1 Restrict group results
`HAVING` filters **groups after** grouping and may use group functions (WHERE may not). Order of evaluation: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY. HAVING can come before GROUP BY in the text, but it's clearer after.
```sql
SELECT department_id, MAX(salary) top_pay, COUNT(*) n
FROM employees WHERE job_id NOT LIKE '%CLERK%'
GROUP BY department_id HAVING MAX(salary) > 9000 ORDER BY top_pay DESC;
```
Output:
```
DEPARTMENT_ID    TOP_PAY          N
------------- ---------- ----------
           90      24000          2
           20      13000          1
           80      11000          2
```
```sql
SELECT department_id, AVG(salary) FROM employees WHERE AVG(salary) > 8000 GROUP BY department_id;
```
Output:
```
(error: ORA-00934: group function is not allowed here)
```

## Explicitly not here
Joins are S09.
