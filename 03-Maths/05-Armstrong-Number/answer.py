def isArmstrong(num):
    original = num
    count = len(str(num))

    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** count)
        num //= 10

    return total == original

if __name__ == '__main__':
    num_input = int(input("Enter a number: "))
    if isArmstrong(num_input):
        print("YES")
    else:
        print("NO")
