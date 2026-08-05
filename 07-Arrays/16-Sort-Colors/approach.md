# Approach

## Main Logic

```python
if nums[mid] == 0:
    nums[low], nums[mid] = nums[mid], nums[low]
    low += 1
    mid += 1
elif nums[mid] == 1:
    mid += 1
else:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
```

- Three pointers split the array into zones: everything before `low` is `0`s, everything from `low` to `mid - 1` is `1`s, everything after `high` is `2`s, and `mid` to `high` is still unsorted.
- Look only at `nums[mid]`, the first unsorted value.
- If it's `0`, swap it into the `0` zone (with `low`) and move both `low` and `mid` forward, the value swapped in at `mid` is already known to be safe.
- If it's `1`, it's already where it belongs, just move `mid` forward.
- If it's `2`, swap it into the `2` zone (with `high`) and pull `high` back. `mid` stays put here, since the value swapped in from `high` hasn't been checked yet.

**Remember:** Only `nums[mid]` is ever inspected. The array sorts itself into three zones as `low`, `mid`, and `high` close in from both sides.

---

## Key Concept

**Dutch National Flag Algorithm**

- Named after the three horizontal stripes on the Dutch flag, since it sorts values into three groups the same way those stripes are separated by color.
- It uses three pointers over one pass: `low` marks where the next `0` should go, `high` marks where the next `2` should go, and `mid` scans through the unsorted middle.
- The array always stays in this shape: `[0s][1s][unsorted][2s]`. Every swap either grows the `0` zone, grows the `2` zone, or confirms the current value is a `1`.
- This sorts an array of three distinct values in one pass, without needing a general-purpose sort.

---

## Dry Run

### Example 1

**Input**

```text
nums = [2, 0, 2, 1, 1, 0]
```

| Step | low | mid | high | nums[mid] | Decision | Array After |
|------|-----|-----|------|-----------|----------|--------------|
| 1 | 0 | 0 | 5 | 2 | swap(mid, high), high→4 | [0, 0, 2, 1, 1, 2] |
| 2 | 0 | 0 | 4 | 0 | swap(low, mid), low→1, mid→1 | [0, 0, 2, 1, 1, 2] |
| 3 | 1 | 1 | 4 | 0 | swap(low, mid), low→2, mid→2 | [0, 0, 2, 1, 1, 2] |
| 4 | 2 | 2 | 4 | 2 | swap(mid, high), high→3 | [0, 0, 1, 1, 2, 2] |
| 5 | 2 | 2 | 3 | 1 | already correct, mid→3 | [0, 0, 1, 1, 2, 2] |
| 6 | 2 | 3 | 3 | 1 | already correct, mid→4 | [0, 0, 1, 1, 2, 2] |

`mid = 4` is now greater than `high = 3`, so the loop stops.

**Output**

```text
[0, 0, 1, 1, 2, 2]
```

---

### Example 2

**Input**

```text
nums = [2, 0, 1]
```

| Step | low | mid | high | nums[mid] | Decision | Array After |
|------|-----|-----|------|-----------|----------|--------------|
| 1 | 0 | 0 | 2 | 2 | swap(mid, high), high→1 | [1, 0, 2] |
| 2 | 0 | 0 | 1 | 1 | already correct, mid→1 | [1, 0, 2] |
| 3 | 0 | 1 | 1 | 0 | swap(low, mid), low→1, mid→2 | [0, 1, 2] |

`mid = 2` is now greater than `high = 1`, so the loop stops.

**Output**

```text
[0, 1, 2]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` - each element is looked at once by `mid`, and `low` and `high` only move inward, so the array is sorted in a single pass.
- **Space Complexity:** `O(1)` - the array is sorted in-place using swaps, no extra array is needed.
