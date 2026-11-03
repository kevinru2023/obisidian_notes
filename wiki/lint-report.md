---
title: "Wiki Health Report"
type: reference
updated: 2026-04-29
tags: [maintenance, lint]
---

# Wiki Health Report — 2026-04-29

46 wiki pages checked (40 previous + 4 new summaries added today: CommonsenseQA, HellaSwag, Trafilatura, Mitchell NB/LR).

Previous lint (2026-04-27) had 3 open items — 0 resolved since then, all carry forward.

This scan found **2 issues fixed inline** and **6 open items** (3 carry-forward, 3 new).

---

## Fixed This Session

| Issue | File | Action |
|---|---|---|
| `crdts.md` missing H1 heading — body started with `## Definition` | `wiki/concepts/crdts.md` | Added `# CRDTs (Conflict-Free Replicated Data Types)` heading |
| `naive-bayes.md` not linked to Mitchell NB/LR textbook chapter | `wiki/concepts/naive-bayes.md` | Added `[[wiki/summaries/mitchell-nb-logreg]]` to `related:` and `NBayesLogReg.pdf` to `sources:` |

---

## Resolved from Prior Lint

None resolved since 2026-04-27 — all three prior issues still open (see below).

---

## Open Items

### 1. Missing concept page: Cross-Validation *(Carry-forward — Medium)*

Cross-validation is referenced in **four separate pages** with no canonical definition page:

| File | Where mentioned |
|---|---|
| `wiki/concepts/knn.md` | "Choose via cross-validation" |
| `wiki/concepts/regularization.md` | "$\lambda$ is chosen via cross-validation" |
| `wiki/concepts/svm.md` | "$C$ is selected via cross-validation" |
| `wiki/courses/CS434.md` | Full model selection section: k-fold CV, LOO, golden rule |

**Fix:** Create `wiki/concepts/cross-validation.md`. Content already exists in `wiki/courses/CS434.md` under "Model Selection & Evaluation" — extract and expand. Add `[[wiki/concepts/cross-validation]]` to `related:` in knn.md, regularization.md, svm.md.

---

### 2. MTH254 Lectures 14–17 pending ingest *(Carry-forward — Low)*

`wiki/courses/MTH254.md` still shows `(pending ingest)` for Lectures 14–17. Extracted `.md` files exist at `raw-sources/courses/MTH254/Lecture14.md` through `Lecture17.md`.

**Fix:** Run `/ingest raw-sources/courses/MTH254/Lecture14.pdf` through `Lecture17.pdf` when covering that material.

---

### 3. Content overlap: permutation-groups.md vs. symmetric-groups.md *(Carry-forward — Low)*

Both pages cover the $S_n$ definition, $|S_n| = n!$, cycle notation, $S_3$ examples, $A_n$, and Cayley's theorem.

**Fix:** `permutation-groups.md` → abstract general case (bijections, two-row notation, group axioms). `symmetric-groups.md` → the full $S_n$ object specifically. Move $S_3$ composition table to `symmetric-groups.md` only.

---

### 4. CS475 lectures 01–04 not individually indexed *(New — Low)*

Extracted `.md` files exist for `01_Introduction`, `02_Cache`, `03_Cache_cont_and_OpenMP`, `04_OpenMP` under `raw-sources/courses/CS475/`, but they have no rows in `index.md`. Lectures 05–08 are individually indexed. The concept pages they informed are already in the wiki.

**Fix:** Add 4 source rows to `index.md` Raw Sources section:
```
| [CS475 L01 — Introduction](raw-sources/courses/CS475/01_Introduction.pdf) | source | CS475 intro: why parallelism, shared/distributed memory, Flynn's taxonomy, programming models | 2026-04-16 |
| [CS475 L02 — Cache](raw-sources/courses/CS475/02_Cache.pdf) | source | Memory hierarchy, cache lines, associativity, temporal/spatial locality, miss rates | 2026-04-16 |
| [CS475 L03 — Cache cont + OpenMP intro](raw-sources/courses/CS475/03_Cache_cont_and_OpenMP.pdf) | source | Loop ordering, blocked matmul, false sharing, OpenMP fork-join basics | 2026-04-16 |
| [CS475 L04 — OpenMP](raw-sources/courses/CS475/04_OpenMP.pdf) | source | OpenMP directives, data environment, reduction, critical sections, barriers | 2026-04-16 |
```

---

### 5. CS434 HW2 extracted but not ingested *(New — Low)*

`raw-sources/courses/CS434/CS434_HW2_S25.md` exists (extracted) but has no wiki page and no index entry. HW1 is listed in the CS434 course page under Homeworks but HW2 shows only `(Spring 2025)` with no details.

**Fix:** Run `/ingest raw-sources/courses/CS434/CS434_HW2_S25.pdf` and update the Homeworks table in `wiki/courses/CS434.md` with what topics it covers.

---

### 6. New NLP summaries have no inbound links from wiki pages *(New — Low)*

The four summaries ingested today are correctly indexed but no existing wiki page links to them, except:
- `naive-bayes.md` now links to `mitchell-nb-logreg.md` (fixed this session)
- `logistic-regression.md` already links to `mitchell-nb-logreg.md` (fixed during ingest)

Remaining isolated summaries:

| Summary | No inbound link from |
|---|---|
| `commonsenseqa.md` | Any wiki page |
| `hellaswag.md` | Any wiki page |
| `trafilatura.md` | Any wiki page |

These are standalone papers not tied to coursework, so isolation is acceptable for now. If Kevin reads more NLP papers, consider adding a `wiki/concepts/nlp-benchmarks.md` concept page or a `wiki/courses/` entry for an NLP course.

**Fix (optional):** No action required unless more NLP material is added and a connecting concept page becomes worthwhile.

---

## Summary Table

| # | Severity | Issue | File(s) | Fix |
|---|---|---|---|---|
| 1 | Medium | No cross-validation concept page | knn.md, regularization.md, svm.md, CS434.md | Create `wiki/concepts/cross-validation.md` |
| 2 | Low | MTH254 lectures 14–17 pending ingest | `wiki/courses/MTH254.md` | `/ingest` when ready |
| 3 | Low | permutation-groups ↔ symmetric-groups overlap | both pages | Differentiate scope on next edit |
| 4 | Low | CS475 L01–04 not indexed | `index.md` | Add 4 source rows |
| 5 | Low | CS434 HW2 extracted but not ingested | `wiki/courses/CS434.md` | `/ingest CS434_HW2_S25.pdf` |
| 6 | Low | CommonsenseQA, HellaSwag, Trafilatura isolated | new summaries | Optional: create NLP concept page when more NLP material added |
