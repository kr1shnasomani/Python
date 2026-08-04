# Approach

## Main Logic

```python
if nums[i] == element:
    count += 1
else:
    count -= 1
    if count == 0:
        element = nums[i]
        count = 1
```

- Assume the first element is the majority candidate.
- If the current number matches the candidate, increase `count`.
- Otherwise, decrease `count` because the two different elements cancel each other.
- When `count` becomes `0`, choose the current number as the new candidate.

**Remember:** Different elements cancel each other. Since the majority element appears more than `n/2` times, it can never be completely cancelled.

---

## Key Concept: Boyer-Moore Voting Algorithm

This is a **greedy algorithm**: at every index, it makes the best decision it can with only the information seen so far (either strengthen the current candidate or cancel it out), and never looks back to reconsider earlier choices. Greedy algorithms don't always land on the correct answer for every problem, but they work here because the majority element can never be fully cancelled out, so the locally best choice at each step never conflicts with the final answer.

Think of each different pair of numbers as cancelling each other.

For example:

```text
[2, 1]
```

Since they are different, both get cancelled.

Now consider:

```text
[2, 2, 1]
```

Cancel one `2` with one `1`:

```text
[2]
```

One `2` is still left.

Since the majority element appears **more than half the time**, it will always have some occurrences left after all possible cancellations.

---

## Dry Run

### Example 1

**Input:** `nums = [3,2,3]`

Start:

```text
element = 3
count = 1
```

| Index | Current Number | Action | Candidate (`element`) | Count |
|:----:|:--------------:|:------:|:---------------------:|:-----:|
| 0 | 3 | Initial value | 3 | 1 |
| 1 | 2 | Different → `count - 1` | 3 | 0 |
|   |   | `count == 0`, choose new candidate | 2 | 1 |
| 2 | 3 | Different → `count - 1` | 2 | 0 |
|   |   | `count == 0`, choose new candidate | 3 | 1 |

Loop ends.

```text
Answer = 3
```

---

### Example 2

**Input:** `nums = [2,2,1,1,1,2,2]`

Start:

```text
element = 2
count = 1
```

| Index | Current Number | Action | Candidate (`element`) | Count |
|:----:|:--------------:|:------:|:---------------------:|:-----:|
| 0 | 2 | Initial value | 2 | 1 |
| 1 | 2 | Same → `count + 1` | 2 | 2 |
| 2 | 1 | Different → `count - 1` | 2 | 1 |
| 3 | 1 | Different → `count - 1` | 2 | 0 |
|   |   | `count == 0`, choose new candidate | 1 | 1 |
| 4 | 1 | Same → `count + 1` | 1 | 2 |
| 5 | 2 | Different → `count - 1` | 1 | 1 |
| 6 | 2 | Different → `count - 1` | 1 | 0 |
|   |   | `count == 0`, choose new candidate | 2 | 1 |

Loop ends.

```text
Answer = 2
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` - We traverse the array only once.
- **Space Complexity:** `O(1)` - Only two extra variables (`element` and `count`) are used.