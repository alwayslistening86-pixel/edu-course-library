# S08_Loops - Lesson: Loops: while, do-while, for, for-in and for-of

## Goal
The learner chooses and writes the right loop for each task, and predicts the effect of break and continue and the difference between for...in and for...of.

## Syllabus items taught here
- 4.3a - while and do...while loops
- 4.3b - break and continue
- 4.4a - for loops over ranges and collections
- 4.5a - for...in over enumerable properties, and its caveats
- 4.6a - for...of over arrays and other iterables

## How to teach this
Ask what for...in and for...of each give when looping over ['a', 'b']. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 4.3a while and do...while loops
`while (cond) { ... }` tests before each pass, so it may run zero times. `do { ... } while (cond);` tests afterwards, so it always runs at least once.
```javascript
let n = 0;
while (n > 0) { console.log("never"); }
do { console.log("do-while ran once, n =", n); } while (n > 0);
let k = 1;
while (k < 100) { k *= 3; }
console.log(k);
```
Output:
```
do-while ran once, n = 0
243
```

#### 4.3b break and continue
`break` leaves the innermost loop (or switch) immediately; `continue` skips to the next pass. A label (`outer:`) lets `break outer` leave several nested loops at once.
```javascript
for (let i = 0; i < 6; i++) {
  if (i === 1) continue;
  if (i === 4) break;
  console.log(i);
}
outer: for (let a = 0; a < 3; a++) {
  for (let b = 0; b < 3; b++) {
    if (b === 1) continue outer;
    if (a === 2) break outer;
    console.log(a, b);
  }
}
```
Output:
```
0
2
3
0 0
1 0
```

#### 4.4a for loops over ranges and collections
`for (init; condition; update)` is the counting loop, often used to walk an array by index.
```javascript
const nums = [3, 8, 1];
let total = 0;
for (let i = 0; i < nums.length; i++) { total += nums[i]; }
for (let i = 10; i > 0; i -= 4) { console.log(i); }
console.log(total);
```
Output:
```
10
6
2
12
```

#### 4.5a for...in over enumerable properties, and its caveats
`for (const key in obj)` visits enumerable property **names** (strings), including inherited enumerable ones. On arrays it gives the indices as strings and may include extra properties, so don't use it for arrays; use `for...of` or a counting loop.
```javascript
const car = { make: "VW", year: 2020 };
for (const k in car) { console.log(k, car[k]); }
const arr = ["x", "y"];
for (const i in arr) { console.log(typeof i, i); }
```
Output:
```
make VW
year 2020
string 0
string 1
```

#### 4.6a for...of over arrays and other iterables
`for (const v of iterable)` visits **values**: array elements, string characters, and the entries of Maps and Sets. Plain objects are *not* iterable (TypeError); loop over `Object.keys(o)` or `Object.entries(o)` instead.
```javascript
for (const v of ["x", "y"]) console.log(v);
for (const ch of "hi") console.log(ch);
try { for (const v of { a: 1 }) {} } catch (e) { console.log(e.name); }
```
Output:
```
x
y
h
i
TypeError
```

## Explicitly not here
Functions are S09.
