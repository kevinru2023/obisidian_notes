---
title: "Bayes' Theorem (Wikipedia)"
type: summary
sources:
  - "[[raw-sources/web-clippings/Bayes' theorem.md]]"
related:
  - "[[wiki/concepts/bayes-theorem]]"
  - "[[wiki/concepts/naive-bayes]]"
  - "[[wiki/concepts/mle-map]]"
updated: 2026-04-28
tags: [probability, bayes, bayesian-inference, statistics]
---

# Bayes' Theorem — Wikipedia Summary

**Source:** Wikipedia article on Bayes' theorem, clipped 2026-04-28.

---

## What It Covers

A comprehensive treatment of Bayes' theorem: history, formal statement, derivation, worked examples, interpretations (Bayesian vs frequentist), extended forms, and applications.

---

## Key Sections

### Statement
$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$$
- $P(A \mid B)$: **posterior** — probability of $A$ after observing $B$
- $P(B \mid A)$: **likelihood** — probability of evidence $B$ given $A$
- $P(A)$: **prior** — initial probability of $A$
- $P(B)$: **marginal** / normalizing constant

### Derivation
Follows from the symmetric definition of joint probability:
$$P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)$$

### Law of Total Probability Extension
For mutually exclusive, exhaustive events $A_1, A_2, \ldots$:
$$P(A_i \mid B) = \frac{P(A_i)\,P(B \mid A_i)}{\sum_j P(A_j)\,P(B \mid A_j)}$$

### Proportional Form
When $B$ is fixed (as in Bayesian inference), the denominator is a constant:
$$P(A \mid B) \propto P(A) \cdot P(B \mid A)$$
"Posterior is proportional to prior times likelihood."

### Odds Form
$$O(A \mid B) = O(A) \cdot \frac{P(B \mid A)}{P(B \mid \neg A)}$$
Posterior odds = prior odds × Bayes factor (likelihood ratio).

### Continuous Random Variables
$$f_{X \mid Y=y}(x) = \frac{f_{Y \mid X=x}(y)\,f_X(x)}{f_Y(y)}$$

---

## Worked Examples

| Example | Prior | Evidence | Posterior |
|---|---|---|---|
| Cancer diagnosis (1/100k prevalence, all cancer patients symptomatic) | $P(\text{cancer}) = 0.00001$ | Symptomatic | $\approx 9.1\%$ |
| Drug test (99% accurate, 0.3% base rate) | $P(\text{user}) = 0.003$ | Positive test | $\approx 23\%$ |
| Disease test (99% accurate, 1% prevalence) | $P(\text{infected}) = 0.01$ | Positive test | $= 50\%$ (odds form) |

The drug test example illustrates **base-rate neglect**: a highly accurate test on a rare condition still produces mostly false positives.

---

## Interpretations

**Bayesian:** probability = rational degree of belief. Bayes' theorem is the update rule for beliefs given new evidence. After observing $B$, update $P(A) \to P(A \mid B)$.

**Frequentist:** probability = long-run proportion. $P(A \mid B)$ is the proportion of $B$-outcomes that also have $A$.

---

## Applications Mentioned

- **Bayesian inference / parameter estimation** — update distributions over model parameters
- **Cryptanalysis** — Alan Turing at Bletchley Park (Enigma, JN-25)
- **Genetics** — carrier/genotype probability from family history
- **Evolutionary biology** — phylogenetic tree inference via MCMC
- **Recreational math** — Monty Hall problem, Three Prisoners, Boy or Girl paradox

---

## History

- Thomas Bayes (1763, posthumous) — original proposition for the binomial parameter
- Richard Price — edited and published Bayes's work, contributed philosophical framing
- Pierre-Simon Laplace (1774) — independent discovery, extended to general form, developed Bayesian probability
- Harold Jeffreys — axiomatic foundation (1973): "Bayes' theorem is to probability what the Pythagorean theorem is to geometry"
