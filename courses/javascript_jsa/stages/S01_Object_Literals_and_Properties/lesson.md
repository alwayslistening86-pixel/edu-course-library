# S01_Object_Literals_and_Properties - Lesson: Object literals and properties

## Goal
The learner creates object literals, changes their properties safely, and chooses between dot and bracket notation.

## Syllabus items taught here
- 1.1a - Creating objects with literal syntax and initialising fields
- 1.2a - Adding, modifying and deleting properties
- 1.2b - Nested properties and optional chaining
- 1.3a - Dot notation for ordinary identifiers
- 1.3b - Bracket notation for multi-word, dynamic or computed keys

## How to teach this
Ask how to read a property whose name is stored in a variable. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 1.1a Creating objects with literal syntax and initialising fields
An **object literal** creates an object directly: `{ key: value, ... }`. Keys are strings (or symbols); quote keys that aren't valid identifiers. Shorthand `{ name }` means `{ name: name }`; computed keys use `[expr]`.
```javascript
const name = "Ann", field = "score";
const player = { name, [field]: 90, "full name": "Ann Lee", level: 1 };
console.log(player);
```
Output:
```
{ name: 'Ann', score: 90, 'full name': 'Ann Lee', level: 1 }
```

#### 1.2a Adding, modifying and deleting properties
Add or modify by assigning (`o.x = 1`); remove with `delete o.x`. Reading a missing property gives `undefined`.
```javascript
const car = { make: "VW" };
car.year = 2020;
car.make = "Audi";
delete car.year;
console.log(car, car.year);
```
Output:
```
{ make: 'Audi' } undefined
```

#### 1.2b Nested properties and optional chaining
Properties can hold objects, giving **nested** structures (`o.address.city`). Reading through a missing level is a TypeError; **optional chaining** `?.` returns `undefined` instead, and pairs well with `??` for a default.
```javascript
const user = { address: { city: "York" } };
const guest = {};
console.log(user.address.city, guest.address?.city, guest.address?.city ?? "unknown");
try { console.log(guest.address.city); } catch (e) { console.log(e.name); }
```
Output:
```
York undefined unknown
TypeError
```

#### 1.3a Dot notation for ordinary identifiers
**Dot notation** (`o.name`) is shorter and clearer, and works whenever the key is a fixed, valid identifier.

#### 1.3b Bracket notation for multi-word, dynamic or computed keys
**Bracket notation** (`o["key"]`) takes any expression: keys with spaces or dashes, keys held in variables, or keys built at run time. Inside brackets the expression is evaluated; `o.key` always means the literal name "key".
```javascript
const o = { "first name": "Bo", total: 5, key: "literal" };
const key = "total";
console.log(o["first name"], o[key], o.key, o["to" + "tal"]);
```
Output:
```
Bo 5 literal 5
```

## Explicitly not here
Enumeration and copying are S02.
