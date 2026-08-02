# Approach

## Main Logic

```python
result = n * factorial(n - 1)
```

- If `n` is `0` or `1`, return `1` (base case).
- Otherwise, multiply `n` by the factorial of `n - 1`.
- Repeat until the base case is reached.

**Remember:** To find the factorial of `n`, multiply `n` with the factorial of `n-1`.

---

## Dry Run

### Example 1: `n = 4`

```text
factorial(4)
= 4 × factorial(3)
= 4 × (3 × factorial(2))
= 4 × (3 × (2 × factorial(1)))
= 4 × (3 × (2 × 1))
= 4 × (3 × 2)
= 4 × 6
= 24
```

**Output:** `24`

---

### Example 2: `n = 3`

```text
factorial(3)
= 3 × factorial(2)
= 3 × (2 × factorial(1))
= 3 × (2 × 1)
= 3 × 2
= 6
```

**Output:** `6`

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` - Recursive call stack.