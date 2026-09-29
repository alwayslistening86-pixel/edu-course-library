# S10_Computer_Networks_and_Cybersecurity - Practice: Computer networks and cybersecurity

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. State which TCP/IP layer is responsible for logical addressing and routing between networks, and name its main protocol. [2 marks]
2. What does this print? (If it raises an error, name it.)
```python
import hashlib
print(hashlib.sha256(b'hello').hexdigest() == hashlib.sha256(b'hello').hexdigest())
print(hashlib.sha256(b'hello').hexdigest() == hashlib.sha256(b'Hello').hexdigest())
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. [2] B1 the Internet layer; B1 IP (Internet Protocol).
2. Actual result (from running it):
```
True
False
```

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
