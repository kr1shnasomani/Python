from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     print(Solution().check(nums))
