---
title: "Regularization"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L3.1 - Multidimension Linear Regression, Basis Functions and Regularization.pdf]]"
related:
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/courses/CS434]]"
updated: 2026-04-19
tags: [machine-learning, regularization, ridge, lasso, overfitting, CS434]
---

# Regularization

Regularization is a technique for **preventing overfitting** by penalizing model complexity — specifically, by discouraging large weights.

---

## The Problem It Solves

When you fit a complex model (e.g., high-degree polynomial regression), the model can "memorize" training data by using very large weights that cancel each other out. This fits training data perfectly but generalizes terribly. Overfitting in linear models correlates strongly with large weight magnitudes.

---

## The Core Idea

Instead of just minimizing your loss $\mathcal{L}(w)$ (e.g., sum of squared error), you minimize:

$$w^* = \arg\min_w \; \mathcal{L}(w) + \lambda \cdot \text{Regularizer}(w)$$

The regularizer penalizes large weights. $\lambda$ controls the tradeoff:
- **Large $\lambda$** → simpler model, less overfitting, but risks underfitting
- **Small $\lambda$** → complex model, better training fit, but risks overfitting

---

## Two Main Forms

**L2 Regularization (Ridge Regression)**

$$w^* = \arg\min_w \; \underbrace{(y - Xw)^T(y - Xw)}_{\text{SSE}} + \lambda \underbrace{w^T w}_{\|w\|_2^2}$$

- Closed-form solution: $w^* = (X^TX + \lambda I)^{-1} X^T y$
- Yields **dense weights** (all weights shrink toward zero but rarely hit exactly zero)
- Bonus: the $\lambda I$ term fixes the invertibility problem when $n < d$

**L1 Regularization (Lasso Regression)**

$$w^* = \arg\min_w \; \text{SSE} + \lambda \|w\|_1$$

- Yields **sparse weights** (some weights go to exactly zero → implicit feature selection)
- Computationally harder to optimize (no closed form)

---

## The Bayesian Interpretation

Regularization is equivalent to **MAP estimation** with a prior on the weights:

| Regularizer | Equivalent prior on $w$ | Method |
|---|---|---|
| L2: $\lambda\|w\|_2^2$ | Gaussian: $w \sim \mathcal{N}(0, \beta I)$ | Ridge |
| L1: $\lambda\|w\|_1$ | Laplace prior | Lasso |

The prior encodes the belief that weights should be small. A larger $\lambda$ = a sharper prior = stronger belief in small weights. See [[wiki/concepts/mle-map]] for the full MAP derivation.

---

## L1 vs L2: Why Sparsity?

The geometry explains it: L1's constraint region is a diamond (pointy corners on the axes), while L2's is a circle. The loss function's contours tend to hit the diamond at a corner — where some weights are exactly zero. L2's smooth circle usually gets touched off-axis, so no weights zero out.

---

## Bias-Variance Tradeoff

| Regularization strength | Bias | Variance |
|---|---|---|
| High $\lambda$ | High (underfit) | Low |
| Low $\lambda$ | Low | High (overfit) |
| Optimal $\lambda$ | Balanced | Balanced |

$\lambda$ is a hyperparameter typically chosen via cross-validation.
