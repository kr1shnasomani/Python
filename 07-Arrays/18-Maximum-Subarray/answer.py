from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum = current_sum + nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    print(Solution().maxSubArray(nums))