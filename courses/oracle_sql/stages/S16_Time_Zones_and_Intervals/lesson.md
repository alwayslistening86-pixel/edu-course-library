# S16_Time_Zones_and_Intervals - Lesson: Time zones, timestamps and INTERVAL types

## Goal
The learner distinguishes SYSDATE, CURRENT_DATE, CURRENT_TIMESTAMP, LOCALTIMESTAMP and SYSTIMESTAMP, works with TIMESTAMP WITH (LOCAL) TIME ZONE, converts between time zones, and uses INTERVAL YEAR TO MONTH and DAY TO SECOND values and functions.

## Syllabus items taught here
- 16.1 - Work with CURRENT_DATE, CURRENT_TIMESTAMP and LOCALTIMESTAMP
- 16.2 - Work with INTERVAL data types

## How to teach this
Ask which of SYSDATE and CURRENT_DATE changes when you run ALTER SESSION SET TIME_ZONE, and why. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 16.1 Work with CURRENT_DATE, CURRENT_TIMESTAMP and LOCALTIMESTAMP
`SYSDATE` (DATE) and `SYSTIMESTAMP` (TIMESTAMP WITH TIME ZONE) come from the **database server's** operating system clock. `CURRENT_DATE` (DATE), `CURRENT_TIMESTAMP` (TIMESTAMP WITH TIME ZONE) and `LOCALTIMESTAMP` (TIMESTAMP, no zone) are in the **session** time zone, which you change with `ALTER SESSION SET TIME_ZONE = '+05:30' | 'Europe/London' | LOCAL | DBTIMEZONE`. `SESSIONTIMEZONE` and `DBTIMEZONE` show the settings. Types: `TIMESTAMP [(fractional precision, default 6)]`, `TIMESTAMP WITH TIME ZONE` (stores the offset or region), `TIMESTAMP WITH LOCAL TIME ZONE` (normalised to the database time zone on storage and shown in the session's zone). Functions: `FROM_TZ(ts, zone)`, `ts AT TIME ZONE zone`, `TZ_OFFSET(zone)`, `EXTRACT(TIMEZONE_HOUR | TIMEZONE_REGION ... FROM ts)`, `TO_TIMESTAMP`, `TO_TIMESTAMP_TZ`, `CAST`. (The actual clock values change every run, so the example shows only what doesn't.)
```sql
COLUMN sess FORMAT A18
ALTER SESSION SET TIME_ZONE = '+05:30';
SELECT SESSIONTIMEZONE sess, EXTRACT(TIMEZONE_HOUR FROM CURRENT_TIMESTAMP) tz_h, EXTRACT(TIMEZONE_MINUTE FROM CURRENT_TIMESTAMP) tz_m,
       ROUND((CAST(LOCALTIMESTAMP AS DATE) - CURRENT_DATE) * 1440) diff_minutes FROM dual;
ALTER SESSION SET TIME_ZONE = 'America/New_York';
SELECT SESSIONTIMEZONE sess, TO_CHAR(FROM_TZ(TIMESTAMP '2024-01-15 12:00:00', 'Europe/London'), 'TZH:TZM') jan,
       TO_CHAR(FROM_TZ(TIMESTAMP '2024-07-15 12:00:00', 'Europe/London'), 'TZH:TZM') jul FROM dual;
SELECT TO_CHAR(FROM_TZ(TIMESTAMP '2024-07-04 12:00:00', 'Europe/London') AT TIME ZONE 'Asia/Tokyo', 'YYYY-MM-DD HH24:MI TZR') tokyo_time,
       TO_CHAR(FROM_TZ(TIMESTAMP '2024-01-15 12:00:00', 'America/New_York') AT TIME ZONE 'UTC', 'HH24:MI TZH:TZM') utc_time
FROM dual;
CREATE TABLE flights (id NUMBER, dep TIMESTAMP WITH LOCAL TIME ZONE);
INSERT INTO flights VALUES (1, TIMESTAMP '2024-07-04 09:00:00 -04:00');
ALTER SESSION SET TIME_ZONE = '+01:00';
SELECT TO_CHAR(dep, 'YYYY-MM-DD HH24:MI') shown_in_session_zone FROM flights;
```
Output:
```
Session altered.

SESS                     TZ_H       TZ_M DIFF_MINUTES
------------------ ---------- ---------- ------------
+05:30                      5         30            0

Session altered.

SESS               JAN    JUL
------------------ ------ ------
America/New_York   +00:00 +01:00

TOKYO_TIME                                        UTC_TIME
------------------------------------------------- ------------
2024-07-04 20:00 ASIA/TOKYO                       17:00 +00:00

Table created.

1 row created.

Session altered.

SHOWN_IN_SESSION
----------------
2024-07-04 14:00
```
(A region name such as Europe/London carries daylight-saving rules, so its offset depends on the date: +00:00 in January, +01:00 in July. `TZ_OFFSET('Europe/London')` returns today's offset, so its answer changes with the season. That's why you store region names rather than fixed offsets when DST matters.)

#### 16.2 Work with INTERVAL data types
`INTERVAL YEAR [(p)] TO MONTH` stores years and months; `INTERVAL DAY [(p)] TO SECOND [(f)]` stores days, hours, minutes and seconds. Literals: `INTERVAL '1-6' YEAR TO MONTH`, `INTERVAL '3' MONTH`, `INTERVAL '2 10:30:00' DAY TO SECOND`, `INTERVAL '90' MINUTE`. Functions: `TO_YMINTERVAL('01-02')`, `TO_DSINTERVAL('2 03:00:00')`, `NUMTOYMINTERVAL(n, 'MONTH')`, `NUMTODSINTERVAL(n, 'HOUR')`, `EXTRACT(DAY | HOUR ... FROM interval)`. Datetime ± interval gives a datetime, and timestamp − timestamp gives an INTERVAL DAY TO SECOND. Adding a month interval to a date whose day doesn't exist in the target month raises ORA-01839 (unlike ADD_MONTHS, which adjusts). The default leading precision is 2, so `INTERVAL '120' DAY` needs `DAY(3)`.
```sql
COLUMN b FORMAT A32
COLUMN c FORMAT A30
COLUMN y FORMAT A14
COLUMN d FORMAT A30
COLUMN big FORMAT A20
COLUMN length FORMAT A14
SELECT DATE '2024-01-15' + INTERVAL '1-6' YEAR TO MONTH a, TIMESTAMP '2024-01-15 08:00:00' + INTERVAL '2 10:30:00' DAY TO SECOND b,
       TIMESTAMP '2024-03-01 12:00:00' - TIMESTAMP '2024-02-28 06:30:00' c
FROM dual;
SELECT TO_YMINTERVAL('03-04') y, NUMTODSINTERVAL(100, 'HOUR') d, EXTRACT(HOUR FROM NUMTODSINTERVAL(100, 'HOUR')) h, INTERVAL '120' DAY(3) big,
       ADD_MONTHS(DATE '2024-01-31', 1) am
FROM dual;
CREATE TABLE warranties (product VARCHAR2(10), length INTERVAL YEAR(2) TO MONTH);
INSERT INTO warranties VALUES ('laptop', INTERVAL '2-6' YEAR TO MONTH);
SELECT product, length, DATE '2024-05-10' + length expires FROM warranties;
SELECT DATE '2024-01-31' + INTERVAL '1' MONTH FROM dual;
```
Output:
```
A                  B                                C
------------------ -------------------------------- ------------------------------
15-JUL-25          17-JAN-24 06.30.00.000000000 PM  +000000002 05:30:00.000000000

Y              D                                       H BIG                  AM
-------------- ------------------------------ ---------- -------------------- ------------------
+000000003-04  +000000004 04:00:00.000000000           4 +120 00:00:00        29-FEB-24

Table created.

1 row created.

PRODUCT    LENGTH         EXPIRES
---------- -------------- ------------------
laptop     +02-06         10-NOV-26
(error: ORA-01839: date not valid for month specified)
```

## Explicitly not here
This is the last stage; the cumulative exam follows.
