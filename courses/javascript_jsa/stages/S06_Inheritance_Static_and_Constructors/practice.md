# S06_Inheritance_Static_and_Constructors - Practice: Inheritance, static members, and classes versus constructors

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
class A { hi() { return 'A'; } }
class B extends A { hi() { return 'B>' + super.hi(); } }
console.log(new B().hi());
```
2. What does this log? (If it throws, name the error.)
```javascript
class U { static count = 0; constructor() { U.count++; } }
new U(); new U();
console.log(U.count, new U().count);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
B>A
```
2. Actual result (from running it):
```
2 undefined
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
