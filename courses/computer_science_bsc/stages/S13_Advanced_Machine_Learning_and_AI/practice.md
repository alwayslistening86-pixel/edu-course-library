# S13_Advanced_Machine_Learning_and_AI - Practice: Advanced machine learning and AI

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
def relu(z):
    return max(0, z)
print(relu(-3), relu(0), relu(4.5))
```
2. Explain why a single perceptron with a step-function activation cannot learn the XOR function. [3 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
0 0 4.5
```
2. [3] B1 XOR is not linearly separable: no single straight line (decision boundary) can separate the (0,0)/(1,1) outputs (0) from the (0,1)/(1,0) outputs (1); B1 a single perceptron with a step activation only computes a linear decision boundary (a weighted sum compared to a threshold); B1 learning XOR requires either multiple layers (a hidden layer introducing non-linearity) or a non-linear model, not a single perceptron.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
