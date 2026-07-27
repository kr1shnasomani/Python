from typing import List
import math

def printDivisors(n: int) -> List[int]:
    result = []
    x = int(math.sqrt(n))

    for i in range(1, x + 1):
        if n % i == 0:
            result.append(i)

            if i != (n // i):
                result.append(n // i)

    result.sort()
    return result

# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     print(printDivisors(n))
