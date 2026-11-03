---
title: "Abstract Algebra: Theory and Applications (Judson, 2012)"
type: summary
sources:
  - "[[raw-sources/courses/MTH343/Judson12.pdf]]"
related:
  - "[[wiki/courses/MTH343]]"
  - "[[wiki/concepts/groups]]"
  - "[[wiki/concepts/rings]]"
  - "[[wiki/concepts/fields]]"
updated: 2026-04-16
tags: [abstract-algebra, groups, rings, fields, MTH343]
---

# Abstract Algebra: Theory and Applications — Judson (2012)

Open-source undergraduate abstract algebra textbook by Thomas W. Judson (Stephen F. Austin State University). Balances theory and applications; emphasizes groups, rings, and fields with practical examples from cryptography and coding theory.

---

## Structure Overview

The book is organized in three broad arcs:

**Groups (Ch. 1–15)**
| Ch | Topic |
|----|-------|
| 1 | Preliminaries — proofs, sets, equivalence relations, functions |
| 2 | The Integers — induction, division algorithm, GCD, primes |
| 3 | Groups — definitions, subgroups, symmetry groups |
| 4 | Cyclic Groups — generators, order, complex roots of unity |
| 5 | Permutation Groups — symmetric groups S_n, dihedral groups D_n |
| 6 | Cosets & Lagrange's Theorem — cosets, index, Fermat's/Euler's theorems |
| 7 | Cryptography — Caesar cipher, RSA (application of group theory) |
| 8 | Algebraic Coding Theory — error-correcting codes, linear codes, parity-check matrices |
| 9 | Isomorphisms — group isomorphism, Cayley's theorem, direct products |
| 10 | Normal Subgroups & Factor Groups — quotient groups, simplicity of A_n |
| 11 | Homomorphisms — kernel, image, isomorphism theorems |
| 12 | Matrix Groups & Symmetry — GL_n, SL_n, crystallographic groups |
| 13 | Structure of Groups — finite abelian groups, solvable groups |
| 14 | Group Actions — orbits, stabilizers, class equation, Burnside counting |
| 15 | Sylow Theorems — p-subgroups, existence/conjugacy of Sylow subgroups |

**Rings (Ch. 16–19)**
| Ch | Topic |
|----|-------|
| 16 | Rings — definitions, integral domains, fields, ideals, homomorphisms |
| 17 | Polynomials — polynomial rings, division algorithm, irreducibility |
| 18 | Integral Domains — fields of fractions, UFDs, PIDs, Euclidean domains |
| 19 | Lattices & Boolean Algebras — partial orders, Boolean algebras, electrical circuits |

**Fields (Ch. 20–23)**
| Ch | Topic |
|----|-------|
| 20 | Vector Spaces — basis, dimension, linear independence |
| 21 | Fields — extension fields, splitting fields, geometric constructions |
| 22 | Finite Fields — structure, polynomial codes |
| 23 | Galois Theory — field automorphisms, Galois group, fundamental theorem |

---

## Key Theorems

- **Lagrange's Theorem** — The order of a subgroup H divides the order of a finite group G.
- **Cayley's Theorem** — Every group is isomorphic to a group of permutations.
- **First Isomorphism Theorem** — $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$ for any homomorphism $\varphi$.
- **Sylow Theorems** — Existence, conjugacy, and number of Sylow $p$-subgroups.
- **Fundamental Theorem of Finite Abelian Groups** — Every finite abelian group is a direct product of cyclic groups of prime-power order.
- **Fundamental Theorem of Galois Theory** — Bijection between subfields of a splitting field and subgroups of its Galois group.

---

## Applications Covered

- **Cryptography (Ch. 7)**: RSA relies on Euler's theorem ($\varphi(n)$); private/public key construction.
- **Error-correcting codes (Ch. 8)**: Hamming codes, linear codes over $\mathbb{Z}_2$.
- **Geometric constructions (Ch. 21)**: Why trisecting an angle and doubling the cube are impossible (field extensions).
- **Finite fields (Ch. 22)**: Used in modern symmetric cryptography (AES uses $GF(2^8)$).

---

## Prerequisites

- Proof techniques (direct, contrapositive, contradiction, induction)
- Basic set theory and functions
- Elementary linear algebra (matrices, determinants) for select sections

---

## Notes on Coverage

A typical one-semester course uses Ch. 1–6, 9–11, 13, 16–18, 20–21. The book contains significantly more material than a single semester covers — Ch. 7–8 (applications), 14–15 (advanced group theory), and 22–23 (Galois theory) are often omitted or covered partially.
