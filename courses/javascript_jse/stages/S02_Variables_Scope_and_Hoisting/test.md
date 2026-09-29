# S02_Variables_Scope_and_Hoisting - Test: Variables, scope and hoisting

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const arr = [1];
arr.push(2);
console.log(arr.length);
```
2. What does this log? (If it throws, name the error.)
```javascript
try {
  const k = 1;
  k = 2;
} catch (e) {
  console.log(e.name);
}
```
3. What does this log? (If it throws, name the error.)
```javascript
if (true) {
  var a = 'var';
  let b = 'let';
}
console.log(a, typeof b);
```
4. What does this log? (If it throws, name the error.)
```javascript
try {
  console.log(z);
  let z = 3;
} catch (e) {
  console.log(e.name);
}
```
5. What does this log? (If it throws, name the error.)
```javascript
let x = 1;
function f() {
  let x = 2;
  return x;
}
console.log(f(), x);
```
6. Which declarations must be given a value immediately? Choose every correct option.
   A. `let`
   B. `const`
   C. `var`
7. What does this log? (If it throws, name the error.)
```javascript
for (var i = 0; i < 3; i++) {}
console.log(i);
```

## Answer key (for the tutor only)
1. Actual result (from running it):
```
2
```
2. Actual result (from running it):
```
TypeError
```
3. Actual result (from running it):
```
var undefined
```
4. Actual result (from running it):
```
ReferenceError
```
5. Actual result (from running it):
```
2 1
```
6. Correct: B (exactly these options, no others)
7. Actual result (from running it):
```
3
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Variables_Scope_and_Hoisting` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Primitive_Types_and_Strings.
