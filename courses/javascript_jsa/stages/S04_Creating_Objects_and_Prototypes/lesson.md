# S04_Creating_Objects_and_Prototypes - Lesson: Factories, constructors, Object.create and prototypes

## Goal
The learner creates objects with factories, constructor functions and Object.create, and explains and manipulates the prototype chain.

## Syllabus items taught here
- 1.10a - Factory functions
- 1.10b - Constructor functions with new
- 1.10c - Object.create() with an explicit prototype
- 1.11a - Prototype-based inheritance links
- 1.11b - __proto__, [[Prototype]] and Function.prototype
- 1.11c - Object.setPrototypeOf()

## How to teach this
Ask where `toString` comes from on an object that never defined it. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 1.10a Factory functions
A **factory function** is an ordinary function that builds and returns a new object, and needs no `new`. It can keep private data in a closure.
```javascript
function makeCounter(start = 0) {
  let count = start;
  return { inc() { return ++count; }, get value() { return count; } };
}
const c = makeCounter(5);
c.inc(); c.inc();
console.log(c.value, c.count);
```
Output:
```
7 undefined
```

#### 1.10b Constructor functions with new
A **constructor function** is called with `new`: a fresh object is created, linked to `Fn.prototype`, bound to `this`, and returned automatically. Shared methods go on `Fn.prototype`, so every instance shares one copy. By convention the name is capitalised.
```javascript
function Point(x, y) { this.x = x; this.y = y; }
Point.prototype.len = function () { return Math.hypot(this.x, this.y); };
const p = new Point(3, 4);
console.log(p.len(), p instanceof Point, Object.getPrototypeOf(p) === Point.prototype, Object.keys(p));
```
Output:
```
5 true true [ 'x', 'y' ]
```

#### 1.10c Object.create() with an explicit prototype
`Object.create(proto)` makes a new object whose prototype is `proto`, with no constructor involved. `Object.create(null)` makes an object with no prototype at all, which is useful as a pure dictionary.
```javascript
const animal = { speak() { return this.name + " makes a sound"; } };
const cat = Object.create(animal);
cat.name = "Tom";
const bare = Object.create(null);
console.log(cat.speak(), Object.getPrototypeOf(cat) === animal, "toString" in bare);
```
Output:
```
Tom makes a sound true false
```

#### 1.11a Prototype-based inheritance links
Every object has an internal link to another object, its **prototype**. When a property isn't found on the object, lookup continues along this chain until it reaches `null`. That's JavaScript's inheritance: objects inherit from objects. Writing a property always writes to the object itself, which shadows the prototype's version.
```javascript
const base = { greet() { return "hi from base"; }, x: 1 };
const child = Object.create(base);
child.x = 2;
console.log(child.greet(), child.x, base.x, Object.getPrototypeOf(Object.getPrototypeOf(child)) === Object.prototype);
```
Output:
```
hi from base 2 1 true
```

#### 1.11b __proto__, [[Prototype]] and Function.prototype
`[[Prototype]]` is the internal link; `obj.__proto__` is an old accessor for it (use `Object.getPrototypeOf` instead). Every function has a `prototype` property: the object that `new Fn()` instances link to. Functions themselves inherit from `Function.prototype`, which is where `call`, `apply` and `bind` come from.
```javascript
function F() {}
const o = new F();
console.log(o.__proto__ === F.prototype, Object.getPrototypeOf(F) === Function.prototype, typeof F.prototype, "call" in F);
```
Output:
```
true true object true
```

#### 1.11c Object.setPrototypeOf()
`Object.setPrototypeOf(obj, proto)` changes an existing object's prototype. It works, but it's slow and rarely needed; prefer `Object.create` when building the object.
```javascript
const walker = { move() { return "walk"; } };
const swimmer = { move() { return "swim"; } };
const duck = Object.create(walker);
console.log(duck.move());
Object.setPrototypeOf(duck, swimmer);
console.log(duck.move());
```
Output:
```
walk
swim
```

## Explicitly not here
Class syntax is S05 and S06.
