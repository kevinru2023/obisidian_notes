---
title: "Cosets in Group Theory | Abstract Algebra (YouTube)"
type: summary
sources:
  - "[[raw-sources/web-clippings/Cosets in Group Theory  Abstract Algebra.md]]"
related:
  - "[[wiki/concepts/cosets]]"
  - "[[wiki/concepts/groups]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, cosets, groups, MTH343]
---

# Cosets in Group Theory — Video Summary

**Source**: YouTube — Wrath of Math, Abstract Algebra series
**URL**: https://www.youtube.com/watch?v=kthl-MhIf4s

---

## What the Video Covers

A self-contained introduction to cosets: definition, concrete examples, and a full proof that overlapping cosets must be equal. Teases Lagrange's theorem as the payoff.

1. **Definition** — left and right cosets; multiplicative vs. additive notation
2. **Finite example** — $\mathbb{Z}_4$ with $H = \{0, 2\}$, showing only two distinct cosets
3. **Infinite example** — $(\mathbb{R}, +)$ with $\mathbb{Z}$; coset $\mathbb{Z} + 0.5$
4. **Partition property** — cosets of $H$ partition $G$ (stated; proof deferred)
5. **Proof** — if $Ha \cap Hb \ne \emptyset$ then $Ha = Hb$
6. **Implication** — the identity coset $H$ is the only coset that is also a subgroup

---

## Key Takeaways

- A coset $xH$ (or $Hx$) is formed by composing a fixed group element with every element of the subgroup.
- Left vs. right cosets: same idea, different side. Be consistent. For abelian groups they're identical.
- Any two cosets are **equal or disjoint** — there's no partial overlap.
- Cosets partition $G$: every element of $G$ lives in exactly one coset.
- Only $H$ itself (the coset of the identity) can be a subgroup.
- This partition structure is what makes **Lagrange's theorem** work.

---

## Proof Summary: $Ha \cap Hb \ne \emptyset \implies Ha = Hb$

Assume $a \in Hb$, so $a = h_1 b$.

**$Ha \subseteq Hb$**: any $x = h_2 a = h_2 h_1 b \in Hb$ since $h_2 h_1 \in H$.

**$Hb \subseteq Ha$**: from $a = h_1 b$ get $b = h_1^{-1} a$, so any $y = h_3 b = h_3 h_1^{-1} a \in Ha$.

Both inclusions hold $\implies Ha = Hb$. $\blacksquare$

---

## Relation to Course Material

Corresponds to **Judson Ch. 6** (Cosets & Lagrange's Theorem). See:
- [[wiki/concepts/cosets]] — full concept page with all examples, proof, and Lagrange's theorem
- [[wiki/concepts/groups]] — general group theory reference
- [[wiki/courses/MTH343]] — course page and chapter map
