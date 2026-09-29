# S09_Set_Map_Dictionaries_and_JSON - Lesson: Set, Map, objects as dictionaries, and JSON

## Goal
The learner chooses between Set, Map and plain objects for a task, and serialises and parses JSON, including its edge cases.

## Syllabus items taught here
- 3.6a - Set: construct, add/has/delete/clear/size, iterate, spread
- 3.7a - Map: construct, set/get/has/delete/clear/size, iterate pairs
- 3.8a - Plain objects as dictionaries: managing and iterating entries
- 3.9a - JSON.stringify and JSON.parse

## How to teach this
Ask for the quickest way to remove duplicates from an array. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 3.6a Set: construct, add/has/delete/clear/size, iterate, spread
A **Set** holds unique values (compared like `===`, but with NaN equal to NaN). Methods: `add` (chainable), `has`, `delete`, `clear`; `size` is a property. Iterate with `for...of` or `forEach`; spread into an array.
```javascript
const s = new Set([3, 1, 3, 2, 1]);
s.add(4).add(1);
console.log(s.size, s.has(2), s.delete(9), [...s]);
console.log([...new Set("mississippi")].join(""));
```
Output:
```
4 true false [ 3, 1, 2, 4 ]
misp
```

#### 3.7a Map: construct, set/get/has/delete/clear/size, iterate pairs
A **Map** holds key-value pairs, where keys can be of **any type** (objects too), and remembers insertion order. Methods: `set` (chainable), `get`, `has`, `delete`, `clear`, and the `size` property. Iterating gives `[key, value]` pairs; `keys()`, `values()` and `entries()` are also available.
```javascript
const m = new Map([["a", 1]]);
const objKey = { id: 7 };
m.set(objKey, "object as key").set(2, "number key");
console.log(m.get(objKey), m.get({ id: 7 }), m.size, m.has(2));
for (const [k, v] of m) console.log(typeof k, v);
```
Output:
```
object as key undefined 3 true
string 1
object object as key
number number key
```

#### 3.8a Plain objects as dictionaries: managing and iterating entries
A plain object can serve as a **dictionary** with string keys: add with `obj[key] = v`, test with `key in obj` or `Object.hasOwn`, delete with `delete`, iterate with `Object.entries`. Prefer a Map when keys aren't strings, change often, or when order and size matter.
```javascript
const counts = {};
for (const w of "to be or not to be".split(" ")) counts[w] = (counts[w] ?? 0) + 1;
console.log(counts, Object.entries(counts).filter(([, n]) => n > 1).map(([w]) => w));
```
Output:
```
{ to: 2, be: 2, or: 1, not: 1 } [ 'to', 'be' ]
```

#### 3.9a JSON.stringify and JSON.parse
`JSON.stringify(value, replacer, indent)` produces text: object keys become double-quoted; `undefined`, functions and symbols are **skipped** in objects (and become `null` in arrays); Dates become ISO strings; Maps and Sets become `{}`. `JSON.parse(text, reviver)` rebuilds plain data, and throws SyntaxError on invalid JSON (single quotes, trailing commas).
```javascript
const data = { n: 1, s: "x", u: undefined, f() {}, arr: [1, undefined], d: new Date(0), m: new Map([[1, 2]]) };
const text = JSON.stringify(data);
console.log(text);
console.log(JSON.parse('{"a":[1,2]}').a[1], JSON.stringify({ a: 1 }, null, 2));
try { JSON.parse("{'a': 1}"); } catch (e) { console.log(e.name); }
```
Output:
```
{"n":1,"s":"x","arr":[1,null],"d":"1970-01-01T00:00:00.000Z","m":{}}
2 {
  "a": 1
}
SyntaxError
```

## Explicitly not here
Math and RegExp are S10.
