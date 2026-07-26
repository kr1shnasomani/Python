# Approach

## Main Logic

```python
count += 1
n //= 10
```

- `count += 1` → Count the current digit.
- `n //= 10` → Remove the last digit.
- Repeat until `n` becomes `0`.

**Remember:** Every time you remove one digit, increase the count by `1`.

---

## Dry Run

### Example 1: `n = 123`

| n | count | New count | New n (`n // 10`) |
|---:|---:|---:|---:|
| 123 | 0 | 1 | 12 |
| 12 | 1 | 2 | 1 |
| 1 | 2 | 3 | 0 |
| 0 | 3 | - | Loop ends |

**Output:** `3`

---

### Example 2: `n = 121`

| n | count | New count | New n (`n // 10`) |
|---:|---:|---:|---:|
| 121 | 0 | 1 | 12 |
| 12 | 1 | 2 | 1 |
| 1 | 2 | 3 | 0 |
| 0 | 3 | - | Loop ends |

**Output:** `3`

---

### Example 3: `n = 38`

| n | count | New count | New n (`n // 10`) |
|---:|---:|---:|---:|
| 38 | 0 | 1 | 3 |
| 3 | 1 | 2 | 0 |
| 0 | 2 | - | Loop ends |

**Output:** `2`

---

## Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`
