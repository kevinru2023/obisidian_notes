---
title: "Gradient Descent"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L3.2 - Logistic regresson, Perceptron and Evaluating Classifiers.pdf]]"
related:
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/courses/CS434]]"
updated: 2026-04-21
tags: [machine-learning, optimization, gradient-descent, CS434]
---

# Gradient Descent

Gradient descent is the standard iterative algorithm for minimizing a differentiable loss function $\mathcal{L}(w)$ when no closed-form solution exists (e.g., logistic regression, neural networks).

---

## Core Idea

The gradient $\nabla_w \mathcal{L}$ points in the direction of steepest increase. Moving opposite to it descends the loss:

$$w \leftarrow w - \alpha \cdot \nabla_w \mathcal{L}(w)$$

where $\alpha > 0$ is the **learning rate** (step size).

Repeat until convergence (gradient is near zero, or loss stops decreasing).

---

## Variants

| Variant | Update uses | Pros | Cons |
|---|---|---|---|
| **Batch GD** | Full dataset gradient | Stable; converges to exact minimum (convex) | Slow per step on large $n$ |
| **Stochastic GD (SGD)** | One random example | Fast per step; can escape local minima | Noisy; needs learning rate schedule |
| **Mini-batch GD** | Random subset of size $B$ | Balance of speed and stability | Tuning batch size $B$ |

In practice mini-batch GD (usually called "SGD" in ML frameworks) is standard.

---

## Learning Rate Sensitivity

- **Too large $\alpha$**: overshoots the minimum, diverges or oscillates.
- **Too small $\alpha$**: converges, but very slowly.
- **Typical approach**: start with a moderate $\alpha$, decay it over training (learning rate schedule), or use an adaptive optimizer (Adam, RMSProp).

---

## Convexity Guarantee

If $\mathcal{L}$ is **convex**, gradient descent finds the global minimum regardless of initialization. Logistic regression's cross-entropy loss is convex — so gradient descent is guaranteed to converge to the optimal $w^*$.

Non-convex losses (neural networks) have local minima and saddle points, but gradient descent still works well in practice.

---

## Worked Example: Logistic Regression

Loss: $\mathcal{L}(w) = -\frac{1}{n} \sum_i \left[ y_i \log \sigma(w^\top x_i) + (1-y_i) \log(1 - \sigma(w^\top x_i)) \right]$

Gradient: $\nabla_w \mathcal{L} = \frac{1}{n} \sum_i (\sigma(w^\top x_i) - y_i)\, x_i$

Update: $w \leftarrow w - \alpha \cdot \frac{1}{n} \sum_i (\hat{y}_i - y_i)\, x_i$

See [[wiki/concepts/logistic-regression]] for the full derivation.
