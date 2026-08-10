# 26. Search Insert Position

Source: `08-Binary-Search/04-Search-Insert-Position`

## Question

https://leetcode.com/problems/search-insert-position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:** `nums = [1,3,5,6]`, `target = 5`
**Output:** `2`

### Example 2

**Input:** `nums = [1,3,5,6]`, `target = 2`
**Output:** `1`

### Example 3

**Input:** `nums = [1,3,5,6]`, `target = 7`
**Output:** `4`

### Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

## Solution

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

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

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the sorted array: ").split()))
    target_input = int(input("Enter the target: "))
    print(Solution().searchInsert(nums_input, target_input))
```

## Approach

### Main Logic

```python
if nums[mid] >= target:
    ans = mid
    high = mid - 1
else:
    low = mid + 1
```

- This is the lower bound idea: shrink the range like binary search, but instead of stopping at an exact match, look for the smallest index where `nums[mid] >= target`.
- Whenever `nums[mid] >= target`, that index could be the answer (either `target` sits there, or `target` would need to be inserted there), so save it in `ans` and keep searching left for an even smaller valid index.
- Whenever `nums[mid] < target`, this index is too small, so search the right half instead.
- `ans` starts at `n`, so if `target` is bigger than every element, it correctly falls back to `n` (insert at the very end).

**Remember:** Whether `target` is found or not, the smallest index where `nums[mid] >= target` is exactly where it belongs, found or inserted.

---

### Dry Run

#### Example 1

**Input**

```text
nums = [1, 3, 5, 6], target = 5
```

| Step | low | high | mid | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|----------|-----|
| 1 | 0 | 3 | 1 | 3 | 3 >= 5? No → low = 2 | 4 |
| 2 | 2 | 3 | 2 | 5 | 5 >= 5 → ans = 2, high = 1 | 2 |

`low = 2` is now greater than `high = 1`, so the loop stops.

**Output**

```text
2
```

---

#### Example 2

**Input**

```text
nums = [1, 3, 5, 6], target = 2
```

| Step | low | high | mid | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|----------|-----|
| 1 | 0 | 3 | 1 | 3 | 3 >= 2 → ans = 1, high = 0 | 1 |
| 2 | 0 | 0 | 0 | 1 | 1 >= 2? No → low = 1 | 1 |

`low = 1` is now greater than `high = 0`, so the loop stops.

**Output**

```text
1
```

---

#### Example 3

**Input**

```text
nums = [1, 3, 5, 6], target = 7
```

| Step | low | high | mid | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|----------|-----|
| 1 | 0 | 3 | 1 | 3 | 3 >= 7? No → low = 2 | 4 |
| 2 | 2 | 3 | 2 | 5 | 5 >= 7? No → low = 3 | 4 |
| 3 | 3 | 3 | 3 | 6 | 6 >= 7? No → low = 4 | 4 |

`low = 4` is now greater than `high = 3`, so the loop stops. Since no index ever satisfied `nums[mid] >= target`, `ans` stays at its starting value, `n = 4`.

**Output**

```text
4
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - the search range is cut in half every step, just like regular binary search.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used, no extra space grows with input size.
