from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the sorted array: ").split()))
#     target = int(input("Enter the target: "))
#     print(Solution().searchInsert(nums, target))
