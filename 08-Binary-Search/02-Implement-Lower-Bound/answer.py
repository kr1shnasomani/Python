def lowerBound(arr: list[int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    arr = list(map(int, input("Enter the sorted array: ").split()))
    n = len(arr)
    x = int(input("Enter x: "))
    print(lowerBound(arr, n, x))
