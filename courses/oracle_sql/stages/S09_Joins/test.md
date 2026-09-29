# S09_Joins - Test: Joins: equijoins, self, non-equi, outer and Cartesian

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name, department_name FROM employees NATURAL JOIN departments ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT e.last_name emp, m.last_name mgr FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id WHERE e.department_id IN (60, 90) ORDER BY 1;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT g.grade_level, COUNT(e.employee_id) n FROM job_grades g LEFT JOIN employees e ON e.salary BETWEEN g.lowest_sal AND g.highest_sal GROUP BY g.grade_level ORDER BY 1;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT d.department_name, e.last_name FROM departments d, employees e WHERE d.department_id = e.department_id(+) AND d.department_id IN (10, 110) ORDER BY 1;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT department_id, d.department_name FROM employees JOIN departments d USING (department_id) WHERE last_name = 'King';
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT e.last_name, l.city FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id WHERE l.country_id = 'UK' ORDER BY 1;
```
7. Which are true of the (+) outer join operator? (choose two) Choose every correct option.
   A. It goes on the side that may have no matching row
   B. It can produce a full outer join when placed on both sides
   C. It can't be combined with an OR condition on that join
   D. It is ANSI standard syntax

## Answer key (for the tutor only)
1. Actual result (from running it):
```
LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Abel         Sales
Ernst        IT
Kochhar      Executive
Rajs         Shipping
```
2. Actual result (from running it):
```
EMP          MGR
------------ ------------
Ernst        Hunold
Hunold       Kochhar
King         (null)
Kochhar      King
```
3. Actual result (from running it):
```
G          N
- ----------
A          0
B          3
C          3
D          3
E          2
```
4. Actual result (from running it):
```
DEPARTMENT_NAME      LAST_NAME
-------------------- ------------
Accounting           (null)
Administration       Whalen
```
5. Actual result (from running it):
```
DEPARTMENT_ID DEPARTMENT_NAME
------------- --------------------
           90 Executive
```
6. Actual result (from running it):
```
LAST_NAME    CITY
------------ --------------------
Abel         Oxford
Zlotkey      Oxford
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Joins` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Subqueries.
