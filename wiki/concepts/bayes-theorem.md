---
title: "Bayes' Theorem"
type: concept
sources:
  - "[[raw-sources/web-clippings/Bayes' theorem.md]]"
related:
  - "[[wiki/concepts/naive-bayes]]"
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/concepts/regularization]]"
updated: 2026-04-28
tags: [probability, bayes, bayesian-inference, statistics, conditional-probability]
---

# Bayes' Theorem

Bayes' theorem gives a rule for **inverting conditional probabilities** — finding the probability of a cause given an observed effect.

$$\boxed{P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}}$$

| Term | Name | Meaning |
|---|---|---|
| $P(A \mid B)$ | **Posterior** | Probability of $A$ after observing $B$ |
| $P(B \mid A)$ | **Likelihood** | Probability of evidence $B$ if $A$ is true |
| $P(A)$ | **Prior** | Initial probability of $A$ before evidence |
| $P(B)$ | **Marginal** | Total probability of evidence; normalizing constant |

---

## Derivation

Joint probability can be written two ways:
$$P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)$$

Dividing both sides by $P(B)$ gives the theorem.

---

## Proportional Form

When $B$ is fixed (the observed evidence doesn't change), the denominator $P(B)$ is a constant:
$$P(A \mid B) \propto P(A) \cdot P(B \mid A)$$

> **Posterior $\propto$ Prior $\times$ Likelihood**

This is the core update rule in Bayesian inference.

---

## Law of Total Probability

When events $A_1, A_2, \ldots$ are mutually exclusive and exhaustive:
$$P(B) = \sum_i P(B \mid A_i)\,P(A_i)$$

Substituting into the denominator:
$$P(A_i \mid B) = \frac{P(A_i)\,P(B \mid A_i)}{\sum_j P(A_j)\,P(B \mid A_j)}$$

Binary case ($A$ vs $\neg A$):
$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B \mid A)\,P(A) + P(B \mid \neg A)\,P(\neg A)}$$

---

## Odds Form

Dividing posteriors for $A$ and $\neg A$ cancels $P(B)$:
$$\underbrace{\frac{P(A \mid B)}{P(\neg A \mid B)}}_{\text{posterior odds}} = \underbrace{\frac{P(A)}{P(\neg A)}}_{\text{prior odds}} \times \underbrace{\frac{P(B \mid A)}{P(B \mid \neg A)}}_{\text{Bayes factor}}$$

The **Bayes factor** (likelihood ratio) measures how much the evidence shifts the odds.

---

## Base Rate Neglect

A common intuition failure: even a highly accurate test produces mostly false positives when applied to a rare condition.

**Example:** Drug test that is 99% sensitive and 99% specific applied to a population where 0.3% use the drug:
$$P(\text{user} \mid \text{positive}) = \frac{0.99 \times 0.003}{0.99 \times 0.003 + 0.01 \times 0.997} \approx 23\%$$

Most positive results are false positives because the prior $P(\text{user})$ is very small.

**Example:** Disease test (99% accurate, 1% prevalence) → positive result gives 50% posterior. Prior odds $\frac{1}{99}$, Bayes factor $\frac{99}{1}$, posterior odds $\frac{1}{1}$.

---

## Continuous Form

For continuous random variables $X$, $Y$ with probability densities:
$$f_{X \mid Y=y}(x) = \frac{f_{Y \mid X=x}(y)\,f_X(x)}{f_Y(y)}$$

---

## Connection to Machine Learning

| ML concept | Bayesian reading |
|---|---|
| **Naïve Bayes** | Directly applies Bayes' theorem; models $P(y)$ and $P(\mathbf{x} \mid y)$ | 
| **MLE** | Maximizes $P(\mathbf{X} \mid \theta)$ — ignores prior |
| **MAP** | Maximizes $P(\theta \mid \mathbf{X}) \propto P(\mathbf{X} \mid \theta)\,P(\theta)$ — uses prior |
| **Bayesian inference** | Maintains full posterior $P(\theta \mid \mathbf{X})$ rather than a point estimate |
| **Logistic regression** | Discriminative — models $P(y \mid \mathbf{x})$ directly, bypasses Bayes' theorem |

See [[wiki/concepts/naive-bayes]] and [[wiki/concepts/mle-map]] for details.

---

## Interpretations

**Bayesian (epistemic):** probability = degree of belief. Bayes' theorem is the rational update rule: when evidence $B$ arrives, revise $P(A) \to P(A \mid B)$.

**Frequentist:** probability = long-run frequency. $P(A \mid B)$ is the proportion of $B$-trials in which $A$ also occurs.
