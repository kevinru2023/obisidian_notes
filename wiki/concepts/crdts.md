---
title: "CRDTs (Conflict-Free Replicated Data Types)"
type: concept
sources:
  - "[[raw-sources/web-clippings/How CRDTs make multiplayer text editing part of Zed's DNA.md]]"
related:
  - "[[wiki/summaries/zed-crdts]]"
updated: 2026-04-29
tags: [crdts, distributed-systems, collaborative-editing, eventual-consistency]
---

# CRDTs (Conflict-Free Replicated Data Types)

## Definition

A **Conflict-Free Replicated Data Type (CRDT)** is a data structure designed so that concurrent operations on different replicas are **inherently commutative** — they can be applied in any order and all replicas converge to the same state without coordination or transformation.

Compare to **Operational Transformation (OT)**, which instead *transforms* incoming operations to compensate for concurrent changes. CRDTs avoid the complexity of defining a correct transform function.

---

## Core Idea: Commutative Operations

The fundamental insight: if we express operations in terms of **logical locations** rather than absolute offsets, then the operation's meaning is stable even as concurrent edits shift text around. CRDT designs ensure $op_A \circ op_B = op_B \circ op_A$ for any concurrent $op_A, op_B$.

---

## CRDT Text Editing (Zed's Model)

### Data Model

- **Insertions are immutable.** Every character (or string) ever inserted is assigned a unique ID and persists forever in the logical history.
- **Unique IDs:** $(replica\_id, seq)$ pairs. The replica ID is centrally assigned once; subsequent IDs are generated locally without coordination.
- **Anchors:** $(insertion\_id, offset)$ pairs — stable logical positions within a specific insertion fragment.

### Fragment Structure

The document is a sequence of **fragments**, each belonging to a specific insertion ID. Applying an insertion splits the target fragment at the specified offset; it never mutates existing text. The full edit history is preserved in the fragment list.

### Convergence Guarantee

Because every replica applies operations to the same logical structure:
- **Insert** at anchor $(id, offset)$: scan for that fragment, insert new text. Result is identical regardless of what concurrent inserts have occurred.
- **Delete** via tombstone: mark fragment hidden, never remove it. Future insertions whose anchors point into tombstoned text still resolve correctly.

---

## Key Mechanisms

### Tombstone Deletion

Deletions mark fragments as hidden rather than removing them. This ensures:
1. Anchors into "deleted" text remain resolvable.
2. Concurrent insertions arriving after a deletion can still be placed correctly.

**Problem:** A deletion might intend to cover text concurrently being inserted (which the deleter never saw). Tombstoning everything in a range including concurrent insertions misrepresents intent.

**Solution:** Each deletion carries a **version vector** — the latest observed sequence number per replica at deletion time. Insertions with sequence numbers *beyond* the version vector are excluded from the tombstone (they were concurrent, not causally prior).

### Lamport Timestamps (Causal Ordering)

When two insertions target the same location, order must be consistent across replicas. Pure ID ordering can violate causality.

**Lamport clock rules:**
$$\text{ts}_{gen} = \text{clock} + 1$$
$$\text{ts}_{recv} = \max(\text{clock},\ \text{incoming.ts})$$

This guarantees: if op A was *visible* when op B was generated, then $\text{ts}(A) < \text{ts}(B)$.

**Ordering rule:** sort same-location concurrent insertions *descending* by Lamport timestamp; break ties by replica ID. Causal predecessors get lower timestamps and are placed before their successors.

### Undo Map

Non-linear undo (each user undoes only their own ops) requires abandoning a global undo stack.

**Undo map:** $operation\_id \to \text{count}$

| Count | Meaning |
|---|---|
| 0 | Not undone |
| Odd | Undone |
| Even | Redone |

Fragment visibility: visible iff (insertion not undone) AND (no active deletion tombstone). Concurrent undos of the same operation both set the count to the same value — idempotent, intent preserved.

---

## Complexity

| Operation | Naïve | Zed (B-tree indexed) |
|---|---|---|
| Apply remote insert | $O(n)$ scan | $O(\log n)$ |
| Apply tombstone | $O(n)$ scan | $O(\log n)$ |

Zed uses a **copy-on-write B-tree** to index fragments, eliminating linear scans.

---

## CRDT vs. OT

| | CRDTs | Operational Transformation |
|---|---|---|
| Approach | Commutative ops by design | Transform ops to compensate for concurrency |
| Correctness | Structural guarantee | Requires correct transform function (hard) |
| Complexity | Data structure design | Algorithm design |
| Examples | Zed, Automerge, Yjs | Google Docs (early), ShareJS |

---

## Related Concepts

- **Eventual consistency** — all replicas converge to the same state given the same set of operations, regardless of delivery order.
- **Vector clocks / version vectors** — track per-replica sequence numbers to establish causal relationships.
- **Lamport timestamps** — scalar logical clocks that capture causal order without requiring full vector clocks.
- **Replica** — an independent copy of a data structure that can be edited concurrently.
