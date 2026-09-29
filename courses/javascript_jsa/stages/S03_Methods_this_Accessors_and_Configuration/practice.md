# S03_Methods_this_Accessors_and_Configuration - Practice: Methods, this, accessors and object configuration

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const o = {
  v: 2,
  get double() { return this.v * 2; }
};
o.double = 100;
console.log(o.double);
```
2. What does this log? (If it throws, name the error.)
```javascript
'use strict';
const f = Object.freeze({ a: 1 });
try {
  f.a = 2;
} catch (e) {
  console.log(e.name);
}
console.log(f.a);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
4
```
2. Actual result (from running it):
```
TypeError
1
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
