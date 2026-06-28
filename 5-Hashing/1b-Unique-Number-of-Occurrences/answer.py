class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for num in arr:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1

        occur = count.values()

        return len(occur) == len(set(occur))
