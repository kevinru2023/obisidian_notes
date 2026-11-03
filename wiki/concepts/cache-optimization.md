---
title: "Cache-Based Optimizations"
type: concept
sources:
  - "[[raw-sources/courses/CS475/02_Cache.pdf]]"
  - "[[raw-sources/courses/CS475/03_Cache_cont_and_OpenMP.pdf]]"
related:
  - "[[wiki/courses/CS475]]"
updated: 2026-04-20
tags: [cache, memory-hierarchy, locality, parallel-programming, performance, matrix-multiplication]
---

# Cache-Based Optimizations

## Why Memory Access Matters

The number of operations and the operations themselves may be identical between two programs, but **the order of data access** determines performance. Data movement from memory to CPU is frequently the bottleneck — not arithmetic.

---

## Principle of Locality

Programs tend to use data and instructions with addresses near or equal to those recently used.

- **Temporal locality**: Recently referenced items are likely to be referenced again soon.
- **Spatial locality**: Items with nearby addresses tend to be referenced close together in time.

```c
// Example: sum array
sum = 0;
for (i = 0; i < n; i++)
    sum += a[i];
return sum;
```
- `a[i]` accesses successive elements → **spatial locality**
- `sum` accessed every iteration → **temporal locality**
- Loop instructions cycle repeatedly → **temporal locality** for instructions

---

## Memory Hierarchy

Storage levels trade speed for capacity and cost:

| Level | Device | Access latency (Intel Nehalem i7) |
|---|---|---|
| L0 | Registers | ~1 cycle (0.376 ns) |
| L1 | L1 cache (SRAM) | ~4 cycles |
| L2 | L2 cache (SRAM) | ~10 cycles |
| L3 | L3 cache (unshared line) | ~40 cycles |
| L3 | L3 cache (shared in another core) | ~65 cycles |
| L3 | L3 cache (modified in another core) | ~75 cycles |
| L4 | Main memory (DRAM) | ~150 cycles |
| L5 | Local disk | ~10,000 cycles |

**Big Idea**: The hierarchy creates storage that costs like cheap memory but serves data at the speed of fast memory — because locality means the fast levels absorb most accesses.

---

## Cache Fundamentals

- **Cache**: Smaller, faster staging area for a subset of data from a larger, slower device.
- At each level k, the device serves as a cache for level k+1.
- **Cache hit**: Data found in cache.
- **Cache miss**: Data not found; must be fetched from a lower level.

### Types of Cache Misses
- **Compulsory miss**: First reference to a line (cold miss).
- **Capacity miss**: Cache is too small to hold all active working set data.
- **Conflict miss**: Multiple items map to the same cache location.

---

## Cache Performance Metrics

| Metric | Definition | Typical values |
|---|---|---|
| **Miss rate** | Misses / total accesses (= 1 − hit rate) | L1: 3–10%; L2: <1% |
| **Hit time** | Cycles to deliver a hit | L1: 1–2 cycles; L2: 5–20 cycles |
| **Miss penalty** | Extra cycles on a miss | 50–200 cycles (DRAM, trending up) |

### Why Small Miss Rate Differences Matter

With hit time = 1 cycle, miss penalty = 100 cycles:
- 97% hit rate → average access = 1 + 0.03 × 100 = **4 cycles**
- 99% hit rate → average access = 1 + 0.01 × 100 = **2 cycles**

Going from 97% → 99% hits **doubles throughput**.

---

## Writing Cache-Friendly Code

1. **Focus on inner loops** of core functions — that's where most time is spent.
2. **Repeated references to the same variable** = temporal locality (hold in register if possible).
3. **Stride-1 access patterns** = spatial locality (access arrays row-by-row in C, not column-by-column).

### C Arrays in Memory

C arrays are **row-major**: each row is contiguous. With cache line size C:
- **Row traversal** (stride-1): compulsory miss rate = 8 bytes / C (e.g., 0.25 misses/access for 32-byte lines)
- **Column traversal**: miss on every access → miss rate = 1.0 (100%)

---

## Register Reuse

### Basic register reuse (dgemm_register)

Move the accumulation variable out of memory into a register:

```c
// Without register reuse: 3 loads + 1 store per inner iteration
for (k = 0; k < n; k++)
    C[i*n+j] += A[i*n+k] * B[k*n+j];

// With register reuse: 2 loads per iteration, 1 store outside loop
register double t = C[i*n+j];
for (k = 0; k < n; k++)
    t += A[i*n+k] * B[k*n+j];
C[i*n+j] = t;
```

### 2×2 blocked register reuse

Process a 2×2 submatrix using registers — each `a[]` and `b[]` element used twice within the block, each `c[]` element hoisted out of the k-loop:

```c
for (i = 0; i < n; i += 2)
  for (j = 0; j < n; j += 2) {
    register double c00 = c[i*n+j], c01 = c[i*n+j+1];
    register double c10 = c[(i+1)*n+j], c11 = c[(i+1)*n+j+1];
    for (k = 0; k < n; k += 2) {
        // load 2x2 blocks of a and b into registers
        // do 8 multiply-adds using only registers
    }
    c[i*n+j] = c00;  // store back once
    // ...
  }
```

---

## Loop Ordering and Cache Miss Rates

Assumption: cache line = 32 bytes = 4 doubles; cache size << n.

| Loop order | A misses/iter | B misses/iter | C misses/iter | Total misses/iter |
|---|---|---|---|---|
| ijk | 0.25 (row-wise) | 1.0 (col-wise) | 0.0 (fixed) | **1.25** |
| jik | 0.25 | 1.0 | 0.0 | **1.25** |
| kij | 0.0 (fixed) | 0.25 (row-wise) | 0.25 (row-wise) | **0.5** |
| ikj | 0.0 | 0.25 | 0.25 | **0.5** |
| jki | 1.0 (col-wise) | 0.0 (fixed) | 1.0 (col-wise) | **2.0** |
| kji | 1.0 | 0.0 | 1.0 | **2.0** |

**Best orderings**: kij and ikj (0.5 misses/iter). **Worst**: jki and kji (2.0 misses/iter).

The key insight: B is stored column-major access in ijk (bad), but kij/ikj access B row-wise (good).

---

## Blocked (Tiled) Matrix Multiplication

### Motivation

Non-blocked mm: total cache misses ≈ **(5/4) × n³**  
Each column of B evicts the previous one before it can be reused.

### Idea

Partition matrices into B×B blocks. Multiply block by block so three blocks fit in cache simultaneously.

```c
for (i = 0; i < n; i += B)
  for (j = 0; j < n; j += B)
    for (k = 0; k < n; k += B)
      // B×B mini matrix multiply
      for (i1 = i; i1 < i+B; i1++)
        for (j1 = j; j1 < j+B; j1++)
          for (k1 = k; k1 < k+B; k1++)
            c[i1*n+j1] += a[i1*n+k1] * b[k1*n+j1];
```

### Miss Analysis

Condition: **3B² < C** (three blocks fit in cache).

- Per block pair: B²/4 misses
- Per block iteration: 2n/B × B²/4 = nB/2 misses
- Total: nB/2 × (n/B)² = **n³ / (2B)**

### Improvement

Non-blocked: (5/4)n³ misses  
Blocked: n³/(2B) misses  
**Speedup factor: (5/4) × 2B = 5B/2**

Choose the largest B such that **3B² < C** (cache size constraint).

### Why This Works

Matrix multiplication has inherent temporal locality: 3n² input data but 2n³ operations → each element is used O(n) times. Blocking exposes this reuse — but only if the code is written to exploit it.

---

## Performance Calculations (Quiz Examples)

Assumptions: 2 GHz CPU, 4 FLOP/cycle, memory additional delay = 100 cycles, cache line = 32 bytes (4 doubles).

### No-cache scenario ($n = 1000$)

**dgemm** (plain, 3 loads + 1 store per inner iteration):

$$T_m = 4n^3 \times \frac{1}{f} \times \Delta_{mem} = 4 \times 10^9 \times \frac{1}{2\,\text{GHz}} \times 100 = 200\,\text{s}$$

$$T_c = \frac{2n^3}{f \times \text{FLOP/cycle}} = \frac{2 \times 10^9}{2\,\text{GHz} \times 4} = 0.25\,\text{s}$$

→ Memory-bound by a factor of 800×.

**dgemm_register** (hoisted accumulator, 2 loads + 1 store per inner iter):

$$T_m = (2n^3 + 2n^2) \times \frac{1}{f} \times \Delta_{mem} \approx 100.1\,\text{s}$$

Register reuse cuts memory time roughly in half.

### With cache ($\Delta_{cache} = 4$ cycles, cache line = 4 doubles, full row doesn't fit)

**dgemm_ijk**: 0.75 cache hits + 1.25 misses per inner iteration:

$$T_m = n^3 (0.75 \times \Delta_{cache} + 1.25 \times \Delta_{mem}) \times \frac{1}{f} \approx 64.05\,\text{s}$$

Cache helps significantly but B's column-wise access still incurs 1.0 miss/iter.

---

## Roofline Model

See [[wiki/concepts/parallel-performance#Roofline Model]] for the full treatment (operational intensity, memory vs. compute ceilings, ridge point).
