# S05_Programming_and_Software_Engineering - Test: Programming and software engineering

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, obs):
        self._observers.append(obs)
    def notify(self, event):
        for obs in self._observers:
            obs.update(event)

class Logger:
    def update(self, event):
        print('logged:', event)

s = Subject()
s.attach(Logger())
s.attach(Logger())
s.notify('temperature changed')
```
2. A `PaymentProcessor` class currently has an if/elif chain choosing between credit-card, PayPal and bank-transfer logic inline. Explain how the Strategy pattern would restructure this, and name one SOLID principle it would better satisfy. [4 marks]
3. Explain the difference between black-box and white-box testing, and give one example test case each approach would specifically motivate for a function `is_leap_year(year)`. [5 marks]
4. Explain what a merge conflict is and when it occurs. [3 marks]
5. A team disables code review to 'move faster'. Give two specific risks this introduces to the codebase or team. [4 marks]
6. Which statements correctly describe the SOLID principles? Choose every correct option.
   A. Liskov Substitution requires a subclass to be usable anywhere its superclass is expected without breaking correctness
   B. Dependency Inversion means high-level modules should depend on concrete low-level implementations directly
   C. Interface Segregation prefers several small, specific interfaces over one large general-purpose interface
   D. Open/Closed means code should be closed for extension and open for modification

## Answer key (for the tutor only)
1. Actual result (from running it):
```
logged: temperature changed
logged: temperature changed
```
2. [4] B1 each payment method becomes its own class implementing a common PaymentStrategy interface (e.g. a pay(amount) method); B1 PaymentProcessor holds a reference to a chosen strategy object and delegates to it, rather than branching internally; B1 adding a new payment method means adding a new strategy class, not editing PaymentProcessor; B1 this better satisfies the Open/Closed Principle (open for extension via new strategies, closed for modification of existing code).
3. [5] B1 black-box: derived from the specification alone, without inspecting the implementation; B1 white-box: derived from knowledge of the code's internal branches/paths, aiming to exercise each one; B1 valid black-box example, e.g. testing a boundary/typical year from the specification of leap years (divisible by 4, not by 100 unless also by 400) such as year=2000 or year=1900; B1 valid white-box example: a test specifically chosen because the code has a distinct branch for 'divisible by 100 but not 400' that black-box testing might miss unless the tester specifically targets it; B1 both examples are genuinely different in *how* they were derived, not just different numbers.
4. [3] B1 occurs when two branches have each changed the same lines of the same file in different, incompatible ways; B1 Git cannot automatically decide which change should 'win', so it cannot complete the merge automatically; B1 the developer must manually inspect and resolve the conflicting sections (choosing one version, combining both, or writing new code) before the merge can be completed.
5. [4] B2 defects that a second reviewer would likely have caught now reach main/production, increasing bug rate and the cost of fixing them later (B1 if named but not explained); B2 knowledge of the codebase becomes siloed in whoever wrote each piece, increasing bus-factor risk and making onboarding/maintenance harder (B1 if named but not explained); credit any two genuinely distinct, well-explained risks.
6. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Programming_and_Software_Engineering` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Practical_Modern_Statistics.
