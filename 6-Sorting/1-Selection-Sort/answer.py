def selectionSort(arr, n):
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp