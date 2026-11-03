---
title: "Trafilatura — ACL 2021"
type: summary
sources:
  - "[[raw-sources/pdfs/2021.acl-demo.15.pdf]]"
related: []
updated: 2026-04-29
tags: [NLP, web-scraping, corpus-building, text-extraction, tools, Python]
---

# Trafilatura — ACL 2021

**Paper:** "Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction"
**Author:** Adrien Barbaresi (Berlin-Brandenburg Academy of Sciences)
**Venue:** ACL 2021 (Demo)

---

## What It Is

Trafilatura is an open-source Python library and CLI tool for **web content extraction**: given a web page, it strips boilerplate (headers, footers, ads, navigation menus) and returns the main text content. It is designed for large-scale corpus construction for NLP.

```bash
pip install trafilatura
trafilatura -u "https://example.com/article"
```

---

## Problem Context

Building NLP corpora from the web requires:
1. **Crawling**: finding and downloading pages
2. **Extraction**: keeping useful text, discarding boilerplate
3. **Quality filtering**: deduplication, language detection, etc.

Step 2 ("boilerplate removal" or "main content extraction") is the focus of Trafilatura. It is harder than it looks: web pages vary enormously in structure, HTML validity, and content mix (ads, links, comments, menus, etc.).

---

## Extraction Algorithm

Trafilatura uses a **cascade of rule-based filters** with two fallback libraries:

1. **XPath-based content delimitation:** excludes unwanted elements (e.g., `<div class='nav'>`) then targets main content regions (e.g., `<section id='entry-content'>`). Same process applied for comments if requested.

2. **Fallback (if triggered):** runs **readability-lxml** and **jusText** as backup algorithms; compares their output to Trafilatura's own by length and "impurity" (presence of non-text elements).

3. **Last resort:** scans for any "wild" text elements that may have been missed.

**Output formats:** plain text, CSV, JSON, XML, XML-TEI (Text Encoding Initiative format). Metadata extraction includes title, site name, author, date, categories, and tags.

**Additional features:**
- URL queue processing with polite crawling (domain-based rate limiting)
- Sitemap (XML/TXT) and web feed (ATOM/RDF/RSS) support
- Language detection via CLD3
- Works with CommonCrawl and Internet Archive data

---

## Benchmark Results (500 Documents)

Evaluated on 500 manually annotated web pages (German + other European languages, English, Chinese, Arabic). Metric: precision/recall/F-score on correctly identified text segments vs. boilerplate.

| Tool | Precision | Recall | F-Score | Relative Speed |
|---|---|---|---|---|
| Raw HTML baseline | 0.527 | 0.878 | 0.659 | 1× |
| jusText 2.2.0 (custom) | 0.870 | 0.584 | 0.699 | 6.1× slower |
| newspaper3k | 0.921 | 0.574 | 0.708 | 12.9× slower |
| boilerpy3 | 0.851 | 0.696 | 0.766 | 4.8× slower |
| goose3 | 0.950 | 0.644 | 0.767 | 18.8× slower |
| dragnet | 0.906 | 0.689 | 0.783 | 3.1× slower |
| readability-lxml | 0.917 | 0.716 | 0.804 | 5.9× slower |
| news-please | 0.924 | 0.718 | 0.808 | 60× slower |
| **Trafilatura (fast)** | **0.925** | **0.868** | **0.896** | **3.9× slower** |
| **Trafilatura (full)** | **0.934** | **0.890** | **0.912** | **8.4× slower** |

Trafilatura achieves the highest F-score (0.912) while being much faster than competing high-precision tools. It also outperforms others in external benchmarks (ScrapingHub article extraction, multilingual DANIEL corpus).

---

## Key Design Points

- **Precision–recall tradeoff:** Rule-based approaches sacrifice some precision for higher recall. Trafilatura's "full" mode uses fallback libraries to improve both.
- **Multilingual robustness:** Tested on German primarily but includes other languages; most tools were developed for English-centric pages.
- **HTML diversity:** "HTMLects" vary by era, geography, and CMS — what works for one style fails on others. Trafilatura tries to mitigate via generic rules + fallbacks.
- **Open-source and actively maintained:** Most comparable tools are abandoned or only available for specific languages.

---

## Use Cases

- Building training corpora for language models
- Web-scale NLP dataset construction (e.g., cleaning CommonCrawl data)
- Lexicographic research (structured text for dictionary/corpus platforms)
- News monitoring / crawling pipelines
