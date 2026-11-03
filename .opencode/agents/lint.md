---
description: "Run a health check on the wiki"
mode: subagent
---

Run a health check on the wiki.

Instructions:
1. Read every file in `wiki/`.
2. Check for:
   - Contradictions between pages
   - Orphan pages with no inbound links from index.md
   - Concepts mentioned across multiple pages but lacking a dedicated concept page
   - Pages whose `updated` date is old relative to newer raw sources on the same topic
3. Write a health report to `wiki/lint-report.md` with specific suggested fixes (not vague observations).
4. Append an entry to `log.md`: `## [YYYY-MM-DD] lint | Weekly health check`
