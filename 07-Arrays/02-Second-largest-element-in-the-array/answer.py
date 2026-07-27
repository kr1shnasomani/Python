def findSecondLargest(sequenceOfNumbers):
    n = len(sequenceOfNumbers)

    largest = float('-inf')
    slargest = float('-inf')

    for i in range(n):
        if sequenceOfNumbers[i] > largest:
            slargest = largest
            largest = sequenceOfNumbers[i]
        elif sequenceOfNumbers[i] > slargest and sequenceOfNumbers[i] != largest:
            slargest = sequenceOfNumbers[i]

    if slargest == float('-inf'):
        return -1

    return slargest

# if __name__ == "__main__":
#     sequenceOfNumbers = list(map(int, input("Enter the array: ").split()))
#     print(findSecondLargest(sequenceOfNumbers))
