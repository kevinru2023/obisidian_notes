---
title: "Alpha-Beta Pruning"
type: concept
sources:
  - "[[raw-sources/Lecture8_Adversarial_Search.pdf]]"
related:
  - "[[wiki/concepts/adversarial-search]]"
  - "[[wiki/courses/CS331]]"
updated: 2026-10-31
tags: [AI, adversarial-search, game-trees, minimax, alpha-beta, pruning, CS331]
---

# Alpha-Beta Pruning

Alpha-beta pruning computes the **same minimax value** as plain [[wiki/concepts/adversarial-search|minimax]], but explores fewer nodes. It skips branches that **cannot possibly influence the final decision**.

> Pruning never changes the result. It only avoids work.

---

## Intuition

- Minimax is a **DFS** that expands children left to right.
- At any moment, the search only needs to consider the nodes along a **single path** from the root.
- Along that path, it tracks two bounds:

| Bound | Meaning | Lives on | Starts at |
|---|---|---|---|
| $\alpha$ | best value found so far **for MAX** along the path (MAX's guaranteed lower bound) | MAX nodes | $-\infty$ |
| $\beta$ | best value found so far **for MIN** along the path (MIN's guaranteed upper bound) | MIN nodes | $+\infty$ |

### Pruning conditions

- **At a MIN node:** prune the remaining children once the node's value is $\le \alpha$. MAX already has an option at least this good elsewhere, so it will never let play reach this node.
- **At a MAX node:** prune the remaining children once the node's value is $\ge \beta$. MIN already has an option at least this good for MIN elsewhere.

Both conditions amount to: **prune when $\alpha \ge \beta$.**

**Example (slide 12–13):** The root MAX gets $\alpha = 5$ from its left MIN child, whose leaves are $5, 10$. The right MIN child's first leaf is $1$, so that MIN node's value is $\le 1 < \alpha = 5$. MAX will never choose this branch, so the MIN node's remaining leaf is pruned.

---

## Pseudocode

```
function ALPHA-BETA-SEARCH(state) returns an action
  v ← MAX-VALUE(state, −∞, +∞)
  return the action in ACTIONS(state) with value v

function MAX-VALUE(state, α, β) returns a utility value
  if TERMINAL-TEST(state) then return UTILITY(state)
  v ← −∞
  for each a in ACTIONS(state) do
    v ← MAX(v, MIN-VALUE(RESULT(s,a), α, β))
    if v ≥ β then return v        // prune
    α ← MAX(α, v)
  return v

function MIN-VALUE(state, α, β) returns a utility value
  if TERMINAL-TEST(state) then return UTILITY(state)
  v ← +∞
  for each a in ACTIONS(state) do
    v ← MIN(v, MAX-VALUE(RESULT(s,a), α, β))
    if v ≤ α then return v        // prune
    β ← MIN(β, v)
  return v
```

**Implementation notes:**
- $(\alpha, \beta)$ are **passed down** from parent to child. A child starts with its parent's current bounds.
- A MAX node updates only $\alpha$. A MIN node updates only $\beta$.
- Values are **returned up**. When a child returns, the parent updates its $v$ and then its own bound.

---

## Trace: Textbook Example (slides 16–18)

Tree: $A$ (MAX) → $B, C, D$ (MIN). Leaves: $B: 3, 12, 8$; $C: 2, 4, 6$; $D: 14, 5, 2$. Notation: $(\alpha, \beta)$.

| Step | Event | Bounds |
|---|---|---|
| a | Visit $A$, then $B$ | $A(-\infty,+\infty)$, $B(-\infty,+\infty)$ |
| b | $B$ sees 3 | $B(-\infty, 3)$ |
| c–d | $B$ sees 12, 8 (no change) | $B(-\infty, 3)$, so $B = 3$ |
| e | Return to $A$ | $A(3, +\infty)$ |
| f | Visit $C$ (inherits bounds) | $C(3, +\infty)$ |
| g–h | $C$ sees 2. Since $2 \le \alpha = 3$, **prune** 4 and 6 | $C \le 2$ |
| i | Visit $D$ | $D(3, +\infty)$ |
| j | $D$ sees 14 | $D(3, 14)$ |
| k | $D$ sees 5 | $D(3, 5)$ |
| l | $D$ sees 2. Since $2 \le 3$, prune, but this is the last leaf so nothing is saved | $D = 2$ |

**Result:** $A = \max(3, 2, 2) = 3$.

---

## In-Class Exercises

### Exercise #1 (slides 19–22)
MAX → two MIN nodes. Leaves: $50, 36 \mid 25, 3$.
- Left MIN $= \min(50, 36) = 36$, so its bounds are $(-\infty, 36)$ and the root becomes $(36, +\infty)$.
- Right MIN sees 25, giving $(36, 25)$. Since $25 < 36$, **prune leaf 3**.
- **Root value: 36.**

### Exercise #2 (slides 23–27)
Same tree as the textbook trace. Leaves: $3,12,8 \mid 2,4,6 \mid 14,5,2$.
- MIN 1 gives $(-\infty, 3)$, so the root becomes $(3, +\infty)$.
- MIN 2 sees 2, giving $(3, 2)$. Since $2 \le 3$, **prune 4 and 6**.
- MIN 3 sees $14, 5, 2$ and ends at $(3, 2)$.
- **Root value: 3.**

### Exercise #3 (slides 28–30)
MAX → actions $a$, $d$. Left MIN: $b{=}10$, $c{=}8$. Right MIN: $e{=}4$, $f{=}50$.

1. **Minimax payoff:** left $= \min(10, 8) = 8$, right $= \min(4, 50) = 4$, so MAX $= 8$ (choose $a$).
2. **Alpha-beta payoff:** also $8$. Pruning never changes the answer. After the left subtree, $\alpha = 8$. At the right MIN, $e = 4 \le 8$, so $f$ is pruned.
3. **Which value of $e$ makes pruning impossible?** Any $e > 8$. The prune condition is $v \le \alpha$, so $f$ must be examined whenever $e > \alpha = 8$.
   - **After swapping** ($e{=}50$, $f{=}4$): $50 > 8$, so no pruning happens. $f = 4$ is examined, right MIN $= 4$, and the payoff is still **8**.

**Takeaway:** move ordering decides how much gets pruned. Putting the "good for MIN" child first on the right enabled the prune.

### Exercise #4 (slides 31–33)
Four-ply tree. $A$ (MAX) → $B, C, D$ (MIN) → $E\ldots K$ (MAX) → leaves.

| MAX node | Leaves |
|---|---|
| $E$ | $L{=}1, M{=}2$ |
| $F$ | $N{=}5, O{=}5$ |
| $G$ | $P{=}8, Q{=}6$ |
| $H$ | $R{=}0, S{=}1$ |
| $I$ | $T{=}4, U{=}2$ |
| $J$ | $V{=}9, W{=}10$ |
| $K$ | $X{=}3, Y{=}7$ |

Trace:
- $E = \max(1,2) = 2$, so $B(-\infty, 2)$.
- $F$ sees $N = 5$, giving $F(5, \ldots)$. Since $5 \ge \beta = 2$, **prune $O$**.
- $G$ sees $P = 8 \ge 2$, so **prune $Q$**. Then $B = 2$ and $A(2, +\infty)$.
- $H = \max(0, 1) = 1$, so $C(2, \le 1)$. Since $\beta \le \alpha$ ($1 < 2$), **prune all of $I$** ($T, U$).
- $J = \max(9, 10) = 10$, giving $D(2, \le 10)$. $K = \max(3, 7) = 7$, giving $D(2, 7)$, so $D = 7$.
- **$A = \max(2, 1, 7) = 7$.** Optimal path: $A \to D \to K \to Y$.

Pruned: $O$, $Q$, and the whole subtree $I$ ($T$, $U$).

---

## Effectiveness

- **It depends on the order of successors.** More pruning happens when good moves come first.
- **Best case (perfect ordering):** time drops from $O(b^m)$ to $O(b^{m/2})$.
- So alpha-beta can **look ahead about twice as deep** as minimax in the same time. Equivalently, the effective branching factor drops from $b$ to $\sqrt{b}$.
- Pruning near the leaves saves little (step *l* above). Pruning near the root removes whole subtrees.

---

## Common Gotchas

- $\alpha$ and $\beta$ are **path-local**. They pass *down* the tree, not sideways to siblings, except through the shared parent.
- A MIN node compares against $\alpha$ (the MAX ancestor's bound). A MAX node compares against $\beta$.
- The returned value of a pruned node is a **bound** (e.g. "$\le 2$"), not its exact minimax value. It is still enough for the parent's decision.
- Alpha-beta does **not** apply directly to [[wiki/concepts/adversarial-search#Expectiminimax|chance nodes]]. An average can't be bounded without knowing the range of the leaf values.
