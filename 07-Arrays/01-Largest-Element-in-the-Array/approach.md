# Approach

## Main Logic

```python
largest = arr[0]

if arr[i] > largest:
    largest = arr[i]
```

- Assume the first element is the largest.
- Traverse the remaining elements one by one.
- If you find a larger element, update `largest`.
- After checking all elements, `largest` will contain the maximum value.

**Remember:** Keep updating the largest element whenever you find a bigger one.

---

## Dry Run

### Example 1

**Input**

```text
arr = [4, 7, 8, 6, 7, 6]
```

| Step | Current Element | Largest So Far | Action |
|------|------------------|----------------|--------|
| Initial | `4` | `4` | Assume first element is the largest |
| 1 | `7` | `7` | Update largest (`7 > 4`) |
| 2 | `8` | `8` | Update largest (`8 > 7`) |
| 3 | `6` | `8` | No change |
| 4 | `7` | `8` | No change |
| 5 | `6` | `8` | No change |

**Output**

```text
8
```

---

### Example 2

**Input**

```text
arr = [5, 9, 3, 4, 8, 4, 3, 10]
```

| Step | Current Element | Largest So Far | Action |
|------|------------------|----------------|--------|
| Initial | `5` | `5` | Assume first element is the largest |
| 1 | `9` | `9` | Update largest (`9 > 5`) |
| 2 | `3` | `9` | No change |
| 3 | `4` | `9` | No change |
| 4 | `8` | `9` | No change |
| 5 | `4` | `9` | No change |
| 6 | `3` | `9` | No change |
| 7 | `10` | `10` | Update largest (`10 > 9`) |

**Output**

```text
10
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` – We traverse the array only once.
- **Space Complexity:** `O(1)` – Only one extra variable (`largest`) is used.