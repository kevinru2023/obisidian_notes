Answer this question using the wiki: $ARGUMENTS

Retrieval strategy — hybrid, keyword first, semantic fallback. Never auto-invoke deep search.

1. **Keyword search first.** Call `mcp__qmd__search` with the question. BM25 match, no models loaded, instant. Review the top snippets. Your wiki has distinctive technical vocabulary (concept names, course codes, algorithm names) so most queries are well-served here.

2. **Assess.** If snippets look directly on-topic, skip to step 4. Escalate to step 3 only if results are weak, empty, or off-topic — or if the question is phrased vaguely ("how do threads step on each other", "why does this feel slow") and unlikely to keyword-match.

3. **Semantic fallback.** Call `mcp__qmd__vector_search`. This loads a ~1.6 GB expansion/embedding model on first use (cached after); only invoke when step 1 is insufficient. **Do NOT auto-invoke `mcp__qmd__deep_search`** — it's the heaviest path and should only run if the user explicitly asks for it.

4. **Read full pages.** Use `mcp__qmd__get` for each relevant hit. Snippets alone aren't enough for a quality answer — pull the full page (and raw sources it links to, if more detail is needed).

5. **Synthesize.** Clear, well-structured answer with citations to the wiki pages used (Obsidian `[[wikilink]]` format).

6. **Offer to save.** If the answer is substantial and reusable, offer to save it as a new page in `wiki/`.

7. **Log.** Append an entry to `log.md`: `## [YYYY-MM-DD] query | <question>` with a one-line note on which sources were used.
