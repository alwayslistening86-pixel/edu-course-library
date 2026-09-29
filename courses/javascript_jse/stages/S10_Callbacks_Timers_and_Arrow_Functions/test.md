# S10_Callbacks_Timers_and_Arrow_Functions - Test: Callbacks, timers and arrow functions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
setTimeout(() => console.log('two'), 20);
setTimeout(() => console.log('one'), 5);
console.log('zero');
```
2. What does this log? (If it throws, name the error.)
```javascript
const sq = n => { n * n; };
const sq2 = n => n * n;
console.log(sq(3), sq2(3));
```
3. What does this log? (If it throws, name the error.)
```javascript
function each(arr, cb) {
  for (const x of arr) cb(x);
}
let s = 0;
each([1, 2, 3], x => { s += x; });
console.log(s);
```
4. What does this log? (If it throws, name the error.)
```javascript
let n = 0;
const id = setInterval(() => {
  n++;
  if (n === 4) {
    clearInterval(id);
    console.log('stopped at', n);
  }
}, 1);
```
5. What does this log? (If it throws, name the error.)
```javascript
const add = (a, b = 10) => a + b;
console.log(add(1), add(1, 1), [1, 2].map(x => x * 10));
```
6. Which are valid arrow functions? Choose every correct option.
   A. `x => x + 1`
   B. `(x, y) => x * y`
   C. `=> 5`
   D. `() => {}`
7. Using setTimeout, print 'ready' 100 ms after the script starts, and print 'waiting' immediately.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
zero
one
two
```
2. Actual result (from running it):
```
undefined 9
```
3. Actual result (from running it):
```
6
```
4. Actual result (from running it):
```
stopped at 4
```
5. Actual result (from running it):
```
11 2 [ 10, 20 ]
```
6. Correct: A, B, D (exactly these options, no others)
7. The tutor runs or reads the learner's answer and checks: waiting appears first, then ready; uses a callback passed to setTimeout.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Callbacks_Timers_and_Arrow_Functions` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Errors_Exceptions_and_Debugging.
