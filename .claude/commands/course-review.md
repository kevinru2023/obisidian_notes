Generate a comprehensive review document for a course. The course is: $ARGUMENTS

This skill works for both midterm and final exam prep. Follow the steps below precisely.

---

### Step 1 — Parse course identifier

Extract the course code from `$ARGUMENTS` (e.g., `CS475`). Normalize to uppercase. If no argument is given, ask the user which course to review.

---

### Step 2 — Read the course wiki page

Call `mcp__qmd__get` on `wiki/courses/[COURSE].md`. Extract:
- Every path listed under `related:` in the frontmatter — these are the concept pages to pull
- Every topic row in the Lecture Map / schedule table
- All algorithm or key-concept sections in the body

---

### Step 3 — Read all linked concept pages

For each `related:` path from Step 2, call `mcp__qmd__get`. Then call `mcp__qmd__search` with the course code to catch any additional concept pages that reference this course but aren't listed in `related:`. Pull those with `mcp__qmd__get` as well.

---

### Step 4 — Read course notes

Call `mcp__qmd__search` with the course code scoped to the `notes` collection. Pull any matching files with `mcp__qmd__get`. These contain Kevin's own intuitions, emphasis marks, and mnemonics — treat them as high-signal indicators of what matters.

---

### Step 5 — Decide what to include

Build the concept list automatically. **Include** a topic if it meets any of these signals:
- Has a dedicated `wiki/concepts/` page
- Appears in the Lecture Map table of the course page
- Appears in Kevin's course notes
- Is mentioned in ≥2 source files for this course

**Exclude** if it only appears as a passing mention in one source with no dedicated concept page. Lean toward inclusion over exclusion — a review doc should be comprehensive.

---

### Step 6 — Generate the review document

Write the file to `wiki/courses/[COURSE]-review.md`. Overwrite it if it already exists. Use this structure:

```
---
title: "[COURSE] Review"
type: reference
sources:
  - "[[wiki/courses/[COURSE]]]"
  - (one entry per concept page used)
related:
  - "[[wiki/courses/[COURSE]]]"
updated: YYYY-MM-DD
tags: [[COURSE], review]
---

# [COURSE] Review

## Quick-Reference Table
| Concept | Core Idea | Key Formula / Rule |
|---|---|---|
| ... | ... | ... |

## [Concept Name]

**Definition:** ...

**Key formula(s):**
$$...$$

**Intuition / When to use:** ...

**Common exam questions:**
- ...

**Gotchas / edge cases:** ...

**See also:** [[wiki/concepts/...]]

---

(repeat for each concept)

---

## Concept Connections

Prose or table explaining how the major concepts relate to each other and build on one another.

## Practice Questions

5–10 synthesis questions that require combining multiple concepts. Do not include answers — these are for self-testing.
```

**Formatting rules:**
- All math in LaTeX: inline as `$...$`, display as `$$...$$`
- All internal references as Obsidian `[[wikilink]]` with paths relative to vault root
- Concept sections ordered from foundational → advanced (roughly following the lecture order on the course page)

---

### Step 7 — Update wiki metadata

1. **index.md** — add or update the row for this review page:
   `| [COURSE Review](wiki/courses/[COURSE]-review.md) | reference | <one-line description> | YYYY-MM-DD |`

2. **Rebuild qmd:**
   - Run `qmd update`
   - Run `qmd embed`

3. **log.md** — append:
   ```
   ## [YYYY-MM-DD] course-review | [COURSE]
   Concepts covered: <comma-separated list>
   Output: wiki/courses/[COURSE]-review.md
   ```

---

### Step 8 — Report

List every file written or modified.
