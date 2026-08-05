def printNos(x):
    if x == 0:
        return []

    result = printNos(x - 1)
    result.append(x)
    return result

if __name__ == "__main__":
    x = int(input())
    print(printNos(x))
