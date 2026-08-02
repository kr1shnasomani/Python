# Approach

## Main Logic

```python
if nums[j] != nums[i]:
    nums[i + 1] = nums[j]
    i += 1
```

- `i` points to the last unique element found.
- `j` scans the array from left to right.
- If `nums[j]` is different from `nums[i]`, we have found a new unique element.
- Place this new element at `i + 1` and move `i` forward.
- At the end, the first `i + 1` elements contain all the unique elements.

**Remember:** `i` builds the answer, while `j` searches for the next unique element.

---

## Flow

```text
i = Last unique element
j = Search for next unique element

        j moves →
[1,1,2,2,3]
 ↑
 i

If nums[j] == nums[i]
        ↓
Skip

If nums[j] != nums[i]
        ↓
Copy nums[j] to i + 1
Move i forward
```

---

## Dry Run

### Example 1

**Input:** `nums = [1,1,2]`

| Step | `i` | `j` | Comparison | Action | Array |
|------|----:|----:|------------|--------|-------|
| Initial | 0 | - | - | `i` starts at first element | `[1,1,2]` |
| 1 | 0 | 1 | `1 == 1` | Skip | `[1,1,2]` |
| 2 | 0 | 2 | `2 != 1` | `nums[1] = 2`, `i = 1` | `[1,2,2]` |

Return `i + 1 = 2`

The first `2` elements are:

```text
[1,2]
```

---

### Example 2

**Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`

| Step | `i` | `j` | Comparison | Action | Array (relevant part) |
|------|----:|----:|------------|--------|------------------------|
| Initial | 0 | - | - | Start | `[0,0,1,1,1,2,2,3,3,4]` |
| 1 | 0 | 1 | `0 == 0` | Skip | `[0,0,1,1,1,2,2,3,3,4]` |
| 2 | 0 | 2 | `1 != 0` | `nums[1]=1`, `i=1` | `[0,1,1,1,1,2,2,3,3,4]` |
| 3 | 1 | 3 | `1 == 1` | Skip | No change |
| 4 | 1 | 4 | `1 == 1` | Skip | No change |
| 5 | 1 | 5 | `2 != 1` | `nums[2]=2`, `i=2` | `[0,1,2,1,1,2,2,3,3,4]` |
| 6 | 2 | 6 | `2 == 2` | Skip | No change |
| 7 | 2 | 7 | `3 != 2` | `nums[3]=3`, `i=3` | `[0,1,2,3,1,2,2,3,3,4]` |
| 8 | 3 | 8 | `3 == 3` | Skip | No change |
| 9 | 3 | 9 | `4 != 3` | `nums[4]=4`, `i=4` | `[0,1,2,3,4,2,2,3,3,4]` |

Return `i + 1 = 5`

The first `5` elements are:

```text
[0,1,2,3,4]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` - We traverse the array only once using two pointers.
- **Space Complexity:** `O(1)` - We modify the array in-place without using any extra space.