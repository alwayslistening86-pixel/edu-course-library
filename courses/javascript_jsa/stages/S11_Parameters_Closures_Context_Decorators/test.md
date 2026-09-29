# S11_Parameters_Closures_Context_Decorators - Test: Parameters, closures, IIFEs, call/apply/bind and decorators

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
function f(x = 5) { return x; }
console.log(f(undefined), f(null), f(0));
```
2. What does this log? (If it throws, name the error.)
```javascript
function opts({ a = 1, b = 2 } = {}) { return a + b; }
console.log(opts(), opts({ b: 10 }), opts({ a: 0, b: 0 }));
```
3. What does this log? (If it throws, name the error.)
```javascript
function counter() {
  let n = 0;
  return () => ++n;
}
const c1 = counter(), c2 = counter();
c1(); c1();
console.log(c1(), c2());
```
4. What does this log? (If it throws, name the error.)
```javascript
const r = (function (x) { return x * 2; })(21);
console.log(r);
```
5. What does this log? (If it throws, name the error.)
```javascript
const m = { v: 7, get() { return this.v; } };
const bound = m.get.bind({ v: 99 });
console.log(bound(), bound.call(m));
```
6. What does this log? (If it throws, name the error.)
```javascript
function logged(fn) {
  return function (...args) {
    const r = fn.apply(this, args);
    console.log(fn.name + '(' + args + ') = ' + r);
    return r;
  };
}
const add = logged(function add(a, b) { return a + b; });
add(2, 3);
```
7. What does this log? (If it throws, name the error.)
```javascript
console.log(Math.max.apply(null, [1, 9, 4]), Math.max.call(null, ...[1, 9, 4]));
```
8. Which return a new function rather than calling the original immediately? Choose every correct option.
   A. `fn.call(obj)`
   B. `fn.apply(obj, [])`
   C. `fn.bind(obj)`
   D. `(function () {})()`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
5 null 0
```
2. Actual result (from running it):
```
3 11 0
```
3. Actual result (from running it):
```
3 1
```
4. Actual result (from running it):
```
42
```
5. Actual result (from running it):
```
99 99
```
6. Actual result (from running it):
```
add(2,3) = 5
```
7. Actual result (from running it):
```
9 9
```
8. Correct: C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Parameters_Closures_Context_Decorators` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Generators_Iterators_and_Callbacks.
