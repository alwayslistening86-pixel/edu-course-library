# S01_Modules_Imports_and_Packages - Lesson: Modules, imports and packages

## Goal
The learner imports modules and packages in every syllabus form, predicts which names each form brings in, and explains how Python finds, caches and runs module code.

## Syllabus items taught here
- 1.1a - Import variants: import, from-import, import-as, from-import-*
- 1.1b - Qualifying names in nested modules
- 1.1c - The dir() function
- 1.1d - The sys.path variable
- 1.5a - Why modules exist: the idea and rationale
- 1.5b - The __pycache__ directory
- 1.5c - The __name__ variable
- 1.5d - Public and private module variables
- 1.5e - The __init__.py file
- 1.5f - How Python searches for modules and packages
- 1.5g - Nested packages versus directory trees

## How to teach this
Ask: 'If two files both define a function called helper, how can one program use both?' Then show modules as the answer. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 1.1a Import variants: import, from-import, import-as, from-import-*
Four forms. `import math` binds the module name; its contents are reached as `math.sqrt`. `from math import sqrt, pi` binds just those names, with no prefix. `import math as m` binds the module under an alias; the name `math` is then *not* bound. `from math import *` binds every public name, which is discouraged because it silently overwrites existing names.
```python
import math as m
from math import sqrt, pi
print(m.floor(2.7), sqrt(16), round(pi, 2))
try:
    math.ceil(1.2)
except NameError as e:
    print("NameError:", e)
```
Output:
```
2 4.0 3.14
NameError: name 'math' is not defined
```

#### 1.1b Qualifying names in nested modules
For nested packages, qualify with dots from the top package down: `import os.path` then `os.path.join(...)`, or `from os.path import join`. With `import a.b.c`, the name bound is `a`, and you still write `a.b.c.f()`.
```python
import os.path
print(os.path.join("dir", "file.txt"), os.path.basename("/x/y/z.py"))
```
Output:
```
dir/file.txt z.py
```

#### 1.1c The dir() function
`dir(module)` lists the names a module defines, sorted alphabetically, including dunder names. `dir()` with no argument lists the current namespace.
```python
import math
print("sqrt" in dir(math), len([n for n in dir(math) if not n.startswith("_")]) > 30, dir(math)[:3])
```
Output:
```
True True ['__doc__', '__loader__', '__name__']
```

#### 1.1d The sys.path variable
`sys.path` is the **list of directories** searched, in order, when you import. It starts with the script's own directory, then the standard library and site-packages. Being a list, it can be changed at run time (`sys.path.append("/my/modules")`).
```python
import sys
print(type(sys.path).__name__, len(sys.path) > 0)
```
Output:
```
list True
```

#### 1.5a Why modules exist: the idea and rationale
A **module** is a `.py` file whose names can be used by other code; a **package** is a directory of modules. They exist to split large programs into manageable, reusable, separately testable parts, and to keep names from different parts from colliding (each module is its own namespace).

#### 1.5b The __pycache__ directory
The first time a module is imported, Python compiles it to **bytecode** and caches it in a `__pycache__` folder beside it (as `name.cpython-3XX.pyc`). Later imports reuse it if the source hasn't changed. The main script itself isn't cached.

#### 1.5c The __name__ variable
Every module has `__name__`. When the file is run directly it's `"__main__"`; when imported it's the module's own name. The common guard `if __name__ == "__main__":` runs test or demo code only when the file is executed directly. A module's top-level code runs **once**, on first import.
```python
import textwrap, os, sys, importlib
open("greet.py", "w").write(textwrap.dedent('''
    print("greet module loading, __name__ =", __name__)
    def hello():
        return "hello"
    if __name__ == "__main__":
        print("run directly")
'''))
sys.path.insert(0, os.getcwd())
import greet
import greet
print(greet.hello(), __name__)
```
Output:
```
greet module loading, __name__ = greet
hello __main__
```

#### 1.5d Public and private module variables
Python has no truly private module variables. By convention a leading underscore (`_helper`) marks a name as internal: `from module import *` skips it, but explicit access `module._helper` still works. A module can also list exactly what `import *` exports in `__all__`.

#### 1.5e The __init__.py file
A directory becomes a regular **package** when it contains `__init__.py`. That file runs when the package is first imported, and can be empty or can set up package-level names. (Python 3 also allows 'namespace packages' without it, but the exam's model is the `__init__.py` package.)

#### 1.5f How Python searches for modules and packages
On `import x`, Python first checks already-loaded modules (`sys.modules`), then searches each directory in `sys.path` in order and takes the first match. A local file named like a standard module (`random.py`) therefore shadows the real one, which is a classic bug.

#### 1.5g Nested packages versus directory trees
A **package tree** mirrors a directory tree: `extra/good/best/sigma.py` is imported as `extra.good.best.sigma`, and each directory level needs its own `__init__.py`. Packages can also be imported from a zip file on `sys.path`.
```python
import os, sys
os.makedirs("extra/good", exist_ok=True)
open("extra/__init__.py", "w").write("")
open("extra/good/__init__.py", "w").write("print('extra.good initialised')")
open("extra/good/tools.py", "w").write("def f():\n    return 42")
sys.path.insert(0, os.getcwd())
import extra.good.tools
from extra.good.tools import f
print(extra.good.tools.f(), f())
```
Output:
```
extra.good initialised
42 42
```

## Explicitly not here
The contents of math, random and platform are S02.
