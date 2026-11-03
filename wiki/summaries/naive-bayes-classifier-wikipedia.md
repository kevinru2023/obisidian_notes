---
title: "Naive Bayes Classifier (Wikipedia)"
type: summary
sources:
  - "[[raw-sources/web-clippings/Naive Bayes classifier.md]]"
related:
  - "[[wiki/concepts/naive-bayes]]"
  - "[[wiki/concepts/bayes-theorem]]"
  - "[[wiki/concepts/logistic-regression]]"
updated: 2026-04-28
tags: [machine-learning, naive-bayes, classification, spam-filtering, text-classification]
---

# Naive Bayes Classifier — Wikipedia Summary

**Source:** Wikipedia article on Naive Bayes classifier, clipped 2026-04-28.

---

## What It Covers

A comprehensive treatment of Naive Bayes classifiers: the probabilistic model, event model variants, parameter estimation, semi-supervised EM training, the relation to logistic regression, and real-world applications (spam filtering, document classification).

---

## Key Points

### Core Model
Given feature vector $\mathbf{x} = (x_1, \ldots, x_n)$ and class $C_k$:

$$p(C_k \mid \mathbf{x}) = \frac{1}{Z} \, p(C_k) \prod_{i=1}^{n} p(x_i \mid C_k)$$

where $Z = p(\mathbf{x})$ is a constant normalizer. Classification uses MAP:

$$\hat{y} = \underset{k}{\operatorname{argmax}} \; p(C_k) \prod_{i=1}^{n} p(x_i \mid C_k)$$

### Log-Space Form
Avoids underflow; log-ratio between two classes cancels $Z$:

$$\ln \frac{p(C_k \mid \mathbf{x})}{p(C_l \mid \mathbf{x})} = \left(\ln p(C_k) + \sum_i \ln p(x_i \mid C_k)\right) - \left(\ln p(C_l) + \sum_i \ln p(x_i \mid C_l)\right)$$

---

## Event Model Variants

| Model | Feature type | $p(\mathbf{x} \mid C_k)$ |
|---|---|---|
| **Gaussian NB** | Continuous | $\mathcal{N}(\mu_k, \sigma_k^2)$ per feature per class |
| **Bernoulli NB** | Binary (word present/absent) | $\prod_i p_{ki}^{x_i}(1-p_{ki})^{1-x_i}$ — explicitly models absence |
| **Multinomial NB** | Frequency counts (bag-of-words) | $\frac{(\sum x_i)!}{\prod x_i!} \prod p_{ki}^{x_i}$ — document word counts |

**Bernoulli vs Multinomial**: Bernoulli uses binary occurrence; Multinomial uses raw term frequencies. They are not the same, and are often confused.

Multinomial NB in log-space is a **linear classifier**: $\log p(C_k \mid \mathbf{x}) \propto b + \mathbf{w}_k^\top \mathbf{x}$ where $b = \log p(C_k)$, $w_{ki} = \log p_{ki}$.

---

## Why NB Works Despite False Independence

- Decoupling features means each conditional distribution can be estimated independently as a 1D distribution — alleviates the curse of dimensionality.
- MAP classification only needs the *correct class to be predicted most probable*, not the probabilities to be accurate. NB is robust to wildly wrong probability estimates.
- Despite producing overconfident probabilities, the classification boundary is often correct.

---

## Relation to Logistic Regression

Naive Bayes (discrete inputs) and multinomial logistic regression form a **generative-discriminative pair**:
- NB optimizes the **joint likelihood** $p(C, \mathbf{x})$
- Logistic regression optimizes the **conditional likelihood** $p(C \mid \mathbf{x})$

**Theorem:** Naive Bayes on binary features is subsumed by logistic regression. In log-odds form, NB's decision function is linear — exactly logistic regression.

**Ng & Jordan (2002) result:** Discriminative classifiers (logistic regression) have lower *asymptotic* error, but NB reaches its asymptotic error faster with fewer samples — giving NB an advantage in low-data regimes.

---

## Semi-Supervised Training (EM)

NB can be extended to learn from labeled $L$ and unlabeled $U$ data:
1. Train NB on labeled $L$.
2. Repeat until convergence:
   - **E-step**: predict $P(C \mid x)$ for all $x \in L \cup U$
   - **M-step**: retrain NB using predicted probabilities (soft labels) for unlabeled data

Convergence measured by improvement to model likelihood $P(D \mid \theta)$.

---

## Spam Filtering

The canonical NB application. Uses bag-of-words features; each word $w_i$ has a "spamicity" $P(\text{spam} \mid w_i)$. Log-likelihood ratio form:

$$\ln \frac{p(S \mid D)}{p(\neg S \mid D)} = \ln \frac{p(S)}{p(\neg S)} + \sum_i \ln \frac{p(w_i \mid S)}{p(w_i \mid \neg S)}$$

**Rare word correction** (beta-distribution prior):
$$\Pr'(S \mid W) = \frac{s \cdot \Pr(S) + n \cdot \Pr(S \mid W)}{s + n}$$

**Bayesian poisoning:** spammers insert legitimate text to lower spam score; countered by using only the most significant probabilities.
