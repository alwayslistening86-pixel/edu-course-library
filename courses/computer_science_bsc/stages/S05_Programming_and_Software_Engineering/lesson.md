# S05_Programming_and_Software_Engineering - Lesson: Programming and software engineering

## Goal
The learner applies the SOLID principles and explains coupling/cohesion, recognises and applies Singleton, Factory Method, Observer and Strategy design patterns, writes and evaluates unit tests using black-box and white-box thinking, and describes a Git branching workflow with code review.

## Syllabus items taught here
- 5a - Object-oriented design principles: the SOLID principles, coupling and cohesion
- 5b - Design patterns: Singleton, Factory Method, Observer and Strategy -- purpose and structure
- 5c - Software testing: unit testing, black-box vs white-box testing, test coverage, test-driven development
- 5d - Version control and collaborative engineering practice: Git branching model, pull requests, code review

## How to teach this
Ask the learner what goes wrong when one class is responsible for reading a file, validating its contents, and emailing a report -- before naming the Single Responsibility Principle. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 5a Object-oriented design principles: the SOLID principles, coupling and cohesion
**SOLID principles** (object-oriented design): **S**ingle Responsibility -- a class should have one reason to change (one responsibility); **O**pen/Closed -- code should be open for extension but closed for modification (add new behaviour via new code, not by editing tested code); **L**iskov Substitution -- a subclass must be usable anywhere its superclass is expected without breaking correctness; **I**nterface Segregation -- prefer several small, specific interfaces over one large general-purpose one, so clients depend only on methods they use; **D**ependency Inversion -- depend on abstractions (interfaces), not concrete implementations, so high-level modules do not depend on low-level details. **Coupling** measures how much one module depends on another's internals (low coupling is desirable: modules can change independently); **cohesion** measures how closely a module's responsibilities relate to each other (high cohesion is desirable: a module does one clear job). Low coupling and high cohesion together make a codebase easier to understand, test and change safely.

#### 5b Design patterns: Singleton, Factory Method, Observer and Strategy -- purpose and structure
**Design patterns** (reusable solutions to recurring design problems). **Singleton**: ensures a class has exactly one instance, with a global access point (e.g. a single configuration manager) -- useful but can hide dependencies and complicate testing if overused. **Factory Method**: defines an interface for creating an object but lets subclasses decide which concrete class to instantiate, decoupling client code from concrete classes. **Observer**: an object (the *subject*) maintains a list of dependents (*observers*) and notifies them automatically of state changes (the basis of most event-handling/publish-subscribe systems, e.g. GUI event listeners). **Strategy**: defines a family of interchangeable algorithms, encapsulates each one, and lets the algorithm be selected/swapped at runtime (e.g. choosing between different sorting or payment-processing strategies without changing the code that uses them).
```python
class SortStrategy:
    def sort(self, data):
        raise NotImplementedError

class AscendingStrategy(SortStrategy):
    def sort(self, data):
        return sorted(data)

class DescendingStrategy(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=True)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    def run(self, data):
        return self.strategy.sort(data)

data = [5, 2, 8, 1]
print(Sorter(AscendingStrategy()).run(data))
print(Sorter(DescendingStrategy()).run(data))
```
Output:
```
[1, 2, 5, 8]
[8, 5, 2, 1]
```

#### 5c Software testing: unit testing, black-box vs white-box testing, test coverage, test-driven development
**Software testing.** A **unit test** checks one small piece of code (e.g. one function) in isolation. **Black-box testing** designs tests from the specification alone, without looking at the implementation (does the function behave correctly for valid input, boundary values, and invalid input?); **white-box testing** designs tests using knowledge of the code's internal structure, aiming to exercise specific branches/paths (e.g. every `if`/`else` branch at least once). **Test coverage** measures the proportion of code exercised by a test suite (e.g. statement coverage, branch coverage); high coverage reduces but does not eliminate the risk of undetected bugs (covered code can still be wrong if the assertions themselves are wrong). **Test-driven development (TDD)** writes a failing test *before* the implementation, then writes just enough code to make it pass, then refactors -- the 'red, green, refactor' cycle.
```python
def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

# black-box tests from the specification: below range, in range, above range, boundary values
tests = [
    (clamp(-5, 0, 10) == 0, "below range"),
    (clamp(5, 0, 10) == 5, "in range"),
    (clamp(15, 0, 10) == 10, "above range"),
    (clamp(0, 0, 10) == 0, "lower boundary"),
    (clamp(10, 0, 10) == 10, "upper boundary"),
]
for passed, name in tests:
    print(name, "PASS" if passed else "FAIL")
```
Output:
```
below range PASS
in range PASS
above range PASS
lower boundary PASS
upper boundary PASS
```

#### 5d Version control and collaborative engineering practice: Git branching model, pull requests, code review
**Version control with Git.** A **branch** is an independent line of development; a common workflow keeps `main` always deployable, creates a **feature branch** for each new piece of work, and merges it back via a **pull request (PR)** once reviewed. A **merge** combines two branches' histories (a *fast-forward* merge if no divergent commits exist on the target branch; otherwise a *merge commit* records both parents); a **rebase** replays one branch's commits on top of another, producing a linear history but rewriting commit hashes (never rebase commits already shared/pushed to others, since this breaks collaborators' history). **Code review**: before a PR is merged, at least one other developer reads the diff, checking correctness, readability, adherence to team standards and test coverage -- catching defects earlier and cheaper than testing alone, and spreading knowledge of the codebase across the team. A **merge conflict** arises when two branches change the same lines differently; it must be resolved manually (or with a merge tool) before the merge can complete.

## Explicitly not here
Requirements engineering and lifecycle models are S04; formal correctness proofs of algorithms are S07/S08.
