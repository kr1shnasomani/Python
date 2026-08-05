def largestElement(arr: list[int], n: int) -> int:
    largest = arr[0]

    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    return largest

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    n = len(arr)
    print(largestElement(arr, n))
