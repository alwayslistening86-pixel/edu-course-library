# S13_Advanced_Machine_Learning_and_AI - Test: Advanced machine learning and AI

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
import math
def sigmoid(z):
    return 1 / (1 + math.exp(-z))
inputs = [0.5, -0.2, 1.0]
weights = [0.6, 0.3, -0.4]
bias = 0.05
z = sum(w*x for w, x in zip(weights, inputs)) + bias
print(round(z, 4), round(sigmoid(z), 4))
```
2. A single perceptron has weights [0.5, -0.3], bias 0.2, and input [2, 4]. Compute z (the weighted sum plus bias) and the output using a step activation (output 1 if z>0, else 0), showing your working. [4 marks]
3. A weight update uses gradient descent with learning rate 0.05, current weight w=2.0, and computed gradient dLoss/dw = 8. Compute the new weight, and explain what would happen if the learning rate were instead 5.0. [4 marks]
4. Explain why a Convolutional Neural Network uses far fewer parameters than a fully-connected network would to process the same image, and why this matters in practice. [4 marks]
5. A company's loan-approval model achieves an equal positive-approval rate across two demographic groups (demographic parity) but a much higher false-positive rate (wrongly approving a loan that later defaults) for one group than the other. Explain why satisfying demographic parity does not guarantee the model is 'fair' in every sense, referring to equalised odds. [4 marks]
6. Which statements about neural network activation functions and architectures are correct? Choose every correct option.
   A. `ReLU is defined as max(0, z)`
   B. A network using only linear activations throughout, however many layers, can only represent a linear function overall
   C. Backpropagation computes gradients using the chain rule, working backwards from the output layer
   D. An RNN processes an entire sequence in one single step with no notion of order

## Answer key (for the tutor only)
1. Actual result (from running it):
```
-0.11 0.4725
```
2. [4] M1 z = (0.5)(2) + (-0.3)(4) + 0.2; M1 = 1 - 1.2 + 0.2; A1 z = 0; A1 step activation output: 0 (since z is not > 0, using the strict '> 0' rule stated).
3. [4] M1 w_new = w - lr x gradient = 2.0 - 0.05 x 8; A1 = 2.0 - 0.4 = 1.6; B1 explains a learning rate of 5.0 gives an update of 2.0 - 5.0x8 = -38.0, a huge overshoot far past any sensible value; B1 explains this risks the weight (and loss) oscillating wildly or diverging rather than converging smoothly towards a minimum -- an overly large learning rate is a genuine practical training failure, not just 'slower'.
4. [4] B1 a CNN's convolutional layer uses one small filter (a fixed, small set of weights) that is reused (slid) across every position in the image, rather than a separate weight for every pixel-to-neuron connection; B1 a fully-connected layer would need a distinct weight for every input pixel to every neuron, growing enormously with image size; B1 fewer parameters means less memory and computation, and crucially less risk of overfitting on a limited amount of training data; B1 the shared filter also means a learned feature (e.g. an edge detector) can be recognised anywhere in the image, not only in the specific location it happened to appear during training.
5. [4] B1 demographic parity only requires the overall approval rate to be similar across groups, saying nothing about whether those approvals are equally *accurate* for each group; B1 equalised odds instead requires the true-positive rate and false-positive rate to be similar across groups, a genuinely different (and here violated) condition; B1 a model can satisfy demographic parity while still systematically making more costly errors (here, false positives leading to defaults) for one group than another; B1 concludes that 'fairness' is not a single fixed property -- different fairness metrics can point in different directions, so which one is appropriate depends on the application and its real-world costs of each type of error.
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Advanced_Machine_Learning_and_AI` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_AI_in_Practice_Cognitive_Science_and_Ethics.
