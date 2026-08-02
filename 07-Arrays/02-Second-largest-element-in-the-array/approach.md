# Approach

## Main Logic

```python
if num > largest:
    slargest = largest
    largest = num
elif num > slargest and num != largest:
    slargest = num
```

- Keep track of the **largest** and **second largest** numbers while traversing the array only once.
- If the current number is greater than the largest, the old largest becomes the second largest.
- Otherwise, if the current number is smaller than the largest but greater than the second largest, update the second largest.
- If the second largest never gets updated, return `-1`.

**Remember:** Whenever the largest changes, the previous largest automatically becomes the second largest.

---

## Dry Run

### Example 1

**Input:** `[2, 4, 5, 6, 8]`

| Step | Current Number | Largest | Second Largest | Action |
|------|----------------|---------|----------------|--------|
| Initial | - | `-∞` | `-∞` | Initialize both variables |
| 1 | 2 | 2 | `-∞` | New largest found |
| 2 | 4 | 4 | 2 | Old largest becomes second largest |
| 3 | 5 | 5 | 4 | Old largest becomes second largest |
| 4 | 6 | 6 | 5 | Old largest becomes second largest |
| 5 | 8 | 8 | 6 | Old largest becomes second largest |

**Answer:** `6`

---

### Sample Input 1 - Test Case 1

**Input:** `[12, 1, 35, 10, 34, 1]`

| Step | Current Number | Largest | Second Largest | Action |
|------|----------------|---------|----------------|--------|
| Initial | - | `-∞` | `-∞` | Initialize |
| 1 | 12 | 12 | `-∞` | New largest |
| 2 | 1 | 12 | 1 | Update second largest |
| 3 | 35 | 35 | 12 | Old largest becomes second largest |
| 4 | 10 | 35 | 12 | No change |
| 5 | 34 | 35 | 34 | Update second largest |
| 6 | 1 | 35 | 34 | No change |

**Answer:** `34`

---

### Sample Input 1 - Test Case 2

**Input:** `[10, 10, 10, 10, 10]`

| Step | Current Number | Largest | Second Largest | Action |
|------|----------------|---------|----------------|--------|
| Initial | - | `-∞` | `-∞` | Initialize |
| 1 | 10 | 10 | `-∞` | New largest |
| 2 | 10 | 10 | `-∞` | Duplicate largest, ignore |
| 3 | 10 | 10 | `-∞` | Duplicate largest, ignore |
| 4 | 10 | 10 | `-∞` | Duplicate largest, ignore |
| 5 | 10 | 10 | `-∞` | Duplicate largest, ignore |

`slargest` is still `-∞`, so return **`-1`**.

**Answer:** `-1`

---

### Sample Input 2

**Input:** `[7, 8, 8, 1, 4, 3]`

| Step | Current Number | Largest | Second Largest | Action |
|------|----------------|---------|----------------|--------|
| Initial | - | `-∞` | `-∞` | Initialize |
| 1 | 7 | 7 | `-∞` | New largest |
| 2 | 8 | 8 | 7 | Old largest becomes second largest |
| 3 | 8 | 8 | 7 | Duplicate largest, ignore |
| 4 | 1 | 8 | 7 | No change |
| 5 | 4 | 8 | 7 | No change |
| 6 | 3 | 8 | 7 | No change |

**Answer:** `7`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` - We traverse the array only once.
- **Space Complexity:** `O(1)` - Only two extra variables (`largest` and `slargest`) are used.