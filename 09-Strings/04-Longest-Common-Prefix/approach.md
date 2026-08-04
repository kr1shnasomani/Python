# Approach

## Main Logic
```python
if prefix[i] == word[i]:
    i += 1
else:
    break

prefix = prefix[:i]
```
- Start by assuming the whole first string, `strs[0]`, is the common prefix.
- For every other word in the list, walk `prefix` and `word` together, character by character, using an index `i` starting at 0.
- The `while` loop's condition (`i < len(prefix) and i < len(word)`) stops you from walking past the end of either string.
- While characters match, move `i` forward. The moment they differ, stop immediately with `break`.
- After comparing against this word, shrink `prefix` down to `prefix[:i]`, keeping only the part that actually matched.
- If `prefix` ever becomes empty, no word can share anything in common anymore, so return `""` right away without checking the rest.
- Once every word has been checked, whatever remains in `prefix` is the answer.

**Remember:** Shrink the prefix as you go, one mismatched word is enough to cut it down, and once it's empty, you can stop early.

---

## Dry Run

### Example 1: `strs = ["flower", "flow", "flight"]`
Start: `prefix = "flower"`

Comparing against `"flow"`:
| i | prefix[i] | word[i] | match? | action |
|---|-----------|---------|--------|--------|
| 0 | f | f | yes | i += 1 |
| 1 | l | l | yes | i += 1 |
| 2 | o | o | yes | i += 1 |
| 3 | w | w | yes | i += 1 |
| 4 | - | - | i == len(word), loop stops | - |

`prefix = prefix[:4]` → `"flow"` (not empty, continue)

Comparing against `"flight"`:
| i | prefix[i] | word[i] | match? | action |
|---|-----------|---------|--------|--------|
| 0 | f | f | yes | i += 1 |
| 1 | l | l | yes | i += 1 |
| 2 | o | i | no | break |

`prefix = prefix[:2]` → `"fl"` (not empty, no more words left)

Return `"fl"`.

### Example 2: `strs = ["dog", "racecar", "car"]`
Start: `prefix = "dog"`

Comparing against `"racecar"`:
| i | prefix[i] | word[i] | match? | action |
|---|-----------|---------|--------|--------|
| 0 | d | r | no | break |

`prefix = prefix[:0]` → `""`

`prefix == ""`, so return `""` immediately, `"car"` never even gets checked.

---

## Complexity Analysis
- Time Complexity: O(n * m) - in the worst case, we compare the shrinking prefix against every other string character by character, where n is the number of strings and m is the length of the shortest string (the prefix can never grow past that).
- Space Complexity: O(m) - aside from the returned string, `prefix` is the only extra string we keep around, bounded by the length of the shortest common prefix.