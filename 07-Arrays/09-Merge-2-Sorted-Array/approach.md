# Approach

## Main Logic

```python
if not union or union[-1] != a[i]:
    union.append(a[i])
```

- Compare `a[i]` and `b[j]`. Whichever is smaller gets added to `union` first, and that pointer moves forward. If they're equal, add the value once and move both pointers.
- Before adding any value, check if it's the same as the last value already in `union`. Since both arrays are sorted, any duplicate of a value already added would always show up right next to it, so this one check is enough to keep `union` free of duplicates.
- Once one array runs out, the other may still have leftover elements. Walk through whatever remains and add each one, still applying the same duplicate check.

**Remember:** Because `a` and `b` are already sorted, merging them with two pointers naturally produces a sorted result. The only extra step is skipping a value if it matches the last one already added.

---

## Dry Run

### Example 1

**Input**

```text
a = [1, 2, 3, 4, 6], b = [2, 3, 5]
```

| Step | i | a[i] | j | b[j] | Decision | Union After |
|------|---|------|---|------|----------|--------------|
| 1 | 0 | 1 | 0 | 2 | 1 < 2 → append 1, i→1 | [1] |
| 2 | 1 | 2 | 0 | 2 | equal → append 2, i→2, j→1 | [1, 2] |
| 3 | 2 | 3 | 1 | 3 | equal → append 3, i→3, j→2 | [1, 2, 3] |
| 4 | 3 | 4 | 2 | 5 | 4 < 5 → append 4, i→4 | [1, 2, 3, 4] |
| 5 | 4 | 6 | 2 | 5 | 6 > 5 → append 5, j→3 | [1, 2, 3, 4, 5] |

Main loop ends here since `j` reached `m = 3`.

**Flush remaining `a`**

| Step | i | a[i] | Decision | Union After |
|------|---|------|----------|--------------|
| 6 | 4 | 6 | 6 ≠ last (5) → append 6, i→5 | [1, 2, 3, 4, 5, 6] |

`i` now reaches `n = 5`, nothing left in `b` either, so the merge is done.

**Output**

```text
[1, 2, 3, 4, 5, 6]
```

---

### Example 2

**Input**

```text
a = [1, 2, 3, 3], b = [2, 2, 4]
```

| Step | i | a[i] | j | b[j] | Decision | Union After |
|------|---|------|---|------|----------|--------------|
| 1 | 0 | 1 | 0 | 2 | 1 < 2 → append 1, i→1 | [1] |
| 2 | 1 | 2 | 0 | 2 | equal → append 2, i→2, j→1 | [1, 2] |
| 3 | 2 | 3 | 1 | 2 | 3 > 2 → 2 = last (2) → skip, j→2 | [1, 2] |
| 4 | 2 | 3 | 2 | 4 | 3 < 4 → append 3, i→3 | [1, 2, 3] |
| 5 | 3 | 3 | 2 | 4 | 3 < 4 → 3 = last (3) → skip, i→4 | [1, 2, 3] |

Main loop ends here since `i` reached `n = 4`.

**Flush remaining `b`**

| Step | j | b[j] | Decision | Union After |
|------|---|------|----------|--------------|
| 6 | 2 | 4 | 4 ≠ last (3) → append 4, j→3 | [1, 2, 3, 4] |

`j` now reaches `m = 3`, nothing left in `a` either, so the merge is done.

**Output**

```text
[1, 2, 3, 4]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n + m)` - each pointer only moves forward, so `i` and `j` together take at most `n + m` steps across the whole array.
- **Space Complexity:** `O(n + m)` - in the worst case, none of the elements repeat and every one of them ends up stored in `union`.
