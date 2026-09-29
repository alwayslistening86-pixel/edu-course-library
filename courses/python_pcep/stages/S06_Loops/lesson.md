# S06_Loops - Lesson: Loops: while, for, range, break, continue and else

## Goal
The learner writes and traces while and for loops, uses range() precisely, and predicts the effect of break, continue, pass and loop-else.

## Syllabus items taught here
- 2.2a - The pass instruction
- 2.2b - Loops with while, for, range() and in
- 2.2c - Iterating through sequences
- 2.2d - Loop else clauses: while-else and for-else
- 2.2e - Nesting loops and conditionals
- 2.2f - Controlling loops with break and continue

## How to teach this
Ask how many times `for i in range(2, 10, 3): print(i)` prints, and which numbers. (Three: 2, 5, 8.) Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 2.2a The pass instruction
`pass` does nothing. It exists because Python needs at least one statement in a block: `if x > 0: pass` or an empty function body while drafting.

#### 2.2b Loops with while, for, range() and in
`while condition:` repeats while the condition stays truthy; something in the body must eventually change it, or the loop is infinite. `for name in iterable:` takes each element in turn. `range(stop)` gives 0 to stop-1; `range(start, stop)`; `range(start, stop, step)`, where step may be negative. The stop value is never included, and an impossible range is simply empty.
```python
n = 3
while n > 0:
    print(n, end=" ")
    n -= 1
print()
print(list(range(5)), list(range(2, 10, 3)), list(range(5, 0, -2)), list(range(3, 1)))
```
Output:
```
3 2 1 
[0, 1, 2, 3, 4] [2, 5, 8] [5, 3, 1] []
```

#### 2.2c Iterating through sequences
`for` iterates through any sequence: the characters of a string, the items of a list or tuple, or the keys of a dictionary. The loop variable keeps its last value after the loop ends.
```python
for ch in "abc":
    print(ch.upper(), end="")
print()
for item in [10, 20]:
    pass
print(item)
```
Output:
```
ABC
20
```

#### 2.2d Loop else clauses: while-else and for-else
A loop can have an `else` block. It runs when the loop **finishes normally**: a `for` that ran out of items, or a `while` whose condition became false. It does **not** run if the loop was left by `break`. It runs even if the loop body never executed.
```python
for n in [3, 5, 7]:
    if n % 2 == 0:
        print("found even")
        break
else:
    print("no even number")
i = 5
while i < 3:
    i += 1
else:
    print("else ran, i =", i)
```
Output:
```
no even number
else ran, i = 5
```

#### 2.2e Nesting loops and conditionals
Loops and conditions nest freely. With nested loops, the inner loop runs completely for every pass of the outer loop, so the body runs outer x inner times.
```python
for r in range(1, 4):
    for c in range(1, 4):
        print(r * c, end=" ")
    print()
```
Output:
```
1 2 3 
2 4 6 
3 6 9 
```

#### 2.2f Controlling loops with break and continue
`break` leaves the **innermost** loop immediately (and skips its else). `continue` skips the rest of this pass and goes on to the next one.
```python
for i in range(10):
    if i == 2:
        continue
    if i == 5:
        break
    print(i, end=" ")
print()
```
Output:
```
0 1 3 4 
```

## Explicitly not here
Lists as data are S07; here lists appear only as things to loop over.
