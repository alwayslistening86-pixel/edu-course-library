# S16_Time_Zones_and_Intervals - Test: Time zones, timestamps and INTERVAL types

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
COLUMN iv FORMAT A30
SELECT TIMESTAMP '2024-05-01 10:00:00' - TIMESTAMP '2024-04-29 22:15:30' iv FROM dual;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT DATE '2024-03-31' + INTERVAL '1' MONTH FROM dual;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
COLUMN t FORMAT A30
SELECT TO_CHAR(FROM_TZ(TIMESTAMP '2024-12-01 09:00:00', '+02:00') AT TIME ZONE '-05:00', 'YYYY-MM-DD HH24:MI TZH:TZM') t FROM dual;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT EXTRACT(DAY FROM INTERVAL '3 20:00:00' DAY TO SECOND) d, EXTRACT(HOUR FROM INTERVAL '3 20:00:00' DAY TO SECOND) h, EXTRACT(MONTH FROM TO_YMINTERVAL('01-07')) m FROM dual;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT INTERVAL '365' DAY FROM dual;
```
6. Which data type stores a timestamp normalised to the database time zone and displays it in the session time zone? (choose one) Choose every correct option.
   A. TIMESTAMP WITH LOCAL TIME ZONE
   B. TIMESTAMP WITH TIME ZONE
   C. `TIMESTAMP`
   D. `DATE`
7. After ALTER SESSION SET TIME_ZONE = '+08:00', which values change? (choose two) Choose every correct option.
   A. `CURRENT_DATE`
   B. `SYSDATE`
   C. `LOCALTIMESTAMP`
   D. `SYSTIMESTAMP`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
IV
------------------------------
+000000001 11:44:30.000000000
```
2. Actual result (from running it):
```
(error: ORA-01839: date not valid for month specified)
```
3. Actual result (from running it):
```
T
------------------------------
2024-12-01 02:00 -05:00
```
4. Actual result (from running it):
```
         D          H          M
---------- ---------- ----------
         3         20          7
```
5. Actual result (from running it):
```
(error: ORA-01873: the leading precision of the interval is too small)
```
6. Correct: A (exactly these options, no others)
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S16_Time_Zones_and_Intervals` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
