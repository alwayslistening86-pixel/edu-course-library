# S05_Classes_Fields_and_Accessors - Test: Classes, instances, fields and accessors

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
class A {
  n = 10;
  constructor() { this.n += 5; }
}
console.log(new A().n);
```
2. What does this log? (If it throws, name the error.)
```javascript
try {
  new Later();
} catch (e) {
  console.log(e.name);
}
class Later {}
```
3. What does this log? (If it throws, name the error.)
```javascript
const Named = class Inner { who() { return Inner.name; } };
console.log(new Named().who(), Named.name);
```
4. What does this log? (If it throws, name the error.)
```javascript
class R {
  constructor(w, h) { this.w = w; this.h = h; }
  get area() { return this.w * this.h; }
}
const r = new R(2, 3);
r.area = 100;
console.log(r.area, Object.keys(r));
```
5. What does this log? (If it throws, name the error.)
```javascript
class S { #v = 1; getV() { return this.#v; } }
const s = new S();
console.log(s.getV(), s['#v'], Object.keys(s).length);
```
6. What does this log? (If it throws, name the error.)
```javascript
class A {}
console.log(new A() instanceof A, A.prototype.constructor === A, typeof new A());
```
7. Which are true of class declarations? Choose every correct option.
   A. The class body runs in strict mode
   B. A class can be called without new
   C. A class can be used before its declaration line
   D. Methods are placed on the prototype

## Answer key (for the tutor only)
1. Actual result (from running it):
```
15
```
2. Actual result (from running it):
```
ReferenceError
```
3. Actual result (from running it):
```
Inner Inner
```
4. Actual result (from running it):
```
6 [ 'w', 'h' ]
```
5. Actual result (from running it):
```
1 undefined 0
```
6. Actual result (from running it):
```
true true object
```
7. Correct: A, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Classes_Fields_and_Accessors` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Inheritance_Static_and_Constructors.
