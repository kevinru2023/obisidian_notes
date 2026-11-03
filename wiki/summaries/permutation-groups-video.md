---
title: "Permutation Groups and Symmetric Groups | Abstract Algebra (YouTube)"
type: summary
sources:
  - "[[raw-sources/web-clippings/Permutation Groups and Symmetric Groups  Abstract Algebra.md]]"
related:
  - "[[wiki/concepts/permutation-groups]]"
  - "[[wiki/concepts/groups]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, permutations, groups, MTH343]
---

# Permutation Groups and Symmetric Groups — Video Summary

**Source**: YouTube lecture on Abstract Algebra (permutation groups chapter)
**URL**: https://www.youtube.com/watch?v=NwqCi63p2ik

---

## What the Video Covers

A self-contained walkthrough of permutation groups and symmetric groups for an undergraduate abstract algebra course. Covers:

1. **Definition of a permutation** — a bijection from a set to itself
2. **Group axioms verified** for the set of all permutations under composition:
   - Closure, associativity, identity ($\varepsilon$), inverses
3. **Symmetric group notation** — $S_A$ (all permutations of set $A$), $S_n$ (permutations of $\{1, \ldots, n\}$)
4. **Worked example**: Full $S_3$ composition table with all 6 elements
5. **Inverse computation**: showing $\alpha$ is its own inverse in $S_3$

---

## Key Points

- A **permutation** is formally a bijection $\sigma : A \to A$, not just an informal "rearrangement."
- The operation is **function composition**; the right-hand permutation acts first.
- Composition of bijections is a bijection → **closure** holds automatically.
- The **identity permutation** $\varepsilon$ satisfies $\varepsilon(x) = x$ for all $x$.
- Every permutation has an **inverse permutation** (since bijections are invertible).
- $|S_n| = n!$ — there are $n!$ permutations on $n$ elements.
- A **group of permutations** can be any subgroup of $S_A$, not necessarily the full symmetric group.

---

## S3 Composition Table (Summary)

The six elements of $S_3$ on $\{1,2,3\}$:

| Name | Mapping |
|------|---------|
| $\varepsilon$ | $1 \to 1,\ 2 \to 2,\ 3 \to 3$ (identity) |
| $\alpha$ | $1 \to 1,\ 2 \to 3,\ 3 \to 2$ |
| $\beta$ | $1 \to 3,\ 2 \to 1,\ 3 \to 2$ |
| $\gamma$ | $1 \to 2,\ 2 \to 1,\ 3 \to 3$ |
| $\delta$ | $1 \to 2,\ 2 \to 3,\ 3 \to 1$ |
| $\kappa$ | $1 \to 3,\ 2 \to 2,\ 3 \to 1$ |

Notable inverse pairs: $\delta$ and $\beta$ are inverses; $\alpha$ is its own inverse ($\alpha^2 = \varepsilon$).

---

## Relation to Course Material

This video is supplementary to **Judson Ch. 5** (Permutation Groups). See:
- [[wiki/concepts/permutation-groups]] — full concept page with cycle notation and Cayley's theorem
- [[wiki/concepts/groups]] — general group theory
- [[wiki/courses/MTH343]] — course page and chapter map
