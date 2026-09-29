# S03_Primitive_Types_and_Strings - Test: Primitive types and strings

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(0.5 + 0.25, 1 / 0, typeof NaN, NaN === NaN);
```
2. What does this log? (If it throws, name the error.)
```javascript
let u;
console.log(u, typeof u, typeof null, u == null);
```
3. What does this log? (If it throws, name the error.)
```javascript
console.log(Number.MAX_SAFE_INTEGER + 2, 9007199254740991n + 2n);
```
4. What does this log? (If it throws, name the error.)
```javascript
const s = 'dataset';
console.log(s.slice(-3), s.slice(2, 4), s.charAt(10), s[10]);
```
5. What does this log? (If it throws, name the error.)
```javascript
console.log('a-b-c'.split('-').length, `line1\nline2`.split('\n'));
```
6. Which throw a TypeError? Choose every correct option.
   A. `1n + 1`
   B. `1n + 1n`
   C. `Number(1n) + 1`
   D. `'1' + 1n`
7. What does this log? (If it throws, name the error.)
```javascript
console.log(0x10, 0b11, 0o10, 2e3);
```

## Answer key (for the tutor only)
1. Actual result (from running it):
```
0.75 Infinity number false
```
2. Actual result (from running it):
```
undefined undefined object true
```
3. Actual result (from running it):
```
9007199254740992 9007199254740993n
```
4. Actual result (from running it):
```
set ta  undefined
```
5. Actual result (from running it):
```
3 [ 'line1', 'line2' ]
```
6. Correct: A (exactly these options, no others)
7. Actual result (from running it):
```
16 3 8 2000
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Primitive_Types_and_Strings` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Type_Conversion.
