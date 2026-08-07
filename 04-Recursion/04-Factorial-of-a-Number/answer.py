def factorial(n):
    if n in (0, 1):
        return 1

    result = n * factorial(n - 1)
    return result

if __name__ == "__main__":
    n_input = int(input("Enter a number: "))
    print(factorial(n_input))
