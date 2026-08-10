# 15. Remove Outermost Parentheses

Source: `09-Strings/01-Remove-Outermost-Parentheses`

## Question

https://leetcode.com/problems/remove-outermost-parentheses

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: `s = P1 + P2 + ... + Pk`, where `Pi` are primitive valid parentheses strings.

Return `s` *after removing the outermost parentheses of every primitive string in the primitive decomposition of* `s`.

### Example 1

**Input:** `s = "(()())(())"`

**Output:** `"()()()"`

**Explanation:**
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

### Example 2

**Input:** `s = "(()())(())(()(()))"`

**Output:** `"()()()()(())"`

**Explanation:**
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

### Example 3

**Input:** `s = "()()"`

**Output:** `""`

**Explanation:**
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

### Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'('` or `')'`.
- `s` is a valid parentheses string.

## Solution

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_count = 0
        ans = []

        for ch in s:
            if ch == "(":
                if open_count > 0:
                    ans.append(ch)
                open_count += 1
            else:
                open_count -= 1
                if open_count > 0:
                    ans.append(ch)

        return "".join(ans)

if __name__ == "__main__":
    s_input = str(input("Enter the string: "))
    print(Solution().removeOuterParentheses(s_input))
```

## Approach

### Main Logic
```python
if ch == "(":
    if open_count > 0:
        ans.append(ch)
    open_count += 1
else:
    open_count -= 1
    if open_count > 0:
        ans.append(ch)
```
- `open_count` tracks how deeply nested the current position is, it goes up on every `(` and down on every `)`.
- For an opening bracket `(`, check `open_count` first. If it's already greater than 0, this bracket is sitting inside something else, so keep it. Only then increase `open_count`.
- For a closing bracket `)`, decrease `open_count` first, then check it. If it's still greater than 0, this bracket is also inside something else, so keep it.
- The order matters on purpose: check-before-increment for `(`, decrement-before-check for `)`. This makes sure the only brackets that ever get skipped are the ones that touch `open_count == 0`, which are exactly the outermost bracket of each primitive group.

**Remember:** A bracket is "outermost" exactly when it's the one crossing the boundary between depth 0 and depth 1, everything else is safely nested and gets kept.

---

### Dry Run

#### Example 1: `s = "(()())(())"`
| Char | open_count (Before) | Action | open_count (After) | ans |
|------|----------------------|--------|---------------------|-----|
| ( | 0 | 0 > 0? no → skip, then increment | 1 | [] |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | ['('] |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | ['(', ')'] |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | ['(', ')', '('] |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | ['(', ')', '(', ')'] |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | ['(', ')', '(', ')'] |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | ['(', ')', '(', ')'] |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | ['(', ')', '(', ')', '('] |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | ['(', ')', '(', ')', '(', ')'] |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | ['(', ')', '(', ')', '(', ')'] |

`"".join(ans)` → `"()()()"`

#### Example 2: `s = "(()())(())(()(()))"`
| Char | open_count (Before) | Action | open_count (After) | ans |
|------|----------------------|--------|---------------------|-----|
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "()()" |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "()()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()()(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()()" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "()()()" |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "()()()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()()()(" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()()()" |
| ( | 1 | 1 > 0? yes → append '(', then increment | 2 | "()()()()(" |
| ( | 2 | 2 > 0? yes → append '(', then increment | 3 | "()()()()((" |
| ) | 3 | decrement → 2, 2 > 0? yes → append ')' | 2 | "()()()()(()" |
| ) | 2 | decrement → 1, 1 > 0? yes → append ')' | 1 | "()()()()(())" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "()()()()(())" |

`"".join(ans)` → `"()()()()(())"`

#### Example 3: `s = "()()"`
| Char | open_count (Before) | Action | open_count (After) | ans |
|------|----------------------|--------|---------------------|-----|
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "" |
| ( | 0 | 0 > 0? no → skip, then increment | 1 | "" |
| ) | 1 | decrement → 0, 0 > 0? no → skip | 0 | "" |

`"".join(ans)` → `""`

---

### Complexity Analysis
- Time Complexity: O(n) - we scan the string once, doing constant work per character, where n is the length of `s`.
- Space Complexity: O(n) - the `ans` list can hold up to n characters in the worst case (excluding the output itself, extra space is O(1), just the `open_count` counter).
