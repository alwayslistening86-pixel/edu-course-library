# S10_Callbacks_Timers_and_Arrow_Functions - Practice: Callbacks, timers and arrow functions

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const f = x => x * 3;
const g = () => ({ ok: true });
console.log(f(2), g());
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
console.log('C');
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
6 { ok: true }
```
2. Actual result (from running it):
```
A
C
B
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
