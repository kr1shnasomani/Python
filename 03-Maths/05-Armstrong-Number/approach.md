# Approach

## Main Logic

```python
digit = num % 10
total = total + (digit ** count)
num //= 10
```

- Take the last digit.
- Raise it to the power of the number of digits.
- Add it to `total`.
- Remove the last digit.
- Repeat until `num` becomes `0`.
- If `total` equals the original number, it is an Armstrong number.

**Remember:** Sum of `(each digit)^(number of digits)` should be equal to the original number.

---

## Dry Run

### Example 1: `num = 153`

Number of digits = **3**

| num | total | Digit (`num % 10`) | New total |
|---:|---:|---:|---:|
| 153 | 0 | 3 | `0 + 3³ = 27` |
| 15 | 27 | 5 | `27 + 5³ = 152` |
| 1 | 152 | 1 | `152 + 1³ = 153` |
| 0 | 153 | - | Loop ends |

Compare:
- Original = `153`
- Total = `153`

**Output:** `YES`

---

### Example 2: `num = 13`

Number of digits = **2**

| num | total | Digit (`num % 10`) | New total |
|---:|---:|---:|---:|
| 13 | 0 | 3 | `0 + 3² = 9` |
| 1 | 9 | 1 | `9 + 1² = 10` |
| 0 | 10 | - | Loop ends |

Compare:
- Original = `13`
- Total = `10`

**Output:** `NO`

---

### Example 3: `num = 371`

Number of digits = **3**

| num | total | Digit (`num % 10`) | New total |
|---:|---:|---:|---:|
| 371 | 0 | 1 | `0 + 1³ = 1` |
| 37 | 1 | 7 | `1 + 7³ = 344` |
| 3 | 344 | 3 | `344 + 3³ = 371` |
| 0 | 371 | - | Loop ends |

Compare:
- Original = `371`
- Total = `371`

**Output:** `YES`

---

## Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`
