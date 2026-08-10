# 28. First and Last Occurrence

Source: `08-Binary-Search/06-Find-First-and-Last-Position-of-Element-in-Sorted-Array`

## Question

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:** `nums = [5,7,7,8,8,10]`, `target = 8`
**Output:** `[3,4]`

### Example 2

**Input:** `nums = [5,7,7,8,8,10]`, `target = 6`
**Output:** `[-1,-1]`

### Example 3

**Input:** `nums = []`, `target = 0`
**Output:** `[-1,-1]`

### Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Solution

```python
from typing import List

class Solution:
    def lowerBound(self, nums: List[int], n: int, target: int) -> int:
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def upperBound(self, nums: List[int], n: int, target: int) -> int:
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        lb = self.lowerBound(nums, n, target)
        ub = self.upperBound(nums, n, target)

        if lb == n or nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the sorted array: ").split()))
    target_input = int(input("Enter the target: "))
    print(Solution().searchRange(nums_input, target_input))
```

## Approach

### Main Logic

```python
lb = self.lowerBound(nums, n, target)
ub = self.upperBound(nums, n, target)

if lb == n or nums[lb] != target:
    return [-1, -1]

return [lb, ub - 1]
```

- `lowerBound` finds the smallest index where `nums[mid] >= target`. If `target` exists, this is exactly where its first occurrence starts.
- `upperBound` finds the smallest index where `nums[mid] > target`. This lands one position past `target`'s last occurrence.
- `lb` might point at an index that doesn't actually hold `target` (it could be `n`, meaning nothing is `>= target`, or it could hold some bigger value). Either way `target` isn't in the array, so return `[-1, -1]`.
- Otherwise `target` really is in the array: the first occurrence is at `lb`, and the last occurrence is right before `ub`, so `ub - 1`.

**Remember:** First occurrence = lower bound index. Last occurrence = upper bound index minus one. Always check `nums[lb] == target` before trusting the range.

---

### Dry Run

#### Example 1

**Input**

```text
nums = [5, 7, 7, 8, 8, 10], target = 8
```

**Lower bound search**

| Step | low | high | mid | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|----------|-----|
| 1 | 0 | 5 | 2 | 7 | 7 >= 8? No → low = 3 | 6 |
| 2 | 3 | 5 | 4 | 8 | 8 >= 8 → ans = 4, high = 3 | 4 |
| 3 | 3 | 3 | 3 | 8 | 8 >= 8 → ans = 3, high = 2 | 3 |

`low = 3` is now greater than `high = 2`, so the loop stops. `lb = 3`.

**Upper bound search**

| Step | low | high | mid | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|----------|-----|
| 1 | 0 | 5 | 2 | 7 | 7 > 8? No → low = 3 | 6 |
| 2 | 3 | 5 | 4 | 8 | 8 > 8? No → low = 5 | 6 |
| 3 | 5 | 5 | 5 | 10 | 10 > 8 → ans = 5, high = 4 | 5 |

`low = 5` is now greater than `high = 4`, so the loop stops. `ub = 5`.

**Range check:** `lb = 3` is not `n = 6`, and `nums[3] = 8` equals `target`, so the range is valid: `[lb, ub - 1] = [3, 4]`.

**Output**

```text
[3, 4]
```

---

#### Example 2

**Input**

```text
nums = [5, 7, 7, 8, 8, 10], target = 6
```

**Lower bound search**

| Step | low | high | mid | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|----------|-----|
| 1 | 0 | 5 | 2 | 7 | 7 >= 6 → ans = 2, high = 1 | 2 |
| 2 | 0 | 1 | 0 | 5 | 5 >= 6? No → low = 1 | 2 |
| 3 | 1 | 1 | 1 | 7 | 7 >= 6 → ans = 1, high = 0 | 1 |

`low = 1` is now greater than `high = 0`, so the loop stops. `lb = 1`.

**Range check:** `lb = 1` is not `n = 6`, but `nums[1] = 7` does not equal `target = 6`. So `target` isn't actually in the array.

**Output**

```text
[-1, -1]
```

---

#### Example 3

**Input**

```text
nums = [], target = 0
```

Here `n = 0`, so `low = 0` and `high = n - 1 = -1` right from the start. Since `low <= high` (`0 <= -1`) is already false, both `lowerBound` and `upperBound` skip their loops entirely and return `ans` unchanged, `lb = 0` and `ub = 0`.

**Range check:** `lb = 0` equals `n = 0`, so `target` cannot be in the array.

**Output**

```text
[-1, -1]
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - lower bound and upper bound are two independent binary searches, each `O(log n)`, run one after another.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used in each search, no extra space grows with input size.
