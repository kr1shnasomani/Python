https://www.naukri.com/code360/problems/1062679

You are given two positive integers `n` and `m`. You have to return the `nth` root of `m`, i.e. `m^(1/n)`. If the `nth` root is not an integer, return -1.

> **Note:**
> `nth` root of an integer `m` is a number, which, when raised to the power `n`, gives `m` as a result.

## Example

**Input:**
`n = 3, m = 27`

**Output:**
`3`

**Explanation:**
3rd Root of 27 is 3, as (3)^3 equals 27.

## Sample Input 1

```text
3 27
```

## Sample Output 1

```text
3
```

## Explanation of Sample Input 1

3rd Root of 27 is 3, as (3)^3 equals 27.

## Sample Input 2

```text
4 69
```

## Sample Output 2

```text
-1
```

## Explanation of Sample Input 2

4th Root of 69 is not an integer, hence -1.

## Expected Time Complexity

`O(log(n+m))`

## Constraints

- `1 <= n <= 30`
- `1 <= m <= 10 ^ 9`
- Time limit: 1 sec
