# S02_Enumerating_Comparing_and_Copying_Objects - Lesson: Enumerating, comparing and copying objects

## Goal
The learner tests for properties, enumerates own properties, compares objects correctly, and copies them without accidental sharing.

## Syllabus items taught here
- 1.4a - Testing existence with in and safe access
- 1.4b - for...in over own properties (with filtering)
- 1.4c - Object.keys(), Object.values(), Object.entries()
- 1.5a - Reference equality versus deep structural comparison
- 1.5b - Identity versus value equivalence
- 1.6a - Copying a reference versus cloning a value
- 1.6b - Shallow clones with Object.assign() and spread
- 1.6c - Deep cloning strategies and caveats

## How to teach this
Ask whether `{a: 1} === {a: 1}` is true, and why. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 1.4a Testing existence with in and safe access
`"key" in obj` is true if the property exists on the object **or its prototype chain**, even when its value is `undefined`. `Object.hasOwn(obj, "key")` (or `obj.hasOwnProperty`) checks own properties only. Comparing with `undefined` can't tell "missing" from "set to undefined".
```javascript
const o = { a: undefined };
console.log("a" in o, o.a === undefined, "b" in o, "toString" in o, Object.hasOwn(o, "toString"));
```
Output:
```
true true false true false
```

#### 1.4b for...in over own properties (with filtering)
`for...in` visits enumerable keys, **including inherited ones**, so filter with `Object.hasOwn` when you only want the object's own.
```javascript
const base = { inherited: 1 };
const o = Object.create(base);
o.own = 2;
for (const k in o) console.log("for-in:", k);
for (const k in o) if (Object.hasOwn(o, k)) console.log("own only:", k);
```
Output:
```
for-in: own
for-in: inherited
own only: own
```

#### 1.4c Object.keys(), Object.values(), Object.entries()
`Object.keys(o)`, `Object.values(o)` and `Object.entries(o)` return arrays of the **own** enumerable keys, values and [key, value] pairs, ready for `for...of` and array methods.
```javascript
const scores = { ann: 7, bo: 9 };
console.log(Object.keys(scores), Object.values(scores), Object.entries(scores));
for (const [k, v] of Object.entries(scores)) console.log(k, v * 10);
```
Output:
```
[ 'ann', 'bo' ] [ 7, 9 ] [ [ 'ann', 7 ], [ 'bo', 9 ] ]
ann 70
bo 90
```

#### 1.5a Reference equality versus deep structural comparison
`===` and `==` on objects compare **references**: true only if both are the same object. Two separately created objects with identical contents aren't equal. Structural comparison needs your own code (compare keys and values, recursing for nested objects) or a library.
```javascript
const a = { x: 1 }, b = { x: 1 }, c = a;
function shallowEqual(p, q) {
  const kp = Object.keys(p), kq = Object.keys(q);
  return kp.length === kq.length && kp.every(k => p[k] === q[k]);
}
console.log(a === b, a === c, shallowEqual(a, b));
```
Output:
```
false true true
```

#### 1.5b Identity versus value equivalence
**Identity** means "the very same object"; **value equivalence** means "same contents". Primitives compare by value; objects by identity. So choose deliberately: are you asking whether it's the same object, or an equal one?

#### 1.6a Copying a reference versus cloning a value
Assigning an object to another variable copies the **reference**, so both names see the same changes. A **clone** is a new object holding the same values.
```javascript
const orig = { n: 1 };
const alias = orig;
alias.n = 99;
console.log(orig.n);
```
Output:
```
99
```

#### 1.6b Shallow clones with Object.assign() and spread
`Object.assign({}, src)` and spread `{ ...src }` make **shallow** clones: top-level properties are copied, but nested objects are still shared. Later sources override earlier ones.
```javascript
const src = { a: 1, inner: { b: 2 } };
const c1 = { ...src };
const c2 = Object.assign({}, src, { a: 5 });
c1.a = 10;
c1.inner.b = 20;
console.log(src.a, src.inner.b, c2.a, c2.inner === src.inner);
```
Output:
```
1 20 5 true
```

#### 1.6c Deep cloning strategies and caveats
**Deep cloning** copies nested objects too. `structuredClone(obj)` is the built-in way (it handles Dates, Maps, Sets and cycles, but not functions). `JSON.parse(JSON.stringify(obj))` works only for JSON-safe data: functions and `undefined` are lost, and Dates become strings. A hand-written recursive copy gives full control.
```javascript
const src = { d: new Date(0), inner: { b: 2 }, f() {} };
const s = structuredClone({ d: src.d, inner: src.inner });
s.inner.b = 99;
const j = JSON.parse(JSON.stringify(src));
console.log(src.inner.b, s.d instanceof Date, typeof j.d, "f" in j);
```
Output:
```
2 true string false
```

## Explicitly not here
Methods and this are S03.
