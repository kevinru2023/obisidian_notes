---
title: "GPU Architecture and CUDA Programming"
type: concept
sources:
  - "[[raw-sources/courses/CS475/07_GPU_basics.pdf]]"
  - "[[raw-sources/courses/CS475/08_GPU_basics_cont.pdf]]"
related:
  - "[[wiki/courses/CS475]]"
  - "[[wiki/concepts/parallel-programming-fundamentals]]"
  - "[[wiki/concepts/cache-optimization]]"
  - "[[wiki/concepts/openmp]]"
updated: 2026-04-24
tags: [cs475, gpu, cuda, parallel-programming, hpc]
---

# GPU Architecture and CUDA Programming

---

## Why GPUs?

CPU clock frequency has plateaued (~3 GHz since ~2005) due to transistor shrinkage limits and power density. The solution: **more cores**. Reducing frequency by 30% cuts power by ~65% (power $\propto f^3$) and runs two cores at 140% of original performance for the same power budget.

**Heterogeneous computing** pairs a **latency-optimized CPU** (fast serial processing with large caches and sophisticated branch prediction) with a **throughput-optimized GPU** (thousands of simple cores that hide latency with massive multithreading).

| | CPU | GPU |
|---|---|---|
| Clock | 3 GHz | 1 GHz |
| Main memory latency | ~100+ ns | ~300+ ns |
| Arithmetic latency | ~1+ ns | ~10+ ns |
| Design goal | Minimize latency of 1 thread | Maximize throughput of all threads |
| Cache strategy | Large caches | Skip caches, hide latency via multithreading |

*(Numbers from Kepler-era GPUs, e.g. GTX 700 / Tesla K20)*

---

## SIMD

**Single Instruction Multiple Data (SIMD)** applies one instruction to multiple data simultaneously. It is distinct from thread-level parallelism — each CPU core has its own SIMD unit, so both can be combined.

| Year | Extension | Width | FP32 words |
|---|---|---|---|
| 1996 | MMX | 64 bits | 2 |
| 1999 | SSE | 128 bits | 4 |
| 2011 | AVX | 256 bits | 8 |
| 2013 | AVX-512 | 512 bits | 16 (= one cache line, one 4×4 matrix) |

Neglecting SIMD is increasingly expensive: AVX wastes 87.5% of potential FP throughput; NVIDIA GPUs have 32-way SIMD and AMD GPUs have 64-way. OpenMP, Pthreads, and MPI all neglect SIMD — use `#pragma omp simd` or assembly intrinsics.

---

## GPU Programming Models

| Model | Notes |
|---|---|
| **CUDA** | NVIDIA-only; most mature, largest ecosystem; C++ with minimal extensions |
| **OpenACC** | Directive-based (like OpenMP); good portability, less fine-grained control |
| **OpenMP 4.0+** | GPU offload; hardware-independent; hard to get peak performance |
| **ROCm / HIP** | AMD's open CUDA equivalent; HIP can target both NVIDIA and AMD |
| **OpenCL** | Multi-architecture (CPU/GPU/FPGA); low-level; functional but not performance portable |
| **SYCL** | C++17-based; performance portable; multiple vendor implementations |

**Why CUDA?** Most mature ecosystem, C/C++ familiarity, full hardware access. NVIDIA GPUs dominate AI/ML/HPC workloads. Paper usage ~9000/year by 2019, dwarfing all alternatives.

---

## CUDA Basics

### Minimal Extensions to C++

```cuda
__global__ void KernelFunc(...);   // kernel: callable from host, runs on device
__device__ void DeviceFunc(...);   // device-only helper function
__device__ int GlobalVar;          // variable in device global memory
__shared__ int SharedVar;          // variable in per-block shared memory

KernelFunc<<<512, 128>>>(...);     // launch: 512 blocks × 128 threads each

dim3 threadIdx;  dim3 blockIdx;  dim3 blockDim;  // built-in thread ID vars

__syncthreads();                   // barrier within a block
```

### Step-by-Step Programming Pattern

```
1. Allocate host arrays (malloc)
2. Allocate device arrays (cudaMalloc)
3. Copy input from host to device (cudaMemcpy, HostToDevice)
4. Launch kernel <<<grid, block>>>
5. Copy output from device to host (cudaMemcpy, DeviceToHost)
6. Free device memory (cudaFree)
7. Free host memory (free)
```

Note: `cudaMemcpy` can be asynchronous; unified memory management (`cudaMallocManaged`) is also available.

### Compiling and Running

```bash
module load cuda/11.8                        # on COE cluster (avoid cuda/13.1+)
nvcc vector_addition.cu -o vector_addition
srun -A cs475-575 -p classgpu --gpus=1 --constraint=v100 --pty bash
```

---

## GPU Thread Hierarchy

CUDA exposes three levels of parallelism, each mapping to a hardware unit:

| Software | Hardware |
|---|---|
| Thread | CUDA Core |
| Thread Block | Streaming Multiprocessor (SM) |
| Grid (of Blocks) | GPU chip |

```
Thread → Core
Block  → SM      (one block per SM; multiple blocks may share one SM)
Grid   → GPU
```

### `dim3` Grid/Block Specification

```cuda
dim3 block(8, 8, 8);      // 8×8×8 threads per block (512 total)
dim3 grid(128, 128, 1);   // 128×128 blocks in the grid
Kernel<<<grid, block>>>(...);
```

Grids and blocks can be 1D, 2D, or 3D. Thread index computation for 1D:

```cuda
uint tid = threadIdx.x + blockDim.x * blockIdx.x;
```

### Hardware Limits

| Property | Value |
|---|---|
| Max threads per block | 1024 |
| Max x-dimension of block | 1024 |
| Max z-dimension of block | 64 |
| Max x-dimension of grid | $2^{31} - 1$ |
| Max y/z-dimension of grid | 65535 |

**Handling large arrays:** When $n > \text{maxBlocks} \times \text{threadsPerBlock}$, use a stride loop:

```cuda
uint tid = threadIdx.x + blockDim.x * blockIdx.x;
while (tid < size) {
    C[tid] = A[tid] + B[tid];
    tid += blockDim.x * gridDim.x;   // stride = total thread count
}
```

---

## Streaming Multiprocessors and Warps

### SM Structure

A **Streaming Multiprocessor (SM)** is the fundamental GPU building block. Thread blocks are assigned to SMs for their **entire lifecycle** — no migration between SMs. Multiple blocks may share one SM; one block cannot span multiple SMs.

$$\text{Total Parallelism} = \text{Number of SMs} \times \text{CUDA cores per SM}$$

### Warps

Inside an SM, threads are grouped into **warps of 32 threads**. All 32 threads in a warp execute the **same instruction** at the same time (SIMT — Single Instruction Multiple Thread). There is only one instruction unit per warp.

**Warp Divergence** occurs when threads within the same warp take different branches:
- **Within-warp divergence:** The two paths are serialized — some threads are masked off while the others run. **Performance penalty.**
- **Between-warp divergence:** Each warp independently takes one branch — no serialization. **No penalty.**

```cuda
if (threadIdx.x % 2 == 0) ...   // within-warp divergence — BAD
if (blockIdx.x % 2 == 0)  ...   // between-warp divergence — fine
```

### Warp Scheduler

The **warp scheduler** hides memory latency: every clock cycle it issues an instruction from one of its resident warps. If the selected warp is waiting on memory, the scheduler instantly switches to another warp that is ready — zero stall overhead compared to CPU context switching.

---

## GPU Memory Hierarchy

| Memory | Location | Scope | Speed | Notes |
|---|---|---|---|---|
| Registers | On-chip (per thread) | Thread | Fastest (~10× faster than shared) | Spills to local if exhausted |
| Shared Memory | On-chip (per block) | Block | Very fast (~28 cycles on V100) | Same hardware as L1; 32 banks |
| L1/L2 Cache | On-chip | SM / chip | Fast | Automatic; L2 shared across SMs |
| Constant Memory | Off-chip, cached | All kernels | Fast if broadcast | Read-only; good for parameters |
| Texture Memory | Off-chip, cached | All kernels | Fast for 2D spatial locality | Read-only |
| Local Memory | Off-chip (global mem) | Thread | Slow | Register overflow; automatic |
| Global Memory | DRAM | All kernels | Slowest on-GPU | `cudaMalloc`; main data store |
| Host Memory | CPU RAM | — | Very slow | Cross-PCIe; avoid in hot paths |

**V100 latency hierarchy (approximate):**
- Registers: ~19 cycles
- Shared memory / L1: ~28 cycles
- L2 cache: ~193 cycles
- HBM2 (global memory): ~1029 cycles

### Arithmetic Intensity

GPUs are **IO-limited**. The ratio of compute to memory bandwidth determines the bottleneck:

- Sandy Bridge-EP CPU: $396\ \text{GFLOP/s} / 51\ \text{GB/s} \approx 7.8\ \text{FLOP/byte}$
- Tesla K20 GPU: $3924\ \text{GFLOP/s} / 250\ \text{GB/s} \approx 15.7\ \text{FLOP/byte}$
- NVIDIA Volta FP32: $14\ \text{TFLOP/s} / 0.9\ \text{TB/s} \approx 15.6\ \text{FLOP/byte}$

To sustain peak GPU performance, each kernel must perform **~16 FLOPs per byte** loaded from global memory.

---

## Global Memory and Coalescing

Global memory (DRAM) is the slowest GPU memory. Accesses trigger **transactions** of 32 bytes (L2-cached) or 128 bytes (L1-cached). Transactions are always aligned to their size and always fully read/written.

$$\text{Degree of coalescing} = \frac{\text{bytes requested}}{\text{bytes transferred}}$$

| Access pattern | Transactions | Bus utilization |
|---|---|---|
| 32 adjacent threads, sequential `a[tid]` | 4 | 100% |
| 32 adjacent threads, shifted `a[tid-1]` | 5 | 80% |
| 32 threads, all access same element `a[33]` | 1 | 12.5% |
| 32 threads, stride-3 access | 12 | 33% |
| 32 threads, fully random | 32 | 12.5% |

**AoS vs. SoA:** Accessing a field of an Array of Structs (e.g. `a[tid].x`) is strided, causing poor coalescing. Prefer Structure of Arrays (SoA) for GPU data. Transposing the data structure costs far less than uncoalesced accesses.

---

## Shared Memory and Bank Conflicts

Shared memory is on-chip per-block memory — same hardware as L1 cache. It is programmer-managed (not a cache) and is the primary tool for avoiding repeated global memory accesses.

**Common pattern:**
```cuda
__shared__ int scratch[BLOCKSIZE];
scratch[threadIdx.x] = global_in[blockIdx.x * blockDim.x + threadIdx.x];
__syncthreads();
// compute using scratch[]
global_out[...] = scratch[...];
```

### Bank Conflicts

Shared memory is divided into **32 banks**. Element $i$ resides in bank $i \bmod 32$. A **bank conflict** occurs when two or more threads in the same warp access **different addresses in the same bank** — accesses are serialized.

- No conflict: all 32 threads access different banks → 1 cycle
- 2-way conflict: 2 threads share a bank → 2 cycles
- Broadcast: all threads access the **same address** → no conflict (HW handles it)

To avoid conflicts, access consecutive elements or restructure data layout.

---

## Register File and Register Spilling

Registers are the fastest storage (~10× faster than shared memory). Each SM has tens of thousands of 32-bit registers, limited to ~32–64 per thread. Variables declared on the stack in kernels go to registers by default.

**Register spilling:** When a thread needs more registers than available, the compiler spills to **local memory** (a reserved region of global memory) — slow. Spilling incurs extra loads and stores and pipeline stalls on dependent instructions.

To avoid spilling:
- Limit scalar temporaries
- Use shared memory for inter-thread communication instead of large per-thread arrays

---

## Parallel Reduction

**Problem:** Sum (or other reduction) of an $n$-element array on the GPU.

**Key constraint:** CUDA has no global synchronization across blocks. Solution: **kernel decomposition** — each kernel launch acts as a global barrier.

```
Level 0: Each block reduces its chunk → partial results in global memory
Level 1: One block reduces the partial results → final answer
```

### Algorithm Evolution

**1. Interleaved addressing (naive):**
```cuda
for (uint s = 1; s < blockDim.x; s *= 2) {
    if (tid % (2*s) == 0)          // divergent warp + expensive % operator
        sdata[tid] += sdata[tid + s];
    __syncthreads();
}
```
Problem: `tid % (2*s)` causes **warp divergence** and is slow.

**2. Non-divergent strided indexing:**
```cuda
for (uint s = 1; s < blockDim.x; s *= 2) {
    int index = 2 * s * tid;
    if (index < blockDim.x)        // all active threads in same branch
        sdata[index] += sdata[index + s];
    __syncthreads();
}
```
Problem: **shared memory bank conflicts** (strided access pattern).

**3. Sequential addressing (bank-conflict-free):**
```cuda
for (uint s = blockDim.x / 2; s > 0; s >>= 1) {
    if (tid < s)
        sdata[tid] += sdata[tid + s];   // adjacent threads → adjacent banks
    __syncthreads();
}
```
Adjacent threads access adjacent banks → **no bank conflicts**.

**4. Warp unrolling (CS575 optimization):**
When $s < 32$, only one warp remains — `if` guards and `__syncthreads()` are unnecessary overhead. Unroll the last 6 iterations:

```cuda
__device__ void warpReduce(volatile int* sdata, int tid) {
    sdata[tid] += sdata[tid + 32];
    sdata[tid] += sdata[tid + 16];
    sdata[tid] += sdata[tid +  8];
    sdata[tid] += sdata[tid +  4];
    sdata[tid] += sdata[tid +  2];
    sdata[tid] += sdata[tid +  1];
}
```

`volatile` is required so the compiler does not reorder or cache these accesses.

---

## GPU Programming Best Practices

| Goal | Technique |
|---|---|
| Maximize global memory throughput | Coalesced (sequential) access patterns; SoA over AoS |
| Reduce global memory traffic | Tile into shared memory; reuse data within a block |
| Avoid serialization | Eliminate within-warp divergence; use sequential reduction addressing |
| Avoid shared memory stalls | Avoid bank conflicts; access consecutive elements |
| Avoid register pressure | Limit temporaries; spill to shared memory instead of local memory |
| Hide memory latency | Launch enough warps per SM to keep the warp scheduler busy |
