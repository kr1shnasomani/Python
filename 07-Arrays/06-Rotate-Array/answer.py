from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse() #for right rotation place here for left rotation place in the end of code

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        return nums

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    k_input = int(input("Enter k: "))
    print(Solution().rotate(nums_input, k_input))
