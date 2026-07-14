def countDigits(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# if __name__ == '__main__':
#     n = int(input("Enter a number: "))
#     print(countDigits(n))