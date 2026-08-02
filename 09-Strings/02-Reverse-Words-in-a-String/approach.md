# Approach

## Main Logic
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

## Dry Run

### Example 1: `s = "the sky is blue"`
| Step | Operation | Result |
|------|-----------|--------|
| 1 | `s.split()` | `["the", "sky", "is", "blue"]` |
| 2 | `.reverse()` | `["blue", "is", "sky", "the"]` |
| 3 | `" ".join(...)` | `"blue is sky the"` |

### Example 2: `s = "  hello world  "`
| Step | Operation | Result |
|------|-----------|--------|
| 1 | `s.split()` | `["hello", "world"]` (leading/trailing spaces dropped) |
| 2 | `.reverse()` | `["world", "hello"]` |
| 3 | `" ".join(...)` | `"world hello"` |

### Example 3: `s = "a good   example"`
| Step | Operation | Result |
|------|-----------|--------|
| 1 | `s.split()` | `["a", "good", "example"]` (extra spaces collapsed) |
| 2 | `.reverse()` | `["example", "good", "a"]` |
| 3 | `" ".join(...)` | `"example good a"` |

---

## Complexity Analysis
- Time Complexity: O(n) - we scan the string once to split it and once more to join it back, where n is the length of `s`.
- Space Complexity: O(n) - the list of words and the final joined string both take space proportional to the input.
