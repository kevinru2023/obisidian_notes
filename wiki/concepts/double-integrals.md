---
title: "Double Integrals"
type: concept
sources:
  - "[[raw-sources/courses/MTH254/Vector Calculus I Week 6 Lecture.pdf]]"
related:
  - "[[wiki/courses/MTH254]]"
updated: 2026-04-16
tags: [math, calculus, integration, multivariable]
---

# Double Integrals

## Definition

Let $f(x, y)$ be defined over a rectangular region $R$ in the $xy$-plane. Partition $R$ into $n$ sub-rectangles with areas $\Delta A_i$ and sample points $(x_i, y_i)$. The **double integral** is

$$\iint_R f(x, y)\,dA = \lim_{\substack{n \to \infty \\ \Delta A_i \to 0}} \sum_{i=1}^{n} f(x_i, y_i)\,\Delta A_i$$

when the limit exists for all such partitions.

The result is the **net signed volume** between $z = f(x,y)$ and the $xy$-plane over $R$ — positive where $f \ge 0$, negative where $f < 0$.

## Fubini's Theorem

**Rectangular regions:** If $f$ is continuous over $R = [x_1, x_2] \times [y_1, y_2]$,

$$\iint_R f(x, y)\,dA = \int_{x_1}^{x_2} \int_{y_1}^{y_2} f(x, y)\,dy\,dx = \int_{y_1}^{y_2} \int_{x_1}^{x_2} f(x, y)\,dx\,dy$$

The two orders of integration are interchangeable — pick whichever is easier to evaluate.

**Example:**
$$\iint_{[-2,2]\times[-2,2]} x^2 + y^2\,dA = \int_{-2}^{2}\int_{-2}^{2} x^2 + y^2\,dy\,dx = \frac{128}{3} \approx 42.67$$

## General Regions

**Type I** — bounded by functions of $x$: $a \le x \le b$, $g(x) \le y \le h(x)$

$$\iint_R f\,dA = \int_a^b \int_{g(x)}^{h(x)} f(x,y)\,dy\,dx$$

**Type II** — bounded by functions of $y$: $c \le y \le d$, $\ell(y) \le x \le m(y)$

$$\iint_R f\,dA = \int_c^d \int_{\ell(y)}^{m(y)} f(x,y)\,dx\,dy$$

A region that is neither pure Type I nor Type II can be split: $\iint_R = \iint_{R_1} + \iint_{R_2}$.

## Switching Order of Integration

When the antiderivative in the chosen order doesn't exist in closed form, re-describe the region and swap the order.

**Example:** $\displaystyle\int_0^4 \int_{x/2}^{2} e^{-y^2}\,dy\,dx$

$e^{-y^2}$ has no elementary antiderivative in $y$. Re-describe: $0 \le x \le 4$, $x/2 \le y \le 2$ becomes $0 \le y \le 2$, $0 \le x \le 2y$.

$$\int_0^4 \int_{x/2}^{2} e^{-y^2}\,dy\,dx = \int_0^2 \int_0^{2y} e^{-y^2}\,dx\,dy = \int_0^2 2y e^{-y^2}\,dy = 1 - e^{-4}$$

## Useful Identities

| Identity | Formula |
|---|---|
| Area recovery | $\iint_R 1\,dA = A(R)$ |
| Average value | $\bar{f} = \dfrac{1}{A}\iint_R f(x,y)\,dA$ |
| Additivity | $\iint_R f\,dA = \iint_{R_1} f\,dA + \iint_{R_2} f\,dA$ |

## Riemann Sum Approximations

Splitting $[-2,2]\times[-2,2]$ into sub-rectangles and evaluating $f(x,y) = x^2+y^2$ at sample points:

| Sub-rectangles | Riemann sum | Exact ($\frac{128}{3}$) |
|---|---|---|
| 16 | 48.00 | 42.67 |
| 25 | 40.96 | 42.67 |
| 100 | 42.24 | 42.67 |
| 400 | 42.56 | 42.67 |
| 1600 | 42.64 | 42.67 |

Convergence to exact value as sub-rectangles increase.
