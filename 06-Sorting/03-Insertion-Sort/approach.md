# Approach

## Main Logic

```python
for i in range(1, n):
    current = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > current:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = current
```

- Consider the first element as already sorted.
- Pick the next element (`current`) from the unsorted part.
- Shift all larger elements in the sorted part one position to the right.
- Insert `current` into its correct position.
- Repeat until all elements are sorted.

**Remember:** After every pass, the sorted portion of the array grows by one element.

---

## Flow

```text
Start with the second element

↓

Store it as the current element

↓

Compare it with elements on its left

↓

Shift larger elements one position to the right

↓

Insert the current element into the empty position

↓

Repeat until the array is sorted.
```

---

## Dry Run

### Example 1

**Input**

```text
arr = [9, 3, 6, 2, 0]
```

| Pass | Current Element | Shifts | Array After Pass |
|------|------------------|---------|------------------|
| Initial | - | - | `[9, 3, 6, 2, 0]` |
| 1 | `3` | Shift `9` right | `[3, 9, 6, 2, 0]` |
| 2 | `6` | Shift `9` right | `[3, 6, 9, 2, 0]` |
| 3 | `2` | Shift `9`, `6`, `3` right | `[2, 3, 6, 9, 0]` |
| 4 | `0` | Shift `9`, `6`, `3`, `2` right | `[0, 2, 3, 6, 9]` |

**Output**

```text
[0, 2, 3, 6, 9]
```

---

### Example 2

**Input**

```text
arr = [4, 3, 2, 1]
```

| Pass | Current Element | Shifts | Array After Pass |
|------|------------------|---------|------------------|
| Initial | - | - | `[4, 3, 2, 1]` |
| 1 | `3` | Shift `4` right | `[3, 4, 2, 1]` |
| 2 | `2` | Shift `4`, `3` right | `[2, 3, 4, 1]` |
| 3 | `1` | Shift `4`, `3`, `2` right | `[1, 2, 3, 4]` |

**Output**

```text
[1, 2, 3, 4]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n²)` – In the worst case (reverse sorted array), each element may need to be compared with and shifted past all previously sorted elements.
- **Space Complexity:** `O(1)` – Sorting is done in-place without using any extra array.