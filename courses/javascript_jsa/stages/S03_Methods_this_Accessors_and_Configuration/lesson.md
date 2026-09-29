# S03_Methods_this_Accessors_and_Configuration - Lesson: Methods, this, accessors and object configuration

## Goal
The learner writes methods that use this correctly, defines getters and setters, and controls properties with descriptors, seal and freeze.

## Syllabus items taught here
- 1.7a - Functions as properties and methods in literals
- 1.7b - Adding methods to existing objects
- 1.7c - this in method calls
- 1.8a - Accessor properties with get and set
- 1.8b - Validating or computing fields with accessors
- 1.9a - Property descriptors with Object.defineProperty()
- 1.9b - Object.preventExtensions(), Object.seal(), Object.freeze()

## How to teach this
Ask what `this` is inside `obj.greet()`, and what happens if you do `const g = obj.greet; g();`. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 1.7a Functions as properties and methods in literals
A **method** is a function stored as a property. The shorthand in literals is `greet() { ... }`.
```javascript
const calc = {
  total: 0,
  add(n) { this.total += n; return this; },
  show: function () { return "total=" + this.total; }
};
console.log(calc.add(2).add(3).show());
```
Output:
```
total=5
```

#### 1.7b Adding methods to existing objects
Methods can be added to an existing object at any time by assigning a function to a property.
```javascript
const dog = { name: "Rex" };
dog.speak = function () { return this.name + " barks"; };
console.log(dog.speak());
```
Output:
```
Rex barks
```

#### 1.7c this in method calls
`this` is set by **how a function is called**: in `obj.method()` it's `obj`. A method pulled out and called on its own loses its object (`this` is `undefined` in strict code), a common bug. Arrow functions don't have their own `this`; they use the surrounding one, so an arrow is a poor choice for a method but a good choice for a callback inside one.
```javascript
"use strict";
const counter = {
  n: 0,
  inc() { this.n++; return this.n; },
  later() { [1, 2].forEach(() => this.n++); return this.n; },
  arrowMethod: () => typeof this
};
console.log(counter.inc(), counter.later(), counter.arrowMethod());
const loose = counter.inc;
try { loose(); } catch (e) { console.log(e.name); }
```
Output:
```
1 3 object
TypeError
```

#### 1.8a Accessor properties with get and set
**Accessor properties** look like data but run code: `get prop() { ... }` runs on read, and `set prop(v) { ... }` runs on assignment. A getter without a setter makes the property read-only (assignment is silently ignored, or a TypeError in strict mode).
```javascript
const temp = {
  celsius: 20,
  get fahrenheit() { return this.celsius * 9 / 5 + 32; },
  set fahrenheit(f) { this.celsius = (f - 32) * 5 / 9; }
};
console.log(temp.fahrenheit);
temp.fahrenheit = 212;
console.log(temp.celsius);
```
Output:
```
68
100
```

#### 1.8b Validating or computing fields with accessors
Setters are the natural place to **validate**; getters can **compute** derived values. Store the real value under another name (often starting with `_`) so the accessor doesn't call itself forever.
```javascript
const account = {
  _balance: 0,
  get balance() { return this._balance; },
  set balance(v) {
    if (typeof v !== "number" || v < 0) throw new RangeError("invalid balance");
    this._balance = v;
  }
};
account.balance = 50;
try { account.balance = -5; } catch (e) { console.log(e.name); }
console.log(account.balance);
```
Output:
```
RangeError
50
```

#### 1.9a Property descriptors with Object.defineProperty()
Every property has a **descriptor**: `value`, `writable`, `enumerable` and `configurable` (or `get`/`set`). `Object.defineProperty(obj, key, descriptor)` sets them; any flag you leave out defaults to **false**. `Object.getOwnPropertyDescriptor` reads them.
```javascript
"use strict";
const o = {};
Object.defineProperty(o, "id", { value: 7, enumerable: true });
Object.defineProperty(o, "secret", { value: "x" });
console.log(Object.keys(o), o.secret, Object.getOwnPropertyDescriptor(o, "id"));
try { o.id = 8; } catch (e) { console.log(e.name); }
```
Output:
```
[ 'id' ] x { value: 7, writable: false, enumerable: true, configurable: false }
TypeError
```

#### 1.9b Object.preventExtensions(), Object.seal(), Object.freeze()
`Object.preventExtensions(o)`: no new properties. `Object.seal(o)`: no new and no deleted properties, but existing ones can still change. `Object.freeze(o)`: nothing can change at all. All three are **shallow**; nested objects remain mutable. `Object.isFrozen` and its siblings test the state. Violations are silent in sloppy mode and a TypeError in strict mode.
```javascript
"use strict";
const s = Object.seal({ a: 1 });
s.a = 2;
const f = Object.freeze({ a: 1, inner: { b: 1 } });
f.inner.b = 99;
const results = [];
for (const act of [() => { s.b = 1; }, () => { delete s.a; }, () => { f.a = 5; }]) {
  try { act(); results.push("ok"); } catch (e) { results.push(e.name); }
}
console.log(s, f, results, Object.isFrozen(f), Object.isFrozen(f.inner));
```
Output:
```
{ a: 2 } { a: 1, inner: { b: 99 } } [ 'TypeError', 'TypeError', 'TypeError' ] true false
```

## Explicitly not here
Constructors and prototypes are S04.
