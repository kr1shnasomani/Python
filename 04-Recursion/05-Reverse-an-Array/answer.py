from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    # nums.reverse()
    # return nums

    result = []
    for i in range(n - 1, -1, -1):
        result.append(nums[i])
    return result
    