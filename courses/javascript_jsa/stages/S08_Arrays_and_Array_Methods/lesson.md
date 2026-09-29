# S08_Arrays_and_Array_Methods - Lesson: Arrays and advanced array methods

## Goal
The learner creates, merges and edits arrays with splice, spread and destructuring, and uses the higher-order array methods fluently.

## Syllabus items taught here
- 3.4a - Arrays: creating, merging, adding and removing, slice and splice, spread and destructuring
- 3.5a - find, every, some, filter, sort, map and reduce

## How to teach this
Ask for the total price of a basket array of objects in one expression. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 3.4a Arrays: creating, merging, adding and removing, slice and splice, spread and destructuring
Create with literals, `Array.from(iterable or {length})` or `Array.of`. Merge with `concat` or spread `[...a, ...b]`. `splice(start, deleteCount, ...items)` edits **in place** and returns the removed items, while `slice` copies. **Destructuring** unpacks: `const [first, , third, ...rest] = arr`, including defaults and swaps.
```javascript
const a = [1, 2, 3], b = [4, 5];
const merged = [...a, ...b];
const removed = merged.splice(1, 2, "x", "y", "z");
const [first, , third = "d", ...rest] = merged;
let p = 1, q = 2;
[p, q] = [q, p];
console.log(merged, removed, first, third, rest, Array.from({ length: 3 }, (_, i) => i * i), p, q);
```
Output:
```
[ 1, 'x', 'y', 'z', 4, 5 ] [ 2, 3 ] 1 y [ 'z', 4, 5 ] [ 0, 1, 4 ] 2 1
```

#### 3.5a find, every, some, filter, sort, map and reduce
Higher-order methods, each taking a callback `(element, index, array)`. `map` builds a new array of results; `filter` keeps the elements for which the callback is truthy; `find` gives the first match (or undefined); `some` and `every` test for any or all; `reduce(fn, initial)` folds everything into one value. `sort` sorts **in place** and, by default, compares **as strings**, so give numbers a comparator.
```javascript
const basket = [{ item: "pen", price: 2, qty: 3 }, { item: "pad", price: 5, qty: 1 }, { item: "ink", price: 8, qty: 2 }];
console.log(basket.map(b => b.item), basket.filter(b => b.price > 4).length, basket.find(b => b.qty === 1).item);
console.log(basket.some(b => b.price > 7), basket.every(b => b.qty > 0), basket.reduce((sum, b) => sum + b.price * b.qty, 0));
const nums = [10, 9, 1, 100];
console.log([...nums].sort(), [...nums].sort((x, y) => x - y), nums);
```
Output:
```
[ 'pen', 'pad', 'ink' ] 2 pad
true true 27
[ 1, 10, 100, 9 ] [ 1, 9, 10, 100 ] [ 10, 9, 1, 100 ]
```

## Explicitly not here
Set and Map are S09.
