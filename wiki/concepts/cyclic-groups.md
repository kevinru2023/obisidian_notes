---
title: "Cyclic Groups"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/mth 343 handouts_4.pdf]]"
related:
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/subgroups]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, groups, cyclic-groups, MTH343]
---

# Cyclic Groups

## Multiplicative Notation

For abstract groups we use multiplicative notation: write $xy$ for $x \star y$, write $1$ for the identity $e$, and $x^{-1}$ for the inverse. Powers: $x^n$ means $n$-fold product, $x^{-n} = (x^{-1})^n$, $x^0 = 1$.

---

## Definitions

**Order of a group.** The **order** of $G$, written $|G|$, is the number of elements. A group may have finite or infinite order.

**Order of an element.** The **order** of $a \in G$, written $|a|$, is the least positive integer $n$ such that $a^n = 1$. If no such $n$ exists, $a$ has **infinite order**.

**Cyclic group.** $G$ is **cyclic** if $G = \{a^n \mid n \in \mathbb{Z}\}$ for some $a \in G$. The element $a$ is a **cyclic generator** and we write $G = \langle a \rangle$.

A finite group $G$ is cyclic iff there exists $a \in G$ with $|a| = |G|$.

---

## Properties of Cyclic Groups

1. Every cyclic group is **abelian**.
2. Every subgroup of a cyclic group is **cyclic**.
3. If $G = \langle a \rangle$ has order $n$, then for any positive integer $k$:

$$|a^k| = \frac{n}{\gcd(k,n)}$$

---

## Properties of $\mathbb{Z}/n\mathbb{Z}$

1. $\mathbb{Z}/n\mathbb{Z}$ is cyclic for all positive integers $n$.
2. $\mathbb{Z}/n\mathbb{Z} = \langle [k] \rangle$ if and only if $\gcd(k,n) = 1$.
3. $(\mathbb{Z}/n\mathbb{Z})^\times$ is **not** cyclic for some $n$ (e.g., $(\mathbb{Z}/8\mathbb{Z})^\times \cong \mathbb{Z}_2 \times \mathbb{Z}_2$).

---

## See Also

- [[wiki/concepts/groups]] — general group theory, subgroups, Lagrange's theorem
- [[wiki/concepts/subgroups]] — subgroup criteria; subgroups of cyclic groups are cyclic
- [[wiki/courses/MTH343]] — MTH343 course page; cyclic groups covered in Ch. 4
