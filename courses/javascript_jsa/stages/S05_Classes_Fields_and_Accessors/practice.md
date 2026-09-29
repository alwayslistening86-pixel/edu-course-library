# S05_Classes_Fields_and_Accessors - Practice: Classes, instances, fields and accessors

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
class P {
  constructor(n) { this.n = n; }
  hi() { return 'hi ' + this.n; }
}
console.log(new P('Bo').hi(), typeof P);
```
2. What does this log? (If it throws, name the error.)
```javascript
class C {
  #x = 1;
  static has(o) { return #x in o; }
}
console.log(C.has(new C()), C.has({}));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
hi Bo function
```
2. Actual result (from running it):
```
true false
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
