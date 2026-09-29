# S12_Generators_Iterators_and_Callbacks - Lesson: Generators, iterators and asynchronous callbacks

## Goal
The learner writes generators and custom iterables, and structures asynchronous callback code with error-first conventions.

## Syllabus items taught here
- 4.5a - Generator functions iterated with for...of
- 4.5b - Custom iterables and iterators
- 4.6a - Asynchronous flows with callbacks and error-first conventions

## How to teach this
Ask what a function that can pause and resume would be useful for. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 4.5a Generator functions iterated with for...of
A **generator function** (`function*`) returns a generator object. Each `next()` runs the function up to the next `yield` and returns `{ value, done }`. Generators are iterable, so `for...of` and spread consume them, and they can be infinite, since values are produced lazily.
```javascript
function* countdown(n) {
  while (n > 0) yield n--;
  return "liftoff";
}
const g = countdown(2);
console.log(g.next(), g.next(), g.next(), g.next());
console.log([...countdown(3)]);
function* naturals() { let i = 1; while (true) yield i++; }
const firstFive = [];
for (const n of naturals()) { if (n > 5) break; firstFive.push(n); }
console.log(firstFive);
```
Output:
```
{ value: 2, done: false } { value: 1, done: false } { value: 'liftoff', done: true } { value: undefined, done: true }
[ 3, 2, 1 ]
[ 1, 2, 3, 4, 5 ]
```

#### 4.5b Custom iterables and iterators
An object is **iterable** if it has a `[Symbol.iterator]()` method returning an **iterator**: an object with `next()` that returns `{ value, done }`. Writing `[Symbol.iterator]` as a generator method is the simplest way to build one.
```javascript
const range = {
  from: 1, to: 4,
  [Symbol.iterator]() {
    let cur = this.from, last = this.to;
    return { next: () => cur <= last ? { value: cur++, done: false } : { value: undefined, done: true } };
  }
};
class Team {
  constructor(...names) { this.names = names; }
  *[Symbol.iterator]() { for (const n of this.names) yield n.toUpperCase(); }
}
console.log([...range], Array.from(new Team("ann", "bo")));
```
Output:
```
[ 1, 2, 3, 4 ] [ 'ANN', 'BO' ]
```

#### 4.6a Asynchronous flows with callbacks and error-first conventions
Asynchronous operations report back later through callbacks. Node's convention is the **error-first callback**, `callback(err, result)`: check `err` before using the result. Nesting one async step inside another leads to deeply indented "callback hell"; errors must be passed along explicitly, because a `try` around the call can't catch an error thrown later.
```javascript
function loadUser(id, cb) {
  setTimeout(() => (id > 0 ? cb(null, { id, name: "User" + id }) : cb(new Error("bad id"))), 5);
}
function loadOrders(user, cb) {
  setTimeout(() => cb(null, [user.id * 10, user.id * 10 + 1]), 5);
}
loadUser(3, (err, user) => {
  if (err) return console.log("failed:", err.message);
  loadOrders(user, (err2, orders) => {
    if (err2) return console.log("failed:", err2.message);
    console.log(user.name, orders);
  });
});
loadUser(-1, err => console.log("failed:", err.message));
```
Output:
```
failed: bad id
User3 [ 30, 31 ]
```

## Explicitly not here
Promises and async/await are S13.
