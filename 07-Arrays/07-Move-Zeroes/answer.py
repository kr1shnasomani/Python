from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     Solution().moveZeroes(nums)
#     print(nums)
