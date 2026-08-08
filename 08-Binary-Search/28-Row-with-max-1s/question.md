https://www.naukri.com/code360/problems/row-of-a-matrix-with-maximum-ones_982768

You are given a 2D matrix `ARR` (containing either `0` or `1`) of size `N` x `M`, where each row is in sorted order.

Find the 0-based index of the first row with the maximum number of 1's.

> **Note:**
> If two rows have the same number of 1's, return the row with a lower index.
>
> If no row exists where at-least one `1` is present, return -1.

## Example

**Input:**
`N = 3, M = 3`
`ARR = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]`

**Output:**
`0`

**Explanation:**
The 0th row of the given matrix has the maximum number of ones.

## Sample Input 1

```text
3 3
1 1 1
0 0 1
0 0 0
```

## Sample Output 1

```text
0
```

## Explanation of Sample Input 1

The 0th row of the given matrix has the maximum number of ones.

## Sample Input 2

```text
2 2
1 1
1 1
```

## Sample Output 2

```text
0
```

## Explanation of Sample Input 2

The 0th and 1st rows of the given matrix have the maximum number of ones, so we will output the lower index value.

## Sample Input 3

```text
2 1
0
0
```

## Sample Output 3

```text
-1
```

## Explanation of Sample Input 3

No row is present where at-least one '1' is present. Hence the answer is -1.

## Constraints

- `1 <= N, M <= 100`
- `0 <= ARR[i][j] <= 1`
- Time limit: 1 sec
