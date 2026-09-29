# S02_Standard_Modules_math_random_platform - Lesson: The math, random and platform modules

## Goal
The learner predicts the results of the syllabus functions in math, uses random reproducibly, and knows what each platform function reports.

## Syllabus items taught here
- 1.2a - math: ceil(), floor(), trunc()
- 1.2b - math: factorial(), hypot(), sqrt()
- 1.3a - random: random() and seed()
- 1.3b - random: choice() and sample()
- 1.4a - platform: platform(), machine(), processor(), system()
- 1.4b - platform: version(), python_implementation(), python_version_tuple()

## How to teach this
Ask what `math.floor(-2.5)`, `math.trunc(-2.5)` and `math.ceil(-2.5)` give. They are all different. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 1.2a math: ceil(), floor(), trunc()
`ceil(x)` rounds up to the next integer, `floor(x)` rounds down, and `trunc(x)` cuts off the fraction, towards zero. They differ only for negatives. All three return an int.
```python
import math
for x in (2.5, -2.5):
    print(x, math.ceil(x), math.floor(x), math.trunc(x))
```
Output:
```
2.5 3 2 2
-2.5 -2 -3 -2
```

#### 1.2b math: factorial(), hypot(), sqrt()
`factorial(n)` is n! for a non-negative int (ValueError for negatives). `hypot(x, y)` is the length of the hypotenuse, sqrt(x² + y²). `sqrt(x)` always returns a float (ValueError for negatives).
```python
import math
print(math.factorial(5), math.hypot(3, 4), math.sqrt(16), math.factorial(0))
```
Output:
```
120 5.0 4.0 1
```

#### 1.3a random: random() and seed()
`random()` returns a float in [0.0, 1.0). The numbers are pseudo-random: `seed(value)` resets the generator, so the same seed gives the same sequence, which is essential for testing.
```python
import random
random.seed(7)
a = [random.random() for _ in range(2)]
random.seed(7)
b = [random.random() for _ in range(2)]
print(a == b, all(0 <= x < 1 for x in a))
```
Output:
```
True True
```

#### 1.3b random: choice() and sample()
`choice(seq)` picks one element. `sample(seq, k)` picks k **distinct** positions, without replacement; k larger than the sequence is a ValueError. (`randint(a, b)` and `randrange` also exist, but aren't on this syllabus list.)
```python
import random
random.seed(1)
s = random.sample(range(10), 4)
print(len(s), len(set(s)), random.choice("xyz") in "xyz")
try:
    random.sample([1, 2], 3)
except ValueError as e:
    print("ValueError")
```
Output:
```
4 4 True
ValueError
```

#### 1.4a platform: platform(), machine(), processor(), system()
`platform.platform()` gives one string describing the OS and version; `machine()` the hardware type (e.g. `x86_64`); `processor()` the processor name (may be empty); `system()` the OS name, such as `Linux`, `Windows` or `Darwin`. All return strings whose values depend on the machine, which is why the exam asks what they report, not what they print.

#### 1.4b platform: version(), python_implementation(), python_version_tuple()
`version()` gives the OS version string; `python_implementation()` gives the interpreter, such as `CPython`; `python_version_tuple()` gives a tuple of **strings**, e.g. `('3', '12', '3')`.
```python
import platform
t = platform.python_version_tuple()
print(type(t).__name__, type(t[0]).__name__, len(t), platform.python_implementation())
```
Output:
```
tuple str 3 CPython
```

## Explicitly not here
Writing your own modules is S01; files are S11.
