# 25. Upper Bound

Source: `08-Binary-Search/03-Implement-Upper-Bound`

## Question

https://www.naukri.com/code360/problems/upper-bound_8165383

You are given a sorted array `arr` containing `n` integers and an integer `x`. Implement the `upper bound` function to find the index of the upper bound of `x` in the array.

> **Note:**
> 1. The upper bound in a sorted array is the index of the first value that is greater than a given value.
> 2. If the greater value does not exist then the answer is `n`, where `n` is the size of the array.
> 3. Try to write a solution that runs in log(n) time complexity.

### Example

**Input:** `arr = {2,4,6,7}` and `x = 5`

**Output:** `2`

**Explanation:** The upper bound of 5 is 6 in the given array, which is at index 2 (00-indexed).

### Sample Input 1

```text
5 7
1 4 7 8 10
```

### Sample Output 1

```text
3
```

### Explanation of Sample Input 1

In the given test case, the lowest value greater than 7 is 8 and is present at index 3(00-indexed).

### Sample Input 2

```text
5 10
1 2 5 6 10
```

### Sample Output 2

```text
5
```

### Sample Input 3

```text
7 5
1 5 5 7 7 9 10
```

### Sample Output 3

```text
3
```

### Constraints

- `1 <= n <= 10^5`
- `1 <= x <= 10^9`
- `1 <= arr[i] <= 10^9`
- Time limit: 1 sec

## Solution

```python
def upperBound(arr: list[int], x: int, n: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the sorted array: ").split()))
    x_input = int(input("Enter x: "))
    n_input = len(arr_input)
    print(upperBound(arr_input, x_input, n_input))
```

## Approach

### Main Logic

```python
if arr[mid] > x:
    ans = mid
    high = mid - 1
else:
    low = mid + 1
```

- This still shrinks the search range like regular binary search, but it isn't looking for an exact match. It's looking for the smallest index where `arr[mid] > x`.
- Whenever `arr[mid] > x`, that index could be the answer, so save it in `ans`. But keep searching the left half anyway, there might be an even smaller valid index.
- Whenever `arr[mid] <= x`, this index is too small to be the answer, so search the right half instead.
- `ans` starts at `n`, so if no element turns out greater than `x`, the answer correctly falls back to `n`.

**Remember:** Upper bound means the smallest index where `arr[mid] > x`.

---

### Dry Run

#### Example 1

**Input**

```text
arr = [2, 4, 6, 7], x = 5
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 3 | 1 | 4 | 4 > 5? No → low = 2 | 4 |
| 2 | 2 | 3 | 2 | 6 | 6 > 5 → ans = 2, high = 1 | 2 |

`low = 2` is now greater than `high = 1`, so the loop stops.

**Output**

```text
2
```

---

#### Sample Input 1

**Input**

```text
arr = [1, 4, 7, 8, 10], x = 7
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 4 | 2 | 7 | 7 > 7? No → low = 3 | 5 |
| 2 | 3 | 4 | 3 | 8 | 8 > 7 → ans = 3, high = 2 | 3 |

`low = 3` is now greater than `high = 2`, so the loop stops.

**Output**

```text
3
```

---

#### Sample Input 2

**Input**

```text
arr = [1, 2, 5, 6, 10], x = 10
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 4 | 2 | 5 | 5 > 10? No → low = 3 | 5 |
| 2 | 3 | 4 | 3 | 6 | 6 > 10? No → low = 4 | 5 |
| 3 | 4 | 4 | 4 | 10 | 10 > 10? No → low = 5 | 5 |

`low = 5` is now greater than `high = 4`, so the loop stops. Since no index ever satisfied `arr[mid] > x`, `ans` stays at its starting value, `n = 5`.

**Output**

```text
5
```

---

#### Sample Input 3

**Input**

```text
arr = [1, 5, 5, 7, 7, 9, 10], x = 5
```

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 6 | 3 | 7 | 7 > 5 → ans = 3, high = 2 | 3 |
| 2 | 0 | 2 | 1 | 5 | 5 > 5? No → low = 2 | 3 |
| 3 | 2 | 2 | 2 | 5 | 5 > 5? No → low = 3 | 3 |

`low = 3` is now greater than `high = 2`, so the loop stops.

**Output**

```text
3
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - the search range is still cut in half every step, just like regular binary search.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used, no extra space grows with input size.
