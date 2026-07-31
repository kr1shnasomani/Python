# Approach

## Main Logic

```python
if num == 1:
    count += 1
    max_count = max(max_count, count)
else:
    count = 0
```

- Traverse the array one element at a time.
- If the current element is `1`, increase the current streak.
- If the current element is `0`, the streak breaks, so reset the count to `0`.
- Keep updating the maximum streak seen so far.

**Remember:** `count` stores the **current streak**, while `max_count` stores the **longest streak** found.

---

## Dry Run

### Example 1

**Input:** `nums = [1,1,0,1,1,1]`

| Step | Current Number | `count` | `max_count` | Action |
|------|---------------:|--------:|------------:|--------|
| Initial | - | 0 | 0 | Start |
| 1 | 1 | 1 | 1 | Increase streak |
| 2 | 1 | 2 | 2 | Increase streak |
| 3 | 0 | 0 | 2 | Reset streak |
| 4 | 1 | 1 | 2 | Increase streak |
| 5 | 1 | 2 | 2 | Increase streak |
| 6 | 1 | 3 | 3 | Increase streak |

**Answer:** `3`

---

### Example 2

**Input:** `nums = [1,0,1,1,0,1]`

| Step | Current Number | `count` | `max_count` | Action |
|------|---------------:|--------:|------------:|--------|
| Initial | - | 0 | 0 | Start |
| 1 | 1 | 1 | 1 | Increase streak |
| 2 | 0 | 0 | 1 | Reset streak |
| 3 | 1 | 1 | 1 | Increase streak |
| 4 | 1 | 2 | 2 | Increase streak |
| 5 | 0 | 0 | 2 | Reset streak |
| 6 | 1 | 1 | 2 | Increase streak |

**Answer:** `2`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` – We traverse the array only once.
- **Space Complexity:** `O(1)` – Only two extra variables (`count` and `max_count`) are used.