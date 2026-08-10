# 12. Maximum Consecutive Ones

Source: `07-Arrays/11-Max-Consecutive-Ones`

## Question

https://leetcode.com/problems/max-consecutive-ones/

Given a binary array `nums`, return the **maximum number of consecutive `1`'s** in the array.

### Example 1

**Input:** `nums = [1,1,0,1,1,1]`
**Output:** `3`

**Explanation:** The first two digits or the last three digits are consecutive `1`s. The maximum number of consecutive `1`s is `3`.

### Example 2

**Input:** `nums = [1,0,1,1,0,1]`
**Output:** `2`

### Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Solution

```python
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    print(Solution().findMaxConsecutiveOnes(nums_input))
```

## Approach

### Main Logic

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

### Dry Run

#### Example 1

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

#### Example 2

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

### Complexity Analysis

- **Time Complexity:** `O(n)` - We traverse the array only once.
- **Space Complexity:** `O(1)` - Only two extra variables (`count` and `max_count`) are used.
