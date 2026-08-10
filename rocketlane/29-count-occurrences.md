# 29. Count Occurrences in a Sorted Array

Source: `08-Binary-Search/07-Count-Occurrences-in-a-Sorted-Array`

## Question

https://www.naukri.com/code360/problems/occurrence-of-x-in-a-sorted-array_630456

You have been given a sorted array/list of integers `arr` of size `n` and an integer `x`.

Find the total number of occurrences of `x` in the array/list.

### Example

**Input:**
`n = 7, x = 3`
`arr = [1, 1, 1, 2, 2, 3, 3]`

**Output:**
`2`

**Explanation:**
Total occurrences of `3` in the array `arr` is 2.

### Sample Input 1

```text
7 3
1 1 1 2 2 3 3
```

### Sample Output 1

```text
2
```

### Explanation of Sample Input 1

In the given list, there are 2 occurrences of integer 3.

### Sample Input 2

```text
5 6
1 2 4 4 5
```

### Sample Output 2

```text
0
```

### Explanation of Sample Input 2

In the given list, there are 0 occurrences of integer 6.

### Expected Time Complexity

`O(log n)`

### Constraints

- `1 <= n <= 10^4`
- `1 <= arr[i] <= 10^9`
- `1 <= x <= 10^9`
- Where `arr[i]` represents the element i-th element in the array/list.
- Time limit: 1sec

## Solution

```python
def lower_bound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def upper_bound(arr, n, x):
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

def count(arr: list[int], n: int, x: int) -> int:
    first = lower_bound(arr, n, x)

    if first == n or arr[first] != x:
        return 0

    last = upper_bound(arr, n, x)
    return last - first

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the sorted array: ").split()))
    x_input = int(input("Enter x: "))
    n_input = len(arr_input)
    print(count(arr_input, n_input, x_input))
```

## Approach

### Main Logic

```python
if first == n or arr[first] != x:
    return 0

last = upper_bound(arr, n, x) - 1
return last - first + 1
```

- `first` is the lower bound of `x`, the index where `x` would first appear if it's in the array.
- If `first` runs off the end (`== n`) or `arr[first]` isn't actually `x`, then `x` never appears, so the count is `0`.
- Otherwise `x` is present. `last` is the upper bound of `x` minus one, the index where `x` last appears.
- The total occurrences is just how many indices that span covers: `last - first + 1`.

**Remember:** Occurrences of `x` = last occurrence index minus first occurrence index, plus one. Both boundaries come straight from lower bound and upper bound.

---

### Dry Run

#### Example

**Input**

```text
arr = [1, 1, 1, 2, 2, 3, 3], x = 3
```

**Lower bound search**

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 6 | 3 | 2 | 2 >= 3? No → low = 4 | 7 |
| 2 | 4 | 6 | 5 | 3 | 3 >= 3 → ans = 5, high = 4 | 5 |
| 3 | 4 | 4 | 4 | 2 | 2 >= 3? No → low = 5 | 5 |

`low = 5` is now greater than `high = 4`, so the loop stops. `first = 5`.

**Check:** `first = 5` is not `n = 7`, and `arr[5] = 3` equals `x`, so `x` is present. Continue to find the last occurrence.

**Upper bound search**

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 6 | 3 | 2 | 2 > 3? No → low = 4 | 7 |
| 2 | 4 | 6 | 5 | 3 | 3 > 3? No → low = 6 | 7 |
| 3 | 6 | 6 | 6 | 3 | 3 > 3? No → low = 7 | 7 |

`low = 7` is now greater than `high = 6`, so the loop stops. Upper bound is `7`, so `last = 7 - 1 = 6`.

**Count:** `last - first + 1 = 6 - 5 + 1 = 2`.

**Output**

```text
2
```

*Sample Input 1 uses the exact same `arr` and `x` as this example, so it produces the same result, `2`.*

---

#### Sample Input 2

**Input**

```text
arr = [1, 2, 4, 4, 5], x = 6
```

**Lower bound search**

| Step | low | high | mid | arr[mid] | Decision | ans |
|------|-----|------|-----|----------|----------|-----|
| 1 | 0 | 4 | 2 | 4 | 4 >= 6? No → low = 3 | 5 |
| 2 | 3 | 4 | 3 | 4 | 4 >= 6? No → low = 4 | 5 |
| 3 | 4 | 4 | 4 | 5 | 5 >= 6? No → low = 5 | 5 |

`low = 5` is now greater than `high = 4`, so the loop stops. `first = 5`.

**Check:** `first = 5` equals `n = 5`, so `x` is not present. The upper bound search never even runs, the count is `0` right away.

**Output**

```text
0
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - lower bound and upper bound are two independent binary searches, each `O(log n)`, run one after another.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used in each search, no extra space grows with input size.
