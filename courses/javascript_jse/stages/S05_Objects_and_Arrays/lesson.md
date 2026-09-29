# S05_Objects_and_Arrays - Lesson: Objects and arrays

## Goal
The learner uses objects as records and arrays as lists, predicting the result of every syllabus array method.

## Syllabus items taught here
- 2.5a - Objects as records: literals, getting and setting properties
- 2.6a - Arrays: length, indexOf, push, unshift, pop, shift
- 2.6b - Arrays: reverse, slice, concat

## How to teach this
Ask what `[1, 2, 3].push(4)` returns (the new length, not the array). Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 2.5a Objects as records: literals, getting and setting properties
An **object** groups named properties: `{ name: "Ann", age: 30 }`. Read or write with a dot (`o.name`) or brackets (`o["name"]`, needed for keys held in variables or containing spaces). Assigning to a new name adds a property. Reading a missing property gives `undefined`, not an error; reading a property *of* `undefined` is a TypeError.
```javascript
const p = { name: "Ann", age: 30 };
p.age += 1; p.city = "Leeds";
const key = "name";
console.log(p[key], p.age, p.city, p.phone, p);
try { console.log(p.phone.number); } catch (e) { console.log(e.name); }
```
Output:
```
Ann 31 Leeds undefined { name: 'Ann', age: 31, city: 'Leeds' }
TypeError
```

#### 2.6a Arrays: length, indexOf, push, unshift, pop, shift
Arrays are ordered, zero-indexed and can hold mixed types. `length` is one more than the highest index. `indexOf(x)` gives the first position or -1. `push` and `unshift` add at the end or start, and **return the new length**. `pop` and `shift` remove from the end or start, and **return the removed item**.
```javascript
const a = [10, 20];
console.log(a.push(30), a.unshift(5), a, a.pop(), a.shift(), a, a.indexOf(20), a.indexOf(99), a.length);
```
Output:
```
3 4 [ 10, 20 ] 30 5 [ 10, 20 ] 1 -1 2
```

#### 2.6b Arrays: reverse, slice, concat
`reverse()` reverses **in place** and returns the same array. `slice(start, end)` returns a new array and leaves the original alone. `concat(...)` returns a new, joined array.
```javascript
const a = [1, 2, 3];
const b = a.slice(1);
const c = a.concat([4, 5], 6);
const r = a.reverse();
console.log(a, b, c, r === a);
```
Output:
```
[ 3, 2, 1 ] [ 2, 3 ] [ 1, 2, 3, 4, 5, 6 ] true
```

## Explicitly not here
Advanced array methods (map, filter, reduce) belong to JSA, not JSE.
