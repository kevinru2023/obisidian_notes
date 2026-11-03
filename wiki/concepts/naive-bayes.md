---
title: "Naïve Bayes"
type: concept
sources:
  - "[[raw-sources/courses/CS434/L4.1 - Naive Bayes.pdf]]"
  - "[[raw-sources/courses/CS434/L4.1&2 - Naive Bayes.pdf]]"
  - "[[raw-sources/web-clippings/Naive Bayes classifier.md]]"
  - "[[raw-sources/pdfs/NBayesLogReg.pdf]]"
related:
  - "[[wiki/concepts/bayes-theorem]]"
  - "[[wiki/concepts/mle-map]]"
  - "[[wiki/concepts/logistic-regression]]"
  - "[[wiki/courses/CS434]]"
  - "[[wiki/summaries/mitchell-nb-logreg]]"
updated: 2026-04-29
tags: [machine-learning, naive-bayes, generative-models, classification, laplace-smoothing, CS434, text-classification]
---

# Naïve Bayes

Naïve Bayes is a **generative classifier** based on Bayes' rule and a strong conditional independence assumption. It is one of the simplest and most effective classifiers for high-dimensional discrete data (e.g., text).

---

## Generative vs. Discriminative Models

| | Discriminative | Generative |
|---|---|---|
| What it learns | $P(y \mid \mathbf{x})$ directly | $P(\mathbf{x} \mid y)$ and $P(y)$ |
| Examples | Logistic regression, kNN, perceptron | Naïve Bayes |
| Prediction | $\operatorname{argmax}_y P(y \mid \mathbf{x})$ | Same, via Bayes' rule |

Both predict via $\operatorname{argmax}_y P(y \mid \mathbf{x})$; they just learn and represent it differently.

**Bayes' rule** to recover $P(y \mid \mathbf{x})$ from generative quantities:

$$P(y \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid y)\,P(y)}{P(\mathbf{x})} = \frac{P(\mathbf{x} \mid y)\,P(y)}{\sum_y P(\mathbf{x} \mid y)\,P(y)}$$

---

## Generative Stories

A generative classifier defines a **fictional story** for how data was produced:

- **Class prior $P(y)$**: how are classes distributed?
- **Class conditionals $P(\mathbf{x} \mid y)$**: given a class, how are features distributed?

**Example — exam scores:**
1. Flip a coin ($P(\text{heads}) = \theta$) → did the student study?
2. If study → sample score from $\mathcal{N}(\mu_{\text{study}}, \sigma_{\text{study}})$
3. If not → sample score from $\mathcal{N}(\mu_{\overline{\text{study}}}, \sigma_{\overline{\text{study}}})$

Fitting: estimate $\theta$ by class frequencies; estimate $\mu, \sigma$ from sample statistics within each class.

---

## The Curse of Joint Distributions

For the general case with $d$ features, each with $m$ options, and $c$ classes, fitting $P(\mathbf{x} \mid y)$ as a full joint table requires:

$$O(c \times m^d) \text{ parameters}$$

For $d = 10{,}000$ words in a vocabulary — **completely intractable**.

---

## The Naïve Bayes Assumption

**Each feature is conditionally independent given the class label:**

$$P(\mathbf{x} \mid y) = \prod_{i=1}^{d} P(x_i \mid y)$$

This reduces the parameter count from $O(c \times m^d)$ to $O(c \times d \times m)$ — linear in $d$ instead of exponential.

### Prediction Rule

$$\hat{y} = \operatorname{argmax}_{c} \; P(y = c) \prod_{i=1}^{d} P(x_i \mid y = c)$$

---

## Conditional Independence

**Independence:** $X \perp Y$ iff $P(X, Y) = P(X)P(Y)$

**Conditional independence:** $X \perp Y \mid Z$ iff $P(X, Y \mid Z) = P(X \mid Z)\,P(Y \mid Z)$

Key intuition:
- Variables that are dependent unconditionally can become independent when conditioned on a third variable (e.g., height and vocabulary are dependent, but independent given age).
- Variables that are independent unconditionally can become dependent when conditioned on a third variable (e.g., rock-paper-scissors choices are independent, but become dependent once you know the outcome).

The NB assumption says: once you know the class $y$, the individual features $x_i$ carry no additional information about each other.

---

## Estimating Joint Distributions (MLE)

For $M$ discrete variables, the MLE estimate for each joint combination is:

$$P(\text{row}) = \frac{\text{count of examples matching that row exactly}}{\text{total examples}}$$

This is the MLE for a categorical distribution.

---

## Training a Naïve Bayes Classifier

1. **Estimate class priors** $P(y = c)$ — count frequency of each class in training data
2. **Estimate conditionals** $P(x_i \mid y = c)$ for each feature $i$ and class $c$ — fit a distribution per feature per class (MLE or MAP)
3. **Predict** on a new $\mathbf{x}$ using $\hat{y} = \operatorname{argmax}_c P(y=c) \prod_i P(x_i \mid y=c)$

---

## Naïve Bayes Variants

| Variant | Feature type | $P(x_i \mid y)$ model | Used for |
|---|---|---|---|
| **Bernoulli NB** | Binary (0/1) | Bernoulli — $p_{ki}^{x_i}(1-p_{ki})^{1-x_i}$ | Word present/absent in text; explicitly models word absence |
| **Multinomial NB** | Integer counts | Multinomial — $\frac{(\sum x_i)!}{\prod x_i!}\prod p_{ki}^{x_i}$ | Bag-of-words with term frequencies; the standard for document classification |
| **Categorical NB** | Discrete categories | Categorical (multi-class) | Discrete integer features (e.g., tumor grade 1–10) |
| **Gaussian NB** | Continuous | $\mathcal{N}(\mu_{iy}, \sigma_{iy}^2)$ — learn $\mu, \sigma$ per feature per class | Continuous features (e.g., height, exam scores) |

Any density estimator can be plugged in for $P(x_i \mid y)$ — the NB framework is agnostic to the choice.

**Bernoulli vs Multinomial (common confusion):** Bernoulli uses binary word-occurrence flags (1 = present, 0 = absent) and explicitly penalizes absent words. Multinomial uses raw term frequencies (word counts) and ignores absent words. They are not interchangeable and produce different classifiers.

**Multinomial NB is a linear classifier** in log-space:
$$\log p(C_k \mid \mathbf{x}) \propto \underbrace{\log p(C_k)}_{b} + \sum_i x_i \underbrace{\log p_{ki}}_{w_{ki}} = b + \mathbf{w}_k^\top \mathbf{x}$$

---

## Practical Problem 1: Zero Probability

If any single $P(x_i \mid y = c) = 0$, the entire product collapses to zero, eliminating that class even if all other evidence strongly supports it.

**Example**: the word "accordion" appears once in positive reviews, never in negative. Any new email containing "accordion" gets $P(y = \text{neg} \mid \mathbf{x}) = 0$, forcing a positive prediction — even though "accordion" is sentiment-neutral.

### Laplace Smoothing (Fix)

Add $\alpha$ fake counts to every possible value. For a binary feature:

$$P(x_i \mid y = c) = \frac{(\text{count of } x_i = 1 \text{ and } y = c) + \alpha}{(\text{count of } y = c) + 2\alpha}$$

For a categorical feature with $k$ values:

$$P(x_i = v \mid y = c) = \frac{(\text{count of } x_i = v \text{ and } y = c) + \alpha}{(\text{count of } y = c) + k\alpha}$$

This is equivalent to MAP estimation with a **Beta(α, α)** prior (Bernoulli) or a **Dirichlet(α)** prior (categorical). Setting $\alpha = 1$ is the standard Laplace smoothing.

**When $\alpha$ is important**: the NB assumption breaks if features are jointly predictive of a label but not individually (e.g., only "red sportscars" are stolen — color and type are not conditionally independent given the class).

---

## Practical Problem 2: Numerical Underflow

Multiplying many small probabilities causes floating-point underflow:

$$P(y=c) \prod_{i=1}^{d} P(x_i \mid y=c) = 0.0001 \times 0.001 \times 0.02 \times \cdots \approx 0$$

**Fix: compute in log space** (argmax is preserved under monotone transforms):

$$\hat{y} = \operatorname{argmax}_c \left[ \log P(y=c) + \sum_{i=1}^{d} \log P(x_i \mid y=c) \right]$$

---

## Worked Example: Laplace Smoothing on Categorical Data

**Car theft dataset** ($n = 10$, features: Color and Type, label: Stolen Yes/No):

| | yes (6 examples) | no (4 examples) |
|--|--|--|
| Red | 3/6 → **(3+α)/(6+4α)** | 0/4 → **(0+α)/(4+4α)** |
| Blue | 2/6 | 0/4 |
| Silver | 0/6 | 1/4 |
| Tan | 1/6 | 3/4 |

Without smoothing, $P(\text{Red} \mid y=\text{no}) = 0$, which would force $P(y=\text{no} \mid \text{red car}) = 0$ regardless of other evidence. With $\alpha = 1$ Laplace smoothing, the denominator gains $k\alpha$ where $k$ is the number of categories.

**Why the NB assumption fails here**: if "only red sportscars are stolen", then Color and Type are **not** conditionally independent given the label — the joint combination matters, not each feature alone. Naïve Bayes would fail to capture this interaction.

---

## In-Class Examples

### Categorical NB — Tumor Classification

- Label $y \in \{0, 1\}$ (benign / malignant); 8 features each $\in \{1, \ldots, 10\}$
- Parameters: $P(y)$ (2 params) + $P(x_i \mid y)$ ($10 \times 8 \times 2 = 160$ params)
- Learn $P(y)$, $P(x_i \mid y = 0)$, $P(x_i \mid y = 1)$ via MLE (with Laplace smoothing)

### Gaussian NB — Winegrape Classification

- Label $y \in \{0, 1, 2\}$ (three grape types); 13 continuous features
- Each $P(x_i \mid y = c) = \mathcal{N}(\mu_{ic}, \sigma_{ic})$ — learn $\mu, \sigma$ per feature per class via MLE
- Parameters: $3 \times 2 \times 13 = 78$ parameters ($\mu$ and $\sigma$ for each feature-class pair)

Any density estimator can be substituted for $P(x_i \mid y)$ — discrete, Gaussian, or otherwise.

---

## Why NB Works Despite False Independence

The independence assumption is almost always wrong in practice, yet NB often classifies correctly because:

1. **Only the argmax matters.** MAP classification only requires the correct class to be ranked highest — the probability values don't need to be accurate. NB can be robust to wildly inaccurate probabilities.
2. **Dimensionality.** Treating each feature as 1D means NB avoids the curse of dimensionality — each conditional $P(x_i \mid y)$ can be estimated reliably from far fewer samples than a full joint $P(\mathbf{x} \mid y)$.

NB frequently produces **overconfident probabilities** (often near 0 or 1) but still achieves strong classification accuracy.

---

## Relation to Logistic Regression

NB (discrete features) and logistic regression form a **generative-discriminative pair**:

| | Naive Bayes | Logistic Regression |
|---|---|---|
| What it optimizes | Joint likelihood $p(C, \mathbf{x})$ | Conditional likelihood $p(C \mid \mathbf{x})$ |
| Model type | Generative | Discriminative |
| Asymptotic error | Higher | Lower |
| Convergence speed | Faster (fewer samples) | Slower |

**Theorem (Ng & Jordan 2002):** Naive Bayes on binary features is subsumed by logistic regression — the NB decision function in log-odds form is linear, which is exactly logistic regression:

$$\log \frac{p(C_1 \mid \mathbf{x})}{p(C_2 \mid \mathbf{x})} = b + \mathbf{w}^\top \mathbf{x}$$

**Practical implication:** Logistic regression has lower asymptotic (large-data) error, but NB reaches its asymptotic error faster. In low-data regimes, NB can outperform logistic regression.

---

## Semi-Supervised Training (EM)

NB can learn from a mix of labeled $L$ and unlabeled $U$ data:

1. Train NB on labeled data $L$.
2. Repeat until convergence:
   - **E-step**: predict $P(C \mid x)$ for all $x \in L \cup U$ (soft labels for unlabeled)
   - **M-step**: re-train NB using these predicted probabilities

Convergence is measured by improvement to model likelihood $P(D \mid \theta)$. This is an instance of the **EM algorithm** under the assumption that data are generated by a mixture model whose components correspond to classes.

---

## Evaluating Classifiers

Evaluation metrics (confusion matrix, precision, recall, F1, precision-recall tradeoff) are covered in [[wiki/concepts/logistic-regression#Evaluating Classifiers]].
