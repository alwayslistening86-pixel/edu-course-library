# S09_Functions_Scope_and_Recursion - Practice: Functions, scope, function expressions and recursion

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
function f(a, b) {
  return a * b;
}
console.log(f(3, 4), f(3));
```
2. What does this log? (If it throws, name the error.)
```javascript
const g = function (n) { return n + 1; };
function twice(fn, v) { return fn(fn(v)); }
console.log(twice(g, 5));
```
3. What does this log? (If it throws, name the error.)
```javascript
function pow(b, e) {
  return e === 0 ? 1 : b * pow(b, e - 1);
}
console.log(pow(2, 10));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
12 NaN
```
2. Actual result (from running it):
```
7
```
3. Actual result (from running it):
```
1024
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
