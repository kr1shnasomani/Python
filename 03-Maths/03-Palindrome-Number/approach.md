# Approach

## Main Logic

```python
rev = rev * 10 + (x % 10)
x //= 10
```

- If `x` is negative, return `False`.
- Store the original number.
- Reverse the number digit by digit.
- Compare the reversed number with the original.
- If both are the same, it is a palindrome.

**Remember:** A number is a palindrome if it is the same forwards and backwards.

---

## Dry Run

### Example 1: `x = 121`

| x | rev | Last digit (`x % 10`) | New rev |
|---:|---:|---:|---:|
| 121 | 0 | 1 | `0 * 10 + 1 = 1` |
| 12 | 1 | 2 | `1 * 10 + 2 = 12` |
| 1 | 12 | 1 | `12 * 10 + 1 = 121` |
| 0 | 121 | - | Loop ends |

Compare:
- Original = `121`
- Reversed = `121`

**Output:** `True`

---

### Example 2: `x = -121`

Since `x < 0`, return `False`.

**Output:** `False`

---

### Example 3: `x = 10`

| x | rev | Last digit (`x % 10`) | New rev |
|---:|---:|---:|---:|
| 10 | 0 | 0 | `0 * 10 + 0 = 0` |
| 1 | 0 | 1 | `0 * 10 + 1 = 1` |
| 0 | 1 | - | Loop ends |

Compare:
- Original = `10`
- Reversed = `1`

**Output:** `False`

---

## Complexity Analysis

- **Time Complexity:** `O(log x)`
- **Space Complexity:** `O(1)`
