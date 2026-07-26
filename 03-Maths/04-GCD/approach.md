# Approach

## Main Logic

```python
remainder = x % y
x = y
y = remainder
```

- Find the remainder when `x` is divided by `y`.
- Make `y` the new `x`.
- Make the remainder the new `y`.
- Repeat until `y` becomes `0`.
- The remaining value of `x` is the GCD.

**Remember:** Replace the bigger number with the smaller number, and the smaller number with the remainder until the remainder becomes `0`.

---

## Dry Run

### Example 1: `x = 20`, `y = 5`

| x | y | Remainder (`x % y`) | New x | New y |
|---:|---:|---:|---:|---:|
| 20 | 5 | 0 | 5 | 0 |
| 5 | 0 | - | Loop ends | - |

**Output:** `5`

---

### Example 2: `x = 96`, `y = 14`

| x | y | Remainder (`x % y`) | New x | New y |
|---:|---:|---:|---:|---:|
| 96 | 14 | 12 | 14 | 12 |
| 14 | 12 | 2 | 12 | 2 |
| 12 | 2 | 0 | 2 | 0 |
| 2 | 0 | - | Loop ends | - |

**Output:** `2`

---

### Example 3: `x = 18`, `y = 12`

| x | y | Remainder (`x % y`) | New x | New y |
|---:|---:|---:|---:|---:|
| 18 | 12 | 6 | 12 | 6 |
| 12 | 6 | 0 | 6 | 0 |
| 6 | 0 | - | Loop ends | - |

**Output:** `6`

---

## Complexity Analysis

- **Time Complexity:** `O(log(min(x, y)))`
- **Space Complexity:** `O(1)`
