https://www.naukri.com/code360/problems/count-with-k-different-characters_1214627

You are given a string `str` of lowercase alphabets and an integer `k`.

Your task is to return the count all the possible substrings that have exactly `k` distinct characters.

## Example

`str = "abcad"` and `k = 2`.

We can see that the substrings `{ab, bc, ca, ad}` are the only substrings with 2 distinct characters.

Therefore, the answer will be 4.

## Sample Input 1

```text
aacfssa
3
```

## Sample Output 1

```text
5
```

## Explanation of Sample Input 1

Given `str = "aacfssa"`. We can see that the substrings with only 3 distinct characters are `{aacf, acf, cfs, cfss, fssa}`.

Therefore, the answer will be 5.

## Sample Input 2

```text
qffds
4
```

## Sample Output 2

```text
1
```

## Constraints

- `1 <= |str| <= 10^5`
- `1 <= k <= 26`
- Time limit: 1 second
