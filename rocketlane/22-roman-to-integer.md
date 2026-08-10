# 22. Roman to Integer

Source: `09-Strings/10-Roman-to-Integer`

## Question

https://leetcode.com/problems/roman-to-integer

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
| ------ | ----: |
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Example 1

**Input:** `s = "III"`
**Output:** `3`

**Explanation:** `III = 3`.

### Example 2

**Input:** `s = "LVIII"`
**Output:** `58`

**Explanation:** `L = 50`, `V = 5`, `III = 3`.

### Example 3

**Input:** `s = "MCMXCIV"`
**Output:** `1994`

**Explanation:** `M = 1000`, `CM = 900`, `XC = 90` and `IV = 4`.

### Constraints

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.

## Solution

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        total = 0

        for i in range(n):
            if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
                total = total - roman[s[i]]
            else:
                total = total + roman[s[i]]

        return total

if __name__ == "__main__":
    s_input = str(input("Enter the roman numeral: "))
    print(Solution().romanToInt(s_input))
```

## Approach

### Main Logic
```python
if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
    total = total - roman[s[i]]
else:
    total = total + roman[s[i]]
```
- A dictionary `roman` maps each symbol to its value, so looking up a symbol's value is instant.
- `total` starts at 0, and `i` scans every character of `s` from left to right.
- At each position, compare the current symbol's value with the next symbol's value.
- If the current value is smaller than the next one (like `I` before `V` in `IV`), that's a subtractive pair, so subtract the current value instead of adding it.
- Otherwise, just add the current value normally.
- The last character has no "next" character to compare with, so the check `i < len(s) - 1` makes sure it always falls into the "add" case.

**Remember:** Whenever a smaller symbol sits right before a bigger one, it means "subtract me", otherwise just add the symbol's value as you go.

---

### Dry Run

#### Example 1: `s = "III"`
| i | s[i] | next | roman[s[i]] | roman[next] | smaller than next? | action | total |
|---|------|------|-------------|-------------|---------------------|--------|-------|
| 0 | I | I | 1 | 1 | no | add | 0 + 1 = 1 |
| 1 | I | I | 1 | 1 | no | add | 1 + 1 = 2 |
| 2 | I | (none, last char) | 1 | - | no | add | 2 + 1 = 3 |

Return `3`.

#### Example 2: `s = "LVIII"`
| i | s[i] | next | roman[s[i]] | roman[next] | smaller than next? | action | total |
|---|------|------|-------------|-------------|---------------------|--------|-------|
| 0 | L | V | 50 | 5 | no | add | 0 + 50 = 50 |
| 1 | V | I | 5 | 1 | no | add | 50 + 5 = 55 |
| 2 | I | I | 1 | 1 | no | add | 55 + 1 = 56 |
| 3 | I | I | 1 | 1 | no | add | 56 + 1 = 57 |
| 4 | I | (none, last char) | 1 | - | no | add | 57 + 1 = 58 |

Return `58`.

#### Example 3: `s = "MCMXCIV"`
| i | s[i] | next | roman[s[i]] | roman[next] | smaller than next? | action | total |
|---|------|------|-------------|-------------|---------------------|--------|-------|
| 0 | M | C | 1000 | 100 | no | add | 0 + 1000 = 1000 |
| 1 | C | M | 100 | 1000 | yes | subtract | 1000 - 100 = 900 |
| 2 | M | X | 1000 | 10 | no | add | 900 + 1000 = 1900 |
| 3 | X | C | 10 | 100 | yes | subtract | 1900 - 10 = 1890 |
| 4 | C | I | 100 | 1 | no | add | 1890 + 100 = 1990 |
| 5 | I | V | 1 | 5 | yes | subtract | 1990 - 1 = 1989 |
| 6 | V | (none, last char) | 5 | - | no | add | 1989 + 5 = 1994 |

Return `1994`.

---

### Complexity Analysis
- Time Complexity: O(n) - we scan the string once, and each dictionary lookup takes O(1), where n is the length of `s`.
- Space Complexity: O(1) - the `roman` dictionary always holds exactly 7 fixed keys, no matter how long `s` is.
