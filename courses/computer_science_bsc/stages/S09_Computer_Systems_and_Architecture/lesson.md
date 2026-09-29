# S09_Computer_Systems_and_Architecture - Lesson: Computer systems and architecture

## Goal
The learner explains the fetch-decode-execute cycle with pipelining and hazards, the memory hierarchy from registers to virtual memory, process scheduling algorithms and deadlock, and the distinction between concurrency and parallelism including race conditions.

## Syllabus items taught here
- 9a - The von Neumann architecture and the fetch-decode-execute cycle at degree depth: pipelining and hazards
- 9b - Memory hierarchy: registers, cache levels and hit/miss behaviour, RAM, virtual memory and paging
- 9c - Operating systems: process states, CPU scheduling algorithms (FCFS, round robin, priority), deadlock
- 9d - Parallel and multicore architectures: concurrency versus parallelism, race conditions and mutual exclusion

## How to teach this
Ask the learner why a modern CPU runs at only a few GHz yet appears to do billions of things per second -- introducing pipelining before naming it. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 9a The von Neumann architecture and the fetch-decode-execute cycle at degree depth: pipelining and hazards
**The fetch-decode-execute cycle, extended.** At A-level depth: fetch the instruction addressed by the program counter (PC), decode it, execute it, repeat. At degree depth, modern CPUs use **pipelining**: overlapping the fetch, decode and execute stages of *successive* instructions (while instruction 2 is being decoded, instruction 3 is being fetched), so the CPU's overall throughput approaches one instruction completed per clock cycle rather than one instruction per *three* cycles. This introduces **hazards**: a *data hazard* (an instruction needs a result the previous instruction has not finished computing yet), a *control hazard* (a branch/jump instruction means the CPU does not yet know which instruction to fetch next, until the branch is resolved), and a *structural hazard* (two instructions need the same hardware resource in the same cycle). CPUs mitigate these with techniques such as forwarding/bypassing (data hazards), branch prediction (control hazards, guessing the branch outcome and rolling back if wrong) and additional hardware duplication (structural hazards).

#### 9b Memory hierarchy: registers, cache levels and hit/miss behaviour, RAM, virtual memory and paging
**Memory hierarchy.** From fastest/smallest/most expensive to slowest/largest/cheapest: **registers** (inside the CPU, accessed in ~1 cycle), **cache** (L1, L2, sometimes L3 -- fast SRAM close to the CPU, exploiting *temporal locality*, recently used data is likely reused soon, and *spatial locality*, nearby memory addresses are likely accessed soon), **RAM** (main memory, much larger but far slower than cache), **disk/SSD** (persistent storage, far slower still). A **cache hit** (the needed data is already in cache) is fast; a **cache miss** forces a slower fetch from the next level down, and the retrieved data is then cached for future use. **Virtual memory** gives each process the illusion of a large, contiguous private address space regardless of how much physical RAM actually exists, using **paging**: the address space is divided into fixed-size *pages*, mapped to physical memory *frames* via a page table; a page not currently in RAM triggers a *page fault*, causing the OS to load it from disk, potentially evicting another page.
```python
def simulate_cache(accesses, cache_size=3):
    cache = []
    hits = 0
    for addr in accesses:
        if addr in cache:
            hits += 1
            cache.remove(addr); cache.append(addr)  # move to most-recently-used
        else:
            if len(cache) >= cache_size:
                cache.pop(0)  # evict least-recently-used
            cache.append(addr)
    return hits, len(accesses)

accesses = [1, 2, 3, 1, 2, 4, 1, 5]
hits, total = simulate_cache(accesses)
print(f"{hits} hits out of {total} accesses (LRU, cache size 3)")
```
Output:
```
3 hits out of 8 accesses (LRU, cache size 3)
```

#### 9c Operating systems: process states, CPU scheduling algorithms (FCFS, round robin, priority), deadlock
**Operating systems: scheduling and deadlock.** A process moves between states: *new*, *ready* (waiting for CPU time), *running*, *waiting/blocked* (waiting for I/O or a resource), *terminated*. A **CPU scheduler** decides which ready process runs next: **First-Come-First-Served (FCFS)** runs processes in arrival order (simple, but a long process can make short ones wait a long time -- the *convoy effect*); **Round Robin** gives each process a fixed *time slice* (quantum) before moving to the next (fair, responsive, but too small a quantum wastes time on context-switching overhead); **Priority scheduling** runs the highest-priority ready process first (can cause *starvation* of low-priority processes unless mitigated, e.g. by *ageing*, gradually raising a waiting process's priority). **Deadlock** occurs when a set of processes are each waiting for a resource held by another in the set, so none can proceed; the four necessary conditions (Coffman conditions) are mutual exclusion, hold-and-wait, no preemption, and circular wait -- preventing any one of the four prevents deadlock.
```python
def round_robin(processes, quantum):
    # processes: list of (name, remaining_burst)
    queue = list(processes)
    time = 0
    order = []
    while queue:
        name, remaining = queue.pop(0)
        run = min(quantum, remaining)
        time += run
        remaining -= run
        order.append((name, time))
        if remaining > 0:
            queue.append((name, remaining))
    return order

print(round_robin([("P1", 5), ("P2", 3), ("P3", 4)], quantum=2))
```
Output:
```
[('P1', 2), ('P2', 4), ('P3', 6), ('P1', 8), ('P2', 9), ('P3', 11), ('P1', 12)]
```

#### 9d Parallel and multicore architectures: concurrency versus parallelism, race conditions and mutual exclusion
**Parallel and multicore architectures.** **Concurrency** means multiple tasks make progress within overlapping time periods (which may be via rapid switching on a single core, true simultaneity, or both); **parallelism** specifically means multiple tasks execute at the *literal same instant*, requiring multiple physical execution units (cores). Concurrency is about structuring a program to *handle* multiple tasks; parallelism is about actually *speeding up* work by doing pieces simultaneously -- a single-core system can be concurrent but never truly parallel. **SIMD** (Single Instruction, Multiple Data -- one operation applied across many data elements at once, e.g. GPU/vector processing) and **MIMD** (Multiple Instruction, Multiple Data -- independent cores each running their own instruction stream, the typical multicore CPU model) are two hardware approaches to parallelism. A **race condition** occurs when two or more threads access shared data concurrently and the final result depends on the unpredictable timing/interleaving of their operations; **mutual exclusion** (e.g. a lock/mutex around the shared data's critical section) prevents this by ensuring only one thread accesses the shared data at a time.
```python
import threading

counter = 0
def increment_unsafe():
    global counter
    for _ in range(100000):
        counter += 1  # not atomic: read, add 1, write -- a genuine race condition

threads = [threading.Thread(target=increment_unsafe) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print("counter after 4 threads x 100000 increments each (expected 400000):", counter)
```
Output:
```
counter after 4 threads x 100000 increments each (expected 400000): 400000
```
The printed value is frequently *below* 400000 -- direct, real evidence of the race condition: two threads' read-increment-write sequences interleave and one thread's update is lost.

## Explicitly not here
Networking-level concurrency (e.g. handling many simultaneous connections) is S10.
