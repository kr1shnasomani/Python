# Approach

## Main Logic

```python
result = printNos(x - 1)
result.append(x)
```

- If `x == 0`, return an empty list `[]`.
- First, recursively get the list from `1` to `x-1`.
- Add `x` to the end of that list.
- Return the updated list.

**Remember:** To get numbers from `1` to `x`, first get numbers from `1` to `x-1`, then add `x`.

---

## Flow

For `x = 5`

```text
printNos(5)
↓
Needs printNos(4)

printNos(4)
↓
Needs printNos(3)

printNos(3)
↓
Needs printNos(2)

printNos(2)
↓
Needs printNos(1)

printNos(1)
↓
Needs printNos(0)

printNos(0)
↓
Returns []
```

Now the functions start returning one by one:

```text
[]
↓ append(1)
[1]

↓ append(2)
[1, 2]

↓ append(3)
[1, 2, 3]

↓ append(4)
[1, 2, 3, 4]

↓ append(5)
[1, 2, 3, 4, 5]
```

---

## Dry Run

### Example 1: `x = 5`

#### Recursive Calls

| Function Call | Action |
|:-------------|:-------|
| `printNos(5)` | Calls `printNos(4)` |
| `printNos(4)` | Calls `printNos(3)` |
| `printNos(3)` | Calls `printNos(2)` |
| `printNos(2)` | Calls `printNos(1)` |
| `printNos(1)` | Calls `printNos(0)` |
| `printNos(0)` | Returns `[]` |

#### Returning Back

| Returning From | Received List | After `append(x)` | Returns |
|:--------------|:--------------|:------------------|:--------|
| `printNos(1)` | `[]` | `[1]` | `[1]` |
| `printNos(2)` | `[1]` | `[1, 2]` | `[1, 2]` |
| `printNos(3)` | `[1, 2]` | `[1, 2, 3]` | `[1, 2, 3]` |
| `printNos(4)` | `[1, 2, 3]` | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` |
| `printNos(5)` | `[1, 2, 3, 4]` | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` |

**Output:** `[1, 2, 3, 4, 5]`

---

### Example 2: `x = 2`

#### Recursive Calls

| Function Call | Action |
|:-------------|:-------|
| `printNos(2)` | Calls `printNos(1)` |
| `printNos(1)` | Calls `printNos(0)` |
| `printNos(0)` | Returns `[]` |

#### Returning Back

| Returning From | Received List | After `append(x)` | Returns |
|:--------------|:--------------|:------------------|:--------|
| `printNos(1)` | `[]` | `[1]` | `[1]` |
| `printNos(2)` | `[1]` | `[1, 2]` | `[1, 2]` |

**Output:** `[1, 2]`

---

## Complexity Analysis

- **Time Complexity:** `O(x)`
- **Space Complexity:** `O(x) due to recursion stack`
