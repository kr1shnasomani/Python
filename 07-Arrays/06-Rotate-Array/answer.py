from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse() #for right rotation place here for left rotation place in the end of code

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the array: ").split()))
#     k = int(input("Enter k: "))
#     print(Solution().rotate(nums, k))