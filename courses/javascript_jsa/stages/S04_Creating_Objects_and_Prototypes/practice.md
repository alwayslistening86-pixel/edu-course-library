# S04_Creating_Objects_and_Prototypes - Practice: Factories, constructors, Object.create and prototypes

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
function Dog(n) { this.n = n; }
Dog.prototype.bark = function () { return this.n + '!'; };
const d = new Dog('Rex');
console.log(d.bark(), Object.hasOwn(d, 'bark'));
```
2. What does this log? (If it throws, name the error.)
```javascript
const proto = { hi() { return 'hi ' + this.who; } };
const o = Object.create(proto, { who: { value: 'you', enumerable: true } });
console.log(o.hi(), Object.keys(o));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
Rex! false
```
2. Actual result (from running it):
```
hi you [ 'who' ]
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
