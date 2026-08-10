# 32. Find Out How Many Times the Array is Rotated

Source: `08-Binary-Search/11-Find-out-how-many-times-the-array-is-rotated`

## Question

https://www.naukri.com/code360/problems/rotation_7449070

You are given an array `arr` having `n` distinct integers sorted in ascending order. The array is right rotated `r` times

Find the minimum value of `r`.

Right rotating an array means shifting the element at `ith` index to `(i+1) mod n` index, for all `i` from 0 to `n-1`.

### Example

**Input:**
`n = 5, arr = [3, 4, 5, 1, 2]`

**Output:**
`3`

**Explanation:**
If we rotate the array [1, 2, 3, 4, 5] right `3` times then we will get the `arr`. Thus `r = 3`.

### Sample Input 1

```text
4
2 3 4 1
```

### Sample Output 1

```text
3
```

### Explanation of Sample Input 1

If we right rotate the array {1, 2, 3, 4} by `3` times then we will get {2, 3, 4, 1}. Thus `r = 3`.

### Sample Input 2

```text
3
1 2 3
```

### Sample Output 2

```text
0
```

### Explanation of Sample Input 2

If we right rotate the array {1, 2, 3} by `0` time then we will get {1, 2, 3}. Thus `r = 0`.

### Expected Time Complexity

`O(log n)`

### Constraints

- `1 <= n <= 10^5`
- `1 <= arr[i] <= 10^9`
- Time limit: 1 sec

## Solution

```python
def findKRotation(arr : list[int]) -> int:
    n = len(arr)

    low = 0
    high = n - 1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            low = mid + 1
        else:
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]
            high = mid - 1

    return index
```

## Approach

### Main Logic

```python
if arr[low] <= arr[mid]:
    if arr[low] < ans:
        index = low
        ans = arr[low]
    low = mid + 1
else:
    if arr[mid] < ans:
        index = mid
        ans = arr[mid]
    high = mid - 1
```

- Whenever `arr[low] <= arr[mid]`, the left half (`low` to `mid`) is sorted. In a sorted ascending stretch, the smallest value is always the first one, `arr[low]`. So `arr[low]` is a candidate for the overall minimum, compare it with the best `ans` found so far and keep the smaller one. Since the left half can't hide anything smaller, search the right half next.
- Whenever `arr[low] > arr[mid]`, the rotation "seam" lies inside the left half, so the right half (`mid` to `high`) must be the sorted one instead. That makes `arr[mid]` the candidate this time, compare it with `ans` and keep the smaller one, then search the left half next since the true minimum is still hiding there.
- The index of the smallest value in the whole array is exactly the number of rotations `r`, because that's how far the original smallest element (which started at index `0`) got shifted to the right.
- `ans` starts at infinity, so the very first comparison always updates it.

**Remember:** The number of rotations equals the index of the minimum element. Keep track of the smallest value and its index while eliminating half the array every step.

---

### Dry Run

#### Example

**Input**

```text
n = 5, arr = [3, 4, 5, 1, 2]
```

| Step | low | high | mid | arr[low] | arr[mid] | Decision | ans | index |
|------|-----|------|-----|----------|----------|----------|-----|-------|
| 1 | 0 | 4 | 2 | 3 | 5 | 3 <= 5 → left sorted. 3 < inf → update. low = 3 | 3 | 0 |
| 2 | 3 | 4 | 3 | 1 | 1 | 1 <= 1 → left sorted. 1 < 3 → update. low = 4 | 1 | 3 |
| 3 | 4 | 4 | 4 | 2 | 2 | 2 <= 2 → left sorted. 2 < 1? No. low = 5 | 1 | 3 |

`low = 5` is now greater than `high = 4`, so the loop stops.

**Output**

```text
3
```

---

#### Sample Input 1

**Input**

```text
n = 4, arr = [2, 3, 4, 1]
```

| Step | low | high | mid | arr[low] | arr[mid] | Decision | ans | index |
|------|-----|------|-----|----------|----------|----------|-----|-------|
| 1 | 0 | 3 | 1 | 2 | 3 | 2 <= 3 → left sorted. 2 < inf → update. low = 2 | 2 | 0 |
| 2 | 2 | 3 | 2 | 4 | 4 | 4 <= 4 → left sorted. 4 < 2? No. low = 3 | 2 | 0 |
| 3 | 3 | 3 | 3 | 1 | 1 | 1 <= 1 → left sorted. 1 < 2 → update. low = 4 | 1 | 3 |

`low = 4` is now greater than `high = 3`, so the loop stops.

**Output**

```text
3
```

---

#### Sample Input 2

**Input**

```text
n = 3, arr = [1, 2, 3]
```

| Step | low | high | mid | arr[low] | arr[mid] | Decision | ans | index |
|------|-----|------|-----|----------|----------|----------|-----|-------|
| 1 | 0 | 2 | 1 | 1 | 2 | 1 <= 2 → left sorted. 1 < inf → update. low = 2 | 1 | 0 |
| 2 | 2 | 2 | 2 | 3 | 3 | 3 <= 3 → left sorted. 3 < 1? No. low = 3 | 1 | 0 |

`low = 3` is now greater than `high = 2`, so the loop stops. Since the array was never actually rotated, the smallest element is still at index `0`.

**Output**

```text
0
```

---

### Complexity Analysis

- **Time Complexity:** `O(log n)` - each step still throws away one full half of the search range, exactly like regular binary search.
- **Space Complexity:** `O(1)` - only a few pointers and one answer pair are used, no extra space grows with input size.
