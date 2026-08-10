# 1. Two Sum

Source: `07-Arrays/15-Two-Sum`

## Question

https://leetcode.com/problems/two-sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the **same element twice**.

You can return the answer in any order.

### Example 1

**Input:** `nums = [2,7,11,15]`, `target = 9`

**Output:** `[0,1]`

**Explanation:**  
Because `nums[0] + nums[1] == 9`, we return `[0,1]`.

### Example 2

**Input:** `nums = [3,2,4]`, `target = 6`

**Output:** `[1,2]`

### Example 3

**Input:** `nums = [3,3]`, `target = 6`

**Output:** `[0,1]`

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Solution

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    target_input = int(input("Enter the target: "))
    print(Solution().twoSum(nums_input, target_input))
```

## Approach

### Main Logic

```python
if nums[i] + nums[j] == target:
    return [i, j]
```

- Pick one number using `i`.
- Check it with every number after it using `j`.
- If their sum equals the target, return their indices immediately.
- `j` starts from `i + 1` so the same element is never used twice.

**Remember:** Compare every unique pair until you find the pair whose sum equals the target.

---

### Flow

![alt text](images/01-two-sum-image1.png)

---

### Dry Run

#### Example 1

**Input:** `nums = [2,7,11,15]`, `target = 9`

| `i` | `j` | Pair | Sum | Matches Target? |
|:---:|:---:|:----:|:---:|:---------------:|
| 0 | 1 | `(2, 7)` | 9 | ✅ Yes |

Return:

```text
[0, 1]
```

---

#### Example 2

**Input:** `nums = [3,2,4]`, `target = 6`

| `i` | `j` | Pair | Sum | Matches Target? |
|:---:|:---:|:----:|:---:|:---------------:|
| 0 | 1 | `(3, 2)` | 5 | ❌ No |
| 0 | 2 | `(3, 4)` | 7 | ❌ No |
| 1 | 2 | `(2, 4)` | 6 | ✅ Yes |

Return:

```text
[1, 2]
```

---

#### Example 3

**Input:** `nums = [3,3]`, `target = 6`

| `i` | `j` | Pair | Sum | Matches Target? |
|:---:|:---:|:----:|:---:|:---------------:|
| 0 | 1 | `(3, 3)` | 6 | ✅ Yes |

Return:

```text
[0, 1]
```

---

### Complexity Analysis

- **Time Complexity:** `O(n²)` - In the worst case, every pair of elements is checked.
- **Space Complexity:** `O(1)` - No extra data structure is used.
