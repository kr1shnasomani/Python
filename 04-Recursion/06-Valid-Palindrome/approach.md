# Approach

## Main Logic

```python
if left >= right:
    return True

if not s[left].isalnum():
    return check(left + 1, right)

if not s[right].isalnum():
    return check(left, right - 1)

if s[left].lower() != s[right].lower():
    return False

return check(left + 1, right - 1)
```

- If the pointers meet or cross, every comparison has matched, so return `True`.
- If the left character is not a letter or number, skip it.
- If the right character is not a letter or number, skip it.
- If the characters do not match (ignoring uppercase/lowercase), return `False`.
- Otherwise, move both pointers inward and continue recursively.

**Remember:** Compare only letters and numbers. Ignore spaces and punctuation.

---

## Dry Run

### Example 1

**Input:**

```text
s = "A man, a plan, a canal: Panama"
```

```text
check(0, 29)

left = 'A'
right = 'a'

'A'.lower() == 'a'.lower() ✓

↓

check(1, 28)

left = ' '
Not alphanumeric

↓

check(2, 28)

left = 'm'
right = 'm'

Match ✓

↓

check(3, 27)

left = 'a'
right = 'a'

Match ✓

↓

check(4, 26)

left = 'n'
right = 'n'

Match ✓

↓

check(5, 25)

left = ','
Not alphanumeric

↓

check(6, 25)

left = ' '
Not alphanumeric

↓

check(7, 25)

left = 'a'
right = 'a'

Match ✓

↓

check(8, 24)

left = ' '
Not alphanumeric

↓

check(9, 24)

left = 'p'
right = ':'

right is not alphanumeric

↓

check(9, 23)

left = 'p'
right = ' '

right is not alphanumeric

↓

check(9, 22)

left = 'p'
right = 'P'

'p'.lower() == 'P'.lower() ✓

↓

check(10, 21)

left = 'l'
right = ' '

right is not alphanumeric

↓

check(10, 20)

left = 'l'
right = 'l'

Match ✓

↓

check(11, 19)

left = 'a'
right = 'a'

Match ✓

↓

check(12, 18)

left = 'n'
right = 'n'

Match ✓

↓

check(13, 17)

left = ','
Not alphanumeric

↓

check(14, 17)

left = ' '
Not alphanumeric

↓

check(15, 17)

left = 'a'
right = 'a'

Match ✓

↓

check(16, 16)

left >= right

↓

Return True
```

**Output:**

```text
True
```

---

### Example 2

**Input:**

```text
s = "race a car"
```

```text
check(0, 9)

left = 'r'
right = 'r'

Match ✓

↓

check(1, 8)

left = 'a'
right = 'a'

Match ✓

↓

check(2, 7)

left = 'c'
right = 'c'

Match ✓

↓

check(3, 6)

left = 'e'
right = ' '

right is not alphanumeric

↓

check(3, 5)

left = 'e'
right = 'a'

'e' != 'a'

↓

Return False
```

**Output:**

```text
False
```

---

### Example 3

**Input:**

```text
s = " "
```

```text
check(0, 0)

left >= right

↓

Return True
```

**Output:**

```text
True
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` (each character is visited at most once)
- **Space Complexity:** `O(n)` (recursive call stack)