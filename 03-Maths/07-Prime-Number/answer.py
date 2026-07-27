import math

def isPrime(n):
    if n <= 1:
        return False

    x = int(math.sqrt(n))
    for i in range(2, x + 1):
        if n % i == 0:
            return False

    return True

# if __name__ == "__main__":
#     n = int(input())
#     print(isPrime(n))
