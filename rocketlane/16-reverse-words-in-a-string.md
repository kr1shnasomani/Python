# 16. Reverse Words in a Given String / Palindrome Check

Source: `09-Strings/02-Reverse-Words-in-a-String`

## Question

https://leetcode.com/problems/reverse-words-in-a-string

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in **reverse order** concatenated by a **single space**.

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Example 1

**Input:** `s = "the sky is blue"`
**Output:** `"blue is sky the"`

### Example 2

**Input:** `s = "  hello world  "`
**Output:** `"world hello"`

**Explanation:** Your reversed string should not contain leading or trailing spaces.

### Example 3

**Input:** `s = "a good   example"`
**Output:** `"example good a"`

**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

### Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        answer = " ".join(words)

        return answer

if __name__ == "__main__":
    s_input = str(input("Enter the string: "))
    print(Solution().reverseWords(s_input))
```

## Approach

### Main Logic
```python
words = s.split()
words.reverse()
answer = " ".join(words)
```
- `s.split()` with no arguments breaks the string into words using any amount of whitespace as the separator, and it automatically ignores leading, trailing, and extra spaces between words.
- `words.reverse()` flips the order of the list in place.
- `" ".join(words)` glues the words back together using exactly one space, giving a clean result with no extra spaces.

**Remember:** Python's `split()` without arguments already solves the "multiple spaces" headache for you, so you don't need to manually clean the string.

---

### Dry Run

#### Example 1: `s = "the sky is blue"`
| Step | Operation | Result |
|------|-----------|--------|
| 1 | `s.split()` | `["the", "sky", "is", "blue"]` |
| 2 | `.reverse()` | `["blue", "is", "sky", "the"]` |
| 3 | `" ".join(...)` | `"blue is sky the"` |

#### Example 2: `s = "  hello world  "`
| Step | Operation | Result |
|------|-----------|--------|
| 1 | `s.split()` | `["hello", "world"]` (leading/trailing spaces dropped) |
| 2 | `.reverse()` | `["world", "hello"]` |
| 3 | `" ".join(...)` | `"world hello"` |

#### Example 3: `s = "a good   example"`
| Step | Operation | Result |
|------|-----------|--------|
| 1 | `s.split()` | `["a", "good", "example"]` (extra spaces collapsed) |
| 2 | `.reverse()` | `["example", "good", "a"]` |
| 3 | `" ".join(...)` | `"example good a"` |

---

### Complexity Analysis
- Time Complexity: O(n) - we scan the string once to split it and once more to join it back, where n is the length of `s`.
- Space Complexity: O(n) - the list of words and the final joined string both take space proportional to the input.
