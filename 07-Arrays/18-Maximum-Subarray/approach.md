# Approach

## Main Logic

```python
if current_sum < 0:
    current_sum = nums[i]
else:
    current_sum = current_sum + nums[i]

if current_sum > max_sum:
    max_sum = current_sum
```

- If the running sum (`current_sum`) has dropped below zero, it can only drag future sums down, so restart it from the current element instead.
- Otherwise, extend the running sum by adding the current element to it.
- After updating, check if this running sum beats the best sum seen so far (`max_sum`), and update it if so.

**Remember:** A negative running sum only hurts what comes next, so throw it away and restart instead of carrying it forward.

---

## Key Concept

### Kadane's Algorithm

- Property: the best subarray ending at each position is either the current element alone, or the current element added to the best subarray ending at the previous position, whichever is larger.
- Why it works: once the running sum goes negative, adding it to future elements only makes those future sums smaller. So the moment it turns negative, it's better to drop it and start fresh from the current element.
- This finds the best subarray in a single left-to-right pass, tracking just two numbers: the running sum and the overall best seen so far.

**Remember:** Kadane's algorithm asks one question at every step: does carrying forward the previous sum help, or should I start fresh here?

---

## Dry Run

### Example 1

**Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`

| i | nums[i] | current_sum (before) | current_sum < 0? | current_sum (after) | max_sum |
|---:|---:|---:|:---:|---:|---:|
| Initial | - | - | - | -2 | -2 |
| 1 | 1 | -2 | Yes → restart | 1 | 1 |
| 2 | -3 | 1 | No → extend | -2 | 1 |
| 3 | 4 | -2 | Yes → restart | 4 | 4 |
| 4 | -1 | 4 | No → extend | 3 | 4 |
| 5 | 2 | 3 | No → extend | 5 | 5 |
| 6 | 1 | 5 | No → extend | 6 | 6 |
| 7 | -5 | 6 | No → extend | 1 | 6 |
| 8 | 4 | 1 | No → extend | 5 | 6 |

**Output:** `6`

---

### Example 2

**Input:** `nums = [1]`

| i | nums[i] | current_sum (before) | current_sum < 0? | current_sum (after) | max_sum |
|---:|---:|---:|:---:|---:|---:|
| Initial | - | - | - | 1 | 1 |

The array has only one element, so the loop never runs.

**Output:** `1`

---

### Example 3

**Input:** `nums = [5,4,-1,7,8]`

| i | nums[i] | current_sum (before) | current_sum < 0? | current_sum (after) | max_sum |
|---:|---:|---:|:---:|---:|---:|
| Initial | - | - | - | 5 | 5 |
| 1 | 4 | 5 | No → extend | 9 | 9 |
| 2 | -1 | 9 | No → extend | 8 | 9 |
| 3 | 7 | 8 | No → extend | 15 | 15 |
| 4 | 8 | 15 | No → extend | 23 | 23 |

**Output:** `23`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` - We scan the array once, doing constant work at each step.
- **Space Complexity:** `O(1)` - Only two extra variables (`current_sum`, `max_sum`) are used.
