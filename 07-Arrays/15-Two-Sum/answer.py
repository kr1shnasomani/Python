from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     target = int(input("Enter the target: "))
#     print(Solution().twoSum(nums, target))
