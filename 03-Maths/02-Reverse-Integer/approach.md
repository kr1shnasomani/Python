# Approach

## Main Logic

```python
rev = rev * 10 + (x % 10)
x //= 10
```

- `x % 10` → Get the last digit.
- `rev * 10` → Shift the current reversed number one place to the left.
- Add the last digit to `rev`.
- `x //= 10` → Remove the last digit from `x`.
- Repeat until `x` becomes `0`.

**Remember:** Keep taking the last digit from the original number and append it to the end of the new number.

---

## Dry Run

### Example 1: `x = 123`

| x | rev | Last digit (`x % 10`) | New rev |
|---:|---:|---:|---:|
| 123 | 0 | 3 | `0 * 10 + 3 = 3` |
| 12 | 3 | 2 | `3 * 10 + 2 = 32` |
| 1 | 32 | 1 | `32 * 10 + 1 = 321` |
| 0 | 321 | - | Loop ends |

**Output:** `321`

---

### Example 2: `x = -123`

Take the absolute value first (`123`), then apply the sign at the end.

| x | rev | Last digit (`x % 10`) | New rev |
|---:|---:|---:|---:|
| 123 | 0 | 3 | `0 * 10 + 3 = 3` |
| 12 | 3 | 2 | `3 * 10 + 2 = 32` |
| 1 | 32 | 1 | `32 * 10 + 1 = 321` |
| 0 | 321 | - | Loop ends |

Apply sign: `321 × (-1) = -321`

**Output:** `-321`

---

### Example 3: `x = 120`

| x | rev | Last digit (`x % 10`) | New rev |
|---:|---:|---:|---:|
| 120 | 0 | 0 | `0 * 10 + 0 = 0` |
| 12 | 0 | 2 | `0 * 10 + 2 = 2` |
| 1 | 2 | 1 | `2 * 10 + 1 = 21` |
| 0 | 21 | - | Loop ends |

**Output:** `21`

---

## Complexity Analysis

- **Time Complexity:** `O(log x)`
- **Space Complexity:** `O(1)`
