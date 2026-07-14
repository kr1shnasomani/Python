class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        req = n // 2

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

        # if asked to find if majority element exist or not
        # check = 0

        # for num in nums:
        #     if num == element:
        #         check += 1

        # if check > req:
        #     return element
        # else:
        #     return -1