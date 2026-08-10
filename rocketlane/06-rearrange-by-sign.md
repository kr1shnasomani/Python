# 6. Rearrange Array Elements by Sign

Source: `07-Arrays/21-Rearrange-Array-Elements-by-Sign`

## Question

https://leetcode.com/problems/rearrange-array-elements-by-sign

You are given a **0-indexed** integer array `nums` of **even** length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in `nums` is preserved.
3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

### Example 1

**Input:** `nums = [3,1,-2,-5,2,-4]`  
**Output:** `[3,-2,1,-5,2,-4]`

**Explanation:**  
The positive integers in `nums` are `[3,1,2]`. The negative integers are `[-2,-5,-4]`.  
The only possible way to rearrange them such that they satisfy all conditions is `[3,-2,1,-5,2,-4]`.  
Other ways such as `[1,-2,2,-5,3,-4]`, `[3,1,2,-2,-5,-4]`, `[-2,3,-5,1,-4,2]` are incorrect because they do not satisfy one or more conditions.

### Example 2

**Input:** `nums = [-1,1]`  
**Output:** `[1,-1]`

**Explanation:**  
`1` is the only positive integer and `-1` the only negative integer in `nums`.  
So `nums` is rearranged to `[1,-1]`.

## Solution

```python
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        positive = 0
        negative = 1

        for num in nums:
            if num > 0:
                ans[positive] = num
                positive += 2
            else:
                ans[negative] = num
                negative += 2

        return ans

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    print(Solution().rearrangeArray(nums_input))
```

## Approach

### Main Logic

```python
if num > 0:
    ans[positive] = num
    positive += 2
else:
    ans[negative] = num
    negative += 2
```

- We make a new empty array called `ans`, the same size as `nums`.
- We use two pointers. `positive` starts at index `0`. `negative` starts at index `1`.
- If the current number is positive, we place it at the `positive` index, then move `positive` forward by `2`.
- If the current number is negative, we place it at the `negative` index, then move `negative` forward by `2`.
- Moving each pointer by `2` means positive numbers always land on even indexes (`0, 2, 4...`) and negative numbers always land on odd indexes (`1, 3, 5...`). That is what creates the alternating pattern.

**Remember:** Positive numbers go to even spots, negative numbers go to odd spots, and moving each pointer by `2` keeps them out of each other's way.

---

### Dry Run

#### Example 1

**Input:** `nums = [3,1,-2,-5,2,-4]`

| i | nums[i] | Sign | Action | positive | negative | ans (after) |
|---:|---:|:---:|---|---:|---:|---|
| Initial | - | - | Start | 0 | 1 | `[0,0,0,0,0,0]` |
| 0 | 3 | positive | `ans[0] = 3`, positive becomes 2 | 2 | 1 | `[3,0,0,0,0,0]` |
| 1 | 1 | positive | `ans[2] = 1`, positive becomes 4 | 4 | 1 | `[3,0,1,0,0,0]` |
| 2 | -2 | negative | `ans[1] = -2`, negative becomes 3 | 4 | 3 | `[3,-2,1,0,0,0]` |
| 3 | -5 | negative | `ans[3] = -5`, negative becomes 5 | 4 | 5 | `[3,-2,1,-5,0,0]` |
| 4 | 2 | positive | `ans[4] = 2`, positive becomes 6 | 6 | 5 | `[3,-2,1,-5,2,0]` |
| 5 | -4 | negative | `ans[5] = -4`, negative becomes 7 | 6 | 7 | `[3,-2,1,-5,2,-4]` |

**Output:** `[3,-2,1,-5,2,-4]`

---

#### Example 2

**Input:** `nums = [-1,1]`

| i | nums[i] | Sign | Action | positive | negative | ans (after) |
|---:|---:|:---:|---|---:|---:|---|
| Initial | - | - | Start | 0 | 1 | `[0,0]` |
| 0 | -1 | negative | `ans[1] = -1`, negative becomes 3 | 0 | 3 | `[0,-1]` |
| 1 | 1 | positive | `ans[0] = 1`, positive becomes 2 | 2 | 3 | `[1,-1]` |

**Output:** `[1,-1]`

---

### Complexity Analysis

- **Time Complexity:** `O(n)` - We go through `nums` only once.
- **Space Complexity:** `O(n)` - We build a new array `ans` that is the same size as `nums`.
