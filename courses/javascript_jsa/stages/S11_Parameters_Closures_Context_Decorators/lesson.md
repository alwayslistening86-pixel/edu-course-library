# S11_Parameters_Closures_Context_Decorators - Lesson: Parameters, closures, IIFEs, call/apply/bind and decorators

## Goal
The learner uses default, rest and spread parameters and options objects, writes closures and IIFEs, controls this with call, apply and bind, and writes decorators.

## Syllabus items taught here
- 4.1a - Default values, rest parameters and spread
- 4.1b - Simulating named parameters with objects and destructuring
- 4.2a - Closures over the lexical environment
- 4.2b - Immediately Invoked Function Expressions (IIFEs)
- 4.3a - Managing this with call, apply and bind
- 4.4a - Decorators: wrapper and higher-order functions

## How to teach this
Ask why `setTimeout(obj.method, 0)` often breaks, and how bind fixes it. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 4.1a Default values, rest parameters and spread
**Defaults** apply when an argument is `undefined` (not when it's `null`), and can refer to earlier parameters. **Rest** `...args` collects the remaining arguments into a real array (it must come last). **Spread** `fn(...arr)` expands an array into separate arguments.
```javascript
function greet(name = "guest", greeting = `Hello ${name}`) { return greeting; }
function sum(first, ...others) { return first + others.reduce((a, b) => a + b, 0); }
console.log(greet(), greet(undefined), greet(null), sum(1, 2, 3, 4), Math.max(...[4, 8, 2]));
```
Output:
```
Hello guest Hello guest Hello null 10 8
```

#### 4.1b Simulating named parameters with objects and destructuring
**Named parameters** are simulated by passing an object and destructuring it in the parameter list, with defaults for each option and `= {}` so the call can omit it entirely.
```javascript
function createUser({ name, role = "reader", active = true } = {}) {
  return `${name ?? "anon"}:${role}:${active}`;
}
console.log(createUser({ name: "Ann", active: false }), createUser());
```
Output:
```
Ann:reader:false anon:reader:true
```

#### 4.2a Closures over the lexical environment
A **closure** is a function together with the variables in scope where it was created; it keeps access to them after the outer function returns. Each call to the outer function creates a fresh environment. Common uses: private state, and functions configured by parameters.
```javascript
function makeAccount(balance) {
  return { deposit: n => (balance += n), get balance() { return balance; } };
}
const a1 = makeAccount(10), a2 = makeAccount(100);
a1.deposit(5);
console.log(a1.balance, a2.balance, a1.balance === 15);
const fns = [];
for (let i = 0; i < 3; i++) fns.push(() => i);
console.log(fns.map(f => f()));
```
Output:
```
15 100 true
[ 0, 1, 2 ]
```

#### 4.2b Immediately Invoked Function Expressions (IIFEs)
An **IIFE** (Immediately Invoked Function Expression), `(function () { ... })();` or `(() => { ... })()`, runs once, straight away, giving a private scope and a place to build a module with private state.
```javascript
const counter = (function () {
  let count = 0;
  return { next: () => ++count };
})();
counter.next();
console.log(counter.next(), typeof count);
```
Output:
```
2 undefined
```

#### 4.3a Managing this with call, apply and bind
`fn.call(thisArg, a, b)` calls fn with a chosen `this` and separate arguments; `fn.apply(thisArg, [a, b])` does the same with an array of arguments; `fn.bind(thisArg, ...preset)` returns a **new function** with `this` (and any preset arguments) fixed permanently. That's how methods are borrowed and how callbacks keep their `this`.
```javascript
function intro(greeting, punct) { return `${greeting}, I'm ${this.name}${punct}`; }
const ann = { name: "Ann" };
console.log(intro.call(ann, "Hi", "!"), intro.apply(ann, ["Hello", "."]));
const annHi = intro.bind(ann, "Hey");
console.log(annHi("?"));
const obj = { n: 5, get() { return this?.n; } };
const lost = obj.get, fixed = obj.get.bind(obj);
console.log(lost(), fixed());
```
Output:
```
Hi, I'm Ann! Hello, I'm Ann.
Hey, I'm Ann?
undefined 5
```

#### 4.4a Decorators: wrapper and higher-order functions
A **decorator** is a higher-order function that takes a function and returns a new one with added behaviour (logging, timing, caching, validation), forwarding the call with `fn.apply(this, args)` so that `this` and the arguments pass through unchanged.
```javascript
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (!cache.has(key)) cache.set(key, fn.apply(this, args));
    return cache.get(key);
  };
}
let calls = 0;
const slowSquare = n => { calls++; return n * n; };
const fastSquare = memoize(slowSquare);
console.log(fastSquare(9), fastSquare(9), fastSquare(3), calls);
```
Output:
```
81 81 9 2
```

## Explicitly not here
Generators and asynchronous code are S12 and S13.
