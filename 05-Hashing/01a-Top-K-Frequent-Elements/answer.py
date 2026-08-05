from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n in count:
                count[n] = count[n] + 1
            else:
                count[n] = 1

        result = sorted(count, key=lambda n: count[n], reverse=True)

        return result[:k]

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter k: "))
    print(Solution().topKFrequent(nums, k))
