# S05_Programming_Paradigms - Practice: Programming paradigms: procedural and object-oriented programming

## Goal
Low-stakes practice: the learner predicts or attempts each item first, then checks it (by running code, or against the model answer). Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " makes a sound"

class Dog(Animal):
    def speak(self):
        return self.name + " barks"

a = Dog("Rex")
print(a.speak())
```
2. Explain what encapsulation means in object-oriented programming, and why it is useful. [2 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
Rex barks
```
2. [2] B1 hiding an object's internal data, exposing it only through its own methods; B1 protects the data from being changed directly in invalid ways from outside the object.

## How to run it
One item at a time. For code-output/trace items the learner commits to a prediction before running or checking anything. Offer a worked explanation only after a genuine attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
