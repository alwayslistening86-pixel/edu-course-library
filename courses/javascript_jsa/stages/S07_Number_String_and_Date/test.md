# S07_Number_String_and_Date - Test: Number, String and Date

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(Number(''), Number('12px'), parseFloat('.5e1'), (0.1 * 3).toFixed(2));
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log(Number.isNaN(NaN), Number.isNaN('x'), isNaN('x'), Number.isInteger('5'));
```
3. What does this log? (If it throws, name the error.)
```javascript
console.log((255).toString(16).toUpperCase(), (8).toString(2).padStart(8, '0'));
```
4. What does this log? (If it throws, name the error.)
```javascript
const s = 'JavaScript';
console.log(s.toLowerCase().indexOf('script'), s.startsWith('Java'), s.slice(-6).toUpperCase(), s.split('a'));
```
5. What does this log? (If it throws, name the error.)
```javascript
const d = new Date(Date.UTC(2026, 11, 25));
console.log(d.getUTCMonth(), d.getUTCDay(), d.getUTCFullYear());
```
6. What does this log? (If it throws, name the error.)
```javascript
const a = new Date('2026-03-01T00:00:00Z');
const b = new Date('2026-02-01T00:00:00Z');
console.log((a - b) / 86400000);
```
7. Which return strings? Choose every correct option.
   A. `(5).toFixed(2)`
   B. `Number('5')`
   C. `(5).toString(2)`
   D. `parseInt('5')`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
0 NaN 5 0.30
```
2. Actual result (from running it):
```
true false true false
```
3. Actual result (from running it):
```
FF 00001000
```
4. Actual result (from running it):
```
4 true SCRIPT [ 'J', 'v', 'Script' ]
```
5. Actual result (from running it):
```
11 5 2026
```
6. Actual result (from running it):
```
28
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Number_String_and_Date` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Arrays_and_Array_Methods.
