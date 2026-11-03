---
title: "Linear Regression"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L2.2 - Linear Algebra and Linear Regression.pdf]]"
  - "[[raw-sources/courses/CS434/L3.1 - Multidimension Linear Regression, Basis Functions and Regularization.pdf]]"
related:
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/concepts/regularization]]"
  - "[[wiki/courses/CS434]]"
  - "[[notes/courses/ML/Linear Regression]]"
updated: 2026-04-21
tags: [machine-learning, regression, linear-regression, CS434]
---

# Linear Regression

Linear regression fits a linear function $f(x) = w^\top x$ to predict a continuous output $y$.

---

## Objective

Minimize the **sum of squared errors (SSE)** over the training set $D = \{(x_i, y_i)\}$:

$$\mathcal{L}(w) = \sum_{i=1}^{n} (y_i - w^\top x_i)^2 = \|y - Xw\|^2$$

where $X \in \mathbb{R}^{n \times d}$ is the design matrix (each row is one training example) and $y \in \mathbb{R}^n$ is the target vector.

**Convention:** fold the bias term $b$ into $w$ by appending a constant 1 feature to every $x$.

---

## Closed-Form Solution

Setting $\nabla_w \mathcal{L} = 0$ yields the **normal equations**:

$$w^* = (X^\top X)^{-1} X^\top y$$

This is the unique global minimum because SSE is convex in $w$.

**When $X^\top X$ is not invertible** (e.g., $n < d$, or collinear features): use ridge regularization ($\lambda I$ term makes it invertible) or a pseudoinverse.

---

## MLE Justification

If we assume $y_i = w^\top x_i + \varepsilon_i$ where $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$ i.i.d., then maximizing the likelihood $P(D \mid w)$ is exactly equivalent to minimizing SSE. The Gaussian noise assumption is what makes least squares the "right" loss. See [[wiki/concepts/mle-map]].

---

## Basis Function Extension

To fit nonlinear data with a linear model, apply a feature map $\phi : \mathbb{R}^d \to \mathbb{R}^m$ and fit:

$$f(x) = w^\top \phi(x)$$

The model is still linear in the new feature space, so the closed-form solution still applies. Common choices:
- **Polynomial**: $\phi(x) = [1, x, x^2, \ldots, x^p]$
- **Radial basis functions**: $\phi_j(x) = \exp(-\|x - \mu_j\|^2 / 2\sigma^2)$

High-degree polynomial expansion risks overfitting — control with regularization.

---

## Regularization

Add a penalty on weight magnitude to prevent overfitting:

**Ridge (L2):** $w^* = \arg\min_w \|y - Xw\|^2 + \lambda\|w\|_2^2$

Closed-form: $w^* = (X^\top X + \lambda I)^{-1} X^\top y$

**Lasso (L1):** $w^* = \arg\min_w \|y - Xw\|^2 + \lambda\|w\|_1$ — yields sparse solutions, no closed form.

See [[wiki/concepts/regularization]] for the full treatment including Bayesian interpretation and L1 vs L2 geometry.

---

## Comparison to Logistic Regression

| | Linear Regression | Logistic Regression |
|---|---|---|
| Task | Regression (continuous $y$) | Binary classification |
| Output | $w^\top x \in (-\infty, +\infty)$ | $\sigma(w^\top x) \in (0, 1)$ |
| Loss | MSE / SSE | Binary cross-entropy |
| Solution | Closed-form | Gradient descent |

See [[wiki/concepts/logistic-regression]].
