# S06_Operators_and_User_Interaction - Practice: Operators and user interaction

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
let i = 1;
console.log(i++ + ++i, i);
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log('' || 'x', 0 && 'y', null ?? 'z', 1 < 2 < 3, 3 > 2 > 1);
```
3. What does this log? (If it throws, name the error.)
```javascript
console.log(typeof typeof 1, [] instanceof Array);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
4 3
```
2. Actual result (from running it):
```
x 0 z true false
```
3. Actual result (from running it):
```
string true
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
