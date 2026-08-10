https://www.naukri.com/code360/problems/rotation_7449070

You are given an array `arr` having `n` distinct integers sorted in ascending order. The array is right rotated `r` times

Find the minimum value of `r`.

Right rotating an array means shifting the element at `ith` index to `(i+1) mod n` index, for all `i` from 0 to `n-1`.

## Example

**Input:**
`n = 5, arr = [3, 4, 5, 1, 2]`

**Output:**
`3`

**Explanation:**
If we rotate the array [1, 2, 3, 4, 5] right `3` times then we will get the `arr`. Thus `r = 3`.

## Sample Input 1

```text
4
2 3 4 1
```

## Sample Output 1

```text
3
```

## Explanation of Sample Input 1

If we right rotate the array {1, 2, 3, 4} by `3` times then we will get {2, 3, 4, 1}. Thus `r = 3`.

## Sample Input 2

```text
3
1 2 3
```

## Sample Output 2

```text
0
```

## Explanation of Sample Input 2

If we right rotate the array {1, 2, 3} by `0` time then we will get {1, 2, 3}. Thus `r = 0`.

## Expected Time Complexity

`O(log n)`

## Constraints

- `1 <= n <= 10^5`
- `1 <= arr[i] <= 10^9`
- Time limit: 1 sec
