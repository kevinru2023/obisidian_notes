---
title: "How CRDTs Make Multiplayer Text Editing Part of Zed's DNA"
type: summary
sources:
  - "[[raw-sources/web-clippings/How CRDTs make multiplayer text editing part of Zed's DNA.md]]"
related:
  - "[[wiki/concepts/crdts]]"
updated: 2026-04-29
tags: [crdts, distributed-systems, collaborative-editing, zed]
---

## Overview

A Zed blog post (Dec 2022) by Nathan Sobo explaining the CRDT-based text representation at Zed's core. The post traces the problem from Engelbart's 1968 collaborative editor through Operational Transformation (OT) to Zed's eventual-consistency approach using CRDTs.

---

## The Core Problem

Collaborative editors over the internet cannot use a mutex on a shared buffer — latency between continents would be prohibitive. Instead, each user edits a local *replica* and syncs asynchronously. Naively replaying remote edits at absolute offsets causes *divergence* when concurrent edits shift text positions.

---

## Why Not OT?

**Operational Transformation** transforms incoming operations to account for concurrent edits (e.g., shifting an insertion's offset). Zed experimented with OT in 2017 but found it hard to define a correct, performant transform function. CRDTs were chosen instead for being more intuitive and powerful.

---

## Zed's CRDT Design

### Immutable Insertions and Anchors

Every piece of text ever inserted is treated as **immutable**. Insertion positions are expressed as *(insertion id, character offset)* pairs called **anchors** — stable logical addresses that survive concurrent edits.

- Unique IDs: a centrally-assigned *replica id* combined with an incrementing sequence number. No central coordination needed after initial ID assignment.
- The initial buffer content is insertion `0.0`. New insertions split existing fragments; they never mutate them.

### Applying Remote Insertions

To apply a remote insertion: scan local fragments for the specified offset within the parent insertion's ID, then insert the new text there. This scan is $O(n)$ naively but Zed indexes fragments in a **copy-on-write B-tree** (described in a future post) to avoid linear scans.

### Deletion via Tombstones

Deleted fragments are **marked with tombstones**, not removed. This allows insertions concurrent with a deletion to still be applied correctly — the anchor still resolves even if the referenced text is "deleted."

To prevent a deletion from accidentally hiding text inserted *concurrently* (which the deleter never saw), each deletion carries a **version vector** (latest observed sequence number per replica). Insertions whose IDs contain sequence numbers *not* in the version vector are excluded from the tombstone.

### Concurrent Insertions at the Same Location

When two insertions target the same location, the order is arbitrary but must be *consistent* across all replicas. Ordering purely by ID can violate causality. Solution: augment each insertion with a **Lamport timestamp**.

- Lamport clock: incremented on every local operation; updated to $\max(\text{local}, \text{incoming})$ on receipt.
- Sort concurrent same-location insertions **descending by Lamport timestamp**, breaking ties by replica ID.
- Guarantees: if op A was visible when op B was generated, $\text{ts}(A) < \text{ts}(B)$. Concurrent ops have no causal order but still get a consistent total order.

### Undo / Redo

Single global undo stacks break in collaborative editors — users expect to undo only their own changes. Zed's approach:

- Maintain an **undo map**: operation ID → undo count.
  - Count = 0 → not undone
  - Count odd → undone
  - Count even → redone
- Fragment visibility check: insertion undone (odd count) **and** no active deletion tombstone (deletion not itself undone) → hidden.
- Two users undoing the same operation concurrently both set the count to the same value — intent preserved.

---

## Key Takeaways

| Mechanism | Problem Solved |
|---|---|
| Immutable insertions + anchors | Stable logical addresses despite concurrent edits |
| Tombstones | Deletion without data loss; supports late-arriving concurrent insertions |
| Version vectors on deletions | Excludes concurrent insertions from tombstones |
| Lamport timestamps | Causal ordering of same-location concurrent insertions |
| Undo map | Per-user non-linear undo in a collaborative context |

The CRDT representation enables **eventual consistency**: all replicas converge to the same document state regardless of the order operations arrive, without any central coordinator.
