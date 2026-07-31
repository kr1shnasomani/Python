# Approach

## Main Logic

```python
if arr[i] == num:
    return i
```

- Check each element one by one.
- If the current element matches the target, return its index immediately.
- If no match is found after checking the entire array, return `-1`.

**Remember:** Linear Search stops as soon as it finds the **first occurrence** of the target.

---

## Dry Run

### Example

**Input:** `n = 5`, `num = 4`

`arr = [6,7,8,4,1]`

| Step | Index (`i`) | `arr[i]` | Match? | Action |
|------|------------:|---------:|--------|--------|
| 1 | 0 | 6 | ❌ | Move to next element |
| 2 | 1 | 7 | ❌ | Move to next element |
| 3 | 2 | 8 | ❌ | Move to next element |
| 4 | 3 | 4 | ✅ | Return `3` |

**Answer:** `3`

---

### Sample Input 1

**Input:** `n = 5`, `num = 4`

`arr = [6,7,8,4,1]`

| Step | Index (`i`) | `arr[i]` | Match? | Action |
|------|------------:|---------:|--------|--------|
| 1 | 0 | 6 | ❌ | Move to next element |
| 2 | 1 | 7 | ❌ | Move to next element |
| 3 | 2 | 8 | ❌ | Move to next element |
| 4 | 3 | 4 | ✅ | Return `3` |

**Answer:** `3`

---

### Sample Input 2

**Input:** `n = 4`, `num = 2`

`arr = [2,5,6,2]`

| Step | Index (`i`) | `arr[i]` | Match? | Action |
|------|------------:|---------:|--------|--------|
| 1 | 0 | 2 | ✅ | Return `0` |

**Answer:** `0`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` – In the worst case, we may have to check every element once.
- **Space Complexity:** `O(1)` – No extra space is used apart from a few variables.