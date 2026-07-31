# Approach

## Main Logic

```python
if n % i == 0:
    result.append(i)

    if i != n // i:
        result.append(n // i)
```

- Check only from `1` to `√n`.
- If `i` divides `n`, then `i` is a divisor.
- `n // i` is also a divisor, so add it too.
- If both divisors are the same (perfect square), add it only once.
- Sort the list before returning.

**Remember:** Divisors always come in pairs, so checking only till `√n` is enough.

---

## Key Concept

### Divisors Come in Pairs

- Divisors of a number `n` always come in pairs: if `i` divides `n`, then `n // i` also divides `n`.
- Property: for every divisor `i ≤ √n`, there's a matching divisor `n // i ≥ √n`.
- Why it works: divisors are symmetric around `√n`. One half of every pair is always ≤ `√n`, so checking only up to `√n` is guaranteed to find both halves of each pair.
- Special case: when `i == n // i` (n is a perfect square), both halves of the pair are the same number, so add it only once.

**Remember:** You never need to check past `√n`. Every divisor beyond it is just the "partner" of one you've already found below it.

---

## Dry Run

### Example 1: `n = 10`

Initially:

```text
result = []
```

| i | `10 % i == 0` | `result.append(i)` | `i != n // i` | `result.append(n // i)` | Result |
|--:|:-------------:|:------------------:|:-------------:|:-----------------------:|:-------|
| 1 | ✅ | Add `1` | `1 != 10` ✅ | Add `10` | `[1, 10]` |
| 2 | ✅ | Add `2` | `2 != 5` ✅ | Add `5` | `[1, 10, 2, 5]` |
| 3 | ❌ | - | - | - | `[1, 10, 2, 5]` |

After sorting:

```text
[1, 2, 5, 10]
```

**Output:** `[1, 2, 5, 10]`

---

### Example 2: `n = 6`

Initially:

```text
result = []
```

| i | `6 % i == 0` | `result.append(i)` | `i != n // i` | `result.append(n // i)` | Result |
|--:|:------------:|:------------------:|:-------------:|:-----------------------:|:-------|
| 1 | ✅ | Add `1` | `1 != 6` ✅ | Add `6` | `[1, 6]` |
| 2 | ✅ | Add `2` | `2 != 3` ✅ | Add `3` | `[1, 6, 2, 3]` |

After sorting:

```text
[1, 2, 3, 6]
```

**Output:** `[1, 2, 3, 6]`

---

### Example 3: `n = 36`

Initially:

```text
result = []
```

| i | `36 % i == 0` | `result.append(i)` | `i != n // i` | `result.append(n // i)` | Result |
|--:|:-------------:|:------------------:|:-------------:|:-----------------------:|:-------|
| 1 | ✅ | Add `1` | `1 != 36` ✅ | Add `36` | `[1, 36]` |
| 2 | ✅ | Add `2` | `2 != 18` ✅ | Add `18` | `[1, 36, 2, 18]` |
| 3 | ✅ | Add `3` | `3 != 12` ✅ | Add `12` | `[1, 36, 2, 18, 3, 12]` |
| 4 | ✅ | Add `4` | `4 != 9` ✅ | Add `9` | `[1, 36, 2, 18, 3, 12, 4, 9]` |
| 5 | ❌ | - | - | - | `[1, 36, 2, 18, 3, 12, 4, 9]` |
| 6 | ✅ | Add `6` | `6 != 6` ❌ | Skip | `[1, 36, 2, 18, 3, 12, 4, 9, 6]` |

After sorting:

```text
[1, 2, 3, 4, 6, 9, 12, 18, 36]
```

**Output:** `[1, 2, 3, 4, 6, 9, 12, 18, 36]`

---

## Complexity Analysis

- **Time Complexity:** `O(√n)`
- **Space Complexity:** `O(d) where d is the number of divisors`
