# Approach

## Main Logic

```python
result = (n * (n + 1)) // 2
```

- Use the mathematical formula:

  **Sum of first `n` natural numbers = `n × (n + 1) / 2`**

- Use `//` to get an integer result.
- Return the calculated sum.

**Remember:** Instead of adding numbers one by one, directly use the formula.

---

## Key Concept

### Gauss's Sum Formula

- Property: `1 + 2 + 3 + ... + n = n × (n + 1) / 2`.
- Why it works: pair the first and last numbers (`1` and `n`), the second and second-last (`2` and `n-1`), and so on. Every pair adds up to the same value, `n + 1`. There are `n / 2` such pairs.
- So the total sum is `(n + 1) × (n / 2)`, which is the same as `n × (n + 1) / 2`.

**Remember:** Pairing numbers from both ends always gives the same sum (`n + 1`). That's why the formula works, so there's no need to add numbers one at a time.

---

## Dry Run

### Example 1: `n = 3`

```text
Sum = (3 × (3 + 1)) // 2
    = (3 × 4) // 2
    = 12 // 2
    = 6
```

**Output:** `6`

---

### Example 2: `n = 5`

```text
Sum = (5 × (5 + 1)) // 2
    = (5 × 6) // 2
    = 30 // 2
    = 15
```

**Output:** `15`

---

## Complexity Analysis

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`