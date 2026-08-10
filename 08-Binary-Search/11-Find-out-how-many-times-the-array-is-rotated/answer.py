def findKRotation(arr : list[int]) -> int:
    n = len(arr)

    low = 0
    high = n - 1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            low = mid + 1
        else:
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]
            high = mid - 1

    return index