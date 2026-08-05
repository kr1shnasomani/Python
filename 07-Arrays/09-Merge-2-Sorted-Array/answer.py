def sortedArray(a: list[int], b: list[int]) -> list[int]:
    n = len(a)
    m = len(b)

    i = 0
    j = 0

    union = []

    while i < n and j < m:
        if a[i] < b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1

        elif a[i] > b[j]:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1

        else:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
            j += 1

    while i < n:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    while j < m:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1

    return union

if __name__ == "__main__":
    a = list(map(int, input("Enter the first sorted array: ").split()))
    b = list(map(int, input("Enter the second sorted array: ").split()))
    print(sortedArray(a, b))
