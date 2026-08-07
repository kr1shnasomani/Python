from typing import List

def reverseArray(n: int, nums: List[int]) -> List[int]:
    def reverse(left: int, right: int):
        if left >= right:
            return

        nums[left], nums[right] = nums[right], nums[left]
        reverse(left + 1, right - 1)

    reverse(0, n - 1)
    return nums

if __name__ == "__main__":
    nums_input = list(map(int, input("Enter the array: ").split()))
    n_input = len(nums_input)
    print(reverseArray(n_input, nums_input))
