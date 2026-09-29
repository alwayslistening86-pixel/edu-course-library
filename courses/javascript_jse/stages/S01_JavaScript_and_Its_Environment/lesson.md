# S01_JavaScript_and_Its_Environment - Lesson: JavaScript and its environment

## Goal
The learner explains how JavaScript is run, where it runs, what tools are used to write and debug it, and how it's attached to a web page.

## Syllabus items taught here
- 1.1a - Interpreting versus compilation; interpreter versus compiler
- 1.1b - Client-side versus server-side JavaScript
- 1.2a - Development tools: editor, console, debugger
- 1.2b - Online versus local development environments
- 1.3a - HTML basics and ways to embed scripts
- 1.3b - Running code in the browser console

## How to teach this
Open a browser console (F12) and type 2 + 2. Ask: where did that code run, and who ran it? Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 1.1a Interpreting versus compilation; interpreter versus compiler
A **compiler** translates a whole program into another form before it runs; an **interpreter** executes the source more or less directly. JavaScript is described as interpreted: the source is shipped as text and the engine (V8 in Chrome and Node, SpiderMonkey in Firefox) runs it, internally using just-in-time (JIT) compilation for speed. Consequence: there's no separate build step, and most errors appear only when the code actually runs.

#### 1.1b Client-side versus server-side JavaScript
**Client-side** JavaScript runs in the user's browser and can change the page (the DOM), respond to clicks and call servers. **Server-side** JavaScript runs on a server under Node.js, where it reads files and databases and answers requests; it has no page and no `window` object. The core language is the same in both.
```javascript
console.log(typeof window, typeof process)
```
Output:
```
undefined object
```

#### 1.2a Development tools: editor, console, debugger
Minimum tools: a **code editor** (VS Code, or even a plain text editor), a way to **run** code (a browser, or Node.js), the **console** for messages and quick experiments, and a **debugger** (the browser's developer tools, or VS Code) for pausing and inspecting a running program.

#### 1.2b Online versus local development environments
**Online** environments (JSFiddle, CodePen, the JS Institute's own sandbox) need no installation and are good for learning and sharing. A **local** set-up (editor, browser and Node.js on your machine) works offline and suits real projects.

#### 1.3a HTML basics and ways to embed scripts
HTML describes a page's structure. JavaScript is attached with the `<script>` element, either inline (`<script>console.log("hi")</script>`) or from a file (`<script src="app.js"></script>`). Scripts run in the order they appear, as the page loads; putting them at the end of `<body>`, or adding `defer`, lets the HTML load first.

#### 1.3b Running code in the browser console
The browser's **console** (developer tools, F12) runs one line or a block at a time and shows the result immediately. `console.log(...)` writes values to it, and the same call works in Node. It's the fastest way to try out an expression.
```javascript
console.log("sum:", 2 + 3, [1, 2], { a: 1 })
```
Output:
```
sum: 5 [ 1, 2 ] { a: 1 }
```

## Explicitly not here
Variables and types start in S02.
