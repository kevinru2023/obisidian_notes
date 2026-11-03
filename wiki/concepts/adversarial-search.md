---
title: "Adversarial Search (Minimax & Expectiminimax)"
type: concept
sources:
  - "[[raw-sources/Lecture8_Adversarial_Search.pdf]]"
related:
  - "[[wiki/concepts/alpha-beta-pruning]]"
  - "[[wiki/courses/CS331]]"
updated: 2026-10-31
tags: [AI, adversarial-search, game-trees, minimax, expectimax, expectiminimax, CS331]
---

# Adversarial Search

Adversarial search finds a good move for an agent playing **against an opponent** by searching the game tree. The opponent's choices are modeled as optimal moves against us, not as random events.

---

## The Game Setting

Classic adversarial search (chess, Go, tic-tac-toe) assumes games that are:

- **Deterministic**: no dice or randomness
- **Discrete**: discrete states and decisions
- **Finite**: finitely many states and decisions
- **Perfect information**: fully observable
- **Two agents whose actions alternate**
- **Zero-sum**: terminal utilities are equal and opposite
- **Time-limited**: a decision must be made within a time budget

### Players

| Player | Role | Goal |
|---|---|---|
| **MAX** (Player 1) | the agent | maximize its utility |
| **MIN** (Player 2) | the opponent | **minimize MAX's utility** |

MAX's strategy must account for MIN's responses, because the players alternate moves.

---

## Minimax

> **Minimax value of a node** = MAX's utility at that node, assuming **both players play optimally** from there to the end of the game.

$$
\text{Minimax}(n) =
\begin{cases}
\text{Utility}(n) & \text{if } n \text{ is terminal} \\
\max_{s \in \text{children}(n)} \text{Minimax}(s) & \text{if } n \text{ is a MAX node} \\
\min_{s \in \text{children}(n)} \text{Minimax}(s) & \text{if } n \text{ is a MIN node}
\end{cases}
$$

**Key property:** the minimax value **maximizes the worst-case outcome for MAX**.

### Worked example (slide 7)

```
              MAX = 8
       /         |         \
   MIN=8       MIN=2       MIN=5
  12 12 8     2  4  6    14  5  17
```

Each MIN node takes the smallest leaf: $\min(12,12,8)=8$, $\min(2,4,6)=2$, $\min(14,5,17)=5$. MAX then takes the largest: $\max(8,2,5)=8$.

### Complexity

Minimax is a **depth-first search** that expands children left to right. For branching factor $b$ and maximum depth $m$:

- Time: $O(b^m)$
- Space: $O(bm)$, because DFS keeps only one path plus siblings

$O(b^m)$ is infeasible for real games, which motivates [[wiki/concepts/alpha-beta-pruning|alpha-beta pruning]]: it skips branches that cannot change the final decision. In the best case this cuts the time to $O(b^{m/2})$.

---

## Games with Uncertainty: Chance Nodes

Some outcomes are controlled **by chance, not by an adversary** (dice rolls, card draws). To model them, add **chance nodes** to the game tree.

### Expectimax

**Idea:** compute the **average score under optimal play**.

- MAX nodes work as in standard minimax.
- Chance nodes are like MIN nodes, except their outcome is uncertain.
- A chance node's value is the **expected utility**: the probability-weighted average of its children.

$$
\text{value}(c) = \sum_{s \in \text{children}(c)} P(s)\,\text{value}(s)
$$

> Unless explicitly specified, assume **equal probabilities** for a chance node's children.

**Example (slide 35):** MAX chooses between two chance nodes with leaves $\{10, 10\}$ and $\{9, 100\}$.
- Expectimax: left $= 10$, right $= \tfrac{9+100}{2} = 54.5$, so MAX picks **right**.
- Minimax would treat the chance nodes as MIN nodes: left $= 10$, right $= 9$, so it would pick left. Minimax is too pessimistic when the "opponent" is really just chance.

### Expectiminimax

Expectiminimax combines MAX, MIN **and** chance nodes. It "gives perfect play".

```
if state is a MAX node:    return highest EXPECTIMINIMAX-VALUE of successors
if state is a MIN node:    return lowest  EXPECTIMINIMAX-VALUE of successors
if state is a chance node: return average EXPECTIMINIMAX-VALUE of successors
```

**Example (slide 37):** MAX → DICE (chance) → MIN → leaves. The dice outcomes have probabilities $0.9$ and $0.1$.

| Action | MIN values | Chance value |
|---|---|---|
| $A_1$ | $2$ (p=0.9), $3$ (p=0.1) | $0.9(2) + 0.1(3) = 2.1$ |
| $A_2$ | $1$ (p=0.9), $4$ (p=0.1) | $0.9(1) + 0.1(4) = 1.3$ |

MAX picks $A_1$.

### Evaluation is scale dependent

Rescale the leaves of the same tree to $20, 30, 1, 400$. This keeps their **order** unchanged.

| Action | Chance value |
|---|---|
| $A_1$ | $0.9(20) + 0.1(30) = 21$ |
| $A_2$ | $0.9(1) + 0.1(400) = 40.9$ |

Now MAX picks $A_2$. **The decision flipped.**

- Minimax depends only on the *ordering* of leaf values. Any order-preserving transformation gives the same move.
- With chance nodes, the *magnitudes* matter. The evaluation function must be proportional to the true expected payoff. *(Standard result, not stated on the slide: only positive affine transformations $aU + b$ with $a > 0$ are guaranteed to preserve expectimax decisions.)*

---

## Adversarial Search in Modern AI

**1. Complex strategy games (Dota 2, StarCraft): DeepMind's AlphaStar.** AlphaStar combines adversarial search ideas with deep learning:
- **Self-play:** self-play reinforcement learning replaces explicit tree search. Each agent learns a policy that maximizes its expected win rate against an adversary. Agents improve by continually playing each other, which produces a population of diverse strategies.
- **Best response:** each agent learns to anticipate the opponent's counter-strategy (the minimax principle).
- **Deep learning for evaluation:** policy-gradient methods replace propagating leaf utilities up the tree.

**2. Adversarial machine learning.** The attacker looks for perturbations $\delta$ that **maximize** model error, and the defender adjusts the model to **minimize** it. This is effectively a minimax game:

$$
\min_{\theta} \max_{\delta} \; \mathcal{L}(f_\theta(x + \delta), y)
$$

---

## Limitations

Adversarial search computes strategies against an **optimal opponent**, but it only works well when:

1. **Players take turns.** It does not handle **simultaneous moves**.
2. **The game is strictly competitive.** In the 2-player setting, MIN's only objective is to minimize MAX's payoff. MIN has no payoffs of its own, so the framework does not cover general-sum games.

---

## Key Questions

- What does the minimax value of a node represent? *(MAX's utility under optimal play by both players, which is the best worst case for MAX)*
- Why does minimax fail when the opponent is chance? *(It assumes the worst outcome, but chance does not pick the worst outcome.)*
- Why does rescaling leaves change expectimax decisions but not minimax decisions?
- Name two assumptions that adversarial search relies on. *(Alternating turns, and a zero-sum game with no separate MIN payoff)*
