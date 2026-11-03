---
title: "RETVec: Resilient and Efficient Text Vectorizer"
type: summary
sources:
  - "[[raw-sources/pdfs/2302.09207v3.pdf]]"
related:
  - "[[wiki/concepts/naive-bayes]]"
updated: 2026-04-20
tags: [nlp, text-vectorization, adversarial-robustness, embeddings, multilingual, machine-learning]
---

# RETVec: Resilient and Efficient Text Vectorizer

**Paper:** Bursztein et al. (Google, 2023) — arXiv 2302.09207  
**Code:** [github.com/google-research/retvec](https://github.com/google-research/retvec) (Apache 2)

## What It Is

RETVec is a character-level text vectorizer that converts words into 256-dimensional embeddings. It is designed to be:
- **Resilient** — robust against typos and adversarial attacks
- **Efficient** — only 230k parameters, <1MB, no vocabulary file required
- **Multilingual** — trained on 157 languages, handles all valid UTF-8 characters with no OOV tokens

## Architecture

**Two-stage pipeline:**

1. **Character Encoder** (stateless, no learned weights):
   - *Integerizer*: converts each character to its UTF-8 codepoint (up to 16 chars)
   - *Binarizer*: encodes each codepoint as a 24-bit binary float → word becomes a $16 \times 24$ float32 matrix

2. **Small MLP Model** (230k params, optional):
   - Dense projection → Flatten → Dense compression → 256-dim embedding layer (tanh activation)
   - Trained via **pair-wise metric learning** (Multi-Similarity Loss) on typo-augmented pairs
   - Goal: words with typos map close to their originals in embedding space

"RETVec-raw" = character encoder only (no model). "RETVec" = encoder + pre-trained model.

## Pre-training

- Dataset: 88.8M unique tokens from Common Crawl (157 languages) + 8.88M random tokens → 1.9B examples after 20 augmentations per token
- 80% of training tokens are typo-augmented (insertion, deletion, substitution, transposition, up to 25% of token length)
- 500k steps, batch size 1024, Adam, cosine LR decay

## Key Results

**Classification accuracy** (avg over 4 datasets, 3 architectures): RETVec leads by ~0.9% over the next-best vectorizer (SentencePiece/whitespace). Particularly strong on multilingual datasets and non-Latin scripts.

**Typo resilience:** At 20% random word typo rate, RETVec is ~15% more accurate than SentencePiece/BPE. fastText and whitespace are more resilient than subword tokenizers, but RETVec still leads.

**Adversarial attack resilience** (TextBugger, DeepWordBug, Pruthi on AG News via BERT-Mini):

| Vectorizer | Original Acc | Under Attack | Attack Success |
|---|---|---|---|
| SentencePiece | 89.8% | 25.8% | 71.3% |
| BPE | 90.8% | 29.2% | 67.8% |
| fastText | 92.6% | 40.5% | 56.3% |
| **RETVec** | **93.7%** | **51.7%** | **44.8%** |

**Speed:** Fastest vectorizer with GPU available; top-3 on multicore CPU. Zero preprocessing time (no vocabulary file to build).

**BERT pre-training (GLUE):** BERT-Base with RETVec-raw achieves 79.4 avg GLUE score vs. 79.6 for SentencePiece — essentially on par, while cutting BERT pre-training time by ~10%.

**In production at Google:** Swapping SentencePiece for RETVec in Gmail spam filtering improved recall at 0.80% FPR by ~0.51% and reduced serving latency by 30%.

## Design Insights

- The binary UTF-8 encoding is key: it's compact, learnable, and stateless. One-hot and single-float-per-character representations didn't work as well.
- A simple MLP outperforms transformer/LSTM/CNN architectures as the embedding model — the task is easy enough that added complexity doesn't help.
- 256-dim embeddings and 16 max characters per word are the sweet spots (larger doesn't improve downstream tasks).
- Lower pre-training loss ≠ better downstream accuracy. An extra validation pass on Amazon Reviews was needed to select hyperparameters.

## Limitations

- Cannot be directly used for generative/decoder tasks because the 256-float embedding has no inverse mapping to token IDs. Applying RETVec to LLMs would require a new pre-training procedure (e.g., character-by-character decoding, VQ-VAE quantization).
- Character deletion is the hardest typo type for both RETVec and RETVec-raw.
- RETVec-raw struggles more with character insertion; the pre-trained model largely fixes this.
