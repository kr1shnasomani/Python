def gcd(x: int, y: int) -> int:
    while y != 0:
        remainder = x % y
        x = y
        y = remainder

    return x

# if __name__ == "__main__":
#     x = int(input())
#     y = int(input())
#     print(gcd(x, y))
