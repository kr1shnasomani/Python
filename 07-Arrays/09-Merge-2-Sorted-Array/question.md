https://www.naukri.com/code360/problems/sorted-array_6613259

Given two sorted arrays, `a` and `b`, of size `n` and `m`, respectively, return the union of the arrays.

The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.

**Note:** `a` and `b` may contain duplicate elements, but the union array must contain unique elements.

### Example:

**Input:** `n = 5`, `m = 3`
`a = [1, 2, 3, 4, 6]`
`b = [2, 3, 5]`

**Output:** `[1, 2, 3, 4, 5, 6]`

**Explanation:**

Common elements in `a` and `b` are: `[2, 3]`
Distinct elements in `a` are: `[1, 4, 6]`
Distinct elements in `b` are: `[5]`
Union of `a` and `b` is: `[1, 2, 3, 4, 5, 6]`

Detailed explanation ( Input/output format, Notes, Images )

### Sample Input 1:

```text id="v7g3fw"
5 3
1 2 3 4 6
2 3 5
```

### Sample Output 1:

```text id="xn8k5j"
1 2 3 4 5 6
```

### Explanation of Sample Input 1:

**Input:** `n = 5`, `m = 3`
`a = [1, 2, 3, 4, 6]`
`b = [2, 3, 5]`

**Output:** `[1, 2, 3, 4, 5, 6]`

**Explanation:** Common elements in `a` and `b` are: `[2, 3]`
Distinct elements in `a` are: `[1, 4, 6]`
Distinct elements in `b` are: `[5]`
Union of `a` and `b` is: `[1, 2, 3, 4, 5, 6]`

### Sample Input 2:

```text id="5c9mzt"
4 3
1 2 3 3
2 2 4
```

### Sample Output 2:

```text id="hk4p2q"
1 2 3 4
```

### Explanation of Sample Input 2:

**Input:** `n = 5`, `m = 3`
`a = [1, 2, 3, 3]`
`b = [2, 2, 4]`

**Output:** `[1, 2, 3, 4]`

**Explanation:** Common elements in `a` and `b` are: `[2]`
Distinct elements in `a` are: `[1, 3]`
Distinct elements in `b` are: `[4]`
Union of `a` and `b` is: `[1, 2, 3, 4]`

### Expected Time Complexity:

`O((N + M))`, where `N` and `M` are the sizes of Array `A` and `B`.

### Constraints:

* `1 <= 'n', 'm' <= 10^5`
* `-10^9 <= 'a'[i], 'b'[i] <= 10^9`

**Time Limit:** 1 sec
