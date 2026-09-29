# S11_Introduction_to_Machine_Learning_and_AI - Lesson: Introduction to machine learning and AI

## Goal
The learner distinguishes classification from regression and explains the train/test split and overfitting/underfitting, implements/traces k-nearest neighbours and a decision tree split, explains k-means clustering, and computes accuracy/precision/recall/F1 from a confusion matrix.

## Syllabus items taught here
- 11a - Supervised learning: classification versus regression, the train/test split, overfitting and underfitting
- 11b - Key supervised algorithms: k-nearest neighbours, decision trees, linear regression as a learned model
- 11c - Unsupervised learning: clustering with k-means, the idea of dimensionality reduction
- 11d - Evaluating classifiers: accuracy, precision, recall, F1 score and the confusion matrix

## How to teach this
Ask the learner why a model that gets 99% accuracy predicting whether a rare disease is present might still be a bad model -- before introducing precision/recall. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 11a Supervised learning: classification versus regression, the train/test split, overfitting and underfitting
**Supervised learning.** In **classification**, the target variable is categorical (e.g. spam/not-spam, which of 3 species); in **regression**, the target is continuous/numeric (e.g. predicting a house price). Both are *supervised* because training data includes the correct answer (*label*) for each example. Data is split into a **training set** (used to fit the model's parameters) and a **test set** (held out, used only to evaluate the final model on data it has never seen, giving an honest estimate of real-world performance) -- often with a further **validation set** used during development to tune choices like model complexity without touching the test set. **Overfitting** occurs when a model learns the training data's noise/idiosyncrasies too closely, performing well on training data but poorly on new data (a model too complex for the amount/nature of the data); **underfitting** occurs when a model is too simple to capture the real underlying pattern, performing poorly on both training and test data.

#### 11b Key supervised algorithms: k-nearest neighbours, decision trees, linear regression as a learned model
**k-nearest neighbours (k-NN)** classifies a new point by finding the k training points closest to it (by some distance measure, e.g. Euclidean distance) and taking a majority vote of their labels -- simple, makes no assumption about the data's underlying distribution, but slow at prediction time on large datasets (must compare against every training point) and sensitive to the choice of k and to irrelevant/unscaled features. **Decision trees** repeatedly split the data on the feature (and threshold) that best separates the classes at each node (commonly chosen to maximise *information gain*, the reduction in entropy/impurity the split achieves), building a tree of yes/no questions down to leaves that predict a class; easy to interpret, but prone to overfitting if grown too deep (mitigated by pruning or limiting depth). **Linear regression** as an ML model fits a line/hyperplane minimising squared error, exactly the same least-squares idea covered statistically in S06, now viewed as a simple, interpretable, fast-to-train supervised learning algorithm.
```python
def euclidean(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def knn_predict(train, labels, point, k):
    dists = sorted(range(len(train)), key=lambda i: euclidean(train[i], point))
    nearest_labels = [labels[i] for i in dists[:k]]
    return max(set(nearest_labels), key=nearest_labels.count)

train = [(1, 1), (1, 2), (5, 5), (6, 5), (2, 1)]
labels = ["A", "A", "B", "B", "A"]
print(knn_predict(train, labels, (1.5, 1.5), k=3))
print(knn_predict(train, labels, (5.5, 5.5), k=3))
```
Output:
```
A
B
```

#### 11c Unsupervised learning: clustering with k-means, the idea of dimensionality reduction
**Unsupervised learning** has no labels: the algorithm finds structure in the data on its own. **k-means clustering** partitions data into k clusters: (1) initialise k cluster *centroids* (e.g. randomly); (2) assign each point to its nearest centroid; (3) recompute each centroid as the mean of the points currently assigned to it; (4) repeat steps 2-3 until assignments stop changing (convergence). The choice of k is itself a modelling decision (not learned from the data automatically), often guided by domain knowledge or heuristics such as the 'elbow method'. **Dimensionality reduction** (e.g. Principal Component Analysis) compresses data with many features into fewer new features that retain as much of the original variance/information as possible -- used to visualise high-dimensional data, reduce noise, or speed up downstream learning, at the cost of the new features no longer having a directly interpretable real-world meaning.
```python
def kmeans_one_iteration(points, centroids):
    def dist(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b))
    assignments = [min(range(len(centroids)), key=lambda c: dist(p, centroids[c])) for p in points]
    new_centroids = []
    for c in range(len(centroids)):
        members = [points[i] for i in range(len(points)) if assignments[i] == c]
        if members:
            new_centroids.append(tuple(sum(coord) / len(members) for coord in zip(*members)))
        else:
            new_centroids.append(centroids[c])
    return assignments, new_centroids

points = [(1, 1), (1, 2), (8, 8), (9, 8), (0, 1)]
assignments, new_centroids = kmeans_one_iteration(points, centroids=[(0, 0), (10, 10)])
print("assignments:", assignments)
print("updated centroids:", [tuple(round(x, 2) for x in c) for c in new_centroids])
```
Output:
```
assignments: [0, 0, 1, 1, 0]
updated centroids: [(0.67, 1.33), (8.5, 8.0)]
```

#### 11d Evaluating classifiers: accuracy, precision, recall, F1 score and the confusion matrix
**Evaluating classifiers.** A **confusion matrix** cross-tabulates predicted vs actual class: **True Positive (TP)** predicted positive, actually positive; **False Positive (FP)** predicted positive, actually negative (a 'false alarm'); **False Negative (FN)** predicted negative, actually positive (a 'miss'); **True Negative (TN)** predicted negative, actually negative. **Accuracy** = (TP+TN)/(TP+TN+FP+FN) -- misleading on imbalanced data (e.g. a rare-disease detector that always predicts 'no disease' can score 99% accuracy while catching zero real cases). **Precision** = TP/(TP+FP) -- of everything predicted positive, how much genuinely was; matters when false positives are costly (e.g. flagging legitimate email as spam). **Recall** = TP/(TP+FN) -- of everything genuinely positive, how much was caught; matters when false negatives are costly (e.g. missing a real disease case, or a real fraud transaction). **F1 score** = 2 x (precision x recall)/(precision + recall) -- the harmonic mean of precision and recall, a single number balancing both, useful when both false positives and false negatives matter and the classes are imbalanced.
```python
def confusion_counts(y_true, y_pred, positive=1):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == positive and p == positive)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t != positive and p == positive)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == positive and p != positive)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t != positive and p != positive)
    return tp, fp, fn, tn

y_true = [1, 1, 1, 0, 0, 0, 0, 1, 0, 1]
y_pred = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
tp, fp, fn, tn = confusion_counts(y_true, y_pred)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print(f"TP={tp} FP={fp} FN={fn} TN={tn}")
print(f"precision={precision:.3f} recall={recall:.3f} f1={f1:.3f}")
```
Output:
```
TP=3 FP=1 FN=2 TN=4
precision=0.750 recall=0.600 f1=0.667
```

## Explicitly not here
Neural networks, backpropagation and deep architectures are S13.
