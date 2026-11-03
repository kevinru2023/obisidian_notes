---
title: "Kernel Methods"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L6.1 - kernel functions.pdf]]"
related:
  - "[[wiki/concepts/svm]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/linear-regression]]"
  - "[[wiki/courses/CS434]]"
updated: 2026-05-04
tags: [CS434, machine-learning, kernel-trick, svm]
---

# Kernel Methods

---

## Motivation: Basis Functions

Many real-world problems are not linearly separable in the original feature space. A natural fix: **map inputs into a higher-dimensional space** where a linear boundary can separate them.

**Basis function mapping** $\Phi: \mathbb{R}^d \to \mathbb{R}^{d'}$:

- Replace every $\mathbf{x}_i$ with $\Phi(\mathbf{x}_i)$
- Solve the same linear model (regression, SVM, perceptron) in the new space
- Prediction for a new point: compute $\Phi(\mathbf{x})$, then apply the learned weights

**Example:** Polynomial regression in 1D — $\Phi(x) = [1, x, x^2, x^3, \ldots]$. The model stays linear in $\Phi(x)$; the decision boundary is nonlinear in $x$.

**Problem:** The feature space grows fast. For $d$-dimensional input and a degree-2 polynomial map, $d' = O(d^2)$ — over 7,000 dimensions for HW1's data. Higher-order maps make this worse.

**Key insight:** Many algorithms only ever access $\Phi(\mathbf{x}_i) \cdot \Phi(\mathbf{x}_j)$ (dot products between mapped points). If we can compute this dot product efficiently *without* forming $\Phi(\mathbf{x})$ explicitly, we get the representational power without the computational cost.

---

## The Kernel Trick

**Definition:** A function $\kappa(\mathbf{a}, \mathbf{b})$ is a **kernel function** if there exists a mapping $\Phi$ such that:

$$\kappa(\mathbf{a}, \mathbf{b}) = \Phi(\mathbf{a}) \cdot \Phi(\mathbf{b})$$

A kernel function computes the dot product in the high-dimensional mapped space **directly in the original space** — without computing $\Phi$ explicitly.

**Example — Quadratic kernel:** For $\mathbf{a}, \mathbf{b} \in \mathbb{R}^d$:

$$(\mathbf{a} \cdot \mathbf{b} + 1)^2 = 1 + 2\mathbf{a} \cdot \mathbf{b} + (\mathbf{a} \cdot \mathbf{b})^2$$

This equals $\Phi(\mathbf{a}) \cdot \Phi(\mathbf{b})$ for the quadratic feature map $\Phi$, computed in $O(d)$ operations vs. $O(d^2)$ for the explicit approach.

---

## What Functions Are Valid Kernels?

**Mercer's Theorem:** A function $\kappa$ is a valid kernel if and only if, for any finite sample $\mathbf{x}_1, \ldots, \mathbf{x}_n$, the **kernel (Gram) matrix** $K$ is **positive semidefinite** (all eigenvalues $\geq 0$):

$$K_{ij} = \kappa(\mathbf{x}_i, \mathbf{x}_j)$$

Kernel matrices are always square and symmetric. Positive semidefiniteness is the necessary and sufficient condition.

Not every similarity function is a valid kernel — if the Gram matrix has negative eigenvalues, the function has no corresponding $\Phi$.

---

## Closure Properties

If $\kappa_1$ and $\kappa_2$ are valid kernels, so are:

| Expression | Notes |
|---|---|
| $\kappa_1(\mathbf{a},\mathbf{b}) + \kappa_2(\mathbf{a},\mathbf{b})$ | Sum of kernels |
| $c \cdot \kappa_1(\mathbf{a},\mathbf{b})$ for $c > 0$ | Positive scalar multiple |
| $\kappa_1(\mathbf{a},\mathbf{b}) \cdot \kappa_2(\mathbf{a},\mathbf{b})$ | Product of kernels |
| $f(\mathbf{a})\, \kappa_1(\mathbf{a},\mathbf{b})\, f(\mathbf{b})$ for any function $f$ | Scaling by arbitrary function |
| $\exp(\kappa_1(\mathbf{a},\mathbf{b}))$ | Exponentiated kernel |

These properties let you construct complex kernels from simple ones.

---

## Common Kernels

| Kernel | Formula | Notes |
|---|---|---|
| Linear | $\kappa(\mathbf{a},\mathbf{b}) = \mathbf{a} \cdot \mathbf{b}$ | No transformation; baseline |
| Polynomial (inhomogeneous) | $\kappa(\mathbf{a},\mathbf{b}) = (\mathbf{a} \cdot \mathbf{b} + 1)^p$ | Degree-$p$ features; $\sqrt{2}$ scaling in $\Phi$ handles cross-terms |
| RBF / Gaussian | $\kappa(\mathbf{a},\mathbf{b}) = \exp\!\left(-\gamma \|\mathbf{a}-\mathbf{b}\|^2\right)$ | Corresponds to **infinite-dimensional** dot product |
| Sigmoid | $\kappa(\mathbf{a},\mathbf{b}) = \tanh(\kappa\, \mathbf{a} \cdot \mathbf{b} + c)$ | Not always PSD; use cautiously |

**RBF proof sketch:** Using $e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$ and expanding $\|\mathbf{a}-\mathbf{b}\|^2$, the RBF kernel can be written as an infinite sum of polynomial kernels — so its corresponding $\Phi$ maps into infinite-dimensional space.

In practice, kernels are used directly without ever specifying $\Phi$.

---

## Kernel SVM

The SVM dual depends only on pairwise dot products. Replace $\mathbf{x}_i^\top \mathbf{x}_j$ with $\kappa(\mathbf{x}_i, \mathbf{x}_j)$:

**Soft-margin Kernel SVM Dual:**

$$\max_{\alpha}\ \sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_i\sum_j \alpha_i \alpha_j y_i y_j\, \kappa(\mathbf{x}_i, \mathbf{x}_j)$$

$$\text{s.t.}\ \sum_i \alpha_i y_i = 0,\quad 0 \leq \alpha_i \leq C\ \forall i$$

**Prediction:**

$$\hat{y} = \operatorname{sgn}\!\left(\sum_i \alpha_i y_i\, \kappa(\mathbf{x}_i, \mathbf{z}) - b\right)$$

No $\mathbf{w}$ vector is ever explicitly formed — the model lives entirely in the $\alpha_i$ coefficients and the training data.

---

## Kernelizing the Perceptron

**Key observation:** After $t$ misclassifications, the perceptron weight vector is a sum of misclassified training examples:

$$\mathbf{w}_t = \sum_{m \in M} y_m \mathbf{x}_m$$

where $M$ is the list of misclassification indices. This means $\mathbf{w}$ always lies in the span of the training data.

**Kernelized form:** Track a count vector $\mathbf{c} \in \mathbb{R}^n$ where $c_i$ counts how many times example $i$ was misclassified:

$$\mathbf{w}_t = \sum_{i=1}^n c_i y_i \mathbf{x}_i$$

Rewrite the prediction and update entirely in terms of dot products:

**Kernelized prediction:**

$$\hat{y}_j = \operatorname{sgn}\!\left(\mathbf{w}_t^\top \mathbf{x}_j\right) = \operatorname{sgn}\!\left(\sum_{i=1}^n c_i y_i\, \kappa(\mathbf{x}_i, \mathbf{x}_j)\right)$$

**Update:** if $\hat{y}_j \neq y_j$, increment $c_j \mathrel{+}= 1$ (no explicit weight vector update).

Both training and prediction are expressed entirely as kernel evaluations.

---

## Kernel Ridge Regression

**L2-regularized linear regression** closed-form solution:

$$\mathbf{w} = (X^\top X + \lambda I)^{-1} X^\top \mathbf{y}$$

Because $\mathbf{w}$ lies in the span of the training data ($\mathbf{w} = \sum_i \alpha_i \mathbf{x}_i = X^\top \boldsymbol{\alpha}$), we can reparametrize in terms of $\boldsymbol{\alpha}$:

| | Original (primal) | Kernel (dual) |
|---|---|---|
| **Predict** | $\hat{y} = \mathbf{w}^\top \mathbf{x}$ | $\hat{y} = \sum_{i=1}^n \alpha_i\, \kappa(\mathbf{x}_i, \mathbf{x})$ |
| **Objective** | $\|\mathbf{y} - X\mathbf{w}\|^2 + \lambda\|\mathbf{w}\|^2$ | $\|\mathbf{y} - K\boldsymbol{\alpha}\|^2 + \lambda\, \boldsymbol{\alpha}^\top K \boldsymbol{\alpha}$ |
| **Solution** | $(X^\top X + \lambda I)^{-1} X^\top \mathbf{y}$ | $(K + \lambda I)^{-1} \mathbf{y}$ |

where $K$ is the $n \times n$ kernel Gram matrix. The dual solution inverts an $n \times n$ matrix instead of $d' \times d'$, which is advantageous when $d' \gg n$.

---

## Summary

| | Original | Kernelized |
|---|---|---|
| **Representation** | Explicit $\Phi(\mathbf{x}) \in \mathbb{R}^{d'}$ | Implicit via $\kappa(\mathbf{x}_i, \mathbf{x}_j)$ |
| **Cost of similarity** | $O(d')$ — can be $O(d^p)$ | $O(d)$ for most kernels |
| **Enables** | Linear boundary in $\mathbb{R}^{d'}$ | Nonlinear boundary in $\mathbb{R}^d$ |
| **Models** | SVM, perceptron, regression, PCA, … | All of the above, via dual formulation |

The kernel trick was the dominant technique in ML through the 1990s–2000s ("everything that could be kernelized was kernelized"). It has since been partially displaced by deep learning, but remains widely used and theoretically important.
