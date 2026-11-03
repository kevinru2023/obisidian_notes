---
title: "k-Nearest Neighbors (kNN)"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L1.2 - kNN.pdf]]"
related:
  - "[[wiki/courses/CS434]]"
  - "[[wiki/concepts/mle-map]]"
updated: 2026-04-16
tags: [machine-learning, kNN, CS434, classification, regression]
---

# k-Nearest Neighbors (kNN)

**Type**: Supervised, non-parametric, lazy learner (no model is built during training — inference does all the work)

---

## Algorithm

**Four choices define a kNN model:**
1. **Distance metric** — how to measure "closeness"
2. **$k$** — how many neighbors to examine
3. **Output function** — how to aggregate neighbor labels
4. **Weighting function** (optional) — do all $k$ neighbors count equally?

**Training**: store $D = \{(x_i, y_i)\}$ (optionally build a kd-tree or LSH for fast lookup).

**Inference on point $x$**:
- Compute distance $d(x, x_i)$ for all training points
- Find the $k$ nearest: $N_k(x) = [n_1, n_2, \ldots, n_k]$ ordered by distance

---

## Classification

**1-NN**: $f_1(x) = y_{N_1(x)}$ — output the label of the single closest point

**$k$-NN majority vote**:
$$f_k(x) = \operatorname{argmax}_y \sum_{i \in N_k(x)} \mathbf{1}[y_i = y]$$

**Weighted $k$-NN**: weight each neighbor's vote by $w(x, x_i)$ — closer neighbors count more.

---

## Regression

**$k$-NN**:
$$f_k(x) = \frac{1}{k} \sum_{i \in N_k(x)} y_i$$

**Weighted $k$-NN**:
$$f_k(x) = \frac{\sum w(x, x_i) \cdot y_i}{\sum w(x, x_i)}$$

**Weighting function**: $w(x, x_i) = \exp\!\left(-d(x, x_i)^2 / \sigma^2\right)$ (Gaussian kernel; $\sigma$ is bandwidth)

---

## Distance Metrics

| Name | Formula |
|------|---------|
| Euclidean ($L_2$) | $\sqrt{\sum (x_i - z_i)^2}$ |
| Manhattan ($L_1$) | $\sum |x_i - z_i|$ |
| Chebyshev ($L_\infty$) | $\max_i |x_i - z_i|$ |
| Minkowski ($L_p$) | $\left(\sum |x_i - z_i|^p\right)^{1/p}$ |

Euclidean = Minkowski $p=2$; Manhattan = $p=1$; Chebyshev = $p \to \infty$.

---

## Effect of $k$

| $k$ value | Behavior |
|-----------|----------|
| $k = 1$ | Training error $= 0$ (each point is its own neighbor). Jagged decision boundary. Overfits noise. |
| $k = n$ | Predicts majority class everywhere (classification) or training mean (regression). Underfits. |
| $1 < k < n$ | Smoother boundary. Choose via cross-validation. |

---

## Curse of Dimensionality

In high dimensions, distance stops being meaningful.

**Volume argument**: In a $d$-ball of radius $1$, the fraction of volume in an outer shell of width $\varepsilon$ is:
$$1 - (1-\varepsilon)^d \;\to\; 1 \quad \text{as } d \to \infty$$

Even for tiny $\varepsilon$, almost all the volume lives near the surface — so all points are roughly equidistant from any query point. This breaks the "nearby = similar" assumption kNN relies on.

**Practical implications**:
- Irrelevant features dilute the distance signal → include only relevant features
- Features need to be normalized (otherwise high-range features dominate)
- May need dimensionality reduction or a learned distance metric

Real data often lies on a lower-dimensional manifold, which is why kNN can still work in practice.

---

## Practical Issues

- **Computational cost**: $O(nd)$ per test point ($n$ = training size, $d$ = dimensions). Speed up with kd-trees, ball-trees, or locality-sensitive hashing.
- **Memory**: must store all training points — prohibitive for massive datasets.
- **Feature normalization**: scale all features to $[0,1]$ or z-score; otherwise large-range features dominate distance.
- **Irrelevant features**: add noise to distance. Perform feature selection first.

---

## Pros & Cons

| Pros | Cons |
|------|------|
| Conceptually simple | Slow at inference: $O(nd)$ |
| No training phase | Must store all data |
| Very flexible decision boundaries | Sensitive to irrelevant features and scale |
| Works for regression and classification | Poor in high dimensions (curse) |
| Naturally handles multi-class | Hard to interpret which features matter |
