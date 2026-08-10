# 11. Find Missing Number

Source: `07-Arrays/10-Missing-Number`

## Question

https://leetcode.com/problems/missing-number

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the **only number** in the range that is missing from the array.

### Example 1

**Input:** `nums = [3,0,1]`
**Output:** `2`

**Explanation:**

`n = 3` since there are `3` numbers, so all numbers are in the range `[0,3]`. `2` is the missing number in the range since it does not appear in `nums`.

### Example 2

**Input:** `nums = [0,1]`
**Output:** `2`

**Explanation:**

`n = 2` since there are `2` numbers, so all numbers are in the range `[0,2]`. `2` is the missing number in the range since it does not appear in `nums`.

### Example 3

**Input:** `nums = [9,6,4,2,3,5,7,0,1]`
**Output:** `8`

**Explanation:**

`n = 9` since there are `9` numbers, so all numbers are in the range `[0,9]`. `8` is the missing number in the range since it does not appear in `nums`.

## Solution

```python
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    print(Solution().missingNumber(nums_input))
```

## Approach

### Main Logic

```python
expected = n * (n + 1) // 2
return expected - actual
```

- Calculate the sum of all numbers from `0` to `n` using the formula.
- Find the actual sum of the given array.
- The difference between the two sums is the missing number.

**Remember:** **Expected Sum − Actual Sum = Missing Number**.

---

### Dry Run

#### Example 1

**Input:** `nums = [3,0,1]`

`n = 3`

Expected sum:

```text
3 × (3 + 1) / 2 = 6
```

Actual sum:

```text
3 + 0 + 1 = 4
```

| Step | Value |
|------|------:|
| Expected Sum | 6 |
| Actual Sum | 4 |
| Missing Number | `6 - 4 = 2` |

**Answer:** `2`

---

#### Example 2

**Input:** `nums = [0,1]`

`n = 2`

Expected sum:

```text
2 × (2 + 1) / 2 = 3
```

Actual sum:

```text
0 + 1 = 1
```

| Step | Value |
|------|------:|
| Expected Sum | 3 |
| Actual Sum | 1 |
| Missing Number | `3 - 1 = 2` |

**Answer:** `2`

---

#### Example 3

**Input:** `nums = [9,6,4,2,3,5,7,0,1]`

`n = 9`

Expected sum:

```text
9 × (9 + 1) / 2 = 45
```

Actual sum:

```text
9 + 6 + 4 + 2 + 3 + 5 + 7 + 0 + 1 = 37
```

| Step | Value |
|------|------:|
| Expected Sum | 45 |
| Actual Sum | 37 |
| Missing Number | `45 - 37 = 8` |

**Answer:** `8`

---

### Complexity Analysis

- **Time Complexity:** `O(n)` - Calculating the sum of the array takes one traversal.
- **Space Complexity:** `O(1)` - Only two extra variables (`expected` and `actual`) are used.
