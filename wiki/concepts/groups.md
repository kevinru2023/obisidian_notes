---
title: "Groups"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/Judson12.pdf]]"
  - "[[raw-sources/courses/MTH343/mth 343 handouts_6.pdf]]"
  - "[[raw-sources/courses/MTH343/mth 343 handouts_9.pdf]]"
related:
  - "[[wiki/concepts/rings]]"
  - "[[wiki/concepts/fields]]"
  - "[[wiki/concepts/permutation-groups]]"
  - "[[wiki/concepts/cosets]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-16
tags: [abstract-algebra, groups, MTH343]
---

# Groups

## Definition

A **binary operation** on $X$ is a function $\star : X \times X \to X$. It is *associative* if $a \star (b \star c) = (a \star b) \star c$; *commutative* if $a \star b = b \star a$. A subset $Y \subseteq X$ is *closed under* $\star$ if $\star$ restricts to a binary operation on $Y$.

A **group** is a set $G$ with a binary operation $\star$ satisfying:

- **(G1)** $\star$ is **associative**.
- **(G2)** There exists an **identity** $e \in G$ such that $a \star e = e \star a = a$ for all $a \in G$.
- **(G3)** For each $a \in G$ there exists an **inverse** $a^{-1} \in G$ with $a \star a^{-1} = a^{-1} \star a = e$.

A group is **abelian** if additionally $a \star b = b \star a$ for all $a, b$. A **finite group** is one where $G$ is a finite set.

### Basic Group Facts

Let $(G, \star)$ be a group:

1. The identity $e$ is **unique**.
2. For each $a \in G$, the inverse $a^{-1}$ is **unique**; we write it $a^{-1}$.
3. $(a^{-1})^{-1} = a$ for all $a$.
4. $(a \star b)^{-1} = b^{-1} \star a^{-1}$ for all $a, b$.
5. Products $a_1 \star \cdots \star a_n$ are independent of parenthesization (generalized associativity).
6. **Cancellation**: $a \star b = a \star c \Rightarrow b = c$; $b \star a = c \star a \Rightarrow b = c$.

**Notation:** For generic groups write $ab$ for $a \star b$, $1$ for $e$, $a^{-1}$ for the inverse (multiplicative). For abelian groups write $a + b$, $0$, $-a$ (additive).

**Order** of a group: $|G|$ (number of elements; may be infinite).
**Order** of an element $g$: smallest positive $n$ such that $g^n = e$.

---

## Standard Examples

| Group                                                             | Operation                 | Abelian?       | Order        |
| ----------------------------------------------------------------- | ------------------------- | -------------- | ------------ |
| $(\mathbb{Z}, +)$                                                 | addition                  | yes            | $\infty$     |
| $(\mathbb{Z}_n, +)$                                               | addition mod $n$          | yes            | $n$          |
| $(\mathbb{Z}_n^*, \cdot)$                                         | mult mod $n$ (units only) | yes            | $\varphi(n)$ |
| $(\mathbb{R}\setminus\{0\}, \cdot)$                               | multiplication            | yes            | $\infty$     |
| $GL_n(\mathbb{R}) = \{A \in M_n(\mathbb{R}) \mid \det A \neq 0\}$ | matrix multiplication     | no ($n \ge 2$) | $\infty$     |
| $SL_n(\mathbb{R}) = \{A \in GL_n(\mathbb{R}) \mid \det A = 1\}$   | matrix multiplication     | no ($n \ge 2$) | $\infty$     |
| $S_n$                                                             | function composition      | no ($n \ge 3$) | $n!$         |
| $D_n$                                                             | symmetries of $n$-gon     | no ($n \ge 3$) | $2n$         |
| $A_n$                                                             | even permutations         | no ($n \ge 4$) | $n!/2$       |

---

## Subgroups

**Subgroup criterion**: $H \le G$ iff $H$ is nonempty and for all $a, b \in H$, $ab^{-1} \in H$.

**Generated subgroup**: $\langle S \rangle$ = smallest subgroup containing set $S$.

**Cyclic group**: $G = \langle g \rangle$ for some $g$. Every cyclic group is abelian.
- Cyclic groups of the same order are isomorphic: $\mathbb{Z}_n$ is the unique cyclic group of order $n$.
- Subgroups of cyclic groups are cyclic (Theorem 4.3 in Judson).

**Center**: $Z(G) = \{g \in G : gx = xg \text{ for all } x \in G\}$ — always a normal abelian subgroup.

---

## Cosets & Lagrange's Theorem

For $H \le G$ and $a \in G$:
- **Left coset**: $aH = \{ah : h \in H\}$
- **Right coset**: $Ha = \{ha : h \in H\}$

Cosets partition $G$. All cosets of $H$ have the same size $|H|$.

**Lagrange's Theorem**: If $G$ is finite, then $|H|$ divides $|G|$ and $[G:H] = |G|/|H|$.

**Corollary**: The order of any element $g \in G$ divides $|G|$. In particular, $g^{|G|} = e$.

**Fermat's Little Theorem** (group theory version): For prime $p$ and $\gcd(a,p) = 1$:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Euler's Theorem**: For $\gcd(a,n) = 1$:
$$a^{\varphi(n)} \equiv 1 \pmod{n}$$

---

## Normal Subgroups & Quotient Groups

**Normal subgroup**: $N \trianglelefteq G$ if $gNg^{-1} = N$ for all $g \in G$.
Equivalently: left cosets = right cosets ($gN = Ng$).

Every subgroup of an abelian group is normal. The kernel of any homomorphism is normal.

**Quotient group** $G/N$: cosets of $N$ with operation $(aN)(bN) = (ab)N$. Well-defined iff $N \trianglelefteq G$.

**Simple group**: $G$ with no proper nontrivial normal subgroups. $A_n$ is simple for $n \ge 5$ (key result for Galois theory).

---

## Homomorphisms

**Homomorphism** $\varphi: G \to H$ — map preserving the operation: $\varphi(ab) = \varphi(a)\varphi(b)$.

- **Kernel**: $\ker(\varphi) = \{g \in G : \varphi(g) = e_H\}$ — always a normal subgroup of $G$
- **Image**: $\operatorname{im}(\varphi) = \varphi(G)$ — a subgroup of $H$
- **Isomorphism**: bijective homomorphism; $G \cong H$

**First Isomorphism Theorem**: $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$

**Second Isomorphism Theorem**: If $H \le G$ and $N \trianglelefteq G$, then $H/(H \cap N) \cong HN/N$

**Third Isomorphism Theorem**: If $N \trianglelefteq M \trianglelefteq G$ and $N \trianglelefteq G$, then $(G/N)/(M/N) \cong G/M$

**Cayley's Theorem**: Every group $G$ is isomorphic to a subgroup of $S_{|G|}$.

---

## Group Actions

A **group action** of $G$ on set $X$: map $G \times X \to X$, written $g \cdot x$, satisfying:
- $e \cdot x = x$
- $(gh) \cdot x = g \cdot (h \cdot x)$

**Orbit** of $x$: $\operatorname{Orb}(x) = \{g \cdot x : g \in G\}$

**Stabilizer** of $x$: $\operatorname{Stab}(x) = \{g \in G : g \cdot x = x\}$ — a subgroup of $G$

**Orbit-Stabilizer Theorem**:
$$|G| = |\operatorname{Orb}(x)| \cdot |\operatorname{Stab}(x)|$$

**Class Equation**:
$$|G| = |Z(G)| + \sum_i [G : C_G(g_i)]$$
(sum over conjugacy class representatives outside the center)

**Burnside's Lemma**: Number of distinct orbits $= \dfrac{1}{|G|} \displaystyle\sum_{g \in G} |\operatorname{Fix}(g)|$

---

## Sylow Theorems

For a finite group $G$ with $|G| = p^k \cdot m$ ($p$ prime, $p \nmid m$):

1. **Existence**: $G$ has a subgroup of order $p^k$ (a Sylow $p$-subgroup).
2. **Conjugacy**: All Sylow $p$-subgroups are conjugate.
3. **Number**: The number of Sylow $p$-subgroups $n_p$ satisfies $n_p \equiv 1 \pmod{p}$ and $n_p \mid m$.

Key use: proving groups of certain orders cannot be simple, or classifying groups of small order.

---

## Structure of Finite Abelian Groups

**Fundamental Theorem**: Every finite abelian group is isomorphic to a direct product of cyclic groups of prime-power order:

$$G \cong \mathbb{Z}_{p_1^{a_1}} \times \mathbb{Z}_{p_2^{a_2}} \times \cdots \times \mathbb{Z}_{p_k^{a_k}}$$

This decomposition is unique up to reordering.
