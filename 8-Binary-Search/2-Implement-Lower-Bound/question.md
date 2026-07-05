https://www.naukri.com/code360/problems/lower-bound_8165382

You are given an array `arr` sorted in non-decreasing order and a number `x`.

You must return the index of the lower bound of `x`.

**Note:**

1. For a sorted array `arr`, the lower bound of a number `x` is defined as the smallest index `idx` such that the value `arr[idx]` is not less than `x`. If all numbers are smaller than `x`, then `n` should be the lower bound of `x`, where `n` is the size of the array.

2. Try to do this in `O(log(n))`.

## Example

**Input:** `arr = [1, 2, 2, 3]` and `x = 0`

**Output:** `0`

**Explanation:**  
Index `0` is the smallest index such that `arr[0]` is not less than `x`.

Detailed explanation (Input/output format, Notes, Images)

## Constraints

- `1 <= n <= 10^5`
- `0 <= arr[i] <= 10^5`
- `1 <= x <= 10^5`

## Sample Input 1

```text
6
1 2 2 3 3 5
0
```

## Sample Output 1

```text
0
```

## Explanation Of Sample Input 1

Index `0` is the smallest index such that `arr[0]` is not less than `x`.

## Sample Input 2

```text
6
1 2 2 3 3 5
2
```

## Sample Output 2

```text
1
```

## Sample Input 3

```text
6
1 2 2 3 3 5
7
```

## Sample Output 3

```text
6
```