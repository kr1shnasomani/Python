def bubbleSort(arr,n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the array: ").split()))
    n_input = len(arr_input)
    print(bubbleSort(arr_input, n_input))
