# Approach

## Main Logic

```python
result = result ^ num
```

- Start with `result = 0`.
- XOR every number with `result`.
- Every duplicate number becomes `0` when XORed with itself.
- The only number left at the end is the one that appears once.

**Remember:** `a ^ a = 0`, so duplicate numbers cancel each other.

---

## Key Concept

### XOR Rules

| Operation | Result |
|-----------|:------:|
| `0 ^ 0` | `0` |
| `1 ^ 1` | `0` |
| `0 ^ 1` | `1` |
| `1 ^ 0` | `1` |

### Important Properties

- `a ^ a = 0`
- `0 ^ a = a`
- `a ^ 0 = a`

---

## Dry Run

### Example 1

**Input:** `nums = [2,2,1]`

Initial:

```text
result = 0
```

### Step 1: `result = 0 ^ 2`

| Number | 8 | 4 | 2 | 1 | Decimal |
|:------:|:-:|:-:|:-:|:-:|:-------:|
| result | 0 | 0 | 0 | 0 | **0** |
| num | 0 | 0 | 1 | 0 | **2** |
| **XOR Result** | 0 | 0 | 1 | 0 | **2** |

```text
result = 2
```

---

### Step 2: `result = 2 ^ 2`

| Number | 8 | 4 | 2 | 1 | Decimal |
|:------:|:-:|:-:|:-:|:-:|:-------:|
| result | 0 | 0 | 1 | 0 | **2** |
| num | 0 | 0 | 1 | 0 | **2** |
| **XOR Result** | 0 | 0 | 0 | 0 | **0** |

Since both numbers are identical, every bit cancels out.

```text
result = 0
```

---

### Step 3: `result = 0 ^ 1`

| Number | 8 | 4 | 2 | 1 | Decimal |
|:------:|:-:|:-:|:-:|:-:|:-------:|
| result | 0 | 0 | 0 | 0 | **0** |
| num | 0 | 0 | 0 | 1 | **1** |
| **XOR Result** | 0 | 0 | 0 | 1 | **1** |

```text
result = 1
```

**Answer:** `1`

---

### Example 2

**Input:** `nums = [4,1,2,1,2]`

Instead of calculating every intermediate XOR value, group the duplicate numbers:

```text
0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2
= 0 ^ 4 ^ (1 ^ 1) ^ (2 ^ 2)
= 0 ^ 4 ^ 0 ^ 0
= 4
```

**Answer:** `4`

---

### Example 3

**Input:** `nums = [1]`

Initial:

```text
result = 0
```

### Step 1: `result = 0 ^ 1`

| Number | 8 | 4 | 2 | 1 | Decimal |
|:------:|:-:|:-:|:-:|:-:|:-------:|
| result | 0 | 0 | 0 | 0 | **0** |
| num | 0 | 0 | 0 | 1 | **1** |
| **XOR Result** | 0 | 0 | 0 | 1 | **1** |

```text
result = 1
```

**Answer:** `1`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` – We traverse the array only once.
- **Space Complexity:** `O(1)` – Only one extra variable (`result`) is used.