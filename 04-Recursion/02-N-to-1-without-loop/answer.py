def printNos(x: int) -> list[int]:
    if x == 0:
        return []

    result = [x] + printNos(x - 1)
    return result

if __name__ == "__main__":
    x = int(input())
    print(printNos(x))