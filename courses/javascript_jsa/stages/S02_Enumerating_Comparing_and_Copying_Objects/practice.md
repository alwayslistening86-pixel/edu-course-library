# S02_Enumerating_Comparing_and_Copying_Objects - Practice: Enumerating, comparing and copying objects

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const o = { a: 1, b: 2 };
console.log(Object.entries(o).map(([k, v]) => k + v).join());
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = { v: [1] };
const b = { ...a };
b.v.push(2);
console.log(a.v, a === b, a.v === b.v);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
a1,b2
```
2. Actual result (from running it):
```
[ 1, 2 ] false true
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
