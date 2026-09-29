# S06_Dates - Lesson: Date arithmetic and date functions

## Goal
The learner does arithmetic with DATE values, and uses SYSDATE, MONTHS_BETWEEN, ADD_MONTHS, NEXT_DAY, LAST_DAY, ROUND and TRUNC on dates, plus EXTRACT.

## Syllabus items taught here
- 4.2 - Perform arithmetic with date data
- 4.4 - Manipulate dates with the date functions

## How to teach this
Ask what data type `hire_date + 7`, `hire_date - hire_date` and `hire_date + hire_date` each give. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 4.2 Perform arithmetic with date data
An Oracle **DATE** holds century, year, month, day, hour, minute and second (the default display format here is `DD-MON-RR`, so the time is hidden). **date + number** or **date - number** adds or subtracts days (fractions are parts of a day: `+ 1/24` is an hour), giving a DATE. **date - date** gives the number of days between them (a NUMBER). **date + date** is an error. `SYSDATE` returns the database server's current date and time.
```sql
SELECT last_name, hire_date, hire_date + 7 week_later, TO_CHAR(hire_date + 1/24, 'DD-MON-YYYY HH24:MI') plus_hour,
       DATE '2024-01-01' - hire_date days_to_2024
FROM employees WHERE employee_id = 100;
SELECT ROUND((DATE '2024-03-01' - DATE '2023-03-01') / 7, 2) weeks FROM dual;
```
Output:
```
LAST_NAME    HIRE_DATE          WEEK_LATER         PLUS_HOUR                  DAYS_TO_2024
------------ ------------------ ------------------ -------------------------- ------------
King         17-JUN-03          24-JUN-03          17-JUN-2003 01:00                  7503

     WEEKS
----------
     52.29
```
```sql
SELECT hire_date + hire_date FROM employees WHERE employee_id = 100;
```
Output:
```
(error: ORA-00975: date + date not allowed)
```

#### 4.4 Manipulate dates with the date functions
`MONTHS_BETWEEN(d1, d2)` (negative if d1 is earlier; fractional); `ADD_MONTHS(d, n)` (keeps the last day of the month); `NEXT_DAY(d, 'FRIDAY')` (the next such day *after* d); `LAST_DAY(d)`; `ROUND(d, 'MONTH' | 'YEAR')` (months round up from the 16th, years from 1 July) and `TRUNC(d, 'MONTH' | 'YEAR')`; `EXTRACT(YEAR | MONTH | DAY FROM d)`.
```sql
SELECT MONTHS_BETWEEN(DATE '2024-03-31', DATE '2024-01-31') a, ROUND(MONTHS_BETWEEN(DATE '2024-01-01', DATE '2024-03-16'), 2) b,
       ADD_MONTHS(DATE '2024-01-31', 1) c, ADD_MONTHS(DATE '2024-02-29', 12) d, NEXT_DAY(DATE '2024-07-05', 'FRIDAY') e,
       LAST_DAY(DATE '2023-02-10') f
FROM dual;
SELECT ROUND(DATE '2024-07-16', 'MONTH') a, TRUNC(DATE '2024-07-16', 'MONTH') b, ROUND(DATE '2024-07-01', 'YEAR') c,
       TRUNC(DATE '2024-07-01', 'YEAR') d, EXTRACT(MONTH FROM DATE '2024-07-16') e
FROM dual;
SELECT last_name, hire_date FROM employees WHERE MONTHS_BETWEEN(DATE '2008-01-01', hire_date) < 12 ORDER BY hire_date;
```
Output:
```
         A          B C                  D                  E                  F
---------- ---------- ------------------ ------------------ ------------------ ------------------
         2      -2.48 29-FEB-24          28-FEB-25          12-JUL-24          28-FEB-23

A                  B                  C                  D                           E
------------------ ------------------ ------------------ ------------------ ----------
01-AUG-24          01-JUL-24          01-JAN-25          01-JAN-24                   7

LAST_NAME    HIRE_DATE
------------ ------------------
Ernst        21-MAY-07
Grant        24-MAY-07
Mourgos      16-NOV-07
Zlotkey      29-JAN-08
```

## Explicitly not here
Formatting dates with TO_CHAR is S07; time zones are S16.
