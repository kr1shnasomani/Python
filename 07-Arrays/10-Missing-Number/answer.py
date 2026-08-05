from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    print(Solution().missingNumber(nums))
