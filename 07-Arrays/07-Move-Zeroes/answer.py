from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     print(Solution().moveZeroes(nums))