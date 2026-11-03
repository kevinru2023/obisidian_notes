Answer this question using the wiki, then render the answer as an HTML page and open it in the browser. Question: $ARGUMENTS

---

## Step 1 — Query

Retrieval strategy — hybrid, keyword first, semantic fallback. Never auto-invoke deep search.

1. **Keyword search first.** Call `mcp__qmd__search` with the question. BM25 match, no models loaded, instant. Review the top snippets. Your wiki has distinctive technical vocabulary (concept names, course codes, algorithm names) so most queries are well-served here.

2. **Assess.** If snippets look directly on-topic, skip to step 4. Escalate to step 3 only if results are weak, empty, or off-topic — or if the question is phrased vaguely ("how do threads step on each other", "why does this feel slow") and unlikely to keyword-match.

3. **Semantic fallback.** Call `mcp__qmd__vector_search`. This loads a ~1.6 GB expansion/embedding model on first use (cached after); only invoke when step 1 is insufficient. **Do NOT auto-invoke `mcp__qmd__deep_search`** — it's the heaviest path and should only run if the user explicitly asks for it.

4. **Read full pages.** Use `mcp__qmd__get` for each relevant hit. Snippets alone aren't enough for a quality answer — pull the full page (and raw sources it links to, if more detail is needed).

5. **Synthesize.** Produce a clear, well-structured answer with citations to the wiki pages used (Obsidian `[[wikilink]]` format). Store this answer in memory for the render step below — do NOT output it to the user yet.

6. **Offer to save.** If the answer is substantial and reusable, note that you'll offer to save it as a new page in `wiki/` after rendering.

---

## Step 2 — Render

Using the answer synthesized above as the content:

1. **Write a self-contained HTML file to `/tmp/wiki_render.html`.** The file must include all of the following, loaded from CDN so no local assets are needed:
   - **marked.js** (`https://cdn.jsdelivr.net/npm/marked/marked.min.js`) for markdown-to-HTML rendering.
   - **KaTeX** stylesheet (`https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css`) and script (`https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js`) for LaTeX math rendering.
   - **KaTeX auto-render extension** (`https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js`) so that LaTeX delimiters inside the rendered markdown are automatically processed. Configure it with delimiters: `$$...$$` for display math, `$...$` for inline math, and `\[...\]` / `\(...\)` as aliases.

2. **Page style.** Use a clean light theme:
   - Background `#f9f9f6`, text `#1a1a1a`, max content width `780px`, centered with `auto` side margins, generous padding, `font-family: Georgia, serif` for body text, `font-family: monospace` for code blocks.
   - Code blocks: background `#f0f0ec`, border-radius `4px`, padding `1em`, overflow-x auto.
   - Blockquotes: left border `3px solid #ccc`, padding-left `1em`, color `#555`.
   - Headings use a slightly darker shade with a bottom border on `h1`.

3. **Page structure.** The HTML body should contain a single `<div id="content">` element. In the page's inline `<script>`, embed the raw markdown string as a JavaScript template literal assigned to a `const md` variable, render it with `document.getElementById('content').innerHTML = marked.parse(md)`, then immediately call `renderMathInElement(document.getElementById('content'), { ... })` with the KaTeX auto-render options. Escape any backticks or backslashes in the markdown content as needed so the template literal is valid JavaScript.

4. **Open the file** by running the shell command `open /tmp/wiki_render.html`.

---

## Step 3 — Log

Append a single entry to `log.md`:
```
## [YYYY-MM-DD] query-render | <question>
Sources: <wiki pages cited>
Output: /tmp/wiki_render.html
```
Use today's date.

---

## Step 4 — Report

Output the synthesized answer to the user, confirm the browser was opened, and report the path `/tmp/wiki_render.html`.
