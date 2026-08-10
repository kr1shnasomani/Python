# 14. Highest Occurring Element in an Array

Source: `05-Hashing/03-Frequency-of-the-Most-Frequent-Element`

## Question

https://leetcode.com/problems/frequency-of-the-most-frequent-element/

## Problem Statement

The **frequency** of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return the **maximum possible frequency** of an element after performing **at most** `k` operations.

### Example 1

```text
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
```

### Example 2

```text
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
```

### Example 3

```text
Input: nums = [3,9,6], k = 2
Output: 1
```

### Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

## Solution

```python
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        total = 0
        result = 0

        for right in range(len(nums)):
            total = total + nums[right]

            while nums[right] * (right - left + 1) - total > k:
                total = total - nums[left]
                left = left + 1

            result = max(result, right - left + 1)

        return result

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    k_input = int(input("Enter k: "))
    print(Solution().maxFrequency(nums_input, k_input))
```

## Approach

### Main Logic

```python
while nums[right] * (right - left + 1) - total > k:
    total = total - nums[left]
    left = left + 1

result = max(result, right - left + 1)
```

- Sort the array first. Once sorted, the cheapest way to make a group of numbers equal is to raise every one of them up to the largest number in that group, `nums[right]`.
- For the current window `[left, right]`, the number of increments needed to raise everyone up to `nums[right]` is `nums[right] * window_size - total`, where `total` is the sum of the elements currently inside the window.
- If that cost is more than `k`, the window is too expensive. Shrink it from the left (subtract `nums[left]` from `total`, move `left` forward) until it becomes affordable again.
- Once the window is affordable, its size (`right - left + 1`) is a valid candidate for the answer, keep the largest one seen so far.

**Remember:** Sort first, then slide a window and keep shrinking from the left whenever "cost to raise everyone to the window's max" goes over the budget `k`.

---

### Key Concept

**Sliding Window with a Running Sum**

- A sliding window is a range `[left, right]` that expands and shrinks over the array instead of restarting from scratch every time.
- Instead of recomputing the sum of the window from zero at every step, keep a running `total` that updates by just adding or removing one element at a time as the window moves. That keeps each step `O(1)` instead of `O(window size)`.
- The window only ever grows from the right and shrinks from the left, both pointers only move forward, they never go backward. That's what keeps the whole scan `O(n)` instead of `O(n^2)`.
- This pattern shows up whenever you're looking for the best (largest, smallest, cheapest) contiguous range that satisfies some running condition, here the condition is "cost to equalize the window is within budget `k`".

---

### Dry Run

#### Example 1

**Input**

```text
nums = [1, 2, 4], k = 5
```

Sorted: `[1, 2, 4]` (already sorted)

| right | nums[right] | total | window size | cost = nums[right]*size - total | cost > k? | left | result |
|-------|-------------|-------|-------------|-----------------------------------|-----------|------|--------|
| 0 | 1 | 1 | 1 | 1*1 - 1 = 0 | No | 0 | 1 |
| 1 | 2 | 3 | 2 | 2*2 - 3 = 1 | No | 0 | 2 |
| 2 | 4 | 7 | 3 | 4*3 - 7 = 5 | No | 0 | 3 |

**Output**

```text
3
```

---

#### Example 2

**Input**

```text
nums = [1, 4, 8, 13], k = 5
```

Sorted: `[1, 4, 8, 13]` (already sorted)

| right | nums[right] | total (before shrink) | window (before shrink) | cost | cost > k? | Shrink | total (after) | window (after) | result |
|-------|-------------|-------------------------|--------------------------|------|-----------|--------|----------------|------------------|--------|
| 0 | 1 | 1 | [0,0] size 1 | 1*1-1=0 | No | - | 1 | [0,0] size 1 | 1 |
| 1 | 4 | 5 | [0,1] size 2 | 4*2-5=3 | No | - | 5 | [0,1] size 2 | 2 |
| 2 | 8 | 13 | [0,2] size 3 | 8*3-13=11 | Yes | total=13-1=12, left=1 | 12 | [1,2] size 2, cost=8*2-12=4 (≤ k, stop) | 2 |
| 3 | 13 | 25 | [1,3] size 3 | 13*3-25=14 | Yes | total=25-4=21, left=2 | 21 | [2,3] size 2, cost=13*2-21=5 (≤ k, stop) | 2 |

**Output**

```text
2
```

---

#### Example 3

**Input**

```text
nums = [3, 9, 6], k = 2
```

Sorted: `[3, 6, 9]`

| right | nums[right] | total (before shrink) | window (before shrink) | cost | cost > k? | Shrink | total (after) | window (after) | result |
|-------|-------------|-------------------------|--------------------------|------|-----------|--------|----------------|------------------|--------|
| 0 | 3 | 3 | [0,0] size 1 | 3*1-3=0 | No | - | 3 | [0,0] size 1 | 1 |
| 1 | 6 | 9 | [0,1] size 2 | 6*2-9=3 | Yes | total=9-3=6, left=1 | 6 | [1,1] size 1, cost=6*1-6=0 (≤ k, stop) | 1 |
| 2 | 9 | 15 | [1,2] size 2 | 9*2-15=3 | Yes | total=15-6=9, left=2 | 9 | [2,2] size 1, cost=9*1-9=0 (≤ k, stop) | 1 |

**Output**

```text
1
```

---

### Complexity Analysis

- **Time Complexity:** `O(n log n)` - dominated by sorting the array, the sliding window itself is `O(n)` since `left` and `right` each move forward at most `n` times.
- **Space Complexity:** `O(1)` - only a running sum, two pointers, and a result variable are used, no extra space grows with input size (ignoring the in-place sort).
