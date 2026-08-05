def findSecondLargest(sequenceOfNumbers):
    largest = float('-inf')
    slargest = float('-inf')

    for num in sequenceOfNumbers:
        if num > largest:
            slargest = largest
            largest = num
        elif num > slargest and num != largest:
            slargest = num

    if slargest == float('-inf'):
        return -1

    return slargest

if __name__ == "__main__":
    sequenceOfNumbers = list(map(int, input("Enter the array: ").split()))
    print(findSecondLargest(sequenceOfNumbers))
