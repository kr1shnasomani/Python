def insertionSort(arr, n):
    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = current

    return arr

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the array: ").split()))
    n_input = len(arr_input)
    print(insertionSort(arr_input, n_input))
