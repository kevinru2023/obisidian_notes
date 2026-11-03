---
title: "CS475 Review"
type: reference
sources:
  - "[[wiki/courses/CS475]]"
  - "[[wiki/concepts/parallel-programming-fundamentals]]"
  - "[[wiki/concepts/cache-optimization]]"
  - "[[wiki/concepts/openmp]]"
  - "[[wiki/concepts/parallel-performance]]"
  - "[[wiki/concepts/gpu-cuda]]"
related:
  - "[[wiki/courses/CS475]]"
updated: 2026-05-05
tags: [CS475, parallel-programming, review]
---

# CS475 Review

Covers: Parallel fundamentals, Cache optimization, OpenMP, Parallel performance analysis, GPU/CUDA.  
Midterm: May 5, 2026 | Final: June 9, 2026

---

## Quick-Reference Table

| Concept | Core Idea | Key Formula / Rule |
|---|---|---|
| Why parallelism | Clock speed plateaued ~2004; more cores, not faster | Power $\propto f^3$; halve $f$ → 87.5% power savings |
| Data vs. task parallelism | Data: same op on different data; Task: different ops concurrently | Data: $T \approx T_{serial}/P$; Task: $T \approx \max_i(T_i)$ |
| Flynn's taxonomy | SIMD = one instruction, many data; MIMD = multiple instruction, multiple data | GPUs are SIMD; multicore CPUs are MIMD |
| Memory hierarchy | Faster = smaller = costlier; exploit temporal + spatial locality | L1: ~4 cycles; DRAM: ~150 cycles; disk: ~10k cycles |
| Loop ordering | Row-major C arrays → stride-1 access is fast | kij/ikj: 0.5 misses/iter (best); jki/kji: 2.0 (worst) |
| Cache blocking | Reuse B×B tiles so 3 blocks fit in cache | Misses: $(5/4)n^3$ → $n^3/(2B)$; speedup $= 5B/2$ |
| OpenMP fork-join | Master forks threads at `#pragma omp parallel`, joins at `}` | Implicit barrier at end of every parallel region |
| False sharing | Threads write different vars on the same cache line → invalidation | Fix: pad arrays, use private scalars, use `reduction` |
| MESI coherence | M/E/S/I states per cache line; write = invalidate all other copies | Write to shared line → transitions S→I for all others |
| `reduction` clause | Private copy per thread; merge at end; zero contention | `reduction(+:sum)` — initial value for `+` is 0 |
| Amdahl's Law | Fixed problem size; serial fraction $f$ caps speedup | $\psi \leq 1/(f + (1-f)/p)$; $\lim_{p\to\infty} \psi = 1/f$ |
| Gustafson-Barsis | Fixed wall-clock time; scale problem with $p$ | $\psi \leq p + (1-p)s$; grows linearly with $p$ |
| Roofline model | Memory-bound vs. compute-bound; ridge point = bandwidth/compute ratio | Operational intensity = FLOP/byte; left of ridge = mem-bound |
| CUDA thread hierarchy | Thread→Core, Block→SM, Grid→GPU | Max 1024 threads/block; $2^{31}-1$ blocks in x |
| Warp divergence | Within-warp if-else serializes paths → penalty | Between-block divergence is fine; within-warp is slow |
| Memory coalescing | Sequential access by 32 consecutive threads = 100% bus util | 32 threads × stride-1 → 4 transactions; stride-3 → 12 |
| Shared memory bank conflicts | 32 banks; bank $= i \bmod 32$; same bank = serialized | Sequential reduction (s>>1) avoids conflicts |
| Parallel reduction | No global sync in CUDA; decompose into 2 kernel launches | Best: sequential addressing + warpReduce unrolling for last warp |

---

## Parallel Programming Fundamentals

**Why parallelism:**  
CPU frequency plateaued ~2004 at ~3 GHz. Power scales as $P \propto f^3$, so increasing $f$ becomes thermally infeasible. Reducing $f$ by 30% cuts power ~65% — run 2 cores at 140% original performance for the same power.

$$\text{Peak FLOPS} = f_{\text{clock}} \times \text{FLOPS/cycle} \times N_{\text{cores}}$$

**Data parallelism:** Same operation on different data. Ideal time: $T \approx T_{serial}/P$.

**Task parallelism:** Different tasks execute simultaneously. Time: $T \approx \max_i(T_i)$. Pipelines are a form of task parallelism.

**Flynn's Taxonomy:**

| | Single Data | Multiple Data |
|---|---|---|
| **Single Instruction** | SISD (serial CPU) | SIMD (GPUs, AVX) |
| **Multiple Instruction** | MISD (rare) | MIMD (multicore, clusters) |

**Memory architectures:**

| | Shared Memory | Distributed Memory |
|---|---|---|
| Communication | Read/write shared vars | Explicit MPI messages |
| Sync needed? | Yes (locks, atomics) | No (private address space) |
| Scales to | Dozens of cores | Thousands of nodes |
| Model | OpenMP | MPI |

CS475 platforms: Multicore CPU → OpenMP; GPU → CUDA; Cluster → MPI.

**Common exam questions:**
- Given cores $p$ and problem $n$, compute peak speedup under ideal conditions.
- Identify whether a workload is data-parallel or task-parallel.
- Classify an architecture in Flynn's taxonomy.
- Why can't you just increase clock speed instead of adding cores?

**Gotchas:**
- MIMD ≠ SIMD: GPU uses SIMT (one instruction per warp of 32 threads), which maps to SIMD hardware.
- Data parallelism time is $T/P$ only if there's no synchronization overhead.

**See also:** [[wiki/concepts/parallel-programming-fundamentals]]

---

## Cache-Based Optimizations

**Memory hierarchy latencies (Intel Nehalem i7):**

| Level | Latency |
|---|---|
| Registers | ~1 cycle |
| L1 cache | ~4 cycles |
| L2 cache | ~10 cycles |
| L3 cache | ~40–75 cycles |
| DRAM | ~150 cycles |

**Principle of locality:**
- *Temporal*: recently used data will be used again → keep in cache.
- *Spatial*: nearby addresses will be accessed → use stride-1 patterns.

**Loop ordering for matrix multiplication (row-major, cache line = 4 doubles):**

| Order | Misses/iter | Notes |
|---|---|---|
| kij / ikj | **0.5** | Best — B and C row-wise |
| ijk / jik | 1.25 | B column-wise (miss every iter) |
| jki / kji | 2.0 | Worst — A and C column-wise |

Rule: the inner two loops should traverse a row of one matrix and a row of another. B being accessed column-wise (ijk) is the most common mistake.

**Register reuse:** Hoist the accumulation variable out of memory:

```c
register double t = C[i*n+j];
for (k = 0; k < n; k++)
    t += A[i*n+k] * B[k*n+j];
C[i*n+j] = t;
```
Cuts loads from 3 to 2 per inner iteration, halving memory time.

**Cache blocking (tiling):**
Partition into $B \times B$ tiles. Condition: $3B^2 < C$ (cache size).

$$\text{Misses (non-blocked)} \approx \frac{5}{4}n^3 \qquad \text{Misses (blocked)} \approx \frac{n^3}{2B}$$

$$\text{Speedup} = \frac{5B}{2}$$

**Performance calculation pattern** (2 GHz, 4 FLOP/cycle, 100-cycle mem penalty):

$$T_m = (\text{mem accesses}) \times \frac{1}{f} \times \Delta_{mem}$$
$$T_c = \frac{2n^3}{f \times \text{FLOP/cycle}}$$

If $T_m \gg T_c$ → memory-bound; register reuse and blocking are the fixes.

**Common exam questions:**
- Given loop order, compute cache misses per inner iteration.
- Compute execution time with and without register reuse.
- What is the optimal tile size $B$ given a cache size $C$?
- How does changing the loop order from ijk to kij affect miss rate?

**Gotchas:**
- Going from 97% to 99% hit rate doubles throughput — small miss rate improvements matter enormously.
- C stores rows contiguously (row-major). Column traversal = miss every access.
- Blocking helps only when $3B^2 < C$; if tiles don't fit, there's no reuse benefit.

**See also:** [[wiki/concepts/cache-optimization]]

---

## OpenMP

**Fork-join model:** Master forks a team; all execute the parallel block; implicit barrier at `}` joins them.

**Hello World pattern:**
```c
omp_set_num_threads(N);
#pragma omp parallel
{
    int id = omp_get_thread_num();
    int nthrds = omp_get_num_threads();
    // work
}
```

**Thread count precedence** (highest to lowest):
1. `num_threads(n)` clause on `#pragma omp parallel`
2. `omp_set_num_threads(n)` in code
3. `OMP_NUM_THREADS` environment variable
4. Implementation default (usually = hardware core count)

**Race conditions and deadlocks:**
- *Race*: ≥2 threads access same variable, ≥1 writes, no sync → undefined result.
- *Deadlock*: circular wait — Thread A holds R1 wants R2; Thread B holds R2 wants R1.

**False sharing:** Threads write to different vars that share a cache line. Each write invalidates the line on all other cores → line bounces between caches.

```
// Problem: sum[0] and sum[1] share a cache line
double sum[NTHREADS];  sum[id] += ...;

// Fix 1: Pad
double sum[NTHREADS][8];  // 8 doubles = 64 bytes = one cache line

// Fix 2: Private scalar + critical
double mysum = 0.0;
for (...) mysum += ...;
#pragma omp critical
    pi += mysum * step;

// Fix 3: reduction clause (best)
#pragma omp parallel for reduction(+:sum)
```

**MESI cache coherence states:**

| State | Meaning |
|---|---|
| Modified | Dirty; only this core has the line |
| Exclusive | Clean; only this core has it |
| Shared | Multiple cores hold valid copies |
| Invalid | Stale; must reload |

Write to an S-state line → all other cores go to I. This is the mechanism behind false sharing overhead.

**Parallel loops:**
```c
#pragma omp parallel for schedule(static, chunk)
for (int i = 0; i < N; i++) { ... }
```

Schedule choices:
- `static`: equal-size blocks assigned at compile time — use when iterations have equal cost.
- `dynamic`: threads pull chunks from a queue at runtime — use when iteration cost varies.
- `guided`: exponentially shrinking chunks — good for tail-heavy workloads.

**Removing loop-carried dependencies:**
```c
// Bad: j depends on previous iteration
int j = 5;
for (int i = 0; i < MAX; i++) { j += 2; A[i] = big(j); }

// Fixed: compute j from i analytically
#pragma omp parallel for
for (int i = 0; i < MAX; i++) { int j = 5 + 2*(i+1); A[i] = big(j); }
```

**Reduction clause:**

```c
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < N; i++) sum += A[i];
```

| Operator | Initial value |
|---|---|
| `+`, `-` | 0 |
| `*` | 1 |
| `min` | Largest positive |
| `max` | Most negative |

`reduction` vs `critical`: reduction = private copy per thread, merge at end (fast); critical = mutex serialized at every update (slow if in inner loop).

**Data environment:**

| Clause            | Effect                                                          |
| ----------------- | --------------------------------------------------------------- |
| `shared(x)`       | All threads share one copy                                      |
| `private(x)`      | Each thread gets own **uninitialized** copy; original unchanged |
| `firstprivate(x)` | Private copy **initialized** to original value                  |
| `default(none)`   | Compiler forces you to declare every variable explicitly        |

**`nowait`:** Skip the implied barrier at the end of a worksharing construct when the next work doesn't depend on it.

**OpenMP Tasks** (for irregular parallelism — linked lists, recursion):
```c
#pragma omp parallel
{
    #pragma omp single  // one thread creates tasks
    {
        struct node *p = listhead;
        while (p) {
            #pragma omp task firstprivate(p)  // copy p now before it advances
                process(p);
            p = p->next;
        }
    }
}
```

Task data scoping defaults:
- Outer `parallel` shared vars → `shared` in task.
- Outer `parallel` private vars → `firstprivate` in task (copy at creation time).
- Vars declared inside task → `private`.

`taskwait` waits for **direct children** only (not all descendants).

**Common exam questions:**
- Identify whether a given program has a race condition.
- Why does padding fix false sharing? How much padding is needed?
- What is the output of a parallel section? (often: order is undefined but each thread runs once)
- When is `dynamic` scheduling preferred over `static`?
- What is the difference between `private` and `firstprivate`?
- What does `default(none)` do and why use it?

**Gotchas:**
- `private(x)` — the variable inside the parallel region is **uninitialized** even if `x` had a value outside. Use `firstprivate` if you need the initial value.
- In task Fibonacci, `x` and `y` must be `shared` on the task (not `firstprivate`) so the child can write results back to the parent.
- `taskwait` only waits for **child** tasks, not grandchildren.
- An implied barrier exists at the end of `#pragma omp for` and `#pragma omp single` — use `nowait` to skip it.

**See also:** [[wiki/concepts/openmp]]

---

## Parallel Performance Analysis

**General speedup formula:**

$$\psi(n, p) \leq \frac{\sigma(n) + \varphi(n)}{\sigma(n) + \varphi(n)/p + \kappa(n,p)}$$

where $\sigma$ = serial work, $\varphi$ = parallel work, $\kappa$ = overhead.

**Parallel efficiency:** $\varepsilon = \psi/p \in (0, 1]$

---

### Amdahl's Law

*Assumption: fixed problem size.*

$$\boxed{\psi \leq \frac{1}{f + \dfrac{1-f}{p}}}$$

$f$ = fraction of time that is inherently serial.

As $p \to \infty$: $\psi \to 1/f$.

| Serial fraction $f$ | Max speedup ($p \to \infty$) |
|---|---|
| 1% | 100× |
| 5% | 20× |
| 10% | 10× |
| 20% | 5× |
| 50% | 2× |

**Worked example:** 80% parallelizable, 8 processors:
$$\psi \leq \frac{1}{0.2 + 0.8/8} = \frac{1}{0.3} \approx 3.33$$

**Limitation:** Ignores communication overhead $\kappa$; assumes problem size is fixed.

---

### Gustafson-Barsis Law

*Assumption: fixed wall-clock time (scale problem to fill available cores).*

$$\boxed{\psi \leq p + (1-p)s}$$

$s$ = fraction of **parallel** run time spent in sequential code.

Speedup grows linearly with $p$ — far more optimistic than Amdahl.

**Worked example:** 32 processors, 5% sequential fraction:
$$\psi = 32 + (1-32)(0.05) = 32 - 1.55 = 30.45$$

**Comparison:**

| | Amdahl | Gustafson-Barsis |
|---|---|---|
| Problem size | Fixed | Grows with $p$ |
| Speedup bound | Converges to $1/f$ | Grows linearly |
| Use case | "Solve this exact problem faster" | "Solve a bigger problem in the same time" |

---

### Roofline Model

Plot attainable GFlop/s vs. **operational intensity** (FLOP/byte of memory traffic):

- **Left of ridge point** (low intensity) → memory-bound; performance scales with bandwidth.
- **Right of ridge point** (high intensity) → compute-bound; performance scales with FLOP/s.

Ridge point $= \text{Peak FLOP/s} / \text{Peak bandwidth}$.

A kernel's position on the roofline tells you which resource to optimize first.

**Common exam questions:**
- Given $f$ and $p$, compute Amdahl speedup.
- Given a scaled speedup target and $p$, solve for maximum $s$.
- Distinguish Amdahl vs. Gustafson-Barsis: which applies when problem size is fixed?
- Classify a kernel as memory-bound or compute-bound given FLOP count and memory bytes.

**Gotchas:**
- Amdahl $f$ is the fraction of **total serial time** that is sequential; Gustafson $s$ is the fraction of **parallel wall-clock time** that is sequential — they are different quantities.
- Amdahl ignores $\kappa$ → overestimates achievable speedup.
- Gustafson doesn't mean parallelism is always efficient; it means the serial overhead is relatively smaller when you scale the problem up.

**See also:** [[wiki/concepts/parallel-performance]]

---

## GPU Architecture and CUDA

### Why GPUs?

CPUs optimize for **latency** (one thread fast); GPUs optimize for **throughput** (thousands of threads hide latency). A GPU has thousands of simpler cores running at ~1 GHz vs. a CPU's few complex cores at ~3 GHz.

Power: $P \propto f^3$ → 30% frequency reduction gives 65% power savings; run 2 cores for the same budget at 140% performance.

**SIMD extensions (CPU):**

| Extension | Width | FP32 words |
|---|---|---|
| SSE | 128-bit | 4 |
| AVX | 256-bit | 8 |
| AVX-512 | 512-bit | 16 |

Ignoring SIMD wastes up to 94% of FP throughput (AVX-512). GPU warps are 32-wide SIMT.

---

### CUDA Programming Model

**Minimal extensions:**
```cuda
__global__ void Kernel(...);         // runs on GPU, called from CPU
__device__ void DevFunc(...);        // runs on GPU, called from GPU
__shared__ float s[BLOCK];          // per-block on-chip memory
Kernel<<<numBlocks, threadsPerBlock>>>(...);  // launch
__syncthreads();                     // barrier within a block
```

**Step-by-step pattern:**
1. `malloc` host arrays
2. `cudaMalloc` device arrays
3. `cudaMemcpy(..., HostToDevice)`
4. `Kernel<<<grid, block>>>(...)`
5. `cudaMemcpy(..., DeviceToHost)`
6. `cudaFree` / `free`

**Thread hierarchy:**

| Software | Hardware | Notes |
|---|---|---|
| Thread | CUDA core | Has registers |
| Block | Streaming Multiprocessor (SM) | Has shared memory; lifetime on one SM |
| Grid | GPU chip | Multiple blocks may share an SM |

```cuda
uint tid = threadIdx.x + blockDim.x * blockIdx.x;  // 1D global thread ID
```

**Hardware limits:**
- Max threads/block: **1024**
- Max grid x-dimension: **$2^{31} - 1$**

**Stride loop for large arrays** ($n >$ grid × block):
```cuda
uint tid = threadIdx.x + blockDim.x * blockIdx.x;
while (tid < n) {
    C[tid] = A[tid] + B[tid];
    tid += blockDim.x * gridDim.x;
}
```

---

### Warps and Warp Divergence

32 threads in a warp execute the **same instruction** simultaneously (SIMT). The warp scheduler issues one instruction per clock; if a warp is waiting on memory, it switches to another ready warp instantly — zero-cost context switch.

**Warp divergence:**
- **Within-warp** (`threadIdx.x % 2`): both branches run serially, inactive threads masked off. **Performance penalty.**
- **Between-warp** (`blockIdx.x % 2`): each warp takes one branch. **No penalty.**

```cuda
if (threadIdx.x % 2 == 0) ...  // BAD — within-warp divergence
if (blockIdx.x  % 2 == 0) ...  // OK  — between-warp divergence
```

---

### GPU Memory Hierarchy

| Memory | Location | Scope | Speed |
|---|---|---|---|
| Registers | On-chip/thread | Thread | Fastest (~19 cycles on V100) |
| Shared memory | On-chip/block | Block | Very fast (~28 cycles); 32 banks |
| L1/L2 | On-chip | SM/chip | Automatic cache |
| Global (DRAM) | Off-chip | All | Slowest (~1029 cycles on V100) |
| Local | Off-chip (DRAM region) | Thread | Same as global; register spill target |

**Arithmetic intensity target:** ~16 FLOP/byte to saturate a NVIDIA Volta GPU (14 TFLOP/s ÷ 0.9 TB/s).

---

### Memory Coalescing

32 consecutive threads accessing 32 consecutive addresses = **4 transactions** at 100% utilization.

| Pattern | Transactions | Utilization |
|---|---|---|
| Sequential `a[tid]` | 4 | 100% |
| Shifted `a[tid-1]` | 5 | 80% |
| Same element `a[33]` | 1 | 12.5% |
| Stride-3 | 12 | 33% |
| Random | 32 | 12.5% |

**AoS → SoA:** accessing `a[tid].x` in an Array of Structs is strided (bad). Transpose to Structure of Arrays so `x[tid]` accesses are sequential (good).

---

### Shared Memory and Bank Conflicts

32 banks; element $i$ is in bank $i \bmod 32$. Two threads in the same warp accessing different addresses in the same bank → **bank conflict** → serialized.

- No conflict: all 32 threads access **different banks** → 1 cycle.
- $k$-way conflict: $k$ threads share a bank → $k$ cycles.
- Broadcast: all threads access **the same address** → no conflict (hardware broadcasts).

To avoid: access consecutive elements; restructure data layout.

---

### Parallel Reduction

**No global sync across blocks in CUDA.** Use two-kernel approach:
1. Each block reduces its chunk to one partial sum stored in global memory.
2. One block reduces the partial sums.

**Algorithm evolution:**

1. **Interleaved addressing** (naive): `tid % (2*s) == 0` — warp divergence + slow `%`.
2. **Non-divergent stride**: `index = 2*s*tid` — no divergence but bank conflicts.
3. **Sequential addressing** (best):
```cuda
for (uint s = blockDim.x/2; s > 0; s >>= 1) {
    if (tid < s)
        sdata[tid] += sdata[tid + s];  // adjacent banks → no conflict
    __syncthreads();
}
```
4. **warpReduce unrolling** (last warp): when $s < 32$, only 1 warp active — no `__syncthreads` needed:
```cuda
__device__ void warpReduce(volatile int* sdata, int tid) {
    sdata[tid] += sdata[tid+32]; sdata[tid] += sdata[tid+16];
    sdata[tid] += sdata[tid+8];  sdata[tid] += sdata[tid+4];
    sdata[tid] += sdata[tid+2];  sdata[tid] += sdata[tid+1];
}
```
`volatile` prevents compiler reordering/caching of writes.

---

**Common exam questions:**
- Given a kernel launch `<<<G, B>>>`, compute thread ID for a given `blockIdx` / `threadIdx`.
- Identify whether a memory access pattern is coalesced. Compute the number of transactions.
- Explain why warp divergence causes a performance penalty within a warp but not between warps.
- What is the difference between shared memory and global memory? When do you use each?
- Why does sequential addressing in reduction avoid bank conflicts?
- What is register spilling and when does it occur?

**Gotchas:**
- `__syncthreads()` synchronizes threads **within a block only** — you cannot synchronize across blocks.
- Register spilling goes to **local memory** (same speed as global memory = slow).
- `volatile` is required in warpReduce — without it, the compiler may cache `sdata[tid]` in a register and never see updates from sibling threads.
- Shared memory bank conflicts require threads in the **same warp** — inter-warp conflicts don't exist.
- A block is assigned to one SM for its entire lifetime; it cannot migrate.

**See also:** [[wiki/concepts/gpu-cuda]]

---

## Concept Connections

```
Parallel Fundamentals
    ├─ Why parallelism (clock plateau, power) → motivates both OpenMP and CUDA
    ├─ Flynn taxonomy: MIMD → OpenMP (multicore); SIMD → CUDA warps
    └─ Shared vs. distributed memory → OpenMP vs. MPI

Cache Optimization
    ├─ Locality principle → also applies inside GPU (shared memory = software-managed cache)
    ├─ Loop ordering → carries into GPU coalescing (sequential access = fast)
    └─ Blocking → analogous to GPU tiling into shared memory

OpenMP
    ├─ Fork-join → different from CUDA's single-kernel-launch model
    ├─ False sharing → MESI coherence; analogous to shared memory bank conflicts in CUDA
    ├─ Reduction → private-copy merge; analogous to parallel reduction in CUDA
    └─ Tasks → irregular parallelism; no direct CUDA analog (dynamic parallelism exists)

Parallel Performance
    ├─ Amdahl: serial fraction limits speedup regardless of OpenMP or CUDA
    ├─ Gustafson: scale problem → GPU's massive thread count makes more sense here
    └─ Roofline: GPU is almost always memory-bound; coalescing directly increases op intensity

GPU / CUDA
    ├─ Warp divergence ↔ branch misprediction in CPUs (but different mechanism)
    ├─ Shared memory ↔ register file / L1 in CPU hierarchy
    └─ Parallel reduction = the GPU answer to OpenMP's reduction clause
```

---

## Practice Questions

1. A parallel program has a serial fraction of 8% and runs on 16 cores. Compute the maximum speedup using Amdahl's Law. What is the speedup limit as $p \to \infty$?

2. A matrix multiplication kernel uses ijk loop order with matrices of size $n = 1000$. Assuming cache line = 32 bytes (4 doubles) and cache much smaller than the matrices, how many cache misses occur per inner-loop iteration for A, B, and C? How would switching to kij change these numbers?

3. A program runs 100 seconds in parallel on 10 processors, with 4 of those seconds spent in serial code. Compute the scaled speedup using Gustafson-Barsis Law.

4. You write an OpenMP program that accumulates a sum using a shared array `double sum[NTHREADS]` where thread $i$ writes to `sum[i]`. Performance degrades as thread count increases. Diagnose the problem and propose two fixes.

5. Explain the difference between `private(x)` and `firstprivate(x)`. Give a concrete example where using `private` instead of `firstprivate` would produce incorrect results.

6. A CUDA kernel launches with `<<<256, 128>>>`. Thread with `blockIdx.x = 3, threadIdx.x = 7` computes its global ID. What is it? If the array has $n = 40000$ elements, does this thread need a stride loop?

7. In a CUDA parallel reduction, why is sequential addressing (stride halving with `s >>= 1`) preferred over interleaved addressing (stride doubling with `tid % (2*s) == 0`)? What are the two separate performance problems with interleaved addressing?

8. You have a CUDA kernel accessing a struct array `particles[tid].vx`. The struct contains four floats `{x, y, vx, vy}`. Why is this access pattern bad? How would you restructure the data to fix it?

9. Explain the MESI cache coherence protocol. Walk through what happens when two cores A and B both cache the same line, B writes to it, and then A reads it again.

10. A GPU kernel performs 2048 FLOPs and reads 256 bytes from global memory per thread. Given peak throughput of 14 TFLOP/s and peak bandwidth of 0.9 TB/s, is this kernel memory-bound or compute-bound? What is its operational intensity and where does it fall on the roofline?
