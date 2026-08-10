def find_floor(a, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] <= x:
            ans = a[mid]
            low = mid + 1
        else:
            high = mid - 1

    return ans

def find_ceil(a, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] >= x:
            ans = a[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ans

def getFloorAndCeil(a, n, x):
    floor = find_floor(a, n, x)
    ceil = find_ceil(a, n, x)
    return [floor, ceil]

if __name__ == "__main__":
    a_input = list(map(int, input("Enter the sorted array: ").split()))
    x_input = int(input("Enter x: "))
    n_input = len(a_input)
    print(getFloorAndCeil(a_input, n_input, x_input))
