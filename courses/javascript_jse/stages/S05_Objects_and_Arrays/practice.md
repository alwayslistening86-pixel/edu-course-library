# S05_Objects_and_Arrays - Practice: Objects and arrays

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const o = { a: 1 };
o.b = 2;
o['c d'] = 3;
console.log(o, o.z);
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = [1, 2, 3];
console.log(a.pop(), a.unshift(0), a);
```
3. What does this log? (If it throws, name the error.)
```javascript
const a = ['x', 'y', 'z'];
console.log(a.slice(1), a.indexOf('z'), a.concat(['w']).length, a.length);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
{ a: 1, b: 2, 'c d': 3 } undefined
```
2. Actual result (from running it):
```
3 3 [ 0, 1, 2 ]
```
3. Actual result (from running it):
```
[ 'y', 'z' ] 2 4 3
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
