# S05_Character_and_Number_Functions - Lesson: Character functions and ROUND, TRUNC and MOD

## Goal
The learner applies the character functions in SELECT and WHERE, and uses ROUND, TRUNC and MOD with positive, zero and negative precision.

## Syllabus items taught here
- 4.1 - Manipulate strings with character functions in SQL SELECT and WHERE clauses
- 4.3 - Manipulate numbers with the ROUND, TRUNC and MOD functions

## How to teach this
Ask what `SUBSTR('Oracle', -3)` and `INSTR('banana', 'a', 1, 3)` return. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 4.1 Manipulate strings with character functions in SQL SELECT and WHERE clauses
**Case:** `LOWER`, `UPPER`, `INITCAP`. **Manipulation:** `CONCAT(a, b)` (exactly two arguments), `SUBSTR(s, start [, length])` (1-based; a negative start counts from the end), `LENGTH`, `INSTR(s, find [, start [, occurrence]])` (0 if not found), `LPAD`/`RPAD(s, n, pad)` (also truncate to n), `TRIM([LEADING|TRAILING|BOTH] ch FROM s)`, `LTRIM`/`RTRIM`, `REPLACE(s, old [, new])` (omitting new removes). Single-row functions return one result per row and can be used in SELECT, WHERE and ORDER BY.
```sql
SELECT INITCAP('the ORACLE way') a, CONCAT(first_name, last_name) b, SUBSTR(last_name, -3) c, SUBSTR(last_name, 2, 3) d,
       LENGTH(last_name) e, INSTR('banana', 'a', 1, 3) f, INSTR('banana', 'x') g
FROM employees WHERE employee_id = 101;
SELECT LPAD(salary, 8, '*') a, RPAD(last_name, 4) b, TRIM('x' FROM 'xxhixx') c, TRIM(LEADING '0' FROM '00420') d,
       REPLACE('a-b-c', '-') e, REPLACE('Jack and Jue', 'J', 'Bl') f
FROM employees WHERE employee_id = 200;
SELECT last_name FROM employees WHERE UPPER(SUBSTR(last_name, 1, 1)) = 'K' AND LENGTH(last_name) < 7 ORDER BY 1;
```
Output:
```
A              B                        C            D                     E          F          G
-------------- ------------------------ ------------ ------------ ---------- ---------- ----------
The Oracle Way NeenaKochhar             har          och                   7          6          0

A                                B                C  D   E   F
-------------------------------- ---------------- -- --- --- --------------
****4400                         Whal             hi 420 abc Black and Blue

LAST_NAME
------------
King
```

#### 4.3 Manipulate numbers with the ROUND, TRUNC and MOD functions
`ROUND(n [, d])` rounds to d decimal places (d defaults to 0; a negative d rounds to the left of the point: -1 tens, -2 hundreds); `TRUNC(n [, d])` cuts off without rounding; `MOD(m, n)` is the remainder of m / n, taking the sign of m, and `MOD(m, 0)` returns m.
```sql
SELECT ROUND(45.926, 2) a, ROUND(45.926) b, ROUND(45.926, -1) c, ROUND(55, -2) d, TRUNC(45.926, 2) e, TRUNC(45.926, -1) f,
       MOD(17, 5) g, MOD(-17, 5) h, MOD(17, 0) i, ROUND(-2.5) j
FROM dual;
SELECT last_name, salary FROM employees WHERE MOD(salary, 1000) <> 0 ORDER BY salary;
```
Output:
```
         A          B          C          D          E          F          G          H          I          J
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
     45.93         46         50        100      45.92         40          2         -2         17         -3

LAST_NAME        SALARY
------------ ----------
Rajs               3500
Whalen             4400
Mourgos            5800
Zlotkey           10500
```

## Explicitly not here
Dates are S06; TO_CHAR is S07.
