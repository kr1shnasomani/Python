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