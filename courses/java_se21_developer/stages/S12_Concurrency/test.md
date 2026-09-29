# S12_Concurrency - Test: Threads, executors, thread safety and parallel processing

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
import java.util.concurrent.*;
// ---- main ----
ExecutorService ex = Executors.newFixedThreadPool(2);
Future<Integer> f = ex.submit(() -> { throw new java.io.IOException("disk"); });
try { f.get(); } catch (ExecutionException e) { System.out.println(e.getCause().getClass().getSimpleName() + ": " + e.getCause().getMessage()); }
ex.shutdown();
System.out.println(ex.awaitTermination(1, TimeUnit.SECONDS) + " " + ex.isTerminated());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
Thread v = Thread.ofVirtual().unstarted(() -> System.out.print("v "));
System.out.print(v.getState() + " ");
v.start(); v.join();
System.out.println(v.getState() + " " + v.isVirtual() + " " + v.isDaemon());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
import java.util.concurrent.atomic.*;
// ---- main ----
AtomicLong a = new AtomicLong(10);
System.out.println(a.incrementAndGet() + " " + a.getAndIncrement() + " " + a.get() + " " + a.accumulateAndGet(3, Math::max) + " " + a.compareAndSet(12, 0) + " " + a);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
import java.util.concurrent.*;
// ---- main ----
List<Integer> safe = new CopyOnWriteArrayList<>(List.of(1, 2));
for (Integer x : safe) safe.add(x * 10);
System.out.print(safe + " ");
List<Integer> unsafe = new ArrayList<>(List.of(1, 2));
for (Integer x : unsafe) unsafe.add(x * 10);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
import java.util.concurrent.*;
// ---- main ----
ConcurrentHashMap<String, Integer> m = new ConcurrentHashMap<>();
try (ExecutorService ex = Executors.newFixedThreadPool(4)) {
    for (int i = 0; i < 100; i++) ex.submit(() -> m.merge("k", 1, Integer::sum));
}
System.out.println(m);
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
Object lock = new Object();
lock.notify();
```
7. Which are true? (choose two) Choose every correct option.
   A. Calling run() on a Thread starts a new thread
   B. Future.get() blocks until the result is available
   C. Virtual threads are always daemon threads
   D. A parallel stream's forEach preserves encounter order

## Answer key (for the tutor only)
1. Actual result (from running it):
```
IOException: disk
true true
```
2. Actual result (from running it):
```
NEW v TERMINATED true true
```
3. Actual result (from running it):
```
11 11 12 12 true 0
```
4. Actual result (from running it):
```
[1, 2, 10, 20] 
(throws ConcurrentModificationException)
```
5. Actual result (from running it):
```
{k=100}
```
6. Actual result (from running it):
```
(throws IllegalMonitorStateException: current thread is not owner)
```
7. Correct: B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Concurrency` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_IO_and_NIO2.
