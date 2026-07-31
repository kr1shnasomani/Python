from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        element = nums[0]
        count = 1

        for i in range(1, n):
            if nums[i] == element:
                count += 1
            else:
                count -= 1
                if count == 0:
                    element = nums[i]
                    count = 1

        return element

        # check = 0

        # for num in nums:
        #     if num == element:
        #         check += 1

        # if check > n // 2:
        #     return element
        # else:
        #     return -1

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     print(Solution().majorityElement(nums))
