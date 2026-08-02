# Approach

## Main Logic
```python
if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
    total = total - roman[s[i]]
else:
    total = total + roman[s[i]]
```
- A dictionary `roman` maps each symbol to its value, so looking up a symbol's value is instant.
- `total` starts at 0, and `i` scans every character of `s` from left to right.
- At each position, compare the current symbol's value with the next symbol's value.
- If the current value is smaller than the next one (like `I` before `V` in `IV`), that's a subtractive pair, so subtract the current value instead of adding it.
- Otherwise, just add the current value normally.
- The last character has no "next" character to compare with, so the check `i < len(s) - 1` makes sure it always falls into the "add" case.

**Remember:** Whenever a smaller symbol sits right before a bigger one, it means "subtract me", otherwise just add the symbol's value as you go.

---

## Dry Run

### Example 1: `s = "III"`
| i | s[i] | next | roman[s[i]] | roman[next] | smaller than next? | action | total |
|---|------|------|-------------|-------------|---------------------|--------|-------|
| 0 | I | I | 1 | 1 | no | add | 0 + 1 = 1 |
| 1 | I | I | 1 | 1 | no | add | 1 + 1 = 2 |
| 2 | I | (none, last char) | 1 | - | no | add | 2 + 1 = 3 |

Return `3`.

### Example 2: `s = "LVIII"`
| i | s[i] | next | roman[s[i]] | roman[next] | smaller than next? | action | total |
|---|------|------|-------------|-------------|---------------------|--------|-------|
| 0 | L | V | 50 | 5 | no | add | 0 + 50 = 50 |
| 1 | V | I | 5 | 1 | no | add | 50 + 5 = 55 |
| 2 | I | I | 1 | 1 | no | add | 55 + 1 = 56 |
| 3 | I | I | 1 | 1 | no | add | 56 + 1 = 57 |
| 4 | I | (none, last char) | 1 | - | no | add | 57 + 1 = 58 |

Return `58`.

### Example 3: `s = "MCMXCIV"`
| i | s[i] | next | roman[s[i]] | roman[next] | smaller than next? | action | total |
|---|------|------|-------------|-------------|---------------------|--------|-------|
| 0 | M | C | 1000 | 100 | no | add | 0 + 1000 = 1000 |
| 1 | C | M | 100 | 1000 | yes | subtract | 1000 - 100 = 900 |
| 2 | M | X | 1000 | 10 | no | add | 900 + 1000 = 1900 |
| 3 | X | C | 10 | 100 | yes | subtract | 1900 - 10 = 1890 |
| 4 | C | I | 100 | 1 | no | add | 1890 + 100 = 1990 |
| 5 | I | V | 1 | 5 | yes | subtract | 1990 - 1 = 1989 |
| 6 | V | (none, last char) | 5 | - | no | add | 1989 + 5 = 1994 |

Return `1994`.

---

## Complexity Analysis
- Time Complexity: O(n) - we scan the string once, and each dictionary lookup takes O(1), where n is the length of `s`.
- Space Complexity: O(1) - the `roman` dictionary always holds exactly 7 fixed keys, no matter how long `s` is.
