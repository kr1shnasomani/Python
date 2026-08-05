# Approach

## Main Logic

```python
if nums[low] <= nums[mid]:
    ans = min(ans, nums[low])
    low = mid + 1
else:
    ans = min(ans, nums[mid])
    high = mid - 1
```

- In a rotated sorted array, one half of the current range (`low` to `mid`, or `mid` to `high`) is always still in perfect ascending order. The other half is the one that got "broken" by the rotation.
- Check `nums[low] <= nums[mid]`. If true, the left half is sorted, so its smallest value is `nums[low]`, save that as a candidate answer, then move past this half by setting `low = mid + 1`.
- If false, the right half is sorted instead, so its smallest value is `nums[mid]`, save that as a candidate, then move past the left side by setting `high = mid - 1`.
- Keep repeating on the remaining half. The smallest candidate seen across every step is the true minimum.

**Remember:** Whichever half is sorted, its own first element is already its minimum, so there's no need to scan it. Only the unsorted half might hide a smaller value, so search stays focused there.

---

## Key Concept

**Binary Search on a Rotated Sorted Array**

- A sorted array rotated at some pivot splits into two parts: one part stays in ascending order, the other part is also ascending internally but starts over from a smaller value after the rotation point.
- At every step, comparing `nums[low]` with `nums[mid]` tells which half is the untouched sorted one. `nums[low] <= nums[mid]` means the left half is sorted, otherwise the right half is.
- Since the minimum can only live inside the unsorted half, that's the only half worth continuing the search in, so the sorted half's smallest value is recorded and the search moves on.
- This keeps the search at `O(log n)`, same as regular binary search, even though the array isn't fully sorted anymore.

---

## Dry Run

### Example 1

**Input**

```text
nums = [3, 4, 5, 1, 2]
```

| Step | low | high | mid | nums[low] | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|-----------|----------|-----|
| 1 | 0 | 4 | 2 | 3 | 5 | 3 <= 5 → left sorted, ans = 3, low = 3 | 3 |
| 2 | 3 | 4 | 3 | 1 | 1 | 1 <= 1 → left sorted, ans = 1, low = 4 | 1 |
| 3 | 4 | 4 | 4 | 2 | 2 | 2 <= 2 → left sorted, ans = 1, low = 5 | 1 |

`low = 5` is now greater than `high = 4`, so the loop stops.

**Output**

```text
1
```

---

### Example 2

**Input**

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

| Step | low | high | mid | nums[low] | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|-----------|----------|-----|
| 1 | 0 | 6 | 3 | 4 | 7 | 4 <= 7 → left sorted, ans = 4, low = 4 | 4 |
| 2 | 4 | 6 | 5 | 0 | 1 | 0 <= 1 → left sorted, ans = 0, low = 6 | 0 |
| 3 | 6 | 6 | 6 | 2 | 2 | 2 <= 2 → left sorted, ans = 0, low = 7 | 0 |

`low = 7` is now greater than `high = 6`, so the loop stops.

**Output**

```text
0
```

---

### Example 3

**Input**

```text
nums = [11, 13, 15, 17]
```

| Step | low | high | mid | nums[low] | nums[mid] | Decision | ans |
|------|-----|------|-----|-----------|-----------|----------|-----|
| 1 | 0 | 3 | 1 | 11 | 13 | 11 <= 13 → left sorted, ans = 11, low = 2 | 11 |
| 2 | 2 | 3 | 2 | 15 | 15 | 15 <= 15 → left sorted, ans = 11, low = 3 | 11 |
| 3 | 3 | 3 | 3 | 17 | 17 | 17 <= 17 → left sorted, ans = 11, low = 4 | 11 |

`low = 4` is now greater than `high = 3`, so the loop stops. This array was never actually broken by rotation, so the minimum found is just its first element.

**Output**

```text
11
```

---

## Complexity Analysis

- **Time Complexity:** `O(log n)` - one half of the range is identified as sorted and skipped every step, cutting the search space in half each time.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used, no extra space grows with input size.
