# Approach

## Main Logic

```python
k %= n

nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])
```

- First, reduce `k` using `k % n` because rotating `n` times brings the array back to its original position.
- Reverse the entire array.
- Reverse the first `k` elements.
- Reverse the remaining `n-k` elements.
- The array is now rotated to the right by `k` positions.

**Remember:** **Reverse Whole → Reverse First `k` → Reverse Remaining**.

---

## Flow

```text
Original Array
      ↓
Reverse Whole Array
      ↓
Reverse First k Elements
      ↓
Reverse Remaining Elements
      ↓
Right Rotated Array
```

---

## Dry Run

### Example 1

**Input:** `nums = [1,2,3,4,5,6,7]`, `k = 3`

`n = 7`

`k = 3 % 7 = 3`

| Step | Array |
|------|-------|
| Original | `[1,2,3,4,5,6,7]` |
| Reverse whole array | `[7,6,5,4,3,2,1]` |
| Reverse first 3 elements | `[5,6,7,4,3,2,1]` |
| Reverse remaining elements | `[5,6,7,1,2,3,4]` |

**Answer:** `[5,6,7,1,2,3,4]`

---

### Example 2

**Input:** `nums = [-1,-100,3,99]`, `k = 2`

`n = 4`

`k = 2 % 4 = 2`

| Step | Array |
|------|-------|
| Original | `[-1,-100,3,99]` |
| Reverse whole array | `[99,3,-100,-1]` |
| Reverse first 2 elements | `[3,99,-100,-1]` |
| Reverse remaining elements | `[3,99,-1,-100]` |

**Answer:** `[3,99,-1,-100]`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` – We reverse the array three times, and each reversal takes linear time.
- **Space Complexity:** `O(1)` – The rotation is performed in-place without using any extra array.