# 19. Isomorphic String

Source: `09-Strings/05-Isomorphic-Strings`

## Question

https://leetcode.com/problems/isomorphic-strings

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

### Example 1

**Input:** `s = "egg"`, `t = "add"`
**Output:** `true`

**Explanation:**

The strings `s` and `t` can be made identical by:

- Mapping `'e'` to `'a'`.
- Mapping `'g'` to `'d'`.

### Example 2

**Input:** `s = "f11"`, `t = "b23"`
**Output:** `false`

**Explanation:**

The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

### Example 3

**Input:** `s = "paper"`, `t = "title"`
**Output:** `true`

### Constraints

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ASCII character.

## Solution

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in s_to_t:
                if s_to_t[ch1] != ch2:
                    return False

            if ch2 in t_to_s:
                if t_to_s[ch2] != ch1:
                    return False

            s_to_t[ch1] = ch2
            t_to_s[ch2] = ch1

        return True

if __name__ == "__main__":
    s_input = str(input("Enter first string: "))
    t_input = str(input("Enter second string: "))
    print(Solution().isIsomorphic(s_input, t_input))
```

## Approach

### Main Logic
```python
if ch1 in s_to_t:
    if s_to_t[ch1] != ch2:
        return False

if ch2 in t_to_s:
    if t_to_s[ch2] != ch1:
        return False

s_to_t[ch1] = ch2
t_to_s[ch2] = ch1
```
- Two dictionaries track the mapping in both directions: `s_to_t` maps a character in `s` to the character it lines up with in `t`, and `t_to_s` maps the other way around.
- At each position `i`, take the matching pair `ch1 = s[i]` and `ch2 = t[i]`.
- If `ch1` was already mapped before, it must map to the same `ch2` again, otherwise `s` is trying to send the same character to two different places, so return `False`.
- If `ch2` was already mapped before, it must map back to the same `ch1` again, otherwise two different characters in `s` are trying to map to the same character in `t`, so return `False`.
- If both checks pass, record the mapping in both dictionaries and move to the next position.

**Remember:** Checking both directions is what enforces a strict one-to-one mapping, a single dictionary would only catch half the violations.

---

### Key Concept
**Two-way hashmap mapping for one-to-one correspondence**
- When you need to confirm that two sequences match up character by character with a strict one-to-one relationship (a bijection), one dictionary isn't enough.
- A single dictionary going only from `s` to `t` can catch "the same source character maps to two different targets", but it can't catch "two different source characters map to the same target".
- Using two dictionaries, one for each direction, covers both cases at once.
- This pattern is useful anytime you need to verify a strict one-to-one matching between two sequences, not just "does a valid mapping exist".

---

### Dry Run

#### Example 1: `s = "egg"`, `t = "add"`
| i | ch1 | ch2 | check s_to_t | check t_to_s | action | s_to_t after | t_to_s after |
|---|-----|-----|--------------|---------------|--------|---------------|---------------|
| 0 | e | a | 'e' not seen | 'a' not seen | map both ways | {e:a} | {a:e} |
| 1 | g | d | 'g' not seen | 'd' not seen | map both ways | {e:a, g:d} | {a:e, d:g} |
| 2 | g | d | 'g' seen, maps to 'd' ✓ | 'd' seen, maps to 'g' ✓ | re-confirm same mapping | {e:a, g:d} | {a:e, d:g} |

Loop finishes with no mismatch, return `True`.

#### Example 2: `s = "f11"`, `t = "b23"`
| i | ch1 | ch2 | check s_to_t | check t_to_s | action | s_to_t after | t_to_s after |
|---|-----|-----|--------------|---------------|--------|---------------|---------------|
| 0 | f | b | 'f' not seen | 'b' not seen | map both ways | {f:b} | {b:f} |
| 1 | 1 | 2 | '1' not seen | '2' not seen | map both ways | {f:b, 1:2} | {b:f, 2:1} |
| 2 | 1 | 3 | '1' seen, maps to '2', but ch2 is '3' ✗ | - | mismatch, return `False` | - | - |

#### Example 3: `s = "paper"`, `t = "title"`
| i | ch1 | ch2 | check s_to_t | check t_to_s | action | s_to_t after | t_to_s after |
|---|-----|-----|--------------|---------------|--------|---------------|---------------|
| 0 | p | t | 'p' not seen | 't' not seen | map both ways | {p:t} | {t:p} |
| 1 | a | i | 'a' not seen | 'i' not seen | map both ways | {p:t, a:i} | {t:p, i:a} |
| 2 | p | t | 'p' seen, maps to 't' ✓ | 't' seen, maps to 'p' ✓ | re-confirm same mapping | {p:t, a:i} | {t:p, i:a} |
| 3 | e | l | 'e' not seen | 'l' not seen | map both ways | {p:t, a:i, e:l} | {t:p, i:a, l:e} |
| 4 | r | e | 'r' not seen | 'e' not seen | map both ways | {p:t, a:i, e:l, r:e} | {t:p, i:a, l:e, e:r} |

Loop finishes with no mismatch, return `True`.

---

### Complexity Analysis
- Time Complexity: O(n) - a single pass through the strings, where n is the length of `s` (equal to the length of `t`).
- Space Complexity: O(n) in general, since the two dictionaries can grow with the number of distinct character pairs seen. Since the input is restricted to ASCII characters (128 possible values), each dictionary holds at most 128 entries, a constant, so auxiliary space is effectively O(1).
