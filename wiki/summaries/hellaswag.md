---
title: "HellaSwag — ACL 2019"
type: summary
sources:
  - "[[raw-sources/pdfs/P19-1472.pdf]]"
related:
  - "[[wiki/summaries/commonsenseqa]]"
updated: 2026-04-29
tags: [NLP, commonsense-reasoning, benchmarks, adversarial-filtering, BERT, NLI, datasets]
---

# HellaSwag — ACL 2019

**Paper:** "HellaSwag: Can a Machine Really Finish Your Sentence?"
**Authors:** Zellers, Holtzman, Bisk, Farhadi, Choi (UW + Allen AI)
**Venue:** ACL 2019

---

## What It Is

HellaSwag is a **commonsense natural language inference (NLI)** benchmark: given a short context (a sentence or paragraph describing an event), a model must choose the most plausible continuation from 4 options. It contains **70,000 problems**.

- **Humans:** >95% accuracy
- **BERT-Large (state-of-the-art at release):** <48% accuracy

The gap is intentional — HellaSwag is designed to be adversarially hard for deep pretrained models while trivially easy for humans.

---

## Motivation: SWAG Was Solved

The predecessor dataset SWAG (Zellers et al. 2018) was similarly structured. When introduced, state-of-the-art models scored <60%, but **BERT soon reached 86%** — near human performance. The paper investigates *why* SWAG was solved and builds a harder successor.

**Key finding from SWAG analysis:** BERT doesn't need context to perform well:
- Drop context ("Ending Only"): accuracy falls only 11.9 points (86.7% → 74.8%)
- Shuffle words in endings ("Shuffled"): accuracy drops less than 10%
- BERT largely learns **lexical/distributional patterns** from the fine-tuning data, not deep commonsense reasoning

---

## Adversarial Filtering (AF)

AF is the core data construction algorithm, also from SWAG:

1. **Generate** candidate wrong answers using a language model (here: GPT fine-tuned on domain data)
2. **Train a discriminator** (BERT-Large) to classify endings as real vs. generated
3. **Replace** easy-to-classify generations with harder ones on each iteration
4. Repeat until discriminator accuracy converges

**Result:** The final dataset is adversarial for *any* model, not just the discriminator used during construction — because making it hard for BERT also made it hard for every other model tested.

**Why SWAG was too easy:** Its generator (a 2-layer LSTM) produced outputs so stylistically different from human text that BERT could distinguish them without needing commonsense. GPT's higher-quality generations don't have this problem.

---

## Dataset Sources

| Source | Domain | Examples |
|---|---|---|
| ActivityNet Captions | Video description (activities) | 25k |
| WikiHow | How-to articles (diverse topics) | 45k |
| **Total** | | **70k** |

**Why WikiHow:** Diverse topics (80k+ how-to articles), longer generations give more opportunities for errors detectable by humans but not models. Two-sentence generations find the "Goldilocks zone" — nonsensical to humans, but confusing to discriminators.

---

## Results

| Model | Overall Accuracy |
|---|---|
| Random chance | 25.0% |
| fastText | 31.6% |
| LSTM + GloVe | 31.7% |
| ESIM + ELMo | 33.3% |
| BERT-Base | 40.5% |
| OpenAI GPT | 41.7% |
| **BERT-Large** | **47.3%** |
| Human | **95.6%** |

Even BERT-Large (used as the adversarial filter) only reaches 47.3% — **48+ points below human performance**.

Performance drops an additional ~5% on **zero-shot categories** (topics not seen during training), indicating BERT is partially memorizing categories rather than learning general reasoning.

---

## Scaling Analysis

The paper extrapolates from pretraining compute vs. accuracy:

$$\text{Estimated compute to reach human-level: } \sim 10^9 \text{ GPU-hours (100k GPU-years)}$$

This suggests pure scaling is insufficient — **algorithmic improvements** (better architectures, pretraining objectives, or world-modeling) are needed to solve commonsense NLI as a task.

---

## Key Contributions

1. **Diagnosis of SWAG:** Shows BERT solved SWAG by learning distributional artifacts, not commonsense
2. **Goldilocks zone:** Identifies the right generation length (2 sentences) where AF produces human-easy, machine-hard examples
3. **HellaSwag benchmark:** 70k problems, humans 95.6%, BERT 47.3%
4. **Evolving benchmarks:** Argues NLP benchmarks must co-evolve with state-of-the-art models via iterative adversarial construction

---

## Relation to CommonsenseQA

Both HellaSwag and CommonsenseQA target commonsense reasoning and show large human–machine gaps. HellaSwag focuses on **situational continuation** (what happens next), while CommonsenseQA focuses on **concept relationships** (where/what/why). Both highlight that BERT-style models exploit surface statistics rather than genuine world knowledge.
