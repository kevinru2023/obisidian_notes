---
title: "Subgroups"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/mth 343 handouts_5.pdf]]"
related:
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/cyclic-groups]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, groups, subgroups, MTH343]
---

# Subgroups

## Definition

Let $G$ be a group with operation $\star$. A **subgroup** of $G$ is a subset $H \subseteq G$ that is itself a group under $\star$.

**Notation:** $H \leq G$ means $H$ is a subgroup of $G$.

**Key inherited properties:**
1. The identity element of $H$ equals the identity of $G$.
2. For any $h \in H$, the inverse of $h$ in $H$ equals its inverse in $G$.

---

## Subgroup Criteria

### Long Criterion
$H \subseteq G$ is a subgroup iff all three hold:
- **(L1)** $e \in H$
- **(L2)** $a, b \in H \Rightarrow a \star b \in H$
- **(L3)** $a \in H \Rightarrow a^{-1} \in H$

### Short Criterion
$H \subseteq G$ is a subgroup iff both hold:
- **(S1)** $e \in H$
- **(S2)** $a, b \in H \Rightarrow a \star b^{-1} \in H$

(S2) combines closure and inverses into a single condition.

### Finite Subgroup Criterion
If $G$ is **finite**, $H \subseteq G$ is a subgroup iff both hold:
- **(F1)** $e \in H$
- **(F2)** $a, b \in H \Rightarrow a \star b \in H$

Inverses come for free in finite groups: closure + finiteness forces $a^{|H|} = e$, so $a^{-1} = a^{|H|-1} \in H$.

---

## See Also

- [[wiki/concepts/groups]] — group axioms, normal subgroups, quotient groups
- [[wiki/concepts/cyclic-groups]] — subgroups of cyclic groups are cyclic
- [[wiki/courses/MTH343]] — MTH343 course page; subgroups covered in Ch. 3
