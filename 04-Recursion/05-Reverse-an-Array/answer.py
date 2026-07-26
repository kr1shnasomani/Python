from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    result = []
    for i in range(n - 1, -1, -1):
        result.append(nums[i])
    return result

# if __name__ == "__main__":
#     n = int(input("Enter the size of the array: "))
#     nums = list(map(int, input("Enter the elements of the array: ").split()))
#     print(reverseArray(n, nums))