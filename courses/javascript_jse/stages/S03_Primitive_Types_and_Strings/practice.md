# S03_Primitive_Types_and_Strings - Practice: Primitive types and strings

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(typeof 5n, 10n / 3n, 7 / 2, Number.isInteger(5.0));
```
2. What does this log? (If it throws, name the error.)
```javascript
const s = 'Hello';
console.log(s.length, s.charAt(1), s.slice(1, 3), s.split('l'));
```
3. What does this log? (If it throws, name the error.)
```javascript
const n = 4;
console.log(`${n} squared is ${n * n}`);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
bigint 3n 3.5 true
```
2. Actual result (from running it):
```
5 e el [ 'He', '', 'o' ]
```
3. Actual result (from running it):
```
4 squared is 16
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
