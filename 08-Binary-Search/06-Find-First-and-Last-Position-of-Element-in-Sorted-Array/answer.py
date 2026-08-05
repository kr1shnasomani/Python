from typing import List

class Solution:
    def lowerBound(self, nums: List[int], n: int, target: int) -> int:
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

    def upperBound(self, nums: List[int], n: int, target: int) -> int:
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        lb = self.lowerBound(nums, n, target)
        ub = self.upperBound(nums, n, target)

        if lb == n or nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]

if __name__ == "__main__":
    nums = list(map(int, input("Enter the sorted array: ").split()))
    target = int(input("Enter the target: "))
    print(Solution().searchRange(nums, target))
