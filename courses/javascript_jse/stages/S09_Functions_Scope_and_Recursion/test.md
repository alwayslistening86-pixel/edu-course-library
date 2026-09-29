# S09_Functions_Scope_and_Recursion - Test: Functions, scope, function expressions and recursion

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(hoisted());
function hoisted() { return 'ok'; }
```
2. What does this log? (If it throws, name the error.)
```javascript
try {
  early();
} catch (e) {
  console.log(e.name);
}
const early = function () { return 1; };
```
3. What does this log? (If it throws, name the error.)
```javascript
let total = 0;
function add(n) {
  let total = n;
  return total;
}
console.log(add(5), total);
```
4. What does this log? (If it throws, name the error.)
```javascript
function f() {
  return;
}
function g(x) {
  if (x) return 'yes';
}
console.log(f(), g(0), g(1));
```
5. What does this log? (If it throws, name the error.)
```javascript
function count(n) {
  if (n <= 0) return '';
  return count(n - 1) + n;
}
console.log(count(4));
```
6. What does this log? (If it throws, name the error.)
```javascript
const ops = { add: function (a, b) { return a + b; } };
const fns = [Math.max, ops.add];
console.log(fns[0](3, 9, 2), fns[1](3, 9));
```
7. Which are true? Choose every correct option.
   A. A function without return returns undefined
   B. Extra arguments cause an error
   C. Missing arguments are undefined
   D. Function expressions are hoisted like declarations
8. Write a recursive function digitSum(n) that adds the digits of a positive integer, e.g. digitSum(4096) is 19.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
ok
```
2. Actual result (from running it):
```
ReferenceError
```
3. Actual result (from running it):
```
5 0
```
4. Actual result (from running it):
```
undefined undefined yes
```
5. Actual result (from running it):
```
1234
```
6. Actual result (from running it):
```
9 12
```
7. Correct: A, C (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Correct base case, recursion on Math.floor(n / 10) and n % 10; returns 19.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Functions_Scope_and_Recursion` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Callbacks_Timers_and_Arrow_Functions.
