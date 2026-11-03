Ingest a new file into the wiki. The file is: $ARGUMENTS

Instructions:
0. **Determine the target file(s).**
   - If $ARGUMENTS is non-empty, use it as the file path (search by filename in raw-sources/ if a full path wasn't given). Proceed to step 1 with that single file.
   - If $ARGUMENTS is empty, run `git status --porcelain` and collect every line starting with `??` whose path begins with `raw-sources/`. Present the list to the user, then ingest each file in sequence using the steps below.
1. Read CLAUDE.md to understand the wiki schema and directory layout.
3. If it's a PDF and there is no corresponding .md file already, run:
   `python tools/extract_pdf.py <path>`
   This produces a .md file alongside the PDF using docling (local, no API calls).
4. Read the extracted/raw content thoroughly.
5. Based on the file type and location, create or update the appropriate wiki pages:
   - Course material → write/update `wiki/courses/[COURSE].md` and relevant `wiki/concepts/` pages
   - Web clipping or article → write a summary to `wiki/summaries/`
   - Book → write a summary to `wiki/summaries/`
   - Personal note → ensure it has frontmatter; no wiki page needed
6. Math formatting pass: scan every wiki page you wrote or edited. Any mathematical
   expression not already in LaTeX must be converted:
   - Inline expressions → $expression$
   - Standalone/display equations → $$expression$$
   Applies to: formulas, integrals, summations, vectors, matrices, Greek letters used
   as math symbols, Big-O notation like O(n log n), probability expressions, etc.
7. Update `index.md` with:
   - A row for the raw-source file itself (category: `source`).
   - A row for each new wiki page created (category: `summary`, `concept`, `course`, or `reference` as appropriate).
8. Re-index the qmd vector database so the new content is searchable:
   - Run `qmd update` (rebuilds the BM25/keyword index).
   - Run `qmd embed` (regenerates vector embeddings — ~2s per doc).
9. Append an entry to `log.md` listing all files touched.
10. Report every file you created or modified.
