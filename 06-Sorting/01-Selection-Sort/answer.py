def selectionSort(arr, n):
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the array: ").split()))
    n_input = len(arr_input)
    print(selectionSort(arr_input, n_input))
