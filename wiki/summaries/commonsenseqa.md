---
title: "CommonsenseQA — NAACL 2019"
type: summary
sources:
  - "[[raw-sources/pdfs/N19-1421.pdf]]"
related:
  - "[[wiki/summaries/hellaswag]]"
updated: 2026-04-29
tags: [NLP, question-answering, commonsense-reasoning, benchmarks, BERT, ConceptNet, datasets]
---

# CommonsenseQA — NAACL 2019

**Paper:** "CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge"
**Authors:** Talmor, Herzig, Lourie, Berant (Tel-Aviv University + Allen AI)
**Venue:** NAACL 2019

---

## What It Is

CommonsenseQA is a multiple-choice QA dataset of **12,247 questions** designed to require commonsense knowledge beyond what appears in any provided context — knowledge humans take for granted but that NLU systems lack.

---

## Dataset Construction

Questions are grounded in **ConceptNet**, a large commonsense knowledge graph with 32 million triplets of the form *(concept, relation, concept)*.

**Generation pipeline:**
1. Sample a **source concept** and three **target concepts** that share the same ConceptNet relation (e.g., source = "River", relation = AtLocation, targets = "Waterfall", "Bridge", "Valley")
2. Crowd workers (Amazon Mechanical Turk) author **one question per target concept** such that only that target is the correct answer, while the other two targets are wrong
3. Workers add **two additional distractors** per question (one from ConceptNet, one hand-authored)
4. Final format: each question has **5 candidate answers** (1 correct, 4 distractors)
5. Web snippets from Google are added as optional context for reading-comprehension baselines

**Quality control:** Each question verified by 2 workers; only questions answered correctly by at least one verifier are kept (filters ~15%).

---

## Key Statistics

| Measurement | Value |
|---|---|
| Total questions | 12,247 |
| Avg. question length | 13.4 tokens |
| Candidate answers per question | 5 |
| Top ConceptNet relation | AtLocation (47.3%) |
| Human accuracy | 88.9% |
| Best model (BERT-Large) accuracy | 55.9% |

---

## Commonsense Skill Categories

Manual analysis of 100 dev examples identified 9 skill types (avg 1.75 per question):

| Skill | Definition |
|---|---|
| Spatial | Concept A appears near Concept B |
| Cause & Effect | A causes B |
| Has Parts | A contains B as a component |
| Is Member Of | A belongs to class B |
| Purpose | A is the purpose of B |
| Social | Social convention linking A and B |
| Activity | A is performed in context of B |
| Definition | A defines B |
| Preconditions | A must hold for B to occur |

---

## Baseline Models and Results

| Model | Random Split Accuracy |
|---|---|
| Random chance | 20.0% |
| VECSIM + Numberbatch | 29.1% |
| LM1B (language model) | 26.1% |
| ESIM + ELMo | 34.1% |
| ESIM + GloVe | 32.8% |
| GPT | 45.5% |
| **BERT-Large** | **55.9%** |
| BIDAF++ (with web context) | 32.0% |
| Human | 88.9% |

**Key finding:** BERT-Large reaches only 55.9% — roughly 33 points below human performance — demonstrating that commonsense knowledge is still a major gap for NLU systems.

**SANITY mode:** When hard distractors are replaced with random ConceptNet distractors, BERT-Large jumps to 92.3%, confirming that difficult distractors (not random ones) are what makes the benchmark hard.

---

## BERT-Large Error Analysis

| Category | Accuracy | Frequency |
|---|---|---|
| Surface clues hint to answer | 77.7% | 35% |
| Negation / antonym required | 42.8% | 7% |
| Factoid knowledge required | 38.4% | 13% |
| Correct answer has finer granularity | 35.4% | 31% |
| Conjunction of conditions required | 23.8% | 23% |

---

## Significance

- **Reporting bias problem:** Questions often require knowledge that humans know implicitly but is rarely stated explicitly on the web, making web-retrieval baselines weak.
- **Annotation artifact mitigation:** By using ConceptNet-seeded distractors (semantically similar to the answer), workers are forced to encode commonsense into the question rather than surface cues.
- **Scale:** Unlike earlier commonsense datasets (Winograd: 150 examples, COPA: 1000), CommonsenseQA provides 12k+ high-quality examples.
