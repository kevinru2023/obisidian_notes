---
title: "Logistic Regression & Perceptron"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L3.2 - Logistic regresson, Perceptron and Evaluating Classifiers.pdf]]"
  - "[[raw-sources/courses/CS434/ciml-v0_99-ch04.pdf]]"
  - "[[raw-sources/pdfs/NBayesLogReg.pdf]]"
related:
  - "[[wiki/courses/CS434]]"
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/concepts/linear-regression]]"
  - "[[wiki/concepts/gradient-descent]]"
  - "[[wiki/concepts/svm]]"
  - "[[wiki/concepts/naive-bayes]]"
  - "[[wiki/summaries/mitchell-nb-logreg]]"
updated: 2026-04-29
tags: [machine-learning, classification, logistic-regression, perceptron, CS434]
---

# Logistic Regression & Perceptron

Both are **linear classifiers** — their decision boundaries are hyperplanes (lines in 2D, planes in 3D).

---

## Logistic Regression

### Why Not Raw Linear Regression for Classification?

Using $w^\top x$ directly as a probability fails because:
- Output is unbounded — not in $[0, 1]$
- $P(y=1 \mid x) + P(y=0 \mid x) = 1$ not guaranteed

### The Model

Squash the linear output through the **sigmoid** $\sigma(z) = \dfrac{1}{1 + e^{-z}}$:

$$P(y=1 \mid x;\, w) = \sigma(w^\top x) = \frac{1}{1 + e^{-w^\top x}}$$

**Decision boundary**: predict $y=1$ if $P > 0.5$, i.e., when $w^\top x > 0$. The boundary $w^\top x = 0$ is a hyperplane.

(Convention: fold bias $b$ into $w$ by appending a constant $1$ feature to $x$.)

### Training via MLE / Cross-Entropy

MLE with a Bernoulli model gives the **binary cross-entropy loss**:

$$\mathcal{L}(w) = -\frac{1}{n} \sum_i \left[ y_i \log \sigma(w^\top x_i) + (1 - y_i) \log(1 - \sigma(w^\top x_i)) \right]$$

- Convex → gradient descent finds the global minimum
- No closed-form solution (unlike linear regression) — must use iterative optimization

**Gradient**:
$$\frac{\partial \mathcal{L}}{\partial w} = \frac{1}{n} \sum_i \left(\sigma(w^\top x_i) - y_i\right) x_i$$

**Gradient descent update**: $w \leftarrow w - \alpha \cdot \dfrac{\partial \mathcal{L}}{\partial w}$

### Comparison to Linear Regression

| | Linear Regression | Logistic Regression |
|---|---|---|
| Task | Regression | Binary classification |
| Output | $w^\top x \in (-\infty, +\infty)$ | $\sigma(w^\top x) \in (0, 1)$ |
| Loss | MSE | Binary cross-entropy |
| Solution | Closed-form | Gradient descent |
| Decision boundary | N/A | Linear hyperplane |

---

## Perceptron

A simpler, older linear classifier (CIML Ch. 4). Error-driven: only updates when it makes a mistake.

### Model

$$\hat{y} = \operatorname{sign}(w^\top x) \quad \text{(predicts } +1 \text{ or } -1\text{)}$$

### Update Rule

For each training example $(x, y)$:
- If $\operatorname{sign}(w^\top x) = y$ → correct, no update
- If $\operatorname{sign}(w^\top x) \ne y$ → **mistake**: $w \leftarrow w + y \cdot x$

**Intuition**: if we predicted wrong, shift $w$ in the direction of $y \cdot x$ to make the correct class more likely.

### Perceptron Convergence Theorem

If the data is **linearly separable** (there exists a perfect separating hyperplane with margin $\gamma$), then the perceptron converges in at most

$$\left(\frac{R}{\gamma}\right)^2 \text{ mistakes,} \quad R = \max_i \|x_i\|$$

If data is **not** linearly separable, the perceptron cycles forever and never converges.

### Perceptron vs Logistic Regression

| | Perceptron | Logistic Regression |
|---|---|---|
| Update trigger | Only on mistakes (error-driven) | Every example contributes to gradient |
| Output | Hard label ($\pm 1$) | Probability in $(0,1)$ |
| Convergence | Only if linearly separable | Always (convex loss) |
| Loss | Implicit (hinge-like) | Explicit cross-entropy |

---

## Evaluating Classifiers

Raw accuracy is misleading with class imbalance (e.g., 99% negative → always predict negative = 99% accuracy).

### Confusion Matrix

|  | Predicted Positive | Predicted Negative |
|--|---|---|
| **Actual Positive** | TP | FN |
| **Actual Negative** | FP | TN |

### Metrics

| Metric | Formula | Answers |
|--------|---------|---------|
| Accuracy | $\dfrac{TP+TN}{\text{total}}$ | Overall correctness |
| Precision | $\dfrac{TP}{TP+FP}$ | Of my positive predictions, how many are right? |
| Recall (Sensitivity) | $\dfrac{TP}{TP+FN}$ | Of all true positives, how many did I catch? |
| F1 Score | $\dfrac{2 \cdot P \cdot R}{P + R}$ | Harmonic mean of precision and recall |

**Precision-Recall tradeoff**: lowering the classification threshold increases recall (catch more positives) but decreases precision (more false alarms). Choose threshold based on the cost of FP vs FN in your application.

---

## Logistic Regression vs. Naive Bayes (Mitchell Ch. 3)

LR and Naive Bayes are the **discriminative/generative pair** for the same underlying model.

**Theorem (Mitchell):** Under Gaussian Naive Bayes assumptions — $P(X_i \mid Y = y_k) = \mathcal{N}(\mu_{ik}, \sigma_i)$ with equal variance across classes — the posterior $P(Y \mid X)$ is exactly the logistic form, with weights:

$$w_i = \frac{\mu_{i1} - \mu_{i0}}{\sigma_i^2}, \qquad w_0 = \sum_i \frac{\mu_{i0}^2 - \mu_{i1}^2}{2\sigma_i^2} + \log\frac{P(Y=1)}{P(Y=0)}$$

The same holds for Bernoulli Naive Bayes (boolean features) — the Bernoulli PMF trick collapses $P(X_i \mid Y)$ into a form whose log-ratio is linear in $x_i$.

| | Naive Bayes | Logistic Regression |
|---|---|---|
| Type | Generative | Discriminative |
| Estimates | $P(X \mid Y)$, $P(Y)$ | $P(Y \mid X)$ directly |
| Convergence speed | $O(\log n)$ examples | $O(n)$ examples |
| If NB assumptions hold | Same accuracy asymptotically | Same accuracy asymptotically |
| If NB assumptions fail | Higher bias | Better asymptotic accuracy |

**Practical rule (Ng & Jordan 2002):** prefer Naive Bayes with scarce data (converges faster), prefer Logistic Regression with abundant data (lower asymptotic error when independence assumption is violated).

See [[wiki/summaries/mitchell-nb-logreg]] for full derivation.
