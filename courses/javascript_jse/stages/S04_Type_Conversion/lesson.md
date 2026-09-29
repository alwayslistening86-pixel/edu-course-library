# S04_Type_Conversion - Lesson: Type conversion

## Goal
The learner converts values explicitly and predicts JavaScript's implicit conversions in arithmetic, concatenation and comparisons.

## Syllabus items taught here
- 2.4a - Converting with String, Number, BigInt and Boolean
- 2.4b - Primitive conversion and implicit (automatic) conversion

## How to teach this
Ask for the results of '5' + 3, '5' - 3 and '5' * '2'. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 2.4a Converting with String, Number, BigInt and Boolean
Explicit conversion functions (called without `new`): `String(x)`, `Number(x)` (`"42"` gives 42, `""` gives 0, `"4x"` gives NaN, `true` gives 1, `null` gives 0, `undefined` gives NaN), `BigInt(x)` (whole numbers only, otherwise RangeError or SyntaxError), and `Boolean(x)`. Falsy values: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`; everything else is truthy, including `"0"`, `"false"`, `[]` and `{}`. `parseInt("42px")` parses a leading number and stops at the first invalid character.
```javascript
console.log(Number("42"), Number(""), Number("4x"), Number(true), Number(null), Number(undefined));
console.log(String(12) + String(null), Boolean("0"), Boolean([]), Boolean(""), BigInt(10) * 2n, parseInt("42px"));
```
Output:
```
42 0 NaN 1 0 NaN
12null true true false 20n 42
```

#### 2.4b Primitive conversion and implicit (automatic) conversion
**Implicit** conversion happens automatically. `+` with a string on either side concatenates, turning the other operand into a string. The other arithmetic operators (`- * / %`) convert to numbers. `==` converts types before comparing (`===` doesn't). Conditions convert to Boolean.
```javascript
console.log("5" + 3, 3 + "5", "5" - 3, "5" * "2", "10" / "4", 1 + 2 + "3", "1" + 2 + 3, true + 1, [] + []);
```
Output:
```
53 35 2 10 2.5 33 123 2 
```

## Explicitly not here
Equality operators in depth are S06.
