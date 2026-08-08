# Pending — DSA Repo Tracker

Living checklist for what's left to solve/write up. Update this whenever a folder gets solved or scaffolded.

## Notes & Preferences

- **Python level:** beginner — avoid `zip`/`enumerate` in `answer.py`; use plain `range(len(...))` indexing.
  - Reverted from `enumerate`/`zip` back to `range(len(...))` in `05-Hashing/03-Frequency-of-the-Most-Frequent-Element`, `07-Arrays/14-Longest-Subarray-With-Sum-K`, `09-Strings/05-Isomorphic-Strings` after a pylint cleanup pass overwrote this. Pylint will flag `range(len(...))` again (C0200, consider-using-enumerate) if re-linted — that's expected, leave it, revisit once comfortable.
- **Swap style:** use `a, b = b, a` tuple swap, not a `temp` variable.
- **approach.md style:** keep prose plain/light, not text-heavy, even when dry runs are thorough.
- An `approach.md` never exists without a solved `answer.py` in this repo — solve first, then write the approach.

## Unsolved — both `answer.py` and `approach.md` blank (22 folders)

**Hashing**
- [ ] `05-Hashing/02-Counting-Frequencies-of-Array-Elements`

**Arrays**
- [ ] `07-Arrays/13-Subarray-Sum-Equals-K`
- [ ] `07-Arrays/22-Next-Permutation`
- [ ] `07-Arrays/23-Leaders-in-an-Array`
- [ ] `07-Arrays/24-Longest-Consecutive-Sequence`

**Binary Search**
- [ ] `08-Binary-Search/05-Floor-and-Ceil-in-Sorted-Array`
- [ ] `08-Binary-Search/07-Count-Occurrences-in-a-Sorted-Array`
- [ ] `08-Binary-Search/09-Search-in-Rotated-Sorted-Array-II`
- [ ] `08-Binary-Search/11-Find-out-how-many-times-the-array-is-rotated`
- [ ] `08-Binary-Search/12-Single-Element-in-a-Sorted-Array`
- [ ] `08-Binary-Search/13-Find-Peak-Element`
- [ ] `08-Binary-Search/14-Sqrt(x)`
- [ ] `08-Binary-Search/15-Find-Nth-Root-Of-M`
- [ ] `08-Binary-Search/16-Koko-Eating-Bananas`
- [ ] `08-Binary-Search/18-Find-the-Smallest-Divisor-Given-a-Threshold`
- [ ] `08-Binary-Search/19-Capacity-To-Ship-Packages-Within-D-Days`
- [ ] `08-Binary-Search/28-Row-with-max-1s`
- [ ] `08-Binary-Search/29-Search-a-2D-Matrix`

**Strings**
- [ ] `09-Strings/11-String-to-Integer-(atoi)`
- [ ] `09-Strings/12-Count-With-K-Different-Characters`
- [ ] `09-Strings/13-Longest-Palindromic-Substring`
- [ ] `09-Strings/14-Sum-of-Beauty-of-All-Substrings`

## Solved but missing `approach.md` (7 folders)

- [ ] `05-Hashing/03-Frequency-of-the-Most-Frequent-Element`
- [ ] `07-Arrays/14-Longest-Subarray-With-Sum-K`
- [ ] `07-Arrays/25-Set-Matrix-Zeroes`
- [ ] `07-Arrays/26-Rotate-Image`
- [ ] `08-Binary-Search/03-Implement-Upper-Bound`
- [ ] `08-Binary-Search/06-Find-First-and-Last-Position-of-Element-in-Sorted-Array`
- [ ] `08-Binary-Search/08-Search-in-Rotated-Sorted-Array`

## Empty topic folders (no problems scaffolded yet)

- `10-Linked-List`
- `12-Bit-Manupilation`
- `13-Stack-and-Queues`
- `14-Sliding-Window-and-Two-Pointer`
- `15-Heaps`
