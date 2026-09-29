# S10_Math_RegExp_and_Extending_Builtins - Lesson: Math, regular expressions and extending built-ins

## Goal
The learner uses the Math functions correctly (including random ranges), writes and applies regular expressions, and extends built-ins only with care.

## Syllabus items taught here
- 3.10a - Math: ceil, floor, round, random, min, max, abs, pow, log and trigonometry
- 3.11a - Regular expressions: RegExp and literals; test, exec, match, search, replace
- 3.12a - Extending built-in types through prototypes, and the risks

## How to teach this
Ask how to get a random whole number from 1 to 6. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 3.10a Math: ceil, floor, round, random, min, max, abs, pow, log and trigonometry
`Math.ceil`, `floor`, `round` (halves round **up**, towards +Infinity, so `round(-2.5)` is -2), `trunc`, `abs`, `min(...)`, `max(...)` (spread an array in), `pow(b, e)`, `sqrt`, `log` (natural log), `log10`, the trigonometry functions `sin`, `cos`, `tan` (in **radians**), and `PI`. `Math.random()` gives [0, 1); a whole number from a to b is `Math.floor(Math.random() * (b - a + 1)) + a`.
```javascript
console.log(Math.round(2.5), Math.round(-2.5), Math.ceil(-1.2), Math.floor(-1.2), Math.max(...[3, 9, 1]), Math.min(), Math.pow(2, 10));
console.log(Math.log(Math.E), Math.sin(Math.PI / 2), Math.abs(-4), Math.cos(0));
const rolls = Array.from({ length: 1000 }, () => Math.floor(Math.random() * 6) + 1);
console.log(Math.min(...rolls) >= 1 && Math.max(...rolls) <= 6);
```
Output:
```
3 -2 -1 -2 9 Infinity 1024
1 1 4 1
true
```

#### 3.11a Regular expressions: RegExp and literals; test, exec, match, search, replace
Regular expressions describe text patterns: as a literal `/ab+c/i` or with `new RegExp("ab+c", "i")` (useful when building one from a string). Flags: `g` (global), `i` (ignore case), `m` (multiline). `re.test(str)` returns a Boolean; `re.exec(str)` returns a match array with groups (or null); `str.match(re)` returns the first match, or all of them with `g`; `str.search(re)` returns an index or -1; `str.replace(re, replacement)` can use `$1` for groups.
```javascript
const re = /(\d{2})-(\d{2})-(\d{4})/;
const m = re.exec("born 26-09-2026 in York");
console.log(re.test("x"), m[0], m[1], m.index);
console.log("a1b22c333".match(/\d+/g), "hello".search(/l+/), "26-09-2026".replace(re, "$3/$2/$1"), new RegExp("^h", "i").test("Hi"));
```
Output:
```
false 26-09-2026 26 5
[ '1', '22', '333' ] 2 2026/09/26 true
```

#### 3.12a Extending built-in types through prototypes, and the risks
Built-ins can be extended by adding to their prototypes (`Array.prototype.last = function () { ... }`), or better, by subclassing (`class Stack extends Array`). Changing built-in prototypes is risky: it affects every script on the page, can clash with future standard methods, and shows up in `for...in`. Prefer utility functions or subclasses.
```javascript
class Stack extends Array {
  peek() { return this[this.length - 1]; }
}
const st = Stack.from([1, 2, 3]);
st.push(4);
console.log(st.peek(), st instanceof Array, st.length);
Object.defineProperty(String.prototype, "shout", { value: function () { return this.toUpperCase() + "!"; }, configurable: true });
console.log("hey".shout());
delete String.prototype.shout;
console.log(typeof "x".shout);
```
Output:
```
4 true 4
HEY!
undefined
```

## Explicitly not here
Functions in depth are S11 to S13.
