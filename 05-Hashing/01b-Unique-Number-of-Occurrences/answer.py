from typing import List

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

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    print(Solution().uniqueOccurrences(arr))
