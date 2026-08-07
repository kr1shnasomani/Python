def linearSearch(n: int, num: int, arr: list[int]) -> int:
    for i in range(n):
        if arr[i] == num:
            return i

    return -1

if __name__ == "__main__":
    arr_input = list(map(int, input("Enter the array: ").split()))
    n_input = len(arr_input)
    num_input = int(input("Enter the number to search: "))
    print(linearSearch(n_input, num_input, arr_input))
