---
title: "OpenMP"
type: concept
sources:
  - "[[raw-sources/courses/CS475/03_Cache_cont_and_OpenMP.pdf]]"
  - "[[raw-sources/courses/CS475/04_OpenMP.pdf]]"
  - "[[raw-sources/courses/CS475/05_OpenMP_cont.pdf]]"
  - "[[raw-sources/courses/CS475/06_OpenMP_task_and_performance.pdf]]"
related:
  - "[[wiki/courses/CS475]]"
  - "[[wiki/concepts/parallel-programming-fundamentals]]"
  - "[[wiki/concepts/parallel-performance]]"
updated: 2026-04-20
tags: [openmp, shared-memory, parallel-programming, cs475]
---

# OpenMP

## What Is OpenMP?

**Open Multi-Processing** — a portable, high-level API for shared-memory parallel programming in C, C++, and Fortran.

Provided by a consortium of companies, labs, and universities. Requires compiler support (`gcc -fopenmp`, `icc -openmp`).

OpenMP gives the biggest multithread benefit per amount of programming effort — most parallelism is expressed with a few pragmas.

---

## What OpenMP Does (and Doesn't Do)

**Will do:**
- Separate a program into serial and parallel regions
- Hide thread creation/destruction and stack management
- Provide synchronization constructs (barriers, locks, atomics)

**Will not:**
- Parallelize code automatically
- Guarantee speedup
- Provide freedom from data races — that's the programmer's responsibility

---

## Fork-Join Execution Model

OpenMP uses a **fork-join** model:

1. Program begins as a single **master thread** (serial).
2. At a parallel region, master **forks** a team of threads.
3. All threads execute the region concurrently.
4. At the end of the region, threads **join** (synchronize at a barrier) and execution returns to the master.

```
Master ──────────────────────────────────────────────────────▶
               │fork                    │fork
               ├── Thread 1             ├── Thread 1
               ├── Thread 2   barrier   ├── Thread 2  barrier
               └── Thread 3 ──────────▶└── Thread 2 ────────▶
```

---

## Shared vs. Private Variables

In a parallel region:
- **Shared variables**: visible to all threads (e.g., global/heap variables). Threads communicate by reading/writing shared state.
- **Private variables**: each thread has its own copy (e.g., loop counters, local variables declared inside a parallel block).

Data races occur when two threads access the same shared variable concurrently and at least one write — must be handled with synchronization.

---

## Pragma Syntax

```c
#pragma omp directive [clause [clause ...]]
```

All OpenMP directives are `#pragma omp ...` — ignored by non-OpenMP compilers, so code degrades gracefully to serial.

---

## Hello World: Serial vs. Pthreads vs. OpenMP

**Serial:**
```c
int main() {
    printf("Hello, World!\n");
    return 0;
}
```

**Pthreads (explicit, verbose):**
```c
void* SayHello(void *foo) {
    printf("Hello, world!\n");
    return NULL;
}
int main() {
    pthread_t threads[16];
    for (int tn = 0; tn < 16; tn++)
        pthread_create(&threads[tn], NULL, SayHello, NULL);
    for (int tn = 0; tn < 16; tn++)
        pthread_join(threads[tn], NULL);
    return 0;
}
// gcc -lpthread
```

**OpenMP (concise):**
```c
int main() {
    omp_set_num_threads(16);
    #pragma omp parallel
    {
        printf("Hello, World!\n");
    }
    return 0;
}
// gcc -fopenmp
```

OpenMP hides all thread lifecycle management.

---

## Shared Memory Programming Options (Comparison)

| Library | Level | Notes |
|---------|-------|-------|
| **Pthreads** | Low | POSIX standard; portable but verbose and heavyweight |
| **OpenMP** | High | Best effort-to-benefit ratio; scientific computing focus |
| **TBB** | Medium | Intel Thread Building Blocks; task-based |
| **CILK** | Medium | Lightweight threads embedded in C |
| **Java threads** | High | Built on Pthreads; object-oriented |

---

## Memory Model

```
           Shared Memory
         ┌────────────────┐
         │  s (shared)    │
         └────────────────┘
              ↑     ↑
    P0: y=..s..   Pn: s=...
    (private: i)  (private: i)
```

Each processor has private local variables (stack). Shared variables live in a common address space. Threads communicate implicitly through writes to shared state.

---

## Compilation

| Compiler | Flag |
|----------|------|
| GCC (Linux/macOS) | `gcc -fopenmp` |
| Intel (Linux/macOS) | `icc -fopenmp` |
| Intel (Linux @ NERSC) | `cc -qopenmp` |
| Intel (Windows) | `icl /Qopenmp` |

Set thread count at runtime:
```bash
export OMP_NUM_THREADS=8
./program
```

Or in code: `omp_set_num_threads(8);`

---

## Two Key Problems in Parallel Programming

### Race Conditions

A **race condition** (data race) occurs when:
1. Two threads access the same variable
2. At least one access is a write
3. The accesses are not synchronized

```c
int s = 0;
// Thread 1: for i = 0..n/2-1: s = s + 1
// Thread 2: for i = n/2..n-1: s = s + 1
// Final value of s with n=100 is UNDEFINED — not necessarily 100
```

### Deadlocks

A **deadlock** occurs when two or more threads are each waiting for a resource held by the other — circular dependency, no progress possible.

```
Thread 1: holds R1, waiting for R2
Thread 2: holds R2, waiting for R1   ← stuck forever
```

---

## OpenMP Common Core

| Pragma / Function / Clause | Purpose |
|---|---|
| `#pragma omp parallel` | Fork a team of threads; structured block executes on all |
| `omp_set_num_threads(n)` | Request $n$ threads for subsequent parallel regions |
| `omp_get_thread_num()` | Return this thread's ID (0 to nthrds−1) |
| `omp_get_num_threads()` | Return actual number of threads in current team |
| `omp_get_num_procs()` | Return number of available cores |
| `omp_get_wtime()` | Wall-clock timer (double, seconds) |
| `setenv OMP_NUM_THREADS N` | Set default thread count via environment |
| `#pragma omp barrier` | All threads wait until every thread reaches this point |
| `#pragma omp critical` | Mutual exclusion — one thread at a time |
| `#pragma omp for` | Distribute loop iterations across thread team |
| `#pragma omp parallel for` | Shortcut combining parallel + for |
| `reduction(op:list)` | Thread-local accumulation merged at end |
| `schedule(static [,chunk])` | Assign contiguous blocks at compile time |
| `schedule(dynamic [,chunk])` | Assign chunks at runtime from a queue |
| `shared(list)` | Declare variables explicitly shared |
| `private(list)` | Each thread gets its own uninitialized copy |
| `firstprivate(list)` | Private copy initialized from master's value |
| `default(none)` | Force explicit declaration of every variable's scope |
| `nowait` | Disable the implied barrier at end of a workshare |
| `#pragma omp single` | Only one thread executes this block |
| `#pragma omp task` / `taskwait` | Asynchronous task creation and synchronization |

---

## Thread Creation

```c
double A[1000];
omp_set_num_threads(4);
#pragma omp parallel
{
    int id     = omp_get_thread_num();   // 0, 1, 2, or 3
    int nthrds = omp_get_num_threads();  // actual thread count
    pooh(id, A);
    // implicit barrier here — all threads sync before proceeding
}
printf("all done\n");
```

- `A` is **shared** (heap allocation, one copy).
- `id` and `nthrds` are **private** (declared inside the block).
- Implicit barrier at `}` — master waits for all threads.

### Thread Count Precedence

1. `num_threads(n)` clause on `#pragma omp parallel` — overrides for that region only, does **not** change ICV
2. `omp_set_num_threads(n)` — overrides ICV globally
3. `OMP_NUM_THREADS` environment variable — sets initial ICV
4. Implementation default (usually = number of logical CPUs)

---

## Worked Example: Computing π

$$\int_0^1 \frac{4}{1+x^2}\,dx = \pi$$

Approximate via Riemann sum with $N$ rectangles of width $\Delta x = 1/N$:

$$\pi \approx \sum_{i=0}^{N-1} \frac{4}{1 + x_i^2}\,\Delta x, \quad x_i = \left(i + 0.5\right)\Delta x$$

### Serial baseline

```c
static long num_steps = 100000000;
double step = 1.0 / num_steps;
double sum = 0.0;
for (int i = 0; i < num_steps; i++) {
    double x = (i + 0.5) * step;
    sum += 4.0 / (1.0 + x*x);
}
double pi = step * sum;
// ~1.83 seconds on dual-core i5 @ 1.7 GHz
```

### SPMD parallelization (cyclic distribution)

Each thread handles every $P$-th iteration (stride = number of threads):

```c
double sum[NUM_THREADS];
#pragma omp parallel
{
    int id     = omp_get_thread_num();
    int nthrds = omp_get_num_threads();
    sum[id] = 0.0;
    for (int i = id; i < num_steps; i += nthrds) {
        double x = (i + 0.5) * step;
        sum[id] += 4.0 / (1.0 + x*x);
    }
}
for (int i = 0; i < nthreads; i++) pi += sum[i] * step;
```

**Problem — false sharing:** `sum[0]`, `sum[1]`, … are adjacent in memory and share a cache line. Each write by one thread invalidates the line in other cores' caches → cache line bounces between cores.

| Threads | SPMD (no fix) |
|---------|--------------|
| 1 | 1.86 s |
| 2 | 1.03 s |
| 3 | 1.08 s |
| 4 | 0.97 s |

3-thread performance is *worse* than 2-thread — false sharing overhead.

### Fix 1: Padding to separate cache lines

```c
#define PAD 8  // 8 doubles = 64 bytes = one cache line
double sum[NUM_THREADS][PAD];
// Each sum[id][0] now lives on its own cache line
```

| Threads | SPMD | SPMD padded |
|---------|------|-------------|
| 1 | 1.86 | 1.86 |
| 2 | 1.03 | 1.01 |
| 3 | 1.08 | 0.69 |
| 4 | 0.97 | 0.53 |

### Fix 2: Private scalar + `critical` for final merge

```c
#pragma omp parallel
{
    int id = omp_get_thread_num(), nthrds = omp_get_num_threads();
    double sum = 0.0;  // private scalar — no array, no false sharing
    for (int i = id; i < num_steps; i += nthrds) {
        double x = (i + 0.5) * step;
        sum += 4.0 / (1.0 + x*x);
    }
    #pragma omp critical
        pi += sum * step;  // only one thread merges at a time
}
```

| Threads | SPMD padded | SPMD critical |
|---------|-------------|---------------|
| 1 | 1.86 | 1.87 |
| 2 | 1.01 | 1.00 |
| 3 | 0.69 | 0.68 |
| 4 | 0.53 | 0.53 |

---

## False Sharing

**Definition:** Two threads write to different variables that happen to reside on the same cache line. Each write forces the line to be invalidated and re-fetched across cores, serializing what should be independent updates.

**Cause:** Promoting a scalar to a thread-indexed array (`sum[id]`) places all elements contiguously — likely on the same 64-byte cache line.

**Fixes:**
1. **Pad** the array: `double sum[NTHREADS][PAD]` where `PAD = 64/sizeof(double) = 8`.
2. **Use private scalars** inside the parallel region and merge with `critical`.
3. **Use `reduction`** clause (OpenMP handles this automatically).

---

## Synchronization

### `critical` — Mutual Exclusion

Only one thread executes the critical region at a time.

```c
#pragma omp parallel
{
    double B = big_SPMD_job(omp_get_thread_num(), omp_get_num_threads());
    #pragma omp critical
        res += consume(B);  // serialized — one thread at a time
}
```

Placing `critical` inside the inner loop (naïve) serializes most of the work — use it only to merge final partial results.

### `barrier` — Synchronization Point

All threads must reach the barrier before any continue.

```c
#pragma omp parallel
{
    int id = omp_get_thread_num(), nthrds = omp_get_num_threads();
    Arr[id] = big_ugly_calc(id, nthrds);
    #pragma omp barrier          // wait for all Arr[] to be filled
    Brr[id] = use_full_arr(id, nthrds, Arr);
}
```

---

## Parallel Loops

### Basic worksharing

```c
#pragma omp parallel
#pragma omp for
    for (int i = 0; i < N; i++)
        a[i] = a[i] + b[i];
```

Shortcut:
```c
#pragma omp parallel for
    for (int i = 0; i < N; i++)
        a[i] = a[i] + b[i];
```

- Loop index `i` is **private** by default.
- Implicit barrier at the end of the loop.

### Loop-carried dependencies

Must eliminate dependencies before parallelizing:

```c
// Bad — j depends on previous iteration
int j = 5;
for (int i = 0; i < MAX; i++) { j += 2; A[i] = big(j); }

// Fixed — compute j analytically from i
#pragma omp parallel for
for (int i = 0; i < MAX; i++) {
    int j = 5 + 2*(i+1);
    A[i] = big(j);
}
```

### Schedule clause

Controls how iterations are mapped to threads:

| Clause | Behavior | Best when |
|--------|----------|-----------|
| `schedule(static [,chunk])` | Assign contiguous blocks of `chunk` iterations at compile time | Uniform work per iteration |
| `schedule(dynamic [,chunk])` | Threads pull `chunk` iterations from a queue at runtime | Variable / unpredictable work |
| `schedule(guided [,chunk])` | Like dynamic but chunk size shrinks exponentially | Tail-heavy workloads |

```c
#pragma omp parallel for schedule(dynamic, 10)
for (int i = 0; i < N; i++)
    variable_work(i);
```

---

## Reduction Clause

For combining values across threads (sum, product, min, max, etc.):

```c
double ave = 0.0;
#pragma omp parallel for reduction(+:ave)
for (int i = 0; i < MAX; i++)
    ave += A[i];
ave /= MAX;
```

OpenMP automatically:
1. Creates a **private** copy of `ave` per thread, initialized to 0.
2. Each thread accumulates into its private copy.
3. At the end, all copies are **reduced** (summed) into the original `ave`.

No false sharing, no explicit `critical` needed.

### Reduction vs. `critical`

Both safely accumulate into a shared variable, but work very differently:

| | `reduction` | `critical` |
|---|---|---|
| Mechanism | Private copy per thread → merge at end | Mutex lock — one thread at a time |
| Contention | Zero during computation | Serializes all threads at each update |
| Performance | Fast | Slow if called inside inner loop |
| When to use | Simple associative ops (+, *, min, max, &, \|, ^, &&, \|\|) | Complex updates (data structures, conditional multi-variable updates) |

### Reduction Operator Reference

| Operator | Initial value |
|---|---|
| `+` | 0 |
| `*` | 1 |
| `-` | 0 |
| `min` | Largest positive number |
| `max` | Most negative number |
| `&` | `~0` |
| `\|` | 0 |
| `^` | 0 |
| `&&` | 1 |
| `\|\|` | 0 |

---

## MESI Cache Coherence Protocol

Multicore systems must keep per-core caches consistent. Each core's L2 cache line has one of four **MESI** states:

| State | Meaning |
|---|---|
| **M**odified | This core has written; copy is dirty; no other core has a valid copy |
| **E**xclusive | Only this core has the line; matches memory; no other core |
| **S**hared | Multiple cores hold valid (clean) copies |
| **I**nvalid | This core's copy is stale and must be reloaded |

**Example walkthrough (two cores A and B):**

| Step | Action | A's state | B's state |
|---|---|---|---|
| 1 | A reads | Exclusive | — |
| 2 | B reads same line | Shared | Shared |
| 3 | B writes | Invalid | Modified |
| 4 | A reads again | Shared (reloaded) | Shared (flushed) |

Step 4 forces B to flush its dirty line to memory, then A reloads it — the source of false sharing overhead.

---

## Data Environment

### Default Scoping Rules

- **Global variables** (file scope, `static`, `malloc`) → **shared**
- **Local variables declared inside a parallel block** → **private**
- **Stack variables in called functions** → **private**

### Clauses

| Clause | Effect |
|---|---|
| `shared(list)` | All threads access the same storage |
| `private(list)` | Each thread gets a new, **uninitialized** copy; original unchanged after |
| `firstprivate(list)` | Private copy **initialized** from the original variable's value |
| `default(none)` | Compiler error for any variable not explicitly scoped — forces discipline |

```c
// default(none) catches bugs:
#pragma omp parallel for default(none) reduction(*:x)
for (int i = 0; i < N; i++) {
    for (int j = 0; j < 3; j++)    // j must be declared private or will error
        x += foobar(i, j, y);       // y must be declared shared or will error
}
```

### `private` vs. `firstprivate`

```c
int tmp = 42;

// private: tmp inside parallel region is uninitialized — NOT 42
#pragma omp parallel for private(tmp)
for (int j = 0; j < N; j++) tmp += j;   // undefined behavior
printf("%d\n", tmp);  // still 42 — original unchanged

// firstprivate: each thread's tmp starts as 42
#pragma omp parallel for firstprivate(tmp)
for (int j = 0; j < N; j++) tmp += j;
```

---

## `nowait` — Skipping Implied Barriers

Worksharing constructs (`for`, `single`) have an **implicit barrier** at the end. Use `nowait` to skip it when the next work doesn't depend on the current region:

```c
#pragma omp parallel
{
    int id = omp_get_thread_num();
    A[id] = big_calc1(id);
    #pragma omp barrier                    // explicit — A must be fully filled

    #pragma omp for
    for (int i = 0; i < N; i++)
        C[i] = big_calc3(i, A);            // implicit barrier after this loop

    #pragma omp for nowait
    for (int i = 0; i < N; i++)
        B[i] = big_calc2(C, i);            // no barrier — threads proceed immediately

    A[id] = big_calc4(id);
}   // implicit barrier at end of parallel region
```

---

## OpenMP Tasks

Tasks let you parallelize **irregular** control flow that doesn't fit loop worksharing — e.g., linked list traversal, recursive algorithms, dynamic graphs.

### Task Model

- A `task` is a packaged unit of work: code block + its data.
- Any thread can execute any task; execution may be deferred.
- Tasks complete at the next **barrier** (explicit or implicit) or at a `taskwait`.

### Core Constructs

```c
#pragma omp task [clauses]
    structured-block
```

```c
#pragma omp taskwait   // wait for all child tasks of the current task (not descendants)
```

### `single` — One Thread Creates Tasks

```c
#pragma omp parallel
{
    #pragma omp single        // one thread runs this block; others wait at implied barrier
    {
        #pragma omp task
            fred();
        #pragma omp task
            daisy();
        #pragma omp taskwait  // fred() and daisy() must finish before billy()
        #pragma omp task
            billy();
    }
    // all tasks complete before this implicit barrier
}
```

### Task Data Scoping

| Variable | Default in task | Behavior |
|---|---|---|
| Shared in enclosing parallel region | `shared` | Task references original storage |
| Private in enclosing parallel region | `firstprivate` | Task gets a copy initialized at packaging time |
| Declared inside task block | `private` | New uninitialized storage at execution time |

Use `firstprivate` explicitly when the variable may go out of scope before the task runs:

```c
p = listhead;
while (p) {
    #pragma omp task firstprivate(p)   // copy p now — it advances before task runs
        process(p);
    p = p->next;
}
```

### Linked List Traversal (Task-Based)

```c
#pragma omp parallel
{
    #pragma omp single
    {
        struct node *p = listhead;
        while (p) {
            #pragma omp task firstprivate(p)
                process(p);
            p = p->next;
        }
    }
}
```

vs. the array-copy workaround (less natural, requires two passes):

```c
// count items, copy pointers into array, then omp for over the array
#pragma omp parallel
{
    #pragma omp for schedule(static,1)
    for (int i = 0; i < count; i++)
        processwork(parr[i]);
}
```

### Recursive Tasks: Fibonacci

```c
int fib(int n) {
    int x, y;
    if (n < 2) return n;
    #pragma omp task shared(x)    // x is local — must be shared so child writes back
        x = fib(n-1);
    #pragma omp task shared(y)
        y = fib(n-2);
    #pragma omp taskwait
    return x + y;
}

int main() {
    #pragma omp parallel
    {
        #pragma omp single
            fib(5000);
    }
}
```

`x` and `y` must be `shared` on the child tasks so the child's result is visible to the parent's `return x + y` after `taskwait`. If they were `firstprivate`, the parent's `x`/`y` would never be updated.

**Note:** recursive task Fibonacci is $O(2^n)$ — the task tree has $2^n$ leaves. Binet's closed-form formula $F_n = (\varphi^n - \psi^n)/\sqrt{5}$ computes in $O(\log n)$ time.

### Task Guidelines

- Don't use tasks for standard `for` loops — the overhead is higher than `#pragma omp for`.
- Control granularity manually: use a `MIN_BLK` threshold to avoid swamping the scheduler with tiny tasks.
- Best results when the programmer, not the runtime, controls the number and size of tasks.
