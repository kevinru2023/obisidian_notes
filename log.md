# Wiki Log

Append-only chronological record of ingests, queries, and maintenance passes.
Each entry starts with `## [YYYY-MM-DD]` for easy grepping:

## [2026-05-06] course-review | CS434
Concepts covered: ML Framework, kNN, MLE/MAP, Linear Regression, Gradient Descent, Regularization, Logistic Regression, Perceptron, Perceptron Convergence, Evaluating Classifiers, Naïve Bayes, SVM (hard/soft margin), Kernel Methods
Output: wiki/courses/CS434-review.md

## [2026-04-30] query | what does the notation G/H mean again?
Sources used: wiki/concepts/normal-subgroups-quotient-groups.md

## [2026-04-30] ingest | normal subgroups and quotient groups handout.pdf, first iso handout.pdf
Sources: raw-sources/courses/MTH343/normal subgroups and quotient groups handout.pdf, raw-sources/courses/MTH343/first iso handout.pdf
Created: wiki/concepts/normal-subgroups-quotient-groups.md
Updated: wiki/concepts/group-homomorphisms.md (added kernel/image properties, First Isomorphism Theorem, natural projection map), wiki/courses/MTH343.md (added sources, new handouts to table), index.md, log.md

## [2026-04-29] query | Bernoulli Naïve Bayes linear boundary proof — does the proof start by assuming Eq. 3 holds?
Answered from image context; confirmed yes, Eq. 3 (ratio > 1) is the assumption, and the proof derives the linear form by substituting Eqs. 1 & 2, taking log, and collecting terms.

## [2026-04-29] lint | Weekly health check
46 pages scanned. Fixed inline: crdts.md missing H1, naive-bayes.md missing Mitchell link. 6 open items: cross-validation page (medium), MTH254 lectures 14–17 (low), permutation group overlap (low), CS475 L01–04 unindexed (low), CS434 HW2 unindested (low), NLP summaries isolated (low).

## [2026-04-29] ingest | N19-1421.pdf, P19-1472.pdf, 2021.acl-demo.15.pdf, NBayesLogReg.pdf
Sources: raw-sources/pdfs/N19-1421.pdf, raw-sources/pdfs/P19-1472.pdf, raw-sources/pdfs/2021.acl-demo.15.pdf, raw-sources/pdfs/NBayesLogReg.pdf
Created: wiki/summaries/commonsenseqa.md, wiki/summaries/hellaswag.md, wiki/summaries/trafilatura.md, wiki/summaries/mitchell-nb-logreg.md
Updated: wiki/concepts/logistic-regression.md (added NB↔LR relationship section), index.md, log.md

## [2026-04-29] query-render | Bernoulli NB: how θ_{i1}^{x_i}(1-θ_{i1})^{1-x_i} substitution works in equation (1)
Sources: wiki/concepts/naive-bayes.md
Output: /tmp/wiki_render.html

## [2026-04-29] query | Naive Bayes free parameter counting — is 23 correct?
Sources: wiki/concepts/naive-bayes.md. Confirmed approach is correct (prior + sum of conditionals, applying sum-to-1 constraint). Individual feature counts (12, 3, 6) imply k={5,2,3} respectively — unverifiable without the full problem statement.

## [2026-04-29] ingest | How CRDTs Make Multiplayer Text Editing Part of Zed's DNA
Sources: raw-sources/web-clippings/How CRDTs make multiplayer text editing part of Zed's DNA.md
Wiki pages created:
  - wiki/summaries/zed-crdts.md (new)
  - wiki/concepts/crdts.md (new)
Index updated:
  - Added source row for the web clipping
  - Added summary row for zed-crdts.md
  - Added concept row for crdts.md

## [2026-04-27] ingest | Support Vector Machine (Wikipedia web clipping)
Sources: raw-sources/web-clippings/Support vector machine.md
Wiki pages created:
  - wiki/summaries/svm-wikipedia.md (new)
Wiki pages updated:
  - wiki/concepts/svm.md (added kernel trick, nonlinear kernels, ERM/hinge loss view, multiclass SVM, SVR sections; added Wikipedia source)
  - index.md (new source row, new summary row, updated concept description)

## [2026-04-27] lint | Weekly health check
36 wiki pages scanned. 11 prior issues resolved. 2 issues fixed inline (parallel-performance.md typo; svm cross-refs added). 3 open: MTH254 ingest pending, cross-validation concept page missing, permutation-group overlap.

## [2026-04-27] ingest | CS434 L5.1 — Support Vector Machines
Sources: raw-sources/courses/CS434/L5.1 - Support Vector Machines_update.pdf
Wiki pages created:
  - wiki/concepts/svm.md (new)
Wiki pages updated:
  - wiki/courses/CS434.md (added L5.1 lecture entry, SVM algorithm section, source + related links)
  - index.md (new concept row, new source row, updated CS434 course description)

## [2026-04-24] ingest | CS475 GPU Basics — Lectures 07 & 08
Sources: raw-sources/courses/CS475/07_GPU_basics.pdf, raw-sources/courses/CS475/08_GPU_basics_cont.pdf
Wiki pages created:
  - wiki/concepts/gpu-cuda.md (new)
Wiki pages updated:
  - wiki/courses/CS475.md (added lectures 07 & 08 entries, updated sources/related)
  - index.md (added 2 source rows + 1 concept row)

## [2026-04-23] ingest | Symmetric Groups — new concept page from MTH343 handouts 3 & 9
Sources: raw-sources/courses/MTH343/mth 343 handouts_3.pdf, mth 343 handouts_9.pdf
Wiki pages created:
  - wiki/concepts/symmetric-groups.md (new)
Wiki pages updated:
  - wiki/concepts/permutation-groups.md (added cross-reference to symmetric-groups)
  - index.md, log.md

## [2026-04-23] query-render | can you give a quick explanation on what tasks are in OpenMP and how they work?
Sources: [[wiki/concepts/openmp.md]]
Output: /tmp/wiki_render.html

## [2026-04-20] ingest | CS475 Lecture 05 — OpenMP Continued
Sources: raw-sources/courses/CS475/05_OpenMP_cont.pdf → .md
Wiki pages touched:
  - wiki/concepts/openmp.md (added: MESI, data environment, nowait, OpenMP tasks)
  - wiki/courses/CS475.md (added lecture 05 entry)
  - wiki/concepts/parallel-performance.md (new)
  - index.md, log.md

## [2026-04-20] ingest | CS475 Lecture 06 — OpenMP Tasks + Performance Analysis
Sources: raw-sources/courses/CS475/06_OpenMP_task_and_performance.pdf → .md
Wiki pages touched:
  - wiki/concepts/openmp.md (added: reduction vs critical, task guidelines, π task solution)
  - wiki/concepts/parallel-performance.md (speedup, Amdahl's, Gustafson-Barsis, Roofline)
  - wiki/courses/CS475.md (added lecture 06 entry)
  - index.md, log.md

## [2026-04-21] query | CS434 HW2 Recall/Precision clarification
Question: Are the two tables in the recall/precision section different tables for metrics, or different data samples? Also calculate recall/precision for t=0.
Answer: The tables represent 16 different samples (y, P(y|x) pairs). At t=0, all samples are predicted as positive (since all probabilities > 0), yielding Recall=1.0, Precision=0.5.

## [2026-04-20] ingest | A Word on Scalability (web clipping)
Sources: raw-sources/web-clippings/A Word on Scalability.md
Wiki page: wiki/summaries/a-word-on-scalability.md (already existed — tracked in index)
index.md updated

## [2026-04-20] query-render | can you provide me a summary for lecture 03 as well please?
Sources: wiki/concepts/cache-optimization.md, wiki/concepts/openmp.md, wiki/courses/cs475.md
Output: /tmp/wiki_render.html

## [2026-04-20] query-render | can you provide a quick summary of whatever content lecture 04_OpenMP.pdf had?
Sources: wiki/concepts/openmp.md, wiki/courses/cs475.md
Output: /tmp/wiki_render.html

## [2026-04-20] ingest | batch — 4 sources from raw-sources/ (auto-detected via git status)
Sources ingested: L4.1 - Naive Bayes.pdf, perc.converge.pdf, 2302.09207v3.pdf (RETVec), A Word on Scalability.md
Wiki pages already present (prior session, uncommitted): naive-bayes.md, perceptron-convergence.md, regularization.md, a-word-on-scalability.md
Created: raw-sources/pdfs/2302.09207v3.md (PDF extraction), wiki/summaries/retvec.md
Updated: index.md

## [2026-04-20] ingest | L4.1 - Naive Bayes.pdf — CS434 lecture on generative models and Naïve Bayes
Created: raw-sources/courses/cs434/L4.1 - Naive Bayes.md (940 lines, full extraction after token limit increase), wiki/concepts/naive-bayes.md
Updated: wiki/courses/CS434.md, index.md, tools/extract_pdf.py (max_tokens 10000→16000)

## [2026-04-20] ingest | perc.converge.pdf — Collins convergence proof for the perceptron
Created: raw-sources/courses/cs434/perc.converge.md, wiki/concepts/perceptron-convergence.md
Updated: wiki/courses/CS434.md, index.md

## [2026-04-19] query | are the answers to Q7 (logistic regression scaling) and Q8 (SSE/MSE/MAE noise assumptions) correct?
Sources: wiki/concepts/logistic-regression, CS434 L3.1 lecture slides — Q7 wrong (same decision boundary); Q8 Gaussian-for-all checkbox wrong (MAE = Laplace noise)

## [2026-04-19] query | is the answer to "when does σ(w^Tx)=0.5 and what does it imply?" correct?
Sources: wiki/concepts/logistic-regression — answer partially wrong: σ=0.5 means point is ON the boundary (w^Tx=0), not the negative side; hyperplane conclusion is correct

## [2026-04-19] query | is "minimize the negative log likelihood using gradient descent" correct for fitting logistic regression?
Sources: wiki/concepts/logistic-regression — confirmed correct: NLL = cross-entropy, no closed form requires gradient descent

## [2026-04-19] query | can you explain what regularization is?
Sources: wiki/concepts/mle-map, sources/courses/cs434/l3-1-multidimension-linear-regression-basis-functions-and-regularization

## [2026-04-19] query | Is KNN an exemplar classifier?
Answered yes — CS434 lecture slides explicitly list KNN's model family as "Exemplar Methods / Instance-based Learning / Non-Parametric." Source: `sources/courses/cs434/l1-2-knn.md`.

## [2026-04-19] render | kNN query answer with LaTeX math
Output: /tmp/wiki_render.html
Query: What type of algorithm is kNN? Is it linear regression without probabilistic interpretation?

## [2026-04-19] query | What type of algorithm is kNN? Is it linear regression without probabilistic interpretation?
Sources: wiki/concepts/knn, raw-sources/courses/CS434/L1.2 - kNN.pdf

## [2026-04-18] ingest | A Word on Scalability
Source: raw-sources/web-clippings/A Word on Scalability.md
Created: wiki/summaries/a-word-on-scalability.md
Updated: index.md, log.md
qmd: 2 new docs indexed, 3 chunks embedded

## [2026-04-17] query | Rundown of symmetric groups and homomorphisms/isomorphisms
Sources: wiki/concepts/permutation-groups, wiki/concepts/group-homomorphisms, wiki/concepts/groups, wiki/courses/mth343

## [2026-04-17] render | Symmetric groups, homomorphisms & isomorphisms
Output: /tmp/wiki_render.html
Query: Rundown of symmetric groups and homomorphisms/isomorphisms

```bash
# Last 5 entries
grep "^## \[" log.md | tail -5

# All ingests
grep "^## \[.*\] ingest" log.md

# All queries
grep "^## \[.*\] query" log.md
```

---

## [2026-04-16] ingest | MTH343 Handouts 1–9

Ingested 9 course handouts scanned from MTH343 (Abstract Algebra). PDFs extracted to markdown via `tools/extract_pdf.py`.

**Sources added:**
- `raw-sources/courses/MTH343/mth 343 handouts_1.md` — Group Homomorphisms & Isomorphisms
- `raw-sources/courses/MTH343/mth 343 handouts_2.md` — Cosets & Lagrange's Theorem
- `raw-sources/courses/MTH343/mth 343 handouts_3.md` — Symmetric & Permutation Groups
- `raw-sources/courses/MTH343/mth 343 handouts_4.md` — Cyclic Groups
- `raw-sources/courses/MTH343/mth 343 handouts_5.md` — Subgroups
- `raw-sources/courses/MTH343/mth 343 handouts_6.md` — Groups (binary ops, G1/G2/G3 axioms)
- `raw-sources/courses/MTH343/mth 343 handouts_7.md` — Dihedral Groups ($D_4$ example)
- `raw-sources/courses/MTH343/mth 343 handouts_8.md` — Properties of $D_4$ & general $D_n$ definition
- `raw-sources/courses/MTH343/mth 343 handouts_9.md` — Important Group Examples

**Wiki pages created:**
- `wiki/concepts/group-homomorphisms.md` — new concept page
- `wiki/concepts/cyclic-groups.md` — new concept page
- `wiki/concepts/subgroups.md` — new concept page
- `wiki/concepts/dihedral-groups.md` — new concept page (covers handouts 7, 8, 9)

**Wiki pages updated:**
- `wiki/courses/MTH343.md` — added all 9 handout sources, new related links, handout summary table
- `wiki/concepts/groups.md` — added formal G1/G2/G3 axiom labels, 6 basic group facts, $SL_n$ example
- `wiki/concepts/cosets.md` — added $L_a$/$R_a$ map formulation, 7 coset properties list
- `wiki/concepts/permutation-groups.md` — added 7 key $S_n$ facts, right-to-left composition convention, $S_6$ example

---

## [2026-04-15] setup | Initial wiki structure created

Migrated existing vault to the LLM wiki pattern. Established directory structure:
- `raw-sources/` — immutable external sources
- `wiki/` — Claude-maintained synthesis layer
- `notes/` — Kevin's personal notes

Migrated content:
- `notes/cpp/` ← C++ Notes (5 files)
- `notes/courses/CS162/` ← CS162 (6 files)
- `notes/cybersec/` ← Cybersec (11 files + writeups)
- `notes/DSA/` ← DSA (7 files + 13 leetcode notes)
- `notes/courses/MTH254/` ← MTH254 (14 files)
- `notes/courses/ML/` ← Intro to ML notes
- `notes/books/` ← book notes (4 files)
- `notes/personal/` ← Random (2 files)
- `raw-sources/web-clippings/` ← Clippings (2 files)
- `raw-sources/pdfs/` ← pdfs (2 PDFs)
- `raw-sources/courses/MTH254/` ← vector calc PDFs (5 files)

Tools created: `tools/extract_pdf.py`, `tools/ingest.sh`

## [2026-04-16] ingest | Judson — Abstract Algebra: Theory and Applications (MTH343)

Source: `raw-sources/courses/MTH343/Judson12.pdf` / `Judson12.md` (1.2 MB, 20,533 lines)

Thomas W. Judson's open-source undergraduate abstract algebra textbook (2012 ed). 23 chapters covering groups, rings, fields, and Galois theory, with applications to cryptography and error-correcting codes.

Files created:
- `wiki/summaries/judson-abstract-algebra.md` — full textbook summary with chapter map and key theorems
- `wiki/courses/MTH343.md` — MTH343 course page with definitions, theorem table, study path
- `wiki/concepts/groups.md` — comprehensive groups concept page (axioms through Sylow theorems)
- `wiki/concepts/rings.md` — rings hierarchy, ideals, polynomial rings, UFD/PID chain
- `wiki/concepts/fields.md` — extensions, splitting fields, finite fields, Galois theory overview

Index and log updated.

## [2026-04-16] ingest | CS434 Machine Learning & Data Mining — Lecture Slides + CIML Chapters

Sources extracted (10 PDFs → markdown via tools/extract_pdf.py):
- `L1.2 - kNN.pdf` — kNN, model selection, curse of dimensionality, cross-validation
- `L2.1 - Prob.,MLE, and MAP copy 2.pdf` — MLE, MAP, Bayesian learning
- `L2.2 - Linear Algebra and Linear Regression.pdf` — linear regression, SSE, closed-form
- `L3.1 - Multidimension Linear Regression, Basis Functions and Regularization.pdf` — vectorized regression, basis functions, ridge regularization
- `L3.2 - Logistic regresson, Perceptron and Evaluating Classifiers.pdf` — logistic regression, perceptron, precision/recall
- `ciml-v0_99-ch04.pdf` — CIML Ch. 4: Perceptron (bio-inspiration, hyperplane classifier, margin)
- `ciml-v0_99-ch05.pdf` — CIML Ch. 5: Practical Issues (feature engineering, cross-validation, debugging)
- `CS434_HW0_W24.pdf`, `CS434_HW1_S25.pdf`, `CS434_HW2_S25.pdf` — homeworks (kNN implementation, Poisson MLE)

Files created:
- `wiki/courses/CS434.md` — course overview with lecture map, algorithm summaries, model selection
- `wiki/concepts/knn.md` — kNN: algorithm, distance metrics, curse of dimensionality, pros/cons
- `wiki/concepts/mle-map.md` — MLE/MAP: statistical learning, connection to regularization
- `wiki/concepts/logistic-regression.md` — logistic regression, perceptron, classifier evaluation metrics

Index and log updated.

## [2026-04-16] ingest | CS475 Lecture 02 — Cache-Based Optimizations

Source: `raw-sources/courses/CS475/02_Cache.pdf`
Extracted to: `raw-sources/courses/CS475/02_Cache.md`

Pages created:
- `wiki/courses/CS475.md` — CS475 course page (new): HPC cluster setup, SLURM, lecture index
- `wiki/concepts/cache-optimization.md` — Cache concept page (new): memory hierarchy, locality, miss rates, register reuse, loop ordering analysis, blocked matrix multiplication, roofline model

Index updated with 2 new rows.

## [2026-04-16] ingest | MTH254 — Vector Calculus I Week 6 Lecture (Double Integrals)

Source: `raw-sources/courses/MTH254/Vector Calculus I Week 6 Lecture.pdf`
Extracted to: `raw-sources/courses/MTH254/Vector Calculus I Week 6 Lecture.md`

Topics: double integrals as Riemann sum limits, Fubini's theorem (rectangular and general regions), Type I/II region setup, switching order of integration.

Files created:
- `wiki/courses/MTH254.md` — new MTH254 course page with lecture index and key theorems
- `wiki/concepts/double-integrals.md` — double integrals concept page

Index updated with 2 new rows.

## [2026-04-16] ingest | CS434 Materials and References (Canvas web clipping)

Source: `raw-sources/web-clippings/Materials and References...CS434.md`

Canvas page listing optional textbooks (CIML, PRML, Math for ML) and supplementary math/Python resources for CS434 S2026.

Files created/modified:
- `wiki/summaries/cs434-resources.md` — summary with quick links
- `wiki/courses/CS434.md` — added Resources & References section

Index updated with 1 new row.

## [2026-04-16] ingest | CS475 Lecture 01 — Introduction to Parallel Programming

Source: `raw-sources/courses/CS475/01_Introduction.pdf`
Extracted to: `raw-sources/courses/CS475/01_Introduction.md`

Topics: why parallelism (clock speed plateau, compute demand trends), data vs. task parallelism, Flynn's taxonomy (SISD/SIMD/MIMD), shared vs. distributed memory architectures, Summit supercomputer node layout, AlphaGo GPU scaling.

Files created/modified:
- `wiki/concepts/parallel-programming-fundamentals.md` — new concept page
- `wiki/courses/CS475.md` — added full schedule, resources, Lecture 01 entry

Index updated with 1 new row; CS475 course page description updated.

## [2026-04-16] ingest | CS475 Lecture 03 — Cache Continued & OpenMP Basics

Source: `raw-sources/courses/CS475/03_Cache_cont_and_OpenMP.pdf`
Extracted to: `raw-sources/courses/CS475/03_Cache_cont_and_OpenMP.md`

Topics: full loop-order miss analysis with step-by-step ijk/kij/jki examples, timing calculations with/without cache (quiz problems), blocked vs non-blocked miss count formulas; OpenMP — fork-join model, shared/private variables, pragma syntax, Pthreads/OpenMP/TBB comparison.

Files created/modified:
- `wiki/concepts/openmp.md` — new OpenMP concept page
- `wiki/concepts/cache-optimization.md` — added performance calculation examples section
- `wiki/courses/CS475.md` — added Lecture 03 entry and openmp relation

Index updated with 1 new row; cache-optimization description updated.

## [2026-04-16] ingest | CS475 Lecture 04 — OpenMP Basics (continued)

Source: `raw-sources/courses/CS475/04_OpenMP.pdf`
Extracted to: `raw-sources/courses/CS475/04_OpenMP.md`

Topics: race conditions and deadlocks, OpenMP common core table (20+ pragmas/functions/clauses), thread creation and ICV precedence, π SPMD parallelization walkthrough with false sharing diagnosis and three fixes (padding, private scalar + critical, reduction), synchronization (critical/barrier), parallel loops (#pragma omp for), schedule clauses (static/dynamic/guided), loop-carried dependency removal, reduction clause.

Files created/modified:
- `wiki/concepts/openmp.md` — major expansion: common core table, π example, false sharing, sync, parallel loops, schedule, reduction
- `wiki/courses/CS475.md` — added Lecture 04 entry

Index updated (openmp description updated, no new pages).

## [2026-04-16] lint | LaTeX formatting pass — all wiki pages

Scanned all 16 wiki pages for unformatted mathematical expressions. Pages ingested before the LaTeX standard was established used Unicode symbols (⁻¹, ∃, ≅, Σ, φ, etc.) and plain-text formulas instead of `$...$` / `$$...$$`.

Full rewrites (heavy math content):
- `wiki/concepts/groups.md` — group axioms, cosets, isomorphism theorems, Sylow, Burnside, class equation
- `wiki/concepts/rings.md` — ring axioms, ideals, polynomial division, factorization hierarchy
- `wiki/concepts/fields.md` — extensions, splitting fields, finite fields, Galois theory
- `wiki/concepts/knn.md` — distance metrics, classification/regression formulas, curse of dimensionality
- `wiki/concepts/mle-map.md` — MLE/MAP argmax expressions, prior table, Bayes' rule
- `wiki/concepts/logistic-regression.md` — sigmoid, cross-entropy loss, gradient, perceptron convergence, evaluation metrics

Targeted edits (lighter math):
- `wiki/courses/MTH343.md` — theorem table, key definitions
- `wiki/courses/CS434.md` — SSE formula, evaluation metrics, core ML framework
- `wiki/summaries/judson-abstract-algebra.md` — φ(n), GF(2^8), isomorphism theorem

No changes needed (already fully LaTeX):
- `wiki/concepts/cache-optimization.md`, `wiki/concepts/double-integrals.md`, `wiki/concepts/openmp.md`, `wiki/concepts/parallel-programming-fundamentals.md`, `wiki/courses/CS475.md`, `wiki/courses/MTH254.md`, `wiki/summaries/cs434-resources.md`

## [2026-04-16] query | CS434 — showing Gamma is a conjugate prior to the Poisson distribution

Source used: `wiki/concepts/mle-map.md`, `wiki/courses/CS434.md`

## [2026-04-16] ingest | Cosets in Group Theory — YouTube lecture (Abstract Algebra)

Source: `raw-sources/web-clippings/Cosets in Group Theory  Abstract Algebra.md`
YouTube: https://www.youtube.com/watch?v=kthl-MhIf4s — Wrath of Math

Covers left/right coset definitions, finite ($\mathbb{Z}_4$) and infinite ($\mathbb{R}/\mathbb{Z}$) examples, the partition property, and a full proof that overlapping cosets are equal. Teases Lagrange's theorem.

Files created:
- `wiki/concepts/cosets.md` — concept page: definitions, worked examples, equal-or-disjoint proof, Lagrange's theorem, normal subgroups connection
- `wiki/summaries/cosets-video.md` — video summary with proof sketch

Files modified:
- `wiki/concepts/groups.md` — added `cosets` to related links
- `wiki/courses/MTH343.md` — added `cosets` to related links

Index updated with 2 new rows.

## [2026-04-16] ingest | Permutation Groups and Symmetric Groups — YouTube lecture (Abstract Algebra)

Source: `raw-sources/web-clippings/Permutation Groups and Symmetric Groups  Abstract Algebra.md`
YouTube: https://www.youtube.com/watch?v=NwqCi63p2ik

Abstract algebra lecture covering permutations as bijections, group axioms for permutation composition, symmetric group notation ($S_A$, $S_n$), and a full worked example with $S_3$ (6 elements, composition table, inverse computation).

Files created:
- `wiki/summaries/permutation-groups-video.md` — video summary with $S_3$ table and key points
- `wiki/concepts/permutation-groups.md` — concept page: two-row notation, cycle notation, even/odd permutations, $S_3$ reference table, Cayley's theorem

Files modified:
- `wiki/concepts/groups.md` — added `permutation-groups` to related links
- `wiki/courses/MTH343.md` — added `permutation-groups` to related links

Index updated with 2 new rows.

## [2026-04-16] query | how does cache optimization work? Why does index order matter?

Source used: `wiki/concepts/cache-optimization.md`
Topics covered: memory hierarchy, locality, C row-major layout, loop ordering miss rate analysis (ijk vs kij vs jki), register reuse, blocked matmul.

## [2026-04-16] setup | qmd vector search wired up

MCP server registered in `.mcp.json` (`qmd mcp`). Three collections indexed: `notes` (64), `wiki` (20), `sources` (20) — 104 docs / 1203 embedded chunks. Contexts added per collection. Embedding model: `embeddinggemma-300M-Q8_0` (328 MB). Prior session crashed mid-sanity-check when the 1.28 GB query-expansion model (`qmd-query-expansion-1.7B-q4_k_m`) was downloading concurrently with active inference — both models are now resident on disk so re-runs won't repeat that burst. Verified: `qmd search`, `qmd vsearch`, and the `mcp__qmd__*` tools all return expected results.

## [2026-04-16] query | what is the subgroup criterion and what chapter can I find in my judson textbook?

Sources used: `wiki/concepts/groups.md`, `sources/courses/mth343/judson12.md` (TOC). Answer: Judson Chapter 3, §3.3 "Subgroups", p. 49.

## [2026-04-17] query | How is \mathbb{Z}/20\mathbb{Z}^x defined?
Sources: wiki/concepts/groups.md, sources/courses/mth343/judson12.md — group of units U(n) definition

## [2026-04-17] query | What is (Z/24Z)^x?
Sources: wiki/concepts/groups.md (prior context from Z/20Z query) — no new search needed

## [2026-04-21] lint | Weekly health check
Scanned all 29 wiki pages. 11 issues found across 5 categories.
Report written to: wiki/lint-report.md
Top issues:
  - CONTRADICTION: CS475 midterm date (April 30 in grading section vs May 5 in schedule)
  - BROKEN LINK: a-word-on-scalability.md → [[wiki/concepts/distributed-systems]] (page doesn't exist)
  - STALE DATE: cache-optimization.md updated date should be 2026-04-20, not 2026-04-16
  - DUPLICATE CONTENT: classifier evaluation metrics in both logistic-regression.md and naive-bayes.md
  - DUPLICATE CONTENT: Roofline stub in cache-optimization.md vs full treatment in parallel-performance.md
  - MISSING PAGES: wiki/concepts/linear-regression.md, wiki/concepts/gradient-descent.md
  - INDEX BUGS: 2× lowercase cs434 paths, 1× duplicate "A Word on Scalability" entry
  - CS475 Lecture 01 missing from Lecture Topics section; topics listed out of order

## [2026-04-21] query | Why do we need parallel programming? (CS475 Q1 answer check)
Sources: sources/courses/cs475/01-introduction.md, wiki/concepts/parallel-programming-fundamentals.md. Confirmed: CPU frequency stagnating ✓, more cores = energy-efficient ✓, shared-memory simpler than serial ✗ (incorrect — parallel adds synchronization complexity).

## [2026-04-21] query | True/False: Same algorithm can have different runtime based on implementation
Sources: wiki/concepts/cache-optimization.md. Confirmed TRUE — loop ordering in matrix multiplication causes 4× miss rate difference; blocking gives 5B/2 speedup.

## [2026-04-21] query | Cache miss rate analysis (stride patterns)
Analyzed cache miss rates for backward iteration vs stride-2 access. Used concepts from CS475 cache materials to calculate: (1) backward loop = 12.5% miss rate (stride-1 spatial locality); (2) stride-2 loop = 25% miss rate (half elements accessed per cache line). Sources: [[wiki/concepts/cache-optimization]], [[sources/courses/cs475/02-cache.md]]

## [2026-04-22] render | Naïve Bayes parameter count explanation
Output: /tmp/wiki_render.html
Query: why does the naive bayes assumption reduce the parameter count to be linear?

## [2026-04-22] query | why does the naive bayes assumption reduce the parameter count to be linear?
Sources: wiki/concepts/naive-bayes.md — joint distribution O(c×m^d) vs factored O(c×d×m); conditional independence explanation.

## [2026-04-22] ingest | CS434 L4.1&2 — Naïve Bayes cont.
Sources: raw-sources/courses/CS434/L4.1&2 - Naive Bayes.pdf → .md (extracted)
Wiki pages updated:
  - wiki/concepts/naive-bayes.md (added: worked Laplace smoothing example with car theft data, categorical/Gaussian in-class examples, updated sources + date)
  - wiki/courses/CS434.md (added: L4.1&2 to sources list, L4.2 row in lecture map)
  - index.md (added: L4.1&2 source row; updated naive-bayes concept row date)
qmd: 1 new source indexed, 9 docs re-embedded

## [2026-04-24] lint-fix | Applied all lint fixes
Fixed 9 issues: deleted empty wiki/concepts/concepts.md; fixed broken source .md extension in a-word-on-scalability; moved 3 source rows to correct index section; capitalized cs434→CS434 in 3 concept page related blocks; back-filled related links in logistic-regression, mle-map, CS434, MTH343, permutation-groups; bumped updated dates on logistic-regression, MTH343, permutation-groups. Carry-forward: MTH254 Lectures 14-17 (pending ingest), content overlap in permutation/symmetric-groups (deferred).

## [2026-04-24] lint | Weekly health check
35 pages scanned. 9/11 previous issues resolved. 10 new issues found.
Top issues: empty orphan file (wiki/concepts/concepts.md), 3 source rows misplaced in index.md, lowercase CS434 links in 3 concept pages, 5 missing related-link back-fills (logistic-regression, mle-map, CS434, MTH343, permutation-groups).
Full report: wiki/lint-report.md

## [2026-04-24] query | Is GL_2(R) an abelian group?
Sources: wiki/concepts/groups.md, sources/courses/mth343/judson12.md — No; matrix multiplication is noncommutative (AB ≠ BA in general), so GL_n(R) is nonabelian for n ≥ 2.

## [2026-04-21] query | CS475 cache miss counting — 2D array with 3 cache lines and LRU policy
Question: Calculate cache misses for three access patterns on a[8][8] with 4 doubles per cache line, 3 total cache lines, LRU replacement. Sources: [[wiki/concepts/cache-optimization]], [[sources/courses/cs475/02-cache.md]] — covered: spatial locality, row-major array layout, cache line granularity, types of misses, LRU policy, stride-1 vs column-wise access patterns.

## [2026-04-25] query | Amdahl's Law — max speedup with 95% parallelizable code on 10 processors
Sources: [[wiki/concepts/parallel-performance]] — Amdahl's Law gives ψ ≤ 1/(0.05 + 0.95/10) ≈ 6.90×.

## [2026-04-25] query | Shauna's problem (Q4) equation check — corrected to 9 = 1/(f + (1-f)/10); f ≈ 1.23%
Sources: [[wiki/concepts/parallel-performance]] — user had f in numerator; corrected to 1.

## [2026-04-25] query | Q2 Amdahl's Law equation check — 1/(0.06 + 0.94/x) = 10
Sources: [[wiki/concepts/parallel-performance]] — equation correct; solving gives x = 23.5, so min 24 processors.

## [2026-04-25] query-render | Parallel performance questions — wiki pointer guide (Q2–Q6)
Sources: [[wiki/concepts/parallel-performance]] — Amdahl's Law (Q2, Q3, Q4) and Gustafson-Barsis (Q5, Q6)
Output: /tmp/wiki_render.html

## [2026-04-26] query | Why shuffle examples each epoch in perceptron learning?
Sources: [[sources/courses/cs434/l3-2-logistic-regresson-perceptron-and-evaluating-classifiers.md]] — slides 44, 47 on ordering sensitivity and convergence
## [2026-04-26] query | Rare disease classifier: which statements are correct (precision/recall/accuracy)
Sources: [[wiki/concepts/logistic-regression]] — precision/recall/accuracy definitions and rare-disease accuracy pitfall

## [2026-04-26] query | Naive Bayes parameter count: K-class, d categorical features, n values each
Sources: [[wiki/concepts/naive-bayes]] — correct answer is K×(n×d−d)+K−1; selected answer K×n×d+K−1 was wrong (ignores n−1 hint)
## [2026-04-28] query | OpenMP race condition — possible values of sum with 2 threads, each running for(i=0;i<50;i++) sum+=1
Sources used: wiki/concepts/openmp.md (Race Conditions section). Answer: 2 and 98 are possible (not 102, which exceeds the max of 100; not 0, which is impossible since only increments occur).
## [2026-04-28] query | OpenMP thread interleaving — possible printf outputs with 2 threads (Hello/World)
Sources used: wiki/concepts/openmp.md (fork-join model, shared vs private). Answer: HelloWorldHelloWorld and HelloHelloWorldWorld are possible; HelloWorldWorldHello and WorldHelloHelloWorld violate intra-thread ordering.
## [2026-04-28] query | OpenMP omp_get_thread_num / omp_get_num_threads outside vs inside parallel region
Sources used: wiki/concepts/openmp.md (loaded in session). Answer: first printf prints '0 1' (serial region, 1 thread), second prints '0 4' (thread 0 inside 4-thread parallel region). Total output: '0 1 0 4'.
## [2026-04-28] query | OpenMP false sharing — which 2D array access pattern avoids false sharing (4 doubles/cache line, 4 threads)
Sources used: wiki/concepts/openmp.md (False Sharing section, loaded in session). Answer: B, C, and D all avoid false sharing; A puts all threads in the same cache line.
## [2026-04-28] query | OpenMP schedule(static) — output when thread 1 prints its iterations (10 iters, 2 threads)
Sources used: wiki/concepts/openmp.md (Schedule clause section). Answer: 5 6 7 8 9. schedule(static) gives contiguous blocks; round-robin only with schedule(static,1).
## [2026-04-28] query | OpenMP static vs dynamic schedule — why schedule(static) is best for sum += 2^i (1000 iterations)
Sources used: wiki/concepts/openmp.md (Schedule clause section). Key point: uniform work per iteration → static; dynamic only needed for non-uniform/unpredictable work.
## [2026-04-28] query | OpenMP bug identification — race condition on sum, uninitialized sum, type mismatch (int vs float)
Sources used: wiki/concepts/openmp.md (Race Conditions section). False sharing was incorrectly identified — actual bugs are race condition on shared scalar, uninitialized variable, and int/float type mismatch.
## [2026-04-28] query | OpenMP loop-carried dependency bug — c[i]=b[i]+b[i-1] in parallel for, plus b[-1] out-of-bounds
Sources used: wiki/concepts/openmp.md (Loop-carried dependencies section). Not a deadlock; fix is two separate parallel for loops with implicit barrier between them.
## [2026-04-28] query | OpenMP shared loop variable bug — j declared outside parallel region causes race condition in nested for loop
Sources used: wiki/concepts/openmp.md (Data Environment / default scoping rules). False sharing was not the bug; reduction handles sum correctly; j must be declared inside or made private.
## [2026-04-28] query | OpenMP private/firstprivate/shared scoping — initial values of A, B, C with private(A) firstprivate(B)
Sources used: wiki/concepts/openmp.md (Data Environment / Clauses section). A=private/undef, B=firstprivate/2, C=shared/3. User had A's scope wrong (said shared).
## [2026-04-28] ingest | Naive Bayes Classifier (Wikipedia web clipping)
Files touched: raw-sources/web-clippings/Naive Bayes classifier.md (source), wiki/summaries/naive-bayes-classifier-wikipedia.md (created), wiki/concepts/naive-bayes.md (updated — added Multinomial NB, Bernoulli vs Multinomial, relation to logistic regression, why NB works, semi-supervised EM), index.md (2 new rows), log.md.

## [2026-04-28] ingest | Bayes' Theorem (Wikipedia web clipping)
Files touched: raw-sources/web-clippings/Bayes' theorem.md (source), wiki/summaries/bayes-theorem-wikipedia.md (created), wiki/concepts/bayes-theorem.md (created), wiki/concepts/naive-bayes.md (added related link), index.md (3 new rows), log.md.

## [2026-04-28] query | OpenMP task data scoping — firstprivate capture of b in tasks, private(b) doesn't write back after parallel region
Sources used: wiki/concepts/openmp.md (Task Data Scoping section). Output: task T0 prints b=0, task T1 prints b=1, final serial printf prints b=2 (original unchanged).

## [2026-05-03] query | True/False: GPU resident threads can be much higher than concurrently executing threads
Sources used: wiki/concepts/gpu-cuda.md, sources/courses/cs475/07-gpu-basics.md, sources/courses/cs475/08-gpu-basics-cont.md. Answer: TRUE — resident threads are all threads loaded on SMs with live register state; only one warp per warp scheduler issues per clock cycle. On Kepler K20: 28,672 resident vs ~448 executing. Mechanism is latency hiding.

## [2026-05-04] ingest | CS434 L6.1 — Kernel Functions
Sources: raw-sources/courses/CS434/L6.1 - kernel functions.pdf → .md (extracted)
Wiki pages created:
  - wiki/concepts/kernel-methods.md (new) — basis functions, kernel trick, Mercer's theorem, closure properties, common kernels, kernel SVM, kernelized perceptron, kernel ridge regression
Wiki pages updated:
  - wiki/courses/CS434.md (added L6.1 lecture row, Kernel Methods algorithm section, source + related links)
  - wiki/concepts/svm.md (added kernel-methods to related links)
  - index.md (added source row for L6.1, new concept row for kernel-methods, updated CS434 description)
qmd: 1 new wiki doc + 1 new source indexed, 4 total chunks embedded

## [2026-05-03] query-render | 65536x1x1 grid, 512x1x1 block vector addition — thread count and task assignment
Sources: wiki/concepts/gpu-cuda.md, sources/courses/cs475/08-gpu-basics-cont.md
Output: /tmp/wiki_render.html

## [2026-05-03] query | model answer for 65536x1x1 grid 512x1x1 block vector addition thread count and task assignment
Sources: wiki/concepts/gpu-cuda.md (thread hierarchy, stride loop), sources/courses/cs475/08-gpu-basics-cont.md (vecAdd kernel). Answer: 33,554,432 threads; thread_index = threadIdx.x + 512*blockIdx.x; each thread handles one element; stride loop for n > 2^25.

## [2026-05-05] query-render | can you explain a bit more about Memory Coalescing and how that utilization table was calculated?
Sources: wiki/concepts/gpu-cuda.md
Output: /tmp/wiki_render.html

## [2026-05-05] query-render | if I were looking at a loop order how would I determine the amount of cache misses?
Sources: wiki/concepts/cache-optimization.md
Output: /tmp/wiki_render.html

## [2026-05-05] render | T_m formula breakdown — three terms and their roles
Output: /tmp/wiki_render.html
Query: T_m formula clarification for dgemm performance calculation

## [2026-05-05] render | dgemm performance calculation — T_m and T_c worked example
Output: /tmp/wiki_render.html
Query: dgemm performance calculation pattern with n=1000

## [2026-05-05] course-review | CS475
Concepts covered: Parallel Programming Fundamentals, Cache-Based Optimizations, OpenMP (fork-join, false sharing, MESI, reduction, tasks), Parallel Performance (Amdahl, Gustafson-Barsis, Roofline), GPU Architecture and CUDA (thread hierarchy, warps, memory hierarchy, coalescing, shared memory, parallel reduction)
Output: wiki/courses/CS475-review.md

## [2026-10-31] ingest | CS331 Lecture 8 — Adversarial Search
Source: raw-sources/Lecture8_Adversarial_Search.pdf (43 slides; new course CS331 — Intro to AI)
Extraction: docling not installed → slides read directly; transcription written to raw-sources/Lecture8_Adversarial_Search.md
Created: wiki/courses/CS331.md, wiki/concepts/adversarial-search.md, wiki/concepts/alpha-beta-pruning.md
Updated: index.md (3 wiki rows + 1 source row), log.md
Notes: worked all in-class exercises (answers: 8, 36, 3, 8 [prune-impossible if e > 8], 7 via A→D→K→Y). qmd re-index skipped — qmd not on PATH.
