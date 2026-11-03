---
title: "Parallel Performance Analysis"
type: concept
sources:
  - "[[raw-sources/courses/CS475/06_OpenMP_task_and_performance.pdf]]"
related:
  - "[[wiki/courses/CS475]]"
  - "[[wiki/concepts/openmp]]"
  - "[[wiki/concepts/parallel-programming-fundamentals]]"
updated: 2026-04-20
tags: [parallel-programming, performance, amdahl, gustafson, speedup, cs475]
---

# Parallel Performance Analysis

---

## Speedup

$$\text{Speedup} = \frac{\text{Sequential execution time}}{\text{Parallel execution time}}$$

Decompose execution time into three components (problem size $n$, cores $p$):

| Component | Meaning |
|---|---|
| $\sigma(n)$ | Inherently sequential computation |
| $\varphi(n)$ | Potentially parallel computation |
| $\kappa(n,p)$ | Communication/synchronization overhead |

**General speedup bound:**

$$\psi(n, p) \leq \frac{\sigma(n) + \varphi(n)}{\sigma(n) + \varphi(n)/p + \kappa(n,p)} \leq \frac{\sigma(n) + \varphi(n)}{\sigma(n) + \varphi(n)/p}$$

**Parallel efficiency:** fraction of cores being usefully used

$$\varepsilon(n, p) = \frac{\psi(n, p)}{p} \leq \frac{\sigma(n) + \varphi(n)}{p\,\sigma(n) + \varphi(n)}, \quad 0 < \varepsilon \leq 1$$

---

## Amdahl's Law

**Assumption: fixed problem size** — $\sigma(n)$ and $\varphi(n)$ are constants.

Let $f$ = fraction of total time that is inherently sequential:

$$f = \frac{\sigma(n)}{\sigma(n) + \varphi(n)}$$

$$\boxed{\psi \leq \frac{1}{f + \dfrac{1-f}{p}}}$$

**Derivation:** substitute $\sigma = f \cdot T$, $\varphi = (1-f) \cdot T$ into the general bound, the $T$ cancels.

**Key insight:** as $p \to \infty$, speedup is bounded by $1/f$. Even a tiny serial fraction caps the max speedup.

### Examples

| Serial fraction $f$ | Limit ($p \to \infty$) |
|---|---|
| 5% | 20× |
| 10% | 10× |
| 20% | 5× |
| 50% | 2× |

**Example 1:** 95% of runtime is parallelizable; 8 CPUs:

$$\psi \leq \frac{1}{0.05 + 0.95/8} \approx 5.93$$

**Example 2:** 20% serial fraction, $p \to \infty$: speedup $\leq 5$.

**Example 3 (quiz):** 80% parallelizable, 8 processors:

$$\psi \leq \frac{1}{0.2 + 0.8/8} \approx 3.33$$

**Example 4 (quiz):** 99s parallelizable + 1s serial, 100 processors:

$$\psi \leq \frac{1}{0.01 + 0.99/100} \approx 50.25$$

### Limitations of Amdahl's Law

- Ignores $\kappa(n, p)$ (communication overhead) → overestimates speedup
- Assumes fixed problem size $n$ — ignores the common case where we use more cores to solve *larger* problems

---

## Gustafson-Barsis Law (Scaled Speedup)

**Assumption: fixed parallel execution time** — keep the wall-clock time constant while growing the problem with $p$.

Let $s$ = fraction of *parallel* execution time spent in sequential code:

$$s = \frac{\sigma(n)}{\sigma(n) + \varphi(n)/p}$$

$$\boxed{\psi \leq p + (1-p)s}$$

**Derivation:** The parallel time is $\sigma + \varphi/p$. The equivalent serial time for the same problem is $\sigma + \varphi$. Divide and simplify using $s$.

**Key insight:** scaled speedup grows linearly with $p$; a small $s$ means we can efficiently use many cores by scaling up the problem.

### Examples

**Example 1:** 10 processors, 3% serial fraction:

$$\psi = 10 + (1-10)(0.03) = 10 - 0.27 = 9.73$$

**Example 2:** Achieve scaled speedup of 7 on 8 processors — what is the maximum serial fraction?

$$7 = 8 + (1-8)s \implies s \approx 0.143 \approx 14.3\%$$

**Example 3 (quiz):** 32 processors, 5% serial fraction:

$$\psi = 32 + (1-32)(0.05) = 32 - 1.55 = 30.45$$

---

## Amdahl vs. Gustafson-Barsis

| | Amdahl's Law | Gustafson-Barsis |
|---|---|---|
| Starting point | Fixed problem size | Fixed parallel execution time |
| As $p$ grows | Problem stays the same size | Problem size grows with $p$ |
| Speedup bound | Converges to $1/f$ | Grows linearly: $p + (1-p)s$ |
| Pessimism | Yes — serial fraction dominates | No — serial fraction stays small relative to scaled work |
| Use case | "How fast can I solve *this* problem?" | "How big a problem can I solve in *this* time?" |

---

## Roofline Model

A visual tool for bounding performance on a given architecture.

**X-axis:** Operational intensity (flops per byte of memory traffic)

**Y-axis:** Attainable performance (GFlops/s)

Two ceilings:
1. **Memory bandwidth ceiling** — diagonal slope determined by peak DRAM bandwidth (stream benchmark)
2. **Compute ceiling** — flat line at peak floating-point throughput

A kernel is **memory-bound** if its operational intensity is left of the ridge point; **compute-bound** if it's to the right.

*Reference: Williams, Waterman, and Patterson, CACM Vol 52 No 4, 2009.*
