# Approach

## Main Logic
```python
sorted_keys = sorted(count, key=count.get, reverse=True)
result.append(char * count[char])
```
- After building a frequency dictionary `count` (same counting technique used earlier: loop through `s`, increment a character's count if seen before, otherwise start it at 1), sort its keys, the characters themselves, directly.
- `sorted(count, key=count.get, reverse=True)` walks through the characters in `count` and, for each one, looks up its frequency using `count.get` to decide the sort order, instead of sorting the characters alphabetically.
- `reverse=True` flips the order so the most frequent character comes first.
- Then loop through `sorted_keys`, and for each `char`, repeat it `count[char]` times using `char * count[char]`, and add the chunk to the result list.
- Finally, join all the chunks together into one string.

**Remember:** `sorted()`'s `key` parameter lets you sort by any property you choose (here, frequency looked up via `count.get`) instead of the natural order of the items themselves.

---

## Dry Run

### Example 1: `s = "tree"`
Building `count`:
| char | t | r | e | e |
|------|---|---|---|---|
| count after step | {t:1} | {t:1,r:1} | {t:1,r:1,e:1} | {t:1,r:1,e:2} |

`sorted_keys` = `sorted(count, key=count.get, reverse=True)` → `['e', 't', 'r']` (e has freq 2; t and r tie at freq 1, keeping their original relative order)

Building `result`:
| char | count[char] | char * count[char] | result so far |
|------|-------------|----------------------|----------------|
| e | 2 | "ee" | ["ee"] |
| t | 1 | "t" | ["ee", "t"] |
| r | 1 | "r" | ["ee", "t", "r"] |

`"".join(result)` → `"eetr"` (a valid answer, matching the problem's own note that "eetr" is acceptable)

### Example 2: `s = "cccaaa"`
Building `count`:
| char | c | c | c | a | a | a |
|------|---|---|---|---|---|---|
| count after step | {c:1} | {c:2} | {c:3} | {c:3,a:1} | {c:3,a:2} | {c:3,a:3} |

`sorted_keys` = `sorted(count, key=count.get, reverse=True)` → `['c', 'a']` (tie on frequency 3, original order kept)

Building `result`:
| char | count[char] | char * count[char] | result so far |
|------|-------------|----------------------|----------------|
| c | 3 | "ccc" | ["ccc"] |
| a | 3 | "aaa" | ["ccc", "aaa"] |

`"".join(result)` → `"cccaaa"` (a valid answer, since the problem accepts either "cccaaa" or "aaaccc")

### Example 3: `s = "Aabb"`
Building `count`:
| char | A | a | b | b |
|------|---|---|---|---|
| count after step | {A:1} | {A:1,a:1} | {A:1,a:1,b:1} | {A:1,a:1,b:2} |

`sorted_keys` = `sorted(count, key=count.get, reverse=True)` → `['b', 'A', 'a']` (b has freq 2; A and a tie at freq 1, keeping their original relative order)

Building `result`:
| char | count[char] | char * count[char] | result so far |
|------|-------------|----------------------|----------------|
| b | 2 | "bb" | ["bb"] |
| A | 1 | "A" | ["bb", "A"] |
| a | 1 | "a" | ["bb", "A", "a"] |

`"".join(result)` → `"bbAa"`

---

## Complexity Analysis
- Time Complexity: O(n + k log k) - counting takes O(n), sorting the k distinct characters takes O(k log k), and building the result takes O(n). Since `s` only has letters and digits, k ≤ 62 here, so the sort is effectively constant time and the total stays close to O(n).
- Space Complexity: O(n) - the `count` dictionary holds at most k (≤ 62) entries, but the `result` list scales with the input size.
