# S01_Object_Literals_and_Properties - Test: Object literals and properties

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const x = 1, y = 2;
const o = { x, y, sum: x + y };
console.log(o);
```
2. What does this log? (If it throws, name the error.)
```javascript
const o = { key: 'dot' };
const key = 'other';
o[key] = 'bracket';
console.log(o.key, o.other, o['key']);
```
3. What does this log? (If it throws, name the error.)
```javascript
const o = { a: { b: null } };
console.log(o.a?.b?.c, o.z?.b);
```
4. What does this log? (If it throws, name the error.)
```javascript
const o = { n: 1 };
console.log(delete o.n, delete o.missing, o);
```
5. Which need bracket notation? Choose every correct option.
   A. `o['first name']`
   B. `o[varHoldingKey]`
   C. `o['total']`
   D. `o['item-' + i]`
6. What does this log? (If it throws, name the error.)
```javascript
const o = {};
try {
  o.deep.value = 1;
} catch (e) {
  console.log(e.name);
}
```

## Answer key (for the tutor only)
1. Actual result (from running it):
```
{ x: 1, y: 2, sum: 3 }
```
2. Actual result (from running it):
```
dot bracket dot
```
3. Actual result (from running it):
```
undefined undefined
```
4. Actual result (from running it):
```
true true {}
```
5. Correct: A, B, D (exactly these options, no others)
6. Actual result (from running it):
```
TypeError
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Object_Literals_and_Properties` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Enumerating_Comparing_and_Copying_Objects.
