def isArmstrong(num):
    original = num

    count = 0
    temp = num

    while temp > 0:
        count += 1
        temp //= 10

    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** count)
        temp //= 10

    return total == original

# if __name__ == '__main__':
#     num = int(input("Enter a number: "))
#     if isArmstrong(num):
#         print("YES")
#     else:
#         print("NO")