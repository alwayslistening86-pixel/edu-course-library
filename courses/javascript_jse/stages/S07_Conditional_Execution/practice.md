# S07_Conditional_Execution - Practice: if and switch

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const v = '5';
switch (v) {
  case 5: console.log('number'); break;
  case '5': console.log('string'); break;
  default: console.log('none');
}
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = 4, b = 9;
if (a > 5 || b > 5) {
  if (a > 5) console.log('a');
  else console.log('b');
}
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
string
```
2. Actual result (from running it):
```
b
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
