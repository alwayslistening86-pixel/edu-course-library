# S05_Classes_Fields_and_Accessors - Lesson: Classes, instances, fields and accessors

## Goal
The learner declares classes with constructors, fields, methods and accessors, creates instances, and uses classes as values.

## Syllabus items taught here
- 2.1a - Class declarations: constructor, fields and methods
- 2.1b - Class expressions; classes as first-class values
- 2.2a - Instantiating with new and checking with instanceof
- 2.3a - Initialising fields in the constructor or with field syntax
- 2.4a - get and set in class bodies

## How to teach this
Rewrite S04's Point constructor as a class and compare them. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 2.1a Class declarations: constructor, fields and methods
`class Name { constructor(...) { ... } method() { ... } }`. Methods go on the prototype, shared by all instances. Class bodies are always in strict mode. Unlike function declarations, classes are **not usable before their declaration**, and calling a class without `new` is a TypeError.
```javascript
class Circle {
  constructor(r) { this.r = r; }
  area() { return Math.PI * this.r ** 2; }
}
const c = new Circle(2);
console.log(c.area().toFixed(2), typeof Circle, Object.getOwnPropertyNames(Circle.prototype));
try { Circle(1); } catch (e) { console.log(e.name); }
```
Output:
```
12.57 function [ 'constructor', 'area' ]
TypeError
```

#### 2.1b Class expressions; classes as first-class values
A **class expression** assigns a class to a variable, and can be anonymous. Classes are first-class values: pass them to functions, return them, store them in arrays.
```javascript
const Animal = class { speak() { return "..."; } };
function build(Cls) { return new Cls(); }
const makeClass = greeting => class { hello() { return greeting; } };
const Hi = makeClass("hiya");
console.log(build(Animal).speak(), new Hi().hello(), Animal.name);
```
Output:
```
... hiya Animal
```

#### 2.2a Instantiating with new and checking with instanceof
`new ClassName(args)` creates an instance: the constructor runs and `this` is the new object. `obj instanceof ClassName` checks the prototype chain, so it's also true for parent classes.
```javascript
class A {}
class B extends A {}
const b = new B();
console.log(b instanceof B, b instanceof A, b instanceof Object, new A() instanceof B);
```
Output:
```
true true true false
```

#### 2.3a Initialising fields in the constructor or with field syntax
Instance fields can be created in the constructor (`this.x = ...`) or declared as **class fields** in the body (`count = 0;`), which are initialised for each new instance before the constructor body runs. A `#name` field is truly **private**: using it outside the class is a SyntaxError.
```javascript
class Counter {
  count = 0;
  #secret = 42;
  constructor(label) { this.label = label; }
  reveal() { return this.#secret; }
}
const c = new Counter("clicks");
c.count++;
console.log(c, c.reveal(), Object.keys(c));
```
Output:
```
Counter { count: 1, label: 'clicks' } 42 [ 'count', 'label' ]
```

#### 2.4a get and set in class bodies
`get` and `set` work in classes exactly as in object literals, and are defined on the prototype. They combine well with private fields for validated state.
```javascript
class Temperature {
  #c = 0;
  get celsius() { return this.#c; }
  set celsius(v) { if (v < -273.15) throw new RangeError("below absolute zero"); this.#c = v; }
  get fahrenheit() { return this.#c * 9 / 5 + 32; }
}
const t = new Temperature();
t.celsius = 100;
console.log(t.celsius, t.fahrenheit);
try { t.celsius = -300; } catch (e) { console.log(e.name, t.celsius); }
```
Output:
```
100 212
RangeError 100
```

## Explicitly not here
extends and static are S06.
