# S08_Arrays_and_Array_Methods - Practice: Arrays and advanced array methods

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const a = [1, 2, 3, 4];
console.log(a.map(x => x * 2).filter(x => x > 4), a.reduce((s, x) => s + x));
```
2. What does this log? (If it throws, name the error.)
```javascript
const [x, [y, z] = [0, 0], ...rest] = [1, undefined, 3, 4];
console.log(x, y, z, rest);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
[ 6, 8 ] 10
```
2. Actual result (from running it):
```
1 0 0 [ 3, 4 ]
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
