# Approach

## Main Logic
```python
return goal in (s+s)
```
- Stick `s` to itself to make `s+s`.
- Check whether `goal` shows up anywhere inside `s+s` as a contiguous substring.
- The `len(s) != len(goal)` guard above this runs first, this matters because without it, a shorter `goal` could accidentally match a chunk of `s+s` without actually being a full rotation of `s`.

**Remember:** If `goal` is a substring of `s+s`, then `goal` is guaranteed to be some rotation of `s`, no need to manually try every shift.

---

## Key Concept
**The string doubling trick for rotations**
- A "rotation" of `s` moves characters from the front to the back, wrapping around the end back to the start.
- If you write `s` twice in a row (`s+s`), every possible rotation of `s` appears as a contiguous substring somewhere inside it, because the doubled string simulates the wrap-around that a single copy of `s` can't represent on its own.
- Example: `s = "abcde"`, so `s+s = "abcdeabcde"`. Every rotation, `"abcde"`, `"bcdea"`, `"cdeab"`, `"deabc"`, `"eabcd"`, can be found by sliding a window of length 5 across `s+s`.
- This turns "try every possible shift and compare" into a single substring search, which Python's `in` operator already does efficiently.

---

## Dry Run

### Example 1: `s = "abcde"`, `goal = "cdeab"`
- `len(s) == len(goal)` → both 5, so continue.
- `s+s` = `"abcdeabcde"`
- Search for `"cdeab"` inside `"abcdeabcde"`:

| Index | Substring of length 5 |
|-------|------------------------|
| 0 | "abcde" |
| 1 | "bcdea" |
| 2 | "cdeab" ← match! |

`"cdeab"` is found starting at index 2, so return `True`.

### Example 2: `s = "abcde"`, `goal = "abced"`
- `len(s) == len(goal)` → both 5, so continue.
- `s+s` = `"abcdeabcde"`
- Search for `"abced"` inside `"abcdeabcde"`:

| Index | Substring of length 5 |
|-------|------------------------|
| 0 | "abcde" |
| 1 | "bcdea" |
| 2 | "cdeab" |
| 3 | "deabc" |
| 4 | "eabcd" |

None of these equal `"abced"` (its last two letters are swapped compared to any real rotation), so return `False`.

---

## Complexity Analysis
- Time Complexity: O(n) - building `s+s` takes O(n), and Python's substring search runs in roughly O(n) for strings of this size, where n is the length of `s`.
- Space Complexity: O(n) - `s+s` creates a new string of length `2n`.
