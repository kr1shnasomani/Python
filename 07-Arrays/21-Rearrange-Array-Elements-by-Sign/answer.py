from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        positive = 0
        negative = 1

        for i in range(n):
            if nums[i] > 0:
                ans[positive] = nums[i]
                positive += 2
            else:
                ans[negative] = nums[i]
                negative += 2

        return ans

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     print(Solution().rearrangeArray(nums))
