# Approach

## Main Logic
```python
if ch == "(":
    depth += 1
    max_depth = max(max_depth, depth)
elif ch == ")":
    depth -= 1
```
- `depth` tracks how deeply nested the current position is, starting at 0.
- Every `(` increases `depth` by 1, and right after that increase, check whether this is the highest `depth` seen so far, if so, update `max_depth`.
- Every `)` decreases `depth` by 1. No need to check `max_depth` here, closing a bracket can only bring you back down, never up to a new high.
- Any character that isn't `(` or `)` (digits, `+`, `-`, `*`, `/`) is simply skipped, it doesn't affect nesting at all.

**Remember:** The deepest point is always reached the instant you open a bracket, so only check for a new max right after incrementing `depth`.

---

## Dry Run

### Example 1: `s = "(1+(2*3)+((8)/4))+1"`
| char | action | depth | max_depth |
|------|--------|-------|-----------|
| ( | depth += 1 | 1 | 1 |
| 1 | ignored | 1 | 1 |
| + | ignored | 1 | 1 |
| ( | depth += 1 | 2 | 2 |
| 2 | ignored | 2 | 2 |
| * | ignored | 2 | 2 |
| 3 | ignored | 2 | 2 |
| ) | depth -= 1 | 1 | 2 |
| + | ignored | 1 | 2 |
| ( | depth += 1 | 2 | 2 |
| ( | depth += 1 | 3 | 3 |
| 8 | ignored | 3 | 3 |
| ) | depth -= 1 | 2 | 3 |
| / | ignored | 2 | 3 |
| 4 | ignored | 2 | 3 |
| ) | depth -= 1 | 1 | 3 |
| ) | depth -= 1 | 0 | 3 |
| + | ignored | 0 | 3 |
| 1 | ignored | 0 | 3 |

Return `max_depth` → `3`.

### Example 2: `s = "(1)+((2))+(((3)))"`
| char | action | depth | max_depth |
|------|--------|-------|-----------|
| ( | depth += 1 | 1 | 1 |
| 1 | ignored | 1 | 1 |
| ) | depth -= 1 | 0 | 1 |
| + | ignored | 0 | 1 |
| ( | depth += 1 | 1 | 1 |
| ( | depth += 1 | 2 | 2 |
| 2 | ignored | 2 | 2 |
| ) | depth -= 1 | 1 | 2 |
| ) | depth -= 1 | 0 | 2 |
| + | ignored | 0 | 2 |
| ( | depth += 1 | 1 | 2 |
| ( | depth += 1 | 2 | 2 |
| ( | depth += 1 | 3 | 3 |
| 3 | ignored | 3 | 3 |
| ) | depth -= 1 | 2 | 3 |
| ) | depth -= 1 | 1 | 3 |
| ) | depth -= 1 | 0 | 3 |

Return `max_depth` → `3`.

### Example 3: `s = "()(())((()()))"`
| char | action | depth | max_depth |
|------|--------|-------|-----------|
| ( | depth += 1 | 1 | 1 |
| ) | depth -= 1 | 0 | 1 |
| ( | depth += 1 | 1 | 1 |
| ( | depth += 1 | 2 | 2 |
| ) | depth -= 1 | 1 | 2 |
| ) | depth -= 1 | 0 | 2 |
| ( | depth += 1 | 1 | 2 |
| ( | depth += 1 | 2 | 2 |
| ( | depth += 1 | 3 | 3 |
| ) | depth -= 1 | 2 | 3 |
| ( | depth += 1 | 3 | 3 |
| ) | depth -= 1 | 2 | 3 |
| ) | depth -= 1 | 1 | 3 |
| ) | depth -= 1 | 0 | 3 |

Return `max_depth` → `3`.

---

## Complexity Analysis
- Time Complexity: O(n) - we scan the string once, doing constant work per character, where n is the length of `s`.
- Space Complexity: O(1) - only `depth` and `max_depth` counters are used, no extra data structures.
