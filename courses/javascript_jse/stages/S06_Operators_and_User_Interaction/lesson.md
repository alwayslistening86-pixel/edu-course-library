# S06_Operators_and_User_Interaction - Lesson: Operators and user interaction

## Goal
The learner predicts the result of every operator on the syllabus, applies precedence correctly, and uses the three browser dialog boxes.

## Syllabus items taught here
- 3.1a - Assignment and compound assignment operators
- 3.1b - Arithmetic operators and string concatenation
- 3.2a - Logical operators
- 3.2b - Equality and relational comparisons
- 3.3a - The conditional (ternary) operator
- 3.3b - typeof, instanceof and delete
- 3.4a - Precedence, associativity and parentheses
- 3.5a - Dialog boxes alert, confirm and prompt; acting on input

## How to teach this
Ask what `'2' == 2`, `'2' === 2` and `null == 0` give. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 3.1a Assignment and compound assignment operators
`=` assigns and returns the assigned value (so `a = b = 5` works right to left). Compound forms: `+= -= *= /= %= **=`. Increment `++` and decrement `--` in prefix form (`++i`) give the new value; in postfix form (`i++`) they give the old value.
```javascript
let i = 5;
const a = i++, b = ++i;
let s = "ab"; s += "c";
let x, y; x = y = 7;
console.log(a, b, i, s, x, y);
```
Output:
```
5 7 7 abc 7 7
```

#### 3.1b Arithmetic operators and string concatenation
`+ - * /` as usual (`/` never truncates), `%` remainder (sign follows the left operand), `**` power. `+` with a string concatenates. Watch the evaluation order: `1 + 2 + "3"` is `"33"`, but `"1" + 2 + 3` is `"123"`.
```javascript
console.log(7 / 2, 7 % 3, -7 % 3, 2 ** 3, "Total: " + 2 + 3, "Total: " + (2 + 3));
```
Output:
```
3.5 1 -1 8 Total: 23 Total: 5
```

#### 3.2a Logical operators
`!` not, `&&` and, `||` or. `&&` and `||` short-circuit and return one of their **operands**, not necessarily a Boolean: `a || b` gives the first truthy operand (or the last), and `a && b` the first falsy one (or the last). `??` returns its right side only when the left is `null` or `undefined`.
```javascript
console.log(!0, "" || "default", 0 || null, "x" && 5, 0 && 5, 0 ?? 9, null ?? 9);
```
Output:
```
true default null 5 0 0 9
```

#### 3.2b Equality and relational comparisons
`===` and `!==` (strict) compare without conversion: prefer them. `==` and `!=` convert first, giving surprises. Relational `< > <= >=` compare numbers numerically, but two strings character by character (`"10" < "9"` is true). `NaN` is unequal to everything, including itself.
```javascript
console.log(2 == "2", 2 === "2", 0 == "", null == 0, null == undefined, "10" < "9", 10 < 9, NaN == NaN);
```
Output:
```
true false true false true true false false
```

#### 3.3a The conditional (ternary) operator
`condition ? valueIfTrue : valueIfFalse` is an expression, so it can be used inside assignments and template strings.
```javascript
const age = 17;
console.log(age >= 18 ? "adult" : "minor", `${age % 2 ? "odd" : "even"}`);
```
Output:
```
minor odd
```

#### 3.3b typeof, instanceof and delete
`typeof x` gives a type string: `"number"`, `"string"`, `"boolean"`, `"undefined"`, `"bigint"`, `"symbol"`, `"function"`, or `"object"` (also for null and arrays). `obj instanceof Class` checks the prototype chain (arrays are instances of Array and of Object). `delete obj.prop` removes a property and returns true.
```javascript
const o = { a: 1, b: 2 };
console.log(typeof 1, typeof "s", typeof undefined, typeof [], typeof null, typeof function () {}, typeof 5n);
console.log([] instanceof Array, [] instanceof Object, delete o.a, o);
```
Output:
```
number string undefined object object function bigint
true true true { b: 2 }
```

#### 3.4a Precedence, associativity and parentheses
Precedence (high to low, simplified): grouping `()`; member access and calls; `!`, `typeof`, unary `-`, `++` and `--`; `**`; `* / %`; `+ -`; `< > <= >=` and `instanceof`; `== != === !==`; `&&`; `||` and `??`; `?:`; assignment. `**` and assignment are **right-associative**; most others are left-associative. Parentheses make the order explicit.
```javascript
console.log(2 + 3 * 4, (2 + 3) * 4, 2 ** 3 ** 2, 10 - 4 - 3, true || false && false, !true || true);
```
Output:
```
14 20 512 3 true true
```

#### 3.5a Dialog boxes alert, confirm and prompt; acting on input
Browser-only dialogs, which block the page until answered: `alert(msg)` shows a message and returns undefined; `confirm(msg)` returns `true` for OK and `false` for Cancel; `prompt(msg, default)` returns the typed **string**, or `null` if cancelled. Always convert and check the result: `const n = Number(prompt("Age?"));`. These functions don't exist in Node; try them in a browser console.

## Explicitly not here
Control flow is S07 and S08.
