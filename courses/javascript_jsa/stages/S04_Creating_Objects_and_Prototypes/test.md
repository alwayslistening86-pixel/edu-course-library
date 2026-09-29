# S04_Creating_Objects_and_Prototypes - Test: Factories, constructors, Object.create and prototypes

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
function makePoint(x, y) {
  return { x, y, move(dx) { this.x += dx; return this; } };
}
console.log(makePoint(1, 2).move(3).x);
```
2. What does this log? (If it throws, name the error.)
```javascript
function Car(make) { this.make = make; }
Car.prototype.wheels = 4;
const a = new Car('VW'), b = new Car('Kia');
b.wheels = 3;
console.log(a.wheels, b.wheels, Car.prototype.wheels);
```
3. What does this log? (If it throws, name the error.)
```javascript
const a = { x: 1 };
const b = Object.create(a);
const c = Object.create(b);
console.log(c.x, Object.getPrototypeOf(c) === b, a.isPrototypeOf(c));
```
4. What does this log? (If it throws, name the error.)
```javascript
function F() {}
const f = new F();
console.log(f.__proto__ === F.prototype, F.prototype.constructor === F, f.constructor.name);
```
5. What does this log? (If it throws, name the error.)
```javascript
const o = Object.create(null);
o.k = 1;
console.log(typeof o.toString, Object.keys(o));
```
6. What does this log? (If it throws, name the error.)
```javascript
const loud = { say() { return 'LOUD'; } };
const quiet = { say() { return 'quiet'; } };
const p = Object.create(quiet);
Object.setPrototypeOf(p, loud);
console.log(p.say());
```
7. Which create an object whose prototype is proto? Choose every correct option.
   A. `Object.create(proto)`
   B. `Object.setPrototypeOf({}, proto)`
   C. `{ ...proto }`
   D. `Object.assign({}, proto)`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
4
```
2. Actual result (from running it):
```
4 3 4
```
3. Actual result (from running it):
```
1 true true
```
4. Actual result (from running it):
```
true true F
```
5. Actual result (from running it):
```
undefined [ 'k' ]
```
6. Actual result (from running it):
```
LOUD
```
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Creating_Objects_and_Prototypes` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Classes_Fields_and_Accessors.
