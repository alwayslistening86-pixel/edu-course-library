# S04_Type_Conversion - Test: Type conversion

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(String(123).length, String(true) + 1);
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log(Boolean(0), Boolean('0'), Boolean(' '), Boolean(null), Boolean({}));
```
3. What does this log? (If it throws, name the error.)
```javascript
console.log(Number(undefined), Number(null), Number([]), Number('0x1A'));
```
4. What does this log? (If it throws, name the error.)
```javascript
console.log('8' / '2', '8' + '2', +'8' + +'2', '5' - - '2');
```
5. What does this log? (If it throws, name the error.)
```javascript
console.log(parseInt('15.9kg'), parseFloat('15.9kg'), Number('15.9kg'));
```
6. What does this log? (If it throws, name the error.)
```javascript
try {
  BigInt(1.5);
} catch (e) {
  console.log(e.name);
}
console.log(BigInt('20') + 1n);
```
7. Which values are falsy? Choose every correct option.
   A. `0`
   B. `'0'`
   C. `''`
   D. `[]`
   E. `NaN`
   F. `null`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3 true1
```
2. Actual result (from running it):
```
false true true false true
```
3. Actual result (from running it):
```
NaN 0 0 26
```
4. Actual result (from running it):
```
4 82 10 7
```
5. Actual result (from running it):
```
15 15.9 NaN
```
6. Actual result (from running it):
```
RangeError
21n
```
7. Correct: A, C, E, F (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Type_Conversion` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Objects_and_Arrays.
