# S11_Parameters_Closures_Context_Decorators - Practice: Parameters, closures, IIFEs, call/apply/bind and decorators

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
function f(a, b = a * 2, ...rest) { return [a, b, rest]; }
console.log(f(1), f(1, 5, 6, 7));
```
2. What does this log? (If it throws, name the error.)
```javascript
const o = { x: 3 };
function show(m) { return this.x * m; }
console.log(show.call(o, 2), show.apply(o, [3]), show.bind(o)(4));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
[ 1, 2, [] ] [ 1, 5, [ 6, 7 ] ]
```
2. Actual result (from running it):
```
6 9 12
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
