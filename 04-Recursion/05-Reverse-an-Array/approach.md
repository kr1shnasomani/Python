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

- **Time Complexity:** `O(n)` (each element is swapped at most once)
- **Space Complexity:** `O(n)` (recursive call stack)