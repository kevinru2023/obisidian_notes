Render content as a self-contained HTML page with markdown and LaTeX support, then open it in the browser. Content to render: $ARGUMENTS

Instructions:

1. **Determine the content to render.**
   - If $ARGUMENTS is non-empty, use $ARGUMENTS as the content verbatim.
   - Otherwise, open `log.md` and find the most recent entry whose header matches `## [YYYY-MM-DD] query | ...`. Extract the question from that line, re-run the `/query` skill with that question, and use the answer as the content.

2. **Write a self-contained HTML file to `/tmp/wiki_render.html`.** The file must include all of the following, loaded from CDN so no local assets are needed:
   - **marked.js** (`https://cdn.jsdelivr.net/npm/marked/marked.min.js`) for markdown-to-HTML rendering.
   - **KaTeX** stylesheet (`https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css`) and script (`https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js`) for LaTeX math rendering.
   - **KaTeX auto-render extension** (`https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js`) so that LaTeX delimiters inside the rendered markdown are automatically processed. Configure it with delimiters: `$$...$$` for display math, `$...$` for inline math, and `\[...\]` / `\(...\)` as aliases.

3. **Page style.** Use a clean light theme:
   - Background `#f9f9f6`, text `#1a1a1a`, max content width `780px`, centered with `auto` side margins, generous padding, `font-family: Georgia, serif` for body text, `font-family: monospace` for code blocks.
   - Code blocks: background `#f0f0ec`, border-radius `4px`, padding `1em`, overflow-x auto.
   - Blockquotes: left border `3px solid #ccc`, padding-left `1em`, color `#555`.
   - Headings use a slightly darker shade with a bottom border on `h1`.

4. **Page structure.** The HTML body should contain a single `<div id="content">` element. In the page's inline `<script>`, embed the raw markdown string as a JavaScript template literal assigned to a `const md` variable, render it with `document.getElementById('content').innerHTML = marked.parse(md)`, then immediately call `renderMathInElement(document.getElementById('content'), { ... })` with the KaTeX auto-render options. Escape any backticks or backslashes in the markdown content as needed so the template literal is valid JavaScript.

5. **Open the file** by running the shell command `open /tmp/wiki_render.html`.

6. **Append to `log.md`.** Add an entry in this format:
   ```
   ## [YYYY-MM-DD] render | <one-line description of what was rendered>
   Output: /tmp/wiki_render.html
   Query: <the question or topic that was rendered, or "manual content" if $ARGUMENTS was provided directly rather than derived from a query>
   ```
   Use today's date. If the content came from a `/query` result, use that query's question as the `Query:` value. If it was arbitrary content passed via $ARGUMENTS, summarize the topic in a few words.

7. **Report** the full path `/tmp/wiki_render.html` and confirm the file was opened.
