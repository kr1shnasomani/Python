# Approach

## Main Logic
```python
if prices[i] > best_buy:
    today_profit = prices[i] - best_buy
    max_profit = max(max_profit, today_profit)

best_buy = min(best_buy, prices[i])
```
- `best_buy` tracks the lowest price seen so far, the best day to have bought up to this point. It starts at `prices[0]`.
- `max_profit` tracks the best profit found so far, starting at 0.
- For every price, first check if selling today would beat the lowest price seen so far. If it would, that's a valid profit, so calculate it and update `max_profit` if it's the best one yet.
- Then, no matter what, update `best_buy` to be the smaller of itself and today's price, since an even cheaper buying day could lead to a bigger profit later.
- Because `best_buy` is updated on every single day, by the time you reach any given day it always holds the lowest price among all the days before it, so the profit check is always comparing against the best possible buying day so far.

**Remember:** One pass is enough because you only need two things at any moment: the cheapest price seen so far, and the best profit selling today against that price would give you.

---

## Dry Run

### Example 1: `prices = [7, 1, 5, 3, 6, 4]`
Start: `best_buy = 7`, `max_profit = 0`

| i | prices[i] | prices[i] > best_buy? | today_profit | max_profit | best_buy after |
|---|-----------|------------------------|---------------|-------------|------------------|
| 0 | 7 | 7 > 7? no | - | 0 | min(7, 7) = 7 |
| 1 | 1 | 1 > 7? no | - | 0 | min(7, 1) = 1 |
| 2 | 5 | 5 > 1? yes | 5 - 1 = 4 | max(0, 4) = 4 | min(1, 5) = 1 |
| 3 | 3 | 3 > 1? yes | 3 - 1 = 2 | max(4, 2) = 4 | min(1, 3) = 1 |
| 4 | 6 | 6 > 1? yes | 6 - 1 = 5 | max(4, 5) = 5 | min(1, 6) = 1 |
| 5 | 4 | 4 > 1? yes | 4 - 1 = 3 | max(5, 3) = 5 | min(1, 4) = 1 |

Return `max_profit` → `5`.

### Example 2: `prices = [7, 6, 4, 3, 1]`
Start: `best_buy = 7`, `max_profit = 0`

| i | prices[i] | prices[i] > best_buy? | today_profit | max_profit | best_buy after |
|---|-----------|------------------------|---------------|-------------|------------------|
| 0 | 7 | 7 > 7? no | - | 0 | min(7, 7) = 7 |
| 1 | 6 | 6 > 7? no | - | 0 | min(7, 6) = 6 |
| 2 | 4 | 4 > 6? no | - | 0 | min(6, 4) = 4 |
| 3 | 3 | 3 > 4? no | - | 0 | min(4, 3) = 3 |
| 4 | 1 | 1 > 3? no | - | 0 | min(3, 1) = 1 |

Return `max_profit` → `0`, prices only ever dropped, so no profitable buy-then-sell exists.

---

## Complexity Analysis
- Time Complexity: O(n) - a single pass through `prices`, where n is the number of days.
- Space Complexity: O(1) - only `best_buy` and `max_profit` are kept, no extra data structures.
