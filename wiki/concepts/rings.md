---
title: "Rings"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/Judson12.pdf]]"
related:
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/fields]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, rings, MTH343]
---

# Rings

## Definition

A **ring** is a set $R$ with two binary operations $+$ (addition) and $\cdot$ (multiplication) satisfying:

1. $(R, +)$ is an **abelian group** (closure, associativity, identity $0$, inverses, commutativity)
2. Multiplication is **associative**: $(ab)c = a(bc)$
3. **Distributivity**: $a(b+c) = ab+ac$ and $(b+c)a = ba+ca$

A ring is **commutative** if $ab = ba$ for all $a, b$. Has a **unity** if $\exists\, 1 \in R$ with $1 \cdot a = a \cdot 1 = a$.

---

## Hierarchy of Ring Types

```
Ring
 └── Commutative ring with unity
      └── Integral domain (no zero divisors)
           └── Principal ideal domain (PID)
                └── Euclidean domain
                     └── Field
```

**Zero divisors**: $a \ne 0$ with $ab = 0$ for some $b \ne 0$.

**Integral domain**: commutative ring with unity and no zero divisors.

**Field**: commutative ring with unity where every nonzero element is a unit.

---

## Standard Examples

| Ring | Type |
|------|------|
| $(\mathbb{Z}, +, \cdot)$ | Integral domain (not a field) |
| $(\mathbb{Z}_n, +, \cdot)$ | Field iff $n$ is prime |
| $(\mathbb{Q}, +, \cdot)$ | Field |
| $(R[x], +, \cdot)$ | Integral domain (polynomial ring) |
| $M_n(\mathbb{R})$ | Non-commutative ring with unity |
| $\mathbb{Z}[i]$ (Gaussian integers) | Euclidean domain |

---

## Ideals

An **ideal** $I \subseteq R$ is a subring satisfying: $rI \subseteq I$ and $Ir \subseteq I$ for all $r \in R$.
- **Left ideal**: $rI \subseteq I$; **right ideal**: $Ir \subseteq I$; **two-sided ideal**: both.

**Principal ideal**: $\langle a \rangle = \{ra : r \in R\}$ in a commutative ring.

**Quotient ring**: $R/I$ — cosets of $I$ under $+$, with $(a+I)(b+I) = ab+I$.

**Maximal ideal**: $I$ is maximal iff $R/I$ is a field.

**Prime ideal**: $I$ is prime iff $R/I$ is an integral domain. Equivalently: $ab \in I \Rightarrow a \in I$ or $b \in I$.

Every maximal ideal is prime (in commutative rings with unity).

---

## Ring Homomorphisms

**Homomorphism** $\varphi: R \to S$ — preserves both $+$ and $\cdot$:
$$\varphi(a+b) = \varphi(a)+\varphi(b) \quad \text{and} \quad \varphi(ab) = \varphi(a)\varphi(b)$$

$\ker(\varphi)$ is always an ideal of $R$.

**First Isomorphism Theorem** for rings: $R/\ker(\varphi) \cong \operatorname{im}(\varphi)$

---

## Polynomial Rings

$R[x]$ — polynomials with coefficients in ring $R$.

**Division Algorithm for polynomials** (when $R$ is a field $F$): For $f, g \in F[x]$ with $g \ne 0$, $\exists$ unique $q, r$ with
$$f = qg + r \quad \text{and} \quad \deg(r) < \deg(g)$$

**Irreducible polynomial**: $p(x) \in F[x]$ with no nontrivial factorization in $F[x]$. Analogous to primes in $\mathbb{Z}$.

**Factor theorem**: $(x - a) \mid f(x)$ iff $f(a) = 0$. Roots correspond to linear factors.

$F[x]/\langle p(x) \rangle$ is a field iff $p(x)$ is irreducible over $F$.

---

## Factorization in Integral Domains

**Unit**: element with a multiplicative inverse.

**Irreducible**: non-unit $a$ with $a = bc \Rightarrow b$ or $c$ is a unit.

**Prime**: non-unit $p$ with $p \mid ab \Rightarrow p \mid a$ or $p \mid b$. (Prime $\Rightarrow$ irreducible; converse holds in UFDs.)

**UFD** (Unique Factorization Domain): every non-unit factors uniquely into irreducibles (up to order and units).

**PID** (Principal Ideal Domain): every ideal is principal ($\langle a \rangle$ for some $a$).

**Euclidean Domain**: has a norm function with a division algorithm. E.g.: $\mathbb{Z}$ (norm $= |\cdot|$), $F[x]$ (norm $= \deg$).

$$\text{Euclidean Domain} \subseteq \text{PID} \subseteq \text{UFD}$$
