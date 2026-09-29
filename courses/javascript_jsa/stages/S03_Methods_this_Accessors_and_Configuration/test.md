# S03_Methods_this_Accessors_and_Configuration - Test: Methods, this, accessors and object configuration

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const bank = {
  total: 0,
  add(n) {
    this.total += n;
    return this;
  }
};
console.log(bank.add(5).add(10).total);
```
2. What does this log? (If it throws, name the error.)
```javascript
'use strict';
const o = { n: 1, get() { return this; } };
const g = o.get;
console.log(o.get() === o, g());
```
3. What does this log? (If it throws, name the error.)
```javascript
const o = {
  items: [1, 2],
  sum() {
    let s = 0;
    this.items.forEach(x => { s += x * this.items.length; });
    return s;
  }
};
console.log(o.sum());
```
4. What does this log? (If it throws, name the error.)
```javascript
const u = {
  _age: 0,
  set age(v) { this._age = Math.max(0, v); },
  get age() { return this._age; }
};
u.age = -5;
console.log(u.age);
```
5. What does this log? (If it throws, name the error.)
```javascript
const o = {};
Object.defineProperty(o, 'hidden', { value: 1 });
o.visible = 2;
console.log(Object.keys(o), o.hidden, JSON.stringify(o));
```
6. What does this log? (If it throws, name the error.)
```javascript
'use strict';
const s = Object.seal({ a: 1 });
s.a = 2;
let r;
try {
  s.b = 3;
  r = 'added';
} catch (e) {
  r = e.name;
}
console.log(s, r, Object.isSealed(s));
```
7. After Object.freeze(obj), which are still possible (without error in sloppy mode having any effect)? Choose every correct option.
   A. Changing obj.nested.value where nested is an object
   B. Adding obj.newProp
   C. Changing obj.topLevel
   D. Reading obj.topLevel

## Answer key (for the tutor only)
1. Actual result (from running it):
```
15
```
2. Actual result (from running it):
```
true undefined
```
3. Actual result (from running it):
```
6
```
4. Actual result (from running it):
```
0
```
5. Actual result (from running it):
```
[ 'visible' ] 1 {"visible":2}
```
6. Actual result (from running it):
```
{ a: 2 } TypeError true
```
7. Correct: A, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Methods_this_Accessors_and_Configuration` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Creating_Objects_and_Prototypes.
