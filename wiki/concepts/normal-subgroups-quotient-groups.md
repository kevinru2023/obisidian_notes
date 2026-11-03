---
title: "Normal Subgroups and Quotient Groups"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/normal subgroups and quotient groups handout.pdf]]"
related:
  - "[[wiki/concepts/subgroups]]"
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/group-homomorphisms]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-30
tags: [abstract-algebra, groups, normal-subgroups, quotient-groups, MTH343]
---

# Normal Subgroups and Quotient Groups

## Normal Subgroup

Let $G$ be a group. A subgroup $H \leq G$ is a **normal subgroup** if

$$aH = Ha \quad \text{(as sets) for all } a \in G$$

Equivalently: $aHa^{-1} = H$ for all $a \in G$.

**Notation:** $H \trianglelefteq G$ when $H$ is normal in $G$.

### Normality Test

$H \leq G$ is normal **if and only if** for every $g \in G$ and $h \in H$:

$$ghg^{-1} \in H$$

This is the most practical check: just verify conjugation stays inside $H$.

### Normality Facts

1. Any subgroup of an **abelian group** is normal (since $aH = Ha$ is immediate from commutativity).
2. Any subgroup of **index 2** is normal. (The only two left cosets are $H$ and $aH$; the only two right cosets are $H$ and $Ha$ — so $aH = Ha$ is forced.)

---

## The Set of Cosets

Let $G$ be a group and $H \leq G$. The **set of left cosets** of $H$ in $G$ is:

$$G/H = \{aH : a \in G\}$$

---

## Coset Operation

Define multiplication on $G/H$ by:

$$(aH)(bH) = (ab)H$$

This is a **well-defined** operation on $G/H$ **if and only if** $H \trianglelefteq G$.

**Why normality is needed:** If $H$ is not normal, the result $(ab)H$ may depend on the choice of representatives $a, b$, not just their cosets. Normality $gH = Hg$ is exactly what makes the product independent of representatives.

---

## Quotient (Factor) Group Theorem

Let $G$ be a group and $H \trianglelefteq G$. Then $G/H$ with the coset operation

$$(aH)(bH) = (ab)H$$

is a **group** — called the **quotient group** (or **factor group**) of $G$ by $H$.

| Element of $G/H$ | Role in the group |
|---|---|
| Cosets $aH$ | Elements |
| $H = eH$ | Identity element |
| $(aH)^{-1} = a^{-1}H$ | Inverse of $aH$ |

**Order of the quotient group:** $|G/H| = [G:H] = |G|/|H|$ (when $G$ is finite).

---

## Connection to Homomorphisms

The kernel of any group homomorphism is always a normal subgroup. Conversely, every normal subgroup arises as a kernel — via the **natural projection** $\pi: G \to G/H$ defined by $\pi(g) = gH$.

See [[wiki/concepts/group-homomorphisms]] for the First Isomorphism Theorem, which ties $G/\ker(\varphi)$ to the image of $\varphi$.

---

## Examples

**$\mathbb{Z}/n\mathbb{Z}$:** The subgroup $n\mathbb{Z} \trianglelefteq \mathbb{Z}$ (integers are abelian). The quotient $\mathbb{Z}/n\mathbb{Z}$ is the familiar group of residues mod $n$.

**$A_n \trianglelefteq S_n$:** The alternating group has index 2 in $S_n$, so it is normal by Normality Fact 2.

**$SL_n \trianglelefteq GL_n$:** $SL_n = \ker(\det)$, hence normal as a kernel of a homomorphism.

---

## See Also

- [[wiki/concepts/subgroups]] — subgroup criteria
- [[wiki/concepts/groups]] — cosets, Lagrange's theorem, brief normal subgroup overview
- [[wiki/concepts/group-homomorphisms]] — kernel/image, First Isomorphism Theorem
- [[wiki/courses/MTH343]] — MTH343 course page; quotient groups covered in Ch. 10
