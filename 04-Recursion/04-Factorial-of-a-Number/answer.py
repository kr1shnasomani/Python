def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = n * factorial(n - 1)
    return result

# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     print(factorial(n))
