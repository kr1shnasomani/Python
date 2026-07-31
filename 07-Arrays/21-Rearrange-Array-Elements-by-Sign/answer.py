from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        positive = 0
        negative = 1

        for num in nums:
            if num > 0:
                ans[positive] = num
                positive += 2
            else:
                ans[negative] = num
                negative += 2

        return ans

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     print(Solution().rearrangeArray(nums))
