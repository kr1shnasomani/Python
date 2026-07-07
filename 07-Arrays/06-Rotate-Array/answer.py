class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse()

        temp = nums[:k]
        temp.reverse()
        nums[:k] = temp

        temp = nums[k:]
        temp.reverse()
        nums[k:] = temp