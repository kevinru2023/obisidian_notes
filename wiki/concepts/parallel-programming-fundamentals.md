---
title: "Parallel Programming Fundamentals"
type: concept
sources:
  - "[[raw-sources/courses/CS475/01_Introduction.pdf]]"
related:
  - "[[wiki/courses/CS475]]"
  - "[[wiki/concepts/cache-optimization]]"
updated: 2026-04-16
tags: [parallel-programming, architecture, hpc, cs475]
---

# Parallel Programming Fundamentals

## Why Parallelism?

CPU clock frequency plateaued around 2004 (~3 GHz). Increasing transistor count no longer translates to faster single-core performance — power dissipation scales as $\sim f^3$.

**Solution:** more cores, not faster cores.

**Frequency reduction example** (3.2 GHz → 2.3 GHz, i.e. 70%):

| | 1 core | 2 cores |
|---|---|---|
| Power | $70\%^3 \approx 35\%$ | $35\% \times 2 = 70\%$ |
| Performance | $70\%$ | $70\% \times 2 = 140\%$ |

Same power budget, 2× performance.

**Compute demand is exploding:**
- Deep learning (2015–2025): training compute roughly $10\times$ every 2 years, reaching $\sim 10^{24}$ FLOPs for frontier models.
- Climate simulation: 50-year prediction in 12 hours requires **288 TFLOPS**; one Intel Xeon Gold 6148 (20 cores, 2.4 GHz, AVX-512) delivers $\sim 0.15$ TFLOPS sustained → need $\approx 2{,}000$ such CPUs.

$$\text{Peak FLOPS} = f_{\text{clock}} \times \text{FLOPS/cycle} \times N_{\text{cores}}$$

## Parallel Programming Models

### Data Parallelism

Same operation applied to different data simultaneously. Each thread/processor handles a partition of the data.

```c
// Serial
for (i = 0; i < N; i++) B[i] = sqrt(A[i]);

// Parallel (3 threads, each takes N/3 elements)
// Thread k: for (i = k*N/3; i < (k+1)*N/3; i++) B[i] = sqrt(A[i]);
```

**Execution time:** $\approx T_{\text{serial}} / P$ (ideal, $P$ = number of processors)

### Task Parallelism

Different tasks execute simultaneously on different processors/threads.

**Serial:** $T = \sum_i T_i$

**Parallel (all tasks run concurrently):** $T \approx \max_i(T_i)$

**Pipeline** (a form of task parallelism): tasks are chained — as processor 1 finishes stage 1 for item $k$, processor 2 starts stage 2 for item $k$ while processor 1 works on item $k+1$. Throughput improves; latency for first item stays at $\sum T_i$.

## Flynn's Taxonomy

Classifies parallel architectures by instruction and data streams:

| | Single Data | Multiple Data |
|---|---|---|
| **Single Instruction** | **SISD** — classic serial CPU | **SIMD** — GPUs, CPU vector units (AVX, SSE) |
| **Multiple Instruction** | **MISD** — rare/theoretical | **MIMD** — multicore CPUs, clusters |

- **SIMD** executes one instruction on many data elements per cycle (e.g., AVX-512 processes 8 doubles at once).
- **MIMD** is the dominant model for general-purpose parallel computing; each processor has its own instruction stream.

## Memory Architectures

### Shared Memory

All processors access a **single global memory space**. Threads communicate by reading/writing shared variables.

- Natural programming model (single address space)
- Requires synchronization (locks, atomics) to prevent race conditions
- Bandwidth becomes a bottleneck at high core counts
- Examples: multicore desktop/server CPUs, GPU streaming multiprocessors within a device

### Distributed Memory

Each node has **private local memory**. Inter-node communication uses an explicit **message-passing library** (MPI).

- Scales to thousands of nodes (clusters, supercomputers)
- Programmer explicitly moves data between nodes
- Network latency and bandwidth are critical performance factors
- Example: COE compute cluster, Summit, Frontier

**Hierarchy in a cluster:**
$$\text{Rack} \supset \text{Node} \supset \text{Socket} \supset \text{Core}$$

Each core has its own L1 cache; cores may share L2/L3; nodes are connected via network interconnect.

## Platforms in CS475

| Platform | Architecture | Programming Model |
|---|---|---|
| Multicore CPU | Shared memory (MIMD) | OpenMP |
| NVIDIA GPU | SIMD + shared memory within SM | CUDA |
| Cluster / Supercomputer | Distributed memory (MIMD) | MPI |

## Supercomputer Example: Summit (Top 1, 2018)

- 256 compute racks × 18 nodes/rack = 4,608 nodes
- Each node: 2 × 22-core IBM POWER9 CPUs + 6 × NVIDIA V100 GPUs
- Total: 9,216 CPUs, 27,648 GPUs
- **Peak: 200 PFLOPS** ($2 \times 10^{17}$ FLOPS)

**Node memory bandwidth:**
- CPU DRAM: 170 GB/s per socket
- GPU HBM2: 900 GB/s per GPU
- NVLink2 (CPU↔GPU): 50 GB/s
- CPU↔CPU: 64 GB/s

## AlphaGo: Parallelism in Practice

Adding GPUs gives large Elo gains up to a point; distributed mode (1,202 CPUs, 176 GPUs) achieved Elo 3,168 vs. a 9-dan player's Elo 2,940 — demonstrating that ML inference/search is parallelizable and benefits massively from distributed hardware.
