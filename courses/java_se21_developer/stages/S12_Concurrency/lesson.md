# S12_Concurrency - Lesson: Threads, executors, thread safety and parallel processing

## Goal
The learner creates platform and virtual threads, runs Runnable and Callable tasks through executor services, manages thread life-cycles, makes shared state thread-safe with synchronized, locks, atomics and concurrent collections, and processes collections concurrently.

## Syllabus items taught here
- 8.1 - Create platform and virtual threads; use Runnable and Callable; manage the thread life-cycle; use Executor services and the concurrent API to run tasks
- 8.2 - Develop thread-safe code using locking mechanisms and the concurrent API
- 8.3 - Process Java collections concurrently and use parallel streams

## How to teach this
Ask why two threads each doing `count++` 100,000 times on a shared int rarely end at 200,000. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 8.1 Create platform and virtual threads; use Runnable and Callable; manage the thread life-cycle; use Executor services and the concurrent API to run tasks
**Creating threads:** pass a `Runnable` to `new Thread(r)` (or subclass Thread) and call `start()` (calling `run()` directly just runs it on the current thread). Java 21 **virtual threads** are lightweight, JVM-scheduled threads for blocking tasks: `Thread.ofVirtual().start(r)`, `Thread.startVirtualThread(r)`, or `Executors.newVirtualThreadPerTaskExecutor()`; `Thread.ofPlatform()` builds platform threads. Virtual threads are always daemon threads. **Life-cycle:** NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED; `join()` waits for a thread to finish; `start()` twice throws `IllegalThreadStateException`; `interrupt()` sets a flag that sleeping or waiting threads receive as `InterruptedException`.
```java
Thread t = new Thread(() -> System.out.println("platform worker on " + Thread.currentThread().getName()), "worker-1");
System.out.println(t.getState());
t.start();
t.join();
System.out.println(t.getState());
Thread v = Thread.ofVirtual().name("v1").start(() -> System.out.println("virtual? " + Thread.currentThread().isVirtual()));
v.join();
System.out.println(v.isDaemon() + " " + v.getName());
Runnable r = () -> System.out.println("run() on " + Thread.currentThread().getName());
new Thread(r, "never-started").run();
Thread sleeper = new Thread(() -> {
    try { Thread.sleep(10_000); } catch (InterruptedException e) { System.out.println("interrupted"); }
});
sleeper.start(); sleeper.interrupt(); sleeper.join();
t.start();
```
Output:
```
NEW
platform worker on worker-1
TERMINATED
virtual? true
true v1
run() on main
interrupted
(throws IllegalThreadStateException)
```
**Executors:** an `ExecutorService` manages a pool: `Executors.newFixedThreadPool(n)`, `newSingleThreadExecutor()`, `newCachedThreadPool()`, `newScheduledThreadPool(n)`, `newVirtualThreadPerTaskExecutor()`. `execute(Runnable)` returns nothing; `submit(Runnable or Callable)` returns a `Future`; `invokeAll` returns a list of futures; `invokeAny` returns one result. A `Callable<V>`'s `call()` returns a value and may throw checked exceptions; `Future.get()` blocks and wraps a task's exception in `ExecutionException`. Always `shutdown()` (or use try-with-resources: since Java 19 `ExecutorService` is `AutoCloseable` and `close()` waits for tasks). After shutdown, new submissions throw `RejectedExecutionException`.
```java
import java.util.concurrent.*;
// ---- main ----
try (ExecutorService pool = Executors.newFixedThreadPool(3)) {
    Callable<Integer> square = () -> 7 * 7;
    Future<Integer> f = pool.submit(square);
    List<Callable<String>> jobs = List.of(() -> "a", () -> "b", () -> "c");
    List<String> results = new ArrayList<>();
    for (Future<String> fu : pool.invokeAll(jobs)) results.add(fu.get());
    Future<?> boom = pool.submit(() -> { throw new IllegalStateException("task failed"); });
    System.out.println(f.get() + " " + results + " " + f.isDone());
    try { boom.get(); } catch (ExecutionException e) { System.out.println("wrapped: " + e.getCause()); }
}
ExecutorService one = Executors.newSingleThreadExecutor();
one.shutdown();
System.out.print(one.isShutdown() + " ");
try { one.submit(() -> 1); } catch (RejectedExecutionException e) { System.out.println("rejected: " + e.getClass().getSimpleName()); }
```
Output:
```
49 [a, b, c] true
wrapped: java.lang.IllegalStateException: task failed
true rejected: RejectedExecutionException
```
```java
import java.util.concurrent.*;
// ---- main ----
try (var vexec = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<Integer>> fs = new ArrayList<>();
    for (int i = 1; i <= 1000; i++) { int n = i; fs.add(vexec.submit(() -> { Thread.sleep(10); return n; })); }
    long sum = 0;
    for (Future<Integer> f : fs) sum += f.get();
    System.out.println("1000 blocking tasks on virtual threads, sum " + sum);
}
```
Output:
```
1000 blocking tasks on virtual threads, sum 500500
```

#### 8.2 Develop thread-safe code using locking mechanisms and the concurrent API
A **race condition** happens when threads read-modify-write shared state without coordination (`count++` is three steps). Fixes: **`synchronized`** methods or blocks (one thread at a time per monitor object; a static synchronized method locks the Class object); **`ReentrantLock`** (`lock()`/`unlock()` in a finally block; `tryLock()` doesn't wait; the same thread may re-acquire; `ReentrantReadWriteLock` allows many readers or one writer); **atomic classes** (`AtomicInteger.incrementAndGet`, `getAndAdd`, `compareAndSet`, `updateAndGet`); **concurrent collections** (`ConcurrentHashMap`, `CopyOnWriteArrayList`, `ConcurrentLinkedQueue`, `BlockingQueue`); coordination tools such as `CountDownLatch` and `CyclicBarrier`. Liveness problems: **deadlock** (threads wait on each other's locks forever), **starvation** and **livelock**. `volatile` makes writes visible to other threads but doesn't make `++` atomic.
```java
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.concurrent.locks.*;
class Counters {
    int unsafe = 0, synced = 0, locked = 0;
    final AtomicInteger atomic = new AtomicInteger();
    final Lock lock = new ReentrantLock();
    synchronized void incSynced() { synced++; }
    void incLocked() { lock.lock(); try { locked++; } finally { lock.unlock(); } }
}
// ---- main ----
Counters c = new Counters();
Runnable job = () -> { for (int i = 0; i < 100_000; i++) { c.unsafe++; c.incSynced(); c.incLocked(); c.atomic.incrementAndGet(); } };
Thread a = new Thread(job), b = new Thread(job);
a.start(); b.start(); a.join(); b.join();
System.out.println("synchronized " + c.synced + ", lock " + c.locked + ", atomic " + c.atomic.get() + ", unsafe <= 200000? " + (c.unsafe <= 200_000));
AtomicInteger ai = new AtomicInteger(5);
System.out.println(ai.compareAndSet(5, 8) + " " + ai.compareAndSet(5, 9) + " " + ai.getAndAdd(2) + " " + ai.updateAndGet(x -> x * 10));
```
Output:
```
synchronized 200000, lock 200000, atomic 200000, unsafe <= 200000? true
true false 8 100
```
(The unsafe total differs from run to run and is usually well below 200000; that unpredictability is the point.)
```java
import java.util.concurrent.*;
import java.util.concurrent.locks.*;
// ---- main ----
ReentrantLock lock = new ReentrantLock();
lock.lock(); lock.lock();
System.out.print(lock.getHoldCount() + " ");
Thread other = new Thread(() -> System.out.print("other got it? " + lock.tryLock() + " "));
other.start(); other.join();
lock.unlock(); lock.unlock();
System.out.println(lock.isLocked());
CountDownLatch ready = new CountDownLatch(3);
ConcurrentHashMap<String, Integer> hits = new ConcurrentHashMap<>();
for (int i = 0; i < 3; i++) Thread.startVirtualThread(() -> { for (int k = 0; k < 1000; k++) hits.merge("page", 1, Integer::sum); ready.countDown(); });
ready.await();
List<Integer> cow = new CopyOnWriteArrayList<>(List.of(1, 2, 3));
for (Integer x : cow) if (x == 1) cow.add(99);
System.out.println(hits + " " + cow);
new ReentrantLock().unlock();
```
Output:
```
2 other got it? false false
{page=3000} [1, 2, 3, 99]
(throws IllegalMonitorStateException)
```

#### 8.3 Process Java collections concurrently and use parallel streams
**Processing collections concurrently:** split work across an executor (`invokeAll` over chunks), use **parallel streams** (`parallelStream()`), and use thread-safe targets. Collecting a parallel stream with `collect(...)` or `toList()` is safe; adding to a shared non-thread-safe list from `forEach` is not. `Collectors.toConcurrentMap` and `groupingByConcurrent` build concurrent maps. Ordinary collections modified while iterating throw `ConcurrentModificationException` (even on one thread); `Collections.synchronizedList` wraps a list, but iterating it still needs a synchronized block.
```java
import java.util.concurrent.*;
// ---- main ----
List<Integer> nums = IntStream.rangeClosed(1, 10_000).boxed().toList();
List<Integer> collected = nums.parallelStream().filter(n -> n % 7 == 0).toList();
List<Integer> shared = Collections.synchronizedList(new ArrayList<>());
nums.parallelStream().filter(n -> n % 7 == 0).forEach(shared::add);
ConcurrentMap<Boolean, Long> evens = nums.parallelStream().collect(Collectors.groupingByConcurrent(n -> n % 2 == 0, Collectors.counting()));
try (ExecutorService pool = Executors.newFixedThreadPool(4)) {
    List<Callable<Long>> chunks = new ArrayList<>();
    for (int c = 0; c < 4; c++) { int from = c * 2500; chunks.add(() -> nums.subList(from, from + 2500).stream().mapToLong(Integer::longValue).sum()); }
    long total = 0;
    for (Future<Long> f : pool.invokeAll(chunks)) total += f.get();
    System.out.println(collected.size() + " " + collected.get(0) + " " + shared.size() + " " + new TreeMap<>(evens) + " " + total);
}
List<String> plain = new ArrayList<>(List.of("a", "b", "c"));
for (String s : plain) if (s.equals("b")) plain.remove(s);
System.out.println(plain);
List<String> plain2 = new ArrayList<>(List.of("a", "b", "c"));
for (String s : plain2) if (s.equals("a")) plain2.remove(s);
```
Output:
```
1428 7 1428 {false=5000, true=5000} 50005000
[a, c]
(throws ConcurrentModificationException)
```
(Removing the second-to-last element happens not to throw, because the loop ends before the check; it's still a bug.)

## Explicitly not here
Parallel stream collectors in general are S11.
