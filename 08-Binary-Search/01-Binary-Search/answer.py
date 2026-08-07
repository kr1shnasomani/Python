from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return -1

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the sorted array: ").split()))
    target_input = int(input("Enter the target: "))
    print(Solution().search(nums_input, target_input))
