# S11_Introduction_to_Machine_Learning_and_AI - Test: Introduction to machine learning and AI

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A model scores 98% accuracy on training data but only 71% accuracy on test data. Name this phenomenon and give one technique that could help address it. [3 marks]
2. What does this print? (If it raises an error, name it.)
```python
def entropy_reduction_demo(counts_parent, counts_left, counts_right):
    import math
    def entropy(counts):
        total = sum(counts)
        if total == 0:
            return 0
        return -sum((c / total) * math.log2(c / total) for c in counts if c > 0)
    n_parent = sum(counts_parent)
    n_left, n_right = sum(counts_left), sum(counts_right)
    weighted_child_entropy = (n_left / n_parent) * entropy(counts_left) + (n_right / n_parent) * entropy(counts_right)
    return round(entropy(counts_parent) - weighted_child_entropy, 4)

print(entropy_reduction_demo([5, 5], [4, 1], [1, 4]))
```
3. Trace k-NN with k=3 to classify the point (4,4) given training points (1,1)=A, (2,2)=A, (8,8)=B, (5,5)=B, (4,5)=B, using Euclidean distance. State the predicted class and show the distances used. [5 marks]
4. Explain why accuracy alone is a misleading metric for a fraud-detection model where only 1% of transactions are actually fraudulent, and state which metric (precision or recall) matters more if missing a real fraud case is far more costly than investigating a false alarm. [4 marks]
5. A classifier produces TP=40, FP=10, FN=20, TN=130. Compute precision, recall and F1 score, showing your working (round to 3 decimal places). [6 marks]
6. Which statements about k-means clustering are correct? Choose every correct option.
   A. k-means requires the number of clusters k to be chosen in advance
   B. k-means is a supervised learning algorithm requiring labelled data
   C. Each iteration reassigns points to their nearest current centroid and then recomputes centroids
   D. k-means is guaranteed to find the same clustering regardless of the initial centroid positions

## Answer key (for the tutor only)
1. [3] B1 overfitting; B1 the model has learned patterns/noise specific to the training data that do not generalise; B1 a valid technique, e.g. regularisation, reducing model complexity, gathering more training data, or cross-validation for model selection (any one genuine, correct technique).
2. Actual result (from running it):
```
0.2781
```
3. [5] M1 computes distances from (4,4): to (1,1) = root(18) approx 4.24; to (2,2) = root(8) approx 2.83; to (8,8) = root(32) approx 5.66; to (5,5) = root(2) approx 1.41; to (4,5) = 1; A2 the 3 nearest are (4,5) dist 1, (5,5) dist approx 1.41, (2,2) dist approx 2.83 (or accept the correct 3 smallest by the learner's own correctly computed distances); A1 among these 3, labels are B, B, A, so majority is B; A1 predicted class: B.
4. [4] B1 a model that always predicts 'not fraud' would score 99% accuracy while catching zero real fraud cases, since accuracy does not distinguish this from genuinely useful predictions on such imbalanced data; B1 accuracy is dominated by the large majority class (not-fraud), hiding how the model performs on the rare, important class; B1 recall matters more here, since it directly measures the proportion of real fraud cases caught (TP/(TP+FN)); B1 correctly explains that prioritising recall accepts more false positives (more investigated false alarms) in exchange for catching more of the costly false negatives (missed fraud).
5. [6] M1 precision = 40/(40+10) = 0.800; M1 recall = 40/(40+20) = 0.667; A1 F1 = 2(0.8)(0.667)/(0.8+0.667); M1 numerator = 1.0672 (or equivalent exact fraction 2x0.8x2/3); A2 F1 approx 0.727 (accept 0.727-0.728 from correct rounding at each stage).
6. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Introduction_to_Machine_Learning_and_AI` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 20 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_HCI_and_Professional_Ethical_Issues.
