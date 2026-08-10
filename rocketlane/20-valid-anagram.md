# 20. Check if Two Strings Are Anagram of Each Other

Source: `09-Strings/07-Valid-Anagram`

## Question

https://leetcode.com/problems/valid-anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Example 1

**Input:** `s = "anagram"`, `t = "nagaram"`
**Output:** `true`

### Example 2

**Input:** `s = "rat"`, `t = "car"`
**Output:** `false`

### Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1

            if count[char] < 0:
                return False

        return True

if __name__ == "__main__":
    s_input = str(input("Enter the first string: "))
    t_input = str(input("Enter the second string: "))
    print(Solution().isAnagram(s_input, t_input))
```

## Approach

### Main Logic
```python
if char not in count:
    return False
count[char] -= 1

if count[char] < 0:
    return False
```
- First, loop through `s` and build a dictionary `count` that stores how many times each character appears in `s`.
- Then loop through `t`. For every character, check if it exists in `count` first, if it's missing entirely, `s` never had that character, so return `False` right away (this also avoids a `KeyError` on the next line).
- Otherwise, decrease that character's count, spending it like a budget.
- If any count ever drops below zero, `t` used more of that character than `s` had, so return `False`.
- Checking `len(s) != len(t)` first is a quick early exit: two strings of different lengths can never be anagrams, so there's no point building the dictionary at all.
- If both loops finish without any early return, every character's count balanced out exactly, so `s` and `t` are anagrams.

**Remember:** A hashmap can act as a shared "budget", build it up while scanning one string, spend it down while scanning the other, and if it ever goes negative or a key is missing, the strings don't match.

---

### Dry Run

#### Example 1: `s = "anagram"`, `t = "nagaram"`
Lengths match (7 == 7), so we proceed.

Building `count` from `s`:
| char | a | n | a | g | r | a | m |
|------|---|---|---|---|---|---|---|
| count after step | {a:1} | {a:1,n:1} | {a:2,n:1} | {a:2,n:1,g:1} | {a:2,n:1,g:1,r:1} | {a:3,n:1,g:1,r:1} | {a:3,n:1,g:1,r:1,m:1} |

Final `count = {a:3, n:1, g:1, r:1, m:1}`

Spending down using `t = "nagaram"`:
| char | in count? | count before | count after | negative? |
|------|-----------|--------------|-------------|-----------|
| n | yes | 1 | 0 | no |
| a | yes | 3 | 2 | no |
| g | yes | 1 | 0 | no |
| a | yes | 2 | 1 | no |
| r | yes | 1 | 0 | no |
| a | yes | 1 | 0 | no |
| m | yes | 1 | 0 | no |

No early return happened, so the function returns `True`.

#### Example 2: `s = "rat"`, `t = "car"`
Lengths match (3 == 3), so we proceed.

Building `count` from `s = "rat"`: `count = {r:1, a:1, t:1}`

Spending down using `t = "car"`:
| char | in count? | result |
|------|-----------|--------|
| c | no | `c` is not in `count`, return `False` immediately |

The function returns `False`.

---

### Complexity Analysis
- Time Complexity: O(n) - we scan `s` once to build the dictionary and `t` once to spend it down, where n is the length of the strings.
- Space Complexity: O(1) - since the strings only contain lowercase English letters, the dictionary holds at most 26 keys no matter how long the strings are.
