# 10. Move Zeros to End

Source: `07-Arrays/07-Move-Zeroes`

## Question

https://leetcode.com/problems/move-zeroes

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this **in-place** without making a copy of the array.

### Example 1

**Input:** `nums = [0,1,0,3,12]`

**Output:** `[1,3,12,0,0]`

### Example 2

**Input:** `nums = [0]`

**Output:** `[0]`

### Constraints

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Solution

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    print(Solution().moveZeroes(nums_input))
```

## Approach

### Main Logic

```python
if nums[i] != 0:
    nums[i], nums[j] = nums[j], nums[i]
    j += 1
```

- `i` scans every element in the array.
- `j` points to the position where the next non-zero element should be placed.
- Whenever a non-zero element is found, swap it with the element at `j`.
- After the swap, move `j` forward.
- By the end, all non-zero elements are at the front in the same order, and all zeros automatically move to the end.

**Remember:** `i` searches for non-zero elements, while `j` builds the array without zeros.

---

### Dry Run

#### Example 1

**Input:** `nums = [0,1,0,3,12]`

| Step | `i` | `j` | Current Element | Action | Array |
|------|----:|----:|----------------:|--------|-------|
| Initial | - | 0 | - | Start | `[0,1,0,3,12]` |
| 1 | 0 | 0 | 0 | Skip | `[0,1,0,3,12]` |
| 2 | 1 | 0 | 1 | Swap `nums[1]` and `nums[0]`, `j = 1` | `[1,0,0,3,12]` |
| 3 | 2 | 1 | 0 | Skip | `[1,0,0,3,12]` |
| 4 | 3 | 1 | 3 | Swap `nums[3]` and `nums[1]`, `j = 2` | `[1,3,0,0,12]` |
| 5 | 4 | 2 | 12 | Swap `nums[4]` and `nums[2]`, `j = 3` | `[1,3,12,0,0]` |

**Answer:** `[1,3,12,0,0]`

---

#### Example 2

**Input:** `nums = [0]`

| Step | `i` | `j` | Current Element | Action | Array |
|------|----:|----:|----------------:|--------|-------|
| Initial | - | 0 | - | Start | `[0]` |
| 1 | 0 | 0 | 0 | Skip | `[0]` |

**Answer:** `[0]`

---

### Complexity Analysis

- **Time Complexity:** `O(n)` - We traverse the array only once.
- **Space Complexity:** `O(1)` - The array is modified in-place using only one extra pointer (`j`).
