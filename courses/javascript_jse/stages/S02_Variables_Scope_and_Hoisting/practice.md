# S02_Variables_Scope_and_Hoisting - Practice: Variables, scope and hoisting

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
let a = 1;
{
  let a = 2;
  console.log(a);
}
console.log(a);
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log(v);
var v = 'set';
console.log(v);
```
3. Which are valid variable names? Choose every correct option.
   A. `$total`
   B. `_x1`
   C. `2nd`
   D. `first-name`
   E. `camelCase`

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
2
1
```
2. Actual result (from running it):
```
undefined
set
```
3. Correct: A, B, E (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
