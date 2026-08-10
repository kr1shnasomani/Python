# 17. Largest Odd Number in a String

Source: `09-Strings/03-Largest-Odd-Number-in-String`

## Question

https://leetcode.com/problems/largest-odd-number-in-string

You are given a string `num`, representing a large integer. Return *the largest-valued odd integer (as a string) that is a non-empty substring of* `num`, *or an empty string* `""` *if no odd integer exists*.

A **substring** is a contiguous sequence of characters within a string.

### Example 1

**Input:** `num = "52"`

**Output:** `"5"`

**Explanation:** The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

### Example 2

**Input:** `num = "4206"`

**Output:** `""`

**Explanation:** There are no odd numbers in "4206".

### Example 3

**Input:** `num = "35427"`

**Output:** `"35427"`

**Explanation:** "35427" is already an odd number.

### Constraints

- `1 <= num.length <= 10^5`
- `num` only consists of digits and does not contain any leading zeros.

## Solution

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)

        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]

        return ""

if __name__ == "__main__":
    num_input = str(input("Enter a number: "))
    print(Solution().largestOddNumber(num_input))
```

## Approach

### Main Logic
```python
if int(num[i]) % 2 != 0:
    return num[:i + 1]
```
- Scan the string from right to left, checking one digit at a time.
- A digit is odd if `digit % 2 != 0`.
- The moment you find the first odd digit while going right to left, stop immediately and return everything from the start of the string up to and including that digit (`num[:i + 1]`).
- This works because the string has no leading zeros, so a longer prefix is always a bigger number than a shorter one. The rightmost odd digit you can find gives you the longest possible prefix that still ends in an odd digit, which makes it the largest odd number available.
- If the loop finishes without finding any odd digit, there's no odd substring at all, so return `""`.

**Remember:** A number's odd/even nature depends only on its last digit, so just walk backward until you hit an odd digit, that's your cutoff point.

---

### Dry Run

#### Example 1: `num = "52"`
| i | num[i] | digit % 2 | odd? | action |
|---|--------|-----------|------|--------|
| 1 | 2 | 0 | no | continue |
| 0 | 5 | 1 | yes | return `num[:1]` → `"5"` |

#### Example 2: `num = "4206"`
| i | num[i] | digit % 2 | odd? | action |
|---|--------|-----------|------|--------|
| 3 | 6 | 0 | no | continue |
| 2 | 0 | 0 | no | continue |
| 1 | 2 | 0 | no | continue |
| 0 | 4 | 0 | no | continue |

Loop finishes with no odd digit found, return `""`.

#### Example 3: `num = "35427"`
| i | num[i] | digit % 2 | odd? | action |
|---|--------|-----------|------|--------|
| 4 | 7 | 1 | yes | return `num[:5]` → `"35427"` |

---

### Complexity Analysis
- Time Complexity: O(n) - in the worst case (no odd digit, or the odd digit is at the very start), we scan every character of `num`.
- Space Complexity: O(1) - aside from the returned substring itself, we only use a loop index, no extra data structures.
