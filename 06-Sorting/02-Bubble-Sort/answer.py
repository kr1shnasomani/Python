def bubbleSort(arr,n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

# if __name__ == "__main__":
#     arr = list(map(int, input("Enter the array: ").split()))
#     n = len(arr)
#     print(bubbleSort(arr, n))