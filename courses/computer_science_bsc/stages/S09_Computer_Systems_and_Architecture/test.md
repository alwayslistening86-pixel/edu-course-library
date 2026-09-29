# S09_Computer_Systems_and_Architecture - Test: Computer systems and architecture

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
def simulate_cache(accesses, cache_size):
    cache = []
    hits = 0
    for a in accesses:
        if a in cache:
            hits += 1
            cache.remove(a); cache.append(a)
        else:
            if len(cache) >= cache_size:
                cache.pop(0)
            cache.append(a)
    return hits
print(simulate_cache([5, 6, 5, 7, 8, 5, 6], cache_size=2))
```
2. Explain why pipelining a CPU's instruction execution improves throughput even though it does not reduce the time to execute any single instruction. [3 marks]
3. Explain the difference between temporal locality and spatial locality, and how cache design exploits each. [4 marks]
4. Three processes P1 (burst 6), P2 (burst 2), P3 (burst 4) arrive together and are scheduled with Round Robin, quantum 3. Trace the schedule, giving the order processes run and the completion time of each. [6 marks]
5. Explain the four necessary conditions for deadlock (the Coffman conditions), and state one general strategy for preventing it that removes one of these conditions. [5 marks]
6. Which statements correctly distinguish concurrency from parallelism? Choose every correct option.
   A. Parallelism requires multiple physical execution units (cores) to be literally true
   B. Concurrency can be achieved on a single core via rapid task switching
   C. Concurrency and parallelism are two names for exactly the same thing
   D. A race condition can only occur in a truly parallel (multi-core) system, never under concurrent single-core scheduling

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1
```
2. [3] B1 without pipelining, each instruction must fully complete (fetch, decode, execute) before the next one starts, so total time is roughly n x (time for one instruction); B1 with pipelining, the fetch of instruction k+1 overlaps with the decode of instruction k and the execute of instruction k-1, so once the pipeline is full, a new instruction completes roughly every cycle; B1 total throughput (instructions completed per unit time) therefore improves even though the latency of any single instruction (its own fetch-decode-execute time) is unchanged or even slightly increased.
3. [4] B2 temporal locality: recently accessed memory is likely to be accessed again soon; caches exploit this by keeping recently used data in cache rather than evicting it immediately (B1 if named but not explained); B2 spatial locality: memory addresses near a recently accessed address are likely to be accessed soon; caches exploit this by fetching a whole block/line of nearby memory on a miss, not just the single requested address (B1 if named but not explained).
4. [6] M1 P1 runs 0-3 (3 left: 3); M1 P2 runs 3-5 (finishes, 0 left); M1 P3 runs 5-8 (1 left: 1); M1 P1 runs 8-11 (finishes, 0 left); M1 P3 runs 11-12 (finishes); A1 completion times: P2=5, P1=11, P3=12, correctly derived from the trace above.
5. [5] B1 mutual exclusion: at least one resource must be held in a non-shareable way; B1 hold-and-wait: a process holds at least one resource while waiting for another; B1 no preemption: a resource cannot be forcibly taken from a process holding it; B1 circular wait: a cycle of processes each waiting for a resource held by the next; B1 a valid prevention strategy naming which condition it removes, e.g. requiring processes to request all needed resources at once (removes hold-and-wait), or imposing a global resource-ordering that processes must request in (removes circular wait).
6. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Computer_Systems_and_Architecture` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 20 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Computer_Networks_and_Cybersecurity.
