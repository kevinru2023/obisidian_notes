---
title: "Fields"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/Judson12.pdf]]"
related:
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/rings]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, fields, MTH343]
---

# Fields

## Definition

A **field** is a commutative ring with unity where every nonzero element has a multiplicative inverse. Equivalently: $(F, +)$ and $(F \setminus \{0\}, \cdot)$ are both abelian groups.

Standard fields: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}_p$ ($p$ prime), $\mathbb{Q}(\sqrt{2})$, finite fields $GF(p^n)$.

---

## Field Extensions

An **extension field** $E$ of $F$ (written $F \subseteq E$ or $E/F$) is a field containing $F$ as a subfield.

**Algebraic element**: $\alpha \in E$ is algebraic over $F$ if it satisfies some nonzero polynomial $f(x) \in F[x]$.

**Transcendental**: not algebraic (e.g., $\pi$ and $e$ are transcendental over $\mathbb{Q}$).

**Minimal polynomial** of $\alpha$ over $F$: the monic irreducible polynomial in $F[x]$ of smallest degree having $\alpha$ as a root.

**Simple extension**: $F(\alpha)$ — smallest field containing $F$ and $\alpha$.
- If $\alpha$ is algebraic with minimal polynomial $p(x)$ of degree $n$: $F(\alpha) \cong F[x]/\langle p(x) \rangle$, with $[F(\alpha):F] = n$.

**Degree of extension**: $[E:F] = \dim_F(E)$ as a vector space over $F$.

**Tower law**: $[E:F] = [E:K] \cdot [K:F]$ for intermediate field $K$.

---

## Splitting Fields

The **splitting field** of $f(x) \in F[x]$ is the smallest extension $E/F$ in which $f$ factors completely into linear factors.

Splitting fields always exist and are unique up to isomorphism.

- Example: The splitting field of $x^2 + 1$ over $\mathbb{R}$ is $\mathbb{C}$ (degree $2$ extension).
- Example: The splitting field of $x^3 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2},\, \omega)$ where $\omega = e^{2\pi i/3}$ (degree $6$ extension).

---

## Finite Fields

**Theorem**: For every prime $p$ and positive integer $n$, there exists a unique (up to isomorphism) field of order $p^n$, denoted $GF(p^n)$ or $\mathbb{F}_{p^n}$.

Properties:
- Characteristic $p$ (i.e., $p \cdot 1 = 0$).
- Multiplicative group $GF(p^n) \setminus \{0\}$ is cyclic of order $p^n - 1$.
- $GF(p^n)$ is the splitting field of $x^{p^n} - x$ over $\mathbb{Z}_p$.

$GF(2^8)$ underlies AES encryption.

---

## Geometric Constructibility

A length is constructible (with compass and straightedge) iff it lies in a field extension of $\mathbb{Q}$ with degree a power of $2$.

**Impossibilities proven via field theory:**
- **Doubling the cube**: requires $\sqrt[3]{2}$, but $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3$ (not a power of $2$). ✗
- **Trisecting an angle**: e.g., trisecting $60°$ requires solving a cubic with no rational root. ✗
- **Squaring the circle**: requires $\pi$, which is transcendental over $\mathbb{Q}$. ✗
- **Regular $n$-gon**: constructible iff $n = 2^k \cdot p_1 \cdot p_2 \cdots$ where $p_i$ are distinct Fermat primes.

---

## Galois Theory (Overview)

For a splitting field $E$ over $F$:
- **Galois group** $\operatorname{Gal}(E/F)$ = group of automorphisms of $E$ fixing $F$ pointwise.
- $|\operatorname{Gal}(E/F)| = [E:F]$ for a Galois extension.

**Fundamental Theorem of Galois Theory**: There is an order-reversing bijection:

$$\text{Subgroups } H \le \operatorname{Gal}(E/F) \;\longleftrightarrow\; \text{Intermediate fields } K \text{ with } F \subseteq K \subseteq E$$

$$H \;\longmapsto\; \operatorname{Fix}(H) = \{x \in E : \sigma(x) = x \text{ for all } \sigma \in H\}$$

**Normal subgroups** $\leftrightarrow$ **Normal (Galois) intermediate extensions**.

**Application**: A polynomial $f(x) \in \mathbb{Q}[x]$ is solvable by radicals iff its Galois group is a solvable group. Since $A_5$ is simple (not solvable), the general quintic is not solvable by radicals.
