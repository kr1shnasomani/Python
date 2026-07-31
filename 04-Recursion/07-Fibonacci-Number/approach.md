# Approach

## Main Logic

```python
result = self.fib(n - 1) + self.fib(n - 2)
```

- If `n` is `0` or `1`, return `n` because these are the base Fibonacci numbers.
- Otherwise, find the previous two Fibonacci numbers recursively.
- Add them together to get the current Fibonacci number.
- The recursion continues until every call reaches the base case.

**Remember:** Every Fibonacci number is the **sum of the previous two Fibonacci numbers**, so we must calculate both `fib(n-1)` and `fib(n-2)`.

---

## Key Concept

### Overlapping Subproblems

- This recursive solution recalculates the same smaller Fibonacci numbers again and again. For example, `fib(5)` calls `fib(3)` twice, `fib(2)` three times, and so on.
- Property: the number of recursive calls roughly doubles with every increase in `n`, giving `O(2ⁿ)` time. This branching pattern is called an exponential recursion tree.
- Why it's slow: none of the repeated work is reused; each call redoes the same calculation from scratch.

**Remember:** This naive version is correct but slow because of repeated work. Later on, memoization/DP techniques store already-computed results so the same subproblem is never solved twice.

---

## Dry Run

### Example 1

**Input:** `n = 2`

```text
fib(2)
= fib(1) + fib(0)

= 1 + 0

= 1
```

**Output:**

```text
1
```

---

### Example 2

**Input:** `n = 3`

```text
fib(3)
= fib(2) + fib(1)

= (fib(1) + fib(0)) + 1

= (1 + 0) + 1

= 2
```

**Output:**

```text
2
```

---

### Example 3

**Input:** `n = 4`

```text
fib(4)
= fib(3) + fib(2)

= (fib(2) + fib(1)) + fib(2)

= ((fib(1) + fib(0)) + 1) + (fib(1) + fib(0))

= ((1 + 0) + 1) + (1 + 0)

= (1 + 1) + 1

= 2 + 1

= 3
```

**Output:**

```text
3
```

---

## Complexity Analysis

- **Time Complexity:** `O(2ⁿ)` (the same Fibonacci numbers are calculated repeatedly)
- **Space Complexity:** `O(n)` (recursive call stack)