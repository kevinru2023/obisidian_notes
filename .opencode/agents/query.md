---
description: "Answer a question using the wiki"
mode: subagent
---

Answer the question provided in the user's message using the wiki. Use a hybrid retrieval strategy — keyword search first, semantic fallback.

Retrieval strategy — never auto-invoke deep search.

1. **Keyword search first.** Use the qmd `search` tool with the question. BM25 match, instant. Review the top snippets. The wiki has distinctive technical vocabulary (concept names, course codes, algorithm names) so most queries are well-served here.

2. **Assess.** If snippets look directly on-topic, skip to step 4. Escalate to step 3 only if results are weak, empty, or off-topic — or if the question is phrased vaguely and unlikely to keyword-match.

3. **Semantic fallback.** Use the qmd `vector_search` tool. This loads a ~1.6 GB local embedding model on first use (cached after); only invoke when step 1 is insufficient. Do NOT auto-invoke `deep_search` — it's the heaviest path and should only run if the user explicitly asks for it.

4. **Read full pages.** Use the qmd `get` tool for each relevant hit. Snippets alone aren't enough for a quality answer — pull the full page (and raw sources it links to, if more detail is needed).

5. **Synthesize.** Clear, well-structured answer with citations to the wiki pages used (Obsidian `[[wikilink]]` format).

6. **Offer to save.** If the answer is substantial and reusable, offer to save it as a new page in `wiki/`.

7. **Log.** Append an entry to `log.md`: `## [YYYY-MM-DD] query | <question>` with a one-line note on which sources were used.
