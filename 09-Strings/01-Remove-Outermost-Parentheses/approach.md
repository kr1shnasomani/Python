# Approach

## Main Logic
```python
if ch == "(":
    if open_count > 0:
        ans.append(ch)
    open_count += 1
else:
    open_count -= 1
    if open_count > 0:
        ans.append(ch)
```
- `open_count` tracks how deeply nested the current position is, it goes up on every `(` and down on every `)`.
- For an opening bracket `(`, check `open_count` first. If it's already greater than 0, this bracket is sitting inside something else, so keep it. Only then increase `open_count`.
- For a closing bracket `)`, decrease `open_count` first, then check it. If it's still greater than 0, this bracket is also inside something else, so keep it.
- The order matters on purpose: check-before-increment for `(`, decrement-before-check for `)`. This makes sure the only brackets that ever get skipped are the ones that touch `open_count == 0`, which are exactly the outermost bracket of each primitive group.

**Remember:** A bracket is "outermost" exactly when it's the one crossing the boundary between depth 0 and depth 1, everything else is safely nested and gets kept.

---

## Dry Run

### Example 1: `s = "(()())(())"`
| Char | open_count (Before) | Action | open_count (After) | ans |
|------|----------------------|--------|---------------------|-----|
| ( | 0 | 0 > 0? no → skip, then increment | 1 | [] |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | ['('] |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | ['(', ')'] |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | ['(', ')', '('] |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | ['(', ')', '(', ')'] |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | ['(', ')', '(', ')'] |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | ['(', ')', '(', ')'] |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | ['(', ')', '(', ')', '('] |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | ['(', ')', '(', ')', '(', ')'] |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | ['(', ')', '(', ')', '(', ')'] |

`"".join(ans)` → `"()()()"`

### Example 2: `s = "(()())(())(()(()))"`
| Char | open_count (Before) | Action | open_count (After) | ans |
|------|----------------------|--------|---------------------|-----|
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "()()" |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "()()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()()(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()()" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "()()()" |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "()()()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()()()(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()()()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()()()()(" |
| ( | 2 | 2 > 0? yes → append '(', then increment | 3 | "()()()()((" |
| ) | 3 | decrement → 2, 2 > 0? yes → append ')' | 2 | "()()()()(()" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()()()(())" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "()()()()(())" |

`"".join(ans)` → `"()()()()(())"`

### Example 3: `s = "()()"`
| Char | open_count (Before) | Action | open_count (After) | ans |
|------|----------------------|--------|---------------------|-----|
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "" |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "" |

`"".join(ans)` → `""`

---

## Complexity Analysis
- Time Complexity: O(n) - we scan the string once, doing constant work per character, where n is the length of `s`.
- Space Complexity: O(n) - the `ans` list can hold up to n characters in the worst case (excluding the output itself, extra space is O(1), just the `open_count` counter).
