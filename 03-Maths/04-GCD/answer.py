def gcd(x: int, y: int) -> int:
    while y != 0:
        remainder = x % y
        x = y
        y = remainder

    return x

if __name__ == "__main__":
    x_input = int(input())
    y_input = int(input())
    print(gcd(x_input, y_input))
