# S04_Console_Input_and_Output - Lesson: Console input and output

## Goal
The learner controls exactly what print() outputs and reads numbers safely from input().

## Syllabus items taught here
- 1.5a - print() and input()
- 1.5b - The sep= and end= keyword arguments of print()
- 1.5c - Converting input with int() and float()

## How to teach this
Ask what `print(1, 2, 3, sep='')` and `print('a', end='')` followed by `print('b')` display. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 1.5a print() and input()
`print()` writes its arguments, separated by a space and followed by a newline; with no arguments it prints an empty line. It returns `None`. `input(prompt)` shows the prompt, waits for a line of typing and **always returns a string** (without the newline).
```python
print("a", 1, True)
print()
result = print("x")
print(result)
```
Output:
```
a 1 True

x
None
```

#### 1.5b The sep= and end= keyword arguments of print()
`sep=` sets what goes *between* arguments (default one space); `end=` sets what goes *after* the last one (default a newline). Both must be strings.
```python
print(1, 2, 3, sep="-")
print("no newline", end="|")
print("next")
print("a", "b", sep="", end="!\n")
```
Output:
```
1-2-3
no newline|next
ab!
```

#### 1.5c Converting input with int() and float()
Because `input()` returns text, arithmetic on it needs conversion: `int(input())` or `float(input())`. Without it, `"3" + "4"` is `"34"`, and `"3" * 2` is `"33"`. A non-numeric entry raises ValueError (handled in S11). Example program (not run here, since it waits for typing): `age = int(input("Age: "))` then `print("Next year:", age + 1)`.

## Explicitly not here
Formatting with f-strings is not on the PCEP syllabus; use sep, end and concatenation.
