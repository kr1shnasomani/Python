from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    print(Solution().moveZeroes(nums_input))
