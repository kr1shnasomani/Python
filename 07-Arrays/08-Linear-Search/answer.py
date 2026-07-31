def linearSearch(n: int, num: int, arr: list[int]) -> int:
    for i in range(n):
        if arr[i] == num:
            return i

    return -1

# if __name__ == "__main__":
#     arr = list(map(int, input("Enter the array: ").split()))
#     n = len(arr)
#     num = int(input("Enter the number to search: "))
#     print(linearSearch(n, num, arr))
