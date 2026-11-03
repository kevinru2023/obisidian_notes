---
title: "Group Homomorphisms and Isomorphisms"
type: concept
sources:
  - "[[raw-sources/courses/MTH343/mth 343 handouts_1.pdf]]"
  - "[[raw-sources/courses/MTH343/first iso handout.pdf]]"
related:
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/cyclic-groups]]"
  - "[[wiki/concepts/normal-subgroups-quotient-groups]]"
  - "[[wiki/courses/MTH343]]"
updated: 2026-04-30
tags: [abstract-algebra, groups, homomorphisms, isomorphisms, MTH343]
---

# Group Homomorphisms and Isomorphisms

## Group Homomorphism

A **group homomorphism** from $(G, \star)$ to $(H, \heartsuit)$ is a function $\phi : G \to H$ such that for all $a, b \in G$:

$$\phi(a \star b) = \phi(a) \heartsuit \phi(b)$$

### Properties of Homomorphisms

Let $\phi : G \to H$ be a group homomorphism.

1. $\phi(1_G) = 1_H$ (identity maps to identity).
2. $\phi(a^{-1}) = (\phi(a))^{-1}$ for all $a \in G$.
3. $\phi(a^n) = (\phi(a))^n$ for all $n \in \mathbb{Z}$, $a \in G$.
4. If $K \leq G$ is a subgroup, then $\phi(K) \leq H$ (images of subgroups are subgroups).
5. The **kernel** $\ker(\phi) = \{g \in G \mid \phi(g) = e_H\}$ is a subgroup of $G$ (and a normal subgroup).

---

## Group Isomorphism

A **group isomorphism** from $G$ to $H$ is a *bijective* group homomorphism $\phi : G \to H$. We write $G \cong H$.

### Properties of Isomorphisms

Let $\phi : G \to H$ be a group isomorphism.

1. $\phi^{-1} : H \to G$ is also an isomorphism.
2. $|a| = |\phi(a)|$ for all $a \in G$ (element orders are preserved).
3. $a, b \in G$ commute $\Leftrightarrow$ $\phi(a), \phi(b) \in H$ commute. In particular, $G$ is abelian iff $H$ is abelian.
4. $G = \langle a \rangle \Leftrightarrow H = \langle \phi(a) \rangle$. In particular, $G$ is cyclic iff $H$ is cyclic.
5. If $G$ is finite, $G$ and $H$ have exactly the same number of elements of each order.

---

## Group Automorphism

A **group automorphism** of $G$ is a group isomorphism $G \to G$.

---

## Proving Groups Are Not Isomorphic

To show $G \not\cong H$, find an isomorphism-invariant property that distinguishes them:

1. $|G| \neq |H|$ (different orders).
2. One is cyclic, the other is not.
3. One is abelian, the other is not.
4. The number of elements of some given order differs between $G$ and $H$.

---

---

## Kernel and Image

Let $\varphi: G \to H$ be a group homomorphism. The **image** and **kernel** are:

$$\operatorname{im}(\varphi) = \varphi(G) = \{\varphi(g) : g \in G\}$$

$$\ker(\varphi) = \{g \in G : \varphi(g) = e_H\}$$

### Properties

1. $\operatorname{im}(\varphi) \leq H$ — the image is a subgroup of $H$.
2. $\ker(\varphi) \trianglelefteq G$ — the kernel is a **normal** subgroup of $G$.
3. $\varphi$ is **injective** if and only if $\ker(\varphi) = \{e_G\}$.

---

## First Isomorphism Theorem

**Natural Projection Map.** Let $G$ be a group and $H \trianglelefteq G$. Define $\pi: G \to G/H$ by $\pi(g) = gH$. Then $\pi$ is a surjective group homomorphism with $\ker(\pi) = H$.

**First Isomorphism Theorem.** Let $\varphi: G \to H$ be a group homomorphism with $K = \ker(\varphi)$. Then:

$$G/K \cong \operatorname{im}(\varphi)$$

This isomorphism is realized by $\psi: G/K \to \operatorname{im}(\varphi)$ defined by $\psi(gK) = \varphi(g)$.

Moreover, the maps satisfy the **commutative diagram**:

$$\varphi = \psi \circ \pi$$

where $\pi: G \to G/K$ is the natural projection. In other words, $\varphi$ factors through the quotient.

**Takeaway:** Every homomorphism is "the same as" the natural projection onto the quotient by its kernel, followed by an isomorphism onto the image.

---

## See Also

- [[wiki/concepts/groups]] — general group theory, cosets, Lagrange's theorem
- [[wiki/concepts/normal-subgroups-quotient-groups]] — normal subgroup definition, quotient group construction
- [[wiki/concepts/cyclic-groups]] — cyclicity is preserved by isomorphisms
- [[wiki/courses/MTH343]] — MTH343 course page; homomorphisms covered in Ch. 11
