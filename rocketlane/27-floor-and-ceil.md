# 27. Floor and Ceil in Sorted Array

Source: `08-Binary-Search/05-Floor-and-Ceil-in-Sorted-Array`

## Question

https://www.naukri.com/code360/problem-details/ceiling-in-a-sorted-array_1825401

You're given a sorted array `a` of `n` integers and an integer `x`.

Find the floor and ceiling of `x` in `a[0..n-1]`.

> **Note:**
> Floor of `x` is the largest element in the array which is smaller than or equal to `x`. Ceiling of `x` is the smallest element in the array greater than or equal to `x`.

### Example

**Input:**
`n=6, x=5, a=[3, 4, 7, 8, 8, 10]`

**Output:**
`4`

**Explanation:**
The floor and ceiling of `x` = 5 are 4 and 7, respectively.

### Sample Input 1

```text
6 8
3 4 4 7 8 10
```

### Sample Output 1

```text
8 8
```

### Explanation of Sample Input 1

Since x = 8 is present in the array, it will be both floor and ceiling.

### Sample Input 2

```text
6 2
3 4 4 7 8 10
```

### Sample Output 2

```text
-1 3
```

### Explanation of Sample Input 2

Since no number is less than or equal to x = 2 in the array, its floor does not exist. The ceiling will be 3.

### Constraints

- `1 <= n <= 2 * 10^5`
- `1 <= a[i] <= 10^9`
- Time limit: 1 sec

## Solution

```python
def find_floor(a, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] <= x:
            ans = a[mid]
            low = mid + 1
        else:
            high = mid - 1

    return ans

def find_ceil(a, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] >= x:
            ans = a[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ans

def getFloorAndCeil(a, n, x):
    floor = find_floor(a, n, x)
    ceil = find_ceil(a, n, x)
    return [floor, ceil]

if __name__ == "__main__":
    a_input = list(map(int, input("Enter the sorted array: ").split()))
    x_input = int(input("Enter x: "))
    n_input = len(a_input)
    print(getFloorAndCeil(a_input, n_input, x_input))
```

## Approach

### Main Logic

**Ceil search**

```python
if a[mid] >= x:
    ans = a[mid]
    high = mid - 1
else:
    low = mid + 1
```

**Floor search**

```python
if a[mid] <= x:
    ans = a[mid]
    low = mid + 1
else:
    high = mid - 1
```

- Floor and ceil are two separate binary searches on the same array, run one after another.
- Ceil search: whenever `a[mid] >= x`, that value could be the answer, so save it and keep searching left for something smaller. Same idea as lower bound, just saving the value instead of the index.
- Floor search: whenever `a[mid] <= x`, that value could be the answer, so save it and keep searching right for something bigger. This is the mirror image of the ceil search, the direction just flips.
- Both `ans` start at `-1`, so if no valid value exists on that side, `-1` is returned automatically.

**Remember:** Ceil narrows left after saving a candidate, floor narrows right after saving a candidate, everything else is the same pattern.

---

### Dry Run

#### Example 1

**Input**

```text
a = [3, 4, 7, 8, 8, 10], x = 5
```

**Floor search**

| Step | low | high | mid | a[mid] | Decision | ans |
|------|-----|------|-----|--------|----------|-----|
| 1 | 0 | 5 | 2 | 7 | 7 <= 5? No → high = 1 | -1 |
| 2 | 0 | 1 | 0 | 3 | 3 <= 5 → ans = 3, low = 1 | 3 |
| 3 | 1 | 1 | 1 | 4 | 4 <= 5 → ans = 4, low = 2 | 4 |

`low = 2` is now greater than `high = 1`, so the loop stops. Floor = `4`.

**Ceil search**

| Step | low | high | mid | a[mid] | Decision | ans |
|------|-----|------|-----|--------|----------|-----|
| 1 | 0 | 5 | 2 | 7 | 7 >= 5 → ans = 7, high = 1 | 7 |
| 2 | 0 | 1 | 0 | 3 | 3 >= 5? No → low = 1 | 7 |
| 3 | 1 | 1 | 1 | 4 | 4 >= 5? No → low = 2 | 7 |

`low = 2` is now greater than `high = 1`, so the loop stops. Ceil = `7`.

**Output**

```text
4
```

---

#### Sample Input 1

**Input**

```text
a = [3, 4, 4, 7, 8, 10], x = 8
```

**Floor search**

| Step | low | high | mid | a[mid] | Decision | ans |
|------|-----|------|-----|--------|----------|-----|
| 1 | 0 | 5 | 2 | 4 | 4 <= 8 → ans = 4, low = 3 | 4 |
| 2 | 3 | 5 | 4 | 8 | 8 <= 8 → ans = 8, low = 5 | 8 |
| 3 | 5 | 5 | 5 | 10 | 10 <= 8? No → high = 4 | 8 |

`low = 5` is now greater than `high = 4`, so the loop stops. Floor = `8`.

**Ceil search**

| Step | low | high | mid | a[mid] | Decision | ans |
|------|-----|------|-----|--------|----------|-----|
| 1 | 0 | 5 | 2 | 4 | 4 >= 8? No → low = 3 | -1 |
| 2 | 3 | 5 | 4 | 8 | 8 >= 8 → ans = 8, high = 3 | 8 |
| 3 | 3 | 3 | 3 | 7 | 7 >= 8? No → low = 4 | 8 |

`low = 4` is now greater than `high = 3`, so the loop stops. Ceil = `8`.

**Output**

```text
8 8
```

---

#### Sample Input 2

**Input**

```text
a = [3, 4, 4, 7, 8, 10], x = 2
```

**Floor search**

| Step | low | high | mid | a[mid] | Decision | ans |
|------|-----|------|-----|--------|----------|-----|
| 1 | 0 | 5 | 2 | 4 | 4 <= 2? No → high = 1 | -1 |
| 2 | 0 | 1 | 0 | 3 | 3 <= 2? No → high = -1 | -1 |

`low = 0` is now greater than `high = -1`, so the loop stops. Since no element was ever `<= x`, `ans` stays `-1`. Floor = `-1`.

**Ceil search**

| Step | low | high | mid | a[mid] | Decision | ans |
|------|-----|------|-----|--------|----------|-----|
| 1 | 0 | 5 | 2 | 4 | 4 >= 2 → ans = 4, high = 1 | 4 |
| 2 | 0 | 1 | 0 | 3 | 3 >= 2 → ans = 3, high = -1 | 3 |

`low = 0` is now greater than `high = -1`, so the loop stops. Ceil = `3`.

**Output**

```text
-1 3
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - floor and ceil are two independent binary searches, each `O(log n)`, run one after another.
- **Space Complexity:** `O(1)` - only a few pointers and one answer variable are used in each search, no extra space grows with input size.
