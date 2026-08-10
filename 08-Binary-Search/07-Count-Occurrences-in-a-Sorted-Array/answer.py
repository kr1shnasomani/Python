def lower_bound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def upper_bound(arr, n, x):
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

def count(arr: list[int], n: int, x: int) -> int:
    first = lower_bound(arr, n, x)

    if first == n or arr[first] != x:
        return 0

    last = upper_bound(arr, n, x)
    return last - first

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the sorted array: ").split()))
    x_input = int(input("Enter x: "))
    n_input = len(arr_input)
    print(count(arr_input, n_input, x_input))