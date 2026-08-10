https://www.naukri.com/code360/problems/occurrence-of-x-in-a-sorted-array_630456

You have been given a sorted array/list of integers `arr` of size `n` and an integer `x`.

Find the total number of occurrences of `x` in the array/list.

## Example

**Input:**
`n = 7, x = 3`
`arr = [1, 1, 1, 2, 2, 3, 3]`

**Output:**
`2`

**Explanation:**
Total occurrences of `3` in the array `arr` is 2.

## Sample Input 1

```text
7 3
1 1 1 2 2 3 3
```

## Sample Output 1

```text
2
```

## Explanation of Sample Input 1

In the given list, there are 2 occurrences of integer 3.

## Sample Input 2

```text
5 6
1 2 4 4 5
```

## Sample Output 2

```text
0
```

## Explanation of Sample Input 2

In the given list, there are 0 occurrences of integer 6.

## Expected Time Complexity

`O(log n)`

## Constraints

- `1 <= n <= 10^4`
- `1 <= arr[i] <= 10^9`
- `1 <= x <= 10^9`
- Where `arr[i]` represents the element i-th element in the array/list.
- Time limit: 1sec
