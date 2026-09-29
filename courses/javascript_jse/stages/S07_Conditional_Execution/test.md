# S07_Conditional_Execution - Test: if and switch

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const t = 0;
if (t) {
  console.log('truthy');
} else if (t === 0) {
  console.log('zero');
} else {
  console.log('other');
}
```
2. What does this log? (If it throws, name the error.)
```javascript
let r = '';
switch (3) {
  case 1: r += '1';
  case 3: r += '3';
  case 4: r += '4';
  default: r += 'd';
}
console.log(r);
```
3. What does this log? (If it throws, name the error.)
```javascript
function f(x) {
  switch (true) {
    case x < 0: return 'neg';
    case x === 0: return 'zero';
    default: return 'pos';
  }
}
console.log(f(-2), f(0), f(9));
```
4. What does this log? (If it throws, name the error.)
```javascript
const m = 'Feb';
let days;
if (m === 'Feb') days = 28;
else if (m === 'Apr' || m === 'Jun') days = 30;
else days = 31;
console.log(days);
```
5. Which comparison does switch use to match a case? Choose every correct option.
   A. `==`
   B. `===`
   C. `Object.is`
   D. `<=`
6. Write a switch that turns a traffic-light colour string into an action ('stop', 'ready', 'go'), printing 'unknown' for anything else.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
zero
```
2. Actual result (from running it):
```
34d
```
3. Actual result (from running it):
```
neg zero pos
```
4. Actual result (from running it):
```
28
```
5. Correct: B (exactly these options, no others)
6. The tutor runs or reads the learner's answer and checks: Correct cases with break or return; default branch; strict string matching.

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Conditional_Execution` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Loops.
