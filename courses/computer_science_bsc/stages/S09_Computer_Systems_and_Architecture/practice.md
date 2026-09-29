# S09_Computer_Systems_and_Architecture - Practice: Computer systems and architecture

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. Name the three classic pipeline hazards and give one word describing what each is caused by (data, control, or resource contention). [3 marks]
2. What does this print? (If it raises an error, name it.)
```python
def fcfs(processes):
    time = 0
    result = []
    for name, burst in processes:
        time += burst
        result.append((name, time))
    return result
print(fcfs([('P1', 4), ('P2', 2), ('P3', 6)]))
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. [3] B1 data hazard -- an instruction needs a result not yet produced by a preceding instruction still in the pipeline; B1 control hazard -- a branch/jump whose outcome is not yet known when the next fetch must happen; B1 structural hazard -- two instructions needing the same hardware resource simultaneously.
2. Actual result (from running it):
```
[('P1', 4), ('P2', 6), ('P3', 12)]
```

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
