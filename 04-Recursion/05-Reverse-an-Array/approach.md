# Approach

## Main Logic

```python
nums[left], nums[right] = nums[right], nums[left]
reverse(left + 1, right - 1)
```

- Start with two pointers:
  - `left = 0` (first element)
  - `right = n - 1` (last element)
- Swap the elements at `left` and `right`.
- Move `left` one step to the right and `right` one step to the left.
- Recursively reverse the remaining middle part.
- Stop when `left >= right`.

**Remember:** After swapping the first and last elements, they are already in the correct position. We only need to reverse the remaining middle part.

---

## Key Concept

### Two-Pointer Technique

- Property: use two pointers moving toward each other (or in the same direction) instead of nested loops or extra space.
- Why it works: many array problems only need to compare or swap elements from opposite ends, or track two positions at once. A single pass with two pointers handles this in `O(n)` time and `O(1)` extra space.
- Here, `left` starts at the front and `right` starts at the back; they swap and move inward until they meet.

**Remember:** Whenever you need to process an array from both ends at once, two pointers moving toward each other usually does it in one pass.

---

## Dry Run

### Example

**Input:**

```text
n = 6
arr = [5, 7, 8, 1, 6, 3]
```

```text
reverse(0, 5)

Swap arr[0] and arr[5]

[3, 7, 8, 1, 6, 5]

↓

reverse(1, 4)

Swap arr[1] and arr[4]

[3, 6, 8, 1, 7, 5]

↓

reverse(2, 3)

Swap arr[2] and arr[3]

[3, 6, 1, 8, 7, 5]

↓

reverse(3, 2)

left >= right

Return
```

**Output:**

```text
[3, 6, 1, 8, 7, 5]
```

---

### Sample Input 1

**Input:**

```text
n = 8
arr = [3, 1, 1, 7, 4, 2, 6, 11]
```

**Output:**

```text
[11, 6, 2, 4, 7, 1, 1, 3]
```

---

### Sample Input 2

**Input:**

```text
n = 4
arr = [8, 1, 3, 2]
```

**Output:**

```text
[2, 3, 1, 8]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` - Each element is swapped at most once.
- **Space Complexity:** `O(n)` - Recursive call stack.