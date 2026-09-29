# S06_Inheritance_Static_and_Constructors - Test: Inheritance, static members, and classes versus constructors

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
class Animal {
  constructor(n) { this.n = n; }
  speak() { return this.n + ' makes a sound'; }
}
class Dog extends Animal {
  speak() { return this.n + ' barks'; }
}
console.log(new Dog('Rex').speak(), new Animal('Cat').speak());
```
2. What does this log? (If it throws, name the error.)
```javascript
class A { constructor() { this.tag = 'A'; } }
class B extends A { constructor() { super(); this.tag += 'B'; } }
class C extends B {}
console.log(new C().tag);
```
3. What does this log? (If it throws, name the error.)
```javascript
class A {}
class B extends A { constructor() { console.log('before'); } }
try {
  new B();
} catch (e) {
  console.log(e.name);
}
```
4. What does this log? (If it throws, name the error.)
```javascript
class MathX { static sq(n) { return n * n; } }
class MathY extends MathX {}
console.log(MathY.sq(4), typeof new MathX().sq);
```
5. What does this log? (If it throws, name the error.)
```javascript
class K { m() {} }
function F() {}
F.prototype.m = function () {};
console.log(Object.keys(K.prototype).length, Object.keys(F.prototype).length);
```
6. What does this log? (If it throws, name the error.)
```javascript
class A { static make() { return new this(); } }
class B extends A {}
console.log(B.make() instanceof B, A.make() instanceof B);
```
7. Which are true? Choose every correct option.
   A. A subclass constructor must call super() before using this
   B. static methods are called on instances
   C. super.method() calls the parent's version of a method
   D. extends works only with other classes, never constructor functions

## Answer key (for the tutor only)
1. Actual result (from running it):
```
Rex barks Cat makes a sound
```
2. Actual result (from running it):
```
AB
```
3. Actual result (from running it):
```
before
ReferenceError
```
4. Actual result (from running it):
```
16 undefined
```
5. Actual result (from running it):
```
0 1
```
6. Actual result (from running it):
```
true false
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Inheritance_Static_and_Constructors` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Number_String_and_Date.
