# Approach

## Main Logic
```python
if int(num[i]) % 2 != 0:
    return num[:i + 1]
```
- Scan the string from right to left, checking one digit at a time.
- A digit is odd if `digit % 2 != 0`.
- The moment you find the first odd digit while going right to left, stop immediately and return everything from the start of the string up to and including that digit (`num[:i + 1]`).
- This works because the string has no leading zeros, so a longer prefix is always a bigger number than a shorter one. The rightmost odd digit you can find gives you the longest possible prefix that still ends in an odd digit, which makes it the largest odd number available.
- If the loop finishes without finding any odd digit, there's no odd substring at all, so return `""`.

**Remember:** A number's odd/even nature depends only on its last digit, so just walk backward until you hit an odd digit, that's your cutoff point.

---

## Dry Run

### Example 1: `num = "52"`
| i | num[i] | digit % 2 | odd? | action |
|---|--------|-----------|------|--------|
| 1 | 2 | 0 | no | continue |
| 0 | 5 | 1 | yes | return `num[:1]` → `"5"` |

### Example 2: `num = "4206"`
| i | num[i] | digit % 2 | odd? | action |
|---|--------|-----------|------|--------|
| 3 | 6 | 0 | no | continue |
| 2 | 0 | 0 | no | continue |
| 1 | 2 | 0 | no | continue |
| 0 | 4 | 0 | no | continue |

Loop finishes with no odd digit found, return `""`.

### Example 3: `num = "35427"`
| i | num[i] | digit % 2 | odd? | action |
|---|--------|-----------|------|--------|
| 4 | 7 | 1 | yes | return `num[:5]` → `"35427"` |

---

## Complexity Analysis
- Time Complexity: O(n) - in the worst case (no odd digit, or the odd digit is at the very start), we scan every character of `num`.
- Space Complexity: O(1) - aside from the returned substring itself, we only use a loop index, no extra data structures.
