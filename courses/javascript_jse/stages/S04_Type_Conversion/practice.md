# S04_Type_Conversion - Practice: Type conversion

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(Number('12'), Number('12a'), Number(' 7 '), Number(false));
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log('3' + 4, '3' - 4, '3' * '4', 4 + 4 + '4');
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
12 NaN 7 0
```
2. Actual result (from running it):
```
34 -1 12 84
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
