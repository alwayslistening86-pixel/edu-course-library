# S09_Functions_Scope_and_Recursion - Lesson: Functions, scope, function expressions and recursion

## Goal
The learner declares and calls functions, predicts return values and scope effects, treats functions as values, and writes simple recursion.

## Syllabus items taught here
- 5.1a - Declaring and calling functions; arguments and return
- 5.2a - Parameters, local variables and shadowing
- 5.3a - Function expressions and functions as values
- 5.4a - Recursion

## How to teach this
Ask what a function with no return statement gives back. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 5.1a Declaring and calling functions; arguments and return
`function name(params) { ... }` declares a function; `name(args)` calls it. `return` ends the function and gives a value; with no return, the result is `undefined`. Missing arguments are `undefined`, and extra arguments are ignored. Function **declarations** are hoisted, so they can be called before the line that defines them.
```javascript
console.log(add(2, 3));
function add(a, b) { return a + b; }
function nothing() {}
console.log(nothing(), add(1), add(1, 2, 3));
```
Output:
```
5
undefined NaN 3
```

#### 5.2a Parameters, local variables and shadowing
Parameters and variables declared inside a function are **local** to it. A local variable with the same name as an outer one **shadows** it. A function can read outer variables, and can change them if it assigns without declaring (don't rely on that).
```javascript
let x = "global";
function f(x) { x = x + "!"; return x; }
function g() { let x = "local"; return x; }
function h() { x = "changed"; }
console.log(f("param"), g(), x);
h();
console.log(x);
```
Output:
```
param! local global
changed
```

#### 5.3a Function expressions and functions as values
Functions are values. A **function expression** assigns one to a variable (`const sq = function (n) { return n * n; };`). It can be anonymous or named, and unlike a declaration it isn't usable before its line. Functions can be passed as arguments and returned from other functions.
```javascript
const sq = function (n) { return n * n; };
const fact = function f(n) { return n <= 1 ? 1 : n * f(n - 1); };
function applyTo(fn, v) { return fn(v); }
console.log(sq(4), fact(5), applyTo(sq, 3), typeof sq);
```
Output:
```
16 120 9 function
```

#### 5.4a Recursion
A **recursive** function calls itself, with a base case that stops it. Too-deep recursion throws a RangeError (maximum call stack size exceeded).
```javascript
function sumTo(n) { return n === 0 ? 0 : n + sumTo(n - 1); }
function forever(n) { return forever(n + 1); }
console.log(sumTo(100));
try { forever(0); } catch (e) { console.log(e.name); }
```
Output:
```
5050
RangeError
```

## Explicitly not here
Callbacks, timers and arrow functions are S10.
