---
title: "CS434 Review"
type: reference
sources:
  - "[[wiki/courses/CS434]]"
  - "[[wiki/concepts/knn]]"
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/concepts/linear-regression]]"
  - "[[wiki/concepts/gradient-descent]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/perceptron-convergence]]"
  - "[[wiki/concepts/regularization]]"
  - "[[wiki/concepts/naive-bayes]]"
  - "[[wiki/concepts/svm]]"
  - "[[wiki/concepts/kernel-methods]]"
related:
  - "[[wiki/courses/CS434]]"
updated: 2026-05-06
tags: [CS434, machine-learning, review]
---

# CS434 Review

## Quick-Reference Table

| Concept | Core Idea | Key Formula / Rule |
|---|---|---|
| kNN | Classify by majority vote of $k$ nearest neighbors | $f_k(x) = \operatorname{argmax}_y \sum_{i \in N_k(x)} \mathbf{1}[y_i = y]$ |
| MLE | Choose $\theta$ that maximizes data likelihood | $\theta_{\text{MLE}} = \operatorname{argmax}_\theta \sum_i \log P(x_i, y_i \mid \theta)$ |
| MAP | MLE + prior; prior becomes a regularizer | $\theta_{\text{MAP}} = \operatorname{argmax}_\theta [\log P(D \mid \theta) + \log P(\theta)]$ |
| Linear Regression | Minimize SSE; closed-form solution | $w^* = (X^\top X)^{-1} X^\top y$ |
| Ridge Regression | L2-regularized least squares | $w^* = (X^\top X + \lambda I)^{-1} X^\top y$ |
| Logistic Regression | Squash linear output to probability; minimize cross-entropy | $P(y=1 \mid x) = \sigma(w^\top x) = \frac{1}{1+e^{-w^\top x}}$ |
| Perceptron | Error-driven linear classifier; update only on mistakes | $w \leftarrow w + y \cdot x$ on mistake |
| Perceptron Convergence | Finite mistakes if linearly separable | $\leq R^2/\gamma^2$ mistakes |
| Naïve Bayes | Generative classifier; conditional independence per feature | $\hat{y} = \operatorname{argmax}_c P(y=c)\prod_i P(x_i \mid y=c)$ |
| Laplace Smoothing | Fix zero-probability problem | $P(x_i = v \mid y = c) = \frac{\text{count}(x_i=v, y=c) + \alpha}{\text{count}(y=c) + k\alpha}$ |
| Hard-Margin SVM | Max-margin linear classifier (separable data) | $\min \frac{1}{2}\mathbf{w}^\top\mathbf{w}$ s.t. $y_i(\mathbf{w}^\top\mathbf{x}_i + b) \geq 1$ |
| Soft-Margin SVM | Allows margin violations via slack ($C$ controls tradeoff) | $\min \frac{1}{2}\mathbf{w}^\top\mathbf{w} + C\sum_i \xi_i$ |
| Kernel Trick | Compute high-dim dot products implicitly | $\kappa(\mathbf{a},\mathbf{b}) = \Phi(\mathbf{a}) \cdot \Phi(\mathbf{b})$ |
| RBF Kernel | Infinite-dimensional dot product | $\kappa(\mathbf{a},\mathbf{b}) = \exp(-\gamma\|\mathbf{a}-\mathbf{b}\|^2)$ |
| Cross-Validation | Reliable hyperparameter tuning without touching test set | $K$ folds; rotate validation fold; average scores |

---

## ML Framework

**Definition:** Every supervised ML problem involves:
- **Dataset** $D = \{(x_i, y_i)\}$ — labeled training examples
- **Hypothesis space** $\mathcal{H}$ — functions the model can represent
- **Loss function** $\mathcal{L}$ — quantifies prediction error
- **Learning algorithm** $A$ — finds best $h \in \mathcal{H}$ minimizing $\mathcal{L}$

**Error decomposition:**

| Error type | Cause |
|---|---|
| **Bayes error** | Irreducible; inherent noise in true function |
| **Modelling error** | $\mathcal{H}$ not expressive enough (underfitting) |
| **Estimation error** | Finite data; best $h$ with $\infty$ data $\neq$ best $h$ on $D$ |
| **Optimization error** | Algorithm doesn't perfectly minimize loss |

**Golden rule of model selection:** Never use the test set for tuning. Split: train → validation → test. Report test results exactly once.

---

## k-Nearest Neighbors (kNN)

**Definition:** Non-parametric, lazy learner — no model built at training time; all computation happens at inference.

**Four choices define a kNN model:** distance metric, $k$, output function, weighting function (optional).

**Inference:** Given query $x$, find the $k$ nearest training points $N_k(x)$.

**Classification (majority vote):**
$$f_k(x) = \operatorname{argmax}_y \sum_{i \in N_k(x)} \mathbf{1}[y_i = y]$$

**Regression:**
$$f_k(x) = \frac{1}{k} \sum_{i \in N_k(x)} y_i$$

**Distance metrics:**

| Name                   | Formula                                |
| ---------------------- | -------------------------------------- |
| Euclidean ($L_2$)      | $\sqrt{\sum (x_i - z_i)^2}$            |
| Manhattan ($L_1$)      | $\sum x_i - z_i$                       |
| Chebyshev ($L_\infty$) | $\max_i x_i - z_i$                     |
| Minkowski ($L_p$)      | $\left(\sum x_i - z_i ^p\right)^{1/p}$ |

**Effect of $k$:**

| $k$ | Behavior |
|---|---|
| $k=1$ | Training error $= 0$; overfits; jagged boundary |
| $k=n$ | Predicts majority class everywhere; underfits |
| $1 < k < n$ | Smooth boundary; choose via cross-validation |

**Curse of Dimensionality:** In high dimensions, all points become roughly equidistant — the "nearby = similar" assumption breaks. Fraction of volume in outer shell of width $\varepsilon$:
$$1 - (1-\varepsilon)^d \to 1 \quad \text{as } d \to \infty$$

**Practical issues:** $O(nd)$ inference cost; must store all data; sensitive to irrelevant features and feature scale (always normalize).

**Common exam questions:**
- Why does $k=1$ achieve zero training error?
- What is the curse of dimensionality and why does it break kNN?
- How does increasing $k$ affect bias and variance?

**Gotchas:** Euclidean distance is dominated by high-variance features — normalize first. LOO cross-validation for kNN is cheap (just exclude each point from its own neighborhood).

**See also:** [[wiki/concepts/knn]]

---

## MLE and MAP

**Definition:** Frameworks for fitting model parameters $\theta$ from data.

**MLE — maximize likelihood:**
$$\theta_{\text{MLE}} = \operatorname{argmax}_\theta \sum_i \log P(x_i, y_i \mid \theta)$$

**MAP — maximize posterior (likelihood + prior):**
$$\theta_{\text{MAP}} = \operatorname{argmax}_\theta \left[\log P(D \mid \theta) + \log P(\theta)\right]$$

**Key connections:**

| Model assumption | MLE equivalent | MAP equivalent |
|---|---|---|
| $\varepsilon \sim \mathcal{N}(0, \sigma^2)$ noise | Minimizing SSE (linear regression) | L2-regularized regression |
| Bernoulli labels | Cross-entropy loss (logistic regression) | L2-regularized logistic regression |
| Gaussian prior on $\theta$ | — | Ridge ($L_2$) regularization |
| Laplace prior on $\theta$ | — | Lasso ($L_1$) regularization |

**MLE vs MAP:**

| | MLE | MAP |
|---|---|---|
| Maximizes | $P(D \mid \theta)$ | $P(\theta \mid D)$ |
| Regularization | None | Yes (log prior) |
| Risk | Overfits small data | More robust |

**Key insight:** Regularization is not arbitrary — it is MAP estimation with a specific prior. $\lambda$ reflects confidence in that prior.

**Common exam questions:**
- Derive that Gaussian noise → MSE loss.
- Show that a Gaussian prior on $w$ corresponds to L2 regularization.
- With large data, do MLE and MAP differ? Why?

**Gotchas:** MLE and MAP both give *point estimates*, not full distributions over $\theta$.

**See also:** [[wiki/concepts/mle-map]]

---

## Linear Regression

**Definition:** Fit $f(x) = w^\top x$ to minimize squared error on continuous targets.

**Objective (SSE):**
$$\mathcal{L}(w) = \sum_{i=1}^n (y_i - w^\top x_i)^2 = \|y - Xw\|^2$$

**Closed-form solution (normal equations):**
$$w^* = (X^\top X)^{-1} X^\top y$$

Setting $\nabla_w \mathcal{L} = 0$ and solving. Unique global minimum because SSE is convex.

**Ridge (L2) regularization:**
$$w^* = (X^\top X + \lambda I)^{-1} X^\top y$$

The $\lambda I$ term also fixes non-invertibility when $n < d$.

**Basis function extension:** Apply $\phi: \mathbb{R}^d \to \mathbb{R}^m$ and fit $f(x) = w^\top \phi(x)$. Still linear in $\phi(x)$, so closed form still applies. Common: polynomial $\phi(x) = [1, x, x^2, \ldots, x^p]$.

**MLE justification:** Assuming $y_i = w^\top x_i + \varepsilon_i$, $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$ i.i.d., maximizing $P(D \mid w)$ is exactly minimizing SSE.

**Common exam questions:**
- Derive the normal equations from $\nabla_w \mathcal{L} = 0$.
- Why does ridge fix the non-invertible $X^\top X$ case?
- When does linear regression fail as a classifier?

**Gotchas:** Fold the bias $b$ into $w$ by appending a constant $1$ feature to each $x$.

**See also:** [[wiki/concepts/linear-regression]]

---

## Gradient Descent

**Definition:** Iterative optimization algorithm for minimizing $\mathcal{L}(w)$ when no closed form exists.

**Update rule:**
$$w \leftarrow w - \alpha \cdot \nabla_w \mathcal{L}(w)$$

where $\alpha > 0$ is the learning rate. Repeat until convergence.

**Variants:**

| Variant | Uses | Pros | Cons |
|---|---|---|---|
| **Batch GD** | Full dataset | Stable; exact minimum (convex) | Slow on large $n$ |
| **SGD** | One random example | Fast; can escape local minima | Noisy |
| **Mini-batch GD** | Batch of size $B$ | Balance of speed + stability | Tune $B$ |

**Convexity guarantee:** If $\mathcal{L}$ is convex (e.g., logistic regression cross-entropy), gradient descent finds the global minimum regardless of initialization.

**Logistic regression gradient:**
$$\nabla_w \mathcal{L} = \frac{1}{n} \sum_i (\sigma(w^\top x_i) - y_i)\, x_i$$

**Learning rate sensitivity:** Too large → diverges/oscillates. Too small → converges very slowly.

**Common exam questions:**
- Why does batch GD guarantee a global minimum on logistic regression but not on neural networks?
- What happens if the learning rate is too large?

**See also:** [[wiki/concepts/gradient-descent]]

---

## Regularization

**Definition:** Prevent overfitting by penalizing large weights; balance data fit vs. model complexity.

**General form:**
$$w^* = \arg\min_w \; \mathcal{L}(w) + \lambda \cdot \text{Regularizer}(w)$$

**L2 (Ridge):**
$$w^* = \arg\min_w \; \|y - Xw\|^2 + \lambda\|w\|_2^2 \quad \Rightarrow \quad w^* = (X^\top X + \lambda I)^{-1} X^\top y$$

**L1 (Lasso):**
$$w^* = \arg\min_w \; \|y - Xw\|^2 + \lambda\|w\|_1$$
Yields sparse solutions (some $w_i = 0$ exactly); no closed form.

**Bayesian interpretation:**

| Regularizer | Equivalent prior | Method |
|---|---|---|
| $\lambda\|w\|_2^2$ | Gaussian: $w \sim \mathcal{N}(0, \beta I)$ | Ridge |
| $\lambda\|w\|_1$ | Laplace | Lasso |

**L1 vs L2 geometry:** L1 constraint region is a diamond (pointy corners on axes) — the loss contour tends to touch a corner where $w_i = 0$. L2's circular region is touched off-axis, so weights shrink but rarely zero out.

**Bias-Variance tradeoff:**

| $\lambda$ | Bias | Variance |
|---|---|---|
| High | High (underfit) | Low |
| Low | Low | High (overfit) |

**Common exam questions:**
- Why does L1 produce sparse solutions but L2 doesn't?
- Show that MAP with a Gaussian prior is equivalent to ridge regression.
- How do you choose $\lambda$?

**See also:** [[wiki/concepts/regularization]], [[wiki/concepts/mle-map]]

---

## Logistic Regression

**Definition:** Discriminative binary classifier. Squashes a linear function through a sigmoid to produce probabilities.

**Model:**
$$P(y=1 \mid x;\, w) = \sigma(w^\top x) = \frac{1}{1 + e^{-w^\top x}}$$

Decision boundary: $w^\top x = 0$ (hyperplane); predict $y=1$ if $P > 0.5$.

**Loss (binary cross-entropy via MLE):**
$$\mathcal{L}(w) = -\frac{1}{n} \sum_i \left[ y_i \log \sigma(w^\top x_i) + (1-y_i) \log(1 - \sigma(w^\top x_i)) \right]$$

Convex → gradient descent finds global minimum. No closed form.

**Gradient:**
$$\frac{\partial \mathcal{L}}{\partial w} = \frac{1}{n} \sum_i (\sigma(w^\top x_i) - y_i)\, x_i$$

**Logistic regression vs Naïve Bayes (Ng & Jordan 2002):**

| | Naïve Bayes | Logistic Regression |
|---|---|---|
| Type | Generative | Discriminative |
| Convergence speed | $O(\log n)$ examples | $O(n)$ examples |
| Asymptotic error | Higher (if NB assumptions fail) | Lower |

Prefer NB with scarce data; prefer LR with abundant data.

**Common exam questions:**
- Why can't we use raw linear regression for classification?
- Derive the logistic regression gradient.
- Under what conditions does NB and LR give the same asymptotic result?

**Gotchas:** Logistic regression models $P(y \mid x)$ directly (discriminative). It is not a generative model.

**See also:** [[wiki/concepts/logistic-regression]]

---

## Perceptron

**Definition:** Simpler linear classifier (labels $\pm 1$). Updates weights only when it makes a mistake.

**Prediction:**
$$\hat{y} = \operatorname{sign}(w^\top x)$$

**Update rule (on mistake):**
$$w \leftarrow w + y \cdot x$$

**Perceptron Convergence Theorem:** If data is linearly separable with margin $\gamma$ and $\|x_i\| \leq R$ for all $i$, the perceptron makes at most:
$$\frac{R^2}{\gamma^2} \text{ mistakes}$$

**Proof sketch:**
- **Lower bound on $\|\theta^{k+1}\|$:** By induction, $\theta^{k+1} \cdot \theta^* \geq k\gamma$, so $\|\theta^{k+1}\| \geq k\gamma$.
- **Upper bound on $\|\theta^{k+1}\|^2$:** On a mistake, $\|\theta^{k+1}\|^2 \leq \|\theta^k\|^2 + R^2$, so $\|\theta^{k+1}\|^2 \leq kR^2$.
- Combining: $k^2\gamma^2 \leq kR^2 \Rightarrow k \leq R^2/\gamma^2$.

The bound is independent of dimensionality and dataset size — only geometry matters.

**Perceptron vs Logistic Regression:**

| | Perceptron | Logistic Regression |
|---|---|---|
| Update trigger | Only on mistakes | Every example |
| Output | Hard label $(\pm 1)$ | Probability $(0,1)$ |
| Convergence | Only if linearly separable | Always (convex) |

**Common exam questions:**
- What happens to the perceptron if data is not linearly separable?
- Walk through the convergence proof (both bounds + combining).
- Why is the mistake bound independent of $d$ and $n$?

**See also:** [[wiki/concepts/perceptron-convergence]], [[wiki/concepts/logistic-regression]]

---

## Evaluating Classifiers

**Why accuracy isn't enough:** With imbalanced classes (99% negative), always predicting negative gives 99% accuracy while being useless.

**Confusion matrix:**

|  | Predicted Positive | Predicted Negative |
|--|---|---|
| **Actual Positive** | TP | FN |
| **Actual Negative** | FP | TN |

**Metrics:**

| Metric | Formula | Answers |
|---|---|---|
| Accuracy | $\frac{TP+TN}{\text{total}}$ | Overall correctness |
| Precision | $\frac{TP}{TP+FP}$ | Of my positive predictions, how many are right? |
| Recall | $\frac{TP}{TP+FN}$ | Of all true positives, how many did I catch? |
| F1 | $\frac{2 \cdot P \cdot R}{P + R}$ | Harmonic mean of precision & recall |

**Precision-recall tradeoff:** Lowering the classification threshold increases recall but decreases precision. Choose based on the relative cost of FP vs FN.

**K-fold cross-validation:** Split training data into $K$ folds; rotate which fold is validation; average performance. More reliable than single train/val split. LOO ($K=n$): expensive but unbiased.

**Common exam questions:**
- When does accuracy mislead? Give a concrete example.
- Compute precision, recall, and F1 from a confusion matrix.
- What is the precision-recall tradeoff? Which threshold direction increases recall?

---

## Naïve Bayes

**Definition:** Generative classifier. Learns $P(y)$ and $P(x_i \mid y)$ separately; predicts via Bayes' rule plus a conditional independence assumption.

**Naïve Bayes assumption:**
$$P(\mathbf{x} \mid y) = \prod_{i=1}^d P(x_i \mid y)$$

Reduces parameters from $O(c \cdot m^d)$ to $O(c \cdot d \cdot m)$.

**Prediction:**
$$\hat{y} = \operatorname{argmax}_c \; P(y=c) \prod_{i=1}^d P(x_i \mid y=c)$$

**Variants:**

| Variant | Feature type | $P(x_i \mid y)$ model |
|---|---|---|
| Bernoulli NB | Binary (0/1) | Bernoulli; models word *absence* |
| Multinomial NB | Integer counts | Multinomial; ignores absent words |
| Categorical NB | Discrete categories | Categorical |
| Gaussian NB | Continuous | $\mathcal{N}(\mu_{iy}, \sigma_{iy}^2)$ |

**Problem 1 — Zero probability:** If any $P(x_i \mid y=c) = 0$, the entire product is $0$.

**Fix — Laplace smoothing:** Add $\alpha$ fake counts to every value:
$$P(x_i = v \mid y = c) = \frac{\text{count}(x_i=v, y=c) + \alpha}{\text{count}(y=c) + k\alpha}$$

Equivalent to MAP with a Dirichlet($\alpha$) prior. Standard: $\alpha = 1$.

**Problem 2 — Numerical underflow:** Products of many small probabilities underflow to zero.

**Fix — Log space:**
$$\hat{y} = \operatorname{argmax}_c \left[\log P(y=c) + \sum_i \log P(x_i \mid y=c)\right]$$

**Why NB works despite false independence:**
1. Only the argmax matters — probabilities don't need to be accurate for classification to be correct.
2. Estimating 1D conditionals avoids the curse of dimensionality.

**Generative vs discriminative:**

| | NB | LR |
|---|---|---|
| Type | Generative | Discriminative |
| Convergence speed | $O(\log n)$ | $O(n)$ |
| Asymptotic error | Higher (if independence fails) | Lower |

**Common exam questions:**
- Compute $\hat{y}$ from a table of counts, with and without Laplace smoothing.
- What parameter count does NB reduce from/to, and why?
- Why does NB produce overconfident probabilities but still classify well?
- Bernoulli vs Multinomial NB — what's the difference?

**Gotchas:** Bernoulli and Multinomial NB are not interchangeable. Bernoulli explicitly penalizes absent words; Multinomial ignores them.

**See also:** [[wiki/concepts/naive-bayes]]

---

## Support Vector Machines (SVM)

**Definition:** Supervised linear classifier that finds the decision boundary maximizing the margin.

**Margin:** distance from the boundary to the nearest training example.

### Hard-Margin SVM (linearly separable)

**Primal:**
$$\min_{\mathbf{w},b}\ \frac{1}{2}\mathbf{w}^\top\mathbf{w} \quad \text{s.t.} \quad y_i(\mathbf{w}^\top\mathbf{x}_i + b) \geq 1\ \forall i$$

Minimizing $\|\mathbf{w}\|$ maximizes the margin $\frac{1}{\|\mathbf{w}\|}$. The constraints keep all points outside the margin band.

**Support vectors:** Points on the margin ($y_i(\mathbf{w}^\top\mathbf{x}_i+b)=1$). Only support vectors influence $\mathbf{w}^*$:
$$\mathbf{w}^* = \sum_i \alpha_i^* y_i \mathbf{x}_i \quad (\alpha_i^* > 0 \text{ only for SVs})$$

**Class balance constraint:** $\sum_i \alpha_i y_i = 0$.

**Dual:**
$$\max_\alpha \sum_i \alpha_i - \frac{1}{2}\sum_i\sum_j \alpha_i\alpha_j y_i y_j \mathbf{x}_i^\top\mathbf{x}_j \quad \text{s.t.} \sum_i \alpha_i y_i = 0,\ \alpha_i \geq 0$$

### Soft-Margin SVM (non-separable)

**Slack variables** $\xi_i \geq 0$ allow margin violations:

**Primal:**
$$\min_{\mathbf{w},b,\xi}\ \frac{1}{2}\mathbf{w}^\top\mathbf{w} + C\sum_i \xi_i \quad \text{s.t.} \quad y_i(\mathbf{w}^\top\mathbf{x}_i+b) \geq 1-\xi_i,\ \xi_i \geq 0$$

**Hyperparameter $C$:**

| $C$ | Effect |
|---|---|
| $C \to 0$ | Violations unpenalized; margin grows wide |
| $C \to \infty$ | Violations heavily penalized; recovers hard-margin |

**Dual:** Same as hard-margin but $0 \leq \alpha_i \leq C$.

**ERM / Hinge loss view:** Soft-margin SVM minimizes:
$$\frac{1}{n}\sum_i \max(0, 1 - y_i(\mathbf{w}^\top\mathbf{x}_i - b)) + \lambda\|\mathbf{w}\|^2$$

Hinge loss $\ell(y,z) = \max(0, 1-yz)$. SVM, logistic regression, and least-squares differ only in loss function (hinge, log, square).

**Common exam questions:**
- Write the primal and dual for hard-margin SVM.
- What is a support vector, and what happens to non-support-vector points?
- How does $C$ affect the margin and error tolerance?
- Show how the dual depends only on dot products (motivation for kernel trick).

**Gotchas:** Hard-margin SVM requires linear separability. If not, use soft-margin. The dual formulation replaces $n$-dimensional $\mathbf{w}$ with $n$ scalars $\alpha_i$ — this is the entry point for kernels.

**See also:** [[wiki/concepts/svm]]

---

## Kernel Methods

**Definition:** Basis function maps $\Phi: \mathbb{R}^d \to \mathbb{R}^{d'}$ enable nonlinear decision boundaries; the kernel trick computes $\Phi(\mathbf{a}) \cdot \Phi(\mathbf{b})$ without ever forming $\Phi$ explicitly.

**Motivation:** Polynomial expansion of degree $p$ over $d$ features has $O(d^p)$ dimensions — intractable. But many algorithms only need pairwise dot products.

**Kernel definition:**
$$\kappa(\mathbf{a},\mathbf{b}) = \Phi(\mathbf{a}) \cdot \Phi(\mathbf{b})$$

Computed in $O(d)$ instead of $O(d^p)$.

**Example — Quadratic kernel:** $({\mathbf{a} \cdot \mathbf{b}} + 1)^2 = \Phi(\mathbf{a}) \cdot \Phi(\mathbf{b})$ for the quadratic feature map.

**Mercer's Theorem:** $\kappa$ is a valid kernel iff the Gram matrix $K_{ij} = \kappa(\mathbf{x}_i, \mathbf{x}_j)$ is **positive semidefinite** for any finite sample. Necessary and sufficient condition.

**Common kernels:**

| Kernel | Formula | Notes |
|---|---|---|
| Linear | $\mathbf{a} \cdot \mathbf{b}$ | No transformation |
| Polynomial (inhomogeneous) | $(\mathbf{a} \cdot \mathbf{b} + 1)^p$ | Degree-$p$ features |
| RBF / Gaussian | $\exp(-\gamma\|\mathbf{a}-\mathbf{b}\|^2)$ | Infinite-dimensional; most common default |
| Sigmoid | $\tanh(\kappa\, \mathbf{a} \cdot \mathbf{b} + c)$ | Not always PSD — use cautiously |

**Closure properties:** Sums, products, positive scalings, and exponentials of valid kernels are valid kernels.

### Kernel SVM

Replace $\mathbf{x}_i^\top\mathbf{x}_j$ with $\kappa(\mathbf{x}_i, \mathbf{x}_j)$ in the dual:

$$\max_\alpha \sum_i \alpha_i - \frac{1}{2}\sum_i\sum_j \alpha_i\alpha_j y_i y_j\, \kappa(\mathbf{x}_i,\mathbf{x}_j) \quad \text{s.t.} \sum_i \alpha_i y_i = 0,\ 0 \leq \alpha_i \leq C$$

**Prediction:** $\hat{y} = \operatorname{sgn}\!\left(\sum_i \alpha_i y_i\, \kappa(\mathbf{x}_i, \mathbf{z}) - b\right)$ — no explicit $\mathbf{w}$.

### Kernelized Perceptron

After $t$ mistakes, $\mathbf{w}_t = \sum_i c_i y_i \mathbf{x}_i$ where $c_i$ counts misclassifications of example $i$.

**Prediction:** $\hat{y}_j = \operatorname{sgn}\!\left(\sum_i c_i y_i\, \kappa(\mathbf{x}_i, \mathbf{x}_j)\right)$

**Update on mistake:** $c_j \mathrel{+}= 1$ (increment count, no explicit weight update).

### Kernel Ridge Regression

**Dual solution:** $\boldsymbol{\alpha} = (K + \lambda I)^{-1} \mathbf{y}$ where $K$ is the $n \times n$ Gram matrix.

**Prediction:** $\hat{y} = \sum_i \alpha_i\, \kappa(\mathbf{x}_i, \mathbf{x})$

Inverts $n \times n$ instead of $d' \times d'$ — advantageous when $d' \gg n$.

**Common exam questions:**
- What is the kernel trick? What problem does it solve?
- Verify that $({\mathbf{a} \cdot \mathbf{b}} + 1)^2$ is a kernel by matching it to a feature map $\Phi$.
- State Mercer's theorem. Why do we need it?
- What does the RBF kernel's $\Phi$ look like?
- How do you kernelize the perceptron? What replaces the weight vector?

**Gotchas:** The RBF kernel corresponds to an **infinite-dimensional** feature space — you cannot write $\Phi$ explicitly, but the kernel is still valid. The sigmoid kernel is not always PSD and must be used cautiously.

**See also:** [[wiki/concepts/kernel-methods]], [[wiki/concepts/svm]]

---

## Concept Connections

The course follows a natural progression from instance-based to parametric to margin-based to kernel methods:

1. **kNN** is the baseline: no parameters, no training, just memorized data. Its failure in high dimensions motivates parametric models.

2. **MLE/MAP** is the statistical foundation underpinning every parametric model. MLE → least squares (linear regression) when noise is Gaussian. MAP → regularization when you have a prior on weights.

3. **Linear Regression** (continuous output) and **Logistic Regression** (classification) share the same linear structure $w^\top x$, differing only in output transform (identity vs sigmoid) and loss (MSE vs cross-entropy). Both optimize via gradient descent; linear regression has a closed form.

4. **Regularization** (Ridge/Lasso) is L2/L1 MAP. Ridge has a closed form and prevents non-invertibility. Lasso produces sparse solutions via geometry.

5. **Perceptron** simplifies logistic regression by only updating on mistakes. The convergence theorem gives a geometry-based mistake bound; it only works when data is linearly separable.

6. **Naïve Bayes** flips the paradigm: instead of modeling $P(y \mid x)$ directly (discriminative), it models $P(x \mid y)$ and $P(y)$ (generative) and uses Bayes' rule to classify. NB and logistic regression are the canonical generative-discriminative pair — NB converges faster; LR has lower asymptotic error when independence fails.

7. **SVM** brings margin maximization: the goal isn't just to classify correctly, but to do so with the largest possible margin. The dual formulation naturally depends only on dot products, which motivates kernels. $C$ (soft-margin) is analogous to $\lambda$ (regularization strength).

8. **Kernel methods** extend all preceding dot-product-based algorithms (SVM, perceptron, ridge regression) to nonlinear decision boundaries without explicit high-dimensional feature maps. The kernel trick is the key enabling idea; Mercer's theorem validates which functions can serve as kernels.

---

## Practice Questions

1. You train a kNN classifier with $k=1$ on 1000 examples. Training accuracy is 100% but test accuracy is 60%. Explain what is happening and what you should try.

2. Derive the normal equations for linear regression. What is the statistical justification for using MSE loss?

3. You have a two-class dataset where 95% of examples are negative. Your model achieves 95% accuracy. Is this a good model? Compute precision and recall if it always predicts negative.

4. Logistic regression and Naïve Bayes are called a "generative-discriminative pair." Explain what this means and when you would prefer each.

5. A soft-margin SVM with a very small $C$ is trained on data that is not linearly separable. Describe the resulting decision boundary qualitatively. What if $C$ is very large?

6. Explain why the perceptron convergence theorem's mistake bound is finite. What happens if the data is not linearly separable?

7. Show that MAP estimation with a Gaussian prior on $w$ leads to L2-regularized loss. What prior leads to L1 (Lasso)?

8. You want to apply SVM to data that lies on a nonlinear manifold. Describe step-by-step how you would use a kernel SVM, including how training and prediction work without ever computing $\Phi(\mathbf{x})$ explicitly.

9. The RBF kernel corresponds to an infinite-dimensional feature space. How is this possible, and why does it still satisfy Mercer's theorem?

10. You are kernelizing the perceptron. What replaces the explicit weight vector $\mathbf{w}$? Write out the kernelized prediction and update rules.
