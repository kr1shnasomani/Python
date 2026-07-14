class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse() #for right rotation place here for left rotation place in the end of code

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])