# S13_Advanced_Machine_Learning_and_AI - Lesson: Advanced machine learning and AI

## Goal
The learner computes a perceptron's forward pass and explains activation functions, describes gradient descent and works a simple weight update, outlines convolutional and recurrent architectures at a conceptual level, and explains bias, fairness metrics and interpretability in applied machine learning.

## Syllabus items taught here
- 13a - Neural networks: the perceptron, activation functions, computing a forward pass by hand
- 13b - Backpropagation and gradient descent: the intuition and a simple worked weight update
- 13c - Deep learning architectures: the convolution operation (CNNs), the idea of a recurrent/sequence model (RNNs)
- 13d - Practical machine learning: bias in training data, fairness metrics, model interpretability

## How to teach this
Ask the learner: if a perceptron is just a weighted sum plus a threshold, how could stacking many of them possibly learn something as complex as recognising a handwritten digit? -- motivating layers and non-linearity. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 13a Neural networks: the perceptron, activation functions, computing a forward pass by hand
**The perceptron.** A single perceptron computes a weighted sum of its inputs plus a bias term, z = sum(w_i . x_i) + b, then applies an **activation function** to produce its output. A step-function activation (output 1 if z>0, else 0) gives the original, simplest perceptron (a linear classifier -- can only separate linearly separable data, famously cannot learn XOR). Modern networks use smoother activations: **sigmoid** (squashes to (0,1), historically common, prone to the 'vanishing gradient' problem in deep networks), **ReLU** (Rectified Linear Unit: max(0, z), simple, fast, the most common choice in modern hidden layers), **tanh** ((-1,1), zero-centred). Stacking layers of such units, each layer's output feeding the next, with a non-linear activation between layers, lets a network learn non-linear decision boundaries a single perceptron cannot.
```python
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def relu(z):
    return max(0, z)

def forward_pass(inputs, weights, bias, activation):
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    return z, activation(z)

inputs = [1.0, 0.5, -1.5]
weights = [0.4, 0.9, -0.6]
bias = 0.1
z, out_sigmoid = forward_pass(inputs, weights, bias, sigmoid)
_, out_relu = forward_pass(inputs, weights, bias, relu)
print(f"z = {z:.3f}")
print(f"sigmoid(z) = {out_sigmoid:.4f}")
print(f"relu(z) = {out_relu:.4f}")
```
Output:
```
z = 1.850
sigmoid(z) = 0.8641
relu(z) = 1.8500
```

#### 13b Backpropagation and gradient descent: the intuition and a simple worked weight update
**Gradient descent and backpropagation.** Training a neural network means finding weights that minimise a **loss function** (a measure of how wrong the network's predictions are, e.g. mean squared error for regression). **Gradient descent** repeatedly nudges each weight in the direction that most reduces the loss: w_new = w_old - (learning_rate x dLoss/dw), where dLoss/dw is the loss's gradient (partial derivative) with respect to that weight -- the learning rate controls the step size (too large overshoots/diverges; too small trains very slowly). **Backpropagation** is the algorithm that efficiently computes every weight's gradient by applying the chain rule backwards from the output layer's error through each preceding layer, reusing intermediate results rather than recomputing each derivative from scratch -- what makes training deep (many-layer) networks computationally feasible at all.
```python
def gradient_descent_step(w, gradient, learning_rate):
    return w - learning_rate * gradient

# a single weight update: loss = (w*x - target)^2, dLoss/dw = 2x(wx - target)
x, target, w, lr = 2.0, 5.0, 1.0, 0.1
prediction = w * x
loss = (prediction - target) ** 2
gradient = 2 * x * (prediction - target)
w_new = gradient_descent_step(w, gradient, lr)
print(f"prediction={prediction}, loss={loss}, gradient={gradient}, w_new={w_new}")
```
Output:
```
prediction=2.0, loss=9.0, gradient=-12.0, w_new=2.2
```
The weight moves from 1.0 towards 2.5 (the value that would make w.x exactly equal target=5), since the gradient points in the direction of increasing loss and the update subtracts a fraction of it.

#### 13c Deep learning architectures: the convolution operation (CNNs), the idea of a recurrent/sequence model (RNNs)
**Deep learning architectures (conceptual level).** A **Convolutional Neural Network (CNN)** applies small learned filters (kernels) that slide across an input (typically an image), each computing a weighted sum over a local neighbourhood of pixels (the *convolution* operation) -- this exploits spatial structure (nearby pixels are related) and lets the same filter detect a feature (e.g. an edge) anywhere in the image, using far fewer parameters than connecting every pixel to every neuron; stacked convolutional layers learn increasingly abstract features (edges, then shapes, then object parts). A **Recurrent Neural Network (RNN)** processes a sequence (e.g. text, time-series) one element at a time while maintaining a *hidden state* that carries information from earlier elements forward -- suited to data where order/context matters, though plain RNNs struggle to retain information over long sequences (addressed by variants such as LSTM, Long Short-Term Memory, which add gating mechanisms to control what is remembered/forgotten).

#### 13d Practical machine learning: bias in training data, fairness metrics, model interpretability
**Practical machine learning: bias, fairness and interpretability.** A model trained on historical data inherits and can amplify that data's **bias**: if past hiring decisions were themselves biased against a group, a model trained to imitate those decisions learns and perpetuates the same bias, even without ever being given demographic data explicitly (it can find a *proxy* for it, e.g. postcode correlating with ethnicity/income). **Fairness metrics** attempt to quantify this, e.g. *demographic parity* (the model's positive-prediction rate should be similar across groups) versus *equalised odds* (the model's true-positive and false-positive rates should be similar across groups) -- these two definitions can conflict with each other and with overall accuracy, so 'fairness' requires an explicit, justified choice of which definition matters for the application, not a single universal metric. **Interpretability**: a simple model (e.g. a shallow decision tree or linear regression) is inherently interpretable (a human can inspect exactly why it made a given prediction); a deep neural network is largely a 'black box' -- techniques such as feature-importance analysis or model-agnostic local explanation methods (e.g. LIME, SHAP) attempt to approximate *why* a complex model made a specific prediction, but are themselves approximations, not the model's true internal reasoning.

## Explicitly not here
Symbolic AI, the Turing Test and philosophy of mind are S14.
