# Approach

## Main Logic

```python
result = [x] + printNos(x - 1)
```

- If `x == 0`, return an empty list `[]`.
- Create a list containing only the current number `x`.
- Recursively get the remaining numbers from `x-1` to `1`.
- Join both lists and return the result.

**Remember:** To get numbers from `N` to `1`, first keep `N`, then get the remaining numbers (`N-1` to `1`).

---

## Flow

For `x = 5`

```text
printNos(5)
↓
result = [5] + printNos(4)

printNos(4)
↓
result = [4] + printNos(3)

printNos(3)
↓
result = [3] + printNos(2)

printNos(2)
↓
result = [2] + printNos(1)

printNos(1)
↓
result = [1] + printNos(0)

printNos(0)
↓
Returns []
```

Now the functions start returning:

```text
printNos(1)
[1] + []
= [1]

↓

printNos(2)
[2] + [1]
= [2, 1]

↓

printNos(3)
[3] + [2, 1]
= [3, 2, 1]

↓

printNos(4)
[4] + [3, 2, 1]
= [4, 3, 2, 1]

↓

printNos(5)
[5] + [4, 3, 2, 1]
= [5, 4, 3, 2, 1]
```

---

## Dry Run

### Example 1: `x = 5`

#### Recursive Calls

| Function Call | Current `result` | Next Call |
|:-------------|:-----------------|:----------|
| `printNos(5)` | `[5]` | `printNos(4)` |
| `printNos(4)` | `[4]` | `printNos(3)` |
| `printNos(3)` | `[3]` | `printNos(2)` |
| `printNos(2)` | `[2]` | `printNos(1)` |
| `printNos(1)` | `[1]` | `printNos(0)` |
| `printNos(0)` | `[]` | Returns `[]` |

#### Returning Back

| Returning From | Current List | Returned List | Final Result |
|:--------------|:-------------|:--------------|:-------------|
| `printNos(1)` | `[1]` | `[]` | `[1]` |
| `printNos(2)` | `[2]` | `[1]` | `[2, 1]` |
| `printNos(3)` | `[3]` | `[2, 1]` | `[3, 2, 1]` |
| `printNos(4)` | `[4]` | `[3, 2, 1]` | `[4, 3, 2, 1]` |
| `printNos(5)` | `[5]` | `[4, 3, 2, 1]` | `[5, 4, 3, 2, 1]` |

**Output:** `[5, 4, 3, 2, 1]`

---

### Example 2: `x = 2`

#### Recursive Calls

| Function Call | Current `result` | Next Call |
|:-------------|:-----------------|:----------|
| `printNos(2)` | `[2]` | `printNos(1)` |
| `printNos(1)` | `[1]` | `printNos(0)` |
| `printNos(0)` | `[]` | Returns `[]` |

#### Returning Back

| Returning From | Current List | Returned List | Final Result |
|:--------------|:-------------|:--------------|:-------------|
| `printNos(1)` | `[1]` | `[]` | `[1]` |
| `printNos(2)` | `[2]` | `[1]` | `[2, 1]` |

**Output:** `[2, 1]`

---

## Complexity Analysis

- **Time Complexity:** `O(x)`
- **Space Complexity:** `O(x) due to recursion stack`
