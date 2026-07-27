def upperBound(arr: [int], x: int, n: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

# if __name__ == "__main__":
#     arr = list(map(int, input("Enter the sorted array: ").split()))
#     x = int(input("Enter x: "))
#     n = len(arr)
#     print(upperBound(arr, x, n))
