# Approach

## Main Logic

```python
expected = n * (n + 1) // 2
return expected - actual
```

- Calculate the sum of all numbers from `0` to `n` using the formula.
- Find the actual sum of the given array.
- The difference between the two sums is the missing number.

**Remember:** **Expected Sum − Actual Sum = Missing Number**.

---

## Dry Run

### Example 1

**Input:** `nums = [3,0,1]`

`n = 3`

Expected sum:

```text
3 × (3 + 1) / 2 = 6
```

Actual sum:

```text
3 + 0 + 1 = 4
```

| Step | Value |
|------|------:|
| Expected Sum | 6 |
| Actual Sum | 4 |
| Missing Number | `6 - 4 = 2` |

**Answer:** `2`

---

### Example 2

**Input:** `nums = [0,1]`

`n = 2`

Expected sum:

```text
2 × (2 + 1) / 2 = 3
```

Actual sum:

```text
0 + 1 = 1
```

| Step | Value |
|------|------:|
| Expected Sum | 3 |
| Actual Sum | 1 |
| Missing Number | `3 - 1 = 2` |

**Answer:** `2`

---

### Example 3

**Input:** `nums = [9,6,4,2,3,5,7,0,1]`

`n = 9`

Expected sum:

```text
9 × (9 + 1) / 2 = 45
```

Actual sum:

```text
9 + 6 + 4 + 2 + 3 + 5 + 7 + 0 + 1 = 37
```

| Step | Value |
|------|------:|
| Expected Sum | 45 |
| Actual Sum | 37 |
| Missing Number | `45 - 37 = 8` |

**Answer:** `8`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` – Calculating the sum of the array takes one traversal.
- **Space Complexity:** `O(1)` – Only two extra variables (`expected` and `actual`) are used.