---
title: "Permutation Groups"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/Judson12.pdf]]"
  - "[[raw-sources/courses/MTH343/mth 343 handouts_3.pdf]]"
  - "[[raw-sources/web-clippings/Permutation Groups and Symmetric Groups  Abstract Algebra.md]]"
related:
  - "[[wiki/concepts/groups]]"
  - "[[wiki/courses/MTH343]]"
  - "[[wiki/concepts/symmetric-groups]]"
updated: 2026-04-24
tags: [abstract-algebra, permutations, groups, MTH343]
---

# Permutation Groups

## Definition

A **permutation** of a set $A$ is a bijection $\sigma : A \to A$.

The set of all permutations of $A$ under function composition forms a group — the **symmetric group** on $A$, denoted $S_A$.

When $A = \{1, 2, \ldots, n\}$, this group is written $S_n$ and called the **symmetric group of degree $n$**.

$$|S_n| = n!$$

---

## Group Axioms Verified

| Axiom | Why it holds |
|-------|-------------|
| **Closure** | Composition of bijections $A \to A$ is again a bijection $A \to A$ |
| **Associativity** | Function composition is always associative: $(f \circ g) \circ h = f \circ (g \circ h)$ |
| **Identity** | $\varepsilon : A \to A$ with $\varepsilon(x) = x$ — the identity function |
| **Inverses** | Every bijection $\sigma$ has an inverse function $\sigma^{-1}$, which is also a bijection |

---

## Two-Row Notation

A permutation on $\{1, \ldots, n\}$ can be written as a $2 \times n$ array:

$$\sigma = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix}$$

reads: $\sigma(1) = 2$, $\sigma(2) = 1$, $\sigma(3) = 3$.

---

## Cycle Notation

More compact representation. A **$k$-cycle** $(a_1\ a_2\ \cdots\ a_k)$ means:

$$a_1 \mapsto a_2 \mapsto \cdots \mapsto a_k \mapsto a_1$$

with all other elements fixed. Every permutation factors uniquely (up to order) into **disjoint cycles**.

**Examples** in $S_5$:
- $(1\ 3\ 5\ 2)$ — a 4-cycle; sends $1 \to 3,\ 3 \to 5,\ 5 \to 2,\ 2 \to 1$
- $(1\ 2)(3\ 4\ 5)$ — product of a 2-cycle and a 3-cycle

A **transposition** is a 2-cycle $(i\ j)$. Every permutation is a product of transpositions (not uniquely, but the parity of the number of transpositions is invariant).

---

## Even and Odd Permutations

A permutation is **even** if it can be written as a product of an even number of transpositions; **odd** otherwise.

The set of all even permutations of $S_n$ forms a normal subgroup called the **alternating group** $A_n$:

$$|A_n| = \frac{n!}{2}$$

$A_n$ is simple for $n \ge 5$ (Judson Ch. 10 — key result in Galois theory).

---

## The Symmetric Group $S_3$

The smallest non-abelian group: $|S_3| = 6$.

| Element | Two-row | Cycle | Order |
|---------|---------|-------|-------|
| $\varepsilon$ | $\begin{pmatrix}1&2&3\\1&2&3\end{pmatrix}$ | $()$ | 1 |
| $\alpha$ | $\begin{pmatrix}1&2&3\\1&3&2\end{pmatrix}$ | $(2\ 3)$ | 2 |
| $\beta$ | $\begin{pmatrix}1&2&3\\3&1&2\end{pmatrix}$ | $(1\ 3\ 2)$ | 3 |
| $\gamma$ | $\begin{pmatrix}1&2&3\\2&1&3\end{pmatrix}$ | $(1\ 2)$ | 2 |
| $\delta$ | $\begin{pmatrix}1&2&3\\2&3&1\end{pmatrix}$ | $(1\ 2\ 3)$ | 3 |
| $\kappa$ | $\begin{pmatrix}1&2&3\\3&2&1\end{pmatrix}$ | $(1\ 3)$ | 2 |

**Composition rule**: right permutation applies first. E.g., $\beta \circ \gamma$: apply $\gamma$ then $\beta$.

$$\beta \circ \gamma: 1 \xrightarrow{\gamma} 2 \xrightarrow{\beta} 1,\quad 2 \xrightarrow{\gamma} 1 \xrightarrow{\beta} 3,\quad 3 \xrightarrow{\gamma} 3 \xrightarrow{\beta} 2 \implies \beta \circ \gamma = \alpha$$

---

## Groups of Permutations

A **group of permutations** is any subgroup of a symmetric group $S_A$. It need not contain all permutations of $A$.

**Cayley's Theorem**: Every group $G$ is isomorphic to a subgroup of $S_{|G|}$. Permutation groups are thus universal — every abstract group can be realized as a group of permutations.

---

## Important Facts about $S_n$ (from course handout)

1. $|S_n| = n!$
2. Every element of $S_n$ can be written as a product of **disjoint cycles** (unique up to order). By convention, start each cycle with its smallest element.
3. Disjoint cycles **commute**.
4. Every element of $S_n$ can be written as a product of **transpositions** (2-cycles). Example: $(1234) = (14)(13)(12)$.
5. The number of transpositions in any decomposition is always even or always odd — **parity is invariant**.
6. The set $A_n = \{\sigma \in S_n \mid \sigma \text{ is a product of an even number of transpositions}\}$ is a subgroup.
7. $|A_n| = \dfrac{n!}{2}$

**Composition convention:** Apply right to left. For example, in $S_6$, the permutation $(245)(46)$ means: apply $(46)$ first, then $(245)$, giving $1\to1,\ 2\to4,\ 3\to3,\ 4\to6,\ 5\to2,\ 6\to5$.

---

## Key Facts

- $S_n$ is non-abelian for $n \ge 3$
- $S_1 \cong \{e\}$, $S_2 \cong \mathbb{Z}_2$
- Every element of $S_n$ has order equal to the LCM of its cycle lengths
- The dihedral group $D_n$ (symmetries of a regular $n$-gon) embeds naturally into $S_n$

---

## See Also

- [[wiki/concepts/symmetric-groups]] — dedicated page for $S_n$: 7 key facts, $S_3$ table, alternating group $A_n$, Cayley's theorem
- [[wiki/concepts/groups]] — general group theory, subgroups, Lagrange's theorem
- [[wiki/courses/MTH343]] — MTH343 course page; permutation groups covered in Ch. 5
- [[wiki/summaries/permutation-groups-video]] — video summary with $S_3$ composition table walkthrough
