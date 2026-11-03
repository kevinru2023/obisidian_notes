---
title: "A Word on Scalability"
type: summary
sources:
  - "[[raw-sources/web-clippings/A Word on Scalability.md]]"
related: []
updated: 2026-04-18
tags: [distributed-systems, scalability, architecture]
---

# A Word on Scalability

**Source:** Werner Vogels (CTO, Amazon) — [allthingsdistributed.com](https://www.allthingsdistributed.com/2006/03/a_word_on_scalability.html), 2006-03-30

## Core Definition

> *A service is scalable if when we increase the resources in a system, it results in increased performance in a manner proportional to resources added.*

Two flavors of "increased performance":
- **Throughput scalability** — serve more units of work (higher request rate, larger datasets)
- **Reliability scalability** — add redundancy without a loss of performance

## Why Scalability is Hard

1. **Must be designed in from the start.** Scalability cannot be retrofitted. Algorithms that perform fine under low load can explode in cost as request rates, dataset size, or node count grow.

2. **Scale-out introduces heterogeneity.** As systems grow, newer hardware generations mix with older ones. Algorithms that assume uniform node capability either break down or underutilize faster nodes.

## Key Takeaway

Good scalability is achievable only if architects:
- Identify *which axes* the system is expected to grow along
- Determine *where* redundancy is required
- Understand how to handle *heterogeneity*
- Know the available tools and their common pitfalls
