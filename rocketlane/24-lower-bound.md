# 24. Lower Bound

Source: `08-Binary-Search/02-Implement-Lower-Bound`

## Question

https://www.naukri.com/code360/problems/lower-bound_8165382

You are given an array `arr` sorted in non-decreasing order and a number `x`.

You must return the index of the lower bound of `x`.

> **Note:**
> 1. For a sorted array `arr`, the lower bound of a number `x` is defined as the smallest index `idx` such that the value `arr[idx]` is not less than `x`. If all numbers are smaller than `x`, then `n` should be the lower bound of `x`, where `n` is the size of the array.
> 2. Try to do this in `O(log(n))`.

### Example

**Input:** `arr = [1, 2, 2, 3]` and `x = 0`

**Output:** `0`

**Explanation:**
Index `0` is the smallest index such that `arr[0]` is not less than `x`.

### Sample Input 1

```text
6
1 2 2 3 3 5
0
```

### Sample Output 1

```text
0
```

### Explanation of Sample Input 1

Index `0` is the smallest index such that `arr[0]` is not less than `x`.

### Sample Input 2

```text
6
1 2 2 3 3 5
2
```

### Sample Output 2

```text
1
```

### Sample Input 3

```text
6
1 2 2 3 3 5
7
```

### Sample Output 3

```text
6
```

### Constraints

- `1 <= n <= 10^5`
- `0 <= arr[i] <= 10^5`
- `1 <= x <= 10^5`

## Solution

```python
def lowerBound(arr: list[int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the sorted array: ").split()))
    x_input = int(input("Enter x: "))
    n_input = len(arr_input)
    print(lowerBound(arr_input, n_input, x_input))
```

## Approach

### Main Logic

```python
if arr[mid] >= x:
    ans = mid
    high = mid - 1
else:
    low = mid + 1
```

- This still shrinks the search range like regular binary search, but it isn't looking for an exact match. It's looking for the smallest index where `arr[mid] >= x`.
- Whenever `arr[mid] >= x`, that index could be the answer, so save it in `ans`. But keep searching the left half anyway, there might be an even smaller valid index.
- Whenever `arr[mid] < x`, this index is too small to be the answer, so search the right half instead.
- `ans` starts at `n`, so if every element turns out smaller than `x`, the answer correctly falls back to `n`.

**Remember:** Lower bound means the smallest index where `arr[mid] >= x`.

---

### Key Concept

**Lower Bound Pattern**

- This is binary search adapted to find a boundary instead of an exact match.
- Instead of returning the moment a condition is true, that index is saved as a possible answer, and the search keeps going on the same side to check for an even better one.
- The range still gets cut in half every step, so it's just as fast as regular binary search, `O(log n)`.
- This "save a candidate and keep narrowing" idea shows up again and again in binary search problems, like upper bound, floor, ceil, and search-the-answer type problems.

---

### Dry Run

#### Example 1

**Input**

```text
arr = [1, 2, 2, 3, 3, 5], x = 0
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 5 | 2 | 2 | 2 >= 0 → ans = 2, high = 1 | 2 |
| 2 | 0 | 1 | 0 | 1 | 1 >= 0 → ans = 0, high = -1 | 0 |

`low = 0` is now greater than `high = -1`, so the loop stops.

**Output**

```text
0
```

---

#### Example 2

**Input**

```text
arr = [1, 2, 2, 3, 3, 5], x = 2
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 5 | 2 | 2 | 2 >= 2 → ans = 2, high = 1 | 2 |
| 2 | 0 | 1 | 0 | 1 | 1 >= 2? No → low = 1 | 2 |
| 3 | 1 | 1 | 1 | 2 | 2 >= 2 → ans = 1, high = 0 | 1 |

`low = 1` is now greater than `high = 0`, so the loop stops.

**Output**

```text
1
```

---

#### Example 3

**Input**

```text
arr = [1, 2, 2, 3, 3, 5], x = 7
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 5 | 2 | 2 | 2 >= 7? No → low = 3 | 6 |
| 2 | 3 | 5 | 4 | 3 | 3 >= 7? No → low = 5 | 6 |
| 3 | 5 | 5 | 5 | 5 | 5 >= 7? No → low = 6 | 6 |

`low = 6` is now greater than `high = 5`, so the loop stops. Since no index ever satisfied `arr[mid] >= x`, `ans` stays at its starting value, `n = 6`.

**Output**

```text
6
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - the search range is still cut in half every step, just like regular binary search.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used, no extra space grows with input size.
