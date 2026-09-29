# S13_Promises_Async_Await_and_Fetch - Lesson: Promises, async/await and network requests

## Goal
The learner creates and consumes promises, combines them, writes async/await code with proper error handling, and makes network requests.

## Syllabus items taught here
- 4.7a - Creating promises; then, catch and finally
- 4.8a - Promise chains; Promise.all, Promise.any, Promise.race
- 4.9a - async functions, await, and try/catch for errors
- 4.10a - Network requests with XMLHttpRequest and the Fetch API

## How to teach this
Take the callback example from S12 and ask how it could read top to bottom instead. Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 4.7a Creating promises; then, catch and finally
A **Promise** represents a future result: pending, then fulfilled (resolved) or rejected. Create one with `new Promise((resolve, reject) => { ... })`. `.then(onFulfilled)` runs with the value; `.catch(onRejected)` handles errors; `.finally(fn)` runs either way. Promise callbacks always run **asynchronously**, after the current code finishes.
```javascript
function wait(ms, value, fail = false) {
  return new Promise((resolve, reject) => setTimeout(() => (fail ? reject(new Error(value)) : resolve(value)), ms));
}
console.log("before");
wait(5, "done").then(v => console.log("then:", v)).finally(() => console.log("finally 1"));
wait(10, "oops", true).then(v => console.log("not reached")).catch(e => console.log("catch:", e.message)).finally(() => console.log("finally 2"));
console.log("after");
```
Output:
```
before
after
then: done
finally 1
catch: oops
finally 2
```

#### 4.8a Promise chains; Promise.all, Promise.any, Promise.race
`then` returns a **new** promise, so steps chain; returning a value, or a promise, from a `then` passes it to the next step, and one `catch` at the end handles an error from any step. `Promise.all([...])` waits for all (it rejects as soon as any rejects) and keeps the input order. `Promise.any` takes the first to **fulfil** (AggregateError if all reject). `Promise.race` takes the first to **settle**, success or failure. `Promise.allSettled` reports every outcome.
```javascript
const wait = (ms, v, fail) => new Promise((res, rej) => setTimeout(() => (fail ? rej(new Error(v)) : res(v)), ms));
Promise.resolve(2).then(x => x * 10).then(x => wait(5, x + 1)).then(x => console.log("chain:", x));
Promise.all([wait(20, "a"), wait(5, "b")]).then(v => console.log("all:", v));
Promise.all([wait(5, "ok"), wait(10, "bad", true)]).catch(e => console.log("all rejected:", e.message));
Promise.any([wait(5, "x", true), wait(15, "y")]).then(v => console.log("any:", v));
Promise.race([wait(5, "fast", true), wait(15, "slow")]).catch(e => console.log("race:", e.message));
```
Output:
```
race: fast
chain: 21
all rejected: bad
any: y
all: [ 'a', 'b' ]
```

#### 4.9a async functions, await, and try/catch for errors
An `async` function always returns a promise. Inside it, `await promise` pauses **that function** (not the whole program) until the promise settles, then gives its value or throws its error, so ordinary `try/catch` works. Awaiting in sequence is slow for independent tasks; `await Promise.all([...])` runs them in parallel.
```javascript
const wait = (ms, v, fail) => new Promise((res, rej) => setTimeout(() => (fail ? rej(new Error(v)) : res(v)), ms));
async function main() {
  const a = await wait(5, 1);
  const [b, c] = await Promise.all([wait(5, 2), wait(5, 3)]);
  try {
    await wait(5, "boom", true);
  } catch (e) {
    console.log("caught", e.message);
  }
  return a + b + c;
}
main().then(total => console.log("total", total));
console.log("main started; it returned a", typeof main().then);
```
Output:
```
main started; it returned a function
caught boom
total 6
caught boom
```

#### 4.10a Network requests with XMLHttpRequest and the Fetch API
**Fetch API**: `fetch(url, options)` returns a promise of a Response. Check `response.ok` (fetch only rejects on network failure, not on HTTP 404 or 500), then read the body with `await response.json()` or `.text()`. POST by passing `{ method: "POST", headers, body: JSON.stringify(data) }`. **XMLHttpRequest** is the older browser API: `const x = new XMLHttpRequest(); x.open("GET", url); x.onload = () => ...; x.send();`, and it's browser-only (try it in a browser console). The example below starts a tiny local server so the requests can really run.
```javascript
const http = require("http");
const server = http.createServer((req, res) => {
  if (req.url === "/api/user") { res.setHeader("Content-Type", "application/json"); res.end(JSON.stringify({ id: 1, name: "Ann" })); }
  else { res.statusCode = 404; res.end("not found"); }
}).listen(0, async () => {
  const base = `http://127.0.0.1:${server.address().port}`;
  try {
    const r1 = await fetch(base + "/api/user");
    console.log(r1.ok, r1.status, await r1.json());
    const r2 = await fetch(base + "/missing");
    console.log(r2.ok, r2.status, await r2.text());
  } catch (e) {
    console.log("network error", e.message);
  } finally {
    server.close();
  }
});
```
Output:
```
true 200 { id: 1, name: 'Ann' }
false 404 not found
```

## Explicitly not here
Web sockets, workers and the DOM are outside JSA-41-01.
