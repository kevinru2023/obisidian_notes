# Wiki Index

Content catalog for Kevin's personal wiki. Updated on every ingest.
Claude reads this first when answering queries to find relevant pages.

Format: `| [Title](path) | category | description | date |`
Categories: `summary`, `concept`, `course`, `reference`, `note`, `personal`

---

## Notes

| Title | Category | Description | Date |
|---|---|---|---|
| [CS162 Notes](notes/courses/CS162/CS162.md) | note | CS162 course overview and index | — |
| [MTH254 Notes](notes/courses/MTH254/MTH254.md) | note | Multivariable calculus course notes | — |
| [DSA Notes](notes/DSA/DSA.md) | note | Data structures and algorithms overview | — |
| [Cybersec Notes](notes/cybersec/Cybersec.md) | note | Cybersecurity reference index | — |
| [C++ Notes](notes/cpp/C++%20Notes.md) | note | C++ language reference notes | — |
| [Book Notes Index](notes/books/book%20notes.md) | note | Index of book notes | — |
| [Linear Regression](notes/courses/ML/Linear%20Regression.md) | note | ML linear regression notes | — |

## Wiki (Claude-maintained)

| Title | Category | Description | Date |
|---|---|---|---|
| [Judson Abstract Algebra](wiki/summaries/judson-abstract-algebra.md) | summary | Full textbook summary — groups, rings, fields, Galois theory (MTH343) | 2026-04-16 |
| [MTH343 Course Page](wiki/courses/MTH343.md) | course | Abstract Algebra course map, key definitions, theorem reference | 2026-04-16 |
| [Groups](wiki/concepts/groups.md) | concept | Group axioms, subgroups, cosets, Lagrange, homomorphisms, Sylow theorems | 2026-04-16 |
| [Rings](wiki/concepts/rings.md) | concept | Ring hierarchy, ideals, quotient rings, polynomial rings, UFD/PID | 2026-04-16 |
| [Fields](wiki/concepts/fields.md) | concept | Field extensions, splitting fields, finite fields, Galois theory overview | 2026-04-16 |
| [MTH254 Course Page](wiki/courses/MTH254.md) | course | Vector Calculus I — double integrals, Fubini's theorem, general regions | 2026-04-16 |
| [Double Integrals](wiki/concepts/double-integrals.md) | concept | Riemann sums in 2D, Fubini's theorem, Type I/II regions, switching integration order | 2026-04-16 |
| [CS434 Resources](wiki/summaries/cs434-resources.md) | summary | CS434 optional textbooks and supplementary links (CIML, PRML, Math4ML, Matrix Cookbook) | 2026-04-16 |
| [CS434 Course Page](wiki/courses/CS434.md) | course | ML & Data Mining — kNN, MLE/MAP, linear/logistic regression, perceptron, Naïve Bayes, SVM, kernel methods | 2026-05-04 |
| [CS434 Review](wiki/courses/CS434-review.md) | reference | Comprehensive exam review — all CS434 concepts with formulas, intuition, gotchas, and practice questions | 2026-05-06 |
| [k-Nearest Neighbors](wiki/concepts/knn.md) | concept | kNN algorithm, distance metrics, curse of dimensionality, model selection | 2026-04-16 |
| [MLE and MAP](wiki/concepts/mle-map.md) | concept | Maximum likelihood estimation, MAP with priors, connection to regularization | 2026-04-16 |
| [Logistic Regression & Perceptron](wiki/concepts/logistic-regression.md) | concept | Sigmoid, cross-entropy loss, perceptron update rule, classifier evaluation metrics | 2026-04-16 |
| [Regularization](wiki/concepts/regularization.md) | concept | L2/Ridge and L1/Lasso regularization, overfitting, Bayesian interpretation, bias-variance tradeoff | 2026-04-19 |
| [Linear Regression](wiki/concepts/linear-regression.md) | concept | Least-squares objective, closed-form solution, basis functions, MLE justification, ridge/lasso | 2026-04-21 |
| [Gradient Descent](wiki/concepts/gradient-descent.md) | concept | Iterative loss minimization, batch/SGD/mini-batch variants, learning rate, convexity guarantee | 2026-04-21 |
| [Perceptron Convergence Theorem](wiki/concepts/perceptron-convergence.md) | concept | Convergence proof: perceptron makes at most R²/γ² mistakes when data is linearly separable | 2026-04-20 |
| [Naïve Bayes](wiki/concepts/naive-bayes.md) | concept | Generative classifier using conditional independence; Bernoulli/Categorical/Gaussian variants; generative vs discriminative | 2026-04-22 |
| [Support Vector Machines](wiki/concepts/svm.md) | concept | Max-margin linear classifier; hard-margin and soft-margin SVM; slack variables; dual formulation; kernel trick; SVR | 2026-05-04 |
| [Kernel Methods](wiki/concepts/kernel-methods.md) | concept | Basis functions, kernel trick, Mercer's theorem, closure properties, common kernels, kernel SVM/perceptron/ridge regression | 2026-05-04 |
| [SVM Wikipedia Summary](wiki/summaries/svm-wikipedia.md) | summary | Wikipedia SVM article — kernel trick, common kernels, ERM/hinge loss, multiclass SVM, SVR, implementation algorithms | 2026-04-27 |
| [CS475 Course Page](wiki/courses/CS475.md) | course | Intro to Parallel Programming — OpenMP, CUDA, MPI; cache, architecture, cluster setup | 2026-04-24 |
| [Parallel Programming Fundamentals](wiki/concepts/parallel-programming-fundamentals.md) | concept | Why parallelism, data/task parallelism, Flynn's taxonomy, shared/distributed memory, supercomputers | 2026-04-16 |
| [Cache-Based Optimizations](wiki/concepts/cache-optimization.md) | concept | Memory hierarchy, locality, miss rates, register reuse, loop ordering, blocked matmul, timing calculations | 2026-04-16 |
| [OpenMP](wiki/concepts/openmp.md) | concept | Fork-join, thread functions, false sharing, MESI, data environment, nowait, tasks, reduction vs critical | 2026-04-20 |
| [Parallel Performance Analysis](wiki/concepts/parallel-performance.md) | concept | Speedup, Amdahl's Law, Gustafson-Barsis Law, parallel efficiency, Roofline model | 2026-04-20 |
| [GPU Architecture and CUDA](wiki/concepts/gpu-cuda.md) | concept | GPU vs CPU, SIMD, CUDA thread hierarchy, warps, memory hierarchy, coalescing, shared memory, parallel reduction | 2026-04-24 |
| [CS475 Review](wiki/courses/CS475-review.md) | reference | Parallel fundamentals, cache optimization, OpenMP, Amdahl/Gustafson, GPU/CUDA — exam review with practice questions | 2026-05-05 |
| [CS475 L07 GPU Basics](raw-sources/courses/CS475/07_GPU_basics.pdf) | source | CS475 lecture 07 — heterogeneous computing, SIMD, CUDA model, thread/block/grid, SM, warps, thread mapping | 2026-04-24 |
| [CS475 L08 GPU Basics Cont](raw-sources/courses/CS475/08_GPU_basics_cont.pdf) | source | CS475 lecture 08 — warp divergence, memory hierarchy, coalescing, shared memory banks, register spilling, parallel reduction | 2026-04-24 |
| [Permutation Groups](wiki/concepts/permutation-groups.md) | concept | Permutations as bijections, symmetric group $S_n$, cycle notation, even/odd, $S_3$ table, Cayley's theorem | 2026-04-16 |
| [Symmetric Groups](wiki/concepts/symmetric-groups.md) | concept | $S_X$/$S_n$ definition, 7 key facts, cycle notation, $S_3$ worked example, alternating group $A_n$, Cayley's theorem | 2026-04-23 |
| [Permutation Groups Video](wiki/summaries/permutation-groups-video.md) | summary | YouTube lecture summary — permutations, $S_3$ composition table, group axioms verified | 2026-04-16 |
| [Cosets](wiki/concepts/cosets.md) | concept | Left/right cosets, partition property, equal-or-disjoint proof, Lagrange's theorem | 2026-04-16 |
| [Cosets Video](wiki/summaries/cosets-video.md) | summary | YouTube lecture summary — coset definition, $\mathbb{Z}_4$ example, proof that overlapping cosets are equal | 2026-04-16 |
| [Group Homomorphisms & Isomorphisms](wiki/concepts/group-homomorphisms.md) | concept | Homomorphism/isomorphism definitions, 5 properties each, automorphisms, non-isomorphism strategies, kernel/image, First Isomorphism Theorem | 2026-04-30 |
| [Normal Subgroups & Quotient Groups](wiki/concepts/normal-subgroups-quotient-groups.md) | concept | Normal subgroup definition, normality test, index-2 fact, coset operation, quotient group theorem | 2026-04-30 |
| [Cyclic Groups](wiki/concepts/cyclic-groups.md) | concept | Order of group/element, $G = \langle a \rangle$, $|a^k| = n/\gcd(k,n)$, properties of $\mathbb{Z}/n\mathbb{Z}$ | 2026-04-16 |
| [Subgroups](wiki/concepts/subgroups.md) | concept | Subgroup definition, long/short/finite subgroup criteria | 2026-04-16 |
| [Dihedral Groups](wiki/concepts/dihedral-groups.md) | concept | Symmetries of regular $n$-gons, $D_n$ generators, $D_4$ example with full Cayley table | 2026-04-16 |
| [A Word on Scalability](wiki/summaries/a-word-on-scalability.md) | summary | Werner Vogels — scalability definition, why it's hard, heterogeneity, design-in-from-start | 2026-04-18 |
| [Zed CRDTs](wiki/summaries/zed-crdts.md) | summary | Zed blog — immutable insertions, tombstone deletion, version vectors, Lamport timestamps, undo map | 2026-04-29 |
| [CRDTs](wiki/concepts/crdts.md) | concept | Conflict-free replicated data types — commutative ops, tombstones, Lamport clocks, undo map, CRDT vs OT | 2026-04-29 |
| [RETVec](wiki/summaries/retvec.md) | summary | Google paper — UTF-8 character encoder + MLP for resilient multilingual text vectorization; beats SentencePiece/BPE on adversarial robustness | 2026-04-20 |
| [CS331 Course Page](wiki/courses/CS331.md) | course | Intro to AI — lecture map; L8 adversarial search (minimax, alpha-beta, expectiminimax) with exercise answers | 2026-10-31 |
| [Adversarial Search](wiki/concepts/adversarial-search.md) | concept | Game setting, minimax value, $O(b^m)$, chance nodes, expectimax/expectiminimax, scale dependence, AlphaStar, adversarial ML, limitations | 2026-10-31 |
| [Alpha-Beta Pruning](wiki/concepts/alpha-beta-pruning.md) | concept | $\alpha$/$\beta$ bounds, prune conditions, pseudocode, step-by-step traces of 4 exercises, move ordering, $O(b^{m/2})$ best case | 2026-10-31 |

## Raw Sources

| Title | Category | Description | Date |
|---|---|---|---|
| [Claude + Obsidian setup](raw-sources/web-clippings/Claude%20+%20Obsidian%20have%20to%20be%20illegal.md) | summary | LLM wiki pattern using Claude Code + Obsidian | 2026-04-09 |
| [How CRDTs Make Multiplayer Text Editing Part of Zed's DNA](raw-sources/web-clippings/How%20CRDTs%20make%20multiplayer%20text%20editing%20part%20of%20Zed's%20DNA.md) | source | Zed blog post — CRDT-based text representation for collaborative editing | 2026-04-29 |
| [A Word on Scalability](raw-sources/web-clippings/A%20Word%20on%20Scalability.md) | source | Werner Vogels on scalability definitions and distributed systems design | 2026-04-18 |
| [RETVec paper (arXiv 2302.09207)](raw-sources/pdfs/2302.09207v3.pdf) | source | Google RETVec paper — resilient multilingual text vectorizer using UTF-8 binary encoding + metric learning | 2026-04-20 |
| [CS475 Lecture 05 — OpenMP Continued](raw-sources/courses/CS475/05_OpenMP_cont.pdf) | source | OpenMP continued: MESI, parallel loops, nowait, data environment, tasks | 2026-04-20 |
| [CS475 Lecture 06 — Tasks + Performance](raw-sources/courses/CS475/06_OpenMP_task_and_performance.pdf) | source | OpenMP tasks deep dive + Amdahl's Law + Gustafson-Barsis Law + Roofline model | 2026-04-20 |
| [perc.converge.pdf](raw-sources/courses/CS434/perc.converge.pdf) | source | Collins convergence proof for the perceptron algorithm | 2026-04-20 |
| [Naive Bayes Classifier (Wikipedia)](raw-sources/web-clippings/Naive%20Bayes%20classifier.md) | source | Wikipedia NB article — probabilistic model, event models, EM semi-supervised, relation to logistic regression, spam filtering | 2026-04-28 |
| [Naive Bayes Classifier (Summary)](wiki/summaries/naive-bayes-classifier-wikipedia.md) | summary | Summary of Wikipedia NB article — event model variants, NB-LR generative-discriminative pair, EM training, spam filtering | 2026-04-28 |
| [Bayes' Theorem (Wikipedia)](raw-sources/web-clippings/Bayes'%20theorem.md) | source | Wikipedia article — theorem statement, derivation, worked examples, interpretations, applications | 2026-04-28 |
| [Bayes' Theorem (Summary)](wiki/summaries/bayes-theorem-wikipedia.md) | summary | Summary of Wikipedia Bayes' theorem article — statement, examples, odds form, interpretations | 2026-04-28 |
| [Bayes' Theorem](wiki/concepts/bayes-theorem.md) | concept | Posterior = prior × likelihood / marginal; base-rate neglect; odds form; ML connections | 2026-04-28 |
| [L4.1 - Naive Bayes.pdf](raw-sources/courses/CS434/L4.1%20-%20Naive%20Bayes.pdf) | source | CS434 lecture slides on generative models, Naïve Bayes, conditional independence | 2026-04-20 |
| [L4.1&2 - Naive Bayes.pdf](raw-sources/courses/CS434/L4.1%262%20-%20Naive%20Bayes.pdf) | source | CS434 L4.2 slides — Laplace smoothing, log-space prediction, logaddexp numerical stability, in-class examples | 2026-04-22 |
| [L5.1 - Support Vector Machines_update.pdf](raw-sources/courses/CS434/L5.1%20-%20Support%20Vector%20Machines_update.pdf) | source | CS434 lecture slides — hard-margin SVM, soft-margin SVM, slack variables, QP solvers, dual formulation | 2026-04-27 |
| [L6.1 - kernel functions.pdf](raw-sources/courses/CS434/L6.1%20-%20kernel%20functions.pdf) | source | CS434 lecture slides — basis functions, kernel trick, Mercer's theorem, kernel SVM, kernelized perceptron/regression | 2026-05-04 |
| [Support Vector Machine (Wikipedia)](raw-sources/web-clippings/Support%20vector%20machine.md) | source | Wikipedia SVM article — motivation, linear/kernel SVM, ERM, multiclass, SVR, implementation | 2026-04-27 |
| [CommonsenseQA (N19-1421)](raw-sources/pdfs/N19-1421.pdf) | source | NAACL 2019 — CommonsenseQA dataset: 12k multiple-choice questions sourced from ConceptNet, human 89% vs BERT 56% | 2026-04-29 |
| [HellaSwag (P19-1472)](raw-sources/pdfs/P19-1472.pdf) | source | ACL 2019 — HellaSwag commonsense NLI benchmark via Adversarial Filtering; human 95.6% vs BERT-Large 47.3% | 2026-04-29 |
| [Trafilatura (2021.acl-demo.15)](raw-sources/pdfs/2021.acl-demo.15.pdf) | source | ACL 2021 demo — Trafilatura web scraping library for corpus construction; best F-score (0.912) among open-source tools | 2026-04-29 |
| [Mitchell — NB & Logistic Regression](raw-sources/pdfs/NBayesLogReg.pdf) | source | Mitchell ML textbook Ch. 3 draft — Naive Bayes, Logistic Regression, and their generative/discriminative relationship | 2026-04-29 |
| [CommonsenseQA Summary](wiki/summaries/commonsenseqa.md) | summary | NAACL 2019 CommonsenseQA paper — ConceptNet-sourced dataset, construction pipeline, baselines, error analysis | 2026-04-29 |
| [HellaSwag Summary](wiki/summaries/hellaswag.md) | summary | ACL 2019 HellaSwag paper — Adversarial Filtering, SWAG analysis, Goldilocks zone, scaling extrapolation | 2026-04-29 |
| [Trafilatura Summary](wiki/summaries/trafilatura.md) | summary | ACL 2021 Trafilatura — web content extraction algorithm, benchmark vs competing tools, corpus construction features | 2026-04-29 |
| [Mitchell NB & LR Summary](wiki/summaries/mitchell-nb-logreg.md) | summary | Mitchell textbook Ch. 3 — NB derivation, Gaussian NB, Logistic Regression training, NB↔LR relationship theorem | 2026-04-29 |
| [Competitive Programmer's Handbook](raw-sources/pdfs/comp%20programming%20handbook.pdf) | reference | CP handbook PDF | — |
| [CS271 Textbook](raw-sources/pdfs/cs271%206th%20edition%20version.pdf) | reference | CS271 textbook PDF | — |
| MTH254 Lecture 14–17 | reference | Vector calculus lecture PDFs | — |
| [Judson Abstract Algebra (PDF)](raw-sources/courses/MTH343/Judson12.pdf) | reference | Judson abstract algebra textbook — source for MTH343 wiki pages | 2026-04-16 |
| [Normal Subgroups & Quotient Groups Handout](raw-sources/courses/MTH343/normal%20subgroups%20and%20quotient%20groups%20handout.pdf) | source | MTH343 handout — normal subgroup definition, normality test, coset operation, quotient group theorem | 2026-04-30 |
| [First Isomorphism Theorem Handout](raw-sources/courses/MTH343/first%20iso%20handout.pdf) | source | MTH343 handout — kernel/image definitions, natural projection map, First Isomorphism Theorem | 2026-04-30 |
| CS434 Lecture Slides (L1.2–L3.2) | reference | kNN, MLE/MAP, linear regression, logistic regression, perceptron | 2026-04-16 |
| CIML Ch. 4–5 | reference | Perceptron algorithm; practical ML issues (features, cross-validation, evaluation) | 2026-04-16 |
| [CS331 Lecture 8 — Adversarial Search](raw-sources/Lecture8_Adversarial_Search.pdf) | source | CS331 L8 slides — minimax, alpha-beta pruning + exercises, expectimax/expectiminimax, modern applications | 2026-10-31 |
