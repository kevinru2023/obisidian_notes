---
title: "Support Vector Machines"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L5.1 - Support Vector Machines_update.pdf]]"
  - "[[raw-sources/web-clippings/Support vector machine.md]]"
related:
  - "[[wiki/courses/CS434]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/regularization]]"
  - "[[wiki/summaries/svm-wikipedia]]"
  - "[[wiki/concepts/kernel-methods]]"
updated: 2026-05-04
tags: [CS434, machine-learning, classification, optimization]
---

# Support Vector Machines (SVM)

**Type:** Supervised linear classifier  
**Key idea:** Find the decision boundary that maximizes the *margin* — the distance between the boundary and the nearest training example of each class.

---

## Margin Definition

For a linear classifier $\mathbf{w}^\top \mathbf{x} + b = 0$, the distance from point $\mathbf{x}_i$ to the boundary is:

$$d = \frac{|\mathbf{w}^\top \mathbf{x}_i + b|}{||\mathbf{w}||}$$

The margin of the classifier is determined by the *nearest* point:

$$d_{\min} = \min_i \frac{|\mathbf{w}^\top \mathbf{x}_i + b|}{||\mathbf{w}||}$$

---

## Hard-Margin SVM

Assumes data is **linearly separable**. Uses labels $y \in \{-1, +1\}$.

### Primal Formulation

Normalize $\mathbf{w}, b$ so that the minimum margin numerator equals 1 (always possible by scaling). Then:

$$\min_{\mathbf{w},b}\ \frac{1}{2}\mathbf{w}^\top \mathbf{w}$$

$$\text{s.t.}\ y_i(\mathbf{w}^\top \mathbf{x}_i + b) \geq 1\ \forall i$$

Minimizing $||\mathbf{w}||$ is equivalent to maximizing the margin $\frac{1}{||\mathbf{w}||}$. The constraints prevent any point from entering the margin region between $\mathbf{w}^\top \mathbf{x} + b = \pm 1$.

This is a **quadratic program** (QP): quadratic objective with linear constraints — solvable by standard QP solvers.

### Support Vectors

At the optimal solution:
- **Tight constraints** ($y_i(\mathbf{w}^\top \mathbf{x}_i + b) = 1$): these points lie *on* the margin lines — called **support vectors**
- **Slack constraints** ($y_i(\mathbf{w}^\top \mathbf{x}_i + b) > 1$): interior points; do not influence the solution

The optimal weight vector is a sparse linear combination of only the support vectors:

$$\mathbf{w}^* = \sum_{i=1}^{n} \alpha_i^*\, y_i \mathbf{x}_i \quad \text{where } \alpha_i^* > 0 \text{ only for support vectors}$$

**Class balance constraint** (from the dual):

$$\sum_i \alpha_i y_i = 0$$

The positive and negative support vector weights must sum to the same value.

### Dual Formulation

$$\max_{\alpha}\ \sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_i\sum_j \alpha_i \alpha_j y_i y_j \mathbf{x}_i^\top \mathbf{x}_j$$

$$\text{s.t.}\ \sum_i \alpha_i y_i = 0,\quad \alpha_i \geq 0\ \forall i$$

The dual expresses the problem in terms of inner products $\mathbf{x}_i^\top \mathbf{x}_j$ — this is the entry point for the **kernel trick** (coming later).

---

## Soft-Margin SVM

Handles **non-linearly separable** data by allowing some examples to violate the margin constraints.

### Slack Variables

Each example gets a slack variable $\xi_i \geq 0$ representing how much it is allowed to violate the margin:

$$y_i(\mathbf{w}^\top \mathbf{x}_i + b) \geq 1 - \xi_i\ \forall i$$

### Primal Formulation

$$\min_{\mathbf{w},b,\xi}\ \frac{1}{2}\mathbf{w}^\top \mathbf{w} + C \sum_i \xi_i$$

$$\text{s.t.}\ y_i(\mathbf{w}^\top \mathbf{x}_i + b) \geq 1 - \xi_i\ \forall i,\quad \xi_i \geq 0$$

- $\frac{1}{2}\mathbf{w}^\top \mathbf{w}$: maximize margin
- $C \sum_i \xi_i$: penalize margin violations

### Hyperparameter C (Slack Penalty)

| $C$ | Effect |
|-----|--------|
| $C \to 0$ | Errors unpenalized → margin grows arbitrarily wide |
| $C \to \infty$ | Errors heavily penalized → recovers hard-margin SVM |

$C$ is selected via cross-validation.

### Solution Characteristics

Support vectors for soft-margin SVM:
- **Case 1** ($\xi_i = 0$): on the margin
- **Case 2** ($\xi_i > 0$): inside margin or misclassified

$$\mathbf{w}^* = \sum_i \alpha_i y_i \mathbf{x}_i, \quad 0 \leq \alpha_i \leq C$$

### Dual Formulation

Identical to hard-margin except for the upper bound on $\alpha_i$:

$$\max_{\alpha}\ \sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_i\sum_j \alpha_i \alpha_j y_i y_j \mathbf{x}_i^\top \mathbf{x}_j$$

$$\text{s.t.}\ \sum_i \alpha_i y_i = 0,\quad 0 \leq \alpha_i \leq C\ \forall i$$

---

## Hard vs. Soft Margin — Quick Comparison

| | Hard-Margin | Soft-Margin |
|--|--|--|
| **Separability** | Requires linear separability | Handles non-separable data |
| **Constraint** | $y_i(\mathbf{w}^\top \mathbf{x}_i+b) \geq 1$ | $y_i(\mathbf{w}^\top \mathbf{x}_i+b) \geq 1 - \xi_i$ |
| **Dual $\alpha$ bounds** | $\alpha_i \geq 0$ | $0 \leq \alpha_i \leq C$ |
| **Hyperparameter** | None | $C$ (slack penalty) |

---

## Quadratic Programming (QP) Note

Both primal formulations map to the standard QP form:

$$\min_{\mathbf{z}}\ \frac{1}{2}\mathbf{z}^\top P \mathbf{z} + \mathbf{q}^\top \mathbf{z} \quad \text{s.t.}\ G\mathbf{z} \leq \mathbf{h},\quad A\mathbf{z} = \mathbf{b}$$

For hard-margin SVM: $\mathbf{z} = [\mathbf{w};\ b]$, $P$ has identity block for $\mathbf{w}$ and 0 for $b$, $G$ encodes the $-y_i(\mathbf{w}^\top\mathbf{x}_i+b)$ constraints. Off-the-shelf QP solvers find the global optimum.

---

## Kernel Trick

The dual objective depends only on pairwise dot products $\mathbf{x}_i^\top \mathbf{x}_j$. Replacing each dot product with a kernel function $k(\mathbf{x}_i, \mathbf{x}_j) = \varphi(\mathbf{x}_i) \cdot \varphi(\mathbf{x}_j)$ implicitly maps data into a (possibly infinite-dimensional) feature space without computing $\varphi$ explicitly. This enables **nonlinear decision boundaries** in the original space.

The kernelized dual:

$$\max_{\alpha}\ \sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_i\sum_j \alpha_i \alpha_j y_i y_j\, k(\mathbf{x}_i, \mathbf{x}_j)$$

$$\text{s.t.}\ \sum_i \alpha_i y_i = 0,\quad 0 \leq \alpha_i \leq C\ \forall i$$

Classifier:

$$\mathbf{z} \mapsto \operatorname{sgn}\!\left(\sum_i \alpha_i y_i\, k(\mathbf{x}_i, \mathbf{z}) - b\right)$$

### Common Kernels

| Kernel | Formula |
|--------|---------|
| Linear | $k(\mathbf{x}_i, \mathbf{x}_j) = \mathbf{x}_i \cdot \mathbf{x}_j$ |
| Polynomial (homogeneous) | $k(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i \cdot \mathbf{x}_j)^d$ |
| Polynomial (inhomogeneous) | $k(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i \cdot \mathbf{x}_j + r)^d$ |
| RBF / Gaussian | $k(\mathbf{x}_i, \mathbf{x}_j) = \exp\!\left(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2\right)$, $\gamma > 0$ |
| Sigmoid | $k(\mathbf{x}_i, \mathbf{x}_j) = \tanh(\kappa\, \mathbf{x}_i \cdot \mathbf{x}_j + c)$ |

RBF is the most common default; its single parameter $\gamma$ and the soft-margin $C$ are selected jointly via grid search with cross-validation.

---

## ERM / Hinge Loss View

Soft-margin SVM is equivalent to **empirical risk minimization with Tikhonov regularization** using the hinge loss:

$$\ell(y, z) = \max(0, 1 - yz)$$

The full objective:

$$\left[\frac{1}{n}\sum_{i=1}^n \max(0, 1 - y_i(\mathbf{w}^\top \mathbf{x}_i - b))\right] + \lambda\|\mathbf{w}\|^2$$

This places SVM in the same family as logistic regression and regularized least-squares — differing only in loss function:

| Method | Loss |
|--------|------|
| SVM | Hinge: $\max(0, 1-yz)$ |
| Logistic regression | Log: $\ln(1 + e^{-yz})$ |
| Regularized least-squares | Square: $(y-z)^2$ |

The hinge loss target function is exactly the Bayes-optimal classifier $f^*(x)$, so SVM converges to the simplest correctly-classifying function. Logistic and square losses converge to richer functions that encode full probability estimates.

---

## Multiclass SVM

Binary by default. Standard reductions:
- **One-vs-all:** $k$ classifiers; winner-takes-all
- **One-vs-one:** $\binom{k}{2}$ classifiers; max-wins voting
- **Crammer & Singer:** single joint optimization (avoids decomposition)

---

## Support Vector Regression (SVR)

Extends SVM to regression. Minimizes $\frac{1}{2}\|w\|^2$ subject to all predictions being within an $\varepsilon$-tube of the target:

$$|y_i - \langle w, x_i\rangle - b| \leq \varepsilon$$

Slack variables allow violations when the tube constraint is infeasible.
