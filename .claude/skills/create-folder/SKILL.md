---
name: create-folder
description: Turn a pasted problem (text or screenshot) plus a number prefix into a fully scaffolded problem folder
trigger: /create-folder
---

You are my DSA repo scaffolding assistant for Striver's A2Z DSA Sheet solutions in Python.

I will give you two things: a number prefix (e.g. `19-`) and a problem, either pasted text or a screenshot. Do the following, in order:

1. **Extract the question.** If it's an image, extract the problem statement exactly as it appears. Do not solve it, explain it, summarize it, or rewrite the wording. Preserve the original wording and all markdown/formatting exactly. **Match the source platform's actual structure, don't force everything into a LeetCode-shaped template.** Before writing, check an existing `question.md` from the same platform elsewhere in the repo as a formatting reference:
   - **Code360 questions**: variables in backticks, a `> **Note:**` blockquote for the Note section, then `## Sample Input N` / `## Sample Output N` headers with fenced ` ```text ` blocks (raw space-separated values, not bracket-list style), `## Explanation of Sample Input N` headers, and `## Constraints` as a bullet list. Skip the "Detailed explanation (Input/output format, Notes, Images)" line, that's just Code360's UI accordion label, not actual problem content.
   - **LeetCode questions**: `## Example N` headers with **Input:**/**Output:**/**Explanation:** bold labels, values in backticks, `## Constraints` as a bullet list.
2. **Find the source URL.** Search in this priority order: Code360 (Naukri) first, then LeetCode if no exact Code360 match, then other major platforms (GeeksforGeeks, HackerRank, InterviewBit, CodeChef, HackerEarth) only if neither has a match. Never invent a URL. Pick the single best match, don't produce a multi-platform report, just the one URL that belongs at the top of `question.md`.
3. **Name the folder** `<number-prefix><Question-Title-From-The-Source>`, hyphen-separated, matching the casing and style already used in this repo (e.g. `19-Next-Permutation`, `20-4-Sum`). Use the title as it appears on the source site.
4. **Create the folder** under the correct top-level section (Arrays, Binary Search, Strings, etc., inferred from the problem type, or ask me if it's ambiguous) with three files:
   - `question.md`: the source URL on the first line, a blank line, then the extracted question content.
   - `answer.py`: empty. I write the solution myself.
   - `approach.md`: empty. Filled in later via the `approach` skill once `answer.py` is done.

Rules:
- Never guess or invent a URL, a title, or problem content you can't verify.
- If you can't confidently find a source match, say so and ask rather than fabricating one.
- Match existing folder naming conventions in the repo (check a sibling folder in the same section if unsure).
