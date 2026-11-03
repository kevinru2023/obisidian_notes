---
title: "Mitchell — Naive Bayes and Logistic Regression (ML Textbook Ch. 3)"
type: summary
sources:
  - "[[raw-sources/pdfs/NBayesLogReg.pdf]]"
related:
  - "[[wiki/concepts/naive-bayes]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/concepts/bayes-theorem]]"
  - "[[wiki/courses/CS434]]"
updated: 2026-04-29
tags: [machine-learning, naive-bayes, logistic-regression, generative-discriminative, CS434, textbook, Mitchell]
---

# Mitchell — Naive Bayes and Logistic Regression (ML Textbook Ch. 3)

**Source:** Chapter 3 draft of *Machine Learning* (2nd ed.), Tom M. Mitchell, CMU, 2020.
Covers Naive Bayes (discrete and Gaussian), Logistic Regression, and their formal relationship.

---

## 1. Learning Classifiers via Bayes Rule

Goal: approximate $f : X \to Y$, equivalently learn $P(Y \mid X)$.

**Generative approach:** estimate $P(X \mid Y)$ and $P(Y)$ from data, then use Bayes rule:

$$P(Y = y_k \mid X) = \frac{P(X \mid Y = y_k) \cdot P(Y = y_k)}{\sum_j P(X \mid Y = y_j) \cdot P(Y = y_j)}$$

**Why naive estimation of $P(X \mid Y)$ is intractable:** If $X$ contains $n$ boolean features, the joint table $P(X \mid Y)$ requires $2(2^n - 1)$ parameters. For $n = 30$: over 3 billion parameters.

---

## 2. Naive Bayes Algorithm

**Conditional independence assumption:** each $X_i$ is conditionally independent of all other $X_j$ given $Y$:

$$P(X \mid Y) = \prod_{i=1}^n P(X_i \mid Y)$$

This reduces the parameter count from $O(2^n)$ to $O(n)$ — linear in the number of features.

**Naive Bayes classification rule:**

$$\hat{y} = \operatorname{argmax}_{y_k} \; P(Y = y_k) \prod_{i=1}^n P(X_i \mid Y = y_k)$$

### 2.1 Discrete Inputs — MLE

Parameters to estimate for each feature $X_i$, value $x_{ij}$, class $y_k$:

$$\hat{\theta}_{ijk} = \hat{P}(X_i = x_{ij} \mid Y = y_k) = \frac{\#_D\{X_i = x_{ij} \wedge Y = y_k\}}{\#_D\{Y = y_k\}}$$

**Smoothed (Laplace) estimate:**

$$\hat{\theta}_{ijk} = \frac{\#_D\{X_i = x_{ij} \wedge Y = y_k\} + \lambda}{\#_D\{Y = y_k\} + J\lambda}$$

where $J$ = number of distinct values $X_i$ can take, $\lambda = 1$ for standard Laplace smoothing. Equivalent to MAP with a Dirichlet prior.

**Class prior:**

$$\hat{P}(Y = y_k) = \frac{\#_D\{Y = y_k\}}{|D|}$$

### 2.2 Gaussian Naive Bayes (Continuous Inputs)

Assume $P(X_i \mid Y = y_k) = \mathcal{N}(\mu_{ik}, \sigma_i^2)$ (note: $\sigma_i$ does not depend on $k$).

MLE estimates:

$$\hat{\mu}_{ik} = \frac{\sum_j X_i^j \cdot \mathbf{1}[Y^j = y_k]}{\#_D\{Y = y_k\}}, \qquad \hat{\sigma}_{ik}^2 = \frac{\sum_j (X_i^j - \hat{\mu}_{ik})^2 \cdot \mathbf{1}[Y^j = y_k]}{\#_D\{Y = y_k\} - 1}$$

---

## 3. Logistic Regression

**Discriminative approach:** directly model $P(Y \mid X)$ without modeling $P(X \mid Y)$.

**Parametric form (boolean $Y$):**

$$P(Y = 1 \mid X) = \frac{1}{1 + e^{-(w_0 + \sum_i w_i X_i)}}$$

$$P(Y = 0 \mid X) = \frac{e^{-(w_0 + \sum_i w_i X_i)}}{1 + e^{-(w_0 + \sum_i w_i X_i)}}$$

**Decision rule:** assign $Y = 1$ if $w_0 + \sum_i w_i X_i > 0$ (linear boundary).

### 3.1 Training via Gradient Ascent on Log-Likelihood

Maximize the conditional log-likelihood:

$$\ell(W) = \sum_l \left[ Y^l \log \hat{P}(Y^l = 1 \mid X^l, W) + (1 - Y^l) \log \hat{P}(Y^l = 0 \mid X^l, W) \right]$$

Gradient (the $i$-th component):

$$\frac{\partial \ell}{\partial w_i} = \sum_l \left( Y^l - \hat{P}(Y^l = 1 \mid X^l, W) \right) X_i^l$$

**Gradient ascent update:**

$$w_i \leftarrow w_i + \eta \cdot \frac{\partial \ell}{\partial w_i}$$

$\ell(W)$ is **concave** in $W$ → gradient ascent converges to the global maximum.

### 3.2 Regularization (L2)

Penalized log-likelihood to prevent overfitting:

$$\ell_\lambda(W) = \ell(W) - \lambda \|W\|^2$$

Equivalent to MAP with a zero-mean Gaussian prior on $W$ with variance $\propto 1/\lambda$. Modified gradient:

$$\frac{\partial \ell_\lambda}{\partial w_i} = \sum_l \left( Y^l - \hat{P}(Y^l = 1 \mid X^l, W) \right) X_i^l - 2\lambda w_i$$

---

## 4. The NB ↔ LR Relationship (Key Theorem)

**Theorem (Mitchell Ch. 3):** Under Gaussian Naive Bayes assumptions — $Y$ boolean, $P(X_i \mid Y = y_k) = \mathcal{N}(\mu_{ik}, \sigma_i)$ (same $\sigma_i$ for both classes) — the posterior $P(Y \mid X)$ takes exactly the logistic regression form:

$$P(Y = 1 \mid X) = \frac{1}{1 + e^{-(w_0 + \sum_i w_i X_i)}}$$

where the weights are determined by GNB parameters:

$$w_i = \frac{\mu_{i1} - \mu_{i0}}{\sigma_i^2}, \qquad w_0 = \sum_i \frac{\mu_{i0}^2 - \mu_{i1}^2}{2\sigma_i^2} + \log\frac{P(Y=1)}{P(Y=0)}$$

**Implication:** Logistic Regression is the discriminative counterpart to Gaussian Naive Bayes. If the GNB assumptions hold exactly, both converge to the same classifier as $n \to \infty$.

---

## 5. Generative vs. Discriminative Comparison

| | Naive Bayes (generative) | Logistic Regression (discriminative) |
|---|---|---|
| What it estimates | $P(X \mid Y)$ and $P(Y)$ | $P(Y \mid X)$ directly |
| Convergence rate | $O(\log n)$ examples | $O(n)$ examples |
| Asymptotic accuracy (if GNB holds) | Same as LR | Same as NB |
| Asymptotic accuracy (if GNB fails) | Worse (biased) | Better (more flexible) |
| With limited data | Often better (lower variance) | Often worse |

**Ng & Jordan (2002) result:** NB reaches its asymptotic accuracy faster (in $O(\log n)$ examples), but LR's asymptote is better when the conditional independence assumption doesn't hold. In practice: **use NB with scarce data, LR with abundant data**.

---

## 6. Exercise Hint — Boolean NB is Also LR

The textbook (Exercise 3) asks you to prove that NB with **boolean** features (not Gaussian) also implies the logistic regression form. The key trick:

$$P(X_i = x_i \mid Y = 1) = \theta_{i1}^{x_i}(1 - \theta_{i1})^{1-x_i}$$

where $\theta_{i1} = P(X_i = 1 \mid Y = 1)$. This is the Bernoulli PMF trick — when $x_i \in \{0,1\}$, both cases collapse into one expression (see [[wiki/concepts/naive-bayes]] for details). The ratio of class-conditional likelihoods reduces to a linear function in $x_i$ in log space, giving the sigmoid form for $P(Y \mid X)$.
