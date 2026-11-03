# Kevin's Personal Wiki

An Obsidian vault that works as my personal knowledge base. I write my notes, and an LLM keeps the wiki on top of them organized.

## Why I built this

I was tired of taking my own notes and writing my own study sheets. Every class meant the same routine: read the slides, rewrite them as notes, then condense those notes into a review sheet before the exam. So I set up a system where an LLM does that bookkeeping. I drop in a lecture PDF or an article, and it summarizes the material, links it to related concepts, and keeps everything cross-referenced. When an exam comes up, I can ask it for a study sheet built from everything I've collected.

It turned out to be a cool project, but I didn't build it to show off. I built it for myself, to solve a problem I had.

## Credit

This project is based on Andrej Karpathy's **[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** idea (April 2026). Rather than retrieving from raw documents every time you ask a question, the LLM builds a persistent, interlinked markdown wiki and keeps adding to it over time. The schema file, [`CLAUDE.md`](CLAUDE.md), follows his structure of raw sources, an LLM-maintained wiki, and a schema.

## How it's organized

| Layer | Owner | What's in it |
|---|---|---|
| `raw-sources/` | Nobody (read-only) | Lecture slides, textbooks, papers and web clippings. **Not included in this repo**, because I don't own that material. |
| `wiki/` | The LLM | Source summaries, concept pages, course synthesis pages and quick-reference cheatsheets. |
| `notes/` | Me | My own notes in my own words: coursework, CTF writeups, DSA/LeetCode, C++, books and personal notes. |

There are also two special files:

- [`index.md`](index.md): an index of every page. The LLM reads this first when answering a question.
- [`log.md`](log.md): an append-only log of every ingest, query and lint pass.

> Because `raw-sources/` isn't in this repo, any `[[raw-sources/...]]` wikilinks inside wiki pages won't resolve here on GitHub.

### What's in here

- **Courses:** CS162, CS271, CS331, CS434 (machine learning), CS475 (parallel programming), MTH254 (vector calculus), MTH343 (abstract algebra), Intro to ML
- **Cybersecurity:** notes and writeups from CTFs (Active Directory, reverse engineering, Linux internals, and more)
- **DSA:** data structures and algorithms notes, plus Neetcode/LeetCode problems
- **C++:** language notes
- **Books and personal:** reading notes, goals and ideas

## Operations

These are slash commands for [Claude Code](https://claude.com/claude-code). They're defined in [`.claude/commands/`](.claude/commands/).

| Command | What it does |
|---|---|
| `/ingest <file>` | Reads a new source, writes a summary, updates concept and course pages, and records it in the index and log |
| `/query <question>` | Answers a question from the wiki and logs it |
| `/query-render <question>` | Same as `/query`, but renders the answer as an HTML page |
| `/course-review <course>` | Generates a full review/study document for a course |
| `/lint` | Runs a health check: broken links, orphan pages, stale entries |

OpenCode ([`opencode.json`](opencode.json), [`.opencode/`](.opencode/)) and Codex ([`.codex/`](.codex/)) are configured to read the same `CLAUDE.md`, so the workflow isn't tied to a single tool.

## Setup

1. Clone the repo and open the folder as an [Obsidian](https://obsidian.md) vault.
2. Create a `raw-sources/` folder and add your own material to it.
3. *(Optional)* To convert PDFs to markdown with [`tools/extract_pdf.py`](tools/extract_pdf.py):
   ```bash
   pip install -r requirements.txt
   cp .env.example .env   # then add your ANTHROPIC_API_KEY
   ```
