from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        low = 0
        mid = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp

                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp

                high -= 1

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array (0s, 1s, 2s): ").split()))
#     Solution().sortColors(nums)
#     print(nums)
