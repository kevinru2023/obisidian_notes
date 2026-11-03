---
title: "Support Vector Machine (Wikipedia)"
type: summary
sources:
  - "[[raw-sources/web-clippings/Support vector machine.md]]"
related:
  - "[[wiki/concepts/svm]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/regularization]]"
  - "[[wiki/courses/CS434]]"
updated: 2026-04-27
tags: [machine-learning, SVM, classification, kernel-methods, optimization]
---

# Summary: Support Vector Machine (Wikipedia)

**Source:** Wikipedia article on Support Vector Machines  
**URL:** https://en.wikipedia.org/wiki/Support_vector_machine

---

## Overview

SVMs are supervised max-margin classifiers developed at AT&T Bell Labs. They find the hyperplane that maximizes the separation (margin) between two classes. The kernel trick extends them to nonlinear boundaries by implicitly mapping data to high-dimensional feature spaces.

---

## Core Formulation

### Hard-Margin (Linearly Separable Data)

Given $n$ labeled points $(\mathbf{x}_i, y_i)$ with $y_i \in \{-1, +1\}$, the maximum-margin hyperplane satisfies:

$$\underset{\mathbf{w},b}{\text{minimize}} \quad \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{subject to} \quad y_i(\mathbf{w}^\top \mathbf{x}_i - b) \geq 1 \quad \forall i$$

The margin width is $\frac{2}{\|\mathbf{w}\|}$. Points on the margin boundaries are the **support vectors** — the only points that determine $\mathbf{w}$.

### Soft-Margin (Non-Separable Data)

Introduces hinge loss $\max(0, 1 - y_i(\mathbf{w}^\top \mathbf{x}_i - b))$ and slack variables $\zeta_i$:

$$\underset{\mathbf{w},b,\zeta}{\text{minimize}} \quad \|\mathbf{w}\|_2^2 + C\sum_{i=1}^n \zeta_i \quad \text{subject to} \quad y_i(\mathbf{w}^\top \mathbf{x}_i - b) \geq 1 - \zeta_i,\ \zeta_i \geq 0$$

Large $C$ → penalizes errors heavily (approaches hard-margin); small $C$ → wider margin with more violations allowed.

### Dual Problem

$$\underset{c_1,\ldots,c_n}{\text{maximize}} \quad \sum_i c_i - \frac{1}{2}\sum_i\sum_j y_i c_i (\mathbf{x}_i^\top \mathbf{x}_j) y_j c_j \quad \text{s.t.} \quad \sum_i c_i y_i = 0,\ 0 \leq c_i \leq \frac{1}{2n\lambda}$$

The weight vector $\mathbf{w} = \sum_i c_i y_i \mathbf{x}_i$ — a linear combination of support vectors only (since $c_i = 0$ for correctly-classified interior points).

---

## Kernel Trick

The dual depends only on dot products $\mathbf{x}_i^\top \mathbf{x}_j$. Replacing these with a kernel function $k(\mathbf{x}_i, \mathbf{x}_j) = \varphi(\mathbf{x}_i) \cdot \varphi(\mathbf{x}_j)$ allows nonlinear classification without explicitly computing the high-dimensional mapping $\varphi$.

**Common kernels:**

| Kernel | Formula |
|--------|---------|
| Linear | $k(\mathbf{x}_i, \mathbf{x}_j) = \mathbf{x}_i \cdot \mathbf{x}_j$ |
| Polynomial (homogeneous) | $k(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i \cdot \mathbf{x}_j)^d$ |
| Polynomial (inhomogeneous) | $k(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i \cdot \mathbf{x}_j + r)^d$ |
| RBF / Gaussian | $k(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2)$ |
| Sigmoid | $k(\mathbf{x}_i, \mathbf{x}_j) = \tanh(\kappa\, \mathbf{x}_i \cdot \mathbf{x}_j + c)$ |

The final classifier using kernels: $\mathbf{z} \mapsto \operatorname{sgn}\!\left(\sum_i c_i y_i k(\mathbf{x}_i, \mathbf{z}) - b\right)$.

Working in higher-dimensional feature space increases generalization error, though given enough samples the algorithm still performs well.

---

## ERM / Hinge Loss Perspective

Soft-margin SVM minimizes:

$$\left[\frac{1}{n}\sum_{i=1}^n \max(0, 1 - y_i(\mathbf{w}^\top \mathbf{x}_i - b))\right] + \lambda\|\mathbf{w}\|^2$$

This is **empirical risk minimization with Tikhonov regularization** using the hinge loss $\ell(y,z) = \max(0, 1-yz)$.

Comparison with other classifiers:

| Method | Loss |
|--------|------|
| SVM | Hinge: $\max(0, 1-yz)$ |
| Regularized least-squares | Square: $(y-z)^2$ |
| Logistic regression | Log: $\ln(1 + e^{-yz})$ |

The hinge loss target function is exactly the Bayes-optimal classifier $f^*(x)$ — SVM converges to the simplest function that classifies correctly, whereas logistic/square losses converge to functions that also encode probability estimates.

---

## Extensions

### Multiclass SVM
Standard SVM is binary. Multiclass approaches:
- **One-vs-all:** train $k$ classifiers; winner-takes-all prediction
- **One-vs-one:** train $\binom{k}{2}$ classifiers; max-wins voting
- **DAGSVM:** directed acyclic graph tournament
- **Crammer & Singer:** single joint optimization problem

### Support Vector Regression (SVR)
Proposed by Vapnik et al. (1996). Minimizes $\frac{1}{2}\|w\|^2$ subject to $|y_i - \langle w, x_i\rangle - b| \leq \varepsilon$. All predictions must fall within an $\varepsilon$-tube around targets. Slack variables allow approximation.

### Transductive SVM
Semi-supervised extension: optimizes over both training labels and unknown test labels simultaneously.

### Bayesian SVM
Views SVM as a graphical model via data augmentation; enables flexible feature modeling and uncertainty quantification.

---

## Implementation Algorithms

| Method | Approach |
|--------|---------|
| Quadratic programming | Classical reduction; scales poorly |
| **SMO (Platt)** | Breaks into 2D sub-problems solved analytically; fast and practical |
| Sub-gradient descent | Works on primal directly; scales with training examples |
| Coordinate descent | Works on dual; efficient for high-dimensional feature spaces |

**LIBLINEAR** is the standard library for linear SVMs; convergence iterations are $O(\text{data size})$ with Q-linear convergence. General kernel SVMs use LIBSVM.

---

## Parameter Selection

Key parameters: kernel choice, kernel parameter (e.g., $\gamma$ for RBF), and $C$ (or $\lambda$). Typically selected by **grid search with cross-validation**. Grid is exponential: $C \in \{2^{-5}, 2^{-3}, \ldots, 2^{15}\}$, $\gamma \in \{2^{-15}, \ldots, 2^3\}$.

---

## Drawbacks

- Requires fully labeled data
- Not inherently probabilistic (no calibrated class membership probabilities)
- Natively binary only; multi-class requires decomposition
- Parameters of the learned model are hard to interpret
