# S10_Math_RegExp_and_Extending_Builtins - Practice: Math, regular expressions and extending built-ins

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(Math.round(1.5), Math.round(-1.5), Math.trunc(-4.7), Math.sign(-3));
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log(/cat/i.test('Concatenate'), 'a.b.c'.split(/\./), 'x1y2'.replace(/\d/g, '#'));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
2 -1 -4 -1
```
2. Actual result (from running it):
```
true [ 'a', 'b', 'c' ] x#y#
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
