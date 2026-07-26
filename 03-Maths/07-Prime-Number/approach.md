# Approach

## Main Logic

```python
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        return False

return True
```

- If `n <= 1`, it is not a prime number.
- Check only from `2` to `√n`.
- If any number divides `n`, then `n` is not prime.
- If no divisor is found, then `n` is prime.

**Remember:** A prime number has exactly **2 divisors**: `1` and itself. If you find any other divisor, it is **not** prime.

---

## Dry Run

### Example 1: `n = 13`

| i | `13 % i == 0` | Action |
|--:|:-------------:|:-------|
| 2 | ❌ | Continue |
| 3 | ❌ | Continue |

Loop ends.

No divisor found.

**Output:** `True`

---

### Example 2: `n = 15`

| i | `15 % i == 0` | Action |
|--:|:-------------:|:-------|
| 2 | ❌ | Continue |
| 3 | ✅ | Return `False` |

A divisor (`3`) is found, so the number is not prime.

**Output:** `False`

---

### Example 3: `n = 2`

Since:

```text
√2 ≈ 1.41
```

The loop:

```python
range(2, int(math.sqrt(2)) + 1)
```

becomes:

```python
range(2, 2)
```

So the loop does not run.

No divisor found.

**Output:** `True`

---

## Complexity Analysis

- **Time Complexity:** `O(√n)`
- **Space Complexity:** `O(1)`
