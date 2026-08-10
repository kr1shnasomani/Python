# 23. Search X in Sorted Array

Source: `08-Binary-Search/01-Binary-Search`

## Question

https://leetcode.com/problems/binary-search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:** `nums = [-1,0,3,5,9,12]`, `target = 9`

**Output:** `4`

**Explanation:**  
`9` exists in `nums` and its index is `4`.

### Example 2

**Input:** `nums = [-1,0,3,5,9,12]`, `target = 2`

**Output:** `-1`

**Explanation:**  
`2` does not exist in `nums` so return `-1`.

### Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Solution

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return -1

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the sorted array: ").split()))
    target_input = int(input("Enter the target: "))
    print(Solution().search(nums_input, target_input))
```

## Approach

### Main Logic

```python
mid = (low + high) // 2

if nums[mid] == target:
    return mid
elif nums[mid] > target:
    high = mid - 1
else:
    low = mid + 1
```

- Look at the middle element of the current search range.
- If it's the target, return its index right away.
- If it's bigger than the target, the target can only be in the left half, so move `high` just before `mid`.
- If it's smaller than the target, the target can only be in the right half, so move `low` just after `mid`.
- Keep shrinking the range until `low` crosses `high`. If nothing was found by then, the target isn't in the array.

**Remember:** Every check throws away half of the remaining array, so the search space shrinks fast.

---

### Dry Run

#### Example 1

**Input**

```text
nums = [-1, 0, 3, 5, 9, 12], target = 9
```

| Step | low | high | mid | nums[mid] | Decision |
|------|-----|------|-----|-----------|----------|
| 1 | 0 | 5 | 2 | 3 | 3 < 9 → low = 3 |
| 2 | 3 | 5 | 4 | 9 | 9 == 9 → return 4 |

**Output**

```text
4
```

---

#### Example 2

**Input**

```text
nums = [-1, 0, 3, 5, 9, 12], target = 2
```

| Step | low | high | mid | nums[mid] | Decision |
|------|-----|------|-----|-----------|----------|
| 1 | 0 | 5 | 2 | 3 | 3 > 2 → high = 1 |
| 2 | 0 | 1 | 0 | -1 | -1 < 2 → low = 1 |
| 3 | 1 | 1 | 1 | 0 | 0 < 2 → low = 2 |

`low = 2` is now greater than `high = 1`, so the loop stops and `-1` is returned.

**Output**

```text
-1
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - the search range is cut in half on every step, so it takes about `log n` steps to shrink it down to nothing.
- **Space Complexity:** `O(1)` - only a few pointers are used, no extra space grows with input size.
