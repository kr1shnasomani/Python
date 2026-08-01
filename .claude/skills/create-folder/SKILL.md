---
name: create-folder
description: Turn a pasted problem (text or screenshot) plus a number prefix into a fully scaffolded problem folder
trigger: /create-folder
---

You are my DSA repo scaffolding assistant for Striver's A2Z DSA Sheet solutions in Python.

I will give you two things: a number prefix (e.g. `19-`) and a problem, either pasted text or a screenshot. Do the following, in order:

1. **Extract the question.** If it's an image, extract the problem statement exactly as it appears. Do not solve it, explain it, summarize it, or rewrite the wording. Preserve the original wording exactly, but lay it out using the **fixed template for the source platform** below, don't improvise formatting and don't just copy whatever heading style happens to be in a sibling file (that's how this repo ended up with competing styles in the first place).

   These two templates are structurally different on purpose, not just styled differently: LeetCode examples are function-call arguments; Code360 samples are raw stdin/stdout blocks (sometimes multiple test cases bundled with a leading count). Never force one platform's content into the other's shape, that means inventing an arg-list that isn't really there, or dropping the real stdin format. Always use `##` for every heading (never `###`), never put a colon after a heading, and use backticks only for inline variables/values, never raw curly quotes and never quote-inside-backtick like `` `'n'` ``.

   **LeetCode template:**
   ````
   <url>

   <problem statement, backticks for variables>

   ## Example 1

   **Input:** `...`
   **Output:** `...`
   **Explanation:** ...   (only if the page shows one)

   ## Example 2
   ...

   ## Constraints

   - `...`
   - `...`
   ````

   **Code360 template:**
   ````
   <url>

   <problem statement>

   > **Note:**
   > ...   (only if the page has a Note callout)

   ## Example

   **Input:**
   `...`

   **Output:**
   `...`

   **Explanation:**
   ...
   (only if the page has a standalone simple example separate from the Sample blocks below — several problems, like the sorting ones, don't have this; skip straight to Sample Input 1 when absent)

   ## Sample Input 1

   ```text
   <raw stdin, exactly as shown>
   ```

   ## Sample Output 1

   ```text
   <raw stdout, exactly as shown>
   ```

   ## Explanation of Sample Input 1

   ...   (this exact heading wording, every time — not "Explanation Of", not "Explanation For", not "Explanation of Input")

   ## Sample Input 2
   ... (repeat the Sample Input/Output/Explanation triplet for every sample the page shows)

   ## Expected Time Complexity

   `...`

   ## Expected Space Complexity

   `...`

   Never drop these when the source page states them, they're real problem content, not skippable chrome. If the page truly doesn't show one of the two, omit only that specific missing one, don't invent a value.

   ## Constraints

   - `...`
   - Time limit: ...   (as the last bullet, only if the page shows a time limit)
   ````
   Skip the "Detailed explanation (Input/output format, Notes, Images)" line always, that's Code360's UI accordion label, not actual problem content. Never add `---` divider rules between sections, headings already separate them.
2. **Find the source URL.** Search in this priority order: Code360 (Naukri) first, then LeetCode if no exact Code360 match, then other major platforms (GeeksforGeeks, HackerRank, InterviewBit, CodeChef, HackerEarth) only if neither has a match. Never invent a URL. Pick the single best match, don't produce a multi-platform report, just the one URL that belongs at the top of `question.md`.
3. **Name the folder** `<number-prefix><Question-Title-From-The-Source>`, hyphen-separated, matching the casing and style already used in this repo (e.g. `19-Next-Permutation`, `20-4-Sum`). Use the title as it appears on the source site.
4. **Create the folder** under the correct top-level section (Arrays, Binary Search, Strings, etc., inferred from the problem type, or ask me if it's ambiguous) with three files:
   - `question.md`: the source URL on the first line, a blank line, then the extracted question content.
   - `answer.py`: empty. I write the solution myself.
   - `approach.md`: empty. Filled in later via the `approach` skill once `answer.py` is done.

Rules:
- Never guess or invent a URL, a title, or problem content you can't verify.
- If you can't confidently find a source match, say so and ask rather than fabricating one.
- Match existing folder naming conventions in the repo (`NN-Title-Case-With-Hyphens`), check a sibling folder in the same section if unsure about naming style specifically.
