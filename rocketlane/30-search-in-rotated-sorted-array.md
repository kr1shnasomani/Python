# 30. Search in Rotated Sorted Array-I

Source: `08-Binary-Search/08-Search-in-Rotated-Sorted-Array`

## Question

https://leetcode.com/problems/search-in-rotated-sorted-array

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is:

`[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (00-indexed).

For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:** `nums = [4,5,6,7,0,1,2]`, `target = 0`
**Output:** `4`

### Example 2

**Input:** `nums = [4,5,6,7,0,1,2]`, `target = 3`
**Output:** `-1`

### Example 3

**Input:** `nums = [1]`, `target = 0`
**Output:** `-1`

### Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

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

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the rotated sorted array: ").split()))
    target_input = int(input("Enter the target: "))
    print(Solution().search(nums_input, target_input))
```

## Approach

### Main Logic

```python
if nums[low] <= nums[mid]:
    if nums[low] <= target < nums[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    if nums[mid] < target <= nums[high]:
        low = mid + 1
    else:
        high = mid - 1
```

- First check if `nums[mid]` is the target directly. If it is, return `mid` right away.
- Otherwise, figure out which half is sorted. Compare `nums[low]` with `nums[mid]`: if `nums[low] <= nums[mid]`, the left half (`low` to `mid`) is sorted.
- If the left half is sorted, check whether `target` falls inside that sorted range (`nums[low] <= target < nums[mid]`). If yes, search left. If no, `target` must be in the other half, so search right instead.
- If the left half isn't sorted, the right half (`mid` to `high`) must be the sorted one. Check whether `target` falls inside that range (`nums[mid] < target <= nums[high]`). If yes, search right. If no, search left instead.
- Either way, one full half gets eliminated every step, so it still runs in `O(log n)`.

**Remember:** One half around `mid` is always sorted in a rotated array. Check if `target` lies inside that sorted half, if it does, search there, otherwise search the other half.

---

### Key Concept

**Rotated Sorted Array Property**

- A sorted array that's been rotated at some unknown point breaks into two chunks, but each chunk by itself is still sorted internally.
- No matter where `mid` lands, one of the two halves (`low` to `mid`, or `mid` to `high`) is guaranteed to be fully sorted. The "break point" can only exist in one of them.
- Once the sorted half is known, a simple range check tells you whether `target` could be hiding there. If it can't, `target` must be in the other (unsorted-looking) half.
- This "spot the sorted half, then decide which side to search" trick is the foundation for every rotated-array binary search problem.

---

### Dry Run

#### Example 1

**Input**

```text
nums = [4, 5, 6, 7, 0, 1, 2], target = 0
```

| Step | low | high | mid | nums[mid] | Decision | 
|------|-----|------|-----|-----------|----------|
| 1 | 0 | 6 | 3 | 7 | 7 != 0. nums[0]=4 <= nums[3]=7 → left sorted. 4 <= 0 < 7? No → low = 4 |
| 2 | 4 | 6 | 5 | 1 | 1 != 0. nums[4]=0 <= nums[5]=1 → left sorted. 0 <= 0 < 1? Yes → high = 4 |
| 3 | 4 | 4 | 4 | 0 | 0 == 0 → return 4 |

**Output**

```text
4
```

---

#### Example 2

**Input**

```text
nums = [4, 5, 6, 7, 0, 1, 2], target = 3
```

| Step | low | high | mid | nums[mid] | Decision | 
|------|-----|------|-----|-----------|----------|
| 1 | 0 | 6 | 3 | 7 | 7 != 3. nums[0]=4 <= nums[3]=7 → left sorted. 4 <= 3 < 7? No → low = 4 |
| 2 | 4 | 6 | 5 | 1 | 1 != 3. nums[4]=0 <= nums[5]=1 → left sorted. 0 <= 3 < 1? No → low = 6 |
| 3 | 6 | 6 | 6 | 2 | 2 != 3. nums[6]=2 <= nums[6]=2 → left sorted. 2 <= 3 < 2? No → low = 7 |

`low = 7` is now greater than `high = 6`, so the loop stops without ever returning. `target` was never found.

**Output**

```text
-1
```

---

#### Example 3

**Input**

```text
nums = [1], target = 0
```

| Step | low | high | mid | nums[mid] | Decision | 
|------|-----|------|-----|-----------|----------|
| 1 | 0 | 0 | 0 | 1 | 1 != 0. nums[0]=1 <= nums[0]=1 → left sorted. 1 <= 0 < 1? No → low = 1 |

`low = 1` is now greater than `high = 0`, so the loop stops without ever returning.

**Output**

```text
-1
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - each step still throws away one full half of the search range, exactly like regular binary search.
- **Space Complexity:** `O(1)` - only a few pointers are used, no extra space grows with input size.
