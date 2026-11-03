---
title: "Statistical Learning — MLE and MAP"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L2.1 - Prob.,MLE, and MAP copy 2.pdf]]"
related:
  - "[[wiki/courses/CS434]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/regularization]]"
  - "[[wiki/concepts/linear-regression]]"
updated: 2026-04-16
tags: [machine-learning, statistics, MLE, MAP, Bayesian, CS434]
---

# Statistical Learning — MLE and MAP

Both MLE and MAP are principled frameworks for choosing model parameters $\theta$ from data.

---

## Maximum Likelihood Estimation (MLE)

**Idea**: choose $\theta$ that makes the observed data most probable.

$$\theta_{\text{MLE}} = \operatorname{argmax}_\theta\, P(D \mid \theta) = \operatorname{argmax}_\theta \prod_i P(x_i, y_i \mid \theta)$$

Since products are numerically unstable, take the log (monotone, so argmax is the same):

$$\theta_{\text{MLE}} = \operatorname{argmax}_\theta \sum_i \log P(x_i, y_i \mid \theta)$$

**Connection to linear regression**: if you assume $y = w^\top x + \varepsilon$ where $\varepsilon \sim \mathcal{N}(0, \sigma^2)$, maximizing the likelihood is exactly equivalent to minimizing MSE. The Gaussian noise assumption is what justifies least squares.

**Connection to logistic regression**: assuming a Bernoulli model for binary labels → MLE gives the cross-entropy loss.

---

## Maximum A Posteriori (MAP)

**Idea**: incorporate a **prior** belief about $\theta$ before seeing data.

By Bayes' rule:
$$P(\theta \mid D) \propto P(D \mid \theta) \cdot P(\theta)$$

MAP chooses $\theta$ to maximize the posterior:
$$\theta_{\text{MAP}} = \operatorname{argmax}_\theta \left[\log P(D \mid \theta) + \log P(\theta)\right]$$

The log prior term acts as a **regularizer**:

| Prior on $\theta$ | Effect on loss | Equivalent regularization |
|---|---|---|
| Gaussian: $P(\theta) \propto \exp(-\lambda\|\theta\|^2)$ | adds $\lambda\|\theta\|^2$ to loss | $L_2$ / Ridge |
| Laplace: $P(\theta) \propto \exp(-\lambda\|\theta\|_1)$ | adds $\lambda\|\theta\|_1$ to loss | $L_1$ / Lasso |

**Key insight**: regularization isn't arbitrary penalty — it's a MAP estimate with a specific prior. The strength of regularization ($\lambda$) reflects how confident you are in the prior.

---

## MLE vs MAP Summary

| | MLE | MAP |
|---|---|---|
| What it maximizes | Likelihood $P(D \mid \theta)$ | Posterior $P(\theta \mid D)$ |
| Prior | Ignored (uniform prior) | Explicitly included |
| Equivalent loss term | Just data fit | Data fit + regularizer |
| Risk | Overfits with small data | More robust with small data |
| Relation to regularization | No regularization | Regularization = log prior |

---

## Practical Notes

- With large amounts of data, MLE and MAP converge to the same answer (data overwhelms the prior).
- With small data, the prior (MAP) matters a lot — it encodes your assumptions and prevents overfitting.
- Choosing the prior is equivalent to choosing a regularizer and its strength.
- Both MLE and MAP give **point estimates** of $\theta$. Full Bayesian inference maintains a distribution over $\theta$ (computationally harder).
