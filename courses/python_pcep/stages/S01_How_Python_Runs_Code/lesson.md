# S01_How_Python_Runs_Code - Lesson: How Python runs code: interpreters, keywords, indentation, comments

## Goal
The learner explains how Python turns source text into running behaviour, recognises keywords, and writes correctly indented, commented code.

## Syllabus items taught here
- 1.1a - Interpreting versus compiling, and what an interpreter does
- 1.1b - Lexis, syntax and semantics of a language
- 1.2a - Python keywords
- 1.2b - Instructions (statements) and how Python reads them
- 1.2c - Indentation as structure
- 1.2d - Comments

## How to teach this
Ask: 'When you press Run, who actually reads your code, and what happens if line 7 has a typo but line 1 is fine?' Let them guess, then run a short file with an error on its last line to show that the earlier lines already ran. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 1.1a Interpreting versus compiling, and what an interpreter does
A **compiler** translates the whole program into machine code before anything runs; an **interpreter** reads the source and carries it out as it goes. CPython (the standard Python) is usually called interpreted: it first turns your file into bytecode and then executes that bytecode instruction by instruction. The practical consequence the exam tests is that a runtime error on a later line does not stop earlier lines from running, while a *syntax* error anywhere stops the file before anything runs.
```python
print("first line runs")
x = 1 / 1
print("second line runs too")
```
Output:
```
first line runs
second line runs too
```

#### 1.1b Lexis, syntax and semantics of a language
Three words the exam uses precisely. **Lexis** is the vocabulary: which words and symbols exist (`while`, `+`, `"text"`). **Syntax** is the grammar: which arrangements are legal (`print("hi"` is a syntax error because a bracket is missing). **Semantics** is the meaning: code can be perfectly legal yet mean the wrong thing (`area = width + height` is valid syntax but the wrong calculation).

#### 1.2a Python keywords
**Keywords** are reserved words with a fixed meaning; you cannot use them as variable names. Examples: `if`, `else`, `elif`, `while`, `for`, `in`, `def`, `return`, `pass`, `break`, `continue`, `True`, `False`, `None`, `and`, `or`, `not`, `try`, `except`, `global`, `import`, `class`, `lambda`, `del`, `is`. Note that `print` and `input` are *not* keywords; they are built-in functions, so `print = 5` is legal (and a bad idea).
```python
import keyword
print(len(keyword.kwlist), "keywords, for example:", keyword.kwlist[:6])
print(keyword.iskeyword("print"))
```
Output:
```
35 keywords, for example: ['False', 'None', 'True', 'and', 'as', 'assert']
False
```

#### 1.2b Instructions (statements) and how Python reads them
An **instruction** (statement) is one complete command. Normally one statement per line; a line ends the statement. Two statements can share a line with a semicolon (`a = 1; b = 2`), but PEP 8 discourages it. Python is case-sensitive: `Print("x")` is a NameError, not a call to `print`.

#### 1.2c Indentation as structure
**Indentation** is part of the syntax. The body of `if`, `while`, `for`, `def` and `try` is the indented block that follows the colon, and it ends where indentation returns to the outer level. Use four spaces per level (PEP 8) and never mix tabs and spaces. Wrong or inconsistent indentation raises `IndentationError` before the program runs.
```python
x = 5
if x > 3:
    print("inside the if")
    print("still inside")
print("outside: always printed")
```
Output:
```
inside the if
still inside
outside: always printed
```

#### 1.2d Comments
A **comment** starts with `#` and runs to the end of the line; the interpreter ignores it. There is no multi-line comment syntax: a triple-quoted string on its own line is a string that happens to be unused, not a comment. A `#` inside a string is just a character (`"#1 fan"`).

## Explicitly not here
Literals, numeric types and operators come in S02 and S03; keep examples to print and simple assignment.
