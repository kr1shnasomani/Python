from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        total = 0
        result = 0

        for right in range(len(nums)):
            total = total + nums[right]

            while nums[right] * (right - left + 1) - total > k:
                total = total - nums[left]
                left = left + 1

            result = max(result, right - left + 1)

        return result

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     k = int(input("Enter k: "))
#     print(Solution().maxFrequency(nums, k))
