# S06_Inheritance_Static_and_Constructors - Lesson: Inheritance, static members, and classes versus constructors

## Goal
The learner builds class hierarchies with extends and super, uses static members, and explains the prototype machinery behind class syntax.

## Syllabus items taught here
- 2.5a - extends and overriding members
- 2.5b - super in constructors and methods
- 2.6a - static methods and properties
- 2.7a - Class syntax related to constructor functions and prototype methods

## How to teach this
Ask what happens if a subclass constructor uses this before calling super(). Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 2.5a extends and overriding members
`class Child extends Parent` sets up the prototype chain. A method with the same name in the child **overrides** the parent's. Instances of Child inherit every Parent method they don't override.
```javascript
class Shape { describe() { return "a shape with area " + this.area(); } area() { return 0; } }
class Square extends Shape { constructor(s) { super(); this.s = s; } area() { return this.s ** 2; } }
console.log(new Square(3).describe(), new Shape().describe());
```
Output:
```
a shape with area 9 a shape with area 0
```

#### 2.5b super in constructors and methods
In a subclass constructor, `super(args)` calls the parent constructor, and **must** be called before `this` is used (otherwise a ReferenceError). In methods, `super.method()` calls the parent's version.
```javascript
class Employee {
  constructor(name) { this.name = name; }
  pay() { return 1000; }
}
class Manager extends Employee {
  constructor(name, bonus) { super(name); this.bonus = bonus; }
  pay() { return super.pay() + this.bonus; }
}
class Broken extends Employee { constructor() { this.x = 1; super("x"); } }
console.log(new Manager("Ann", 500).pay());
try { new Broken(); } catch (e) { console.log(e.name); }
```
Output:
```
1500
ReferenceError
```

#### 2.6a static methods and properties
`static` members belong to the **class itself**, not to instances: utility methods, constants and factories. Call them as `ClassName.member`; they're inherited by subclasses. Inside a static method, `this` is the class.
```javascript
class Temp {
  static ABS_ZERO = -273.15;
  static fromF(f) { return new this((f - 32) * 5 / 9); }
  constructor(c) { this.c = c; }
}
class Temp2 extends Temp {}
const t = Temp2.fromF(212);
console.log(Temp.ABS_ZERO, t.c, t instanceof Temp2, t.ABS_ZERO, typeof t.fromF);
```
Output:
```
-273.15 100 true undefined undefined
```

#### 2.7a Class syntax related to constructor functions and prototype methods
Classes are mostly cleaner syntax over constructor functions: `class A { m() {} }` makes a function `A`, with `m` on `A.prototype`. The differences: a class can't be called without `new`; its body is strict; its methods are non-enumerable; and it isn't hoisted for use.
```javascript
class C { m() { return "m"; } }
function F() {}
F.prototype.m = function () { return "m"; };
console.log(typeof C, typeof C.prototype.m, Object.keys(C.prototype), Object.keys(F.prototype), new C().m() === new F().m());
```
Output:
```
function function [] [ 'm' ] true
```

## Explicitly not here
Built-in objects are S07 to S10.
