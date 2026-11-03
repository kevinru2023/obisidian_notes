# Kevin's Personal Wiki — Schema

## Purpose

This is a personal wiki maintained collaboratively by Kevin and Claude. It serves as:

- An academic knowledge base (CS, Math coursework)
- A technical reference base (cybersecurity, DSA, C++)
- A personal knowledge base (books, articles, ideas, goals)
- A rich source of context for any Claude session

The wiki follows the **LLM Wiki pattern**: raw sources are immutable inputs; Claude maintains the `wiki/` layer; Kevin owns the `notes/` layer. The human curates and asks questions — Claude handles the bookkeeping.

---

## Directory Structure

### `raw-sources/`
External material Kevin has consumed. **Treat as immutable — never modify these files.** This is the source of truth.

| Subdirectory | Contents |
|---|---|
| `raw-sources/web-clippings/` | Articles saved via Obsidian Web Clipper |
| `raw-sources/books/` | Book PDFs |
| `raw-sources/courses/CS162/` | CS162 lecture slides, assignments, reference material |
| `raw-sources/courses/CS271/` | CS271 material |
| `raw-sources/courses/CS434/` | CS434 lecture slides, assignment PDFs, extra resources |
| `raw-sources/courses/CS475/` | CS475 lecture notes, assignment PDFs |
| `raw-sources/courses/MTH254/` | MTH254 vector calculus slides and PDFs |
| `raw-sources/courses/ML/` | Intro to ML course materials |
| `raw-sources/pdfs/` | General reference PDFs not tied to a specific course |
| `raw-sources/personal/` | Saved conversations, transcripts, personal documents |


### `wiki/`
LLM-generated and maintained markdown. **Claude owns this layer entirely.** Kevin reads it; Claude writes it.

| Subdirectory | Contents |
|---|---|
| `wiki/summaries/` | One summary page per ingested source |
| `wiki/concepts/` | Concept/topic pages (e.g., "Binary Trees", "Active Directory", "Gradient Descent") |
| `wiki/courses/` | Course-level synthesis pages (one per course) |
| `wiki/reference/` | Quick-reference cheatsheets (tool commands, language syntax, etc.) |

### `notes/`
Kevin's own writing — in his own words. **Kevin owns this layer.** Claude may clean formatting and add frontmatter metadata but must preserve content and intent.

| Subdirectory | Contents |
|---|---|
| `notes/courses/CS162/` | CS162 course notes |
| `notes/courses/CS271/` | CS271 course notes |
| `notes/courses/CS434/` | CS434 course notes |
| `notes/courses/CS475/` | CS475 course notes |
| `notes/courses/MTH254/` | MTH254 vector calculus notes (loose Cornell format) |
| `notes/courses/ML/` | Intro to ML notes |
| `notes/cybersec/` | Cybersecurity reference material from past CTFs and problems |
| `notes/cybersec/writeups/` | CTF writeups |
| `notes/DSA/` | Data structures and algorithms notes |
| `notes/DSA/leetcode/` | Neetcode/LeetCode problem notes |
| `notes/cpp/` | C++ language notes |
| `notes/books/` | Notes and annotations from books read |
| `notes/personal/` | Goals, ideas, reflections, random thoughts |

### Special Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | This file — the schema and operating instructions |
| `index.md` | Content index. Updated on every ingest. Claude reads this first on every query. |
| `log.md` | Append-only chronological log of ingests, queries, and lint passes |

### Other

| Path | Purpose |
|---|---|
| `tools/extract_pdf.py` | Convert PDFs to Markdown using the Anthropic API (vision-capable; auto-chunks textbooks; LaTeX math formatting built in). Dependencies: `pip install anthropic pypdf python-dotenv` |
| `.claude/commands/` | Slash command definitions — `/ingest`, `/query`, `/lint` |
| `templates/` | Obsidian note templates (do not modify) |
| `Images/` | Image attachments referenced by notes |

---

## Page Conventions

### Wiki pages (`wiki/`) — frontmatter
```yaml
---
title: "Page Title"
type: summary | concept | course | reference
sources:
  - "[[raw-sources/path/to/source]]"
related:
  - "[[wiki/concepts/related-concept]]"
updated: YYYY-MM-DD
tags: [tag1, tag2]
---
```

### Notes (`notes/`) — frontmatter
```yaml
---
title: "Note Title"
course: CS434        # if applicable
type: course-notes | reference | book-notes | personal
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

### Linking conventions
- All internal links use Obsidian `[[wikilink]]` format with paths relative to vault root
- Wiki pages link to raw sources: `[[raw-sources/courses/CS434/lecture01.pdf]]`
- Wiki pages cross-reference each other: `[[wiki/concepts/binary-trees]]`
- Notes may reference wiki pages: `[[wiki/concepts/gradient-descent]]`

### index.md format
Each entry is a table row:
```
| [Title](path/to/file.md) | category | One-line description | YYYY-MM-DD |
```
Categories: `summary`, `concept`, `course`, `reference`, `note`, `personal`

### log.md format
Each entry starts with a consistent prefix for easy grepping:
```
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query | Question asked
## [YYYY-MM-DD] lint | Weekly health check
```

---

## Operations

All operations are available as slash commands inside Claude Code. Drop the file first, then:

| What you want | Command |
|---|---|
| Ingest any new file | `/ingest <filename>` |
| Ask a question | `/query <your question>` |
| Weekly health check | `/lint` |

Slash command definitions live in `.claude/commands/` — edit them there if the behavior needs tuning.

---

## Domain Notes (read before touching these areas)

### Cybersecurity (`notes/cybersec/`)
Reference material from past CTFs and security problems. **Preserve exact commands, tool flags, and observations verbatim** — this is a lookup resource, not a teaching document. Do not summarize or paraphrase technical details.

### Course Notes (`notes/courses/`)
Follow a **loose Cornell format** (main notes + key questions/concepts in margin, summary at bottom) but don't enforce it strictly. Consistent frontmatter is more important than rigid structure. Never rewrite Kevin's explanations — he wrote them to match his mental model.

### Personal notes (`notes/personal/`)
Informal and varied — goals, shower thoughts, book reactions, random ideas. Don't over-structure. Just ensure they have frontmatter and show up in index.md.
