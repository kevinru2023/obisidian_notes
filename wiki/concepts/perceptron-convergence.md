---
title: "Perceptron Convergence Theorem"
type: concept
sources:
  - "[[raw-sources/courses/CS434/perc.converge.pdf]]"
related:
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/svm]]"
  - "[[wiki/courses/CS434]]"
updated: 2026-04-20
tags: [machine-learning, perceptron, convergence, proof, CS434]
---

# Perceptron Convergence Theorem

*Source: Michael Collins*

The perceptron is guaranteed to converge in a **finite number of mistakes** if the training data is linearly separable. This is formalized by the convergence theorem.

---

## Setup

**Algorithm recap** (see also [[wiki/concepts/logistic-regression]]):

- Initialize $\theta = \mathbf{0}$
- For each training example $(x_t, y_t)$ where $y_t \in \{-1, +1\}$:
  - Predict $y' = \text{sign}(x_t \cdot \theta)$
  - If $y' \neq y_t$: update $\theta \leftarrow \theta + y_t x_t$
  - Else: leave $\theta$ unchanged

---

## The Theorem

**Theorem (Collins).** Assume:

1. There exists $\theta^*$ with $\|\theta^*\| = 1$ and $\gamma > 0$ such that for all training examples $t = 1 \ldots n$:

$$y_t(\mathbf{x}_t \cdot \theta^*) \geq \gamma$$

   (i.e., $\theta^*$ correctly classifies every example with margin at least $\gamma$)

2. For all $t$: $\|\mathbf{x}_t\| \leq R$

Then the perceptron makes at most

$$\frac{R^2}{\gamma^2}$$

mistakes.

**Intuition**: the bound grows with $R$ (larger inputs → harder geometry) and shrinks with $\gamma$ (larger margin → easier problem).

---

## Proof

Let $\theta^k$ denote the parameter vector just before the $k$-th mistake.

Note $\theta^1 = \mathbf{0}$.

### Part 1 — Lower bound on $\|\theta^{k+1}\|$

When the $k$-th mistake is made on example $t$, the update gives $\theta^{k+1} = \theta^k + y_t \mathbf{x}_t$. Taking the dot product with $\theta^*$:

$$\theta^{k+1} \cdot \theta^* = (\theta^k + y_t \mathbf{x}_t) \cdot \theta^* = \theta^k \cdot \theta^* + y_t \mathbf{x}_t \cdot \theta^* \geq \theta^k \cdot \theta^* + \gamma$$

By induction (base case $\theta^1 \cdot \theta^* = 0$):

$$\theta^{k+1} \cdot \theta^* \geq k\gamma$$

Since $\|\theta^{k+1}\| \cdot \|\theta^*\| \geq \theta^{k+1} \cdot \theta^*$ (Cauchy-Schwarz) and $\|\theta^*\| = 1$:

$$\|\theta^{k+1}\| \geq k\gamma \tag{4}$$

### Part 2 — Upper bound on $\|\theta^{k+1}\|$

$$\|\theta^{k+1}\|^2 = \|\theta^k + y_t \mathbf{x}_t\|^2 = \|\theta^k\|^2 + y_t^2\|\mathbf{x}_t\|^2 + 2y_t \mathbf{x}_t \cdot \theta^k$$

Two facts about the error case:
- $y_t^2 \|\mathbf{x}_t\|^2 = \|\mathbf{x}_t\|^2 \leq R^2$
- $y_t \mathbf{x}_t \cdot \theta^k \leq 0$ (because $\theta^k$ made an error on example $t$)

Therefore:

$$\|\theta^{k+1}\|^2 \leq \|\theta^k\|^2 + R^2$$

By induction (base case $\|\theta^1\|^2 = 0$):

$$\|\theta^{k+1}\|^2 \leq kR^2 \tag{8}$$

### Combining the Bounds

From (4): $\|\theta^{k+1}\|^2 \geq k^2\gamma^2$

From (8): $\|\theta^{k+1}\|^2 \leq kR^2$

Therefore:

$$k^2\gamma^2 \leq kR^2 \implies k \leq \frac{R^2}{\gamma^2} \qquad \square$$

---

## Key Takeaways

| Quantity | Role |
|---|---|
| $\gamma$ | Margin of the separating hyperplane — how "confidently" separable the data is |
| $R$ | Maximum input norm — how spread out the data is |
| $R^2/\gamma^2$ | Upper bound on mistakes — finite iff data is linearly separable |

- The bound is **independent of dimensionality** $d$ and dataset size $n$ — only geometry matters.
- If data is **not** linearly separable, the perceptron never converges (cycles forever).
- The convergence guarantee is on the number of **mistakes**, not iterations.
