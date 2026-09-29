# S06_Operators_and_User_Interaction - Test: Operators and user interaction

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
let x = 10;
x -= 3;
x *= 2;
x %= 5;
console.log(x);
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log(1 + '1' - 1, '2' ** 3, 10 % -3);
```
3. What does this log? (If it throws, name the error.)
```javascript
console.log(0 == false, '' == 0, null == false, undefined == null, 1 === 1.0);
```
4. What does this log? (If it throws, name the error.)
```javascript
const n = 0;
console.log(n || 5, n ?? 5, !!'false');
```
5. What does this log? (If it throws, name the error.)
```javascript
const o = { k: 1 };
console.log(delete o.k, 'k' in o, typeof o.k);
```
6. What does this log? (If it throws, name the error.)
```javascript
console.log(2 * 3 ** 2, (2 * 3) ** 2, 1 + 2 > 2 && 'yes');
```
7. What can prompt() return? Choose every correct option.
   A. A number when the user types digits
   B. A string
   C. null if the user cancels
   D. undefined if the user cancels
8. What does this log? (If it throws, name the error.)
```javascript
const score = 72;
console.log(score >= 80 ? 'A' : score >= 70 ? 'B' : 'C');
```

## Answer key (for the tutor only)
1. Actual result (from running it):
```
4
```
2. Actual result (from running it):
```
10 8 1
```
3. Actual result (from running it):
```
true true false true true
```
4. Actual result (from running it):
```
5 0 true
```
5. Actual result (from running it):
```
true false undefined
```
6. Actual result (from running it):
```
18 36 yes
```
7. Correct: B, C (exactly these options, no others)
8. Actual result (from running it):
```
B
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Operators_and_User_Interaction` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Conditional_Execution.
