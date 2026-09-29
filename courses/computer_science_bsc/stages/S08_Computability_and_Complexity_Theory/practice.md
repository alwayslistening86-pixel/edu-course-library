# S08_Computability_and_Complexity_Theory - Practice: Computability and complexity theory

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
import re
pattern = re.compile(r'^(01)+$')
for s in ['01', '0101', '011', '']:
    print(s, bool(pattern.match(s)))
```
2. State which level of the Chomsky hierarchy is needed to recognise balanced parentheses (e.g. '(()())' valid, '(()' invalid), and explain why a finite state machine cannot do this. [3 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
01 True
0101 True
011 False
 False
```
2. [3] B1 context-free (needs a pushdown automaton); B1 recognising balanced parentheses requires counting how many are currently open, to arbitrary depth; B1 a finite state machine has only a fixed, finite number of states, so it cannot remember an unboundedly large open-parenthesis count -- it cannot distinguish e.g. depth 5 from depth 500 with a fixed number of states.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
